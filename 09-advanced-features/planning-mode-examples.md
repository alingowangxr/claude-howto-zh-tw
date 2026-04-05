# Planning Mode 範例

這裡給一些 planning mode 的典型用法範例，幫助你理解什麼時候值得先規劃再執行。

## Example 1: 構建 REST API

使用 `/plan` 後，Claude 應該先輸出：

- 分階段計劃
- 需要建立哪些檔案
- 核心技術選型
- 風險點
- 預計工作量

而不是直接開始寫程式碼。

## Example 2: 資料庫遷移

面對 MongoDB → PostgreSQL 這類高風險任務，planning mode 應該先明確：

- 分階段遷移策略
- dual-write / rollback 方案
- 資料一致性檢查
- cutover 節點

## Example 3: 前端大規模重構

例如 class components → hooks，規劃裡應該先給：

- 元件盤點
- 複雜度分級
- 遷移順序
- 測試與回退策略
