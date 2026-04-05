<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../resources/logos/claude-howto-logo-dark.svg">
  <img alt="Claude How To" src="../resources/logos/claude-howto-logo.svg">
</picture>

# CLI 指南

Claude Code 的 CLI 是最核心的使用入口。  
很多功能看起來像“對話式能力”，但真正要高效使用、做自動化、接入腳本或 CI/CD，最後都繞不開 CLI。

---

## 最常用的命令

| 命令 | 用途 |
|------|------|
| `claude` | 開啟互動模式 |
| `claude "query"` | 帶初始問題進入 REPL |
| `claude -p "query"` | print mode，一次執行後退出 |
| `claude -c` | 繼續最近一次會話 |
| `claude -r "session"` | 復原指定 session |
| `claude mcp` | 管理 MCP |
| `claude agents` | 檢視 agents |
| `claude plugin` | 管理 plugins |
| `claude remote-control` | 啟動遠端控制 |
| `claude auth status` | 檢視登入狀態 |

如果你是新手，先熟悉 `claude`、`claude -p`、`claude -c`、`claude -r` 就已經很有價值。

---

## 互動模式 vs print mode

### 互動模式

適合：

- 連續問答
- 多輪上下文
- 現場探索
- 需要邊改邊聊

```bash
claude
claude "explain this project"
```

### print mode

適合：

- 一次性任務
- shell 腳本
- CI/CD
- 透過 pipe 處理輸入
- 結構化輸出

```bash
claude -p "what does this function do?"
cat error.log | claude -p "explain this error"
```

### 一個實用判斷標準

- 你要連續來回對話：互動模式
- 你要“給一條明確任務，然後退出”：print mode

---

## 新手最該掌握的 flags

| flag | 用途 |
|------|------|
| `-p, --print` | 進入 print mode |
| `-c, --continue` | 繼續最近一次會話 |
| `-r, --resume` | 復原指定 session |
| `-n, --name` | 給 session 起名 |
| `-w, --worktree` | 在 worktree 中啟動 |
| `--model` | 指定模型 |
| `--effort` | 指定思考強度 |
| `--permission-mode` | 指定許可權模式 |
| `--bare` | 以最小模式啟動 |
| `--add-dir` | 加額外目錄到工作上下文 |

---

## 一些真正常用的範例

### 檢視專案

```bash
claude "explain this project"
```

### 處理日誌

```bash
cat error.log | claude -p "explain this error"
```

### 繼續最近一次工作

```bash
claude -c
```

### 復原命名會話

```bash
claude -r "auth-refactor" "finish this task"
```

### 用於自動化

```bash
claude -p "Run tests and summarize failures" --permission-mode dontAsk
```

---

## 模型與設定

CLI 常見會和這些設定一起使用：

- `--model`
- `--fallback-model`
- `--effort`
- `--settings`
- `--append-system-prompt`

範例：

```bash
claude --model opus "design a caching strategy"
claude -p --fallback-model sonnet "summarize this diff"
claude --append-system-prompt "Always explain tradeoffs" "review this plan"
```

如果你要長期使用 Claude Code，把模型、許可權、輸出格式這些引數理解清楚，會直接影響效率和成本。

---

## 工具與許可權相關 flags

下面這些引數非常重要，但也是最容易被誤用的一組：

- `--permission-mode`
- `--dangerously-skip-permissions`
- `--allowedTools`
- `--disallowedTools`
- `--tools`

### 實用範例

```bash
# 只做只讀分析
claude --permission-mode plan "review this codebase"

# 非互動測試摘要
claude -p "Run tests" --permission-mode dontAsk

# 限制工具範圍
claude -p --tools "Read,Grep,Glob" "find all TODO comments"
```

---

## 輸出與格式

如果你要把 Claude Code 接進腳本或程式，最值得關注的是：

- `--output-format`
- `--json-schema`
- `--include-partial-messages`

### 常見使用方式

```bash
# 預設文字輸出
claude -p "explain this code"

# JSON 輸出
claude -p --output-format json "list all functions in main.py"

# 用 schema 約束結構
claude -p --json-schema '{"type":"object"}' "return structured analysis"
```

如果你的下游還要接 `jq`、Python、Node 或 CI job，結構化輸出會非常有用。

---

## workspace 與多目錄

如果你需要讓 Claude 同時看多個目錄，可以用：

