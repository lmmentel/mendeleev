.. _api:

*************
API Reference
*************

Here you'll find API documentation of the mendeleev's modules. For most users it'll be enough to use the high-level API provided by the classes below.
For more advances use cases you can use the lower-level functions and classes across the modules.

.. toctree::
   :maxdepth: 2

   Models <models>


Modules
=======

.. autosummary::
   :toctree:

   mendeleev.cli
   mendeleev.db
   mendeleev.econf
   mendeleev.electronegativity
   mendeleev.fetch
   mendeleev.mendeleev
   mendeleev.utils


Visualization
=============

The main entry point for visualizing periodic tables with different
properties is the :func:`periodictable.periodic_table` function.

.. autosummary::
   :toctree:

   mendeleev.vis.bokeh
   mendeleev.vis.periodictable
   mendeleev.vis.plotly
   mendeleev.vis.seaborn
   mendeleev.vis.utils