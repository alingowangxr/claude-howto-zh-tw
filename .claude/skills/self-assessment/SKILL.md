---
name: self-assessment
version: 2.2.0
description: Claude Code 中文自測與學習路徑顧問。用於評估當前水平、識別短板、推薦學習順序。Use when asked to "assess my level", "take the quiz", "find my level", "where should I start", "what should I learn next", "check my skills", "skill check", or similar Chinese requests.
---

# Self-Assessment & Learning Path Advisor

這是一個完整的 Claude Code 互動式自測 skill，用來評估使用者在 10 個能力域上的熟練度，並據此生成個性化學習路徑。

## Instructions

### Step 1: 先讓使用者選擇評估模式

使用 AskUserQuestion 提供兩個選項：

- **Quick Assessment**：8 個問題，約 2 分鐘，用於快速判斷 Beginner / Intermediate / Advanced
- **Deep Assessment**：5 輪問題，約 5 分鐘，用於分別評估 10 個主題的掌握情況

如果使用者選擇 Quick Assessment，進入 Step 2A。  
如果使用者選擇 Deep Assessment，進入 Step 2B。

---

### Step 2A: Quick Assessment

使用兩個多選問題完成快速自測，每個問題最多 4 個選項。

**Question 1**（header: `Basics`）  
Prompt:
`Part 1/2: Which of these Claude Code skills do you already have?`

Options:
1. `Start Claude Code and chat` — 我會執行 `claude` 並進入對話
2. `Created/edited CLAUDE.md` — 我設定過專案或個人 memory
3. `Used 3+ slash commands` — 例如 `/help`、`/clear`、`/model`
4. `Created custom command/skill` — 寫過 `SKILL.md` 或 `.claude/commands/`

**Question 2**（header: `Advanced`）  
Prompt:
`Part 2/2: Which of these advanced skills do you have?`

Options:
1. `Configured an MCP server` — 設定過 GitHub、資料庫或其他外部資料來源
2. `Set up hooks` — 設定過 `~/.claude/settings.json` 裡的 hooks
3. `Created/used subagents` — 使用過 `.claude/agents/`
4. `Used print mode (claude -p)` — 用過非互動模式或 CI/CD 整合

**Quick 模式評分：**

- 0-2 項：Level 1 — Beginner
- 3-5 項：Level 2 — Intermediate
- 6-8 項：Level 3 — Advanced

進入 Step 3A 輸出結果，並列出未勾選項作為短板。

---

### Step 2B: Deep Assessment

Deep 模式共 5 輪，每輪 1 個多選問題，每題最多 4 個選項，每輪覆蓋 2 個主題。

#### Round 1 — Slash Commands & Memory

Header: `Commands`  
Prompt:
`Which of these have you done? Select all that apply.`

Options:
1. `Created a custom slash command or skill` — 寫過帶 frontmatter 的 `SKILL.md` 或 `.claude/commands/` 檔案
2. `Used dynamic context in commands` — 用過 `$ARGUMENTS`、`$0`/`$1`、`!command`、`@file`
3. `Set up project + personal memory` — 同時設定過專案級和個人級 `CLAUDE.md`
4. `Used memory hierarchy features` — 理解層級優先順序、用過 `.claude/rules/`、path-specific rules 或 `@import`

Scoring:
- 1-2 對映到 Slash Commands（0-2）
- 3-4 對映到 Memory（0-2）

#### Round 2 — Skills & Hooks

Header: `Automation`

Options:
1. `Installed and used an auto-invoked skill` — 使用過自動觸發的 skill
2. `Controlled skill invocation behavior` — 用過 `disable-model-invocation`、`user-invocable` 或 `context: fork`
3. `Set up a PreToolUse or PostToolUse hook` — 設定過常見 hook
4. `Used advanced hook features` — 用過 prompt hooks、component-scoped hooks、HTTP hooks、custom JSON output

Scoring:
- 1-2 對映到 Skills（0-2）
- 3-4 對映到 Hooks（0-2）

#### Round 3 — MCP & Subagents

Header: `Integration`

Options:
1. `Connected an MCP server and used its tools`
2. `Used advanced MCP features` — project-scope `.mcp.json`、OAuth、Tool Search、`claude mcp serve`
3. `Created or configured custom subagents`
4. `Used advanced subagent features` — worktree isolation、persistent memory、background tasks、agent allowlists、agent teams

Scoring:
- 1-2 對映到 MCP（0-2）
- 3-4 對映到 Subagents（0-2）

#### Round 4 — Checkpoints & Advanced Features

Header: `Power User`

Options:
1. `Used checkpoints for safe experimentation`
2. `Used planning mode or extended thinking`
3. `Configured permission modes`
4. `Used remote/desktop/web features`

