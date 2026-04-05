---
name: claude-md
description: 按最佳實踐建立或更新 CLAUDE.md，幫助 AI agent 更快理解專案。Use when users want to create, update, audit, or improve a CLAUDE.md file.
---

# CLAUDE.md / 專案記憶整理

## User Input

```text
$ARGUMENTS
```

支援的意圖：

- `create`
- `update`
- `audit`
- 指定某個路徑下的 `CLAUDE.md`

## Core Principles

- `CLAUDE.md` 是 Claude Code 自動載入的長期專案上下文
- 內容要短、準、長期有效
- 不要把 lint / format 規則硬塞進去
- 不要把一次性任務說明塞進去
- 不要自動生成一堆無價值內容

## 推薦結構

- Project Overview
- Tech Stack
- Project Structure
- Development Commands
- Critical Conventions
- Known Issues / Gotchas

## Execution Flow

### create

1. 分析專案結構和技術堆疊
2. 草擬 `CLAUDE.md`
3. 給使用者審閱
4. 確認後寫入

### update

1. 讀取現有 `CLAUDE.md`
2. 找出冗餘、過時或不該存在的內容
3. 給出最佳化建議
4. 審閱後更新

### audit

1. 檢查行數和結構
2. 識別 anti-patterns
3. 輸出報告，不直接改檔案

## Quality Constraints

- 目標儘量少於 300 行
- 面向所有會話都適用
- 儘量用檔案引用替代長程式碼塊
- 命令必須真實可用
