#!/usr/bin/env bash
# pipe-example.sh — 透過 pipe 把資料餵給 claude -p 的常見範例
# 使用方式：直接執行或複製片段到自己的腳本
#
# 注意：執行前確認 ANTHROPIC_API_KEY 已設定

set -euo pipefail

# ── 1. 解釋錯誤日誌 ─────────────────────────────────────────────────────────
explain_log() {
  local logfile="${1:-/dev/stdin}"
  echo "=== 解釋日誌：$logfile ==="
  cat "$logfile" | \
    claude -p "請用繁體中文解釋這份日誌中的錯誤，並列出最可能的根本原因" \
      --permission-mode plan
}

# ── 2. 分析 git log ──────────────────────────────────────────────────────────
summarize_commits() {
  local since="${1:-1 week ago}"
  echo "=== 最近提交摘要（since: $since）==="
  git log --since="$since" --oneline | \
    claude -p "請用繁體中文為這些 commit 生成一份週報摘要，按功能分類" \
      --permission-mode plan
}

# ── 3. 解釋某個函式 ─────────────────────────────────────────────────────────
explain_function() {
  local file="$1"
  echo "=== 解釋檔案：$file ==="
  cat "$file" | \
    claude -p "請用繁體中文解釋這段程式碼的主要邏輯，適合給剛接手的工程師閱讀" \
      --permission-mode plan
}

# ── 4. 結構化 JSON 輸出範例 ──────────────────────────────────────────────────
structured_analysis() {
  local file="$1"
  echo "=== 結構化分析：$file ==="
  cat "$file" | \
    claude -p "分析這段程式碼，回傳 JSON，格式：{\"summary\":\"...\",\"issues\":[],\"suggestions\":[]}" \
      --permission-mode plan \
      --output-format json
}

# ── 主程式：示範用法 ─────────────────────────────────────────────────────────
case "${1:-demo}" in
  log)
    explain_log "${2:-}"
    ;;
  commits)
    summarize_commits "${2:-1 week ago}"
    ;;
  explain)
    [ -z "${2:-}" ] && { echo "用法：$0 explain <檔案路徑>"; exit 1; }
    explain_function "$2"
    ;;
  json)
    [ -z "${2:-}" ] && { echo "用法：$0 json <檔案路徑>"; exit 1; }
    structured_analysis "$2"
    ;;
  demo)
    echo "pipe-example.sh 示範模式"
    echo ""
    echo "可用指令："
    echo "  $0 log [logfile]          解釋錯誤日誌（不指定則從 stdin 讀）"
    echo "  $0 commits [since]        摘要 git commit（預設：1 week ago）"
    echo "  $0 explain <file>         解釋程式碼檔案"
    echo "  $0 json <file>            結構化分析並輸出 JSON"
    echo ""
    echo "直接 pipe 範例："
    echo "  cat error.log | claude -p \"解釋這個錯誤\""
    echo "  git diff HEAD | claude -p \"這個 diff 改了什麼\""
    ;;
esac
