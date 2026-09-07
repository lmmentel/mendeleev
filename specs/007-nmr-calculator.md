# Feature: NMR Calculator

## Overview

Add NMR (Nuclear Magnetic Resonance) utility functions using existing isotope data. Compute gyromagnetic ratio, Larmor frequency at a given field strength, and relative receptivity.

**Existing data in mendeleev:** The `Isotope` model already stores all required inputs: `g_factor` (dimensionless magnetic moment), `spin` (nuclear spin quantum number as string), `quadrupole_moment` (float), and `abundance` (natural abundance). These are accessible via `element("H").isotopes[0].g_factor` etc. However, there's no NMR-specific API — no gyromagnetic ratio computation, no Larmor frequency calculation, no receptivity comparison. Periodictable has a full `nmr` module; pymatgen stores quadrupole moments but no calculator.

## API Design

```python
class Isotope:
    def gyromagnetic_ratio(self) -> float | None:
        """Gyromagnetic ratio in MHz/T.

        Computed from the g-factor and nuclear magneton:
        gamma = g * mu_N / h, where mu_N = 5.05078e-27 J/T, h = 6.626e-34 J·s.
        Returns None if g_factor is not available.
        """

    def larmor_frequency(self, field: float) -> float | None:
        """Larmor frequency in MHz for a given magnetic field strength (in Tesla).

        f = gamma * B / (2 * pi)  where gamma is the gyromagnetic ratio.
        Returns None if g_factor is not available.
        """

    def receptivity(self, reference: str = "1H") -> float | None:
        """Relative NMR receptivity compared to a reference isotope.

        Receptivity scales as gamma^2 * I * (I+1) * abundance,
        where I is the spin quantum number.
        Args:
            reference: isotope to normalize to (default: 1H).
        Returns:
            ratio (dimensionless), or None if data is missing.
        """
```

Convenience functions:
```python
def larmor_frequency(isotope: str, field: float) -> float | None:
    """Shorthand: larmor_frequency("1H", 11.74) -> 500.0 MHz."""

def receptivity(isotope: str, reference: str = "1H") -> float | None:
    """Shorthand for receptivity comparison."""
```

## Implementation Steps

1. Create `mendeleev/nmr.py` with standalone functions.
2. Add `gyromagnetic_ratio()`, `larmor_frequency()`, `receptivity()` to `Isotope`.
3. Implement gyromagnetic ratio from g_factor: `gamma = g * mu_N / h`.
4. Implement receptivity: `gamma^2 * I*(I+1) * abundance` normalized to reference.
5. Tests: verify 1H at 11.74T = 500 MHz; 13C receptivity vs 1H (~0.016).
6. Docs: add NMR section to tutorials or FAQ.

## Effort

**M** — Straightforward physics calculations using stored data. ~80 lines.

## Cross-language comparison

| Package | Language | Has NMR calculator? | Notes |
|---------|----------|---------------------|-------|
| periodictable | Python | Yes | Full `nmr` module: `nmr.gamma`, `nmr.frequency`, `nmr.receptivity` |
| Mendeleev.jl | Julia | Yes | `gyromagnetic_ratio`, `larmor_frequency` on isotopes |
| pymatgen | Python | Partial | `Element.gi` (quadrupole moment) only — no frequency or receptivity |
| MolSSI | Python | Yes | `psi4` has NMR constants |
| Chemaxon | Java | No | Not implemented |

## References

- Gyromagnetic ratio: https://en.wikipedia.org/wiki/Gyromagnetic_ratio
- NMR receptivity: https://en.wikipedia.org/wiki/Nuclear_magnetic_resonance#Receptivity
- NIST fundamental physical constants: https://physics.nist.gov/cgi-bin/cuu/Value?mun
- Bruker NMR frequency table: https://www.bruker.com/en/products-and-solutions/mr/nmr/nmr-frequency-table.html
