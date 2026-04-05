<picture>
  <source media="(prefers-color-scheme: dark)" srcset="resources/logos/claude-howto-logo-dark.svg">
  <img alt="Claude How To" src="resources/logos/claude-howto-logo.svg">
</picture>

[![Source Project](https://img.shields.io/badge/source-luongnv89%2Fclaude--howto-24292f)](https://github.com/luongnv89/claude-howto)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Localization](https://img.shields.io/badge/localization-zh--TW-brightgreen)](LOCALIZATION-STYLE.md)
[![Claude Code](https://img.shields.io/badge/Claude_Code-2.1+-purple)](https://code.claude.com)

# Claude Code 中文全面上手指南

從會輸入 `claude`，到真正會組合使用 slash commands、memory、skills、hooks、MCP、subagents 和 plugins。

這是一個基於上游專案 [`luongnv89/claude-howto`](https://github.com/luongnv89/claude-howto) 的 **非官方繁體中文化 fork**。它不是生硬逐句翻譯，而是面向臺灣使用者重寫表達方式、補齊學習路徑、保留所有關鍵可執行標識，並加入翻譯後相容性校驗。

**[15 分鐘快速開始](#-15-分鐘快速開始)** | **[先判斷你適合從哪開始](#-不知道從哪裡開始)** | **[瀏覽功能總表](CATALOG.md)** | **[Windows 使用指南](WINDOWS-GUIDE.md)** | **[排錯指南](TROUBLESHOOTING.md)** | **[檢視來源與同步說明](UPSTREAM.md)**

---

## 最近同步

- **最近同步日期**：2026-04-01
- **同步上游基線**：`d41b335` -> `0ca8c37`
- **本次同步內容**：
  - 上游不再推薦透過 `06-hooks/auto-adapt-mode.py` 學習使用者核准記錄，改為一次性許可權種子腳本 `09-advanced-features/setup-auto-mode-permissions.py`
  - `Advanced Features` 中的 auto-mode 許可權基線收窄為更保守的預設集合，並支援按需開啟 edits、tests、git writes、package installs、GitHub write 等能力
  - 上游 `README` 增加了 GitHub Trending 徽章；中文版倉庫**不直接照搬該徽章**，避免把上游熱度狀態誤寫成當前中文 fork 的實際狀態

---

## Table of Contents

- [最近同步](#最近同步)
- [這是什麼專案](#這是什麼專案)
- [本專案做了哪些調整](#本專案做了哪些調整)
- [哪些內容為了相容性不會翻譯](#哪些內容為了相容性不會翻譯)
- [為什麼這份指南更適合初學者](#為什麼這份指南更適合初學者)
- [怎麼使用這份指南](#怎麼使用這份指南)
- [不知道從哪裡開始](#-不知道從哪裡開始)
- [15 分鐘快速開始](#-15-分鐘快速開始)
- [你能用它搭什麼](#你能用它搭什麼)
- [常見問題](#常見問題)
- [Contributing](#contributing)
- [License](#license)

---

## 這是什麼專案

如果你已經裝好了 Claude Code，但只會簡單對話，很容易卡在這幾個地方：

- 官方檔案告訴你“有什麼功能”，卻不會告訴你“這些功能怎麼組合起來真正在專案裡省時間”。
- 你知道 `CLAUDE.md`、hooks、MCP、skills、subagents 這些詞，但不知道先學哪個、後學哪個。
- 你能看懂一些簡單範例，但還不會把它們變成自己的 code review、檔案生成、自動化流程。

這個倉庫的目標，就是把這些碎片能力整理成一條可落地的學習路徑，讓你知道：

- 先學什麼最有效
- 每個功能什麼時候用
- 哪些範例可以直接複製
- 哪些看起來像普通文字、其實不能亂翻

---

## 本專案做了哪些調整

和上游英文專案相比，這個中文版做了這些本土化處理：

- 把首頁、學習路線、速查卡、功能目錄等核心入口檔案改成中文主線表達。
- 用初學者更容易理解的方式重寫“是什麼 / 什麼時候用 / 怎麼裝 / 怎麼跑 / 常見坑”。
- 保留所有會影響執行的關鍵標識，避免為了翻譯把範例翻壞。
- 補充新手使用者常見障礙說明，比如 GitHub Token、`npm` / `npx` / `uv` / Python 環境、網路與代理程式、macOS / Windows / WSL 差異。
- 增加來源宣告、同步策略和在地化風格規範，方便後續持續跟進上游版本。
- 增加在地化校驗腳本，自動檢查 frontmatter、JSON/YAML、shell 腳本、關鍵命令名和受保護標識是否仍然可用。

詳細規則見：

- [UPSTREAM.md](UPSTREAM.md)
- [LOCALIZATION-STYLE.md](LOCALIZATION-STYLE.md)

---

## 哪些內容為了相容性不會翻譯

為了確保範例仍然能直接複製執行，下列內容預設 **保留英文，不做中文化改名**：

- 目錄名、檔名
- slash command 名稱
- skill / subagent / plugin 名稱
- YAML frontmatter key
- JSON / YAML key
- CLI flags、環境變數名、路徑佔位符、MCP server 名
- 程式碼塊裡的可執行命令、設定片段、協議欄位

舉例來說，`skills`、`CLI`、`hooks`、`MCP`、`subagents` 這些術語在正文裡通常會保留英文，並在首次出現時補充中文解釋；但不會粗暴改成一個中文詞後再讓讀者回頭猜原始命令是什麼。

---

## 為什麼這份指南更適合初學者

這個中文版本不是“翻譯腔”檔案，而是按學習體驗重新組織表達：

- 先講清楚“這是什麼”和“什麼時候用”，再給你命令和設定。
- 儘量把容易混淆的概念放在一起對比，比如 slash commands、skills、memory、hooks、plugins 的職責邊界。
- 對新手開發者常見的安裝、訪問和許可權問題，直接給出前置提醒，不讓你跑到一半才踩坑。
- 對高風險範例明確提醒哪些行不能翻、哪些欄位不能改。

---

## 怎麼使用這份指南

### 1. 先找自己的起點

直接看 [LEARNING-ROADMAP.md](LEARNING-ROADMAP.md)，先做自測，再按 beginner / intermediate / advanced 路線學。

### 2. 再按模組逐步上手

倉庫裡的 10 個模組按推薦順序排列：

1. [Slash Commands](01-slash-commands/)
2. [Memory](02-memory/)
3. [Checkpoints](08-checkpoints/)
4. [CLI Basics](10-cli/)
5. [Skills](03-skills/)
6. [Hooks](06-hooks/)
7. [MCP](05-mcp/)
8. [Subagents](04-subagents/)
9. [Advanced Features](09-advanced-features/)
10. [Plugins](07-plugins/)

### 3. 邊學邊複製範本

這個倉庫不是純閱讀材料。很多檔案都可以直接複製到你的專案裡，例如：

- `01-slash-commands/*.md`
- `02-memory/project-CLAUDE.md`
- `03-skills/*/SKILL.md`
- `04-subagents/*.md`
- `05-mcp/*.json`
- `06-hooks/*.sh`
- `07-plugins/*`

### 4. 每改一處範例都先確認相容性

如果你繼續 fork 並深度在地化，建議每次改完都跑：

```bash
uv run python scripts/validate_localization.py
```

它會幫你檢查：

- Markdown 相對連結
- YAML frontmatter
- JSON / YAML 解析
- shell 腳本語法
- 關鍵可執行標識是否被誤改

---

## 🌱 不知道從哪裡開始

如果你還不確定自己算什麼水平，可以直接用下面這套簡版判斷：

| 你目前的情況 | 建議起點 | 預計時間 |
|--------------|----------|----------|
| 只會開啟 Claude Code 聊天 | [01-slash-commands](01-slash-commands/) | 約 2.5 小時 |
| 已經用過 `CLAUDE.md` 和一些命令 | [03-skills](03-skills/) | 約 3.5 小時 |
| 已經開始碰 hooks、MCP、subagents | [09-advanced-features](09-advanced-features/) | 約 5 小時 |

完整路線見 [LEARNING-ROADMAP.md](LEARNING-ROADMAP.md)。

---

## 🚀 15 分鐘快速開始

如果你只是想先跑起來，不想馬上看完整教學，可以先做這一套：

```bash
# 1. 準備專案目錄
mkdir -p /path/to/your-project/.claude/commands

# 2. 複製第一個 slash command
cp 01-slash-commands/optimize.md /path/to/your-project/.claude/commands/

# 3. 在 Claude Code 裡試用
# /optimize

# 4. 加上專案級 memory
cp 02-memory/project-CLAUDE.md /path/to/your-project/CLAUDE.md

# 5. 安裝一個 skill
mkdir -p ~/.claude/skills
cp -r 03-skills/code-review ~/.claude/skills/
```

如果你想在 1 小時內完成最小可用設定，可以繼續：

```bash
# Slash commands
cp 01-slash-commands/*.md .claude/commands/

# Project memory
cp 02-memory/project-CLAUDE.md ./CLAUDE.md

# A reusable skill
cp -r 03-skills/code-review ~/.claude/skills/

# 週末目標：繼續加 hooks、MCP、subagents、plugins
```

---

## 你能用它搭什麼

| 場景 | 你會組合哪些能力 |
|------|------------------|
| 自動化程式碼審查 | Slash Commands + Subagents + Memory + MCP |
| 團隊 onboarding | Memory + Slash Commands + Plugins |
| 檔案自動生成 | Skills + Subagents + Plugins |
| CI/CD 自動化 | CLI + Hooks + Background Tasks |
| 安全審計 | Skills + Hooks + Subagents |
| DevOps 流程 | Plugins + MCP + Hooks |
| 大型重構 | Checkpoints + Planning Mode + Hooks |

---

## 常見問題

**這是官方專案嗎？**  
不是。這是基於上游社群專案做的繁體中文化 fork，來源與同步策略見 [UPSTREAM.md](UPSTREAM.md)。

**我能直接複製裡面的命令和設定嗎？**  
大多數可以，但前提是你不要改壞關鍵標識。像 frontmatter key、JSON key、CLI flags、環境變數名這些不能為了中文化而改掉。

**為什麼有些術語不翻譯？**  
因為很多術語一旦翻譯，會讓你在真實使用 Claude Code、搜尋官方檔案、複製命令時更容易混淆。這個專案遵循“術語保真，解釋中文化”的原則。

**新手使用者最容易卡在哪？**  
常見是：GitHub 訪問、Token 許可權、`npm` / `npx` / `uv` / Python 環境、Windows 和 WSL 差異、以及把範例裡可執行欄位誤翻譯。

**能離線看嗎？**  
可以。執行：

```bash
uv run scripts/build_epub.py
```

會生成 EPUB 電子書。腳本說明見 [scripts/README.md](scripts/README.md)。

**之後怎麼跟上游同步？**  
請先看 [UPSTREAM.md](UPSTREAM.md)。本倉庫預設按“持續同步上游、中文側增量跟進”的方式維護。

---

<details>
<summary>快速導航：所有核心能力</summary>

| 能力 | 說明 | 入口 |
|------|------|------|
| 功能總表 | 一眼看全所有功能、安裝方式、適用場景 | [CATALOG.md](CATALOG.md) |
| 學習路線 | 從新手到進階的推薦學習順序 | [LEARNING-ROADMAP.md](LEARNING-ROADMAP.md) |
| Quick Reference | 安裝命令、路徑、常用場景速查 | [QUICK_REFERENCE.md](QUICK_REFERENCE.md) |
| Slash Commands | 使用者主動觸發的快捷操作 | [01-slash-commands/](01-slash-commands/) |
| Memory | 持久上下文與規則 | [02-memory/](02-memory/) |
| Skills | 自動觸發的複用能力 | [03-skills/](03-skills/) |
| Subagents | 分工明確的 AI 助手 | [04-subagents/](04-subagents/) |
| MCP | 外部工具與實時資料接入 | [05-mcp/](05-mcp/) |
| Hooks | 事件驅動自動化 | [06-hooks/](06-hooks/) |
| Plugins | 多能力打包分發 | [07-plugins/](07-plugins/) |
| Checkpoints | 安全試錯與回退 | [08-checkpoints/](08-checkpoints/) |
| Advanced Features | plan、auto mode、background tasks 等高階能力 | [09-advanced-features/](09-advanced-features/) |
| CLI | `claude` / `claude -p` / session / automation 參考 | [10-cli/](10-cli/) |
| 互動學習工具 | self-assessment 自測 + lesson-quiz 模組測驗 | [CATALOG.md#互動學習工具](CATALOG.md#互動學習工具) |

</details>

<details>
<summary>核心能力對照</summary>

| 能力 | 觸發方式 | 永續性 | 最適合什麼 |
|------|----------|--------|------------|
| Slash Commands | 手動輸入 `/cmd` | 當前會話 | 高頻快捷操作 |
| Memory | 自動載入 | 跨會話 | 長期規則與偏好 |
| Skills | 自動觸發 | 檔案系統級 | 可複用工作流 |
| Subagents | 自動委派或顯式呼叫 | 獨立上下文 | 任務拆分 |
| MCP | 自動查詢 | 實時 | 外部系統接入 |
| Hooks | 事件觸發 | 設定級 | 自動檢查和攔截 |
| Plugins | 一次安裝 | 組合能力 | 團隊級打包方案 |
| Checkpoints | 內建 | 會話級 | 安全試錯 |
| Planning Mode | 手動或自動進入 | 計劃階段 | 複雜實現 |
| CLI | 終端命令 | 腳本 / 會話 | 自動化與 CI/CD |

</details>

---

## Contributing

歡迎繼續把這個中文 fork 做得更適閤中文使用者，但請遵循兩個底線：

- 先看 [LOCALIZATION-STYLE.md](LOCALIZATION-STYLE.md)，不要把可執行標識翻壞。
- 先看 [UPSTREAM.md](UPSTREAM.md)，不要在沒有記錄對映關係的情況下隨意偏離上游結構。

如果你要貢獻翻譯或重寫內容，建議至少本機跑一次：

```bash
uv run python scripts/validate_localization.py
```

---

## License

本倉庫沿用上游專案的 [MIT License](LICENSE)。

來源專案、上游 commit、同步策略和在地化邊界見 [UPSTREAM.md](UPSTREAM.md)。
