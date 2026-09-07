# Feature: Isotopic Distribution Calculator

## Overview

Compute isotopic distributions (mass spectra) for elements and chemical formulas from existing isotope data. Given a formula like "H2O", compute the probability distribution of molecular masses across all possible isotopologues. This is essential for mass spectrometry workflows and is a key differentiator in molmass, IsoSpecPy, and Chemistry.NET.

**Existing data in mendeleev:** The `Isotope` model stores `mass`, `abundance`, `mass_number`, and `half_life` for each isotope. The `Element.isotopes` relationship provides access to all isotopes of an element. All inputs for distribution computation are already available — no new data or DB columns needed.

## API Design

```python
@dataclass
class IsotopicPeak:
    """A single peak in an isotopic distribution."""
    mass: float           # exact isotopic mass
    intensity: float      # relative intensity (0-1)
    mass_number: int      # nominal mass number

class IsotopicDistribution:
    """Isotopic distribution for an element or formula."""

    def __init__(self, formula: str | None = None, element: str | None = None):
        """Compute distribution from a chemical formula or single element.

        Args:
            formula: chemical formula like "H2O", "C8H10N4O2"
            element: element symbol like "C" (for single-element distribution)
        """

    @property
    def peaks(self) -> list[IsotopicPeak]:
        """All peaks sorted by mass."""

    @property
    def monoisotopic_mass(self) -> float:
        """Mass of the most intense peak."""

    @property
    def average_mass(self) -> float:
        """Weighted average mass (should match Element.atomic_weight)."""

    @property
    def most_abundant_mass(self) -> float:
        """Mass of the highest-abundance peak."""

    def normalized(self, min_intensity: float = 1e-4) -> list[IsotopicPeak]:
        """Return peaks above intensity threshold, normalized to max=1."""

    def __repr__(self) -> str: ...
```

Convenience function:
```python
def isotopic_distribution(formula: str) -> IsotopicDistribution:
    """Shorthand for IsotopicDistribution(formula=formula)."""
```

## Implementation Steps

1. Create `mendeleev/isotopes.py` with `IsotopicPeak` and `IsotopicDistribution`.
2. Implement single-element distribution: iterate isotopes, return peaks.
3. Implement formula distribution: convolve element distributions (Cartesian product of isotopes weighted by atom count).
4. Handle edge cases: missing isotope data, elements with no stable isotopes.
5. Add `isotopic_distribution()` convenience function.
6. Tests: verify C has 2 peaks (12, 13), H2O has correct mass pattern, C8H10N4O2 (caffeine) matches known spectrum.
7. Docs: add mass spectrometry tutorial.

## Effort

**M** — Pure computation from existing data, no DB changes. ~120 lines. The convolution algorithm for multi-element formulas is the main complexity.

## Cross-language comparison

| Package | Language | Has isotopic distribution? | Notes |
|---------|----------|--------------------------|-------|
| molmass | Python | Yes | `Formula.spectrum()` returns mass/intensity arrays |
| IsoSpecPy | Python | Yes | Fine-structure calculator, optimized for large molecules |
| Chemistry.NET | C# | Yes | `IsotopicDistribution` class |
| Mendeleev.jl | Julia | No | Gap — not implemented |
| periodictable | Python | No | Gap — not implemented |
| pymatgen | Python | No | Gap — not implemented |

## References

- molmass isotopic distribution: https://github.com/cgohlke/molmass
- IsoSpecPy: https://pypi.org/project/IsoSpecPy/
- Chemistry.NET `IsotopicDistribution`: https://github.com/Sejoslaw/Chemistry.NET
- Mass spectrometry isotope patterns: https://en.wikipedia.org/wiki/Isotope_pattern
