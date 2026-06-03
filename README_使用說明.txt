APMMS_website 使用說明

建議先開啟：
/Users/kobeyang/Desktop/20260513暫存/2026APMMS東京/2026 APMMS會議整理/APMMS_website/index.html

這是方案 A：純 HTML + CSS + JavaScript 的本機靜態網站版。

已建立頁面：
1. index.html：首頁與會議總覽
2. agenda.html：官方 Agenda 圖與 Session / Speaker 架構
3. sessions/session-1.html、session-2.html、session-3.html：各 Session 頁
4. speakers/*.html：10 位講者 / Topic 頁
5. insights.html：全會議核心結論
6. search.html：本機前端搜尋
7. print.html：列印 / 儲存 PDF 友善版

使用方式：
- 直接用瀏覽器打開 index.html。
- 若 search.html 因瀏覽器 file:// 安全限制無法讀取 JSON，可在此資料夾用本機伺服器開啟：
  python3 -m http.server 8000
  然後開 http://localhost:8000/
- 不需要上傳外部網站即可本機閱讀。
- 若要分享給別人，可將整個 APMMS_website 資料夾壓縮後給對方。

注意：
- 本版未刪除、未覆蓋任何既有 APMMS 檔案。
- 本版未上傳到外部網站。
- 官方圖檔僅複製到 assets/images/official 供本機網站使用。


第二版更新：
- 首頁改為更接近 APMMS / EYES HAVE DREAMS 風格的紫藍視覺封面。
- 新增 speakers.html：講者視覺入口，並嵌入官方 Speakers.jpg。
- 新增 learning-guide.html：內部教育訓練導讀頁，但不把會議紀錄直接改寫成 SOP。
- Session 頁與 Speaker 頁新增側邊導覽與回到頂端按鈕。
- 搜尋索引新增講者入口與內部導讀頁。

第二版完成時間：由 Hermes Agent 產生。


試做更豐富首頁版本：
- 已在修改前備份首頁與 CSS 到 _backups/homepage_before_richer_mockup/。
- 新增裝置框視覺、MYOPIA 背景字樣、Session 色塊與 Featured Insights。
- 若不喜歡，可請 Hermes 回到 homepage_before_richer_mockup，或執行該備份資料夾內的 RESTORE_homepage_previous_version.py。
