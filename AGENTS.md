# AGENTS.md — Mendeleev

Pythonic periodic table library. SQLAlchemy models + SQLite db (`mendeleev/elements.db`).

## Dev commands

```bash
poetry install                    # core deps only
poetry install --with vis         # add bokeh/plotly/seaborn
poetry install --with vis,docs    # add vis + docs deps (nbsphinx, ipykernel)
poetry run pytest                 # runs with -n auto (xdist) by default
poetry run pytest -k "element"    # pattern match
poetry run pytest tests/test_element.py::test_element  # single test
poetry run pytest --cov=mendeleev # coverage
pre-commit run --all-files        # ruff lint + format (must pass before commit)
cd docs && poetry run make html   # build docs (needs --with docs)
poetry run inv render-data-docs   # regenerate data reference rst from PropertyMetadata
poetry run inv export             # dump db tables to csv/json/html/md/sql
```

## Architecture

- **`mendeleev/mendeleev.py`** — main entrypoint: `element()`, `isotope()`, `get_all_elements()`
- **`mendeleev/models.py`** — all SQLAlchemy models (Element, Isotope, Ion, etc.)
- **`mendeleev/db.py`** — creates read-only SQLite engine by default (URI with `?mode=ro`)
- **`mendeleev/fetch.py`** — `fetch_table()` for pandas access
- **`mendeleev/__init__.py`** — dynamic `__getattr__` so `from mendeleev import C` works
- **CLI**: `element.py <symbol|name|number>` via `mendeleev.cli:clielement`

## Key conventions

- **Ruff only** for linting + formatting (v0.3.3). No typechecker (mypy/pyright) configured.
- **pre-commit excludes** `alembic/` and `notebooks/`
- Database is **read-only by default** via URI parameter. Alembic needs write access.
- Adding a property: update model → alembic revision → upgrade → update PropertyMetadata → `inv render-data-docs`
- Tests use `-n auto` (pytest-xdist). Set `PYTEST_ADDOPTS=""` to override. **Use pytest-style tests only** — plain functions with `assert`, no `unittest.TestCase` or class-based tests.
- CI matrix: 3 OS × 5 Python versions (3.10–3.14). Runs ruff (pre-commit) then pytest.
- Documentation uses **sphinx-immaterial** theme (fork of sphinx-material). Workaround: `object_description_options` disables `generate_synopses` to avoid a sphinx-immaterial KeyError. If upgrading sphinx-immaterial or Sphinx, try removing that workaround first. Notebooks in `docs/source/notebooks/` are rendered by nbsphinx. Dev notebooks in root `notebooks/` are ignored by pre-commit.
- Package published to PyPI on tags via trusted publishing (no password needed).
