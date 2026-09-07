# Feature: Spectral Lines (NIST ASD)

## Overview

Add spectral line data from the NIST Atomic Spectra Database: wavelengths, transition probabilities, oscillator strengths, and line classifications. This is one of the largest NIST ASD data categories and is essential for spectroscopy (OES, ICP-AES, LIBS, astrochemistry). Mendeleev currently stores only ionization energies from NIST ASD — spectral lines are a major gap.

**Existing data:** Mendeleev has no spectral line data. The `ScatteringFactor` table stores X-ray scattering factors (f1/f2 vs energy from Henke/LBNL), which is unrelated.

**Data source:** NIST ASD Lines endpoint (`https://physics.nist.gov/cgi-bin/ASD/lines1.pl`). The API supports CSV output filtered by element, wavelength range, and transition type. NIST provides both observed and Ritz wavelengths, transition probabilities (A values), oscillator strengths (f, gf), and full level classifications.

## API Design

New model and table:

```python
class SpectralLine(Base, ReprMixin):
    """Spectral line data from NIST ASD."""
    __tablename__ = "spectrallines"

    id = Column(Integer, primary_key=True)
    atomic_number = Column(Integer, ForeignKey("elements.atomic_number"), nullable=False)
    ion_charge = Column(Integer, nullable=False)  # 0 = neutral, 1 = singly ionized, ...

    # Wavelength data (Angstroms)
    wavelength = Column(Float)            # observed wavelength
    wavelength_ritz = Column(Float)       # Ritz wavelength (derived from energy levels)
    wavelength_obs_ritz = Column(Float)   # observed - Ritz difference

    # Transition probabilities
    a_value = Column(Float)               # transition probability (s^-1)
    f_value = Column(Float)               # absorption oscillator strength
    log_gf = Column(Float)               # log10(gf)

    # Level classification (lower)
    lower_configuration = Column(String)
    lower_term = Column(String)
    lower_j = Column(String)              # J value as string (e.g. "3/2")
    lower_energy = Column(Float)          # energy in cm^-1

    # Level classification (upper)
    upper_configuration = Column(String)
    upper_term = Column(String)
    upper_j = Column(String)
    upper_energy = Column(Float)

    # Metadata
    relative_intensity = Column(Float)    # for prominent lines
    uncertainty_wavelength = Column(Float)  # wavelength uncertainty
    uncertainty_a_value = Column(Float)     # A value uncertainty
    is_allowed = Column(Boolean)          # True = E1 (allowed), False = forbidden (M1, E2, ...)

    element = relationship("Element", back_populates="spectral_lines")
```

Access via `Element`:
```python
class Element:
    @property
    def spectral_lines(self) -> list["SpectralLine"]:
        """All spectral lines for this element across all ion stages."""

    def spectral_lines_filter(
        self,
        ion_charge: int | None = None,
        min_wavelength: float | None = None,
        max_wavelength: float | None = None,
        only_with_a_value: bool = False,
    ) -> list["SpectralLine"]:
        """Filter spectral lines by charge state and wavelength range."""
```

Convenience function:
```python
def spectral_lines(
    element: str,
    ion_charge: int | None = None,
    min_wavelength: float | None = None,
    max_wavelength: float | None = None,
) -> list[SpectralLine]:
    """Fetch spectral lines for an element, optionally filtered."""
```

## Implementation Steps

1. **Alembic migration**: Create `spectrallines` table.
2. **Model**: Add `SpectralLine` class to `mendeleev/models.py` + `spectral_lines` relationship on `Element`.
3. **Parser**: Extend `mendeleev/interfaces/nist_asd.py` with a `NISTLinesQuery` model and async fetcher (same pattern as `NISTIEQuery`).
4. **Data import**: Fetch lines for all 118 elements. Filter to only lines with transition probabilities or energy level classifications to reduce dataset size.
5. **Size management**: NIST ASD has hundreds of thousands of lines. Consider storing only:
   - Lines with `A > 0` (known transition probability)
   - Lines with energy level classifications
   - Or provide a flag column to distinguish "complete" vs "selected" datasets
6. **PropertyMetadata**: Add entries for wavelength (Å), A value (s⁻¹), oscillator strength.
7. **Tests**: Verify Fe I 438.355 nm line exists; verify H I Balmer series wavelengths.
8. **Docs**: New tutorial on querying spectral lines for spectroscopy.

## Effort

**XL** — New table, large data import pipeline, async parser, ~400 lines + migration + data scripts.

## Data Volume Concern

NIST ASD contains ~500,000+ spectral lines across all elements. Storing all of them would significantly increase the database size. Options:

| Strategy | Rows (est.) | DB size (est.) | Trade-off |
|----------|-------------|----------------|-----------|
| All lines | ~500K | ~200 MB | Complete but large |
| Only with A values | ~200K | ~80 MB | Most useful subset |
| Only with level classifications | ~300K | ~120 MB | Good for energy level work |
| Only prominent lines | ~5K | ~2 MB | Minimal but very fast |

Recommendation: Start with "only with A values" (~200K rows) as default. Users who need the full dataset can re-import.

## Cross-language comparison

| Package | Language | Has spectral lines? | Notes |
|---------|----------|---------------------|-------|
| periodictable | Python | No | Gap — not implemented |
| Mendeleev.jl | Julia | No | Gap — not implemented |
| pymatgen | Python | No | Gap — not implemented |
| molmass | Python | No | Gap — not implemented |
| XrayDB | Python | Partial | X-ray emission lines only (Kα, Kβ) |

No periodic table package stores comprehensive visible/UV spectral lines. This would be a major differentiator for mendeleev.

## References

- NIST ASD Lines Form: https://physics.nist.gov/PhysRefData/ASD/lines_form.html
- NIST ASD help (line output format): https://physics.nist.gov/PhysRefData/ASD/Html/help.html
- NIST ASD DOI: https://dx.doi.org/10.18434/T4W30F
- Kramida, A., Ralchenko, Y., Reader, J., and NIST ASD Team (2024). NIST Atomic Spectra Database (ver. 5.12), [Online]. Available: https://physics.nist.gov/asd
