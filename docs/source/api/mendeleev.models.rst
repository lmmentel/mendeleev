mendeleev.models
================

.. automodule:: mendeleev.models

   This module contains all the SQLAlchemy data models representing chemical entities
   and their properties. These models map to tables in the SQLite database.

   .. rubric:: Core Models

   .. autosummary::
      :toctree:

      Element
      Isotope
      Ion

   .. rubric:: Property Models

   .. autosummary::
      :toctree:

      IonicRadius
      IonizationEnergy
      OxidationState
      ScreeningConstant
      ScatteringFactor
      PhaseTransition

   .. rubric:: Organization Models

   .. autosummary::
      :toctree:

      Group
      Series

   .. rubric:: Metadata Models

   .. autosummary::
      :toctree:

      PropertyMetadata

   .. rubric:: Enumerations

   .. autosummary::
      :toctree:

      ValueOrigin

   .. note::
      For detailed documentation of each model class, see :doc:`models`.
      Most users will access these through :func:`mendeleev.element` or
      :func:`mendeleev.fetch.fetch_table`.
