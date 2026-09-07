# Feature: X-Ray Transition Energies (NIST SRD 128)

## Overview

Add K and L shell X-ray transition energies from the NIST X-Ray Transition Energies Database (SRD 128). This provides precise Kα1, Kα2, Kβ1, Lα1, Lα2, Lβ1, Lγ1, and edge energies for elements Z=10–100. Essential for XRF, EDX, XPS, and synchrotron spectroscopy workflows.

**Existing data:** Mendeleev has `ScatteringFactor` (f1/f2 vs energy from Henke/LBNL), which is energy-dependent atomic scattering — NOT the same as characteristic X-ray line energies. X-ray transition energies are specific emission/absorption line positions, not scattering factors.

**Data source:** NIST SRD 128 (`https://physics.nist.gov/PhysRefData/XrayTrans/Html/`) — static HTML tables with experimental and theoretical transition energies. Covers Z=10 (Ne) to Z=100 (Fm). Both experimental (SI-consistent) and theoretical values are provided.

## API Design

New model and table:

```python
class XrayTransitionEnergy(Base, ReprMixin):
    """Characteristic X-ray transition energies from NIST SRD 128."""
    __tablename__ = "xraytransitionenergies"

    id = Column(Integer, primary_key=True)
    atomic_number = Column(Integer, ForeignKey("elements.atomic_number"), nullable=False)

    transition = Column(String, nullable=False)     # e.g. "KL3", "L3M5"
    transition_name = Column(String)                 # e.g. "Kalpha1", "Lalpha1"
    shell = Column(String)                           # "K", "L1", "L2", "L3"
    subshell_from = Column(String)                   # initial shell
    subshell_to = Column(String)                     # final shell

    energy_experimental = Column(Float)              # eV (experimental)
    energy_theoretical = Column(Float)               # eV (theoretical)
    wavelength = Column(Float)                       # Angstroms (computed from energy)

    element = relationship("Element", back_populates="xray_transitions")
```

Access via `Element`:
```python
class Element:
    @property
    def xray_transitions(self) -> list["XrayTransitionEnergy"]:
        """All X-ray transition energies for this element."""

    def xray_line(self, transition: str) -> "XrayTransitionEnergy | None":
        """Get a specific X-ray line, e.g. element("Fe").xray_line("KL3") -> Kα1."""

    @property
    def k_alpha1(self) -> float | None:
        """Kα1 transition energy in eV."""

    @property
    def k_alpha2(self) -> float | None:
        """Kα2 transition energy in eV."""

    @property
    def k_beta1(self) -> float | None:
        """Kβ1 transition energy in eV."""

    @property
    def l_alpha1(self) -> float | None:
        """Lα1 transition energy in eV."""
```

Convenience function:
```python
def xray_transition_energy(element: str, transition: str) -> float | None:
    """Get X-ray transition energy (eV) for an element and transition."""
```

## Transitions Covered

### K shell transitions
| Transition | Name | Description |
|-----------|------|-------------|
| KL1 | — | K to L1 |
| KL2 | Kα2 | K to L2 |
| KL3 | Kα1 | K to L3 |
| KM2 | Kβ3 | K to M2 |
| KM3 | Kβ1 | K to M3 |
| KM4 | Kβ5 II | K to M4 |
| KM5 | Kβ5 I | K to M5 |
| KN2 | Kβ2 II | K to N2 |
| KN3 | Kβ2 I | K to N3 |
| K edge | — | K shell binding energy |

### L shell transitions
| Transition | Name | Description |
|-----------|------|-------------|
| L3M5 | Lα1 | L3 to M5 |
| L3M4 | Lα2 | L3 to M4 |
| L2M4 | Lβ1 | L2 to M4 |
| L3M1 | Ll | L3 to M1 |
| L1M2 | Lβ4 | L1 to M2 |
| L1M3 | Lβ3 | L1 to M3 |
| L2N4 | Lγ1 | L2 to N4 |
| L1N2 | Lγ2 | L1 to N2 |
| L1N3 | Lγ3 | L1 to N3 |
| L1 edge | — | L1 binding energy |
| L2 edge | — | L2 binding energy |
| L3 edge | — | L3 binding energy |

(~50 transitions total per element)

## Implementation Steps

1. **Alembic migration**: Create `xraytransitionenergies` table.
2. **Model**: Add `XrayTransitionEnergy` class to `mendeleev/models.py` + relationship on `Element`.
3. **Parser**: Create `mendeleev/interfaces/nist_xray.py` to scrape the NIST SRD 128 HTML tables:
   - Parse `http://physics.nist.gov/PhysRefData/XrayTrans/Html/theoretical.html` (by element)
   - Parse `http://physics.nist.gov/PhysRefData/XrayTrans/Html/experimental.html` (by element)
   - Map transition codes (KL3, L3M5, etc.) to human-readable names (Kα1, Lα1)
4. **Data import**: Fetch for all elements Z=10–100. ~91 elements × ~50 transitions = ~4,500 rows.
5. **Compute wavelengths**: `λ(Å) = 12398.42 / E(eV)` from energy.
6. **PropertyMetadata**: Add entries for energy (eV) and wavelength (Å).
7. **Tests**: Verify Fe Kα1 ≈ 6404 eV, Cu Kα1 ≈ 8048 eV, Pb Lα1 ≈ 10551 eV.
8. **Docs**: Add X-ray spectroscopy section to data reference.

## Effort

**M** — New table, HTML parser, ~200 lines + migration. Dataset is small (~4,500 rows) and static (last updated 2005).

## Cross-language comparison

| Package | Language | Has X-ray transitions? | Notes |
|---------|----------|----------------------|-------|
| XrayDB | Python | Yes | `xray_lines()` returns emission lines for all elements |
| periodictable | Python | Partial | Has `xray_energy` attribute on elements |
| Mendeleev.jl | Julia | No | Gap — not implemented |
| pymatgen | Python | No | Gap — not implemented |
| molmass | Python | No | Gap — not implemented |
| Chemaxon | Java | No | Gap — not implemented |

XrayDB is the main comparison — it stores similar data but from different sources (Elam/Ravel/Sieber compilations). NIST SRD 128 provides SI-consistent values with theoretical estimates.

## References

- NIST SRD 128: https://dx.doi.org/10.18434/T4859Z
- NIST X-Ray Transition Energies Database: https://www.nist.gov/pml/x-ray-transition-energies-database
- Deslattes et al., Rev. Mod. Phys. 75, 35 (2003)
- Theoretical data: http://physics.nist.gov/PhysRefData/XrayTrans/Html/theoretical.html
- Experimental data: http://physics.nist.gov/PhysRefData/XrayTrans/Html/experimental.html
- XrayDB (comparison): https://xraypy.github.io/XrayDB/xraydb.html
