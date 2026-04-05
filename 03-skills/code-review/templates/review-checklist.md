# Code Review Checklist / 審查清單

## Security Checklist

- [ ] 沒有硬編碼 secrets
- [ ] 所有使用者輸入都有校驗
- [ ] 避免 SQL injection
- [ ] 狀態修改介面有 CSRF 保護（如適用）
- [ ] 有 XSS 防護
- [ ] 受保護介面有鑑權檢查

## Performance Checklist

- [ ] 沒有明顯 O(n²) 熱路徑
- [ ] 避免 N+1 查詢
- [ ] 快取策略合理
- [ ] 沒有明顯記憶體浪費

## Quality Checklist

- [ ] 命名清晰
- [ ] 函式職責單一
- [ ] 沒有明顯重複程式碼
- [ ] 關鍵邏輯有足夠測試
