---
name: Expand Unit Tests
description: 針對未覆蓋分支、邊界情況和錯誤路徑補全測試
tags: testing, coverage, unit-tests
---

# Expand Unit Tests / 擴充套件單元測試

請根據專案現有測試框架擴充套件單元測試覆蓋：

1. **先分析覆蓋率**：識別未覆蓋分支、邊界情況和低覆蓋區域
2. **找出缺口**：
   - 邏輯分支
   - 錯誤路徑
   - 邊界值
   - 空值 / 空集合 / null 輸入
3. **按專案現有框架補測試**：
   - Jest / Vitest / Mocha
   - pytest / unittest
   - Go testing / testify
   - Rust test framework
4. **重點覆蓋**：
   - 錯誤處理
   - 邊界值
   - corner cases
   - 狀態變化和副作用
5. **再次驗證**：重新跑覆蓋率並確認提升

輸出要求：

- 只輸出新增測試程式碼塊或明確的測試檔案改動
- 遵循專案現有測試風格和命名習慣
