.. _installation:

************
Installation
************

Requirements
============

Python 3.10, 3.11, 3.12, 3.13, or 3.14.

User installation
=================

pip
---

.. code-block:: bash

   pip install mendeleev

With visualization support (bokeh, plotly, seaborn):

.. code-block:: bash

   pip install mendeleev[vis]

conda-forge
-----------

.. code-block:: bash

   conda install conda-forge::mendeleev

Latest from source
------------------

.. code-block:: bash

   pip install git+https://github.com/lmmentel/mendeleev.git


Development setup
=================

For contributors who want to run tests, build docs, or modify the code:

.. code-block:: bash

   git clone https://github.com/lmmentel/mendeleev.git
   cd mendeleev

   # Install core dependencies
   poetry install

   # With visualization extras
   poetry install --with vis

   # Install pre-commit hooks (ruff lint + format)
   pre-commit install

   # Run tests
   poetry run pytest

   # Build docs
   cd docs
   poetry run pip install -r requirements.txt   # one-time
   poetry run make html

See :doc:`CONTRIBUTING` for full contribution guidelines.
