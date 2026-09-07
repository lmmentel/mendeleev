# Feature: Element Serialization

## Overview

Add `to_dict()`, `to_dataframe()`, and `to_json()` methods to `Element` (and other model classes) for easy export to common data formats. This is the most-requested missing feature and is critical for ML pipelines, interop with other libraries, and general developer ergonomics. Pymatgen's `Element.data` dict is a key part of its appeal.

## API Design

```python
class Element:
    def to_dict(self, exclude: list[str] | None = None) -> dict[str, Any]:
        """Return element data as a plain dict.

        Args:
            exclude: attribute names to omit (e.g. ['description', 'uses'])

        Returns:
            dict mapping attribute names to their values (None for missing data)
        """

    def to_json(self, path: str | Path | None = None, **kwargs) -> str | None:
        """Serialize to JSON.

        Args:
            path: if given, write JSON to this file; otherwise return string
            **kwargs: forwarded to json.dumps (e.g. indent=2)

        Returns:
            JSON string if path is None, else None
        """

    def to_dataframe(self) -> "pd.DataFrame":
        """Return a single-row DataFrame with the element as a row."""
```

Also on `Isotope`:
```python
class Isotope:
    def to_dict(self, exclude: list[str] | None = None) -> dict[str, Any]: ...
```

Module-level convenience:
```python
def to_dataframe(elements: list[Element]) -> pd.DataFrame:
    """Convert multiple elements to a DataFrame (one row per element)."""
```

## Implementation Steps

1. Add `to_dict()` to `Element` — iterate column attributes via SQLAlchemy `inspect()`, skip relationships, handle `None`.
2. Add `to_json()` — call `to_dict()` + `json.dumps()`, optional file write.
3. Add `to_dataframe()` — `pd.DataFrame([self.to_dict()])` with `atomic_number` as index.
4. Add same methods to `Isotope`.
5. Add module-level `to_dataframe(elements)` convenience.
6. Tests: round-trip `to_dict()` -> reconstruct values; JSON validity; DataFrame shape.
7. Update `quick.rst` with example.

## Effort

**S** — Pure Python, no DB migration, no new dependencies. ~50 lines of code.

## Cross-language comparison

| Package | Language | Has serialization? | Notes |
|---------|----------|-------------------|-------|
| pymatgen | Python | Yes | `Element.data` dict, `Element.to_json()` |
| molmass | Python | Yes | `Element` dataclass with all fields |
| Mendeleev.jl | Julia | Yes | `ChemElem` struct with ~80 fields, Julia dict access |
| Chemistry.NET | C# | Yes | `Element` properties, JSON serialization |
| periodictable | Python | Partial | `Element` attributes but no explicit serialization |
| BioJava | Java | Partial | `Element` enum with accessor methods |

## References

- pymatgen `Element.data` property: https://github.com/materialsproject/pymatgen/blob/master/src/pymatgen/core/periodic_table.py
- ROADMAP.md item #5
- molmass `Element` dataclass: https://github.com/cgohlke/molmass
