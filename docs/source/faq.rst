.. _faq:

**************************
Frequently Asked Questions
**************************

General Questions
=================

What is mendeleev?
------------------

mendeleev is a Python library that provides a convenient API for accessing various
properties of chemical elements, ions, and isotopes from the periodic table. It includes
data on atomic properties, physical properties, ionization energies, isotopes, and more.

How is mendeleev different from other periodic table libraries?
----------------------------------------------------------------

mendeleev offers:

- **Comprehensive data**: Over 80 properties per element with proper citations
- **Multiple data types**: Elements, isotopes, ions, and their relationships
- **Electronegativity scales**: 15+ different scales, both stored and computed
- **Visualization**: Built-in periodic table visualizations using bokeh, plotly, and seaborn
- **Units support**: Integration with pint for proper physical units (v1.1.0+)
- **Database backend**: SQLAlchemy-based for flexible data access

See :doc:`citing` for related projects.

Is mendeleev free to use?
--------------------------

Yes! mendeleev is released under the MIT license, making it free for both academic and
commercial use. See :doc:`license_link` for full details.


Installation & Setup
====================

How do I install mendeleev?
----------------------------

The recommended method is using conda:

.. code-block:: bash

    conda install conda-forge::mendeleev

Or using pip:

.. code-block:: bash

    pip install mendeleev

For visualization features:

.. code-block:: bash

    pip install mendeleev[vis]

See :doc:`install` for more options.

Which Python versions are supported?
-------------------------------------

mendeleev supports Python 3.9, 3.10, 3.11, 3.12, and 3.13.

Do I need to download the database separately?
-----------------------------------------------

No, the database (``elements.db``) is included with the package and automatically
available after installation.


Using mendeleev
===============

How do I access element data?
------------------------------

There are several ways:

.. code-block:: python

    # Import by symbol directly
    from mendeleev import Si
    print(Si.name)  # 'Silicon'

    # Use the element function with symbol, name, or atomic number
    from mendeleev import element
    si = element('Si')       # Symbol
    si = element('Silicon')  # Name
    si = element(14)         # Atomic number

See :doc:`data_access` for more details.

How do I get data for multiple elements?
-----------------------------------------

Use ``fetch_table()`` for bulk data access:

.. code-block:: python

    from mendeleev import fetch_table

    # Get all elements as a pandas DataFrame
    elements = fetch_table('elements')

    # Filter and select specific data
    alkali_metals = elements[elements['group_id'] == 1]
    symbols = alkali_metals['symbol'].tolist()

See :doc:`notebooks/bulk_data_access` tutorial.

Can I access isotope data?
---------------------------

Yes, through the element's ``isotopes`` attribute:

.. code-block:: python

    from mendeleev import element

    carbon = element('C')
    for isotope in carbon.isotopes:
        print(f"C-{isotope.mass_number}: {isotope.abundance}%")

See :doc:`data` for available isotope properties.

How do I create visualizations?
--------------------------------

Use the ``periodic_table()`` function:

.. code-block:: python

    from mendeleev.vis import periodic_table

    # Create a periodic table colored by a property
    periodic_table(colorby='atomic_radius')

See :doc:`notebooks/visualizations` and :doc:`notebooks/advanced_visualizations` tutorials.

What electronegativity scales are available?
---------------------------------------------

mendeleev provides 15+ electronegativity scales:

- Stored: Allen, Ghosh, Pauling, Miedema, and more
- Computed: Allred-Rochow, Mulliken, Sanderson, Cottrell-Sutton, and more

.. code-block:: python

    from mendeleev import element

    si = element('Si')
    print(si.en_pauling)           # Pauling scale
    print(si.en_allen)             # Allen scale
    print(si.en_mulliken())        # Mulliken (computed)

See :doc:`electronegativity` for all available scales.


Data & Citations
================

Where does the data come from?
------------------------------

All data includes proper citations to peer-reviewed sources. You can view sources for
any property using the ``PropertyMetadata`` table:

