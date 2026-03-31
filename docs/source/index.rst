.. _mendeleev:

************************************
Welcome to mendeleev's documentation
************************************

.. raw:: html

   <img src="_static/img/name_and_logo.png" alt="Logo" style="display: block;margin-left: auto;margin-right: auto;">


**Pythonic periodic table of elements**

A Python package with a convenient API for accessing various properties of elements, ions, and isotopes
in the periodic table. Visualize trends, explore chemical data, and integrate periodic table information
into your scientific workflows.

.. image:: _static/img/mendeleev_periodic_series.png
   :width: 1000px
   :align: center
   :alt: Periodic table

Quick Installation
==================

Install from conda-forge (recommended):

.. code-block:: bash

   conda install conda-forge::mendeleev

Or via pip:

.. code-block:: bash

   pip install mendeleev

Quick Start
===========

Access element data directly:

.. code-block:: python

   >>> from mendeleev import element

   >>> si = element('Si')
   >>> si.name
   'Silicon'
   >>> si.atomic_number
   14
   >>> si.thermal_conductivity
   149

   >>> # Access isotopes
   >>> for iso in si.isotopes:
   ...     print(f"{iso.mass_number}: {iso.abundance}%")
   28: 92.23%
   29: 4.67%
   30: 3.10%

Or import elements by symbol:

.. code-block:: python

   >>> from mendeleev import Fe, O, H
   >>> Fe.name
   'Iron'
   >>> H.atomic_weight
   1.008

Key Features
============

📊 **Rich Dataset**
   Access 100+ properties per element including atomic, physical, thermodynamic, and electronic data

🔬 **Isotope Information**
   Complete isotope data with abundances, masses, half-lives, and nuclear properties

📏 **Units Support** (v1.1.0+)
   Integration with `pint <https://pint.readthedocs.io/>`_ for unit-aware calculations and conversions

📈 **Visualization**
   Create custom periodic tables with `bokeh <https://bokeh.org/>`_ and explore trends interactively

🗄️ **Data Access**
   Query the SQLite database directly or export to pandas DataFrames

⚡ **Multiple Access Methods**
   By symbol, name, atomic number, or bulk queries

Explore the Documentation
==========================

Getting Started
---------------

New to mendeleev? Start here!

.. grid:: 2

   .. grid-item-card:: 📖 Installation Guide
      :link: install
      :link-type: doc

      Step-by-step installation instructions for conda, pip, and development setup.

   .. grid-item-card:: 🚀 Tutorials
      :link: tutorials
      :link-type: doc

      Interactive Jupyter notebooks covering common use cases and advanced features.

Data & Features
---------------

Learn what data is available and how to use it.

.. grid:: 2

   .. grid-item-card:: 🔢 Available Data
      :link: data
      :link-type: doc

      Comprehensive list of 100+ element properties with references and metadata.

   .. grid-item-card:: 📊 Accessing Data
      :link: data_access
      :link-type: doc

      Query elements, fetch tables, export to pandas, and work with the database.

   .. grid-item-card:: 📏 Units Support
      :link: units
      :link-type: doc

      Work with physical units using pint integration (v1.1.0+).

   .. grid-item-card:: ⚡ Electronegativity
      :link: electronegativity
      :link-type: doc

      Calculate electronegativity using multiple scales and methods.

API Documentation
-----------------

Detailed API reference and architecture.

.. grid:: 2

   .. grid-item-card:: 🏗️ API Overview
      :link: api_overview
      :link-type: doc

      Architecture, usage patterns, and decision flowchart for choosing the right approach.

   .. grid-item-card:: 📚 API Reference
      :link: api/api
      :link-type: doc

      Complete reference for all modules, classes, and functions.

Help & Resources
----------------

Get help and contribute to the project.

.. grid:: 2

   .. grid-item-card:: ❓ FAQ
      :link: faq
      :link-type: doc

      Frequently asked questions about installation, usage, and development.

   .. grid-item-card:: 🔧 Troubleshooting
      :link: troubleshooting
      :link-type: doc

      Common issues and solutions for data access, performance, and visualization.

   .. grid-item-card:: 🤝 Contributing
      :link: CONTRIBUTING
      :link-type: doc

      Learn how to contribute code, report bugs, and suggest enhancements.

   .. grid-item-card:: 📖 Bibliography
      :link: bibliography
      :link-type: doc

      Data sources and references used in mendeleev.


.. toctree::
   :caption: Documentation
   :maxdepth: 2
   :hidden:

   Overview <quick>
   Installation <install>
   Tutorials <tutorials>
   Data <data>
   Accessing data <data_access>
   Units <units>
   Electronegativity <electronegativity>
   FAQ <faq>
   Troubleshooting <troubleshooting>
   Contributing guide <CONTRIBUTING>
   API Overview <api_overview>
   API Reference <api/api>
   Bibliography <bibliography>
   Changes <changes_link>
   License <license_link>


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
