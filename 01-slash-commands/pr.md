---
description: 整理程式碼、暫存改動並準備 pull request
allowed-tools: Bash(git add:*), Bash(git status:*), Bash(git diff:*), Bash(npm test:*), Bash(npm run lint:*)
---

# Pull Request Preparation Checklist / PR 準備清單

在建立 PR 之前，請按下面步驟執行：

1. 跑 lint：`prettier --write .`
2. 跑測試：`npm test`
3. 檢查 diff：`git diff HEAD`
4. 暫存改動：`git add .`
5. 生成符合 conventional commits 的提交資訊：
   - `fix:` bug 修復
   - `feat:` 新功能
   - `docs:` 檔案變更
   - `refactor:` 程式碼重構
   - `test:` 測試補充
   - `chore:` 維護項
6. 輸出 PR 摘要，至少包括：
   - 改了什麼
   - 為什麼改
   - 做了哪些測試
   - 可能影響到什麼

要求：

- 先檢查是否有明顯不該提交的內容
- 優先讓使用者看到摘要和風險點
