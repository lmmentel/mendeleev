# Feature: Thermal Expansion

## Overview

Add coefficient of linear thermal expansion for elements. This is a standard material property used in engineering and materials science. Pymatgen stores it; mendeleev does not. Single column addition.

## API Design

```python
class Element(Base, ReprMixin, UnitMixin):
    thermal_expansion_coefficient = Column(Float)  # K^-1
```

```python
Fe = element("Fe")
Fe.thermal_expansion_coefficient_u  # -> 1.18e-05 / kelvin
```

## Implementation Steps

1. **Data sourcing**: CRC Handbook or pymatgen's `elemental_properties.yaml`.
2. **Alembic migration**: Add 1 nullable `Float` column.
3. **Model + PropertyMetadata**.
4. **Tests**: Spot-check (Fe ~11.8e-6, Al ~23.1e-6, W ~4.5e-6).
5. **Docs**: auto-generated.

## Effort

**S** — Single column, well-documented values. ~30 lines + migration.

## Cross-language comparison

| Package | Language | Has thermal expansion? | Notes |
|---------|----------|----------------------|-------|
| pymatgen | Python | Yes | `Element.coefficient_of_linear_thermal_expansion` |
| Mendeleev.jl | Julia | Yes | `thermal_expansion_coefficient` field |
| periodictable | Python | No | Gap — not implemented |
| molmass | Python | No | Gap — not implemented |
| JSci | Java | No | Gap — not implemented |

## References

- pymatgen `coefficient_of_linear_thermal_expansion`
- CRC Handbook thermal expansion coefficients
- Wikipedia "Thermal expansion" data tables
