# Lesson Quiz — Question Bank

每個 lesson 預置 8 道題。每題都包含：

- `category`
- `question`
- `options`
- `correct`
- `explanation`
- `review`

---

## Lesson 01: Slash Commands

### Q1
- **Category**: conceptual
- **Question**: slash commands 在 Claude Code 中最適合做什麼？
- **Options**: A) 存長期專案規則 | B) 顯式觸發某個快捷操作或工作流 | C) 替代所有 hooks | D) 替代所有 skills
- **Correct**: B
- **Explanation**: slash commands 更適合使用者主動輸入並顯式觸發某個動作，例如 `/optimize`、`/pr`。
- **Review**: 什麼是 slash commands

### Q2
- **Category**: practical
- **Question**: 安裝單個範例命令 `/optimize` 的正確方式是什麼？
- **Options**: A) `cp 01-slash-commands/optimize.md .claude/commands/` | B) `cp 01-slash-commands/optimize.md .claude/skills/` | C) `mv optimize.md ~/.claude/` | D) `claude install optimize`
- **Correct**: A
- **Explanation**: 當前範例 command 安裝到 `.claude/commands/`，即可透過 `/optimize` 使用。
- **Review**: 怎麼安裝

### Q3
- **Category**: conceptual
- **Question**: slash commands 和 skills 的一個核心區別是什麼？
- **Options**: A) 前者自動觸發，後者手動觸發 | B) 前者更適合手動顯式觸發，後者更適合自動複用能力 | C) 二者完全無關 | D) skills 只能用於外掛
- **Correct**: B
- **Explanation**: slash commands 偏使用者主動觸發；skills 偏 Claude 按描述自動呼叫。
- **Review**: slash commands 和 skills 的關係

### Q4
- **Category**: practical
- **Question**: 哪些內容在 command 檔案裡不應該被翻譯？
- **Options**: A) 標題和段落說明 | B) 真實命令名、frontmatter key、程式碼塊命令 | C) 所有內容都不能改 | D) 只有 Markdown 標題
- **Correct**: B
- **Explanation**: `description`、`allowed-tools`、`/optimize`、命令列片段等都屬於高風險標識。
- **Review**: command 檔案裡哪些不能翻

### Q5
- **Category**: conceptual
- **Question**: 為什麼新手適合先學 slash commands？
- **Options**: A) 因為它最複雜 | B) 因為必須先學完 hooks 才能用 | C) 因為安裝簡單、回饋快、回報高 | D) 因為它是唯一能執行的功能
- **Correct**: C
- **Explanation**: slash commands 是最快能獲得收益的一類能力，能幫助新手建立信心。
- **Review**: Slash Commands 指南開頭

### Q6
- **Category**: practical
- **Question**: 如果 command 檔案放對了但不生效，首先應該檢查什麼？
- **Options**: A) GPU 驅動 | B) 路徑、副檔名和 frontmatter 格式 | C) 資料庫連線 | D) 瀏覽器快取
- **Correct**: B
- **Explanation**: 最常見問題就是檔案不在 `.claude/commands/`、不是 `.md` 或 frontmatter 格式損壞。
- **Review**: 常見坑

### Q7
- **Category**: conceptual
- **Question**: 什麼時候應該把 command 升級成 skill？
- **Options**: A) 任何時候都不該升級 | B) 當它變成長期複用工作流，並需要範本、腳本或自動觸發時 | C) 只有程式碼超過 500 行時 | D) 只有在 Windows 下
- **Correct**: B
- **Explanation**: 當一個 command 變得需要長期複用、附帶資源或自動觸發時，更適合轉為 skill。
- **Review**: 什麼時候該升級成 skill

### Q8
- **Category**: practical
- **Question**: `/pr` 這個範例 command 的重點是什麼？
- **Options**: A) 管理 MCP | B) 準備 PR 前的檢查、測試和摘要整理 | C) 部署到生產環境 | D) 設定 CLAUDE.md
- **Correct**: B
- **Explanation**: `/pr` 用於在發 PR 前整理改動、跑測試、生成摘要。
- **Review**: 本目錄裡的範例命令

---

## Lesson 02: Memory

### Q1
- **Category**: conceptual
- **Question**: memory 和當前會話上下文的核心區別是什麼？
- **Options**: A) memory 只在本次會話有效 | B) memory 是長期規則層，會跨會話影響 Claude 的預設上下文 | C) 二者沒有區別 | D) memory 只給人看，不影響 Claude
- **Correct**: B
- **Explanation**: `CLAUDE.md` 體系提供的是長期上下文，不是當前對話中的一次性說明。
- **Review**: memory 是什麼

