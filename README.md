# APMMS 2026 Tokyo Conference Hub

這是 APMMS 2026 Tokyo 會議整理的 GitHub Pages 靜態網站版本。

## 本機預覽

```bash
python3 -m http.server 8000
```

然後開啟：

```text
http://localhost:8000/
```

## 主要頁面

- `index.html`：首頁
- `agenda.html`：官方 Agenda
- `speakers.html`：講者入口
- `sessions/`：Session 頁
- `speakers/`：講者內容頁
- `insights.html`：全會議洞察
- `learning-guide.html`：內部教育訓練導讀
- `search.html`：本機前端搜尋
- `print.html`：列印 / 儲存 PDF 友善頁

## GitHub Pages 上線方式

目前這個資料夾只是在本機準備好，尚未上傳。

上傳後有兩種方式：

### 方式 A：Deploy from branch

1. 建立 GitHub repository。
2. 將本資料夾內容推到 `main` branch。
3. GitHub repository → Settings → Pages。
4. Source 選 `Deploy from a branch`。
5. Branch 選 `main`，Folder 選 `/ (root)`。
6. 儲存後等待 GitHub Pages 產生網址。

### 方式 B：GitHub Actions

此版本未附 GitHub Actions workflow，原因是目前 GitHub 認證 token 沒有 `workflow` scope；為避免推送失敗，建議使用方式 A：Deploy from branch。

## 注意事項

- `.nojekyll` 已加入，避免 GitHub Pages 使用 Jekyll 處理靜態檔案。
- 本版本沒有任何後端，不需要 Node / React / build step。
- 若內容不適合公開，請建立 private repository，並確認 GitHub Pages 的可見性設定是否符合你的 GitHub 方案與權限需求。
- 本資料夾不含 `_backups`。

Prepared locally: 20260603_1625
