# Lesson Quiz

> 針對單個 Claude Code lesson 的互動測驗 skill。它不只是隨便出幾道題，而是會按 lesson 組織題面、給出評分、錯題解釋、複習建議和後續動作。

## Highlights

- 每次固定 8 題
- 覆蓋 10 個 lesson
- 支援學前、學中、學後三種測驗時機
- 每道錯題都會給出解釋和建議回看的章節
- 會給出總分、等級判斷和下一步建議

## 什麼時候用

| 你可以這樣說 | 它會做什麼 |
|---|---|
| “幫我測一下 hooks” | 做一輪 `06-hooks` 相關測驗 |
| “我會不會 MCP” | 測 `05-mcp` 的理解程度 |
| “來個 lesson quiz” | 讓你先選 lesson，再開始測 |
| “測試我對 skills 的理解” | 直接進入 `03-skills` 測驗 |

## 使用方式

```text
/lesson-quiz [lesson-name-or-number]
```

例如：

```text
/lesson-quiz hooks
/lesson-quiz 03
/lesson-quiz advanced-features
/lesson-quiz
```

## 輸出內容

### 1. 總分與等級

- 例如 `7/8 — Proficient`

### 2. 每題結果

- 哪些答對
- 哪些答錯
- 概念題 / 實踐題表現如何

### 3. 錯題解釋

對每個答錯的問題，給出：

- 你選了什麼
- 正確答案是什麼
- 為什麼正確答案更合理
- 建議回看 lesson 的哪一節

### 4. 後續動作

測完後可以繼續：

- 重測當前 lesson
- 切到另一課
- 讓 Claude 詳細解釋某道錯題
