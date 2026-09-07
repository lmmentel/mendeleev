# Mendeleev Roadmap

Ideas for future work, collected from codebase exploration and feature brainstorming.
This file is intentionally **not committed** — it documents backlog items to be picked up
as separate PRs. Each item lists file targets, key formulas, and a test plan.

Priority order was agreed as: **bonding utilities → NMR calculator → radius-ratio/ionic
tools → trends & Z=119+ prediction → pandas/ML ergonomics**, followed by the lower-priority
items at the end.

> All items below are **pure-Python computed features** (no new DB columns), so they need no
> alembic migrations unless new stored data is added. New stored data would require the
> full workflow: model → alembic revision → upgrade → PropertyMetadata → `inv render-data-docs`.

## Spec files

Detailed feature specifications are in `specs/`:

| Spec | Title | Status | DB changes? |
|------|-------|--------|-------------|
| 001 | Element Serialization | Not started | No |
| 002 | Mechanical Properties | Not started | Yes (7 columns) |
| 003 | Electrical & Optical Properties | Not started | Yes (4 columns) |
| 004 | Chemical Formula Parser | Not started | No |
| 005 | PEP 561 py.typed Marker | Not started | No |
| 006 | Term Symbol Parsing | Not started | No (data exists in `ionizationenergies`) |
| 007 | NMR Calculator | Not started | No (data exists in `isotopes`) |
| 008 | Thermal Expansion | Not started | Yes (1 column) |
| 009 | Bonding Utilities | Not started | No |
| 010 | Element Classification Enum | Not started | No (data exists: `block`, `geochemical_class`) |
| 011 | Neutron Scattering | Not started | Yes (new table) |
| 012 | Superconduction Temperature | Not started | Yes (1 column) |
| 013 | Isotopic Distribution Calculator | Not started | No (data exists in `isotopes`) |
| 014 | Spectral Lines (NIST ASD) | Not started | Yes (new `spectrallines` table) |
| 015 | X-Ray Transition Energies (NIST SRD 128) | Not started | Yes (new `xraytransitionenergies` table) |

## Cross-language research findings

Research was conducted across Python, JS/TS, Rust, Go, Java, R, Julia, C#, Ruby, and Dart periodic table packages. Key findings:

