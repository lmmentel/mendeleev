.. _api-overview:

************
API Overview
************

This page provides a high-level overview of the mendeleev API, explaining the main components,
common usage patterns, and how to choose the right function or class for your needs.

.. contents:: On this page
   :local:
   :depth: 2

Architecture
============

The mendeleev package is organized into several layers:

.. code-block:: text

    User-Facing API
    ├── Element Access (element, isotope)
    ├── Bulk Data (fetch_table, fetch_*)
    └── Visualization (periodic_table)
         │
    Data Models
    ├── Element, Isotope, Ion
    ├── IonicRadius, IonizationEnergy
    └── Other property classes
         │
    Database Layer
    └── SQLite database (elements.db)

Main Components
===============

1. Element Access Functions
----------------------------

High-level functions for accessing individual elements and isotopes.

:py:func:`element <mendeleev.mendeleev.element>`
    Primary function for getting element data by symbol, name, or atomic number.
    **Use this** for most element access needs.

:py:func:`isotope <mendeleev.mendeleev.isotope>`
    Get specific isotope data by element and mass number.

:py:func:`get_all_elements <mendeleev.mendeleev.get_all_elements>`
    Get a list of all elements. **Note**: For data analysis, use :py:func:`fetch_table <mendeleev.fetch.fetch_table>` instead.

**Example**::

    from mendeleev import element

    # Get silicon by symbol
    si = element('Si')
    print(si.atomic_radius)  # 132

    # Get multiple elements
    c, h, o = element(['C', 'H', 'O'])

2. Data Fetching Functions
---------------------------

Functions for bulk data access, returning pandas DataFrames.

:py:func:`fetch_table <mendeleev.fetch.fetch_table>`
    Fetch any database table as a DataFrame. **Most versatile** bulk access function.
    Available tables: ``elements``, ``isotopes``, ``ionicradii``, ``ionizationenergies``,
    ``oxidationstates``, ``screeningconstants``, ``series``, ``groups``, ``propertymetadata``.

:py:func:`fetch_electronegativities <mendeleev.fetch.fetch_electronegativities>`
    Get electronegativity data across multiple scales.

:py:func:`fetch_ionization_energies <mendeleev.fetch.fetch_ionization_energies>`
    Get ionization energy data for specific degrees.

:py:func:`fetch_ionic_radii <mendeleev.fetch.fetch_ionic_radii>`
    Get ionic radii data with different radius types.

**Example**::

    from mendeleev import fetch_table

    # Get all elements as DataFrame
    elements = fetch_table('elements')

    # Filter and analyze
    noble_gases = elements[elements['group_id'] == 18]
    print(noble_gases[['symbol', 'name', 'boiling_point']])

3. Data Models
--------------

Object-oriented representations of chemical entities and properties.

**Core Models:**

:py:class:`Element <mendeleev.models.Element>`
    The main element class with 80+ properties and methods.
    Access via :py:func:`element() <mendeleev.mendeleev.element>`.

:py:class:`Isotope <mendeleev.models.Isotope>`
    Isotope data including mass, abundance, half-life, and decay modes.
    Access via :py:func:`isotope() <mendeleev.mendeleev.isotope>` or ``element.isotopes``.

:py:class:`Ion <mendeleev.ion.Ion>`
    Ionic species with charge-dependent properties.
    Create with ``Ion('Fe', charge=2)``.

**Property Models:**

:py:class:`IonicRadius <mendeleev.models.IonicRadius>`
    Ionic radii for different oxidation states and coordination numbers.

:py:class:`IonizationEnergy <mendeleev.models.IonizationEnergy>`
    Successive ionization energies.

:py:class:`OxidationState <mendeleev.models.OxidationState>`
    Possible oxidation states for elements.

:py:class:`PropertyMetadata <mendeleev.models.PropertyMetadata>`
    Metadata about properties including units, sources, and citations.

4. Visualization Functions
---------------------------

Functions for creating interactive periodic table visualizations.

:py:func:`periodic_table <mendeleev.vis.periodictable.periodic_table>`
    Main function for creating customizable periodic tables.
    Supports multiple backends: bokeh, plotly, seaborn.

**Backends:**

- :py:mod:`mendeleev.vis.bokeh` - Interactive Bokeh visualizations
- :py:mod:`mendeleev.vis.plotly` - Interactive Plotly visualizations
- :py:mod:`mendeleev.vis.seaborn` - Static matplotlib/seaborn visualizations

**Example**::

    from mendeleev.vis import periodic_table

    # Create interactive periodic table colored by property
    periodic_table(colorby='atomic_radius', backend='plotly')

5. Electronegativity Functions
-------------------------------

Functions for computing various electronegativity scales.

