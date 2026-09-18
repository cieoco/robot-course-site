from pathlib import Path
import shutil
import markdown

ROOT = Path(__file__).resolve().parent
OUT = ROOT / 'site'
ASSETS = ROOT / 'assets'
OUT.mkdir(exist_ok=True)
if ASSETS.is_dir():
    shutil.copytree(ASSETS, OUT / 'assets', dirs_exist_ok=True)

css = (ROOT / 'style.css').read_text(encoding='utf-8')
css += (ROOT / 'lesson-diagrams.css').read_text(encoding='utf-8')
css += '''
.download{display:block;background:#294e40;color:#fff;text-decoration:none;padding:18px 22px;border-radius:10px;font-weight:700;margin:18px 0}.download:hover{background:#41674f}.download span{display:block;font-size:13px;font-weight:400;opacity:.85}.lesson-shot{margin:25px 0 30px}.lesson-shot img{display:block;width:100%;border:1px solid #d5dbd1;border-radius:10px}.lesson-shot figcaption{margin-top:8px;color:#617268;font-size:13px}.phone-shot{max-width:430px;margin-left:auto;margin-right:auto}.phone-shot figcaption{max-width:430px;margin-left:auto;margin-right:auto}.course-stage{padding:35px 0 8px;border-top:1px solid #d5dbd1}.course-stage:first-of-type{border-top:0}.stage-head{display:flex;align-items:baseline;gap:14px;margin-bottom:16px}.stage-head h2{margin:0;font-size:25px}.stage-head span{font-size:13px;color:#617268}.feature-grid{display:grid;grid-template-columns:repeat(2,1fr);gap:18px}.feature-card{padding:24px 26px;border:1px solid #d7ded2;border-radius:12px;text-decoration:none;background:#fcfcf7}.feature-card:hover{border-color:#294e40}.feature-card.primary{background:#eaf0e2;border-color:#98ac8e}.feature-card h3{margin:7px 0;font-size:21px}.feature-card p{margin:0;color:#657360;font-size:14px}.feature-card small{display:block;margin-top:13px;color:#677661;font-size:12px}.feature-card .badge{display:inline-block}.controller-preview{max-width:640px;margin:22px auto 0}.controller-preview img{width:100%;display:block;border-radius:12px;border:1px solid #d5dbd1}@media(max-width:760px){.feature-grid{grid-template-columns:1fr}.stage-head{display:block}.stage-head span{display:block;margin-top:4px}}
'''

def shell(title, body):
    return f'''<!doctype html><html lang="zh-Hant"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="description" content="phone_blocky 電控入門：從手機連線到積木控制，一步一步學會。"><title>{title} · ROBOT LAB</title><style>{css}</style></head><body><a class="skip" href="#main">跳至內容</a><header><a class="brand" href="index.html"><span class="brand-icon">R</span> ROBOT LAB <small>實作教室</small></a><nav aria-label="主要導覽"><a href="index.html#courses">課程地圖</a><a href="install.html">開始學習 ↗</a></nav></header>{body}<footer><span>ROBOT LAB / phone_blocky</span><span>教學網站試作 · 教材整理於 2026.09.18</span></footer></body></html>'''

def md(name):
    return markdown.markdown((ROOT / 'content' / name).read_text(encoding='utf-8'), extensions=['tables', 'fenced_code'])

def lesson_page(title, eyebrow, lead, minutes, tasks, content_name, next_href, next_label):
    side = ''.join(f'<p>{i:02d} {task}</p>' for i, task in enumerate(tasks, 1))
    body = f'''<main id="main" class="lesson"><a class="back" href="index.html#courses">← 回到課程地圖</a><div class="lesson-head"><p class="eyebrow">{eyebrow}</p><h1>{title}</h1><p class="lead">{lead}</p><div class="lesson-meta"><span>約 {minutes} 分鐘</span><span>手機與已燒錄的控制板</span><button onclick="window.print()">列印／存成 PDF ↓</button></div></div><div class="lesson-grid"><aside class="lesson-side"><strong>本課任務</strong>{side}<hr><small>不確定下一步時，先停止動作並回到前一項確認。</small></aside><article>{md(content_name)}<a class="button" href="{next_href}">{next_label} ↗</a></article></div></main>'''
    return shell(title, body)

