<picture>
  <source media="(prefers-color-scheme: dark)" srcset="resources/logos/claude-howto-logo-dark.svg">
  <img alt="Claude How To" src="resources/logos/claude-howto-logo.svg">
</picture>

# 常見問題與排錯指南

這份文件把各模組常見踩坑整合在一起，方便快速定位。  
如果某個問題只屬於特定模組，說明後面會附上該模組的詳細連結。

---

## 快速導航

- [安裝與啟動](#安裝與啟動)
- [Slash Commands](#slash-commands)
- [Memory / CLAUDE.md](#memory--claudemd)
- [Skills](#skills)
- [Subagents](#subagents)
- [MCP](#mcp)
- [Hooks](#hooks)
- [Plugins](#plugins)
- [CLI / Print Mode](#cli--print-mode)
- [Windows / WSL 專屬問題](#windows--wsl-專屬問題)
- [翻譯與在地化錯誤](#翻譯與在地化錯誤)

---

## 安裝與啟動

### `claude` 命令找不到

```
'claude' is not recognized as an internal or external command
```

**解法**：

```bash
npm install -g @anthropic-ai/claude-code
# 重新開啟終端後再試
```

如果 npm 安裝成功但仍找不到，檢查 npm global bin 是否在 PATH 裡：

```bash
npm bin -g    # 確認路徑
echo $PATH    # 確認 PATH 包含上面那個路徑
```

### API Key 未設定

```
Error: ANTHROPIC_API_KEY environment variable is not set
```

**解法**：

```bash
export ANTHROPIC_API_KEY="your_api_key"
# 永久生效請寫進 ~/.bashrc 或 ~/.zshrc
```

Windows 使用者見 [WINDOWS-GUIDE.md](WINDOWS-GUIDE.md)。

---

## Slash Commands

### 命令安裝後輸入 `/xxx` 沒反應

**排查順序**：

1. 確認檔案放在 `.claude/commands/`，不是 `.claude/` 根目錄
2. 確認副檔名是 `.md`（不是 `.txt`）
3. 確認 frontmatter 格式正確（YAML，不能有多餘縮排或空行）
4. 重新啟動 Claude Code 讓新命令生效

**正確路徑範例**：

```
your-project/
└── .claude/
    └── commands/
        └── optimize.md   ← 這裡
```

### 命令執行了但行為不對

最常見原因：frontmatter 裡的 `allowed-tools` 或 `description` 被誤改成中文。  
這些欄位必須保留英文原樣：

```yaml
---
description: Analyze performance and suggest optimizations   ← 不要翻這行
allowed-tools: Bash(git status:*), Read, Grep               ← 不要翻這行
---
```

**相關說明**：[01-slash-commands/README.md](01-slash-commands/README.md)

---

## Memory / CLAUDE.md

### Claude 每次進來都不記得專案規則

**排查順序**：

1. 確認檔案名稱是 `CLAUDE.md`（大寫，不是 `claude.md`）
2. 確認位置是專案根目錄（`./CLAUDE.md`）或 `~/.claude/CLAUDE.md`（個人級）
3. 在 Claude Code 裡輸入 `/memory` 確認是否有載入

### `CLAUDE.md` 寫了很多但 Claude 還是沒按規則做

**常見原因**：

- 寫了太多泛泛說明，沒有具體可執行的規則
- 規則和專案實際狀況已脫節

**建議**：優先寫「做 X 前先做 Y」、「禁止 Z」這類明確動作，而非「本專案是一個...」的介紹。

**相關說明**：[02-memory/README.md](02-memory/README.md)

---

## Skills

### Skill 安裝後 Claude 從不觸發

**排查順序**：

1. 確認安裝路徑是 `~/.claude/skills/<skill-name>/SKILL.md` 或 `.claude/skills/<skill-name>/SKILL.md`
2. 確認 `SKILL.md` 有 frontmatter，且 `description` 欄位描述夠具體
3. `description` 是 Claude 判斷何時觸發的依據——如果描述太模糊，Claude 不知道什麼時候該用

**description 寫得不好的例子**：

```yaml
description: A helpful skill for writing   # 太模糊
```

**較好的例子**：

```yaml
description: Use when user asks to review code quality, find bugs, or check style issues in changed files
```

### 把 SKILL.md 裡的欄位名翻成中文後 skill 壞了

frontmatter 欄位名不能翻譯：

```yaml
---
name: code-review          ← 不翻
description: ...           ← 不翻 key，value 可以中文
effort: low                ← 不翻
---
```

**相關說明**：[03-skills/README.md](03-skills/README.md)

---

## Subagents

### Subagent 裝了但 Claude 不知道什麼時候用它

同 Skills 問題：`description` 欄位要具體描述使用時機。

### 工具許可權給太多或太少

- 給太多：subagent 繞開了隔離的目的
- 給太少：agent 做不了事，頻繁報錯

建議從最小集合開始，例如 `Read, Grep, Glob`，再按需加。

**相關說明**：[04-subagents/README.md](04-subagents/README.md)

---

## MCP

### MCP Server 連不上

**排查順序**：

1. 確認 token 已匯出：`echo $GITHUB_TOKEN`
2. 確認 token scope 足夠（GitHub MCP 通常需要 `repo` scope）
3. 確認 `npx` 可正常執行：`npx --version`
4. 網路問題：在台灣嘗試連 GitHub 或 npm registry 有時需要代理程式

### 設定寫進去了但 MCP 不載入

最常見原因：JSON key 被翻譯成中文。以下欄位必須保留英文：

```json
{
  "mcpServers": {        ← 不能翻
    "github": {          ← 不能翻（server 名稱）
      "command": "npx",  ← 不能翻
      "env": {
        "GITHUB_PERSONAL_ACCESS_TOKEN": "..."  ← 不能翻
      }
    }
  }
}
```

### Windows 下 npx MCP 失敗

改用 `cmd /c` 形式，詳見 [WINDOWS-GUIDE.md](WINDOWS-GUIDE.md#mcp-servernpx-相關)。

**相關說明**：[05-mcp/README.md](05-mcp/README.md)

---

## Hooks

### Hook 設定好了但沒有觸發

**排查順序**：

1. 事件名是否正確（注意大小寫）：`PreToolUse`、`PostToolUse`、`UserPromptSubmit`
2. `matcher` 是否匹配到目標工具（例如 `"Write"` 不等於 `"write"`）
3. 腳本是否有執行權限：`chmod +x your-hook.sh`
4. 腳本路徑是否存在：用絕對路徑更保險
5. 腳本內部依賴是否安裝（`python3`、`node` 等）

### Hook 觸發了但行為不對

常見問題：
- exit code 不對：成功應返回 `0`，失敗返回非 `0`
- stdout 格式不對：如果要用 JSON 控制 Claude 行為，確認 JSON 格式正確
- hook 太慢：timeout 預設通常是 60 秒，複雜操作要注意

### 欄位名被翻成中文

```json
{
  "hooks": {           ← 不翻
    "PreToolUse": [{   ← 不翻（事件名）
      "matcher": "...", ← 不翻
      "hooks": [{
        "type": "command",  ← 不翻
        "command": "..."    ← 不翻
      }]
    }]
  }
}
```

**相關說明**：[06-hooks/README.md](06-hooks/README.md)

---

## Plugins

### Plugin 安裝後命令不見

**排查順序**：

1. `plugin.json` manifest 是否有效（JSON 格式正確、欄位名保留英文）
2. `commands/`、`agents/`、`hooks/` 目錄是否在正確位置
3. plugin 名稱是否保留英文（被翻成中文會導致識別失敗）

### 外部服務依賴連不上

Plugin 裡如果帶有 GitHub / Kubernetes / 第三方 API 設定，先確認：
- 對應的 token / API key 已設定
- 從本機可以連到那個服務
- 沒有公司防火牆或代理程式阻擋

**相關說明**：[07-plugins/README.md](07-plugins/README.md)

---

## CLI / Print Mode

### `claude -p` 輸出不如預期

**常見原因**：

- 任務描述太模糊——print mode 需要明確的一次性指令
- 需要互動才能完成的任務不適合 print mode

**建議**：從清晰、輸入輸出明確的任務開始，例如：

```bash
cat error.log | claude -p "條列這份日誌裡所有錯誤的原因"
```

### `claude -p` 要求額外許可權導致卡住

```bash
# 加上 --permission-mode dontAsk 避免互動中斷
claude -p "Run tests" --permission-mode dontAsk
```

### session 找不回來

- 建議在重要任務開始前用 `/rename "task-name"` 命名 session
- `claude -r "session-name"` 復原
- 如果沒有命名，用 `claude -c` 接續最近一次會話

**相關說明**：[10-cli/README.md](10-cli/README.md)

---

## Windows / WSL 專屬問題

Windows 下的問題通常集中在：

- `claude` 找不到 → PATH 沒更新，重開終端或重新安裝
- `.sh` 腳本無法執行 → 用 WSL 或 Git Bash 執行
- MCP npx 失敗 → 改用 `cmd /c npx ...` 形式
- 換行符號錯誤 → `dos2unix script.sh`
- 環境變數不生效 → 確認在正確的 shell 裡設定

完整說明見 **[WINDOWS-GUIDE.md](WINDOWS-GUIDE.md)**。

---

## 翻譯與在地化錯誤

### 常見"翻壞了"的位置

| 位置 | 不能翻的內容 |
|------|-------------|
| Slash command frontmatter | `description`、`allowed-tools` 的 key |
| SKILL.md frontmatter | `name`、`description`、`effort`、`shell` 的 key |
| Subagent frontmatter | `name`、`description`、`tools`、`model` 的 key |
| MCP JSON | `mcpServers`、server 名稱、`command`、`env` key |
| Hooks JSON | `hooks`、`matcher`、`type`、`command`、事件名 |
| Plugin manifest | `name`、`version`、`description`、`license` |

**通用原則**：可以翻 value（說明文字），不能翻 key（欄位名）。

### 驗證是否翻壞

```bash
uv run python scripts/validate_localization.py
```

這個腳本會自動檢查 frontmatter、JSON / YAML 解析、關鍵標識是否被誤改。

**相關說明**：[LOCALIZATION-STYLE.md](LOCALIZATION-STYLE.md)

---

## 還是解決不了？

1. 先跑 `uv run python scripts/validate_localization.py` 確認格式
2. 在 Claude Code 裡輸入 `/help` 看內建說明
3. 查閱對應模組的 README（每個模組末尾都有常見坑說明）
4. 回報問題：請在 GitHub 開 Issue