:py:mod:`mendeleev.electronegativity`
    Module containing functions for 15+ electronegativity scales:

    - **Stored scales**: Access via ``element.en_pauling``, ``element.en_allen``, etc.
    - **Computed scales**: Functions like :py:func:`mulliken() <mendeleev.electronegativity.mulliken>`,
      :py:func:`sanderson() <mendeleev.electronegativity.sanderson>`, etc.

See :doc:`electronegativity` for detailed scale descriptions.

6. Database Functions
---------------------

Low-level database access (advanced users).

:py:func:`get_session <mendeleev.db.get_session>`
    Get SQLAlchemy session for direct database queries.

:py:func:`get_engine <mendeleev.db.get_engine>`
    Get SQLAlchemy engine.

**Note**: Most users should use :py:func:`element() <mendeleev.mendeleev.element>`
or :py:func:`fetch_table() <mendeleev.fetch.fetch_table>` instead.

Common Usage Patterns
======================

Pattern 1: Single Element Properties
-------------------------------------

**Use case**: Get specific properties for one or a few elements.

**Use**: :py:func:`element() <mendeleev.mendeleev.element>`

::

    from mendeleev import element

    si = element('Si')
    print(f"Atomic radius: {si.atomic_radius} pm")
    print(f"Electronegativity: {si.en_pauling}")
    print(f"Melting point: {si.melting_point} K")

Pattern 2: Bulk Data Analysis
------------------------------

**Use case**: Analyze properties across many elements.

**Use**: :py:func:`fetch_table() <mendeleev.fetch.fetch_table>`

::

    from mendeleev import fetch_table
    import matplotlib.pyplot as plt

    # Get all elements
    df = fetch_table('elements')

    # Analyze trends
    metals = df[df['block'].isin(['s', 'd', 'f'])]

    # Plot
    plt.scatter(metals['atomic_number'], metals['density'])
    plt.xlabel('Atomic Number')
    plt.ylabel('Density (g/cm³)')
    plt.show()

Pattern 3: Isotope Information
-------------------------------

**Use case**: Get isotope data for an element.

**Method 1**: Via element object

::

    from mendeleev import element

    carbon = element('C')
    for iso in carbon.isotopes:
        print(f"C-{iso.mass_number}: {iso.abundance}%")

**Method 2**: Direct isotope access

::

    from mendeleev import isotope

    c14 = isotope('C', 14)
    print(f"Half-life: {c14.half_life} years")

Pattern 4: Ion Properties
--------------------------

**Use case**: Work with ionic species.

**Use**: :py:class:`Ion <mendeleev.ion.Ion>` class

::

    from mendeleev.ion import Ion

    fe2 = Ion('Fe', charge=2)
    fe3 = Ion('Fe', charge=3)

    print(f"Fe²⁺ ionic radius: {fe2.ionic_radius} pm")
    print(f"Fe³⁺ ionic radius: {fe3.ionic_radius} pm")

Pattern 5: Visualization
-------------------------

**Use case**: Create periodic table visualizations.

**Use**: :py:func:`periodic_table() <mendeleev.vis.periodictable.periodic_table>`

::

    from mendeleev.vis import periodic_table

    # Interactive plot with plotly
    periodic_table(
        colorby='atomic_radius',
        title='Atomic Radii',
        backend='plotly'
    )

    # Static plot with seaborn
    periodic_table(
        colorby='electronegativity_pauling',
        backend='seaborn',
        output='en_plot.png'
    )

Pattern 6: Electronegativity Comparison
----------------------------------------

**Use case**: Compare multiple electronegativity scales.

**Use**: :py:func:`fetch_electronegativities() <mendeleev.fetch.fetch_electronegativities>`

::

    from mendeleev import fetch_electronegativities

    # Get specific scales
    en_df = fetch_electronegativities(['pauling', 'allen', 'mulliken'])

    # Compare for specific element
    si_en = en_df[en_df['symbol'] == 'Si']
    print(si_en)

Pattern 7: Property Metadata Lookup
------------------------------------

**Use case**: Find units, sources, and citations for properties.

**Use**: :py:class:`PropertyMetadata <mendeleev.models.PropertyMetadata>`

::

    from mendeleev import fetch_table

    metadata = fetch_table('propertymetadata')

    # Find properties with energy units
    energy_props = metadata[metadata['unit'].str.contains('eV', na=False)]
    print(energy_props[['attribute_name', 'unit', 'citation_keys']])

Decision Guide
==============

Use this flowchart to choose the right API component:

.. code-block:: text

    What do you want to do?
    │
    ├─ Get data for ONE element
    │  └─> Use element('Symbol')
    │
    ├─ Get data for MANY elements
    │  └─> Use fetch_table('elements')
    │
    ├─ Get isotope data
    │  ├─ For one isotope
    │  │  └─> Use isotope('Symbol', mass_number)
    │  └─ For all isotopes of element
    │     └─> Use element('Symbol').isotopes
    │
    ├─ Work with ions
    │  └─> Use Ion('Symbol', charge=N)
    │
    ├─ Create visualizations
    │  └─> Use periodic_table(...)
    │
    ├─ Compare electronegativity scales
    │  └─> Use fetch_electronegativities([scales])
    │
    └─ Direct database queries
       └─> Use get_session() (advanced)

