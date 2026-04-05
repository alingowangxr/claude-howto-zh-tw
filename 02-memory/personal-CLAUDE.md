# 我的開發偏好

## About Me

- **Experience Level**: 8 年全棧開發經驗
- **Preferred Languages**: TypeScript、Python
- **Communication Style**: 直接、清晰、帶範例
- **Learning Style**: 喜歡圖示和程式碼結合

## Code Preferences

### Error Handling

偏好顯式錯誤處理，儘量使用清晰的 `try-catch` 和有意義的錯誤資訊。  
避免過於泛化的錯誤；排查時儘量保留日誌上下文。

### Comments

註釋優先解釋 **WHY**，不要只是重複程式碼在做什麼。  
更適合解釋業務邏輯或不明顯的決策。

### Testing

偏好 TDD。  
儘量先寫測試，再實現。  
測試關注行為，而不是實現細節。

### Architecture

偏好模組化、低耦合設計。  
重視可測試性和職責分離。

## Debugging Preferences

- `console.log` 建議帶 `[DEBUG]` 字首
- 日誌包含函式名和關鍵變數
- 能給 stack trace 時儘量給
- 日誌裡儘量保留時間戳

## Communication

- 複雜概念先給範例再講理論
- 需要時提供 before / after 程式碼片段
- 長回答最後給一個簡要總結

## Project Organization

我常用的專案結構：

```text
project/
  ├── src/
  │   ├── api/
  │   ├── services/
  │   ├── models/
  │   └── utils/
  ├── tests/
  ├── docs/
  └── docker/
```

## Tooling

- **IDE**: VS Code + vim keybindings
- **Terminal**: Zsh + Oh-My-Zsh
- **Format**: Prettier（100 字元換行）
- **Linter**: ESLint + airbnb config
- **Test Framework**: Jest + React Testing Library