- **Most implemented feature across languages**: Formula parsing (molmass, chemformula, Chemaxon, Chemistry.NET, Dart quds)
- **Rarest feature**: NMR calculator (only periodictable and Mendeleev.jl have it)
- **Biggest gap in mendeleev**: Isotopic distribution calculator (molmass, IsoSpecPy, Chemistry.NET have it; we don't)
- **Differentiating features for mendeleev**: Mechanical properties (few packages have these), comprehensive electronegativity scales (8+), screening constants, NIST ASD ionization energies (full charge-state coverage)

## NIST ASD data audit

NIST Atomic Spectra Database (ver. 5.12, Nov 2024) contains four main data categories:

| NIST ASD Category | In mendeleev? | Spec |
|---|---|---|
| Ground States & Ionization Energies | **YES** — `ionizationenergies` table | — (existing) |
| Spectral Lines (wavelengths, A values) | **NO** | 014 |
| Energy Levels | **NO** | (not yet specced) |
| X-Ray Transition Energies (SRD 128) | **NO** | 015 |

**Other NIST databases:**
- XCOM photon cross sections (compton, photoelectric) — not in mendeleev
- X-Ray Form Factor/Attenuation/Scattering (Chantler) — mendeleev has Henke f1/f2, not Chantler
- Condensed matter DFT data — not in mendeleev (niche)

**Packages with more features than mendeleev:**
- Mendeleev.jl (Julia): ~80+ properties, thermal expansion, superconduction T_c, bond polarity
- molmass (Python): isotopic distribution, mass spectrum, formula parsing
- periodictable (Python): neutron scattering, SLD calculator, NMR module

**Packages with fewer features than mendeleev:**
- Most JS/TS, Ruby, Dart packages: basic data only
- R PeriodicTable: data.frame with basic properties
- Chemaxon JChem: classification booleans but no computed properties

---

## 1. Bonding utilities — `mendeleev/bond.py` (new)

- `en_difference(a, b, scale="pauling") -> float` — wraps existing `Element.electronegativity()`.
- `ionic_character(dchi)` — Pauling fraction of ionic character `1 - exp(-0.25 * dchi**2)`;
  optional Hannay–Smith variant `1 - exp(-0.25 * dchi**2)` with different pre-factor.
- `bond_polarity(a, b)` -> dataclass `Bond(a, b, dchi, ionic_character, label)` with
  configurable thresholds (textbook defaults: `<0.4` covalent, `0.4–1.7` polar covalent,
  `>1.7` ionic).
- `Bond` should be a small `@dataclass` (frozen) in the style of existing lightweight classes.
- `deltaN` was fixed in the bug PR; consider moving it here and re-exporting from
  `mendeleev.mendeleev` for back-compat.
- Tests: `tests/test_bond.py`
  - H–C: `dchi` ≈ 0.4 → polar-covalent boundary
  - Na–Cl: `dchi` ≈ 2.1 → ionic, `ionic_character` ≈ 0.7
  - scale argument routing through `electronegativity_scales()`

## 2. NMR calculator — `mendeleev/nmr.py` (new)

Data already stored per isotope: `g_factor` (dimensionless), `spin`, `half_life`,
`half_life_unit`.

Constants (CODATA): `mu_N / h = 7.622593285 MHz/T`.

- `gyromagnetic_ratio(isotope) -> Quantity` — `gamma = g * mu_N / hbar` (rad·s⁻¹·T⁻¹);
  `gamma/2pi` in MHz/T.
- `larmor_frequency(isotope, field) -> Quantity` — `nu = |g| * mu_N * B / h`.
- `receptivity(isotope)` — absolute receptivity `∝ gamma**3 * abundance * I*(I+1)`.
- Guard `spin == 0` / even–even nuclei (`g_factor == 0` → no NMR): return `None` and raise a
  clear informative error when explicitly requested.
- Add thin methods on `Isotope`: `Isotope.gyromagnetic_ratio()`, `Isotope.larmor_frequency(B)`.
- `format_half_life(isotope)` helper — the stored `half_life_unit` strings are inconsistent
  (`"ysec"`, `"zsec"`, `"msec"`, `"minute"`, `"Eyear"`, …). Needs a unit-mapping parser, see
  full distinct list in `tests/test_isotope.py::test_isotopes_half_life_units`.
- Tests: `tests/test_nmr.py`; known reference values:
  - ¹H at 11.74 T ≈ 499.84 MHz; ¹H gamma/2pi = 42.576 MHz/T
  - ³¹P gamma/2pi ≈ 17.24 MHz/T
  - ¹²C, ¹⁶O (spin 0) → `None`

## 3. Radius-ratio & ionic tools — extend `mendeleev/ion.py`

`IonicRadius` already stores `charge`, `coordination`, `spin`, `crystal_radius`,
`ionic_radius`, `origin`, `most_reliable`.

- `Ion.get_radius(spin=None, coordination=None, radius_type="ionic_radius", most_reliable_only=False)`
  — structured filter (keep existing `radius` property).
- `Ion.mean_radius(radius_type=...)` property — mirrors the averaging in `ionic_potential()`.
- `radius_ratio(cation, anion) -> float` — ratio of (smallest-CN, most-reliable) radii.
- `coordination_number(ratio)` — Pauling boundaries: CN2 `>0.155`, CN3 `>0.225`, CN4 `>0.414`,
  CN6 `>0.732`, CN8 `>1`, else CN12.
- Tests: extend `tests/test_ion.py`
  - Na⁺/Cl⁻ and Mg²⁺/O²⁻ → predicted CN6
  - radius filtering by spin (LS/HS) and coordination
  - empty filter result → informative error / `None`, not a `StatisticsError` from `mean()`

## 4. Trends & prediction — `mendeleev/trends.py` (new)

- Promote `interpolate_property` (currently in `mendeleev/electronegativity.py:46`, used by
  Sanderson’s scale) to a public API.
- `trend(property, axis="period" | "group", which=None) -> DataFrame` — values for one row/column.
- `predict_property(property, z)` — extrapolation along **group** columns of period 8
  (Z = 119–126) using the last 3 known members (existing polyfit logic). Raise informative
  errors where no trend exists (f-block). Return `(value, note)` with a speculativeness caveat.
- `predicted_elements()` — DataFrame for Z = 119–126 of well-behaved properties (covalent
  radius, Allen EN, melting point).
- Tests: `tests/test_trends.py`
  - leave-one-out validation: predict Pb(`82`) from group-14 trend excluding Pb, compare to stored value
  - sanity: noble-gas group (18) interpolation matches stored values (Sanderson already relies on this)

## 5. Pandas / ML ergonomics

- `Element.to_dict()` / `to_dataframe()` / `to_json()` — scalar columns + `ionenergies`,
  `oxistates`, isotope summary; exclude heavy lazy relations.
- `mendeleev/features.py`:
  - `default_features` — curated numeric list (radii, EN scales, IE1, EA, density, …)
  - `feature_matrix(attributes=None, include_periodic=True, impute=True) -> DataFrame`
    indexed by symbol; one-hot/ordinal encoding of `block`, `series`, `group`, `period`
  - `as_features(symbol)` — single-row vector
- Extend `fetch_table` (`mendeleev/fetch.py:16`) with `columns`, `where` (e.g.
  `{"group_id": 18}`), `order_by`, `limit` — back-compatible.
- Tests: `tests/test_features.py`; extend `tests/test_fetch.py`.

---

## Lower-priority backlog

### 6. Chemical formulas & molecules
- `mendeleev/formula.py`: parse formulas (`"Fe2(SO4)3"`, hydrates, charged `"SO4^2-"`)
- `molecular_weight("H2SO4")` from stored atomic weights; elemental composition (weight % / atom %)
- isotopic mass pattern for mass spectrometry using stored isotope abundances
- `formula_of(...)` reverse helper

### 7. Nuclear & radiochemistry utilities
- Decay-mode parent/daughter analysis (data in `isotopedecaymodes`)
- Radioactivity grading (stable / primordial / long-lived / short-lived)
- Standardized half-life formatting, “most stable isotope” lookup per element

### 8. X-ray / scattering utilities
- K/L/M edge energies, characteristic line energies (Kα₁, Kα₂, Kβ), fluorescence yields
- Mass attenuation coefficient from stored `scattering_factors` (`mu_a = 2 * r0 * lambda * f2`)
- **Requires new stored data** → full model/migration/PropertyMetadata workflow

### 9. CLI upgrade — `mendeleev/cli.py`
- Rich inline tables (replacing `to_string`)
- `--compare Fe O`, `--property <attr> --all`, `--json` output
- ASCII colored periodic-table printout

### 10. Visualization additions — `mendeleev/vis/`
- Linked periodic-table + property-vs-Z trend explorer (bokeh)
- Property correlation matrix (seaborn already has `heatmap`)
- Printable element-card / periodic-table HTML export

### 11. Robustness & hygiene
- `math.isclose` in `boiling_point`/`melting_point` (`models.py`) raises `TypeError` if a
  transition value is `None` — currently no stored element triggers it, but guard it anyway
- `mean()` over empty lists in `Ion.ionic_potential` → `StatisticsError`; return `None`
- Consider adding `deltaN` to `mendeleev/__init__.py` exports for discoverability