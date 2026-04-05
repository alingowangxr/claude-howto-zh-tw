---
allowed-tools: Bash(git add:*), Bash(git status:*), Bash(git commit:*), Bash(git diff:*)
argument-hint: [message]
description: 基於當前改動生成並執行一次 git commit
---

# Commit / 提交改動

## Context

- 當前 git 狀態：!`git status`
- 當前 diff：!`git diff HEAD`
- 當前分支：!`git branch --show-current`
- 最近提交：!`git log --oneline -10`

## Your task

請基於以上改動建立一次單獨的 git commit。

如果使用者透過引數傳入了 message，直接使用：`$ARGUMENTS`

否則，請分析改動並生成一條符合 conventional commits 的提交資訊：

- `feat:` 新功能
- `fix:` 修復 bug
- `docs:` 檔案改動
- `refactor:` 重構
- `test:` 新增或調整測試
- `chore:` 雜項維護

提交資訊要：

- 準確概括這次改動
- 儘量簡潔
- 不要編造未發生的內容
