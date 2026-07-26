.. _api:

*************
API Reference
*************

Here you'll find API documentation of the mendeleev's modules. For most users it'll be enough to use the high-level API provided by the classes below.
For more advanced use cases you can use the lower-level functions and classes across the modules.

.. tip::
   New to the API? Start with the :doc:`API Overview <../api_overview>` for architecture explanations,
   usage patterns, and a decision guide to help you choose the right functions.

.. toctree::
   :maxdepth: 2

   Models <models>


Core Modules
============

High-level functions and classes for accessing element data.

.. autosummary::
   :toctree:

   mendeleev.mendeleev
   mendeleev.fetch
   mendeleev.ion

Data Models
===========

SQLAlchemy models representing chemical entities and properties.

.. autosummary::
   :toctree:

   mendeleev.models

Specialized Modules
===================

Modules for specific calculations and data processing.

.. autosummary::
   :toctree:

   mendeleev.electronegativity
   mendeleev.econf

Utility Modules
===============

Database access and utility functions.

.. autosummary::
   :toctree:

   mendeleev.db
   mendeleev.utils
   mendeleev.cli


Visualization
=============

The main entry point for visualizing periodic tables with different
properties is the :func:`mendeleev.vis.periodictable.periodic_table` function.

.. toctree::

   mendeleev.vis.periodictable
   mendeleev.vis.bokeh
   mendeleev.vis.plotly
   mendeleev.vis.seaborn
   mendeleev.vis.utils