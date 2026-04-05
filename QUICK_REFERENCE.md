<picture>
  <source media="(prefers-color-scheme: dark)" srcset="resources/logos/claude-howto-logo-dark.svg">
  <img alt="Claude How To" src="resources/logos/claude-howto-logo.svg">
</picture>

# Claude Code 速查卡（Quick Reference）

這份速查卡適合兩種場景：

- 你已經知道大概原理，現在只想快速複製命令
- 你正在本土化或二次改寫倉庫，想快速確認哪些路徑和標識不能動

---

## 🚀 安裝命令速查

### Slash Commands

```bash
# 安裝全部範例 slash commands
cp 01-slash-commands/*.md .claude/commands/

# 安裝單個命令
cp 01-slash-commands/optimize.md .claude/commands/
```

### Memory

```bash
# 專案級 memory
cp 02-memory/project-CLAUDE.md ./CLAUDE.md

# 個人級 memory
cp 02-memory/personal-CLAUDE.md ~/.claude/CLAUDE.md
```

### Skills

```bash
# 個人 skills
cp -r 03-skills/code-review ~/.claude/skills/

# 專案 skills
cp -r 03-skills/code-review .claude/skills/
```

### Subagents

```bash
# 安裝全部 subagents
cp 04-subagents/*.md .claude/agents/

# 安裝單個 subagent
cp 04-subagents/code-reviewer.md .claude/agents/
```

### MCP

```bash
# 先準備憑證
export GITHUB_TOKEN="your_token"
export DATABASE_URL="postgresql://..."

# 專案級 MCP 設定
cp 05-mcp/github-mcp.json .mcp.json

# 或者寫進使用者級設定 ~/.claude.json
```

### Hooks

```bash
mkdir -p ~/.claude/hooks
cp 06-hooks/*.sh ~/.claude/hooks/
chmod +x ~/.claude/hooks/*.sh
```

### Plugins

```bash
/plugin install pr-review
/plugin install devops-automation
/plugin install documentation
```

### Checkpoints

```bash
# checkpoints 預設自動建立
/rewind
```

### Advanced Features

```bash
# 進入規劃模式
/plan Task description

# 常見 permission mode
claude --permission-mode default
claude --permission-mode acceptEdits
claude --permission-mode plan
claude --permission-mode dontAsk
claude --permission-mode bypassPermissions

# session 常用命令
/resume
/rename "session-name"
/branch                # 某些版本中 `/fork` 仍可作为兼容别名
claude -c
claude -r "session-name"
```

---

## 📋 功能速查表

| 能力 | 安裝 / 所在位置 | 典型用法 | 備註 |
|------|------------------|----------|------|
| Slash Commands | `.claude/commands/*.md` | `/command-name` | 使用者主動觸發 |
| Memory | `./CLAUDE.md` / `~/.claude/CLAUDE.md` | 自動載入 | 長期規則和偏好 |
| Skills | `.claude/skills/*/SKILL.md` | 自動觸發 | 可複用工作流 |
| Subagents | `.claude/agents/*.md` | 自動委派 / 顯式呼叫 | 分工執行 |
| MCP | `.mcp.json` / `~/.claude.json` | `/mcp`、工具呼叫 | 實時外部能力 |
| Hooks | `~/.claude/hooks/*.sh` 等 | 事件觸發 | 自動檢查和自動化 |
| Plugins | `/plugin install` | 一次安裝多能力 | 團隊分發 |
| Checkpoints | 內建 | `Esc+Esc`、`/rewind` | 安全試錯 |
| Planning Mode | 內建 | `/plan <task>` | 複雜任務規劃 |
| Print Mode | 內建 | `claude -p` | 腳本 / CI/CD |

---

## 🧠 哪些標識不能翻

這部分最容易踩坑，單獨列出來：

- `/optimize`、`/pr`、`/review-pr`
- `skills`、`hooks`、`MCP`、`CLI`
- `allowed-tools`、`tools`、`model`、`env`
- `GITHUB_TOKEN`、`DATABASE_URL`
- `.mcp.json`
- `claude -p`

想繼續中文化倉庫時，先看：

- [LOCALIZATION-STYLE.md](LOCALIZATION-STYLE.md)
- [UPSTREAM.md](UPSTREAM.md)

---

## 🎯 常見場景速查

### 程式碼審查

```bash
# 方法 1：slash command
cp 01-slash-commands/optimize.md .claude/commands/
# 使用：/optimize

# 方法 2：subagent
cp 04-subagents/code-reviewer.md .claude/agents/

# 方法 3：skill
cp -r 03-skills/code-review ~/.claude/skills/

# 方法 4：plugin
/plugin install pr-review
```

### 檔案生成

```bash
cp 01-slash-commands/generate-api-docs.md .claude/commands/
cp 04-subagents/documentation-writer.md .claude/agents/
cp -r 03-skills/doc-generator ~/.claude/skills/
/plugin install documentation
```

### DevOps

```bash
/plugin install devops-automation
# 常見命令：/deploy /rollback /status /incident
```

### 團隊規範

```bash
cp 02-memory/project-CLAUDE.md ./CLAUDE.md
```

### 自動化與 Hooks

```bash
mkdir -p ~/.claude/hooks
cp 06-hooks/*.sh ~/.claude/hooks/
chmod +x ~/.claude/hooks/*.sh

# 常見例子
# - pre-commit.sh
# - format-code.sh
# - security-scan.sh
```

### 安全試錯

```bash
# 修改前後都記得 checkpoint 可回退
/rewind
```

### CI/CD

```bash
claude -p "Run all tests and generate report"
claude -p "Run tests" --permission-mode dontAsk
```

---

## 🇹🇼 新手使用者特別注意

### GitHub 訪問和 Token

- 很多 MCP 範例、plugin 範例預設依賴 GitHub。
- 開始之前先確認你能訪問 GitHub，並且 `GITHUB_TOKEN` 具備需要的 scope。

### `npm` / `npx` / `uv`

- 很多範例會用到 `npx` 安裝 MCP server。
- Python 相關腳本和測試通常依賴 `uv`。
- 如果第一次安裝很慢，優先檢查網路、代理程式、包管理映象和證書環境。

### Windows / WSL

- 如果你在 Windows 上，優先明確自己是在 PowerShell、Git Bash，還是 WSL 裡操作。
- 部分 shell 腳本和路徑寫法預設更偏 Unix / macOS / Linux 風格。

### 翻譯不要碰的地方

- frontmatter 欄位名
- JSON key
- shell 命令
- 環境變數
- slash command / skill / plugin / subagent 的名稱

---

## 🔗 常用入口

- [README.md](README.md)
- [LEARNING-ROADMAP.md](LEARNING-ROADMAP.md)
- [CATALOG.md](CATALOG.md)
- [01-slash-commands/](01-slash-commands/)
- [02-memory/](02-memory/)
- [03-skills/](03-skills/)
- [04-subagents/](04-subagents/)
- [05-mcp/](05-mcp/)
- [06-hooks/](06-hooks/)
- [07-plugins/](07-plugins/)
- [09-advanced-features/](09-advanced-features/)
- [10-cli/](10-cli/)
