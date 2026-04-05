<picture>
  <source media="(prefers-color-scheme: dark)" srcset="resources/logos/claude-howto-logo-dark.svg">
  <img alt="Claude How To" src="resources/logos/claude-howto-logo.svg">
</picture>

# Claude Code 功能總表（Feature Catalog）

> 適合“先建立全域地圖，再進入某個模組”的讀者。

**快速導航**：  
[Slash Commands](#slash-commands) | [Permission Modes](#permission-modes) | [Subagents](#subagents) | [Skills](#skills) | [Plugins](#plugins) | [MCP](#mcp) | [Hooks](#hooks) | [Memory](#memory) | [新功能提示](#新功能提示)

---

## Summary

| 類別 | 內建能力 | 倉庫範例 | 適合先學嗎 | 入口 |
|------|----------|----------|------------|------|
| Slash Commands | 55+ | 8 | 非常適合 | [01-slash-commands/](01-slash-commands/) |
| Memory | 7 類 | 3 | 非常適合 | [02-memory/](02-memory/) |
| Skills | 5 個 bundled skills + 範例 | 多個 | 適合進階 | [03-skills/](03-skills/) |
| Subagents | 6 個內建 | 多個 | 適合進階 | [04-subagents/](04-subagents/) |
| MCP | 1 個內建生態入口 + 範例 | 多個 | 適合整合場景 | [05-mcp/](05-mcp/) |
| Hooks | 25 個事件 | 7 | 適合自動化 | [06-hooks/](06-hooks/) |
| Plugins | - | 3 | 適合團隊級方案 | [07-plugins/](07-plugins/) |
| Checkpoints | 內建 | 範例檔案 | 新手必學 | [08-checkpoints/](08-checkpoints/) |
| Advanced Features | 多項 | 範例檔案 | 高階再學 | [09-advanced-features/](09-advanced-features/) |
| CLI | 內建 | 參考檔案 | 全階段都用得到 | [10-cli/](10-cli/) |

---

## Slash Commands

slash commands 是使用者在 Claude Code 裡主動輸入的快捷操作，例如 `/help`、`/model`、`/rewind`。這也是新手最容易立刻感受到收益的能力。

### 常見內建命令

| 命令 | 用途 |
|------|------|
| `/help` | 檢視幫助 |
| `/clear` | 清空當前對話 |
| `/config` | 檢視或編輯設定 |
| `/agents` | 檢視可用 agents |
| `/skills` | 檢視可用 skills |
| `/hooks` | 檢視 hooks |
| `/mcp` | 檢視或管理 MCP servers |
| `/plugin` | 管理 plugins |
| `/plan` | 進入 planning mode |
| `/rewind` | 回退到 checkpoint |
| `/resume` | 復原之前的 session |
| `/branch` | 從當前對話分叉（某些版本中 `/fork` 仍可能可用） |

### 倉庫裡的範例命令

| 命令 | 檔案 | 典型用途 |
|------|------|----------|
| `/optimize` | `01-slash-commands/optimize.md` | 效能分析 |
| `/pr` | `01-slash-commands/pr.md` | PR 準備流程 |
| `/generate-api-docs` | `01-slash-commands/generate-api-docs.md` | API 檔案生成 |
| `/commit` | `01-slash-commands/commit.md` | 帶上下文的提交說明 |
| `/push-all` | `01-slash-commands/push-all.md` | stage + commit + push |
| `/doc-refactor` | `01-slash-commands/doc-refactor.md` | 檔案重構 |
| `/setup-ci-cd` | `01-slash-commands/setup-ci-cd.md` | CI/CD 初始化 |
| `/unit-test-expand` | `01-slash-commands/unit-test-expand.md` | 測試補全 |

**適合先學的原因**：複製檔案就能用，回饋快，挫敗感低。

---

## Permission Modes

permission modes 決定 Claude Code 在使用工具時需要多大授權。

| 模式 | 說明 | 適合什麼時候 |
|------|------|--------------|
| `default` | 大多數風險操作前詢問 | 日常互動 |
| `acceptEdits` | 自動接受檔案編輯，其他操作仍可能詢問 | 較信任的本機編輯 |
| `plan` | 只讀分析，不做修改 | 方案設計、程式碼閱讀 |
| `dontAsk` | 跳過需要額外授權的動作 | 非互動腳本 |
| `bypassPermissions` | 跳過許可權檢查 | 可信、受控的自動化環境 |
| `auto` | 根據分類器自動決定 | 高自動化流程（需要謹慎） |

新手使用者在剛上手時，優先理解 `default`、`acceptEdits`、`plan`、`dontAsk` 這四個就足夠了。

---

## Subagents

subagents 是專門負責某類任務的子代理程式。它們適合複雜任務拆分，比如“一個做程式碼審查，一個做測試，一個做檔案”。

### 常見內建 subagents

| 名稱 | 典型用途 |
|------|----------|
| `general-purpose` | 通用複雜任務 |
| `Plan` | 方案設計 |
| `Explore` | 快速搜尋與理解程式碼 |
| `Bash` | 終端命令執行 |

### 倉庫裡的範例 subagents

| 名稱 | 檔案 | 用途 |
|------|------|------|
| `code-reviewer` | `04-subagents/code-reviewer.md` | 程式碼品質審查 |
| `test-engineer` | `04-subagents/test-engineer.md` | 測試策略 |
| `documentation-writer` | `04-subagents/documentation-writer.md` | 檔案撰寫 |
| `secure-reviewer` | `04-subagents/secure-reviewer.md` | 安全審查 |
| `implementation-agent` | `04-subagents/implementation-agent.md` | 實現任務 |
| `debugger` | `04-subagents/debugger.md` | 根因分析 |
| `data-scientist` | `04-subagents/data-scientist.md` | 資料與 SQL 分析 |

---

## Skills

skills 是 Claude Code 會根據描述自動觸發的複用能力。它們往往比單個 slash command 更適合長期維護的工作流。

### 倉庫裡的範例 skills

| 名稱 | 資料夾 | 典型用途 |
|------|--------|----------|
| `code-review` | `03-skills/code-review/` | 程式碼審查 |
| `brand-voice` | `03-skills/brand-voice/` | 文案語氣統一 |
| `doc-generator` | `03-skills/doc-generator/` | 檔案生成 |
| `refactor` | `03-skills/refactor/` | 結構化重構 |
| `blog-draft` | `03-skills/blog-draft/` | 部落格草稿生成 |
| `claude-md` | `03-skills/claude-md/` | 生成或調整 `CLAUDE.md` |

### skill 結構

```text
.claude/skills/skill-name/
├── SKILL.md
├── scripts/
└── templates/
```

### 高風險提醒

`SKILL.md` 裡的 frontmatter 是可執行設定的一部分，不要翻譯這些欄位：

- `name`
- `description`
- `effort`
- `shell`

---

## Plugins

plugins 適合“把整套方案打包給團隊用”。它們通常會組合多個能力：

- slash commands
- skills
- subagents
- MCP
- hooks

### 倉庫裡的範例 plugins

| 名稱 | 位置 | 用途 |
|------|------|------|
| `pr-review` | `07-plugins/pr-review/` | PR 審查工作流 |
| `documentation` | `07-plugins/documentation/` | 檔案生成與同步 |
| `devops-automation` | `07-plugins/devops-automation/` | 部署、監控與事故處理 |

### plugin 結構

```text
plugin-name/
├── .claude-plugin/plugin.json
├── commands/
├── agents/
├── hooks/
├── mcp/
└── scripts/
```

`.claude-plugin/plugin.json` 是 manifest，`name`、`version`、`description`、`license` 這些 key 不要翻。

---

## MCP

MCP（Model Context Protocol）用於讓 Claude Code 連線外部工具、服務和實時資料。

### 倉庫裡的典型 MCP 設定

| 檔案 | 用途 |
|------|------|
| `05-mcp/github-mcp.json` | GitHub 整合 |
| `05-mcp/database-mcp.json` | 資料庫訪問 |
| `05-mcp/filesystem-mcp.json` | 檔案系統訪問 |
| `05-mcp/multi-mcp.json` | 多服務組合 |

### 新手使用者常見卡點

- `npx` 首次安裝 MCP server 時很慢
- GitHub Token 沒許可權或沒匯出
- Windows / WSL 環境下 shell 和路徑行為不同

### 高風險提醒

以下內容不要翻：

- `mcpServers`
- server 名稱，例如 `github`
- 環境變數名，例如 `GITHUB_TOKEN`
- 路徑佔位符和命令欄位

---

## Hooks

hooks 是事件驅動的自動化動作。適合這些場景：

- 調工具前做風險攔截
- 提交前跑測試
- 改完程式碼後自動格式化
- 結束前記錄上下文

### 倉庫裡的範例 hooks

| 檔案 | 用途 |
|------|------|
| `06-hooks/pre-commit.sh` | 提交前跑測試 |
| `06-hooks/format-code.sh` | 自動格式化 |
| `06-hooks/security-scan.sh` | 安全檢查 |
| `06-hooks/validate-prompt.sh` | prompt 校驗 |
| `06-hooks/log-bash.sh` | Bash 日誌記錄 |

### hook 型別

- `command`
- `http`
- `prompt`
- `agent`

這些型別名同樣不要翻成中文欄位。

---

## Memory

memory 是 Claude Code 用來長期載入規則和上下文的機制。

### 本倉庫裡的 memory 範例

| 檔案 | 用途 |
|------|------|
| `02-memory/project-CLAUDE.md` | 專案規則 |
| `02-memory/personal-CLAUDE.md` | 個人偏好 |
| `02-memory/directory-api-CLAUDE.md` | 目錄級規則範例 |

### 新手最重要的理解

- `CLAUDE.md` 不是隨便寫筆記的地方，它更像專案規範和上下文入口。
- 專案級和個人級 memory 適合放不同內容。
- memory 很強，但它不替代 skills、hooks 和 slash commands。

---

## 互動學習工具

這個倉庫內建了兩個互動式學習 skill，安裝後可以直接在 Claude Code 裡做自測和練習。

| skill | 位置 | 用途 |
|-------|------|------|
| `self-assessment` | `.claude/skills/self-assessment/` | 評估目前水平、識別短板、生成個人化學習路徑 |
| `lesson-quiz` | `.claude/skills/lesson-quiz/` | 針對單一模組出互動測驗題，檢查理解程度 |

### 如何安裝

```bash
mkdir -p ~/.claude/skills
cp -r .claude/skills/self-assessment ~/.claude/skills/
cp -r .claude/skills/lesson-quiz ~/.claude/skills/
```

### 如何使用

安裝後在 Claude Code 裡輸入：

```text
# 做整體水平自測
/self-assessment

# 對某個模組做測驗
/lesson-quiz hooks
/lesson-quiz 03
```

`self-assessment` 提供 Quick（2 分鐘）和 Deep（5 分鐘）兩種模式，最後會生成個人化學習路徑。  
`lesson-quiz` 每次 8 題，支援 before / during / after 三種測驗時機，答完給出錯題解析。

---

## 新功能提示

這個倉庫同步的是 Claude Code 較新的能力集，因此你會在檔案裡頻繁看到這些內容：

- Auto Mode
- Voice Dictation
- Channels
- background tasks
- scheduled tasks
- worktrees
- web sessions
- remote control

如果你是初學者，不需要先掌握這些。按 [LEARNING-ROADMAP.md](LEARNING-ROADMAP.md) 的順序往下學即可。

---

## 推薦閱讀順序

1. [README.md](README.md)
2. [LEARNING-ROADMAP.md](LEARNING-ROADMAP.md)
3. [QUICK_REFERENCE.md](QUICK_REFERENCE.md)
4. [01-slash-commands/](01-slash-commands/)
5. [02-memory/](02-memory/)
6. [10-cli/](10-cli/)
