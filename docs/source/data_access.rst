.. _data-access:

Accessing data
==============

.. tip::

    If you're looking for raw data behind ``mendeleev`` have a look at `mendeleev-data <https://github.com/lmmentel/mendeleev-data>`_ repo.

    You can find **all data assets** in multiple formats: 
    
    - csv, 
    - html,
    - json, 
    - sql,
    - markdown.

    All releases a tagged with the same version numbers as ``mendeeleev``.

Individual Elements
-------------------

The easiest way to access individual elements is simply by importing them from
the :doc:`mendeleev </index>` directly using their symbols::

    >>> from mendeleev import H, C, O, Og
    >>> [x.name for x in [H, C, O, Og]]
    ['Hydrogen', 'Carbon', 'Oxygen', 'Oganesson']


An alternative method of access is through the :py:func:`element` function that
returns either a single :py:class:`Element <mendeleev.models.Element>` instance or a tuple of those instances depending on the input. It provides a more flexible interface
since it accepts element names, atomic numbers and symbols as well as their combinations.

.. autofunction:: element

Fetching data in bulk
---------------------

.. currentmodule:: mendeleev.fetch

If you want a whole set of data you can retrieve one of the tables from the
database as `pandas <http://pandas.pydata.org/>`_
`DataFrame <http://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.html>`_ through the :py:func:`fetch_table`. The following
tables are available:

- :ref:`elements <element-class>`
- :ref:`groups <group-class>`
- :ref:`ionicradii <ionicradius-class>`
- :ref:`ionizationenergies <ionizationenergy-class>`
- :ref:`isotopedecaymodes <isotopedecaymode-class>`
- :ref:`isotopes <isotope-class>`
- :ref:`oxidationstates <oxidationstate-class>`
- :ref:`phasetransitions <phasetransition-class>`
- :ref:`propertymetadata <propertymetadata-class>`
- :ref:`scattering_factors <scatteringfactor-class>`
- :ref:`screeningconstants <screeningconstant-class>`
- :ref:`series <series-class>`

.. autofunction:: fetch_table

.. autofunction:: fetch_ionization_energies

.. autofunction:: fetch_ionic_radii



Computed properties
-------------------

Some properties need to be computed rather than directly retrieved from the database. :doc:`electronegativity`

.. autofunction:: fetch_electronegativities


Units support
-------------

The ``mendeleev`` package provides built-in support for accessing physical properties with their proper units using the `Pint <https://pint.readthedocs.io/>`_ library. This feature allows you to get dimensional quantities with units attached, making calculations safer and more transparent.

Accessing properties with units
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To access any property with units, simply append ``_u`` to the property name::

    >>> from mendeleev import H, C
    >>> H.atomic_weight
    1.008
    >>> H.atomic_weight_u
    1.008 dalton
    >>> C.density
    2.267
    >>> C.density_u  
    2.267 gram / centimeter ** 3

Properties that don't have units defined will raise an ``AttributeError``::

    >>> H.symbol_u
    AttributeError: 'Element' has no unit defined for 'symbol'

If a property value is ``None`` (missing data), the unit-enabled version will also return ``None``::

    >>> H.melting_point
    None
    >>> H.melting_point_u
    None

Working with unit quantities
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The returned objects are `Pint Quantity <https://pint.readthedocs.io/en/stable/user/defining-quantities.html>`_ instances that support unit conversions and arithmetic operations::

    >>> from mendeleev import Fe
    >>> Fe.melting_point_u
    1811.0 kelvin
    >>> Fe.melting_point_u.to('celsius')
    1537.85 degree_Celsius
    >>> Fe.melting_point_u.to('fahrenheit')  
    2800.13 degree_Fahrenheit

You can perform calculations while preserving units::

    >>> Fe.density_u * Fe.atomic_volume_u
    55.845 gram / mole

Element properties with units
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The following Element properties support units:

**Atomic properties:**
    - ``atomic_radius_u`` (pm) - Atomic radius
    - ``atomic_radius_rahm_u`` (pm) - Atomic radius by Rahm et al.
    - ``atomic_volume_u`` (cm³/mol) - Atomic volume
    - ``atomic_weight_u`` (Da) - Relative atomic weight
    - ``atomic_weight_uncertainty_u`` (Da) - Uncertainty in atomic weight

**Abundance:**
    - ``abundance_crust_u`` (mg/kg) - Abundance in Earth's crust
    - ``abundance_sea_u`` (mg/L) - Abundance in seawater

