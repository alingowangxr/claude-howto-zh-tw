# Changelog

> 本檔案保留上游版本資訊的時間順序，但用中文補充閱讀說明，方便中文使用者快速判斷“這個倉庫最近同步了什麼”。

## 中文版同步 — 2026-04-01

### Upstream Sync

- 同步上游範圍：`d41b335` → `0ca8c37`
- 核心變化：
  - hooks 不再推薦舊的 `auto-adapt-mode` 動態學習方案
  - 新增一次性許可權種子腳本 `09-advanced-features/setup-auto-mode-permissions.py`
  - auto-mode 許可權基線改為更保守的預設集合，並支援按需開啟 edits、tests、git writes、packages、GitHub writes
  - 上游 `README` 新增 Trending 徽章

### Chinese Fork Handling

- 刪除本倉庫中的舊 `06-hooks/auto-adapt-mode.py`
- 在 `06-hooks/README.md` 和 `09-advanced-features/README.md` 中補上新的中文說明
- 在 `README.md` 中加入最近同步日期與更新內容說明
- 未直接照搬上游 Trending 徽章，以避免誤導為當前中文 fork 的真實熱度狀態

## v2.2.0 — 2026-03-26

### Documentation

- 將全部教學和參考檔案同步到 Claude Code `v2.1.84`
  - slash commands 更新為 55+ 個內建命令 + 5 個 bundled skills，並標記 3 個已廢棄項
  - hooks 事件從 18 個擴充套件到 25 個，並新增 `agent` hook type
  - advanced features 新增 Auto Mode、Channels、Voice Dictation
  - `SKILL.md` frontmatter 新增 `effort`、`shell`
  - subagent 欄位新增 `initialPrompt`、`disallowedTools`
  - MCP 新增 WebSocket transport、elicitation、2KB tool cap 等說明
  - plugins 新增 LSP、`userConfig`、`${CLAUDE_PLUGIN_DATA}` 相關支援
  - 更新 `CATALOG`、`QUICK_REFERENCE`、`LEARNING-ROADMAP`、`INDEX`
- README 改寫為更像 landing page 的結構

### Bug Fixes

- 為 CI 補充缺失的 cSpell 詞條和 README 章節
- 在 cSpell 詞典中加入 `Sandboxing`

**Full Changelog**: https://github.com/luongnv89/claude-howto/compare/v2.1.1...v2.2.0

---

## v2.1.1 — 2026-03-13

### Bug Fixes

- 刪除導致連結檢查失敗的無效 marketplace 連結
- 在 cSpell 詞典中補充 `sandboxed` 和 `pycache`

**Full Changelog**: https://github.com/luongnv89/claude-howto/compare/v2.1.0...v2.1.1

---

## v2.1.0 — 2026-03-13

### Features

- 新增自適應學習路徑、自測和課後測驗相關 skills
  - `/self-assessment`：對 10 個能力域做互動式自測並給出個性化學習路徑
  - `/lesson-quiz [lesson]`：針對單個模組做 8-10 題知識檢查

### Bug Fixes

- 更新失效 URL、已廢棄寫法和過時引用
- 修復資源檔案和自測 skill 裡的壞鏈
- 將概念指南中的巢狀程式碼塊改為波浪線 fence
- 增補 cSpell 詞典缺失詞條

### Documentation

- 修正檔案裡的術語、URL 和一致性問題
- 完成缺失能力覆蓋與參考檔案補齊
- 在 MCP 章節加入 MCPorter 執行時說明
- 補充缺失命令、設定項和特性說明
- 新增風格指南
- 將自測和 lesson-quiz 引入 README 與路線圖

### New Contributors

- `@VikalpP` 首次貢獻

**Full Changelog**: https://github.com/luongnv89/claude-howto/compare/v2.0.0...v2.1.0

---

## v2.0.0 — 2026-02-01

### Features

- 將檔案整體同步到 2026 年 2 月的 Claude Code 能力集
  - 新增 Auto Memory
  - 新增 Remote Control、Web Sessions、Desktop App
  - 新增 Agent Teams（實驗性）
  - 新增 MCP OAuth 2.0、Tool Search、Claude.ai Connectors
  - 新增 subagents 的 persistent memory 與 worktree isolation
  - 新增 background subagents、task list、prompt suggestions
  - 新增 sandboxing 與 managed settings
  - 新增 HTTP hooks 和 7 個新事件
  - 新增 plugin settings、LSP、marketplace 相關說明
  - 補充 checkpoints 的 summarize from checkpoint
  - 補充 17 個新 slash commands
  - 補充一批新 CLI flags 和環境變數

### Design

- 重做 logo，改為更簡潔的視覺設計

### Bug Fixes / Corrections

- 更新模型名：Sonnet 4.5 → Sonnet 4.6，Opus 4.5 → Opus 4.6
- 修正 permission mode 名稱
- 修正 hooks 事件名
- 修正 CLI 寫法：`claude-code --headless` → `claude -p`
- 修正 checkpoint 命令範例
- 修正 session 管理命令
- 修正 plugin manifest：`plugin.yaml` → `.claude-plugin/plugin.json`
- 修正 MCP 設定路徑
- 修正檔案 URL，並刪除虛構地址
- 移除多個虛構設定欄位

**Full Changelog**: https://github.com/luongnv89/claude-howto/compare/20779db...v2.0.0
