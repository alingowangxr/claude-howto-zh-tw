<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../resources/logos/claude-howto-logo-dark.svg">
  <img alt="Claude How To" src="../resources/logos/claude-howto-logo.svg">
</picture>

# Memory 指南

memory 是 Claude Code 中最容易被低估的一項能力。很多人覺得自己只是“加了個 `CLAUDE.md`”，實際上它影響的是 Claude 在每次進入專案時會自動帶上的長期上下文。

---

## memory 是什麼

Claude Code 的 memory 主要依賴檔案系統中的 `CLAUDE.md` 體系。你可以把它理解成：

- 專案規則入口
- 團隊約定入口
- 個人偏好入口
- 某個目錄下的區域性規則入口

它和“當前對話裡的臨時上下文”不同，memory 更像是長期生效的規則層。

---

## 什麼時候最該先配 memory

以下情況非常值得先配 `CLAUDE.md`：

- 你每次都要重複告訴 Claude 程式碼風格
- 團隊裡有固定約定，例如測試要求、命名規範、Git 流程
- 專案目錄複雜，希望 Claude 一進來就知道哪些目錄幹什麼
- 你想把一部分專案知識長期儲存下來，而不是每次重新解釋

---

## 高價值命令

| 命令 / 寫法 | 用途 |
|-------------|------|
| `/init` | 初始化專案 memory |
| `/memory` | 檢視或編輯 memory |
| `# your rule` | 快速把一句規則寫進 memory |
| `# remember this` | 用自然語言追加記憶 |
| `@README.md` | 在 `CLAUDE.md` 中引用外部檔案 |

---

## 最快上手方式

### 方法 1：直接複製專案範本

```bash
cp 02-memory/project-CLAUDE.md ./CLAUDE.md
```

### 方法 2：讓 Claude 幫你初始化

```text
/init
```

這通常適合新專案起步時使用。

### 方法 3：對話中快速寫入一條規則

```text
# Always run tests before commit
```

---

## 常見 memory 型別

### 專案級 memory

位置通常是：

- `./CLAUDE.md`
- 或 `.claude/CLAUDE.md`

適合放：

- 專案背景
- 目錄結構
- 技術堆疊
- 程式碼規範
- 測試規則
- 提交和 PR 規範

### 個人級 memory

位置通常是：

- `~/.claude/CLAUDE.md`

適合放：

- 你的個人編碼偏好
- 你習慣的回答風格
- 常用工具和命令約定

### 目錄級 memory

適合大型專案或 monorepo，在區域性目錄下放更細粒度規則。

---

## 寫什麼最有價值

新手最容易把 `CLAUDE.md` 寫成“泛泛而談的專案介紹”，這價值並不大。更推薦寫這些：

- 哪些目錄最重要
- 哪些規則最容易被忽略
- 提交前必須做什麼
- 哪些工具是本專案預設用法
- 哪些檔案不要亂動
- 測試和驗證的最低標準

---

## 一個適合初學者的最小範本

```md
# Project Memory

## Project Overview
- This is a TypeScript web application.

## Development Rules
- Run tests before commit.
- Prefer async/await.
- Keep API changes documented.

## Important Paths
- `src/` main application code
- `tests/` automated tests
- `docs/` documentation
```

---

## 哪些內容不適合寫進 memory

- 過長、每次都不一定相關的大段背景知識
- 會頻繁變化的實時資料
- 明顯更適合做成 skill 或 hook 的工作流細節
- 會影響執行的命令名或設定 key 的中文重新命名

如果你發現某段內容更像“流程範本”，通常更適合去做 skill，而不是塞進 `CLAUDE.md`。

---

## 新手使用者特別注意

- 如果你在 Windows 上工作，路徑規則和 shell 說明最好明確寫清楚。
- 如果專案依賴 `uv`、`npm`、`pnpm`、`bun` 等特定工具，也建議寫入 memory。
- 如果專案所在團隊有 GitHub、內網、代理程式、映象源要求，也值得寫在 memory 裡。

---

## 常見坑

### 1. 以為 memory 越長越好

不是。memory 要優先放高價值、長期穩定、對 Claude 行為影響大的規則。

### 2. 把專案規則和個人偏好全混在一起

推薦區分專案級和個人級，這樣更方便團隊協作。

### 3. 讓 `CLAUDE.md` 和實際倉庫脫節

如果專案目錄或規範已經變了，要及時更新 memory，否則 Claude 會學到過期規則。

---

## 推薦下一步

- 想做可複用工作流：看 [03-skills](../03-skills/)
- 想安全試錯：看 [08-checkpoints](../08-checkpoints/)
- 想看完整學習順序：看 [LEARNING-ROADMAP.md](../LEARNING-ROADMAP.md)
