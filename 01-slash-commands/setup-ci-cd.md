---
name: Setup CI/CD Pipeline
description: 為專案建立 pre-commit hooks 和 GitHub Actions 品質門禁
tags: ci-cd, devops, automation
---

# Setup CI/CD Pipeline / 設定 CI/CD 流水線

請為專案建立一套務實的 DevOps 品質門禁：

1. **分析專案**：識別語言、框架、構建系統和現有工具鏈
2. **設定 pre-commit hooks**：
   - 格式化：Prettier / Black / gofmt / rustfmt 等
   - lint：ESLint / Ruff / golangci-lint / Clippy 等
   - 安全：Bandit / gosec / cargo-audit / npm audit 等
   - 型別檢查：TypeScript / mypy / flow
   - 測試：執行核心 test suite
3. **建立 GitHub Actions**：
   - push / PR 時映象執行本機檢查
   - 必要時做多版本或多平臺矩陣
   - 包含 build 與 test 驗證
   - 如果需要，加入部署步驟
4. **驗證整條流水線**：
   - 本機先跑通
   - 建立測試 PR
   - 確認所有檢查綠燈

要求：

- 優先使用開源免費工具
- 尊重專案已有設定
- 保持執行速度，不要一開始就堆太重的檢查
