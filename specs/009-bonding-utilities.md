# Feature: Bonding Utilities

## Overview

Add utilities for computing bond properties from electronegativity differences: ionic character percentage and bond polarity. This is ROADMAP item #1. The building blocks exist (electronegativity scales, `coeffs()` in utils.py) but are not exposed as a coherent bonding module.

## API Design

```python
@dataclass
class Bond:
    """A two-center bond between elements."""
    element1: Element
    element2: Element
    electronegativity_scale: str = "pauling"

    @property
    def en_difference(self) -> float:
        """Electronegativity difference (absolute value)."""

    @property
    def ionic_character(self) -> float:
        """Percent ionic character (Pauling formula):
        % = (1 - exp(-0.25 * delta_chi^2)) * 100"""

    @property
    def bond_polarity(self) -> float:
        """Bond polarity index (0 = nonpolar covalent, 1 = ionic)."""
```

Module-level helpers:
```python
def ionic_character(en1: float, en2: float) -> float:
    """Percent ionic character from two electronegativity values."""

def bond_polarity(en1: float, en2: float) -> float:
    """Bond polarity index from two electronegativity values."""
```

## Implementation Steps

1. Create `mendeleev/bond.py` with `Bond` dataclass and helpers.
2. Implement Pauling ionic character formula.
3. Implement bond polarity (sin-based or Pauling's formula).
4. Tests: NaCl ~67% ionic, H2 ~0%, HF ~43%.
5. Docs: add bonding section to quick.rst.

## Effort

**S** — Pure Python, ~50 lines, no DB changes.

## References

- ROADMAP.md item #1
- Pauling electronegativity and ionic character: https://en.wikipedia.org/wiki/Electronegativity#Electronegativity_and_ionic_character
- Allred-Rochow ionic character
