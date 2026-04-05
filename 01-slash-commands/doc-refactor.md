---
name: Documentation Refactor
description: 按專案型別重組檔案結構，提高可讀性和可維護性
tags: documentation, refactoring, organization
---

# Documentation Refactor / 檔案重構

請根據專案實際型別對檔案做結構化重構：

1. **先分析專案**：判斷它是 library、API、web app、CLI 還是微服務，並識別主要讀者是誰
2. **集中整理檔案**：把技術性檔案歸攏到 `docs/`，並補齊交叉引用
3. **整理根目錄 `README.md`**：讓它只承擔入口職責，包含 overview、quickstart、模組摘要、license、聯絡方式
4. **補齊元件級檔案**：為模組、包或服務增加 README，並寫清 setup / testing / usage
5. **按主題組織 `docs/`**：
   - Architecture
   - API Reference
   - Database
   - Design
   - Troubleshooting
   - Deployment
   - Contributing
6. **按需生成指南**：
   - User Guide
   - API Documentation
   - Development Guide
   - Deployment Guide
7. **圖示統一用 Mermaid**

要求：

- 檔案要短、清晰、可掃描
- 先從專案入口和高頻模組開始
- 不要為了“看起來完整”而增加無意義章節
