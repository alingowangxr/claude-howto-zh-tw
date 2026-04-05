<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../resources/logos/claude-howto-logo-dark.svg">
  <img alt="Claude How To" src="../resources/logos/claude-howto-logo.svg">
</picture>

# MCP 指南

MCP（Model Context Protocol）是 Claude Code 用來接入外部工具、服務和實時資料的協議。你可以把它理解成：Claude 不只是“聊天”，而是真的能透過標準介面去訪問 GitHub、資料庫、檔案系統等外部能力。

---

## MCP 解決什麼問題

如果沒有 MCP，Claude 只能基於你提供的上下文回答。  
有了 MCP，它可以：

- 獲取實時資料
- 呼叫外部工具
- 訪問專案外的資訊源
- 把結果帶回當前工作流

和 memory 的區別很簡單：

- memory 適合長期穩定規則
- MCP 適合實時、外部、動態資料

---

## MCP 常見應用場景

- GitHub PR / issue 查詢
- 資料庫讀寫
- 檔案系統訪問
- Slack / Docs / 其他 SaaS 工具整合

---

## 本目錄裡的範例設定

| 檔案 | 用途 |
|------|------|
| `github-mcp.json` | GitHub MCP 設定 |
| `database-mcp.json` | 資料庫 MCP 設定 |
| `filesystem-mcp.json` | 檔案系統 MCP 設定 |
| `multi-mcp.json` | 多個 MCP server 組合範例 |

---

## 最常見的安裝方式

### HTTP transport

```bash
claude mcp add --transport http notion https://mcp.notion.com/mcp
```

### stdio transport

```bash
claude mcp add --transport stdio myserver -- npx @myorg/mcp-server
```

### WebSocket transport

```bash
claude mcp add --transport ws realtime-server wss://example.com/mcp
```

---

## 直接複製範例設定

如果你只想先試 GitHub MCP：

```bash
export GITHUB_TOKEN="your_token"
cp 05-mcp/github-mcp.json .mcp.json
```

如果你想一次掛多個服務：

```bash
cp 05-mcp/multi-mcp.json .mcp.json
```

---

## 哪些內容不能翻

MCP 設定是高風險檔案，以下內容預設不要翻：

- `mcpServers`
- server 名稱，例如 `github`
- `command`
- `args`
- `env`
- 環境變數名，例如 `GITHUB_TOKEN`

正文解釋可以中文化，但 JSON key 和 server 名稱不要改。

---

## 新手使用者特別注意

### 1. 網路和代理程式

很多 MCP server 依賴：

- `npx`
- 外部 API
- GitHub 或第三方服務

如果你在臺灣網路環境下第一次執行慢、失敗、超時，優先檢查：

- 代理程式設定
- npm registry / Node 環境
- GitHub 訪問
- 證書與公司網路策略

### 2. Token 和許可權

例如 GitHub MCP 最常見的失敗原因是：

- `GITHUB_TOKEN` 沒設定
- token scope 不夠
- 環境變數只在一個 shell 會話裡設定了

### 3. Windows / WSL 差異

如果你在原生 Windows 上執行 `npx` MCP server，有時需要參考官方建議用 `cmd /c` 風格處理。

---

## memory 和 MCP 怎麼選

### 用 memory

- 專案規則
- 團隊約定
- 長期穩定背景資訊

### 用 MCP

- GitHub / 資料庫 / 檔案系統 / 第三方平臺
- 需要實時查詢
- 需要讀寫工具結果

---

## 常見坑

### 1. 把 JSON 設定翻譯掉

這會直接導致 MCP 無法載入。

### 2. 忘記匯出環境變數

設定檔案寫對了，Claude 也會因為 token 缺失而連不上。

### 3. 一上來就接很多服務

推薦先接最核心的一個，例如 GitHub 或 filesystem，確認跑通後再擴充套件。

---

## 推薦下一步

- 想讓 Claude 自動在關鍵時機跑腳本：看 [06-hooks](../06-hooks/)
- 想把 MCP 和 commands / agents 一起打包：看 [07-plugins](../07-plugins/)
- 想快速查常見設定：看 [QUICK_REFERENCE.md](../QUICK_REFERENCE.md)
