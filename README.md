## 此 Fork 的自動建構

[![Build](https://github.com/win10ogod/Kamen_Rider_Craft/actions/workflows/build.yml/badge.svg)](https://github.com/win10ogod/Kamen_Rider_Craft/actions/workflows/build.yml)

此 Fork 以 [kelcok22/Kamen_Rider_Craft](https://github.com/kelcok22/Kamen_Rider_Craft) 為上游，使用 Java 21 與專案附帶的 Gradle Wrapper 建構 Minecraft 1.21.1 模組。

推送、Pull Request 或 Actions 頁面的 **Run workflow** 都會執行完整 `build`。成功後，在該次執行的 **Artifacts** 下載 `kamenridercraft-mc1.21.1-*`，解壓即可取得 JAR、SHA-256 校驗碼與版本／提交資訊；產物保留 30 天。

**[Sync upstream](https://github.com/win10ogod/Kamen_Rider_Craft/actions/workflows/sync-upstream.yml)** 每 6 小時檢查作者的 `main`，有更新就合併到此 Fork，接著自動建構該次合併後的提交。成功後直接在該次同步執行的 **Artifacts** 下載 JAR。排程沒有新提交時會略過建構；想立即同步並建構，可在 **Sync upstream → Run workflow** 手動執行。

同步使用 GitHub 內建權杖，不需另設個人 Token。合併會保留此 Fork 的修改；發生衝突時工作流會失敗並顯示原因，需處理衝突後重跑。排程時間可能受 GitHub 排隊延遲；公開儲存庫連續 60 天沒有活動時，GitHub 會停用排程，屆時可到 Actions 重新啟用。

建構產物代表該次提交的開發狀態，不等同作者正式發行版本；前置模組版本請以 `gradle.properties` 和 JAR 內的模組資訊為準。

---

![KELCO BUCKET RELEASE](https://cdn.discordapp.com/icons/355766960207691778/abf749648d4566b2a343948ae3a504a6.webp)
=======
This is the official Github page of Kamen Rider Craft.


Since 1971, The Kamen Rider Series has captivated people across the world with its stories, characters, and its 'tokusatsu' production techniques. Now, with over 50 years of Japanese cultural icons arrives in Minecraft!


Kamen Rider Craft began as a small project I stated in late 2012, and has since evolved into a massive mod with hundreds of items, weapons, and forms with multiple developers on board. Back at the start of 2023 I decided to start to recode this mod from scratch. With the goal to make the mod a lot more friendly to work on, now over a year later there is still a lot of work to do, but I want to share it.
