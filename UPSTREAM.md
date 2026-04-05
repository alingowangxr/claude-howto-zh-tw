# Upstream & Fork Notes

## 上游來源

- 上游倉庫：[`luongnv89/claude-howto`](https://github.com/luongnv89/claude-howto)
- 上游分支：`main`
- 在地化基線 commit：`0ca8c37c81918458e063739425c4740ca92c2db2`
- 上游許可證：[MIT License](LICENSE)

## 本倉庫性質

本倉庫是一個 **非官方繁體中文化 fork**，目標是面向初學者使用者重寫 Claude Code 學習材料，同時儘量保持與上游結構、範例和執行行為相容。

它不是：

- 官方 Anthropic 檔案
- 上游倉庫的逐字逐句翻譯映象
- 為臺灣平臺完全重構後的獨立產品

## 本倉庫做了哪些調整

- 把首頁、學習路線、Quick Reference、Catalog 等核心入口檔案改成中文主線。
- 用“先講用途，再講安裝，再講範例和常見坑”的方式重寫表達。
- 保留目錄結構、檔案路徑、命令名、frontmatter key、JSON/YAML key、環境變數、CLI flags 等關鍵相容元素。
- 增加新手使用者常見障礙說明，例如 GitHub Token、`npm` / `npx` / `uv` / Python 環境、網路與代理程式、Windows / WSL 差異。
- 增加在地化校驗腳本與 CI 護欄，避免翻譯把範例和設定改壞。

## 在地化原則

1. **相容性優先**  
   任何會影響 Claude Code 執行、載入或複製執行的標識，預設不翻。

2. **中文表達優先**  
   給人看的說明文字、學習路徑、FAQ、對比表、導語等內容，以中文重寫為主。

3. **術語保真**  
   `skills`、`CLI`、`hooks`、`MCP`、`subagents` 這類高頻術語保留英文，首次出現補中文解釋。

4. **持續同步**  
   本倉庫預設採用“跟進上游版本 -> 判定受影響檔案 -> 更新中文內容 -> 記錄處理結果”的維護方式。

## 推薦同步流程

1. 獲取上游新版本或新 commit。
2. 列出上游變更的檔案範圍。
3. 判斷哪些檔案影響本倉庫的中檔案案、範例或校驗腳本。
4. 優先同步以下型別的變化：
   - 命令名、欄位名、協議名、路徑約定
   - 新增或廢棄功能
   - 影響複製可執行性的範例變更
5. 更新中檔案案後，執行：

```bash
uv run python scripts/validate_localization.py
```

6. 在提交說明或更新日誌中記錄：
   - 上游變更點
   - 本倉庫採取了什麼處理
   - 哪些內容暫時未同步

## 最近一次同步記錄

### Upstream Sync — 2026-04-01

- Upstream range: `d41b335` → `0ca8c37`
- Affected files:
  - `06-hooks/README.md`
  - `06-hooks/auto-adapt-mode.py`
  - `09-advanced-features/README.md`
  - `09-advanced-features/setup-auto-mode-permissions.py`
  - `README.md`
- Chinese fork actions:
  - 刪除舊的 `auto-adapt-mode` hook 檔案，不再繼續維護“動態記憶核准”方案
  - 新增 `09-advanced-features/setup-auto-mode-permissions.py`，同步上游的一次性許可權種子腳本
  - 在中文 `Advanced Features` 和 `Hooks` 檔案中補上新的使用方式、適用場景和安全邊界
  - 在專案介紹中寫明最近同步日期與本次上游更新內容
  - 上游新增的 Trending 徽章未直接照搬，因為它描述的是上游倉庫狀態，而不是當前中文 fork 的狀態

## 建議記錄範本

```md
## Upstream Sync - YYYY-MM-DD

- Upstream range: <old>...<new>
- Affected files:
  - README.md
  - 05-mcp/README.md
- Chinese fork actions:
  - 同步了 MCP 章节新增字段说明
  - 保留了命令名与 JSON key 不变
  - 补充了台灣用户的安装注意事项
```

## 額外說明

- 如果你未來將本倉庫釋出到自己的 GitHub 賬號下，建議倉庫名使用 `claude-howto-zh-tw`。
- 如果需要替換徽章、封面圖、倉庫 URL，請在保留來源宣告的前提下調整。
- 如果某處翻譯和可執行性衝突，**優先保留原始標識**，並在正文中補中文解釋。
