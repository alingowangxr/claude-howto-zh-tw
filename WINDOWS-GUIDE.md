<picture>
  <source media="(prefers-color-scheme: dark)" srcset="resources/logos/claude-howto-logo-dark.svg">
  <img alt="Claude How To" src="resources/logos/claude-howto-logo.svg">
</picture>

# Windows 使用指南

本倉庫的大多數腳本和命令預設以 Unix / macOS / Linux 環境為基礎撰寫。  
如果你在 Windows 上使用 Claude Code，這頁集中說明你會遇到的差異點和解法。

---

## 先決定你用哪個環境

在 Windows 上跑 Claude Code，最常見的三種環境：

| 環境 | 特點 | 建議給誰 |
|------|------|----------|
| **WSL 2**（推薦） | 最接近 Unix 環境，相容性最好 | 有一點 Linux 基礎、長期要用 hooks / MCP / scripts 的人 |
| **Git Bash** | 輕量，支援大多數 shell 命令 | 只需要基本命令和 git 操作的人 |
| **PowerShell** | Windows 原生，功能完整 | 主要在 Windows 生態工作、不打算裝 WSL 的人 |

**建議**：沒有特殊限制的話，優先選 WSL 2，後續踩到環境問題的機率最低。

---

## 安裝 Claude Code

```powershell
# 先確認 Node.js 已安裝（建議 18+）
node --version

# 安裝 Claude Code CLI
npm install -g @anthropic-ai/claude-code

# 確認安裝成功
claude --version
```

如果 `npm install -g` 失敗，可能是權限問題，用管理員身分開啟 PowerShell 再試。

---

## WSL 2 環境設定

### 安裝 WSL 2

```powershell
# 在 PowerShell（管理員）執行
wsl --install

# 安裝完重啟後，設定預設版本
wsl --set-default-version 2
```

### 在 WSL 2 裡安裝 Claude Code

```bash
# 在 WSL bash 裡
curl -fsSL https://deb.nodesource.com/setup_20.x | sudo -E bash -
sudo apt-get install -y nodejs
npm install -g @anthropic-ai/claude-code
```

### WSL 2 的路徑說明

| 你在哪裡 | 存取 Windows 檔案的路徑 |
|----------|------------------------|
| WSL bash | `/mnt/c/Users/你的名字/...` |
| Windows Explorer | `\\wsl$\Ubuntu\home\你的名字\...` |

---

## 環境變數設定

### PowerShell（當次會話）

```powershell
$env:ANTHROPIC_API_KEY = "your_api_key"
$env:GITHUB_TOKEN = "your_github_token"
```

### PowerShell（永久）

```powershell
[System.Environment]::SetEnvironmentVariable("ANTHROPIC_API_KEY", "your_api_key", "User")
```

### Git Bash / WSL

```bash
export ANTHROPIC_API_KEY="your_api_key"
export GITHUB_TOKEN="your_github_token"

# 永久寫入
echo 'export ANTHROPIC_API_KEY="your_api_key"' >> ~/.bashrc
source ~/.bashrc
```

---

## Shell 腳本相容性

倉庫裡的 `.sh` 腳本（如 `06-hooks/*.sh`、`10-cli/*.sh`）都是 bash 語法。

| 環境 | 執行方式 |
|------|----------|
| WSL 2 | 直接 `bash script.sh` 或 `chmod +x && ./script.sh` |
| Git Bash | 直接 `bash script.sh` |
| PowerShell | 需要先啟動 Git Bash 或 WSL，或改用 PowerShell 版本 |

**在 PowerShell 中執行 bash 腳本**：

```powershell
# 方法 1：透過 Git Bash
"C:\Program Files\Git\bin\bash.exe" script.sh

# 方法 2：透過 WSL
wsl bash script.sh
```

---

## MCP Server（npx 相關）

很多 MCP server 透過 `npx` 安裝和執行。在 Windows 下可能遇到：

### 問題：`npx` 執行 MCP server 失敗

**原因**：Windows 路徑中有空格或特殊字元。

**解法**：在 MCP 設定裡改用 `cmd /c` 形式：

```json
{
  "mcpServers": {
    "github": {
      "command": "cmd",
      "args": ["/c", "npx", "-y", "@modelcontextprotocol/server-github"],
      "env": {
        "GITHUB_PERSONAL_ACCESS_TOKEN": "your_token"
      }
    }
  }
}
```

### 問題：首次安裝很慢

`npx` 第一次執行時會下載套件，在台灣網路環境可能需要 1–5 分鐘。  
建議先確認：

- npm registry 是否可正常連線
- 是否需要設定代理程式（見下方）

---

## 代理程式設定

如果你在公司網路或需要代理：

### npm 代理

```bash
npm config set proxy http://proxy.company.com:8080
npm config set https-proxy http://proxy.company.com:8080
```

### Git 代理

```bash
git config --global http.proxy http://proxy.company.com:8080
```

### WSL 代理

```bash
export http_proxy=http://proxy.company.com:8080
export https_proxy=http://proxy.company.com:8080
```

---

## Hooks 在 Windows 下的注意事項

`06-hooks/` 裡的範例腳本預設 bash 環境。在 Windows 下：

1. **路徑寫法**：設定檔裡的路徑要用正斜線或跳脫反斜線

```json
{
  "hooks": {
    "PreToolUse": [{
      "matcher": "Bash",
      "hooks": [{
        "type": "command",
        "command": "bash /c/Users/你的名字/.claude/hooks/pre-commit.sh"
      }]
    }]
  }
}
```

2. **Python hooks**：確認 `python3` 在 PATH 裡，或改用 `python`（視安裝方式而定）

3. **Git Bash 使用者**：把 hooks 腳本放在 `~/.claude/hooks/` 時，路徑是 Git Bash 的 home，通常是 `C:\Users\你的名字\.claude\hooks\`

---

## Python / uv 環境

部分腳本（如 `09-advanced-features/setup-auto-mode-permissions.py`）需要 Python。

```powershell
# 確認 Python 已安裝
python --version

# 安裝 uv（推薦的 Python 管理工具）
pip install uv

# 執行需要 uv 的腳本
uv run python scripts/validate_localization.py
```

在 WSL 2 裡：

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
uv run python scripts/validate_localization.py
```

---

## 常見錯誤速查

| 錯誤訊息 | 原因 | 解法 |
|----------|------|------|
| `'claude' is not recognized` | Claude Code 未安裝或不在 PATH | `npm install -g @anthropic-ai/claude-code`，重開終端 |
| `ANTHROPIC_API_KEY not set` | 環境變數未設定 | 見上方「環境變數設定」 |
| `npx: command not found` | Node.js 未安裝 | 安裝 Node.js 18+ |
| `permission denied` on `.sh` | 腳本沒執行權限 | `chmod +x script.sh`（WSL / Git Bash） |
| MCP server 連不上 | Token 未設定或網路問題 | 檢查 token scope 和代理程式設定 |
| `\r` 換行符號錯誤 | Windows CRLF 換行 | `dos2unix script.sh` 或設定 `git config core.autocrlf false` |

---

## 推薦下一步

- 想設定 hooks：看 [06-hooks](06-hooks/)
- 想接 MCP：看 [05-mcp](05-mcp/)
- 想用 CLI 自動化：看 [10-cli](10-cli/)
- 想查常用命令：看 [QUICK_REFERENCE.md](QUICK_REFERENCE.md)