Quick Reference
===============

Most Common Functions
---------------------

.. list-table::
   :header-rows: 1
   :widths: 30 50 20

   * - Function
     - Purpose
     - Returns
   * - ``element(id)``
     - Get element by symbol/name/number
     - Element
   * - ``fetch_table(name)``
     - Get database table as DataFrame
     - DataFrame
   * - ``isotope(el, mass)``
     - Get specific isotope
     - Isotope
   * - ``periodic_table(...)``
     - Create visualization
     - Plot/Figure
   * - ``Ion(el, charge)``
     - Create ionic species
     - Ion

Most Useful Element Properties
-------------------------------

.. list-table::
   :header-rows: 1
   :widths: 25 35 20 20

   * - Property
     - Description
     - Unit
     - Example
   * - ``atomic_number``
     - Atomic number
     - —
     - ``14``
   * - ``atomic_weight``
     - Atomic weight
     - Da
     - ``28.085``
   * - ``atomic_radius``
     - Atomic radius (Slater)
     - pm
     - ``132``
   * - ``electronegativity_pauling``
     - Pauling electronegativity
     - —
     - ``1.9``
   * - ``electron_affinity``
     - Electron affinity
     - eV
     - ``1.39``
   * - ``ionization_energies``
     - Ionization energies
     - eV
     - ``[8.15, ...]``
   * - ``melting_point``
     - Melting point
     - K
     - ``1683``
   * - ``boiling_point``
     - Boiling point
     - K
     - ``2628``
   * - ``density``
     - Density at 295K
     - g/cm³
     - ``2.33``
   * - ``isotopes``
     - List of isotopes
     - —
     - ``[Isotope, ...]``

Available Database Tables
-------------------------

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Table Name
     - Contents
   * - ``elements``
     - All element data (main table)
   * - ``isotopes``
     - Isotope data with masses, abundances, half-lives
   * - ``ionicradii``
     - Ionic radii for various oxidation states
   * - ``ionizationenergies``
     - Successive ionization energies
   * - ``oxidationstates``
     - Possible oxidation states
   * - ``screeningconstants``
     - Nuclear screening constants
   * - ``groups``
     - Periodic table group information
   * - ``series``
     - Element series (alkali metals, noble gases, etc.)
   * - ``propertymetadata``
     - Metadata about properties (units, sources, citations)
   * - ``isotopedecaymodes``
     - Isotope decay modes and branching ratios
   * - ``phasetransitions``
     - Phase transition data
   * - ``scattering_factors``
     - X-ray and neutron scattering factors

Type Hints
==========

The mendeleev API uses type hints extensively. Here are the main types:

.. code-block:: python

    from typing import Union, List
    from mendeleev.models import Element, Isotope
    from mendeleev.ion import Ion
    import pandas as pd

    # Element access
    element(ids: Union[int, str]) -> Element
    element(ids: Union[List, Tuple]) -> List[Element]

    # Isotope access
    isotope(symbol_or_atn: Union[str, int], mass_number: int) -> Isotope

    # Bulk data
    fetch_table(table: str) -> pd.DataFrame

    # Ions
    Ion(label: Union[str, int], charge: int) -> Ion

Error Handling
==============

Common exceptions and how to handle them:

**ValueError: Element not found**

::

    from mendeleev import element

    try:
        el = element('Unobtanium')
    except ValueError as e:
        print(f"Element not found: {e}")

**ValueError: Invalid charge for ion**

::

    from mendeleev.ion import Ion

    try:
        # Charge too large
        ion = Ion('H', charge=5)
    except ValueError as e:
        print(f"Invalid charge: {e}")

**NoResultFound: Isotope not found**

::

    from mendeleev import isotope
    from sqlalchemy.exc import NoResultFound

    try:
        # Non-existent isotope
        iso = isotope('C', 999)
    except NoResultFound:
        print("Isotope not found")

See Also
========

- :doc:`data_access` - Detailed guide on accessing data
- :doc:`data` - Complete property reference
- :doc:`tutorials` - Step-by-step tutorials
- :doc:`api/api` - Complete API reference
- :doc:`troubleshooting` - Common issues and solutions

Next Steps
==========

**New Users**: Start with the :doc:`quick start guide <quick>` and :doc:`tutorials <tutorials>`.

**Data Analysis**: Learn about :doc:`bulk data access <notebooks/bulk_data_access>`.

**Visualization**: Explore :doc:`visualization tutorials <notebooks/visualizations>`.

**Advanced**: Read the full :doc:`API Reference <api/api>`.