### Q2
- **Category**: practical
- **Question**: 最快安裝專案級 memory 的方式是什麼？
- **Options**: A) `cp 02-memory/project-CLAUDE.md ./CLAUDE.md` | B) `touch memory.md` | C) `claude --memory init` | D) `mv project-CLAUDE.md docs/`
- **Correct**: A
- **Explanation**: 直接複製專案範本到根目錄的 `CLAUDE.md` 是最快方式。
- **Review**: 最快上手方式

### Q3
- **Category**: conceptual
- **Question**: 哪類資訊最適合寫進 memory？
- **Options**: A) 高頻且長期穩定的專案規則 | B) 臨時一次性任務說明 | C) 實時資料庫資料 | D) 聊天記錄全文
- **Correct**: A
- **Explanation**: memory 應該存長期穩定、高價值、跨會話都適用的規則。
- **Review**: 寫什麼最有價值

### Q4
- **Category**: practical
- **Question**: 個人偏好通常更適合放在哪個檔案？
- **Options**: A) `~/.claude/CLAUDE.md` | B) `README.md` | C) `package.json` | D) `.mcp.json`
- **Correct**: A
- **Explanation**: 個人級 memory 通常放在 `~/.claude/CLAUDE.md`。
- **Review**: 個人級 memory

### Q5
- **Category**: conceptual
- **Question**: 為什麼不建議把一次性任務說明塞進 `CLAUDE.md`？
- **Options**: A) 因為 Claude 看不懂 | B) 因為這會汙染長期規則層，讓 memory 失去聚焦 | C) 因為檔案會變只讀 | D) 因為 Git 不支援
- **Correct**: B
- **Explanation**: 一次性任務更適合放在當前對話或單獨檔案，而不是長期自動載入的 memory。
- **Review**: 哪些內容不適合寫進 memory

### Q6
- **Category**: practical
- **Question**: 對話中快速寫入一條 memory 的常見方式是什麼？
- **Options**: A) `/remember now` | B) 以 `#` 開頭寫一條規則 | C) `@memory` | D) `/save-context`
- **Correct**: B
- **Explanation**: `# your rule` 這種形式是常見的快速寫入方式。
- **Review**: 高價值命令

### Q7
- **Category**: conceptual
- **Question**: 專案級 memory 和個人級 memory 的一個重要區別是什麼？
- **Options**: A) 前者更適合團隊共享，後者更適合個人偏好 | B) 前者不能被 Claude 讀取 | C) 後者必須提交到 Git | D) 二者路徑完全相同
- **Correct**: A
- **Explanation**: 專案級適合團隊規範，個人級適合個人風格與習慣。
- **Review**: 常見 memory 型別

### Q8
- **Category**: practical
- **Question**: 如果你在 Windows 上工作，memory 裡特別值得補充什麼？
- **Options**: A) 股票價格 | B) 路徑規則、shell 差異和環境要求 | C) 天氣預報 | D) 表情包
- **Correct**: B
- **Explanation**: 對新手使用者和 Windows 使用者來說，路徑與 shell 差異是高頻踩坑點。
- **Review**: 新手使用者特別注意

---

## Lesson 03: Skills

### Q1
- **Category**: conceptual
- **Question**: skills 最核心的價值是什麼？
- **Options**: A) 替代所有命令列 | B) 讓穩定工作流可以被 Claude 複用和自動觸發 | C) 只用於圖片生成 | D) 只用於外掛市場
- **Correct**: B
- **Explanation**: skills 的意義在於把流程、範本和實踐沉澱為可複用能力。
- **Review**: skills 是什麼

### Q2
- **Category**: practical
- **Question**: 一個 skill 的核心檔名是什麼？
- **Options**: A) `README.md` | B) `SKILL.md` | C) `RULES.md` | D) `PROMPT.md`
- **Correct**: B
- **Explanation**: `SKILL.md` 是 skill 的主定義檔案。
- **Review**: 一個 skill 的基本結構

### Q3
- **Category**: conceptual
- **Question**: progressive disclosure 的意義是什麼？
- **Options**: A) 一開始把所有內容全塞進上下文 | B) 按需載入 metadata、instructions 和 resources | C) 讓 skill 只能手動觸發 | D) 讓檔案更短
- **Correct**: B
- **Explanation**: skills 的優勢之一是按需載入，避免上下文被一開始就塞滿。
- **Review**: progressive disclosure 是什麼意思

