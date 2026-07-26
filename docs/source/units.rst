.. _units:

****************************
Working with Physical Units
****************************

.. versionadded:: 1.1.0

mendeleev integrates with `pint <https://pint.readthedocs.io/>`_ to provide unit-aware
access to physical properties. Append ``_u`` to any property name to get a
`pint.Quantity <https://pint.readthedocs.io/en/stable/>`_ with proper units attached.


Quick Example
=============

.. code-block:: python

    >>> from mendeleev import Fe, Al
    >>> Fe.atomic_weight_u
    55.845 dalton
    >>> Al.density_u
    2.7 gram / centimeter ** 3

That's it — just add ``_u``.


How It Works
============

When you access ``element.property_u``, mendeleev:

1. Strips the ``_u`` suffix to get the base property name.
2. Looks up the unit in the ``PropertyMetadata`` database table.
3. Multiplies the raw value by that unit using ``pint``.
4. Returns a ``pint.Quantity`` object.

If the property doesn't exist, you'll get an ``AttributeError``. If it has no
unit defined, you'll also get an ``AttributeError``. If the value is ``None``
(missing data), the ``_u`` version returns ``None`` too.


Basic Usage
===========

Accessing properties with units
-------------------------------

.. code-block:: python

    >>> from mendeleev import H, C, Fe
    >>> H.atomic_weight
    1.008
    >>> H.atomic_weight_u
    1.008 dalton
    >>> C.density
    2.267
    >>> C.density_u
    2.267 gram / centimeter ** 3

Without the ``_u`` suffix, you get raw numbers (just like before). With it,
you get pint Quantity objects that know their units.


Unit Conversions
================

The returned Quantity objects support easy unit conversions:

.. code-block:: python

    >>> from mendeleev import Al, Fe
    >>> Al.melting_point_u
    933.47 kelvin
    >>> Al.melting_point_u.to('celsius')
    660.3199999999997 degree_Celsius
    >>> Al.melting_point_u.to('fahrenheit')
    1220.576 degree_Fahrenheit

.. code-block:: python

    >>> Fe.atomic_radius_u
    126 picometer
    >>> Fe.atomic_radius_u.to('angstrom')
    1.26 angstrom


Calculations with Units
=======================

pint Quantities support arithmetic while preserving dimensional correctness:

.. code-block:: python

    >>> from mendeleev import Al
    >>> from mendeleev.models import ureg

    >>> # Mass = density × volume
    >>> density = Al.density_u
    >>> volume = 100 * ureg.milliliter
    >>> mass = density * volume
    >>> mass.to('gram')
    270.0 gram

.. code-block:: python

    >>> from mendeleev import Fe
    >>> # Convert electron affinity to joules
    >>> Fe.electron_affinity_u.to('joule')
    3.9342e-19 joule

The ``ureg`` (pint UnitRegistry) is available from ``mendeleev.models`` if you
need to create new quantities for calculations.


Error Handling
==============

Properties without units raise ``AttributeError``:

.. code-block:: python

    >>> from mendeleev import H
    >>> H.symbol_u
    Traceback (most recent call last):
        ...
    AttributeError: ...

Properties with ``None`` values return ``None``:

.. code-block:: python

    >>> H.melting_point
    None
    >>> H.melting_point_u
    None


Supported Classes
=================

The ``_u`` suffix works on these model classes:

- :py:class:`Element <mendeleev.models.Element>` — the main element class
- :py:class:`IonicRadius <mendeleev.models.IonicRadius>`
- :py:class:`IonizationEnergy <mendeleev.models.IonizationEnergy>`
- :py:class:`Isotope <mendeleev.models.Isotope>`
- :py:class:`PhaseTransition <mendeleev.models.PhaseTransition>`
- :py:class:`ScatteringFactor <mendeleev.models.ScatteringFactor>`


Properties with Units
=====================

Element properties with units
-----------------------------

**Atomic properties:**
    - ``atomic_radius_u`` (pm) — Atomic radius
    - ``atomic_radius_rahm_u`` (pm) — Atomic radius by Rahm et al.
    - ``atomic_volume_u`` (cm³/mol) — Atomic volume
    - ``atomic_weight_u`` (Da) — Relative atomic weight
    - ``atomic_weight_uncertainty_u`` (Da) — Uncertainty in atomic weight

**Abundance:**
    - ``abundance_crust_u`` (mg/kg) — Abundance in Earth's crust
    - ``abundance_sea_u`` (mg/L) — Abundance in seawater

**Covalent radii:**
    - ``covalent_radius_bragg_u`` (pm) — Bragg covalent radius
    - ``covalent_radius_cordero_u`` (pm) — Cordero covalent radius
    - ``covalent_radius_pyykko_u`` (pm) — Pyykkö single bond covalent radius
    - ``covalent_radius_pyykko_double_u`` (pm) — Pyykkö double bond covalent radius
    - ``covalent_radius_pyykko_triple_u`` (pm) — Pyykkö triple bond covalent radius

**Van der Waals radii:**
    - ``vdw_radius_u`` (pm) — Van der Waals radius
    - ``vdw_radius_alvarez_u`` (pm) — Alvarez VdW radius
    - ``vdw_radius_batsanov_u`` (pm) — Batsanov VdW radius
    - ``vdw_radius_bondi_u`` (pm) — Bondi VdW radius
    - ``vdw_radius_dreiding_u`` (pm) — Dreiding VdW radius
    - ``vdw_radius_mm3_u`` (pm) — MM3 VdW radius
    - ``vdw_radius_rt_u`` (pm) — RT VdW radius
    - ``vdw_radius_truhlar_u`` (pm) — Truhlar VdW radius
    - ``vdw_radius_uff_u`` (pm) — UFF VdW radius

