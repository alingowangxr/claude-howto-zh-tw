# 專案設定

## Project Overview

- **Name**: E-commerce Platform
- **Tech Stack**: Node.js, PostgreSQL, React 18, Docker
- **Team Size**: 5 developers
- **Deadline**: Q4 2025

## Architecture

@docs/architecture.md  
@docs/api-standards.md  
@docs/database-schema.md

## Development Standards

### Code Style

- 使用 Prettier
- 使用 ESLint + airbnb config
- 最大行長 100
- 2-space indentation

### Naming Conventions

- **Files**: kebab-case
- **Classes**: PascalCase
- **Functions/Variables**: camelCase
- **Constants**: UPPER_SNAKE_CASE
- **Database Tables**: snake_case

### Git Workflow

- 分支命名：`feature/description` 或 `fix/description`
- 提交資訊遵循 conventional commits
- 合併前需要 PR
- 所有 CI/CD 檢查必須透過
- 至少 1 個 approval

### Testing Requirements

- 最低 80% 覆蓋率
- 關鍵路徑必須有測試
- unit tests 用 Jest
- E2E 用 Cypress
- 檔案命名：`*.test.ts` 或 `*.spec.ts`

### API Standards

- 使用 RESTful endpoints
- JSON request / response
- 正確使用 HTTP status code
- API 統一帶版本：`/api/v1/`
- 所有 endpoint 要有範例檔案

### Database

- schema 變更必須走 migration
- 不允許硬編碼憑證
- 使用 connection pooling
- 開發環境開啟 query logging
- 定期備份

### Deployment

- Docker-based deployment
- Kubernetes orchestration
- blue-green deployment
- 失敗自動回滾
- deploy 前先跑資料庫遷移

## Common Commands

| Command | Purpose |
|---------|---------|
| `npm run dev` | 啟動開發服務 |
| `npm test` | 執行測試 |
| `npm run lint` | 檢查程式碼風格 |
| `npm run build` | 生產構建 |
| `npm run migrate` | 執行資料庫遷移 |

## Team Contacts

- Tech Lead: Sarah Chen (`@sarah.chen`)
- Product Manager: Mike Johnson (`@mike.j`)
- DevOps: Alex Kim (`@alex.k`)

## Known Issues & Workarounds

- PostgreSQL 連線池高峰期限制為 20
- 臨時方案：實現 query queuing
- Safari 14 對 async generators 有相容性問題
- 臨時方案：使用 Babel transpiler

## Related Projects

- Analytics Dashboard: `/projects/analytics`
- Mobile App: `/projects/mobile`
- Admin Panel: `/projects/admin`