.. code-block:: python

    from mendeleev import fetch_table

    metadata = fetch_table('propertymetadata')
    # View citation keys for a property
    prop = metadata[metadata['attribute_name'] == 'atomic_radius']
    print(prop[['attribute_name', 'citation_keys', 'description']])

See :doc:`bibliography` for full references.

How often is the data updated?
-------------------------------

The data is updated with new releases. Major updates include:

- Version 1.1.0 (2024): Added units support, updated property metadata
- Version 1.0.0 (2023): Major refactoring with pydantic models

Check :doc:`changes_link` for version history.

Can I export the data?
----------------------

Yes, using the export functionality:

.. code-block:: bash

    # Clone the repository
    git clone https://github.com/lmmentel/mendeleev.git
    cd mendeleev

    # Export to multiple formats (CSV, JSON, HTML, Markdown, SQL)
    poetry install
    poetry run inv export

Or access the raw data at `mendeleev-data <https://github.com/lmmentel/mendeleev-data>`_.

Is the data accurate?
---------------------

We strive for accuracy and include citations for all data. However:

- Some properties are only available for certain elements
- Data may be updated as new measurements are published
- Different sources may report slightly different values

If you find an error, please `report it <https://github.com/lmmentel/mendeleev/issues>`_.


Development & Contributing
===========================

How can I contribute?
---------------------

Contributions are welcome! You can:

- Report bugs or data inconsistencies
- Suggest new features
- Add missing data with proper citations
- Improve documentation
- Submit pull requests

See :doc:`CONTRIBUTING` for guidelines.

How do I run the tests?
------------------------

.. code-block:: bash

    # Install development dependencies
    poetry install

    # Run all tests
    poetry run pytest

    # Run with coverage
    poetry run pytest --cov=mendeleev

How do I build the documentation locally?
------------------------------------------

.. code-block:: bash

    cd docs
    make html

    # View the docs
    open build/html/index.html  # macOS
    # or
    xdg-open build/html/index.html  # Linux

Can I use mendeleev in my research paper?
------------------------------------------

Yes! Please cite it as:

    L. M. Mentel, *mendeleev* - A Python resource for properties of chemical
    elements, ions and isotopes. , 2014-- . Available at:
    https://github.com/lmmentel/mendeleev

See :doc:`citing` for BibTeX and BibLaTeX formats.


Performance
===========

Why is importing mendeleev slow?
---------------------------------

The initial import loads the database and models. To improve performance:

- Import only what you need: ``from mendeleev import element``
- Use bulk operations with ``fetch_table()`` instead of loops
- Consider lazy imports in performance-critical code

See :doc:`troubleshooting` for more optimization tips.

How can I speed up data access?
--------------------------------

Use ``fetch_table()`` for bulk operations instead of accessing elements individually:

.. code-block:: python

    # Slow (don't do this)
    from mendeleev import element
    radii = [element(i).atomic_radius for i in range(1, 119)]

    # Fast (do this)
    from mendeleev import fetch_table
    elements = fetch_table('elements')
    radii = elements['atomic_radius'].tolist()


Units & Conversions
===================

Does mendeleev support units?
------------------------------

Yes, starting from version 1.1.0, mendeleev integrates with the
`pint <https://pint.readthedocs.io/>`_ library for unit support.

See :doc:`units` for detailed information.

What units are properties stored in?
-------------------------------------

Common units include:

- Radii: picometers (pm)
- Energies: electron volts (eV)
- Temperatures: Kelvin (K)
- Masses: Daltons (Da)
- Densities: g/cm³

Check the ``PropertyMetadata`` table for specific units:

.. code-block:: python

    from mendeleev import fetch_table
    metadata = fetch_table('propertymetadata')
    print(metadata[['attribute_name', 'unit']])


Still Have Questions?
=====================

- Check :doc:`troubleshooting` for common issues
- Search `GitHub Issues <https://github.com/lmmentel/mendeleev/issues>`_
- Start a `Discussion <https://github.com/lmmentel/mendeleev/discussions>`_
- Read the full :doc:`API Reference <api/api>`
