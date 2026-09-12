## 此 Fork 的自動建構

[![Build](https://github.com/win10ogod/Kamen_Rider_Craft/actions/workflows/build.yml/badge.svg)](https://github.com/win10ogod/Kamen_Rider_Craft/actions/workflows/build.yml)

此 Fork 以 [kelcok22/Kamen_Rider_Craft](https://github.com/kelcok22/Kamen_Rider_Craft) 為上游，使用 Java 21 與專案附帶的 Gradle Wrapper 建構 Minecraft 1.21.1 模組。

推送、Pull Request 或 Actions 頁面的 **Run workflow** 都會執行完整 `build`。成功後，在該次執行的 **Artifacts** 下載 `kamenridercraft-mc1.21.1-*`，解壓即可取得 JAR、SHA-256 校驗碼與版本／提交資訊；產物保留 30 天。

若要編譯作者的新提交，先同步上游到此 Fork，再執行工作流。建構產物代表該次提交的開發狀態，不等同作者正式發行版本；前置模組版本請以 `gradle.properties` 和 JAR 內的模組資訊為準。

---

![KELCO BUCKET RELEASE](https://cdn.discordapp.com/icons/355766960207691778/abf749648d4566b2a343948ae3a504a6.webp)
=======
This is the official Github page of Kamen Rider Craft.


Since 1971, The Kamen Rider Series has captivated people across the world with its stories, characters, and its 'tokusatsu' production techniques. Now, with over 50 years of Japanese cultural icons arrives in Minecraft!


Kamen Rider Craft began as a small project I stated in late 2012, and has since evolved into a massive mod with hundreds of items, weapons, and forms with multiple developers on board. Back at the start of 2023 I decided to start to recode this mod from scratch. With the goal to make the mod a lot more friendly to work on, now over a year later there is still a lot of work to do, but I want to share it.