### Q4
- **Category**: practical
- **Question**: `SKILL.md` 裡哪些欄位最不能被中文化？
- **Options**: A) `name`、`description`、`effort`、`shell` 這些 key | B) 只有標題 | C) 只有第一行 | D) 都可以翻
- **Correct**: A
- **Explanation**: 這些 frontmatter key 會被系統解析，必須保真。
- **Review**: `SKILL.md` 裡哪些不能翻

### Q5
- **Category**: conceptual
- **Question**: skills 和 slash commands 的一個重要區別是什麼？
- **Options**: A) skills 更偏自動複用，slash commands 更偏手動顯式觸發 | B) slash commands 可以自動觸發，skills 不行 | C) 二者完全相同 | D) skills 不能附帶腳本
- **Correct**: A
- **Explanation**: skills 適合長期複用和自動呼叫；slash commands 更適合手動入口。
- **Review**: skills 和 slash commands 的區別

### Q6
- **Category**: practical
- **Question**: 將 `code-review` 安裝到個人 skills 目錄的正確方式是什麼？
- **Options**: A) `cp -r 03-skills/code-review ~/.claude/skills/` | B) `mv code-review ~/.claude/` | C) `claude install skill code-review` | D) `cp SKILL.md CLAUDE.md`
- **Correct**: A
- **Explanation**: 個人級 skill 安裝到 `~/.claude/skills/`。
- **Review**: 如何安裝

### Q7
- **Category**: conceptual
- **Question**: skills 什麼時候最值得使用？
- **Options**: A) 當某個流程經常重複出現，而且希望 Claude 在合適場景自動幫你做 | B) 只在第一次使用 Claude 時 | C) 只在設計 logo 時 | D) 只在沒有程式碼時
- **Correct**: A
- **Explanation**: 高頻、穩定、可複用的工作流最適合 skill 化。
- **Review**: skills 為什麼重要

### Q8
- **Category**: practical
- **Question**: 如果 script 依賴 `python` 或 `node`，在 skill 檔案裡最好補什麼？
- **Options**: A) 股票程式碼 | B) shell / 環境變數 / 執行依賴說明 | C) 作者郵箱 | D) 社交媒體連結
- **Correct**: B
- **Explanation**: 這能顯著減少新手使用者和 Windows 使用者的實際踩坑。
- **Review**: 新手使用者特別注意

---

## Lesson 04: Subagents

### Q1
- **Category**: conceptual
- **Question**: subagents 最適合解決什麼問題？
- **Options**: A) 複雜任務拆分與專業分工 | B) 替代 Git | C) 存長期規則 | D) 生成 favicon
- **Correct**: A
- **Explanation**: subagents 的核心優勢是分工、隔離和上下文拆分。
- **Review**: subagents 是什麼

### Q2
- **Category**: practical
- **Question**: 專案級 subagents 通常放在哪？
- **Options**: A) `.claude/agents/` | B) `.claude/skills/` | C) `.mcp.json` | D) `docs/agents/`
- **Correct**: A
- **Explanation**: 專案級 agents 目錄是 `.claude/agents/`。
- **Review**: 檔案放哪裡

### Q3
- **Category**: conceptual
- **Question**: subagent 為什麼能減少主對話汙染？
- **Options**: A) 因為它有自己獨立的上下文視窗 | B) 因為它不會讀檔案 | C) 因為它不能返回結果 | D) 因為它只能執行一次
- **Correct**: A
- **Explanation**: subagents 透過獨立上下文隔離細節，避免主會話被複雜內容淹沒。
- **Review**: subagents 的核心價值

### Q4
- **Category**: practical
- **Question**: 以下哪個欄位屬於 subagent frontmatter，且不應翻譯？
- **Options**: A) `tools` | B) `模型` | C) `用途说明` | D) `附加提示词说明`
- **Correct**: A
- **Explanation**: `name`、`description`、`tools`、`model` 等欄位都屬於 frontmatter 協議部分。
- **Review**: frontmatter 裡這些欄位不要翻

### Q5
- **Category**: conceptual
- **Question**: 什麼情況下不建議拆 subagents？
- **Options**: A) 任務很小且耦合很高 | B) 任務複雜且多執行緒 | C) 需要不同角色並行分析 | D) 需要工具隔離
- **Correct**: A
- **Explanation**: 小任務或高度耦合任務強拆 subagents，反而增加複雜度。
- **Review**: 如何決定要不要拆成 subagents

