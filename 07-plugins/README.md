<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../resources/logos/claude-howto-logo-dark.svg">
  <img alt="Claude How To" src="../resources/logos/claude-howto-logo.svg">
</picture>

# Plugins 指南

如果說 skills、hooks、MCP、subagents 分別是單項能力，那麼 plugins 就是把這些能力打包成“一整套可安裝方案”的方式。

對新手使用者來說，plugin 章節之所以重要，不只是因為它“高階”，而是因為它最接近團隊實際使用場景：一套命令、一套 agents、一套 hooks、一套外部整合，最好一次裝好、一次分發。

---

## plugin 是什麼

plugin 通常會組合這些內容：

- commands
- skills
- subagents
- hooks
- `.mcp.json`
- 輔助腳本與範本

所以它特別適合：

- 團隊統一工作流
- 跨專案複用
- 把一套最佳實踐做成可分發單元

---

## plugin 的價值到底在哪裡

當你已經有很多零散設定時，plugin 解決的是：

- 怎麼一次裝完整套能力
- 怎麼讓團隊成員取得一致設定
- 怎麼讓“個人技巧”變成“團隊資產”

如果你已經有單獨的 slash command、skill、subagent、hook 在工作，那麼下一步自然就是考慮是否要把它們打包。

---

## 基本結構

```text
my-plugin/
├── .claude-plugin/
│   └── plugin.json
├── commands/
├── agents/
├── skills/
├── hooks/
├── .mcp.json
├── scripts/
├── templates/
└── docs/
```

### 這些目錄分別做什麼

| 目錄 | 用途 |
|------|------|
| `.claude-plugin/plugin.json` | plugin manifest |
| `commands/` | 可直接呼叫的命令入口 |
| `agents/` | 子代理程式定義 |
| `skills/` | 自動觸發或複用能力 |
| `hooks/` | 自動化事件處理 |
| `.mcp.json` | 外部系統接入 |
| `scripts/` | 實際執行腳本 |
| `templates/` | 輸出範本 |

---

## manifest 結構與高風險欄位

plugin manifest 採用 JSON 格式，位置是：

```text
.claude-plugin/plugin.json
```

一個最小範例：

```json
{
  "name": "my-first-plugin",
  "description": "A greeting plugin",
  "version": "1.0.0",
  "author": {
    "name": "Your Name"
  },
  "license": "MIT"
}
```

### 這些 key 不要翻

- `name`
- `version`
- `description`
- `author`
- `license`

同樣，plugin 名稱本身也不要改成中文標識，否則會影響識別、安裝和後續同步維護。

---

## plugin 還有哪些可選能力

### 1. LSP 支援

plugin 可以透過 `.lsp.json` 或 manifest 中的 `lsp` 設定提供 LSP 支援。

適合：

- 語言診斷
- 跳轉定義
- symbol 瀏覽
- hover 資訊

### 2. 使用者設定項

某些 plugin 會暴露使用者可設定項，例如 API key、部署 region、開關引數。

### 3. 持久化資料

某些 plugin 會使用持久化目錄儲存快取、資料庫或狀態。

如果你在做團隊級 plugin，這三類能力很值得提前規劃。

---

## 本目錄裡的範例 plugins

| plugin | 用途 | 適合誰 |
|--------|------|--------|
| `pr-review` | PR 審查流程 | 程式碼審查較頻繁的團隊 |
| `documentation` | 檔案生成與同步 | 檔案經常落後的專案 |
| `devops-automation` | 部署、監控、事故處理 | 有穩定交付流程的團隊 |

### `pr-review`

把安全檢查、測試覆蓋檢查和效能影響分析整合進 PR 工作流。

### `documentation`

把 README、API docs、檔案同步和校驗整理成一套檔案工作流。

### `devops-automation`

把部署、回滾、狀態檢查和 incident 響應整合起來。

---

## 怎麼安裝

### Marketplace / 已釋出 plugin

```text
/plugin install pr-review
```

### 本機開發 plugin

如果你是在本機除錯自己寫的 plugin，一般會使用 Claude Code 支援的本機 plugin 目錄或測試方式。

### 從 Git 倉庫安裝

如果以後你把中文 plugin 釋出到自己的倉庫，建議在 README 中明確寫出：

- 倉庫地址
- 安裝方式
- 依賴條件
- 支援平臺

---

## 什麼時候值得做 plugin

### 值得做 plugin

- 你已經有多項能力要一起分發
- 團隊成員都要用
- 安裝過程需要足夠簡單
- 你希望工作流版本化

### 先別急著做 plugin

- 你還只有一個 command 或 skill
- 工作流還沒穩定
- 需求變化很快

這時通常先用單獨的 skills、hooks 或 agents 更合適。

---

## 設計一個好 plugin 的建議

### 1. 先確定“解決哪個完整場景”

不要只是把幾個檔案塞一起。好的 plugin 通常對應一個完整場景，例如：

- 程式碼審查
- 檔案維護
- 部署與事故處理

### 2. 明確依賴邊界

需要寫清楚：

- 外部服務依賴
- 必要的 token / env vars
- 所需 CLI
- 許可權需求

### 3. 不要把實驗性設定過早打包

plugin 一旦面向團隊分發，穩定性要求就會更高。

---

## 新手使用者特別注意

### 1. 外部服務依賴

plugin 裡經常帶有：

- GitHub
- Kubernetes
- 第三方 API
- 網路 webhook

不要預設這些服務在本機就能直接訪問。

### 2. token / CLI / 環境變數

釋出中文 plugin 時，建議 README 明確說明：

- 依賴哪些外部服務
- 需要哪些 token / CLI / 環境變數
- Windows / WSL 是否支援

### 3. 安裝方式別寫得太抽象

新手使用者最怕“概念都懂，但不知道下一步打什麼命令”。  
建議每個 plugin 至少給一個“最小安裝路徑”。

---

## 常見坑

### 1. 只改 README，不檢查 manifest

真正影響安裝和識別的是 `.claude-plugin/plugin.json`，不是說明文。

### 2. 過早打包

如果工作流還不穩定，plugin 只會增加維護負擔。

### 3. 把 plugin 名和命令名翻譯掉

這會直接影響呼叫、安裝和同步維護。

### 4. 沒寫清依賴

對新手使用者來說，這是導致“看起來很強但根本跑不起來”的高頻原因。

---

## Troubleshooting

如果 plugin 裝了但不好用，優先排查：

1. manifest 是否有效
2. 依賴的 commands / agents / hooks / MCP 是否都在正確目錄
3. 外部服務是否能訪問
4. 環境變數是否正確匯出
5. 外掛名稱空間和命令名是否保持英文原樣

---

## Best Practices

- 先跑通單項能力，再打包
- 保持 plugin 目標聚焦
- 在 README 中明確依賴和適用場景
- 不要為了中文化改壞 manifest 和命令標識
- 團隊釋出前先做一輪真實安裝演練

---

## 推薦下一步

- 想先理解單項能力：回看 [03-skills](../03-skills/)、[04-subagents](../04-subagents/)、[05-mcp](../05-mcp/)、[06-hooks](../06-hooks/)
- 想補高階工作流與許可權控制：看 [09-advanced-features](../09-advanced-features/)
