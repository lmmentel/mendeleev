# Feature: Element Classification Enum

## Overview

Add an `ElementType` enum for categorizing elements (metal, nonmetal, metalloid, noble gas, halogen, alkali metal, alkaline earth metal, transition metal, post-transition metal, lanthanide, actinide, etc.). Useful for filtering, querying, and ML feature engineering.

**Existing data in mendeleev:** The `Element` model already stores `block` (s/p/d/f), `geochemical_class` (string like "alkali metal"), and `goldschmidt_class` (string). These partially overlap with the proposed enum but are strings with no programmatic enum access, no `is_metal`/`is_nonmetal` boolean helpers, and no `elements_by_type()` query function. Pymatgen has `ElementType`; BioJava and Chemaxon provide `isMetal()`/`isNonMetal()`/`isMetalloid()` methods.

## API Design

```python
class ElementType(Enum):
    ALKALI_METAL = "alkali_metal"
    ALKALINE_EARTH_METAL = "alkaline_earth_metal"
    TRANSITION_METAL = "transition_metal"
    POST_TRANSITION_METAL = "post_transition_metal"
    METALLOID = "metalloid"
    NONMETAL = "nonmetal"
    HALOGEN = "halogen"
    NOBLE_GAS = "noble_gas"
    LANTHANIDE = "lanthanide"
    ACTINIDE = "actinide"

class Element:
    @property
    def element_type(self) -> ElementType:
        """Classify the element into its primary chemical category."""

    @property
    def is_metal(self) -> bool:
        """True if the element is a metal (any metal category)."""

    @property
    def is_nonmetal(self) -> bool:
        """True if the element is a nonmetal (including metalloids)."""
```

Query helpers:
```python
def elements_by_type(element_type: ElementType) -> list[Element]:
    """Return all elements of a given type."""
```

## Implementation Steps

1. Define `ElementType` enum in `mendeleev/models.py` (or a new `mendeleev/classification.py`).
2. Implement classification logic based on `block`, `group_id`, `period` (standard textbook categories).
3. Add `element_type`, `is_metal`, `is_nonmetal` properties to `Element`.
4. Add `elements_by_type()` helper.
5. Tests: H=NONMETAL, Na=ALKALI_METAL, Fe=TRANSITION_METAL, Si=METALLOID, etc.
6. Docs: add to API reference.

## Effort

**S** — Classification logic is well-defined. ~60 lines, no DB changes.

## Cross-language comparison

| Package | Language | Has classification? | Notes |
|---------|----------|---------------------|-------|
| pymatgen | Python | Yes | `ElementType` enum with 10+ members, `Element.element_type` |
| BioJava | Java | Yes | `Element.isMetal()`, `isNonMetal()`, `isMetalloid()`, `isHalogen()`, `isChalcogen()` |
| Chemaxon JChem | Java | Yes | `PeriodicTable.isMetal()`, `isMetalloid()`, `isAlkaliMetal()`, etc. |
| Chemistry.NET | C# | Yes | `ElementType` enum, `PhysicalState` enum |
| Mendeleev.jl | Julia | Partial | `category` string field (from PeriodicTable.jl) |
| molmass | Python | No | Has `block` and `series` but no metal/nonmetal classification |
| periodictable | Python | No | Has `metal` boolean attribute only |

## References

- pymatgen `ElementType` enum: https://github.com/materialsproject/pymatgen/blob/master/src/pymatgen/core/periodic_table.py
- BioJava `Element`: https://biojava.org/docs/api/org/biojava/nbio/structure/Element.html
- Chemaxon `PeriodicTable`: https://apidocs.chemaxon.com/jchem/developer/beans/api/chemaxon/struc/PeriodicTable.html
- Wikipedia "Periodic table" groupings
- IUPAC nomenclature
