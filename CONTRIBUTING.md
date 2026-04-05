<picture>
  <source media="(prefers-color-scheme: dark)" srcset="resources/logos/claude-howto-logo-dark.svg">
  <img alt="Claude How To" src="resources/logos/claude-howto-logo.svg">
</picture>

# Contributing

歡迎為這個繁體中文化倉庫繼續貢獻內容。

## 貢獻方向

- 改進中文表達
- 補充新手使用者常見坑
- 修復無效連結和錯誤範例
- 補全教學、範本、skills、plugins 範例
- 同步上游更新

## 提交前請先看

- [UPSTREAM.md](UPSTREAM.md)
- [LOCALIZATION-STYLE.md](LOCALIZATION-STYLE.md)

## 本機驗證

```bash
uv venv
uv pip install -r scripts/requirements-dev.txt
uv run python scripts/validate_localization.py
uv run pytest scripts/tests/ -q
```

## 貢獻原則

- 不要把可執行標識翻壞
- 不要隨意改目錄結構和檔名
- 修改時儘量保持和上游對映關係清楚
