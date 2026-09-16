# ROBOT LAB 教學網站

phone_blocky 教學網站試作，獨立於韌體 repo。首頁與 S0-E04 示範課已完成，其餘課程為規劃。

## 本機預覽

```powershell
python -m pip install -r requirements.txt
python build.py
python -m http.server 8765 --bind 127.0.0.1 --directory site
```

開啟 http://127.0.0.1:8765 。修改 content/connect.md 後重新 build。

## GitHub Pages

將本 repo 推送至你選定的 GitHub repository，在該 repository 的 Settings → Pages 選擇 GitHub Actions 作為來源。內附工作流程會建立並部署 site/。尚未建立遠端 repo 或發布。

## 教材來源

C:/project/ROBOT/phone_blocky/docs/course/README.md
C:/project/ROBOT/phone_blocky/docs/course/scripts/S0-E04-手機連上它.md
C:/project/ROBOT/phone_blocky/docs/卡住了怎麼辦.md
C:/project/ROBOT/phone_blocky/README.md

本網站無外部字型或 JavaScript 依賴；列印按鈕可保存課程為 PDF。勾選狀態不持久化。未實際連線或驅動硬體。