**Covalent radii:**
    - ``covalent_radius_bragg_u`` (pm) - Bragg covalent radius
    - ``covalent_radius_cordero_u`` (pm) - Cordero covalent radius 
    - ``covalent_radius_pyykko_u`` (pm) - Pyykkö single bond covalent radius
    - ``covalent_radius_pyykko_double_u`` (pm) - Pyykkö double bond covalent radius
    - ``covalent_radius_pyykko_triple_u`` (pm) - Pyykkö triple bond covalent radius

**Van der Waals radii:**
    - ``vdw_radius_u`` (pm) - Van der Waals radius
    - ``vdw_radius_alvarez_u`` (pm) - Alvarez VdW radius
    - ``vdw_radius_batsanov_u`` (pm) - Batsanov VdW radius  
    - ``vdw_radius_bondi_u`` (pm) - Bondi VdW radius
    - ``vdw_radius_dreiding_u`` (pm) - Dreiding VdW radius
    - ``vdw_radius_mm3_u`` (pm) - MM3 VdW radius
    - ``vdw_radius_rt_u`` (pm) - RT VdW radius
    - ``vdw_radius_truhlar_u`` (pm) - Truhlar VdW radius
    - ``vdw_radius_uff_u`` (pm) - UFF VdW radius

**Thermal properties:**
    - ``boiling_point_u`` (K) - Boiling point
    - ``melting_point_u`` (K) - Melting point
    - ``critical_temperature_u`` (K) - Critical temperature
    - ``critical_pressure_u`` (MPa) - Critical pressure
    - ``triple_point_temperature_u`` (K) - Triple point temperature
    - ``triple_point_pressure_u`` (kPa) - Triple point pressure
    - ``evaporation_heat_u`` (kJ/mol) - Heat of vaporization
    - ``fusion_heat_u`` (kJ/mol) - Heat of fusion
    - ``heat_of_formation_u`` (kJ/mol) - Heat of formation
    - ``molar_heat_capacity_u`` (J/mol/K) - Molar heat capacity
    - ``specific_heat_capacity_u`` (J/g/K) - Specific heat capacity
    - ``thermal_conductivity_u`` (W/m/K) - Thermal conductivity

**Physical properties:**
    - ``density_u`` (g/cm³) - Density
    - ``lattice_constant_u`` (Å) - Lattice constant
    - ``metallic_radius_u`` (pm) - Metallic radius
    - ``metallic_radius_c12_u`` (pm) - Metallic radius (coordination 12)

**Electronic properties:**
    - ``dipole_polarizability_u`` (bohr³) - Dipole polarizability
    - ``dipole_polarizability_unc_u`` (bohr³) - Uncertainty in dipole polarizability
    - ``electron_affinity_u`` (eV) - Electron affinity
    - ``c6_u`` (hartree/bohr⁶) - C₆ dispersion coefficient
    - ``c6_gb_u`` (hartree/bohr⁶) - C₆ dispersion coefficient (Gould-Bučko)
    - ``hardness_u`` (eV) - Chemical hardness
    - ``softness_u`` (1/eV) - Chemical softness

**Electronegativity scales:**
    - ``electronegativity_allen_u`` (eV) - Allen electronegativity
    - ``electronegativity_allred_rochow_u`` (e²/pm²) - Allred-Rochow electronegativity
    - ``electronegativity_cottrell_sutton_u`` (e⁰·⁵/pm⁰·⁵) - Cottrell-Sutton electronegativity
    - ``electronegativity_ghosh_u`` (1/pm) - Ghosh electronegativity
    - ``electronegativity_gordy_u`` (e/pm) - Gordy electronegativity
    - ``electronegativity_li_xue_u`` (1/pm) - Li-Xue electronegativity
    - ``electronegativity_martynov_batsanov_u`` (eV⁰·⁵) - Martynov-Batsanov electronegativity
    - ``electronegativity_mulliken_u`` (eV) - Mulliken electronegativity
    - ``electronegativity_nagle_u`` (1/bohr) - Nagle electronegativity
    - ``en_gunnarsson_lundqvist_u`` (eV) - Gunnarsson-Lundqvist electronegativity
    - ``en_miedema_u`` (V) - Miedema electronegativity
    - ``en_robles_bartolotti_u`` (eV) - Robles-Bartolotti electronegativity

**Chemical properties:**
    - ``gas_basicity_u`` (kJ/mol) - Gas basicity
    - ``proton_affinity_u`` (kJ/mol) - Proton affinity

**Economic properties:**
    - ``price_per_kg_u`` (USD/kg) - Price per kilogram
    - ``production_concentration_u`` (%) - Production concentration
    - ``recycling_rate_u`` (%) - Recycling rate
    - ``reserve_distribution_u`` (%) - Reserve distribution

**Miedema parameters:**
    - ``miedema_molar_volume_u`` (cm³) - Miedema molar volume