home = '''<main id="main"><section class="hero"><div><p class="eyebrow">PHONE_BLOCKY / 從零開始的電控實驗</p><h1>用對入口，<br><em>一步一步讓機構動起來。</em></h1><p class="lead">每一頁都對應控制器的一項實際功能。先準備硬體，再測試、操作，最後才寫程式與調參。</p><a class="button" href="install.html">從燒錄開始 <span>↓</span></a><p class="caption">適合電控初學者 · 每一課都有成功訊號與卡住時的處理方式</p></div><div class="diagram" role="img" aria-label="手機經 Wi-Fi 連到 ESP32 控制板，再控制馬達"><div class="diagram-top">PHONE_BLOCKY LEARNING PATH <span>●</span></div><div class="phone">▥<small>你的手機</small></div><div class="signal">))) <span>Wi-Fi</span></div><div class="board"><span>ESP32</span><div class="chip">phone<br>blocky</div><small>CONTROL BOARD</small></div><div class="motor">M<small>馬達與機構</small></div><div class="diagram-foot">準備　→　自檢　→　控制　→　程式</div></div></section><section class="intro"><p class="eyebrow">CONTROLLER MAP</p><h2>依功能選課，不需要猜從哪一頁開始。</h2><p>照綠色的主路徑完成一次，便能確認硬體、用手機控制馬達，並開始寫第一支積木程式。</p><figure class="controller-preview"><img src="assets/controller-home.png" alt="phone_blocky 控制器主選單，包含 Blockly、AI、搖桿、硬體檢測、設定與接線說明。"><figcaption>控制器主選單的六個功能，已在下方各自對應成教學。</figcaption></figure></section><section id="courses"><div class="course-stage"><div class="stage-head"><h2>01　先準備好</h2><span>燒錄、接線、連線與自檢；第一次操作請依序完成</span></div><div class="feature-grid"><a class="feature-card primary" href="install.html"><span class="badge">必做</span><h3>下載並燒錄工具</h3><p>用整合工具把韌體與手機網頁燒進 ESP32，並讀出 AP 名稱與 MAC。</p><small>約 10 分鐘 · Windows 電腦</small></a><a class="feature-card primary" href="wiring.html"><span class="badge">必做</span><h3>接線說明</h3><p>核對馬達、舵機、編碼器與共地；接線完成後才接上外部電源。</p><small>約 8 分鐘 · 接線時查詢</small></a><a class="feature-card primary" href="connect.html"><span class="badge">必做</span><h3>手機連上它</h3><p>用 AP 名稱辨識自己的控制板，打開控制器主選單。</p><small>約 5 分鐘 · 手機</small></a><a class="feature-card primary" href="hardware.html"><span class="badge">必做</span><h3>硬體功能檢測</h3><p>只勾選已接元件，逐項確認馬達、舵機與感測器。</p><small>約 10 分鐘 · 自檢完成再前進</small></a></div></div><div class="course-stage"><div class="stage-head"><h2>02　直接控制機構</h2><span>先確認手指指令能變成正轉、停止與反轉</span></div><div class="feature-grid"><a class="feature-card primary" href="remote.html"><span class="badge">主路徑</span><h3>虛擬搖桿控制</h3><p>找到緊急停止，用滑桿控制 M3／M4 與舵機，觀察角度讀值。</p><small>約 10 分鐘 · 即時操作</small></a><a class="feature-card primary" href="motor.html"><span class="badge">主路徑</span><h3>Blockly 積木程式</h3><p>使用 setup、馬達、延遲與停止積木，完成第一個安全動作。</p><small>約 15 分鐘 · 第一支程式</small></a></div></div><div class="course-stage"><div class="stage-head"><h2>03　進階功能</h2><span>完成主路徑後再使用，避免不必要的設定與誤動作</span></div><div class="feature-grid"><a class="feature-card" href="settings.html"><span class="badge muted">進階</span><h3>相關設定與調參</h3><p>修改 AP 名稱、加入教室 Wi-Fi；理解 RAM 測試與 NVS 保存的差別。</p><small>按需要使用 · 會影響下次開機</small></a><a class="feature-card" href="ai.html"><span class="badge muted">選用</span><h3>AI 生成程式</h3><p>把自然語言轉成可驗證的 PROG JSON；先檢查，再執行或存檔。</p><small>需 AI relay 與 Azure 設定</small></a></div></div></section><aside class="note"><strong>操作順序：接線後先自檢，再用搖桿，最後才用積木或 AI。</strong><p>出現非預期動作時，先按控制器的緊急停止，讓馬達回到停止狀態，再依當前課程的「卡住時」逐項檢查。</p></aside></main>'''

