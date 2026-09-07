# Feature: Chemical Formula Parser

## Overview

Add a `Formula` class for parsing chemical formulas, computing molecular weight, mass fractions, and Hill notation. Chemical formula parsing is a fundamental chemistry utility — periodictable, chemformula, molmass, and chemsynthcalc all provide it. Mendeleev's existing `coeffs()` in utils.py is primitive. A formula parser also enables X-ray/neutron SLD calculations (#11, #13).

## API Design

```python
class Formula:
    """A parsed chemical formula.

    Args:
        formula: string like "H2O", "Fe2(SO4)3", "Ca(OH)2·H2O"
    """

    def __init__(self, formula: str) -> None: ...

    @property
    def composition(self) -> dict[str, int]:
        """Element symbol -> count, e.g. {'H': 2, 'O': 1}"""

    @property
    def molecular_weight(self) -> float:
        """Formula weight in g/mol using mendeleev atomic weights."""

    @property
    def mass_fractions(self) -> dict[str, float]:
        """Element symbol -> mass fraction (0-1)."""

    @property
    def hill_notation(self) -> str:
        """Formula in Hill notation (C first, then H, then alphabetical)."""

    @property
    def element_count(self) -> int:
        """Total number of atoms."""

    def __repr__(self) -> str: ...
    def __str__(self) -> str: ...
    def __mul__(self, n: int) -> "Formula": ...
    def __add__(self, other: "Formula") -> "Formula": ...
```

Convenience function:
```python
def molecular_weight(formula: str) -> float:
    """Shorthand for Formula(formula).molecular_weight."""
```

## Implementation Steps

1. Create `mendeleev/formula.py` with `Formula` class.
2. Implement formula tokenizer/parser (regex-based, handle parentheses, hydrates, charges).
3. Implement `molecular_weight` using `element(sym).atomic_weight`.
4. Implement `mass_fractions`, `hill_notation`.
5. Add `__mul__` and `__add__` for stoichiometric arithmetic.
6. Tests: parse ~20 formulas (H2O, Ca(OH)2, Fe2(SO4)3·5H2O, [Cu(NH3)4]SO4, C8H10N4O2), verify molecular weights against known values.
7. Update `quick.rst` with example.

## Effort

**M** — Pure Python, no DB changes. Parser is ~100 lines; rest is straightforward. No new dependencies.

## Cross-language comparison

| Package | Language | Has formula parser? | Notes |
|---------|----------|---------------------|-------|
| molmass | Python | Yes | `Formula` class: molecular weight, composition, mass spectrum, Hill notation |
| chemformula | Python | Yes | `ChemFormula`: LaTeX/HTML output, arithmetic, CAS numbers |
| Chemaxon JChem | Java | Yes | `Formula` class with molecular weight, formula parsing |
| Mendeleev.jl | Julia | No | Gap — not implemented |
| Chemistry.NET | C# | Yes | `ChemicalFormula` class, isotopic distribution |
| Dart quds | Dart | Yes | `Atom` class with formula parsing |
| periodictable | Python | Yes | `Formulas` module: `formula("H2O")`, molecular weight |

## References

- periodictable formulas: https://periodictable.readthedocs.io/en/latest/api/formula.html
- chemformula: https://github.com/molshape/chemformula
- molmass: https://github.com/cgohlke/molmass
- chemsynthcalc: https://pypi.org/project/chemsynthcalc/
- chemistry-tools parser: https://chemistry-tools.readthedocs.io/en/latest/api/formulae/parser.html
