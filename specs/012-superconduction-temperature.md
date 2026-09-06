# Feature: Superconduction Temperature

## Overview

Add superconduction transition temperature (T_c) for elements that exhibit superconductivity. This is a standard property in pymatgen and is useful for condensed matter physics and materials science research. Single column addition.

## API Design

```python
class Element(Base, ReprMixin, UnitMixin):
    superconduction_temperature = Column(Float)  # K
```

```python
Nb = element("Nb")
Nb.superconduction_temperature_u  # -> 9.26 kelvin
Pb.superconduction_temperature_u  # -> 7.19 kelvin
```

Only ~30 elements have known T_c values; the rest are `None`.

## Implementation Steps

1. **Data sourcing**: CRC Handbook superconductivity tables, NIST, or pymatgen's data.
2. **Alembic migration**: Add 1 nullable `Float` column.
3. **Model + PropertyMetadata** (unit: kelvin).
4. **Tests**: Verify Nb=9.26K, Pb=7.19K, Hg=4.15K, Al=1.18K.
5. **Docs**: auto-generated from PropertyMetadata.

## Effort

**S** — Single column, well-documented values. ~30 lines + migration.

## References

- pymatgen `superconduction_temperature`
- CRC Handbook superconductivity data
- Wikipedia "List of superconductors" — elemental T_c values
- NIST SRD 126: Superconductivity Database
