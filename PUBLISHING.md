# Publishing Notes

## 推薦 commit message

### 單行版本

```text
docs: ship the first polished zh-tw Claude Code guide release
```

### 帶正文版本

```text
docs: ship the first polished zh-tw Claude Code guide release

- localize all tracked markdown docs into a Chinese-first guide
- restore interactive self-assessment and lesson-quiz flows
- add localization guardrails, tests, and CI validation
- improve release readiness for Chinese beginner users
```

## 推薦倉庫描述（GitHub About）

```text
Claude Code 中文全面上手指南。基于 luongnv89/claude-howto 本土化重写，面向台灣小白用户，保留命令与配置兼容性，并附学习路径与本地化校验护栏。
```

## 推薦 GitHub 首頁摘要

```text
这是一个基于 luongnv89/claude-howto 的非官方中文本土化 fork，目标不是逐句翻译，而是做成适合台灣小白长期学习的 Claude Code 全面上手指南。

你可以从 README、学习路线图和速查卡开始，再逐步进入 slash commands、memory、skills、MCP、hooks、subagents、plugins、CLI 等模块。仓库同时保留了关键可执行标识，并提供本地化校验脚本，尽量避免“中文化后示例不可用”的问题。
```

## 推薦首版 Release 標題

```text
v1.0.0 — 首个中文本土化发布
```

## 推薦首版 Release 摘要

```text
首个正式中文本土化版本，面向台灣小白用户重写 Claude Code 学习主线，并保留关键命令、配置和 frontmatter 兼容性。

本版完成了中文首页、学习路线、速查卡、功能总表、主要模块 README，以及高频执行型 Markdown 的中文化收口；同时恢复了 self-assessment / lesson-quiz 的完整交互结构，并加入本地化校验脚本、测试与 CI 护栏。
```

## 釋出前建議核對

- 倉庫預設分支是否正確
- `UPSTREAM.md` 中的來源說明是否保留
- GitHub 倉庫 About 文案是否與 README 首段一致
- Release 標題、tag 和 `RELEASE_NOTES.md` 是否統一
