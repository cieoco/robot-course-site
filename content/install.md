## 這個工具是做什麼的？

**PhoneBlockyMotorTuner** 是給 Windows 使用的整合工具。它已經帶著 phone_blocky 韌體與網頁檔，第一次準備控制板時，不必安裝 Python、PlatformIO 或另外尋找燒錄程式。

它可以燒錄韌體、檢查接線、測試馬達，並在之後協助調整有編碼器的 M3、M4。

## 01　下載工具

請在 Windows 電腦下載並儲存這個檔案：

<a class="download" href="https://github.com/cieoco/robot-course-site/releases/download/v2026.07.27/PhoneBlockyMotorTuner.exe">下載 PhoneBlockyMotorTuner.exe <span>71.5 MB · Windows</span></a>

檔案下載完成後，建議先確認檔名仍是 `PhoneBlockyMotorTuner.exe`，再雙擊開啟。

> Windows 可能顯示未知發行者或 SmartScreen 提示，因為此工具目前尚未進行程式碼簽章。請只從本頁的 GitHub 下載連結取得檔案；若檔名或下載來源不同，請停止執行並向老師確認。

## 02　接上控制板

將 AFMotor Shield 插在 WeMos D1 R32（ESP32）上，再用 USB 線接到 Windows 電腦。電腦通常會出現一個新的 COM 埠。

**開始前先注意：** ESP32 的 USB 電源用於燒錄與通訊；馬達實際轉動時仍需要驅動板的外接電源。

## 03　開啟工具並燒錄

1. 開啟 `PhoneBlockyMotorTuner.exe`。
2. 切換到最右側的「**燒錄**」分頁。
3. 若上方已經連上 USB，先按「**斷線**」，讓燒錄程式能使用 COM 埠。
4. 在視窗最上方選擇「**USB（序列）**」與正確的 COM 埠；不確定時按上方的「**重新整理**」。燒錄分頁會直接使用這個選擇。

<figure class="lesson-shot"><img src="assets/flash-com-port.png" alt="PhoneBlockyMotorTuner 的燒錄分頁，上方 USB 序列連線列選擇 COM4；燒錄設定提示會使用上方選擇的 COM 埠。"><figcaption>先在最上方選擇 USB（序列）與正確 COM 埠；燒錄設定不需要再選一次。</figcaption></figure>
5. 保持四個燒錄檔都啟用，然後按「**開始燒錄**」。首次燒錄不要取消 `littlefs.bin`，它包含手機操作網頁。
6. 看見「**燒錄完成，請重新啟動 ESP32**」後，重新插拔 USB 或按控制板的 RST。

一般情況維持預設 Baud `921600`；若中途失敗，改成 `460800` 或 `115200` 再試。

## 成功訊號

- 工具可以看見並選到控制板的 COM 埠。
- 燒錄紀錄顯示完成，沒有錯誤訊息。
- 重啟後，手機 Wi-Fi 清單出現 `ESP32-` 開頭的熱點。

完成後，繼續閱讀「手機連上它」，用手機開啟控制板的主選單。

## 常見卡點

| 現象 | 先做什麼 |
| --- | --- |
| 工具找不到 COM 埠 | 換一條可傳資料的 USB 線；確認控制板供電；安裝對應的 CH340 或 CP2102 USB 驅動。 |
| 開始燒錄後立刻失敗 | 先在工具上方按「斷線」釋放 COM 埠，再確認上方 USB 連線列選的是正確埠。 |
| 燒錄會中斷 | 將 Baud 降到 `460800` 或 `115200`，避免鬆動的 USB 線。 |
| 有 ESP32 熱點，但網頁空白或 404 | 重新燒錄時確認四個檔案都啟用，特別是 `littlefs.bin`。 |

## 下載檔案校驗

版本：2026.07.27  
SHA-256：`8111FAE94FC40F766816B9243510D895DEF273F52C98BD0AF1E030066B8C4542`

這個校驗碼可用來確認下載檔與本課程使用的版本相同。