### Q6
- **Category**: practical
- **Question**: `code-reviewer` 這類 subagent 最適合什麼時候使用？
- **Options**: A) 在程式碼改動後做結構化審查 | B) 初始化 npm | C) 改 favicon 顏色 | D) 改 Git 使用者名稱
- **Correct**: A
- **Explanation**: `code-reviewer` 就是典型的審查型 subagent。
- **Review**: 本目錄裡的範例 subagents

### Q7
- **Category**: conceptual
- **Question**: subagent 的工具許可權為什麼重要？
- **Options**: A) 因為不同 agent 需要不同能力邊界和安全範圍 | B) 因為工具越多越好 | C) 因為工具隻影響 UI | D) 因為工具會決定字型大小
- **Correct**: A
- **Explanation**: 工具許可權既影響功能，也影響安全性和任務邊界。
- **Review**: subagents 的核心價值

### Q8
- **Category**: practical
- **Question**: Windows 使用者在使用依賴 shell 的 subagent 時，最該先確認什麼？
- **Options**: A) GPU 型號 | B) 當前到底在 PowerShell、Git Bash 還是 WSL 中執行 | C) 顯示器重新整理率 | D) 本機桌布
- **Correct**: B
- **Explanation**: 路徑、shell 語法和命令相容性都會受執行環境影響。
- **Review**: 新手使用者特別注意

---

## Lesson 05: MCP

### Q1
- **Category**: conceptual
- **Question**: MCP 的核心價值是什麼？
- **Options**: A) 提供長期專案規則 | B) 讓 Claude 接入外部工具和實時資料 | C) 取代 CLI | D) 取代所有 plugins
- **Correct**: B
- **Explanation**: MCP 是 Claude 訪問外部系統和實時資料的標準協議。
- **Review**: MCP 解決什麼問題

### Q2
- **Category**: practical
- **Question**: 試用 GitHub MCP 範例前，最常見需要先準備什麼？
- **Options**: A) `GITHUB_TOKEN` | B) `AWS_SECRET` | C) `JAVA_HOME` | D) `DISPLAY`
- **Correct**: A
- **Explanation**: GitHub MCP 通常首先依賴可用的 `GITHUB_TOKEN`。
- **Review**: 直接複製範例設定

### Q3
- **Category**: conceptual
- **Question**: MCP 和 memory 的一個重要區別是什麼？
- **Options**: A) memory 更適合實時外部資料 | B) MCP 更適合實時外部資料，memory 更適合長期規則 | C) 二者完全一樣 | D) MCP 只能存檔案
- **Correct**: B
- **Explanation**: memory 適合長期穩定規則；MCP 適合實時和外部資料接入。
- **Review**: MCP 解決什麼問題

### Q4
- **Category**: practical
- **Question**: 下面哪個 JSON key 在 MCP 設定裡絕對不能翻譯？
- **Options**: A) `mcpServers` | B) “用途” | C) “說明” | D) “備註”
- **Correct**: A
- **Explanation**: `mcpServers` 屬於協議欄位，翻譯會直接破壞設定。
- **Review**: 哪些內容不能翻

### Q5
- **Category**: conceptual
- **Question**: 為什麼新手使用者在第一次用 MCP 時更容易遇到安裝問題？
- **Options**: A) 因為 MCP 只能在美國用 | B) 因為常依賴 `npx`、外部 API、GitHub 和網路環境 | C) 因為 MCP 需要專用鍵盤 | D) 因為 JSON 不能儲存中文
- **Correct**: B
- **Explanation**: 首次安裝或連通性往往受 npm、代理程式、證書和 GitHub 網路影響。
- **Review**: 新手使用者特別注意

### Q6
- **Category**: practical
- **Question**: 如果想一次掛多個服務，應該參考哪個範例？
- **Options**: A) `multi-mcp.json` | B) `README.md` | C) `favicon-32.svg` | D) `personal-CLAUDE.md`
- **Correct**: A
- **Explanation**: 多服務組合對應 `05-mcp/multi-mcp.json`。
- **Review**: 本目錄裡的範例設定

### Q7
- **Category**: conceptual
- **Question**: 為什麼不建議一上來接很多 MCP 服務？
- **Options**: A) 因為只能接一個 | B) 因為排障和許可權問題會疊加，推薦先跑通最核心的一個 | C) 因為 Git 會壞 | D) 因為 Claude 不支援
- **Correct**: B
- **Explanation**: 推薦先跑通 GitHub 或 filesystem，再逐步擴充套件。
- **Review**: 常見坑

