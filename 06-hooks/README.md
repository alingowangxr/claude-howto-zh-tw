<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../resources/logos/claude-howto-logo-dark.svg">
  <img alt="Claude How To" src="../resources/logos/claude-howto-logo.svg">
</picture>

# Hooks 指南

hooks 是 Claude Code 的“事件觸發自動化”機制。它允許你在某些時機自動做點事情，例如：

- 調工具前先檢查風險
- 寫完檔案後自動格式化
- 提交前跑測試
- 結束前記錄日誌或上下文

如果你已經會 `slash commands` 和 `CLAUDE.md`，下一步最值得掌握的自動化能力通常就是 hooks。

---

## hooks 是什麼

你可以把 hook 理解成一條規則：

1. 某個事件發生
2. 匹配某個工具或場景
3. 自動執行一個動作

這些動作可以是：

- shell command
- HTTP webhook
- prompt 型判斷
- agent 型評估

hooks 最大的價值，是把“你本來每次都要手動做的檢查”變成自動流程。

---

## 常見設定位置

- `~/.claude/settings.json`：使用者級，對所有專案生效
- `.claude/settings.json`：專案級，適合團隊共享
- `.claude/settings.local.json`：本機專案設定，不建議提交
- plugin 內的 `hooks/hooks.json`
- 某些 skill / subagent frontmatter 內的 component-scoped hooks

如果你是新手，建議先從使用者級或專案級設定開始。

---

## 基本結構

```json
{
  "hooks": {
    "EventName": [
      {
        "matcher": "ToolPattern",
        "hooks": [
          {
            "type": "command",
            "command": "your-command-here",
            "timeout": 60
          }
        ]
      }
    ]
  }
}
```

### 關鍵欄位說明

| 欄位 | 作用 | 範例 |
|------|------|------|
| `hooks` | hook 頂層設定入口 | `{ "PreToolUse": [...] }` |
| `matcher` | 匹配工具名或模式 | `"Write"`、`"Edit|Write"`、`"*"` |
| `type` | hook 型別 | `"command"`、`"http"`、`"prompt"`、`"agent"` |
| `command` | 執行的 shell 命令 | `"$CLAUDE_PROJECT_DIR/.claude/hooks/format.sh"` |
| `timeout` | 超時秒數 | `30` |
| `once` | 每會話只跑一次 | `true` |

> **注意**：這些欄位屬於設定協議的一部分，不要為了中文化把它們翻掉。

---

## matcher 怎麼用

| 形式 | 含義 | 範例 |
|------|------|------|
| 精確匹配 | 只匹配某個工具 | `"Write"` |
| 正則匹配 | 匹配多個工具 | `"Edit|Write"` |
| 全匹配 | 匹配全部工具 | `"*"` 或 `""` |
| MCP 工具模式 | 匹配 MCP 工具 | `"mcp__memory__.*"` |

如果你不確定先配什麼，最常見的起點是：

- `Bash`
- `Write`
- `Edit|Write`

---

## 四種 hook 型別

### 1. `command`

最常見的型別。適合：

- shell 校驗
- 安全掃描
- 自動格式化
- 日誌記錄

```json
{
  "type": "command",
  "command": "python3 \"$CLAUDE_PROJECT_DIR/.claude/hooks/validate.py\"",
  "timeout": 60
}
```

### 2. `http`

適合把事件發給 webhook 或外部系統。

```json
{
  "type": "http",
  "url": "https://example.com/hook"
}
```

常見用途：

- 通知系統
- 團隊訊息流
- 外部審計系統

### 3. `prompt`

讓模型根據 prompt 判斷是否該繼續，常見於：

- 任務完成檢查
- 結束前品質判斷
- prompt 合規性判斷

### 4. `agent`

讓 Claude 用獨立 agent 做更復雜的評估，適合：

- 架構規則檢查
- 多步驗證
- 比較複雜的品質門禁

---

## 常見事件

當前最值得先掌握的事件：

| 事件 | 什麼時候觸發 | 最常見用途 |
|------|--------------|------------|
| `PreToolUse` | 工具執行前 | 校驗、阻止、改輸入 |
| `PostToolUse` | 工具執行後 | 驗證、補上下文、記錄 |
| `UserPromptSubmit` | 使用者提交 prompt 時 | prompt 校驗 |
| `Stop` / `SubagentStop` | Claude / subagent 結束時 | 完成度判斷 |
| `SessionStart` / `SessionEnd` | 會話開始 / 結束 | 初始化、清理、日誌 |

更完整的生態還包括：

- `PermissionRequest`
- `PostToolUseFailure`
- `Notification`
- `TaskCreated`
- `TaskCompleted`
- `CwdChanged`
- `WorktreeCreate`
- `WorktreeRemove`

如果你是新手，不需要一上來把所有事件都學完。

---

## 最實用的三個起步場景

### 場景 1：提交前跑測試

這是最容易感受到 hooks 價值的起點。

