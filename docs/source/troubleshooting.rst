.. _troubleshooting:

***************
Troubleshooting
***************

This page covers common issues and their solutions when using mendeleev.

Installation Issues
===================

Missing Database File
---------------------

**Problem:** Error message about missing ``elements.db`` file.

**Solution:**
The database file should be included with the package installation. If it's missing:

1. Reinstall the package:

   .. code-block:: bash

       pip uninstall mendeleev
       pip install mendeleev

2. If using development installation, ensure you're in the correct directory:

   .. code-block:: bash

       cd /path/to/mendeleev
       poetry install

Dependencies Not Installed
---------------------------

**Problem:** Import errors for optional dependencies like ``bokeh``, ``plotly``, or ``seaborn``.

**Solution:**
Install with visualization dependencies:

.. code-block:: bash

    # Using pip
    pip install mendeleev[vis]

    # Using poetry
    poetry install --with vis

    # Using conda
    conda install -c conda-forge mendeleev bokeh plotly seaborn


Data Access Issues
==================

Element Not Found
-----------------

**Problem:** ``NoResultFound`` or similar error when accessing an element.

**Solution:**
Ensure you're using a valid identifier (symbol, name, or atomic number):

.. code-block:: python

    from mendeleev import element

    # Correct ways to access elements
    si = element('Si')           # Symbol (case-sensitive)
    si = element('Silicon')      # Name
    si = element(14)             # Atomic number

    # Common mistakes
    # element('si')  # Wrong: lowercase symbol
    # element('SI')  # Wrong: uppercase both letters

Missing Property Data
---------------------

**Problem:** Property returns ``None`` or ``NaN``.

**Solution:**
Not all properties are available for all elements. Check if the data exists:

.. code-block:: python

    from mendeleev import element

    el = element('H')

    # Check before using
    if el.atomic_radius is not None:
        print(f"Atomic radius: {el.atomic_radius} pm")
    else:
        print("Atomic radius not available for this element")

To see which elements have a specific property:

.. code-block:: python

    from mendeleev import fetch_table

    elements = fetch_table('elements')
    # Filter elements with atomic_radius data
    has_radius = elements[elements['atomic_radius'].notna()]
    print(f"Elements with atomic radius data: {len(has_radius)}")


Database Lock Errors
--------------------

**Problem:** ``OperationalError: database is locked``

**Solution:**
This can occur when multiple processes try to access the database simultaneously.

1. Ensure you close database sessions when done:

   .. code-block:: python

       from mendeleev.db import get_session

       session = get_session()
       try:
           # Your database operations
           pass
       finally:
           session.close()

2. For read-only operations, use the higher-level API (``element()``, ``fetch_table()``)
   instead of direct database access.


Performance Issues
==================

Slow Import Times
-----------------

**Problem:** Importing mendeleev takes a long time.

**Solution:**
Import only what you need:

.. code-block:: python

    # Instead of importing all elements
    # from mendeleev import *

    # Import specific elements
    from mendeleev import element, H, C, O

    # Or use the element function
    from mendeleev import element
    si = element('Si')

**Check import time:**

.. code-block:: bash

    poetry run inv timeimport

Slow Data Fetching
------------------

**Problem:** Fetching large amounts of data is slow.

**Solution:**

1. Use ``fetch_table()`` for bulk data access instead of iterating over elements:

   .. code-block:: python

       # Slow approach
       from mendeleev import element
       data = []
       for i in range(1, 119):
           el = element(i)
           data.append(el.atomic_radius)

       # Fast approach
       from mendeleev import fetch_table
       elements = fetch_table('elements')
       data = elements['atomic_radius'].tolist()

2. Select only the columns you need:

   .. code-block:: python

       from mendeleev import fetch_table

       # Get only specific columns
       df = fetch_table('elements')
       subset = df[['symbol', 'atomic_number', 'atomic_radius']]


Visualization Issues
====================

Bokeh/Plotly Not Displaying
----------------------------

**Problem:** Visualizations don't show in Jupyter notebooks.

**Solution:**

For Bokeh:

.. code-block:: python

    from bokeh.io import output_notebook
    output_notebook()

    # Then create your visualization
    from mendeleev.vis import periodic_table
    periodic_table(...)

For Plotly:

.. code-block:: python

    import plotly.io as pio
    pio.renderers.default = "notebook"

    # Then create your visualization

Missing Visualization Dependencies
-----------------------------------

**Problem:** Import error for visualization modules.

**Solution:**
Install visualization dependencies:

.. code-block:: bash

    pip install mendeleev[vis]
    # or
    poetry install --with vis


Type Hinting Issues
===================

MyPy or Type Checker Errors
---------------------------

**Problem:** Type checkers report errors when using mendeleev.

**Solution:**
Some type information may be incomplete. You can:

1. Add type ignore comments for specific lines:

   .. code-block:: python

       from mendeleev import element
       si = element('Si')  # type: ignore

2. Install pandas-stubs for better pandas type support:

   .. code-block:: bash

       pip install pandas-stubs


Data Inconsistencies
====================

Unexpected Property Values
--------------------------

**Problem:** A property value seems incorrect or outdated.

**Solution:**

1. Check the citation keys to see the data source:

   .. code-block:: python

       from mendeleev import fetch_table

       metadata = fetch_table('propertymetadata')
       prop_info = metadata[metadata['attribute_name'] == 'atomic_radius']
       print(prop_info['citation_keys'])

2. Report data issues on GitHub with:

   - Element and property name
   - Expected vs. actual value
   - Reference to correct data source

   `Report data issue → <https://github.com/lmmentel/mendeleev/issues/new>`_


Getting Help
============

If you can't find a solution here:

1. **Search existing issues**: `GitHub Issues <https://github.com/lmmentel/mendeleev/issues>`_
2. **Start a discussion**: `GitHub Discussions <https://github.com/lmmentel/mendeleev/discussions>`_
3. **Report a bug**: `Bug Report <https://github.com/lmmentel/mendeleev/issues/new?template=bug_report.md>`_

When reporting issues, please include:

- mendeleev version (``python -c "import mendeleev; print(mendeleev.__version__)"``）
- Python version
- Operating system
- Minimal code example that reproduces the issue
- Full error traceback

See Also
========

- :doc:`Installation <install>`
- :doc:`Getting started <quick>`
- :doc:`FAQ <faq>`
- :doc:`Contributing guide <CONTRIBUTING>`
