---
name: lesson-quiz
version: 1.0.0
description: Claude Code 單模組互動測驗。Use when asked to "quiz me on hooks", "test my knowledge of lesson 3", "lesson quiz", "practice quiz for MCP", "do I understand skills", or similar Chinese requests.
---

# Lesson Quiz

這是一個針對單個 Claude Code lesson 的完整互動測驗 skill，用於檢查使用者對某一課的理解程度。

## Instructions

### Step 1: 確認 lesson

如果使用者提供了引數，就對映到 lesson 目錄：

- `01` / `slash-commands` / `commands` → `01-slash-commands`
- `02` / `memory` → `02-memory`
- `03` / `skills` → `03-skills`
- `04` / `subagents` / `agents` → `04-subagents`
- `05` / `mcp` → `05-mcp`
- `06` / `hooks` → `06-hooks`
- `07` / `plugins` → `07-plugins`
- `08` / `checkpoints` → `08-checkpoints`
- `09` / `advanced-features` / `advanced` → `09-advanced-features`
- `10` / `cli` → `10-cli`

如果使用者沒提供引數，使用 AskUserQuestion 分 2-3 輪讓使用者選擇 lesson。

---

### Step 2: 讀取 lesson 與題庫

先讀取：

- `<lesson-directory>/README.md`
- `references/question-bank.md`

優先使用題庫中該 lesson 的預置題。  
如果題庫不足 8 題，可根據 lesson README 補充生成，但必須保持與 lesson 內容一致。

---

### Step 3: 詢問測驗時機

用 AskUserQuestion 詢問使用者當前是在：

1. `Before (pre-test)`
2. `During (progress check)`
3. `After (mastery check)`

不同 timing 會影響結果解讀。

---

### Step 4: 出題

- 每次固定 8 題
- 每輪 2 題，共 4 輪
- 混合概念題和實踐題
- 每題使用 AskUserQuestion，提供 3-4 個選項

每題必須包含這些資訊：

- `category`
- `question`
- `options`
- `correct`
- `explanation`
- `review`

記錄使用者答案，最後統一評分。

---

### Step 5: 評分與結果輸出

每題答對記 1 分，總分 8 分。

等級：

- 8：Mastered
- 6-7：Proficient
- 4-5：Developing
- 2-3：Beginning
- 0-1：Not yet

輸出格式必須包含：

```markdown
## Lesson Quiz Results: [Lesson Name]

**Score: N/8** — [Grade]
**Quiz timing**: [Before / During / After]
**Question breakdown**: N conceptual correct, N practical correct

### Per-Question Results
| # | Category | Question (short) | Your Answer | Result |

### Incorrect Answers — Review These
**Q[N]: [Question]**
- Your answer:
- Correct answer:
- Explanation:
- Review:

### Timing-specific message
[根據 pre-test / progress check / mastery check 給不同反饋]

### Recommended Next Steps
- [繼續下一課 / 回看哪一節 / 重測 / 深入解釋]
```

---

### Step 6: 根據 timing 解釋結果

#### If pre-test

- 把成績解釋為“學習前基線”
- 強呼叫戶接下來應重點關注哪些主題

#### If during

- 把成績解釋為“階段性進度檢查”
- 明確哪些點已經掌握、哪些點要補

#### If after

- 把成績解釋為“lesson mastery check”
- 如果分數高，建議進入下一課
- 如果分數一般，列出明確回看點

---

### Step 7: 提供後續動作

最後再用 AskUserQuestion 讓使用者選擇：

1. `Retake this quiz`
2. `Quiz another lesson`
3. `Explain a topic I missed`
4. `Done`

如果選第三項，先問錯題編號，再讀取該 lesson README 的相關部分，用中文解釋並給範例。

## Output Requirements

- 中文表達清晰
- 保留關鍵英文術語
- 錯題解釋必須具體
- 複習建議要明確到 lesson 或章節
- 不要把測驗做成泛泛聊天
