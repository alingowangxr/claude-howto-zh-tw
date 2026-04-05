---
description: 暫存全部改動、提交併推送到遠端（高風險操作，謹慎使用）
allowed-tools: Bash(git add:*), Bash(git status:*), Bash(git commit:*), Bash(git push:*), Bash(git diff:*), Bash(git log:*), Bash(git pull:*)
---

# Commit and Push Everything / 全量提交併推送

⚠️ **CAUTION**：這個命令會把當前工作區裡的全部改動一起提交併推送。只有在你確認這些改動應該放在同一個 commit 裡時才使用。

## Workflow

### 1. 先分析改動

並行檢視：

- `git status`
- `git diff --stat`
- `git log -1 --oneline`

### 2. 安全檢查

如果發現下面這些問題，必須停止並明確警告：

- secrets：`.env*`、`*.key`、`*.pem`、`credentials.json`、`id_rsa`
- 真正的 API key / token
- 大檔案（例如 >10MB）
- 構建產物：`node_modules/`、`dist/`、`build/`、`.venv/`
- 臨時檔案：`.DS_Store`、`*.tmp`、`*.swp`

### 3. 請求確認

在真正執行前，先給出摘要並等待使用者明確輸入 `yes`。

### 4. 執行

```bash
git add .
git status
```

### 5. 生成提交資訊

使用 conventional commits，格式如下：

```text
[type]: Brief summary

- Key change 1
- Key change 2
- Key change 3
```

### 6. 提交併推送

```bash
git commit -m "..."
git push
```

如推送失敗，可提示：

- `git pull --rebase && git push`
- `git push -u origin [branch]`

### 7. 確認成功

輸出：

- commit hash
- branch
- files changed

## When to Use

✅ 適合：

- 檔案大改
- 一次完整功能交付
- 明確屬於同一主題的多檔案修改

❌ 不適合：

- 改動來源不清
- 有 secrets 風險
- 你其實想要更細粒度 commit
- 當前分支是受保護分支
