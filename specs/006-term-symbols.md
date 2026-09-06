# Feature: Term Symbol Parsing and Computation

## Overview

Add support for parsing and computing ground-state term symbols (e.g. `4F9/2` for Fe) from electronic configurations. The `IonizationEnergy` model already stores `ground_level` (term symbol + J value) but there's no parsing, validation, or computation. Pymatgen stores `ground_state_term_symbol` as a string attribute. Computing term symbols from electronic configuration + Hund's rules is a useful educational and scientific tool.

## API Design

```python
@dataclass
class TermSymbol:
    """A spectroscopic term symbol 2S+1 L_J."""
    multiplicity: int          # 2S+1 (singlet, doublet, triplet, ...)
    letter: str                # S, P, D, F, G, ...
    j: Fraction | float       # total angular momentum quantum number
    seniority: int | None = None  # for f-electron systems

    @classmethod
    def from_string(cls, s: str) -> "TermSymbol":
        """Parse '4F9/2' -> TermSymbol(multiplicity=4, letter='F', j=Fraction(9,2))"""

    def __str__(self) -> str:  # -> '4F9/2'
    def __repr__(self) -> str: ...

    @property
    def L(self) -> int:
        """Orbital angular momentum quantum number (S=0, P=1, D=2, F=3, ...)."""

    @property
    def S(self) -> float:
        """Total spin quantum number."""

class Element:
    def ground_term_symbol(self) -> TermSymbol | None:
        """Compute the ground-state term symbol from the electronic configuration
        using Hund's rules. Returns None for noble gases or incomplete configs."""
```

## Implementation Steps

1. Create `mendeleev/term_symbol.py` with `TermSymbol` dataclass.
2. Implement `TermSymbol.from_string()` — regex parser for standard notation.
3. Implement `Element.ground_term_symbol()` — derive from `self.ec` (ElectronicConfiguration):
   - Identify the subshell being filled (last subshell with unpaired electrons).
   - Apply Hund's rules to determine S, L, J.
4. Map L values to spectroscopic letters (S/P/D/F/G/H/I).
5. Tests: verify against known term symbols (C: `3P0`, N: `4S3/2`, Fe: `5D4`, O: `3P2`).
6. Docs: add example to electronegativity or electronic configuration docs.

## Effort

**L** — Hund's rules implementation is non-trivial, especially for d- and f-electron systems with intermediate coupling. The parser is straightforward; the computation needs careful handling of degenerate ground states. ~200 lines.

## References

- pymatgen `ground_state_term_symbol`: https://github.com/materialsproject/pymatgen/blob/master/src/pymatgen/core/periodic_table.py
- Hund's rules: https://en.wikipedia.org/wiki/Hund%27s_rules
- Spectroscopic notation: https://en.wikipedia.org/wiki/Term_symbol
- NIST Atomic Spectra Database Levels: https://physics.nist.gov/PhysRefData/ASD/index.html