### Q8
- **Category**: practical
- **Question**: Windows 原生環境執行 `npx` MCP server 時，檔案建議優先關注什麼？
- **Options**: A) `cmd /c` 風格與 shell 差異 | B) 滑鼠 DPI | C) 桌布解析度 | D) Git commit message
- **Correct**: A
- **Explanation**: Windows shell 相容性是 MCP 設定中非常常見的差異點。
- **Review**: 新手使用者特別注意

---

## Lesson 06: Hooks

### Q1
- **Category**: conceptual
- **Question**: hooks 最適合把什麼事情自動化？
- **Options**: A) 每次都要手動重複檢查的動作 | B) 所有寫作任務 | C) 只做圖片壓縮 | D) 只管理 GitHub stars
- **Correct**: A
- **Explanation**: hooks 的核心價值是把重複檢查、提醒和攔截變成事件驅動自動化。
- **Review**: hooks 是什麼

### Q2
- **Category**: practical
- **Question**: 一個 hooks 設定裡最外層的關鍵 JSON key 是什麼？
- **Options**: A) `hooks` | B) `memory` | C) `plugins` | D) `agents`
- **Correct**: A
- **Explanation**: hooks 的設定結構從 `hooks` 這個 key 開始。
- **Review**: 基本結構

### Q3
- **Category**: conceptual
- **Question**: `PreToolUse` 和 `PostToolUse` 的主要區別是什麼？
- **Options**: A) 一個在工具前，一個在工具後 | B) 一個只給圖片用 | C) 一個是 CLI，一個是 MCP | D) 完全一樣
- **Correct**: A
- **Explanation**: `PreToolUse` 適合攔截和校驗；`PostToolUse` 適合驗證與補充上下文。
- **Review**: 最常見的事件

### Q4
- **Category**: practical
- **Question**: 如果你想先體驗 hooks 的價值，最推薦先試哪個範例？
- **Options**: A) `pre-commit.sh` | B) `favicon-32.svg` | C) `README.backup.md` | D) `project-CLAUDE.md`
- **Correct**: A
- **Explanation**: 提交前跑測試是最容易體會 hooks 價值的起步範例。
- **Review**: 一個高價值起步範例

### Q5
- **Category**: conceptual
- **Question**: hooks 支援哪四種型別？
- **Options**: A) `command`、`http`、`prompt`、`agent` | B) `shell`、`json`、`yaml`、`plugin` | C) `pre`、`post`、`read`、`write` | D) `sync`、`async`、`web`、`app`
- **Correct**: A
- **Explanation**: 這是 hooks 的四類主要執行方式。
- **Review**: 四種 hook 型別

### Q6
- **Category**: practical
- **Question**: hooks 設定裡哪些欄位最不能翻？
- **Options**: A) `hooks`、`matcher`、`type`、`command`、事件名 | B) 所有 Markdown 標題 | C) 只有註釋 | D) 只有檔名
- **Correct**: A
- **Explanation**: 這些欄位和事件名屬於協議結構，翻譯會直接損壞設定。
- **Review**: hooks 設定裡哪些不能翻

### Q7
- **Category**: conceptual
- **Question**: 為什麼“hook 做得太重”會影響使用體驗？
- **Options**: A) 因為它會讓每次觸發都變慢 | B) 因為 hook 會自動刪檔案 | C) 因為 hook 會禁用 Claude | D) 因為 hook 會禁用 Git
- **Correct**: A
- **Explanation**: 高成本 hook 會讓常規工作流變得拖沓，應該先從輕量檢查做起。
- **Review**: 常見坑

### Q8
- **Category**: practical
- **Question**: Windows 使用者使用 hooks 前，最重要的一個檢查點是什麼？
- **Options**: A) 當前 shell 是什麼 | B) 滑鼠速度 | C) 電池電量 | D) GitHub 頭像
- **Correct**: A
- **Explanation**: PowerShell、Git Bash、WSL 的差異會直接影響腳本相容性。
- **Review**: 新手使用者特別注意

---

## Lesson 07: Plugins

### Q1
- **Category**: conceptual
- **Question**: plugin 的核心價值是什麼？
- **Options**: A) 把多項 Claude Code 能力打包成一套可安裝方案 | B) 只用來放圖片 | C) 只用來寫 README | D) 只用來存 token
- **Correct**: A
- **Explanation**: plugin 用於分發整套工作流，而不是單一能力。
- **Review**: plugin 是什麼

