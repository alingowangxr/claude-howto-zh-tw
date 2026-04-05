<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../resources/logos/claude-howto-logo-dark.svg">
  <img alt="Claude How To" src="../resources/logos/claude-howto-logo.svg">
</picture>

# Skills 指南

skills 是 Claude Code 裡最值得認真掌握的能力之一。它們讓 Claude 不再只是“每次重新聽你描述要求”，而是能在合適場景下自動拿出一套固定工作流、範本和最佳實踐。

---

## skills 是什麼

你可以把 skill 理解成：

- 一個帶 frontmatter 的 `SKILL.md`
- 可附帶腳本、範本、參考資料
- 會被 Claude 自動發現和按需載入
- 更適合長期複用的工作流能力

和普通 prompt 相比，skills 更穩定、更易複用，也更適合團隊共享。

---

## skills 為什麼重要

當你開始頻繁做這些事時，skills 的價值就非常明顯：

- 程式碼審查
- 檔案生成
- 程式碼重構
- 品牌語氣統一
- 專案初始化或規範生成

如果每次都靠你手打一大段提示詞，既累，也不穩定。skill 的目標就是把這部分沉澱下來。

---

## 一個 skill 的基本結構

```text
skill-name/
├── SKILL.md
├── templates/
├── scripts/
└── references/
```

### `SKILL.md` 負責什麼

- 定義 skill 名稱
- 說明 skill 在什麼情況下應該觸發
- 告訴 Claude 該怎麼做

### 其他目錄負責什麼

- `templates/`：輸出範本
- `scripts/`：輔助腳本
- `references/`：參考規則或背景知識

---

## progressive disclosure 是什麼意思

skills 的一個核心優點是按需載入，而不是一上來把所有內容都塞進上下文裡。

簡單理解：

1. Claude 先只知道有哪些 skills，以及它們大概幹什麼
2. 真正需要某個 skill 時，再讀取 `SKILL.md`
3. 只有在需要時，才進一步讀範本、腳本或參考資料

這意味著你可以裝很多 skills，而不會一開始就把上下文塞爆。

---

## skills 放哪裡

| 型別 | 路徑 | 適合什麼 |
|------|------|----------|
| 個人級 | `~/.claude/skills/<skill-name>/SKILL.md` | 個人工作流 |
| 專案級 | `.claude/skills/<skill-name>/SKILL.md` | 團隊共享 |
| plugin 自帶 | `<plugin>/skills/...` | 和 plugin 一起分發 |

---

## 本目錄裡的範例 skills

| skill | 位置 | 用途 |
|-------|------|------|
| `code-review` | `03-skills/code-review/` | 程式碼審查 |
| `brand-voice` | `03-skills/brand-voice/` | 文案風格統一 |
| `doc-generator` | `03-skills/doc-generator/` | 檔案生成 |
| `refactor` | `03-skills/refactor/` | 結構化重構 |
| `claude-md` | `03-skills/claude-md/` | 生成或調整 `CLAUDE.md` |

---

## 如何安裝

### 安裝到個人目錄

```bash
mkdir -p ~/.claude/skills
cp -r 03-skills/code-review ~/.claude/skills/
```

### 安裝到專案目錄

```bash
mkdir -p .claude/skills
cp -r 03-skills/code-review .claude/skills/
```

---

## `SKILL.md` 裡哪些不能翻

這點是在地化時最容易翻壞的地方。下面這些欄位要保留原樣：

- `name`
- `description`
- `effort`
- `shell`

同時，skill 名稱本身也不要擅自中文化改名。

---

## skills 和 slash commands 的區別

### 更適合用 skill 的情況

- 你希望 Claude 自動判斷什麼時候該觸發
- 你需要附帶範本、腳本、參考資料
- 這是一個長期工作流，而不是一次性快捷命令

### 更適合用 slash command 的情況

- 你希望自己手動明確觸發
- 它更像一個短促的操作入口
- 你希望使用者一眼知道“我要輸入哪個命令”

---

## 如何寫出更好用的 skill

- `description` 要具體，不要空泛
- 一個 skill 聚焦一類問題，別做成“大雜燴”
- 如果依賴腳本或範本，放進 skill 目錄，不要散落各處
- 優先寫“什麼時候觸發”和“輸出長什麼樣”

---

## 常見坑

### 1. description 寫得太泛

Claude 就不知道什麼時候該用它，或者會誤觸發。

### 2. 把 skill 寫成一大段散文

推薦寫成結構化說明，讓 Claude 更容易執行。

### 3. 把 frontmatter key 翻譯掉

這會直接讓 skill 無法正確解析。

---

## 新手使用者特別注意

- skill 裡如果呼叫 shell 腳本，先確認本機 shell 環境。
- 如果腳本依賴 `python`、`node`、`uv`、`npm`，建議在 skill 說明裡提前寫明。
- Windows 使用者優先考慮 PowerShell / Git Bash / WSL 差異。

---

## 推薦下一步

- 想讓任務分工更專業：看 [04-subagents](../04-subagents/)
- 想在工具呼叫前後做自動動作：看 [06-hooks](../06-hooks/)
- 想繼續用中文規範擴寫：看 [LOCALIZATION-STYLE.md](../LOCALIZATION-STYLE.md)
