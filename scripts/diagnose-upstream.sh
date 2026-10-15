#!/usr/bin/env bash
set -euo pipefail

fork_url=$1
base_sha=$2
upstream_url=$3
output=$4
mkdir -p "$output"
checkout="$output/repository.git"

# Inspect the merge without checking out assets or changing either remote branch.
git clone --bare --single-branch --branch main --filter=blob:none -- "$fork_url" "$checkout" > "$output/fetch.txt" 2>&1
git -C "$checkout" fetch --no-tags --filter=blob:none "$upstream_url" main >> "$output/fetch.txt" 2>&1
status=0
git -C "$checkout" merge-tree --write-tree "$base_sha" FETCH_HEAD > "$output/merge-result.txt" 2>&1 || status=$?
cat "$output/merge-result.txt"
exit "$status"
