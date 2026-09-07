# Feature: PEP 561 py.typed Marker

## Overview

Add a `py.typed` marker file so that type checkers (mypy, pyright) recognize mendeleev as a typed package. This is a standard practice for modern Python libraries and was recently added to periodictable (v2.1.0). Mendeleev already has reasonable type annotations in function signatures but lacks the marker file.

## API Design

No API changes. Add an empty `mendeleev/py.typed` marker file and ensure it's included in the sdist/wheel via `pyproject.toml` or `MANIFEST.in`.

## Implementation Steps

1. Create empty `mendeleev/py.typed` file.
2. Add to `pyproject.toml` under `[tool.setuptools.package-data]`:
   ```toml
   mendeleev = ["py.typed"]
   ```
3. Optionally run mypy or pyright on the codebase to identify and fix the most egregious type errors (not a blocker — the marker itself is the deliverable).
4. Tests: verify `importlib.resources` can find `py.typed`.

## Effort

**S** — One empty file + one line in pyproject.toml. ~5 minutes.

## Cross-language comparison

| Package | Language | Has py.typed? | Notes |
|---------|----------|--------------|-------|
| periodictable | Python | Yes | Added in v2.1.0 |
| pymatgen | Python | Yes | PEP 561 compliant |
| molmass | Python | No | Not implemented |
| chemformula | Python | No | Not implemented |

## References

- PEP 561: https://peps.python.org/pep-0561/
- periodictable v2.1.0 added py.typed: https://github.com/python-periodictable/periodictable
- mypy py.typed docs: https://mypy.readthedocs.io/en/stable/installed_packages.html#making-pep-561-compliant-packages