Scoring:
- 1 對映到 Checkpoints（0-1）
- 2-4 對映到 Advanced Features（0-2，最多記 2 分）

#### Round 5 — Plugins & CLI

Header: `Mastery`

Options:
1. `Installed or created a plugin`
2. `Used plugin advanced features` — plugin hooks、plugin MCP、LSP、`--plugin-dir`
3. `Used print mode in scripts or CI/CD`
4. `Used advanced CLI features` — `-c/-r`、`--agents`、`--json-schema`、`--fallback-model`、`--from-pr`

Scoring:
- 1-2 對映到 Plugins（0-2）
- 3-4 對映到 CLI（0-2）

進入 Step 3B 輸出結果。

---

### Step 3A: Quick 模式結果輸出

輸出必須包含：

```markdown
## Claude Code 自測結果

### 你的等級：Level 1 / Level 2 / Level 3

你勾選了 **N/8** 項。

[一句鼓勵性的總結]

### 你的能力概覽

| Area | Status |
|------|--------|
| Basic CLI & Conversations | [Checked / Gap] |
| CLAUDE.md & Memory | [Checked / Gap] |
| Slash Commands | [Checked / Gap] |
| Custom Commands & Skills | [Checked / Gap] |
| MCP | [Checked / Gap] |
| Hooks | [Checked / Gap] |
| Subagents | [Checked / Gap] |
| Print Mode & CI/CD | [Checked / Gap] |

### 主要短板

[對每個未勾選項，給一行說明 + 對應教程連結]

### 個性化學習路徑

[按 Step 4 生成]
```

---

### Step 3B: Deep 模式結果輸出

Deep 模式要輸出完整結果：

```markdown
## Claude Code 自測結果

### Overall Level: [Level 1 / Level 2 / Level 3]

**Total Score: N/20**

[一句鼓勵性總結]

### 你的能力畫像

| Feature Area | Score | Mastery | Status |
|-------------|-------|---------|--------|
| Slash Commands | N/2 | None / Basic / Proficient | Learn / Review / Mastered |
| Memory | N/2 | None / Basic / Proficient | Learn / Review / Mastered |
| Skills | N/2 | None / Basic / Proficient | Learn / Review / Mastered |
| Hooks | N/2 | None / Basic / Proficient | Learn / Review / Mastered |
| MCP | N/2 | None / Basic / Proficient | Learn / Review / Mastered |
| Subagents | N/2 | None / Basic / Proficient | Learn / Review / Mastered |
| Checkpoints | N/1 | None / Proficient | Learn / Mastered |
| Advanced Features | N/2 | None / Basic / Proficient | Learn / Review / Mastered |
| Plugins | N/2 | None / Basic / Proficient | Learn / Review / Mastered |
| CLI | N/2 | None / Basic / Proficient | Learn / Review / Mastered |
```

然後繼續輸出：

- **Strength Areas**：得分滿分的主題
- **Priority Gaps**：得分 0 的主題，按依賴順序排列
- **Review Areas**：得分 1 的主題
- **Your Personalized Learning Path**

Deep 模式總體等級：

- 0-6：Level 1
- 7-13：Level 2
- 14-20：Level 3

---

### Step 4: 生成個性化學習路徑

不要簡單重複通用路線，要按短板動態生成。

規則：

1. 滿分主題不再列為重點學習項
2. 按依賴順序排學習路徑：
   - Slash Commands → Skills
   - Memory → Subagents
   - Hooks 依賴 Slash Commands
   - Plugins 依賴 MCP、Skills、Hooks
   - Advanced Features 依賴前面大多數基礎
3. 得分 1 的主題推薦“深入補課”
4. 按還沒掌握的主題估算總時長
5. 路徑分成 2-3 個 phase

輸出格式：

```markdown
### Your Personalized Learning Path

**Estimated time**: ~N hours

#### Phase 1: [Name] (~N hours)

**[Topic]** — [Learn from scratch / Deep dive]
- Tutorial: [link]
- Focus on: [sections]
- Key exercise: [one exercise]
- Done when: [success criterion]
```

---

### Step 5: 提供後續動作

結果給完後，再用 AskUserQuestion 讓使用者選擇：

1. `Start with my first gap`
2. `Deep dive into a topic`
3. `Set up a practice project`
4. `Retake the assessment`

如果使用者選第一項：直接進入第一個短板主題的學習建議。  
如果使用者選第二項：讓使用者選一個主題並解釋。  
如果使用者選第三項：根據短板組合一個練習專案。  
如果使用者選第四項：重新開始。

## Output Requirements

- 全程使用中文
- 保留關鍵英文術語，例如 skills、MCP、CLI
- 不要空泛鼓勵，要給可執行建議
- 教學引用優先指向倉庫內對應 lesson
