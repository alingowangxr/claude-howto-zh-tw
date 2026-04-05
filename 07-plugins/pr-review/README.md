<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../../resources/logos/claude-howto-logo-dark.svg">
  <img alt="Claude How To" src="../../resources/logos/claude-howto-logo.svg">
</picture>

# PR Review 外掛

把安全檢查、測試檢查、效能檢查和 PR 審查打包成一套工作流。

## Features

- 安全分析
- 測試覆蓋檢查
- 檔案檢查
- 程式碼品質審查
- 效能影響分析

## Installation

```bash
/plugin install pr-review
```

## What's Included

### Commands

- `/review-pr`
- `/check-security`
- `/check-tests`

### Agents

- `security-reviewer`
- `test-checker`
- `performance-analyzer`

## Requirements

- Git 倉庫
- GitHub 訪問
- 必要時設定 `GITHUB_TOKEN`

## 最小設定

```bash
export GITHUB_TOKEN="your_github_token"
```

如果你當前機器無法穩定訪問 GitHub，這個 plugin 的體驗會明顯受影響。

## 一個最小使用流程

### 1. 安裝 plugin

```text
/plugin install pr-review
```

### 2. 在程式碼改動或 PR 場景中執行

```text
/review-pr
```

### 3. Claude 通常會做什麼

1. 收集當前改動或 PR 上下文
2. 分別呼叫安全、測試、效能相關 agents
3. 彙總問題並輸出優先順序建議

## 什麼時候最適合用

- 發 PR 前做一次結構化審查
- 你懷疑改動對安全或測試有影響
- 團隊想形成相對固定的審查範本

## 常見坑

### 1. 沒有 `GITHUB_TOKEN`

如果你的流程依賴 GitHub 資料，這會直接影響外掛能力。

### 2. 以為它會替代人工 review

這個 plugin 更適合作為結構化預審查，而不是替代所有人工判斷。

### 3. 當前目錄不是 Git 倉庫

很多審查能力都預設建立在 Git 工作流之上。
