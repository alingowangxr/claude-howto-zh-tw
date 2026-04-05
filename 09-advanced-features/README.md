<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../resources/logos/claude-howto-logo-dark.svg">
  <img alt="Claude How To" src="../resources/logos/claude-howto-logo.svg">
</picture>

# Advanced Features 指南

當你已經會用 slash commands、memory、skills、MCP、hooks 和 subagents 之後，Claude Code 的高階能力會決定你能不能把它真正用到複雜專案和高自動化工作流裡。

這部分不是“你必須一口氣全會”，而是你要知道：

- 哪些高階能力最值得先學
- 哪些適合日常開發
- 哪些適合團隊和自動化
- 哪些不該在沒準備好的情況下亂開

---

## 這部分包含什麼

主要包括：

- planning mode
- extended thinking
- Auto Mode
- background tasks
- scheduled tasks
- permission modes
- print mode / headless usage
- session management
- remote / desktop / web sessions
- worktrees
- sandboxing
- configuration

---

## 最推薦先掌握的四項

### 1. planning mode

複雜任務先規劃再執行。

### 2. permission modes

明確 Claude 在本機到底能做多少事。

### 3. print mode

把 Claude Code 接進腳本、CI/CD 和自動化流程的關鍵入口。

### 4. background tasks

讓耗時任務後臺跑，不阻塞當前會話。

如果你不是重度使用者，先掌握這四個就足夠產生明顯收益。

---

## planning mode

### planning mode 是什麼

它是“兩階段工作流”：

1. 先做計劃
2. 再按計劃執行

適合：

- 多檔案重構
- 新功能設計
- 架構調整
- 資料遷移
- 高風險變更

不太適合：

- 小 bug
- 單檔案輕改
- 只問一個簡單問題

### 常見入口

```text
/plan Implement user authentication system
```

也可以透過許可權模式進入只讀規劃狀態：

```bash
claude --permission-mode plan
```

### 一個好的 planning mode 輸出應該包含什麼

- 分階段計劃
- 預計會改哪些檔案
- 風險點
- 驗證方式
- 使用者需要確認的地方

如果 planning mode 只給你幾句空話，那不是好計劃。

---

## extended thinking

extended thinking 的價值在於：讓 Claude 對複雜問題多想一步，而不是急著下結論。

它特別適合：

- 架構對比
- 技術選型
- 高歧義問題
- 邊界條件分析

對新手使用者來說，一個實用理解是：  
**不是所有問題都要更長思考，但複雜問題最好別讓 Claude 秒答。**

---

## Auto Mode

Auto Mode 屬於更偏自動化、也更需要謹慎的能力。

它適合：

- 明確受控的自動化環境
- 已經知道自己在放開什麼許可權
- 你對專案風險邊界比較清楚

它不適合：

- 你還沒搞清 permission modes 差異
- 你還不確定專案裡哪些操作是危險的

新手建議先不要把 Auto Mode 作為預設。

---

## 沒有 Team plan 時的替代方案：一次性許可權種子腳本

如果你沒有 Team plan，或者你不想用“後臺分類器 + 自動判定”這套模式，上游最近新增了一種更務實的替代方案：

- 直接用一次性腳本把一組 **更保守的安全許可權基線** 寫進 `~/.claude/settings.json`

腳本位置：

```text
09-advanced-features/setup-auto-mode-permissions.py
```

### 典型用法

```bash
# 先預覽會加什麼，不落盤
python3 09-advanced-features/setup-auto-mode-permissions.py --dry-run

# 寫入保守基線
python3 09-advanced-features/setup-auto-mode-permissions.py

# 按需再放開能力
python3 09-advanced-features/setup-auto-mode-permissions.py --include-edits --include-tests
python3 09-advanced-features/setup-auto-mode-permissions.py --include-git-write --include-packages
python3 09-advanced-features/setup-auto-mode-permissions.py --include-gh-read --include-gh-write
```

### 這組許可權預設包含什麼

| 類別 | 範例 |
|------|------|
| Core read-only tools | `Read(*)`、`Glob(*)`、`Grep(*)`、`Agent(*)`、`WebSearch(*)`、`WebFetch(*)` |
| Local inspection | `Bash(git status:*)`、`Bash(git log:*)`、`Bash(git diff:*)`、`Bash(cat:*)` |
| Optional edits | `Edit(*)`、`Write(*)`、`NotebookEdit(*)` |
| Optional test/build | `Bash(pytest:*)`、`Bash(cargo test:*)`、`Bash(make:*)` |
| Optional git writes | `Bash(git add:*)`、`Bash(git commit:*)`、`Bash(git stash:*)` |
| Optional packages | `Bash(npm install:*)`、`Bash(pip install:*)` |
| Optional GitHub CLI | `Bash(gh pr view:*)`、`Bash(gh pr create:*)` |

### 它和舊的 `auto-adapt-mode` 有什麼不同

舊思路：

- 透過 hook 動態學習你核准過什麼

現在的新思路：

- 一次性寫入一組明確的規則
- 再透過命令列引數按需增加範圍

這對中文使用者尤其有幫助，因為它更容易解釋清楚：

- 現在到底開了哪些許可權
- 哪些是預設安全基線
- 哪些是你主動額外放開的

### 明確不會自動加進去的危險操作

腳本明確不會幫你加入這些型別：