### Q2
- **Category**: practical
- **Question**: plugin manifest 的標準位置是什麼？
- **Options**: A) `.claude-plugin/plugin.json` | B) `plugin.yaml` | C) `README.md` | D) `.mcp.json`
- **Correct**: A
- **Explanation**: 當前範例與現代結構都使用 `.claude-plugin/plugin.json`。
- **Review**: 基本結構

### Q3
- **Category**: conceptual
- **Question**: 什麼情況下特別適合做 plugin？
- **Options**: A) 只有一個簡單 command 時 | B) 工作流需要團隊統一分發時 | C) 只想做一篇部落格時 | D) 只想改單個註釋
- **Correct**: B
- **Explanation**: plugin 最適合做團隊級、一鍵安裝的整套能力分發。
- **Review**: 什麼時候該做 plugin

### Q4
- **Category**: practical
- **Question**: `.claude-plugin/plugin.json` 裡哪些 key 最不能翻？
- **Options**: A) `name`、`version`、`description`、`author`、`license` | B) 只有第一行 | C) 只有註釋 | D) 都可以翻
- **Correct**: A
- **Explanation**: 這些 key 直接影響 manifest 解析和 plugin 識別。
- **Review**: plugin manifest 裡哪些不能翻

### Q5
- **Category**: conceptual
- **Question**: 為什麼不建議在工作流還沒穩定時過早做 plugin？
- **Options**: A) 因為 plugin 不能改 | B) 因為打包會提高後續迭代成本 | C) 因為外掛只能官方維護 | D) 因為 plugin 不能含 commands
- **Correct**: B
- **Explanation**: 先把單項能力跑順，再打包更穩妥。
- **Review**: 什麼時候該做 plugin

### Q6
- **Category**: practical
- **Question**: `pr-review` 這個範例 plugin 主要解決什麼問題？
- **Options**: A) PR 審查流程 | B) Docker 映象壓縮 | C) 圖片裁剪 | D) 字型管理
- **Correct**: A
- **Explanation**: `pr-review` 把安全、測試和效能審查整合到 PR review 流程中。
- **Review**: 本目錄裡的範例 plugins

### Q7
- **Category**: conceptual
- **Question**: plugin 裡常見會一起打包哪些能力？
- **Options**: A) commands、skills、subagents、hooks、MCP | B) 只有 Markdown | C) 只有 shell | D) 只有 logo
- **Correct**: A
- **Explanation**: plugin 的價值就在於組合能力，而不是單檔案。
- **Review**: plugin 是什麼

### Q8
- **Category**: practical
- **Question**: 釋出中文 plugin 時，README 裡最值得額外說明什麼？
- **Options**: A) 依賴的外部服務、token、CLI、Windows / WSL 支援情況 | B) 作者最喜歡的電影 | C) 鍵盤顏色 | D) 不需要額外說明
- **Correct**: A
- **Explanation**: 這直接決定新手使用者能不能順利安裝和使用。
- **Review**: 新手使用者特別注意

---

## Lesson 08: Checkpoints

### Q1
- **Category**: conceptual
- **Question**: checkpoints 最核心的價值是什麼？
- **Options**: A) 幫你安全試錯和回退 | B) 自動部署 | C) 存 API key | D) 替代 Git
- **Correct**: A
- **Explanation**: checkpoints 讓你敢試，因為隨時可以回退。
- **Review**: checkpoint 是什麼

### Q2
- **Category**: practical
- **Question**: 開啟 checkpoint / rewind 介面的兩種常見方式是什麼？
- **Options**: A) `Esc+Esc` 或 `/rewind` | B) `/checkpoint-save` 或 `Ctrl+R` | C) `Alt+P` 或 `/memory` | D) 只能重啟 Claude
- **Correct**: A
- **Explanation**: 最常見方式就是雙擊 `Esc` 或使用 `/rewind`。
- **Review**: 怎麼開啟

### Q3
- **Category**: conceptual
- **Question**: 為什麼 checkpoints 對新手尤其重要？
- **Options**: A) 因為能降低“怕改壞”的心理門檻 | B) 因為必須先開 checkpoint 才能聊天 | C) 因為只對新手開放 | D) 因為它能自動修 bug
- **Correct**: A
- **Explanation**: 它解決的是試錯焦慮，而不只是回滾功能。
- **Review**: 為什麼它重要

