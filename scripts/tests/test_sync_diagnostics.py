from pathlib import Path
import subprocess
import tempfile
import unittest


SCRIPT = Path(__file__).resolve().parents[1] / 'diagnose-upstream.sh'


def git(root, *args):
    return subprocess.check_output(['git', '-C', str(root), *args], text=True, stderr=subprocess.PIPE).strip()


class SyncDiagnosticsTests(unittest.TestCase):
    def inspect_merge(self, conflict):
        with tempfile.TemporaryDirectory(prefix='krc sync ') as temp:
            root = Path(temp)
            upstream = root / 'upstream'
            fork = root / 'fork'
            upstream.mkdir()
            git(upstream, 'init', '-b', 'main')
            git(upstream, 'config', 'user.name', 'Sync fixture')
            git(upstream, 'config', 'user.email', 'fixture@example.invalid')
            (upstream / 'README.md').write_text('base\n')
            git(upstream, 'add', 'README.md')
            git(upstream, 'commit', '-m', 'base')
            subprocess.run(['git', 'clone', '--quiet', str(upstream), str(fork)], check=True)
            git(fork, 'config', 'user.name', 'Sync fixture')
            git(fork, 'config', 'user.email', 'fixture@example.invalid')
            (fork / 'README.md' if conflict else fork / 'fork.txt').write_text('fork change\n')
            git(fork, 'add', '.')
            git(fork, 'commit', '-m', 'fork change')
            before = git(fork, 'rev-parse', 'HEAD')
            (upstream / 'README.md').write_text('upstream change\n')
            git(upstream, 'add', 'README.md')
            git(upstream, 'commit', '-m', 'upstream change')
            upstream_before = git(upstream, 'rev-parse', 'HEAD')
            output = root / 'diagnostics'
            result = subprocess.run(['bash', str(SCRIPT), str(fork), before, str(upstream), str(output)], capture_output=True, text=True)
            self.assertEqual(git(fork, 'rev-parse', 'HEAD'), before)
            self.assertEqual(git(upstream, 'rev-parse', 'HEAD'), upstream_before)
            return result, (output / 'merge-result.txt').read_text()

    def test_conflict_names_file_and_leaves_both_branches_intact(self):
        result, report = self.inspect_merge(True)
        self.assertEqual(result.returncode, 1)
        self.assertIn('CONFLICT (content): Merge conflict in README.md', report)

    def test_clean_merge_is_reported_without_pushing_it(self):
        result, report = self.inspect_merge(False)
        self.assertEqual(result.returncode, 0)
        self.assertNotIn('CONFLICT', report)
