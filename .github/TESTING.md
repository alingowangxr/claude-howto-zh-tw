# Testing Guide

本專案的測試主要覆蓋兩類內容：

- Python 腳本與 EPUB 構建
- 在地化校驗腳本與相關守護邏輯

## 本機執行

```bash
uv venv
uv pip install -r scripts/requirements-dev.txt
uv run pytest scripts/tests/ -v
uv run python scripts/validate_localization.py
```

## 關注點

- EPUB 是否還能正常構建
- 中文化是否破壞 frontmatter、JSON/YAML、shell 腳本
- 關鍵受保護標識是否還存在
