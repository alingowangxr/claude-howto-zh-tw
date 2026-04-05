<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../resources/logos/claude-howto-logo-dark.svg">
  <img alt="Claude How To" src="../resources/logos/claude-howto-logo.svg">
</picture>

# Slash Commands 指南

slash commands 是你在 Claude Code 裡最容易立即上手的能力。它們本質上是“用 `/command` 快速觸發某個操作或工作流”。

對新手來說，先學會 slash commands，通常比先碰 hooks、MCP 或 plugins 更有回報，因為：

- 安裝簡單
- 回饋快
- 更容易理解 Claude Code 的工作方式
- 很多常用工作流都能先用它起步

---

## 什麼是 slash commands

Claude Code 裡的 slash commands 大致分四類：

- **Built-in commands**：Claude Code 自帶的命令，如 `/help`、`/clear`、`/model`
- **Skills 形式的命令**：透過 `SKILL.md` 定義，仍然可以用 `/name` 呼叫
- **Plugin commands**：安裝 plugin 後帶來的命令
- **MCP prompts**：由 MCP server 暴露出來的命令

> 現在更推薦用 `skills` 來承載自定義命令。`.claude/commands/` 依然能用，但新專案更建議看 [03-skills](../03-skills/)。

---

## 先知道這幾個高頻命令

| 命令 | 用途 |
|------|------|
| `/help` | 檢視幫助和命令列表 |
| `/clear` | 清空當前會話 |
| `/config` | 檢視或編輯設定 |
| `/context` | 看上下文使用情況 |
| `/model` | 切換模型 |
| `/agents` | 檢視可用 agents |
| `/skills` | 檢視可用 skills |
| `/hooks` | 檢視 hooks |
| `/mcp` | 管理 MCP |
| `/plugin` | 管理 plugins |
| `/plan` | 進入 planning mode |
| `/rewind` | 回退到 checkpoint |
| `/resume` | 復原以前的 session |

這些命令不用安裝，開箱即用。

---

## 本目錄裡的範例命令

| 檔案 | 觸發方式 | 用途 |
|------|----------|------|
| `optimize.md` | `/optimize` | 分析效能與最佳化機會 |
| `pr.md` | `/pr` | 提交 PR 前的整理與檢查 |
| `generate-api-docs.md` | `/generate-api-docs` | 生成 API 檔案 |
| `commit.md` | `/commit` | 生成提交說明 |
| `push-all.md` | `/push-all` | stage + commit + push |
| `doc-refactor.md` | `/doc-refactor` | 檔案重構 |
| `setup-ci-cd.md` | `/setup-ci-cd` | CI/CD 初始化 |
| `unit-test-expand.md` | `/unit-test-expand` | 擴充測試覆蓋 |

---

## 怎麼安裝

### 安裝全部範例命令

```bash
mkdir -p .claude/commands
cp 01-slash-commands/*.md .claude/commands/
```

### 安裝單個命令

```bash
mkdir -p .claude/commands
cp 01-slash-commands/optimize.md .claude/commands/
```

然後在 Claude Code 中直接輸入：

```text
/optimize
```

---

## command 檔案裡哪些不能翻

這一點非常重要。`*.md` 裡的說明文字可以中文化，但這些內容不要翻：

- frontmatter key，例如 `description`、`allowed-tools`
- 真實命令名，例如 `/optimize`
- `Bash(...)` 許可權約束
- 程式碼塊裡的可執行命令

例如 [`pr.md`](./pr.md) 裡的這些行必須保留：

- `allowed-tools:`
- `Bash(git add:*)`
- `Bash(git status:*)`
- `Bash(git diff:*)`

---

## 推薦你先用哪幾個

如果你是第一次認真用 Claude Code，優先試這幾個：

### `/optimize`

適合你想讓 Claude 幫你看效能問題、記憶體問題、演算法改進時。

### `/pr`

適合你準備發 PR 前做一次結構化檢查，順手整理提交資訊。

### `/generate-api-docs`

適合後端或介面專案，尤其是你已經有一些固定的介面風格想統一輸出檔案時。

---

## slash commands 和 skills 的關係

很多人一開始會混：

- slash commands：更像“我主動輸入一個命令，觸發一個固定動作”
- skills：更像“Claude 在合適的時候自動呼叫的複用能力”

簡單理解：

- 想自己明確觸發：先用 slash commands
- 想讓 Claude 自動判斷是否該啟用：再考慮 skills

---

## 什麼時候該升級成 skill

如果你發現某個 slash command 出現這些情況，就可以考慮遷移到 skill：

- 你在多個專案裡都要重複用
- 它不只是一個短 prompt，還依賴腳本、範本、參考檔案
- 你希望 Claude 在合適場景下自動呼叫，而不是每次手動輸入

下一步可以看 [03-skills](../03-skills/)。

---

## 常見坑

### 1. 檔案放對了，但命令不生效

優先檢查：

- 路徑是不是 `.claude/commands/`
- 副檔名是不是 `.md`
- frontmatter 格式是不是正確

### 2. 翻譯後命令壞了

最常見是把這些東西翻譯掉了：

- `description`
- `allowed-tools`
- `/command-name`

### 3. 以為 command 和 skill 是兩套完全不同的東西

不是。現在推薦實踐是更偏向 skill，只是呼叫方式和使用時機不同。

---

## 推薦下一步

- 剛會用 slash commands：去看 [02-memory](../02-memory/)
- 想做自動觸發工作流：去看 [03-skills](../03-skills/)
- 想快速查命令：回到 [QUICK_REFERENCE.md](../QUICK_REFERENCE.md)
