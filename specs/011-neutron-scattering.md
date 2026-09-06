# Feature: Neutron Scattering Data

## Overview

Add neutron scattering properties: bound coherent scattering length (b_c), coherent cross section, incoherent cross section, total cross section, and absorption cross section. This is periodictable's strongest differentiator and would make mendeleev the go-to package for neutron scientists (reactor physics, neutron diffraction, SANS, reflectometry). Data is publicly available from the neutron data booklet (IAEA).

## API Design

New model and columns:

```python
class NeutronScattering(Base, ReprMixin):
    """Neutron scattering data for an isotope."""
    __tablename__ = "neutronscattering"

    id = Column(Integer, primary_key=True)
    atomic_number = Column(Integer, ForeignKey("elements.atomic_number"))
    mass_number = Column(Integer)
    b_c = Column(Float)                    # bound coherent scattering length (fm)
    b_c_imaginary = Column(Float)          # imaginary part (absorption)
    coherent = Column(Float)               # coherent cross section (barns)
    incoherent = Column(Float)             # incoherent cross section (barns)
    absorption = Column(Float)             # absorption cross section (barns)
    total = Column(Float)                  # total cross section (barns)
    is_energy_dependent = Column(Boolean)  # rare earths have energy-dependent b_c

    isotope = relationship("Isotope", ...)

class Isotope:
    neutron = relationship("NeutronScattering", uselist=False, ...)

class Element:
    @property
    def neutron_scattering_length(self) -> float | None:
        """Weighted average coherent scattering length for natural abundance."""

    @property
    def neutron_total_cross_section(self) -> float | None:
        """Weighted average total cross section for natural abundance."""
```

Also add SLD calculator:
```python
def neutron_sld(compound: str, density: float, wavelength: float = 1.8) -> tuple[float, float]:
    """Compute neutron scattering length density (real, imaginary) for a compound.

    Args:
        compound: chemical formula (e.g. "H2O")
        density: mass density in g/cm³
        wavelength: neutron wavelength in Angstrom (default: 1.8 Å, cold neutrons)
    """
```

## Implementation Steps

1. **Data sourcing**: IAEA neutron data booklet / periodictable's `nsf_tables.py` (public domain data).
2. **Alembic migration**: Create `neutronscattering` table.
3. **Model**: `NeutronScattering` class + relationships on `Isotope` and `Element`.
4. **Data population**: Script to parse and import scattering data for all stable isotopes.
5. **SLD calculator**: Depends on Formula parser (#4) or use simple element-count approach.
6. **Tests**: Verify H-1 b_c = -3.7406 fm, H-2 b_c = 6.671 fm, Ni coherent = 14.4 barns.
7. **Docs**: new tutorial on neutron scattering with mendeleev.

## Effort

**L** — New DB table, data import script, SLD calculator, ~300 lines + data pipeline.

## References

- periodictable neutron scattering: https://periodictable.readthedocs.io/en/latest/api/nsf.html
- IAEA neutron data booklet: https://www-nds.iaea.org/nrdc/
- NIST neutron scattering lengths: https://www.ncnr.nist.gov/programs/nbsp/
- Neutron Data Booklet (Laue Langevin Institute): https://www.ill.eu/document/nlx15ieawgnp
