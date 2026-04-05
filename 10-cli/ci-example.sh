#!/usr/bin/env bash
# ci-example.sh — 在 CI/CD 環境中使用 claude -p 的常見範例
# 使用方式：cp 10-cli/ci-example.sh your-project/.github/scripts/
#
# 注意：執行前確認
#   1. ANTHROPIC_API_KEY 已設定在 CI 環境變數中
#   2. claude CLI 已安裝（npm install -g @anthropic-ai/claude-code）
#   3. 根據實際需求調整 --permission-mode

set -euo pipefail

# ── 1. 跑測試並讓 Claude 摘要失敗原因 ──────────────────────────────────────
echo "=== 跑測試 ==="
if ! npm test 2>&1 | tee test-output.txt; then
  echo "測試失敗，請 Claude 摘要："
  claude -p "以下是測試失敗的輸出，請用繁體中文條列出每個失敗的根本原因和建議修法" \
    --permission-mode plan \
    < test-output.txt
  exit 1
fi

# ── 2. 靜態分析結果摘要 ─────────────────────────────────────────────────────
echo "=== 靜態分析 ==="
npx eslint . --format json > lint-output.json 2>/dev/null || true

if [ -s lint-output.json ]; then
  claude -p "以下是 ESLint 輸出（JSON），請列出最需要優先修正的 3 個問題並說明原因" \
    --permission-mode plan \
    < lint-output.json
fi

# ── 3. PR diff 摘要（在 PR 流程中執行）────────────────────────────────────
if [ -n "${GITHUB_BASE_REF:-}" ]; then
  echo "=== 生成 PR 摘要 ==="
  git diff "origin/${GITHUB_BASE_REF}...HEAD" | \
    claude -p "請用繁體中文為這份 diff 生成 PR 摘要，包含：改了什麼、為什麼、可能影響範圍" \
      --permission-mode plan
fi

echo "=== CI 完成 ==="
