# Feature: Electrical and Optical Properties

## Overview

Add electrical resistivity, reflectivity, refractive index, and velocity of sound. These are standard elemental data used in materials science, optics, and condensed matter physics. Pymatgen stores all four; mendeleev has none.

## API Design

New columns on `Element`:

```python
class Element(Base, ReprMixin, UnitMixin):
    electrical_resistivity = Column(Float)   # Ohm·m
    reflectivity = Column(Float)             # dimensionless (0-1)
    refractive_index = Column(Float)         # dimensionless
    velocity_of_sound = Column(Float)        # m/s
```

Unit-annotated access:
```python
Au = element("Au")
Au.electrical_resistivity_u  # -> 2.44e-08 ohm·meter
Au.velocity_of_sound_u       # -> 3240.0 meter / second
```

## Implementation Steps

1. **Data sourcing**: pymatgen's `elemental_properties.yaml` for resistivity, reflectivity, refractive index, velocity of sound. CRC Handbook as cross-reference.
2. **Alembic migration**: Add 4 nullable `Float` columns.
3. **Model update**: Add columns to `Element`.
4. **Data population**: Script or migration to fill values.
5. **PropertyMetadata**: Units and citations.
6. **Tests**: Spot-check (Au reflectivity, Si refractive index, Cu resistivity).
7. **Docs**: Auto-generated from PropertyMetadata.

## Effort

**M** — Same pattern as mechanical properties. ~80 lines + migration + data.

## Cross-language comparison

| Package | Language | Has electrical/optical? | Notes |
|---------|----------|------------------------|-------|
| pymatgen | Python | Yes | `Element.electrical_resistivity`, `velocity_of_sound`, etc. |
| Mendeleev.jl | Julia | Yes | `electrical_resistivity` field |
| JSci | Java | Yes | `Element.getElectricalConductivity()`, `getThermalConductivity()` |
| periodictable | Python | No | Gap — not implemented |
| molmass | Python | No | Gap — not implemented |

## References

- pymatgen `_ELEMENT_GETATTR_ITEMS`: https://github.com/materialsproject/pymatgen/blob/master/src/pymatgen/core/periodic_table.py
- CRC Handbook electrical resistivity tables
- CRC Handbook optical properties
- NIST data on velocity of sound in elements
