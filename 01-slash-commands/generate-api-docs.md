---
description: 從原始碼生成結構化 API 檔案
---

# API Documentation Generator / API 檔案生成

請按下面步驟生成 API 檔案：

1. 掃描 `/src/api/` 下的相關檔案
2. 提取函式簽名、路由資訊和 JSDoc 註釋
3. 按 endpoint / module 分組整理
4. 輸出為 Markdown 檔案
5. 包含 request / response schema
6. 補充錯誤返回說明

輸出要求：

- 寫入 `/docs/api.md`
- 每個 endpoint 儘量提供 `curl` 範例
- 如專案使用 TypeScript，補充相關型別說明
- 檔案結構清晰，適合團隊直接維護