- `rm -rf`
- `sudo`
- force push
- `git reset --hard`
- `DROP TABLE`
- `kubectl delete`
- `terraform destroy`
- `npm publish`
- `curl | bash`
- 生產環境 deploy

如果你想要“更自動化”，請先明確你是**真的需要**，而不是隻是覺得方便。

---

## permission modes

permission modes 決定 Claude 在本機能做什麼，以及什麼時候會請求你確認。

### 常見模式

- `default`
- `acceptEdits`
- `plan`
- `dontAsk`
- `bypassPermissions`
- `auto`

### 如何理解

| 模式 | 適合什麼 |
|------|----------|
| `default` | 日常安全使用 |
| `acceptEdits` | 希望編輯流暢一些 |
| `plan` | 只想分析，不想改 |
| `dontAsk` | 非互動腳本 |
| `bypassPermissions` | 可信環境中的強自動化 |
| `auto` | 有更高自動化訴求、且明確接受風險 |

### 一個常見誤區

很多人以為許可權模式只是“麻煩不麻煩”。  
其實它決定的是：

- 風險控制
- 自動化強度
- 你是否還能及時攔住錯誤操作

---

## print mode / headless usage

`claude -p` 是 Claude Code 進入自動化世界的關鍵入口。

適合：

- shell 腳本
- CI/CD
- 一次性任務
- 管道輸入
- 結構化輸出

例如：

```bash
claude -p "Run tests and summarize failures"
cat error.log | claude -p "Explain this error"
```

### print mode 使用建議

- 任務儘量清晰明確
- 一開始先用小任務試
- 不要直接上高許可權全自動流程
- 需要 JSON 輸出時，先確認消費端怎麼解析

---

## background tasks 與 scheduled tasks

### background tasks

適合：

- 長時間執行的任務
- 不想阻塞當前對話
- 需要並行推進的工作

### scheduled tasks

適合：

- 週期性檢查
- 定時重複 prompt
- 簡單提醒或輪詢式任務

如果你還沒掌握 print mode 和許可權模式，先別急著把 scheduled tasks 做複雜。

---

## session management

session 管理能力在任務複雜後會非常重要。

高頻場景：

- 復原之前的工作
- 給當前任務命名
- 從當前 session 分叉實驗

常見操作：

- `/resume`
- `/rename`
- `/branch`（較新的主名稱，部分環境中 `/fork` 仍可能作為相容別名出現）
- `claude -c`
- `claude -r "session-name"`

如果你不命名 session，後期會越來越難管理。

---

## remote / web / desktop

這些能力適合：

- 在多臺機器間切換
- 在本機和雲端之間接力
- 用 desktop 做更好的視覺化 diff 或會話管理

對於新手，先知道它們存在即可。  
真正要用時，再重點看網路和許可權環境。

---

## worktrees

worktrees 特別適合：

- 多分支並行方案
- 大任務拆成多個實驗方向
- 和 planning mode / agent workflows 配合

如果你已經開始同時試兩三種實現路線，worktrees 會非常有價值。

---

## sandboxing

sandboxing 的核心不是“更麻煩”，而是“更安全地控制 Claude 的能力範圍”。

適合：

- 風險敏感環境
- 企業環境
- 希望限制檔案系統或網路訪問

不適合：

- 你還沒搞清當前工具鏈本身怎麼跑

---

## configuration 與環境變數

高階能力很多都會回到設定層，例如：

- permission mode
- thinking effort
- channels
- auto mode
- plugins
- MCP

所以你最終還是會需要理解：

- settings 檔案
- CLI flags
- 環境變數

如果你想長期高效使用 Claude Code，這一步繞不過去。

---

## 新手使用者特別注意

### 1. 自動化前先看網路

如果你要用：

- `claude -p`
- remote / web / desktop
- MCP
- plugins

先確認：

- API 訪問
- GitHub 連通性
- npm / uv / Python 依賴下載
- 公司代理程式和證書環境

### 2. 先理解許可權，再追求自動化

很多人會一開始就想“全自動”，但許可權模式沒搞清時，這很容易出事。

### 3. Windows / WSL 差異要提前確認

高階特性裡很多命令和腳本預設更貼近 Unix 生態。

---

## 常見坑

### 1. 把 advanced features 全當成“酷炫功能”

它們本質上是控制力、風險邊界和自動化能力，不只是花哨選項。

### 2. 還沒理解許可權就開高自動化

這會讓“讓 Claude 幫忙”很快變成“讓 Claude 瞎動”。

### 3. print mode 用得太重太快

建議從日誌解釋、測試摘要、靜態分析這種低風險任務開始。

### 4. session 不命名

長任務一多，後面很難找回。

---

## Troubleshooting

如果高階功能“看起來有、實際上跑不起來”，優先檢查：

1. 許可權模式是否合適
2. 當前命令是否應該用互動模式還是 print mode
3. 環境變數是否齊全
4. 遠端或外部服務是否可訪問
5. 當前是否受網路、代理程式、公司策略影響

---

## Best Practices

- 先掌握 planning mode、permission modes、print mode、background tasks
- 先小範圍試自動化，再逐漸放權
- 高風險任務優先用 plan / checkpoints / worktrees 保護自己
- 新手使用者優先排除網路和 shell 環境問題

---

## 推薦下一步

- 想把高階能力接進腳本：看 [10-cli](../10-cli/)
- 想打包團隊工作流：看 [07-plugins](../07-plugins/)
- 想理解 checkpoint 和安全試錯：看 [08-checkpoints](../08-checkpoints/)
