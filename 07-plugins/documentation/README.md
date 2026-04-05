<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../../resources/logos/claude-howto-logo-dark.svg">
  <img alt="Claude How To" src="../../resources/logos/claude-howto-logo.svg">
</picture>

# Documentation 外掛

用於把 API 檔案、README 生成、檔案同步和檔案校驗打包成一套方案。

## Features

- API 檔案生成
- README 建立與更新
- 檔案同步
- 程式碼註釋改進
- 範例生成

## Installation

```bash
/plugin install documentation
```

## What's Included

### Commands

- `/generate-api-docs`
- `/generate-readme`
- `/sync-docs`
- `/validate-docs`

### Agents

- `api-documenter`
- `code-commentator`
- `example-generator`

## 適合什麼專案

- API 或 SDK 專案
- README 常年落後的專案
- 範例程式碼和實際實現經常不同步的專案

## 最小使用流程

### 1. 安裝 plugin

```text
/plugin install documentation
```

### 2. 從一個具體入口開始

例如：

```text
/generate-api-docs
```

或者：

```text
/generate-readme
```

### 3. Claude 通常會做什麼

1. 掃描程式碼結構
2. 分配給相關檔案 agents
3. 生成或更新檔案
4. 檢查連結、範例與結構是否一致

## 常見坑

### 1. 以為它能自動理解一切上下文

如果程式碼結構混亂、註釋缺失，這個 plugin 也需要更多人工引導。

### 2. 檔案生成後不做驗證

生成不等於正確，最好配合 `/validate-docs` 使用。

### 3. 只更新 README，不更新 API 檔案

檔案類 plugin 的核心價值之一，就是幫助你保持多個檔案入口的一致性。