Other classes with units support
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**IonicRadius:**
    - ``charge_u`` (e) - Ionic charge
    - ``crystal_radius_u`` (pm) - Crystal radius
    - ``ionic_radius_u`` (pm) - Ionic radius

**IonizationEnergy:**
    - ``ion_charge_u`` (e) - Ion charge
    - ``ionization_energy_u`` (eV) - Ionization energy
    - ``uncertainty_u`` (eV) - Uncertainty in ionization energy

**Isotope:**
    - ``mass_u`` (Da) - Isotopic mass
    - ``mass_uncertainty_u`` (Da) - Uncertainty in isotopic mass
    - ``quadrupole_moment_u`` (100 fm²) - Nuclear quadrupole moment
    - ``quadrupole_moment_uncertainty_u`` (100 fm²) - Uncertainty in quadrupole moment

**PhaseTransition:**
    - ``boiling_point_u`` (K) - Boiling point
    - ``critical_pressure_u`` (MPa) - Critical pressure
    - ``critical_temperature_u`` (K) - Critical temperature
    - ``melting_point_u`` (K) - Melting point
    - ``triple_point_pressure_u`` (kPa) - Triple point pressure
    - ``triple_point_temperature_u`` (K) - Triple point temperature

**ScatteringFactor:**
    - ``energy_u`` (eV) - Energy

Examples
~~~~~~~~

Here are some practical examples of working with units::

    >>> from mendeleev import Al, Fe
    >>> import numpy as np
    
    # Temperature conversions
    >>> Al.melting_point_u.to('celsius')
    660.3199999999997 degree_Celsius
    
    # Density calculations
    >>> volume = 1 * ureg.liter  # Need to import ureg for new units
    >>> from mendeleev.models import ureg
    >>> volume = 1 * ureg.liter
    >>> mass_of_aluminum = Al.density_u * volume
    >>> mass_of_aluminum.to('gram')
    2700.0 gram
    
    # Energy comparisons
    >>> Fe.electron_affinity_u.to('joule')
    2.4563519104e-20 joule
    
    # Working with arrays of elements
    >>> elements = [Al, Fe]
    >>> densities = [el.density_u for el in elements]
    >>> [d.magnitude for d in densities]  # Get numeric values
    [2.7, 7.874]
    >>> [str(d.units) for d in densities]  # Get units
    ['gram / centimeter ** 3', 'gram / centimeter ** 3']



Database session and engine
---------------------------

For those how want to interact with the database through
a layer of `SQLAlchemy <http://www.sqlalchemy.org/>`_ there are methods
for getting the session or the engine:

.. autofunction:: mendeleev.db.get_session

.. autofunction:: mendeleev.db.get_engine


Export data
-----------

The data can be exported to a number of formats using the CLI by invoking `inv export` command. The following formats are supported:

- csv
- json
- html
- markdown

The command will export all the tables from the database to a set of files in the specified format.

In order to use this functionality you'll need to clone the mendeleev repository and install the package in the development mode. Here's how you can do it:

.. code-block:: bash

    gh clone lmmentel/mendeleev
    cd mendeleev
    poetry install
    poetry run inv export


After the command is executed you'll find the exported files in the `data` directory. The
contents should look like this:

.. code-block:: bash

    data
    ├── csv
    │   ├── elements.csv
    │   ├── groups.csv
    │   ├── ionicradii.csv
    │   ├── ionizationenergies.csv
    │   ├── isotopedecaymodes.csv
    │   ├── isotopes.csv
    │   ├── oxidationstates.csv
    │   ├── phasetransitions.csv
    │   ├── screeningconstants.csv
    │   └── series.csv
    ├── html
    │   ├── elements.html
    │   ├── groups.html
    │   ├── ionicradii.html
    │   ├── ionizationenergies.html
    │   ├── isotopedecaymodes.html
    │   ├── isotopes.html
    │   ├── oxidationstates.html
    │   ├── phasetransitions.html
    │   ├── screeningconstants.html
    │   └── series.html
    ├── json
    │   ├── elements.json
    │   ├── groups.json
    │   ├── ionicradii.json
    │   ├── ionizationenergies.json
    │   ├── isotopedecaymodes.json
    │   ├── isotopes.json
    │   ├── oxidationstates.json
    │   ├── phasetransitions.json
    │   ├── screeningconstants.json
    │   └── series.json
    └── markdown
        ├── elements.markdown
        ├── groups.markdown
        ├── ionicradii.markdown
        ├── ionizationenergies.markdown
        ├── isotopedecaymodes.markdown
        ├── isotopes.markdown
        ├── oxidationstates.markdown
        ├── phasetransitions.markdown
        ├── screeningconstants.markdown
        └── series.markdown
