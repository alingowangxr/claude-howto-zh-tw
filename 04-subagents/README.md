<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../resources/logos/claude-howto-logo-dark.svg">
  <img alt="Claude How To" src="../resources/logos/claude-howto-logo.svg">
</picture>

# Subagents 指南

subagents 是 Claude Code 裡做複雜任務拆分的關鍵能力。你可以把它理解成“主 Claude 把某個子任務交給一個更專業、上下文更獨立的助手去做”。

---

## subagents 是什麼

subagent 具備這些特點：

- 有自己的角色定位
- 有自己的上下文視窗
- 可以限制可用工具
- 可以使用單獨的 system prompt
- 適合做任務拆分和專業分工

它不是簡單的“再開一個對話”，而是 Claude Code 的正式能力機制。

---

## 什麼時候值得用 subagents

非常適合：

- 大型程式碼審查
- 安全審查
- 測試策略分析
- 檔案生成
- 除錯與根因定位
- 多條線並行處理

不太適合：

- 單檔案的小改動
- 簡單解釋性問題
- 只需要幾步就能完成的輕任務

---

## subagents 的核心價值

| 價值 | 說明 |
|------|------|
| 上下文隔離 | 避免主對話被複雜細節汙染 |
| 專業分工 | 不同 agent 做不同任務 |
| 工具隔離 | 可以限制某個 agent 能做什麼 |
| 可複用 | 適合團隊共享常用角色 |

---

## 檔案放哪裡

| 型別 | 路徑 | 作用域 |
|------|------|--------|
| 專案級 | `.claude/agents/` | 當前專案 |
| 使用者級 | `~/.claude/agents/` | 所有專案 |
| plugin 自帶 | plugin 的 `agents/` 目錄 | 隨 plugin 啟用 |

---

## 檔案格式長什麼樣

subagent 檔案通常是：

1. YAML frontmatter
2. 後面跟 Markdown 形式的 system prompt

一個典型結構如下：

```yaml
---
name: code-reviewer
description: Review recent changes for quality issues
tools: Read, Grep, Glob, Bash
model: inherit
---
```

---

## frontmatter 裡這些欄位不要翻

- `name`
- `description`
- `tools`
- `model`
- `effort`
- `permissionMode`
- `skills`
- `mcpServers`

如果你是做中文字地化，這些欄位要保真；可以翻譯的是下面真正給人看的 system prompt 正文。

---

## 本目錄裡的範例 subagents

| 名稱 | 檔案 | 用途 |
|------|------|------|
| `code-reviewer` | `code-reviewer.md` | 程式碼審查 |
| `clean-code-reviewer` | `clean-code-reviewer.md` | Clean Code 角度審查 |
| `test-engineer` | `test-engineer.md` | 測試覆蓋與測試策略 |
| `documentation-writer` | `documentation-writer.md` | 檔案生成 |
| `secure-reviewer` | `secure-reviewer.md` | 安全檢查 |
| `implementation-agent` | `implementation-agent.md` | 功能實現 |
| `debugger` | `debugger.md` | 錯誤除錯與根因定位 |
| `data-scientist` | `data-scientist.md` | 資料分析與 SQL 任務 |

---

## 如何安裝

```bash
mkdir -p .claude/agents
cp 04-subagents/*.md .claude/agents/
```

或者安裝單個：

```bash
cp 04-subagents/code-reviewer.md .claude/agents/
```

---

## 如何決定要不要拆成 subagents

### 推薦拆

- 任務本身可以天然分工
- 某個子任務需要單獨工具許可權
- 某個子任務需要更專門的 system prompt
- 你希望並行推進多個分析方向

### 不推薦拆

- 任務太小
- 子任務之間高度耦合、必須反覆共享細節
- 你自己還沒想清楚主任務是什麼

---

## 常見坑

### 1. subagent 角色太模糊

如果 description 太空，Claude 就不知道什麼時候該委派給它。

### 2. 工具給太多或太少

- 給太多：失去隔離價值
- 給太少：agent 做不了事

### 3. 直接把中文翻譯寫進欄位名

像 `tools`、`model`、`name` 這些不能翻。

---

## 新手使用者特別注意

- 如果 subagent 需要呼叫 shell，先確認 shell 環境。
- 如果某個 agent 依賴 Git、Python、Node、資料庫 CLI 等工具，最好在正文裡寫清依賴。
- Windows 環境下尤其要提前確認路徑和命令相容性。

---

## 推薦下一步

- 想讓 Claude 連線外部系統：看 [05-mcp](../05-mcp/)
- 想做自動檢查和自動觸發：看 [06-hooks](../06-hooks/)
- 想打包成團隊工作流：看 [07-plugins](../07-plugins/)
