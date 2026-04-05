---
description: 分析程式碼中的效能問題並提出最佳化建議
---

# Code Optimization / 程式碼最佳化

請按優先順序檢查程式碼中的這些問題：

1. **Performance bottlenecks**：是否存在 O(n²) 操作、低效迴圈、重複查詢
2. **Memory leaks**：是否有資源未釋放、快取失控、迴圈引用等問題
3. **Algorithm improvements**：是否有更合適的資料結構或演算法
4. **Caching opportunities**：哪些重複計算或查詢適合快取
5. **Concurrency issues**：是否存在競態條件、鎖問題、執行緒安全隱患

輸出格式請包含：

- 問題嚴重級別：Critical / High / Medium / Low
- 位置
- 原因解釋
- 推薦修復方式
- 必要時給出程式碼範例
