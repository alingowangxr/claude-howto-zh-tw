# Checkpoint 範例

下面是一些更貼近真實工作的 checkpoint 用法範例。

> 注意：checkpoints 預設會自動建立。你不需要手動儲存，只需要在需要時用 `Esc+Esc` 或 `/rewind` 回退。

## Example 1: 資料庫遷移方案對比

- 先嚐試直接遷移
- 測試失敗後回退
- 再嘗試 dual-write 方案
- 對比兩種策略後選擇更穩妥的實現

## Example 2: 效能最佳化實驗

- 基線 checkpoint
- 嘗試快取
- 回退
- 嘗試查詢最佳化
- 再組合方案

## Example 3: UI 方案迭代

- 儲存起始狀態
- 試 sidebar
- 回退
- 試 top nav
- 回退
- 試 card grid
- 最後組合最佳方案

## Example 4: 除錯假設切換

- 鎖定一個 bug
- 試第一種假設
- 不成立就回退
- 換第二種假設
- 直到找到根因

## Example 5: API 設計演進

- 從 REST 方案開始
- 回退後切到 GraphQL 方案
- 再比較哪種更適合當前專案
