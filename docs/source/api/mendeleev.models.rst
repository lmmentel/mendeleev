mendeleev.models
================

.. automodule:: mendeleev.models

   This module contains all the SQLAlchemy data models representing chemical entities
   and their properties. These models map to tables in the SQLite database.

   .. note::
      For detailed documentation of each model class, see :doc:`models`.
      Most users will access these through :func:`mendeleev.element() <mendeleev.mendeleev.element>` or
      :func:`mendeleev.fetch.fetch_table`.

      The :class:`~mendeleev.ion.Ion` class is documented separately in
      :doc:`mendeleev.ion` as it's not a SQLAlchemy model.