**Thermal properties:**
    - ``boiling_point_u`` (K) — Boiling point
    - ``melting_point_u`` (K) — Melting point
    - ``critical_temperature_u`` (K) — Critical temperature
    - ``critical_pressure_u`` (MPa) — Critical pressure
    - ``triple_point_temperature_u`` (K) — Triple point temperature
    - ``triple_point_pressure_u`` (kPa) — Triple point pressure
    - ``evaporation_heat_u`` (kJ/mol) — Heat of vaporization
    - ``fusion_heat_u`` (kJ/mol) — Heat of fusion
    - ``heat_of_formation_u`` (kJ/mol) — Heat of formation
    - ``molar_heat_capacity_u`` (J/mol/K) — Molar heat capacity
    - ``specific_heat_capacity_u`` (J/g/K) — Specific heat capacity
    - ``thermal_conductivity_u`` (W/m/K) — Thermal conductivity

**Physical properties:**
    - ``density_u`` (g/cm³) — Density
    - ``lattice_constant_u`` (Å) — Lattice constant
    - ``metallic_radius_u`` (pm) — Metallic radius
    - ``metallic_radius_c12_u`` (pm) — Metallic radius (coordination 12)

**Electronic properties:**
    - ``dipole_polarizability_u`` (bohr³) — Dipole polarizability
    - ``dipole_polarizability_unc_u`` (bohr³) — Uncertainty in dipole polarizability
    - ``electron_affinity_u`` (eV) — Electron affinity
    - ``c6_u`` (hartree/bohr⁶) — C₆ dispersion coefficient
    - ``c6_gb_u`` (hartree/bohr⁶) — C₆ dispersion coefficient (Gould-Bučko)
    - ``hardness_u`` (eV) — Chemical hardness
    - ``softness_u`` (1/eV) — Chemical softness

**Electronegativity scales:**
    - ``electronegativity_allen_u`` (eV) — Allen electronegativity
    - ``electronegativity_allred_rochow_u`` (e²/pm²) — Allred-Rochow electronegativity
    - ``electronegativity_cottrell_sutton_u`` (e⁰·⁵/pm⁰·⁵) — Cottrell-Sutton electronegativity
    - ``electronegativity_ghosh_u`` (1/pm) — Ghosh electronegativity
    - ``electronegativity_gordy_u`` (e/pm) — Gordy electronegativity
    - ``electronegativity_li_xue_u`` (1/pm) — Li-Xue electronegativity
    - ``electronegativity_martynov_batsanov_u`` (eV⁰·⁵) — Martynov-Batsanov electronegativity
    - ``electronegativity_mulliken_u`` (eV) — Mulliken electronegativity
    - ``electronegativity_nagle_u`` (1/bohr) — Nagle electronegativity
    - ``en_gunnarsson_lundqvist_u`` (eV) — Gunnarsson-Lundqvist electronegativity
    - ``en_miedema_u`` (V) — Miedema electronegativity
    - ``en_robles_bartolotti_u`` (eV) — Robles-Bartolotti electronegativity

**Chemical properties:**
    - ``gas_basicity_u`` (kJ/mol) — Gas basicity
    - ``proton_affinity_u`` (kJ/mol) — Proton affinity

**Economic properties:**
    - ``price_per_kg_u`` (USD/kg) — Price per kilogram
    - ``production_concentration_u`` (%) — Production concentration
    - ``recycling_rate_u`` (%) — Recycling rate
    - ``reserve_distribution_u`` (%) — Reserve distribution

**Miedema parameters:**
    - ``miedema_molar_volume_u`` (cm³) — Miedema molar volume


Other classes with units
------------------------

**IonicRadius:**
    - ``charge_u`` (e) — Ionic charge
    - ``crystal_radius_u`` (pm) — Crystal radius
    - ``ionic_radius_u`` (pm) — Ionic radius

**IonizationEnergy:**
    - ``ion_charge_u`` (e) — Ion charge
    - ``ionization_energy_u`` (eV) — Ionization energy
    - ``uncertainty_u`` (eV) — Uncertainty in ionization energy

**Isotope:**
    - ``mass_u`` (Da) — Isotopic mass
    - ``mass_uncertainty_u`` (Da) — Uncertainty in isotopic mass
    - ``quadrupole_moment_u`` (100 fm²) — Nuclear quadrupole moment
    - ``quadrupole_moment_uncertainty_u`` (100 fm²) — Uncertainty in quadrupole moment

**PhaseTransition:**
    - ``boiling_point_u`` (K) — Boiling point
    - ``critical_pressure_u`` (MPa) — Critical pressure
    - ``critical_temperature_u`` (K) — Critical temperature
    - ``melting_point_u`` (K) — Melting point
    - ``triple_point_pressure_u`` (kPa) — Triple point pressure
    - ``triple_point_temperature_u`` (K) — Triple point temperature

**ScatteringFactor:**
    - ``energy_u`` (eV) — Energy


See Also
========

- :doc:`Tutorials <tutorials>` — notebook tutorial on working with units
- :doc:`Data reference <data>` — complete list of available properties
- :doc:`Data access <data_access>` — how to fetch and query data
- `pint documentation <https://pint.readthedocs.io/>`_ — full pint library docs
