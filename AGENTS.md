# AGENTS.md

> Guidelines for agentic coding agents operating in this repository.

## Project Overview

This is a **documentation repository** (Chinese localization of `claude-howto`) — not a software application. It contains Markdown guides, Python tooling (EPUB builder + localization validator), and Claude Code skill definitions.

**Primary languages:** Markdown (docs), Python 3.10+ (scripts)
**Package manager:** `uv` (Astral)

---

## Commands

### Setup

```bash
uv venv
uv pip install -r scripts/requirements-dev.txt
```

### Tests (pytest)

```bash
# Run all tests
uv run pytest scripts/tests/ -v

# Run a single test file
uv run pytest scripts/tests/test_build_epub.py -v

# Run a single test function
uv run pytest scripts/tests/test_build_epub.py::test_epub_config_defaults -v

# Run with coverage
uv run pytest scripts/tests/ -v --tb=short --cov=scripts --cov-report=xml --cov-report=term-missing
```

**pytest config** (`scripts/pyproject.toml`): `asyncio_mode = "auto"`, `addopts = "-v"`, test paths = `["scripts/tests"]`

### Lint & Format

```bash
# Python format check
uv run ruff format --check scripts/

# Python auto-format
uv run ruff format scripts/

# Python lint
uv run ruff check scripts/

# Python lint with auto-fix
uv run ruff check --fix scripts/

# Security scan
uv run bandit -c scripts/pyproject.toml -r scripts/ --exclude scripts/tests/

# All pre-commit hooks
pre-commit run --all-files

# Markdown lint (CI uses global npm)
markdownlint '**/*.md'

# Localization validation (must pass before committing doc changes)
uv run python scripts/validate_localization.py
```

### Build

```bash
# Build EPUB ebook from all Markdown content
uv run scripts/build_ep.py
```

---

## Python Code Style

**Tooling:** Ruff (linter + formatter), Bandit (security)

### Imports

- Sorted by `isort` rules (via Ruff)
- Standard library → third-party → first-party (`build_epub`)
- `combine-as-imports = true`

### Formatting

- Line length: 88 (enforced by Ruff formatter)
- Double quotes for strings
- Space indentation (4 spaces)
- Trailing commas preserved

### Type Hints

- Use type hints for function signatures
- `TCH003` (type-checking imports) is ignored — not enforced strictly

### Naming

- Follow PEP 8 conventions
- Function/method names: `snake_case`
- Class names: `PascalCase`
- Constants: `UPPER_SNAKE_CASE`
- Private members: leading underscore prefix

### Error Handling

- Be explicit — never bare `except:`
- Use specific exception types
- Bandit `B110` (pass in except) is not explicitly skipped — avoid silent failures

### Ignored Ruff Rules

| Rule | Reason |
|------|--------|
| `E501` | Line length handled by formatter |
| `PLR0913` | Too many arguments |
| `PLR2004` | Magic value comparison |
| `PLR0915` | Too many statements |
| `PERF203` | try-except in loop (acceptable) |
| `PERF403` | Dict comprehension (readability) |
| `TC003` | Type-checking imports |
| `PLC0415` | Import not at top level |
| `RUF005` | Collection concatenation |

### Test Files

- `S101` (assert) and `PLR2004` ignored in `scripts/tests/*.py`
- Use `pytest` fixtures from `conftest.py`
- Async tests use `asyncio_mode = "auto"` — no need for `@pytest.mark.asyncio`

---

## Markdown Documentation Style

This repo's primary content is Markdown docs in Chinese. Follow these rules:

### Localization Rules (from `LOCALIZATION-STYLE.md`)

- **Never translate** executable identifiers: filenames, directory names, slash commands, skill/plugin names, frontmatter keys, JSON/YAML keys, CLI commands, flags, environment variables, MCP server names, path placeholders
- **Keep English** for high-frequency terms: `skills`, `hooks`, `MCP`, `subagents`, `plugins`, `CLI`, `slash commands`, `checkpoints`, `session`, `worktree`
- First occurrence format: `skills`（可複用能力）— keep English, add Chinese explanation
- Short sentences preferred; avoid translation-style long sentences
- Structure: what it is → when to use → prerequisites → how to install/configure → common pitfalls

### Risk Levels for Editing

| Risk | Files | Rules |
|------|-------|-------|
| Low | README, learning guides, FAQ, comparison tables | Full Chinese rewrite OK |
| Medium | `SKILL.md`, subagent `.md`, slash command `.md` | Only translate human-readable text; preserve protocol format, field names, commands, identifiers |
| High | `.json`, `.yml`, `.yaml`, `.py`, `.sh`, GitHub Actions | No functional changes; only edit comments or user-facing copy if needed |

### File Naming

- Keep original directory names and filenames
- Do not rename executable files to Chinese

---

## Clean Code Principles (from `clean-code-rules.md`)

- Names should express intent
- Functions should be short with a single responsibility
- Avoid valueless comments
- Don't repeat yourself
- Error handling must be explicit
- Prioritize readability over cleverness

---

## CI/CD

| Workflow | Trigger | Key Jobs |
|----------|---------|----------|
| `ci.yml` | Push/PR to `main` | lint, localization-guard, security, test (3.10/3.11/3.12), build EPUB |
| `test.yml` | Push to `main`/`develop` (scripts paths) | pytest (3 versions), lint, security, mypy, build EPUB |
| `docs-check.yml` | Push/PR to `main` (markdown paths) | markdown-lint, link-check, cspell, frontmatter validation |
| `release.yml` | Git tags `v*` | Build EPUB + GitHub Release |

---

## Key Directories

```
01-slash-commands/   # Slash command templates
02-memory/           # CLAUDE.md memory examples
03-skills/           # Reusable skill examples
04-subagents/        # Subagent definitions
05-mcp/              # MCP server configs
06-hooks/            # Hook scripts (.sh, .py)
07-plugins/          # Plugin examples
08-checkpoints/      # Checkpoint usage guide
09-advanced-features/ # Advanced features
10-cli/              # CLI reference
scripts/             # Python tooling (EPUB builder, validation, tests)
.claude/skills/      # Project-level Claude Code skills
.github/workflows/   # CI/CD pipelines
```

---

## Pre-commit Hooks

Run `pre-commit install` to enable. Hooks: Ruff lint, Ruff format, Bandit security, YAML check, TOML check, EOF fixer, trailing whitespace fix, large file check (>1000KB), merge conflict check.