### Q4
- **Category**: practical
- **Question**: `Restore code` 和 `Restore conversation` 的一個關鍵區別是什麼？
- **Options**: A) 前者主要回程式碼，後者主要回對話 | B) 二者完全一樣 | C) 前者會刪 Git 倉庫 | D) 後者會清空系統設定
- **Correct**: A
- **Explanation**: rewind 不是隻有一種回退方式，可以只退程式碼或只退對話。
- **Review**: rewind 時你會看到什麼選項

### Q5
- **Category**: conceptual
- **Question**: checkpoint 除了回退，還有什麼價值？
- **Options**: A) 用於探索多個實現方案並比較 | B) 只能清快取 | C) 只能匯出圖片 | D) 只能查版本號
- **Correct**: A
- **Explanation**: 它同樣適合做方案對比和實驗分支。
- **Review**: 一個很實用的工作流

### Q6
- **Category**: practical
- **Question**: 如果你想在中文化大改中安全嘗試多個版本，checkpoint 有什麼幫助？
- **Options**: A) 可以在誤翻關鍵標識後快速回退 | B) 會自動提交到 GitHub | C) 會幫你寫文案 | D) 會自動翻譯所有欄位
- **Correct**: A
- **Explanation**: 這類大範圍替換最適合藉助 checkpoint 做安全迭代。
- **Review**: 新手使用者特別注意

### Q7
- **Category**: conceptual
- **Question**: 為什麼 `Summarize from here` 對長會話很有用？
- **Options**: A) 因為它能壓縮上下文負擔 | B) 因為它會把程式碼刪掉 | C) 因為它會關掉 hooks | D) 因為它會改模型
- **Correct**: A
- **Explanation**: 長會話中，用 summary 替代大段歷史可以減少上下文壓力。
- **Review**: 新手最容易忽略的點

### Q8
- **Category**: practical
- **Question**: 哪類任務最適合配合 checkpoints 使用？
- **Options**: A) 高風險重構或多方案試驗 | B) 只看天氣 | C) 只改桌面圖示 | D) 單純改使用者名稱
- **Correct**: A
- **Explanation**: 高風險或多路線任務最能體現 checkpoint 的價值。
- **Review**: 常見使用場景

---

## Lesson 09: Advanced Features

### Q1
- **Category**: conceptual
- **Question**: planning mode 最適合什麼任務？
- **Options**: A) 多檔案複雜改動或高風險實現 | B) 一個小 typo | C) 只查一個命令拼寫 | D) 只看 logo
- **Correct**: A
- **Explanation**: planning mode 適合複雜任務先規劃再執行。
- **Review**: planning mode 什麼時候該用

### Q2
- **Category**: practical
- **Question**: 進入 planning mode 的一個常見入口是什麼？
- **Options**: A) `/plan ...` | B) `/memory` | C) `claude --logo` | D) `npm plan`
- **Correct**: A
- **Explanation**: `/plan` 是最常見入口之一。
- **Review**: planning mode 什麼時候該用

### Q3
- **Category**: conceptual
- **Question**: permission modes 為什麼重要？
- **Options**: A) 因為它決定 Claude 在本機能做多少事以及自動化邊界 | B) 因為它決定 logo 顏色 | C) 因為它決定磁碟大小 | D) 因為它替代 Git
- **Correct**: A
- **Explanation**: 許可權模式直接關係到風險控制和自動化強度。
- **Review**: permission modes 怎麼理解

### Q4
- **Category**: practical
- **Question**: `claude -p` 在 advanced features 裡最關鍵的意義是什麼？
- **Options**: A) 進入腳本和 CI/CD 自動化場景 | B) 改桌面主題 | C) 刪除 session | D) 生成 plugin market
- **Correct**: A
- **Explanation**: print mode 是 Claude Code 進入自動化的關鍵介面。
- **Review**: print mode 為什麼重要

### Q5
- **Category**: conceptual
- **Question**: 為什麼 background tasks 有價值？
- **Options**: A) 讓長任務後臺跑，不堵當前對話 | B) 它會自動修所有 bug | C) 它只給企業版用 | D) 它會替代 hooks
- **Correct**: A
- **Explanation**: background tasks 的價值是提升並行工作體驗。
- **Review**: background tasks 和 scheduled tasks

### Q6
- **Category**: practical
- **Question**: 如果你在公司網路環境中使用遠端或 web 功能，最該先確認什麼？
- **Options**: A) 網路、代理程式和訪問穩定性 | B) 滑鼠顏色 | C) Git 提交範本 | D) 顯示器亮度
- **Correct**: A
- **Explanation**: 遠端、web、desktop 相關能力很依賴網路環境。
- **Review**: 新手使用者特別注意

