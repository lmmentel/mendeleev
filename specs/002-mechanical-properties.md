# Feature: Mechanical Properties

## Overview

Add mechanical property data for elements: bulk modulus, Young's modulus, rigidity (shear) modulus, Brinell hardness, Vickers hardness, mineral (Mohs) hardness, and Poisson's ratio. These are among the most-used pymatgen Element attributes and are absent from mendeleev. Data comes from the CRC Handbook and pymatgen's curated YAML sources.

## API Design

New columns on `Element`:

```python
class Element(Base, ReprMixin, UnitMixin):
    # DB columns (nullable Float, units via PropertyMetadata)
    bulk_modulus = Column(Float)           # GPa
    youngs_modulus = Column(Float)         # GPa
    rigidity_modulus = Column(Float)       # GPa
    brinell_hardness = Column(Float)       # MPa
    vickers_hardness = Column(Float)       # MPa
    mineral_hardness = Column(Float)       # Mohs scale (dimensionless)
    poissons_ratio = Column(Float)         # dimensionless
```

All accessible with `_u` suffix via UnitMixin:
```python
Fe = element("Fe")
Fe.bulk_modulus_u  # -> 170.0 gigapascal  (if stored as GPa)
```

## Implementation Steps

1. **Data sourcing**: Extract values from pymatgen's `elemental_properties.yaml` (CC-BY-BSD) or CRC Handbook tables. Map element symbols to values.
2. **Alembic migration**: Add 7 new nullable `Float` columns to `elements` table.
3. **Model update**: Add columns to `Element` class.
4. **Data population**: Write a script or alembic data migration to populate the new columns.
5. **PropertyMetadata**: Add entries for each new column with correct units and citations.
6. **Tests**: Verify values for spot-checked elements (Fe, Cu, W, diamond/C).
7. **Docs**: Update `data.rst` (auto-generated from PropertyMetadata) and `quick.rst` example.

## Effort

**M** — Alembic migration + data sourcing + model changes. The data collection and validation is the bulk of the work. ~100 lines of code + migration + data script.

## References

- pymatgen periodic table data: https://github.com/materialsproject/pymatgen/blob/master/src/pymatgen/core/periodic_table.py
- pymatgen YAML sources: https://github.com/materialsproject/pymatgen/tree/master/src/pymatgen/core
- CRC Handbook of Chemistry and Physics, mechanical properties tables
- Wikipedia "Bulk modulus" / "Young's modulus" data tables
