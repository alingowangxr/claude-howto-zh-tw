# API 模組規則

這個檔案用於覆蓋根目錄 `CLAUDE.md`，作用範圍是 `/src/api/` 下的內容。

## API 專屬規範

### Request Validation

- 使用 Zod 做 schema validation
- 所有輸入都必須校驗
- 校驗失敗返回 400
- 錯誤資訊儘量提供欄位級細節

### Authentication

- 所有 endpoint 預設需要 JWT token
- token 放在 `Authorization` header
- token 預設 24 小時過期
- 實現 refresh token 機制

### Response Format

所有成功響應統一遵循下面的結構：

```json
{
  "success": true,
  "data": { /* actual data */ },
  "timestamp": "2025-11-06T10:30:00Z",
  "version": "1.0"
}
```

錯誤響應：

```json
{
  "success": false,
  "error": {
    "code": "VALIDATION_ERROR",
    "message": "User message",
    "details": { /* field errors */ }
  },
  "timestamp": "2025-11-06T10:30:00Z"
}
```

### Pagination

- 使用 cursor-based pagination
- 返回 `hasMore`
- 單頁最大 100
- 預設每頁 20

### Rate Limiting

- 登入使用者每小時 1000 次
- 公共介面每小時 100 次
- 超限返回 429
- 包含 `retry-after` header

### Caching

- 使用 Redis 做 session caching
- 預設快取 5 分鐘
- 寫操作後主動失效
- cache key 帶資源型別標籤