```bash
claude --add-dir ../frontend ../backend ../shared "find all API endpoints"
```

這對 monorepo、前後端分倉或跨目錄排查問題特別有幫助。

---

## MCP 與 plugin 相關 CLI

你不只會在檔案裡看到：

- `claude mcp`
- `claude mcp serve`
- `claude plugin`

你實際使用中也經常會碰到它們。

### 典型場景

```bash
claude mcp
claude mcp serve
claude plugin install my-plugin
```

如果你要做自動化、整合第三方系統或團隊分發，這些命令遲早會用到。

---

## session 管理

當你開始做稍複雜的工作後，session 管理會非常重要。

常見場景：

- 延續昨天的任務
- 給當前任務起名
- 從當前會話分叉出實驗方案

常用命令和 flags：

- `/resume`
- `/rename`
- `/branch`（較新的主名稱，部分舊環境中 `/fork` 仍可能可用）
- `claude -c`
- `claude -r`

不命名 session，前期感覺沒問題，後期會越來越難管理。

---

## CLI 和自動化的關係

當你要做這些事情時，CLI 會變得尤其重要：

- CI/CD
- shell 腳本
- 批處理
- JSON 輸出
- 定時任務
- 後臺任務編排

很多“高階能力”最後都會落回 CLI 引數和腳本呼叫層。

所以如果你真想把 Claude Code 用深，CLI 不是可選項，而是核心能力。

---

## 哪些內容絕對不能翻

如果你在在地化檔案，這些內容必須保持英文原樣：

- `claude`
- `claude -p`
- flags，例如 `--model`、`--permission-mode`
- 子命令，例如 `claude mcp`、`claude plugin`
- 輸出格式名，例如 `json`

CLI 是最典型的“說明文字可以翻，命令本身不能翻”的內容。

---

## 新手使用者特別注意

### 1. 網路環境

如果你在公司網路、代理程式或受控環境下使用 CLI，先確認：

- API 訪問
- GitHub 連通性
- npm / uv / Python 依賴下載
- 證書與代理程式設定

### 2. Windows / WSL 差異

Windows 使用者建議儘早確認自己使用的是：

- PowerShell
- Git Bash
- WSL

這會直接影響路徑、命令列為和腳本相容性。

### 3. 自動化不要一開始就開太猛

建議從這些低風險任務開始：

- 日誌解釋
- 測試摘要
- 結構化分析

不要一開始就上高許可權全自動修改流程。

---

## 常見坑

### 1. 把 print mode 當普通聊天

`claude -p` 更適合一次性、明確輸入輸出的任務。

### 2. 不給 session 命名

短期還行，任務一多就會混亂。

### 3. 翻譯 CLI flags

這會讓使用者複製命令後直接失敗。

### 4. 沒區分“能跑”和“適合自動化”

某個命令能跑，不代表它就適合直接放進 CI/CD。

---

## Troubleshooting

如果 CLI 行為不符合預期，優先排查：

1. 當前是不是該用互動模式，而不是 print mode
2. flags 是否拼對
3. 許可權模式是否合適
4. 環境變數是否已匯出
5. 當前 shell / 路徑環境是否匹配

---

## Best Practices

- 先熟練 `claude`、`claude -p`、`claude -c`、`claude -r`
- 自動化從小任務開始
- 所有 CLI 範例都保留英文原樣
- 把 session 命名當成好習慣
- 新手使用者優先排除網路與 shell 環境問題

---

## 本目錄的範例腳本

| 腳本 | 用途 |
|------|------|
| `ci-example.sh` | CI/CD 場景：測試摘要、靜態分析、PR diff 摘要 |
| `pipe-example.sh` | Pipe 場景：日誌解釋、commit 摘要、程式碼解析、JSON 輸出 |

```bash
# 複製到專案使用
cp 10-cli/ci-example.sh your-project/.github/scripts/
cp 10-cli/pipe-example.sh your-project/scripts/

# 直接試跑 pipe-example.sh 示範模式
bash 10-cli/pipe-example.sh demo
```

---

## 推薦下一步

- 想更系統地看高階能力：看 [09-advanced-features](../09-advanced-features/)
- 想查安裝與路徑：看 [QUICK_REFERENCE.md](../QUICK_REFERENCE.md)
- 想結合 hooks / MCP / plugins：回看 [06-hooks](../06-hooks/)、[05-mcp](../05-mcp/)、[07-plugins](../07-plugins/)