### Q7
- **Category**: conceptual
- **Question**: worktrees 和 sandboxing 分別更偏什麼？
- **Options**: A) 前者偏並行分支隔離，後者偏安全限制 | B) 二者都是寫部落格 | C) 二者都是影象編輯 | D) 前者做音訊，後者做影片
- **Correct**: A
- **Explanation**: worktrees 偏並行開發，sandboxing 偏許可權與隔離。
- **Review**: worktrees 和 sandboxing

### Q8
- **Category**: practical
- **Question**: 對新手來說，學 advanced features 的更合理順序是什麼？
- **Options**: A) 優先 planning mode、permission modes、print mode、background tasks | B) 先學全部高階特性 | C) 只學 remote | D) 不用學 CLI
- **Correct**: A
- **Explanation**: 這是最容易直接產生價值的一條主線。
- **Review**: 最該先掌握哪幾個

---

## Lesson 10: CLI

### Q1
- **Category**: conceptual
- **Question**: Claude Code CLI 最核心的地位是什麼？
- **Options**: A) 是最主要的使用入口，也是自動化基礎 | B) 只是裝飾功能 | C) 只能看版本號 | D) 只用於圖片處理
- **Correct**: A
- **Explanation**: 很多能力最後都要落到 CLI 使用和自動化整合上。
- **Review**: CLI 指南開頭

### Q2
- **Category**: practical
- **Question**: 下面哪個命令屬於 print mode？
- **Options**: A) `claude -p "explain this error"` | B) `/memory` | C) `/plugin install` | D) `git status`
- **Correct**: A
- **Explanation**: `claude -p` 是 print mode 的常見入口。
- **Review**: 互動模式 vs print mode

### Q3
- **Category**: conceptual
- **Question**: 互動模式和 print mode 的一個關鍵差別是什麼？
- **Options**: A) 前者偏多輪對話，後者偏一次性任務與腳本 | B) 二者完全相同 | C) print mode 不能輸出文字 | D) 互動模式不能讀檔案
- **Correct**: A
- **Explanation**: 這是兩種使用模式最核心的差別。
- **Review**: 互動模式 vs print mode

### Q4
- **Category**: practical
- **Question**: 哪個 flag 用於復原指定 session？
- **Options**: A) `-r, --resume` | B) `--logo` | C) `--theme` | D) `--fast-open`
- **Correct**: A
- **Explanation**: `-r` / `--resume` 用於復原指定 session。
- **Review**: 新手最該掌握的 flags

### Q5
- **Category**: conceptual
- **Question**: 為什麼 CLI 檔案裡的命令和 flags 不能中文化？
- **Options**: A) 因為它們是可複製執行的真實介面 | B) 因為中文不好看 | C) 因為 Git 不支援中文 | D) 因為 README 不允許
- **Correct**: A
- **Explanation**: CLI 是最典型的“說明文字可以翻，但命令本身不能翻”的內容。
- **Review**: 哪些內容不能翻

### Q6
- **Category**: practical
- **Question**: 哪組 flags 更適合新手優先掌握？
- **Options**: A) `-p`、`-c`、`-r`、`--model`、`--permission-mode` | B) 只學 `--version` | C) 只學 `--logo` | D) 只學 `--color`
- **Correct**: A
- **Explanation**: 這些是最直接影響日常使用效率的一組 flags。
- **Review**: 新手最該掌握的 flags

### Q7
- **Category**: conceptual
- **Question**: CLI 為什麼對自動化特別重要？
- **Options**: A) 因為腳本、CI/CD、批處理和結構化輸出都依賴它 | B) 因為它會自動幫你寫 README | C) 因為它會替代 memory | D) 因為它只能在瀏覽器裡執行
- **Correct**: A
- **Explanation**: 自動化幾乎都需要 CLI 入口。
- **Review**: CLI 和自動化的關係

### Q8
- **Category**: practical
- **Question**: Windows 使用者使用 CLI 時，最值得先確認什麼？
- **Options**: A) 當前是在 PowerShell、Git Bash 還是 WSL 中執行 | B) 鍵盤佈局 | C) 顯示器解析度 | D) 手機型號
- **Correct**: A
- **Explanation**: 這直接關係到命令相容性與路徑行為。
- **Review**: 新手使用者特別注意