pages = {
    'index.html': shell('phone_blocky 教學地圖', home),
    'install.html': lesson_page('燒錄：一輩子只做一次', '01 準備 / E02', '下載整合工具，完成控制板的韌體與手機網頁準備。', '10', ['下載工具', '接上控制板', '完成燒錄', '記下 AP 名稱'], 'install.md', 'wiring.html', '下一課：接線說明'),
    'wiring.html': lesson_page('接線說明：先核對再通電', '01 準備 / E03', '用控制板內建接線圖確認通道、電源與共地。', '8', ['開啟接線頁', '核對通道', '確認共地', '準備自檢'], 'wiring.md', 'connect.html', '下一課：手機連上它'),
    'connect.html': lesson_page('手機連上它', '01 準備 / E04', '把手機與控制板連在一起，打開你的電控實驗入口。', '5', ['連上 Wi-Fi', '保持連線', '開啟主選單', '辨識功能'], 'connect.md', 'hardware.html', '下一課：硬體功能檢測'),
    'hardware.html': lesson_page('硬體功能檢測：逐項綠燈', '01 準備 / E05', '先驗證硬體與接線，讓後面的程式除錯有明確起點。', '10', ['確認連線', '勾選已接元件', '觀察動作', '記錄問題'], 'hardware.md', 'remote.html', '下一課：虛擬搖桿控制'),
    'remote.html': lesson_page('第一次指揮它', '02 控制 / E06', '用手機遙控頁，直接控制 M3、M4 與舵機。', '10', ['找緊急停止', '控制 M3', '試角度模式', '看讀值'], 'remote.md', 'motor.html', '下一課：Blockly 積木程式'),
    'motor.html': lesson_page('積木程式：讓馬達開始轉', '02 控制 / E10–E13', '從 Blockly 控制器的第一個 PWM 指令，理解出力、方向與馬達個體差異。', '15', ['組出動作', '比較 PWM', '驗證方向', '觀察差異'], 'motor.md', 'settings.html', '下一步：相關設定與調參'),
    'settings.html': lesson_page('相關設定：名稱、Wi-Fi 與調參', '03 進階 / 設定', '先處理日常的 AP 名稱與 Wi-Fi；PID 與硬體參數留給需要調參時。', '8', ['選擇設定', '辨識 AP', '了解 Wi-Fi', '區分 RAM 與 NVS'], 'settings.md', 'ai.html', '選用：AI 生成程式'),
    'ai.html': lesson_page('AI 生成程式：先驗證再執行', '03 進階 / AI', '把動作描述轉成 JSON；安全與結果仍由你在實機上確認。', '10', ['選擇模式', '描述動作', '驗證 JSON', '安全執行'], 'ai.md', 'index.html#courses', '返回教學地圖'),
}
for name, page in pages.items():
    (OUT / name).write_text(page, encoding='utf-8')
(OUT / '.nojekyll').write_text('', encoding='utf-8')
print('Built: ' + str(OUT))
