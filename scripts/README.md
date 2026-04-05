<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../resources/logos/claude-howto-logo-dark.svg">
  <img alt="Claude How To" src="../resources/logos/claude-howto-logo.svg">
</picture>

# EPUB 構建腳本與在地化校驗腳本

這個目錄現在主要包含兩類腳本：

- `build_epub.py`：把倉庫內的 Markdown 檔案打包成 EPUB
- `validate_localization.py`：校驗繁體中文化過程中是否把可執行標識、連結或設定翻壞

---

## `build_epub.py`

用於把整個指南打包成 EPUB 電子書。

當前預設會優先使用倉庫裡的固定封面圖：

`assets/cover/epub-cover-official.png`

如果這個檔案存在，就直接作為 EPUB 封面；如果不存在，才回退到腳本自動生成封面。

### 功能

- 按目錄結構組織章節
- 把 Mermaid 圖透過 Kroki.io 渲染成圖片
- 生成封面
- 處理內部 Markdown 連結
- 在構建失敗時明確報錯

### 依賴

- Python 3.10+
- [uv](https://github.com/astral-sh/uv)
- 可訪問 Kroki.io 的網路環境

### 快速開始

```bash
uv run scripts/build_epub.py
```

### 常見選項

```text
usage: build_epub.py [-h] [--root ROOT] [--output OUTPUT] [--verbose]
                     [--timeout TIMEOUT] [--max-concurrent MAX_CONCURRENT]
```

```bash
# 檢視詳細記錄檔
uv run scripts/build_epub.py --verbose

# 自定義輸出位置
uv run scripts/build_epub.py --output ~/Desktop/claude-guide.epub

# 如果遇到速率限制，降低併發
uv run scripts/build_epub.py --max-concurrent 5
```

---

## `validate_localization.py`

用於在繁體中文化過程中做“翻譯後驗活”，避免這些問題：

- 內部 Markdown 連結失效
- YAML frontmatter 被改壞
- JSON / YAML 無法解析
- shell 腳本語法損壞
- 關鍵命令名、欄位名、環境變數名、plugin manifest 標識被誤改

### 快速開始

```bash
uv run python scripts/validate_localization.py
```

### 它會檢查什麼

- Markdown 相對連結
- frontmatter 合法性
- `.json` / `.yml` / `.yaml` 語法
- `*.sh` 的 `bash -n`
- 關鍵 protected tokens

### 什麼時候執行

- 每次大規模翻譯或重寫之後
- 每次修改 `SKILL.md`、subagent、slash command 或 plugin manifest 之後
- 每次準備提交前
- 每次同步上游變更後

---

## 本機開發

```bash
# 建立虛擬環境
uv venv

# 啟用並安裝相依
source .venv/bin/activate
uv pip install -r scripts/requirements-dev.txt

# 執行全部測試
pytest scripts/tests/ -v

# 執行本地化校驗
uv run python scripts/validate_localization.py

# 構建 EPUB
python scripts/build_epub.py
```

---

## 常見問題

**EPUB 構建失敗且提示網路錯誤**  
先檢查網路、代理程式以及 Kroki.io 是否可訪問，可以嘗試提高 `--timeout`。

**在地化校驗失敗**  
優先檢查：

- 是否把 `/optimize`、`/pr`、`claude -p` 這類命令改壞了
- 是否把 `allowed-tools`、`tools`、`model`、`env` 這類欄位翻譯掉了
- 是否刪掉了 `GITHUB_TOKEN`、`mcpServers`、`license` 等受保護標識

**中文內容導致拼寫檢查報錯**  
倉庫已對中文字元做了忽略處理；如果仍然報錯，多半是英文術語或專案名新增了未收錄詞條。
