.. _data-access:

Accessing data
==============

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
- :ref:`isotopes <isotope-class>`
- :ref:`oxidationstates <oxidationstate-class>`
- :ref:`screeningconstants <screeningconstant-class>`
- :ref:`series <series-class>`

.. autofunction:: fetch_table

.. autofunction:: fetch_ionization_energies

.. autofunction:: fetch_ionic_radii



Computed properties
-------------------

Some properties need to be computed rather than directly retrieved from the database. :doc:`electronegativity`

.. autofunction:: fetch_electronegativities



Database session and engine
---------------------------

For those how want to interact with the database through
a layer of `SQLAlchemy <http://www.sqlalchemy.org/>`_ there are methods
for getting the session or the engine:

.. autofunction:: mendeleev.db.get_session

.. autofunction:: mendeleev.db.get_engine