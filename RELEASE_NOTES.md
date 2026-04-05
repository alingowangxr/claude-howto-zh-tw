# Release Notes

## v1.0.0 — 首個繁體中文化釋出

這是 `claude-howto-zh-tw` 的首個正式釋出版本。

本次釋出的目標不是做“逐句翻譯映象”，而是把上游專案重構成一個 **更適合初學者長期學習、同時保留真實可用性的 Claude Code 中文全面上手指南**。

## 本版重點

### 1. 中文主線入口完成

- `README`
- `LEARNING-ROADMAP`
- `QUICK_REFERENCE`
- `CATALOG`
- 核心模組 `README`

這些入口檔案現在已經統一成中文主線表達，學習路徑、安裝方式、使用場景和常見坑更貼近中文使用者閱讀習慣。

### 2. 執行型檔案完成相容性收口

- 保留命令名、frontmatter key、JSON/YAML key、CLI flags、環境變數等關鍵標識
- 修復了不應被中文化的顯示標識
- 自動觸發類 descriptions 補回英文觸發短語

目標是避免“看起來翻譯對了，但複製就跑不起來”的問題。

### 3. 互動學習能力補回完整結構

- `self-assessment` 復原為完整自測流程
- `lesson-quiz` 復原為完整 lesson 測驗流程
- 題庫復原為結構化格式，並統一評分口徑

### 4. 釋出前護欄已落地

- 在地化校驗腳本：`scripts/validate_localization.py`
- 對應測試已補齊
- CI / docs-check 工作流已擴充套件

## 自動驗證

本版釋出前已透過：

```bash
uv run python scripts/validate_localization.py
uv run pytest scripts/tests/ -q
```

## 適合誰

- 想系統學 Claude Code 的中文使用者
- 想把上游專案改成中文團隊教材的人
- 想保留真實命令和設定相容性的本土化維護者

## 說明

- 本專案為 **非官方繁體中文化 fork**
- 來源與同步策略見 `UPSTREAM.md`
- 在地化邊界與術語規則見 `LOCALIZATION-STYLE.md`
