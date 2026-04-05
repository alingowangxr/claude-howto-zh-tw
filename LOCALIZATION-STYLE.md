# Localization Style Guide

## 目標

這份規範用於約束 `claude-howto-zh-tw` 的繁體中文化方式，確保兩件事同時成立：

- 中文使用者更容易讀懂、學會、照著做
- 檔案裡的命令、設定、範本、frontmatter、JSON/YAML 片段仍然可執行

## 核心原則

### 1. 術語保真，解釋中文化

優先保留英文術語，並在首次出現時補充中文解釋。例如：

- `skills`：可複用、可自動觸發的能力
- `CLI`：命令列介面
- `hooks`：事件觸發的自動化動作
- `MCP`：用於連線外部工具和資料的協議
- `subagents`：用於分工協作的子代理程式

不建議把這些詞統一硬翻成一個中文詞後全文替換。

### 2. 執行相關標識禁止翻譯

以下內容預設視為 **protected tokens**：

- 目錄名、檔名、副檔名
- slash command 名稱
- skill / subagent / plugin 名稱
- YAML frontmatter key
- JSON / YAML key
- CLI 命令和 flags
- 環境變數名
- MCP server 名
- 路徑佔位符
- 程式碼塊中的可執行命令

範例：

- `allowed-tools`
- `tools`
- `model`
- `env`
- `GITHUB_TOKEN`
- `.mcp.json`
- `/optimize`
- `claude -p`

這些內容可以解釋，但不要改名。

### 3. 面向初學者重寫表達

正文儘量遵循這個順序：

1. 這是什麼
2. 什麼時候用
3. 需要提前準備什麼
4. 怎麼安裝 / 設定 / 執行
5. 常見坑和排錯建議

不要一上來就給一大段術語、欄位表或抽象定義。

## 建議保留英文的高頻術語

- Claude Code
- slash commands
- memory
- skills
- subagents
- hooks
- plugins
- MCP
- CLI
- print mode
- planning mode
- Auto Mode
- checkpoints
- session
- worktree

## 中文寫法建議

- 第一次出現術語時寫成：`skills`（可複用能力）這樣的格式。
- 解釋型內容多用短句，少用生硬長句。
- 能直接幫助使用者操作的提醒，優先寫在命令前面。
- 對新手使用者常見障礙，儘量提前提示，不要等到“疑難排解”章節再說。

## 允許改寫的內容

- 標題
- 導語
- 對比表
- FAQ
- 學習路線描述
- 註釋和說明型輸出
- Mermaid 圖中的說明性文字

## 預設不要改的內容

- frontmatter 欄位名
- JSON / YAML key
- shell 命令
- 路徑和目錄名
- 環境變數名
- 插件/skill/subagent/command 的真實標識

## 風險等級

### 低風險

- 普通 `README.md`
- 學習路線、FAQ、導讀、對比表

可以做完整中文重寫。

### 中風險

- `SKILL.md`
- subagent `.md`
- slash command `.md`

只翻譯人類可讀說明，保留協議格式、欄位名、命令、識別符號。

### 高風險

- `.json`
- `.yml` / `.yaml`
- `.py`
- `.sh`
- GitHub Actions

除非明確知道不會影響行為，否則不要做功能性改寫；如需中文化，只改註釋或使用者可見文案。

## 提交前檢查

提交前至少執行一次：

```bash
uv run python scripts/validate_localization.py
```

它會檢查：

- Markdown 相對連結
- YAML frontmatter
- JSON / YAML 語法
- shell 腳本語法
- 關鍵 protected tokens 是否仍存在

## 常見反例

錯誤做法：

- 把 `skills` 全文改成“技能系統”，卻不保留原英文
- 把 `allowed-tools` 翻成 `允许工具`
- 把 `/optimize` 改成 `/优化`
- 把 `GITHUB_TOKEN` 改成 `GitHub令牌`
- 把 `.mcp.json` 改成中檔案名

推薦做法：

- 保留 `/optimize`，正文裡解釋“這是一個用於效能分析的 slash command”
- 保留 `GITHUB_TOKEN`，正文裡補充“需要先在 GitHub 建立 token 並匯出到環境變數”