```bash
mkdir -p ~/.claude/hooks
cp 06-hooks/pre-commit.sh ~/.claude/hooks/
chmod +x ~/.claude/hooks/pre-commit.sh
```

常見設定思路：

- 監聽 `PreToolUse`
- matcher 設為 `Bash`
- 在腳本裡判斷是否是 `git commit`

### 場景 2：寫完檔案自動格式化

適合在 `PostToolUse` + `Write|Edit` 場景下做程式碼格式化或輕量校驗。

### 場景 3：安全掃描

適合在檔案修改後，自動掃明顯危險模式，例如 secrets、危險命令或敏感字串。

---

## hook 的輸入輸出是怎麼工作的

### 輸入

hooks 通常透過 `stdin` 接收 JSON 輸入。

### 輸出

可以透過：

- exit code
- stdout JSON

把結果回饋回 Claude。

常見控制方式包括：

- `allow`
- `deny`
- `ask`
- `updatedInput`
- `additionalContext`

如果你只是在做簡單 shell 檢查，先把“成功返回 0，失敗返回非 0”跑通就夠了。

---

## 本目錄範例腳本怎麼用

| 檔案 | 用途 | 適合什麼時候先試 |
|------|------|------------------|
| `pre-commit.sh` | 提交前跑測試 | 第一個推薦範例 |
| `format-code.sh` | 自動格式化 | 寫程式碼後自動收尾 |
| `security-scan.sh` | 安全掃描 | 團隊規範較嚴格時 |
| `validate-prompt.sh` | prompt 校驗 | 控制輸入品質 |
| `log-bash.sh` | 記錄命令使用 | 做審計或追蹤 |
| `notify-team.sh` | 通知團隊 | 配合外部訊息系統 |
| `context-tracker.py` | 上下文追蹤 | 除錯長會話問題 |

---

## 關於 `auto-adapt-mode` 的更新

如果你之前看過舊資料，可能見過一種思路：

- 在 `PostToolUse` 裡記錄你核准過的命令
- 自動把這些核准“泛化”進本機許可權設定

上游最近已經把這條路線下掉了，不再推薦繼續使用舊的：

- `06-hooks/auto-adapt-mode.py`

新的建議方式是：

- 使用一次性腳本 `09-advanced-features/setup-auto-mode-permissions.py`
- 直接把一組更保守、更可控的許可權規則寫進 `~/.claude/settings.json`
- 再透過命令列引數按需放開 edits、tests、git writes、package installs、GitHub write 等能力

這樣做的好處是：

- 不再依賴“邊用邊學你的核準”
- 設定更可預測
- 更適合團隊分享和審閱
- 對新手使用者來說，也更容易解釋“當前到底開了哪些許可權”

如果你在意 Auto Mode 但又沒有 Team plan，優先看：

- [09-advanced-features/README.md](../09-advanced-features/README.md)

---

## hooks 設定裡哪些絕對不能翻

- `hooks`
- `matcher`
- `type`
- `command`
- `timeout`
- 事件名，例如 `PreToolUse`
- JSON key
- 實際命令列片段

可以翻譯：

- 註釋
- 使用說明
- README 正文

不能翻譯：

- 協議欄位
- 事件名
- 命令

---

## 新手使用者特別注意

### 1. shell 差異

很多範例預設更偏 Unix / macOS / Linux 風格。  
Windows 使用者請先確認你當前用的是：

- PowerShell
- Git Bash
- WSL

### 2. 環境依賴

如果 hook 裡呼叫：

- `python`
- `node`
- `uv`
- `npm`
- `pytest`

請先確認本機路徑和環境變數，否則“設定看起來對，執行卻沒效果”非常常見。

### 3. 網路與代理程式

如果 hook 會發 HTTP 請求，記得考慮：

- 公司代理程式
- TLS 證書
- 外部服務可訪問性

---

## debugging 和排錯思路

如果 hook 沒生效，優先按這個順序排查：

1. 事件名是否正確
2. `matcher` 是否匹配到了目標工具
3. 路徑是否正確
4. 腳本是否可執行
5. 腳本內部依賴是否存在
6. stdout / exit code 是否符合預期

如果 hook 觸發了但效果不對，重點看：

- 命令是否真的執行成功
- 你的 hook 是否過重、太慢
- 是否在錯誤事件上繫結了錯誤的邏輯

---

## Best Practices

- 從一個輕量 hook 開始，不要一口氣加很多
- 優先做“高頻、確定、低風險”的自動動作
- 不要讓 hook 變成新的複雜系統
- 先讓 hook 穩，再考慮把它放進 plugin
- 對新手使用者來說，環境說明和 shell 差異提示非常重要

---

## 推薦下一步

- 想做自動觸發的複用能力：看 [03-skills](../03-skills/)
- 想接入外部系統：看 [05-mcp](../05-mcp/)
- 想把一整套流程打包分發：看 [07-plugins](../07-plugins/)
