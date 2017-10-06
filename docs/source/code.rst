.. currentmodule:: mendeleev.mendeleev
.. _api:

*************
API Reference
*************

Accessing data
==============

Elements
--------

The easiest way to access individual elements is simply by importing them from
the :doc:`mendeleev </index>` directly using their symbols::

    >>> from mendeleev import H, C, O, Og
    >>> [x.name for x in [H, C, O, Og]]
    ['Hydrogen', 'Carbon', 'Oxygen', 'Oganesson']


An alternative method of access is through the :py:func:`element` function that
returns either a single :py:class:`Element <mendeleev.tables.Element>` instance or a tuple of those instances depending on the input. It provides a more flexible interface
since it accepts element names, atomic numbers and symbols as well as their combinations.

.. autofunction:: element

Tables
------

If you want a whole set of data you can retrieve one of the tables from the
database as `pandas <http://pandas.pydata.org/>`_
`DataFrame <http://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.html>`_ through the :py:func:`get_table <mendeleev.mendeleev.get_table>`. The following
tables are available:
                         
- :ref:`elements <element-class>`
- :ref:`groups <group-class>`
- :ref:`ionicradii <ionicradius-class>`
- :ref:`ionizationenergies <ionizationenergy-class>`
- :ref:`isotopes <isotope-class>`
- :ref:`oxidationstates <oxidationstate-class>`
- :ref:`screeningconstants <screeningconstant-class>`
- :ref:`series <series-class>`

.. autofunction:: get_table


Database session and engine
---------------------------

For those how want to interact with the database through
a layer of `SQLAlchemy <http://www.sqlalchemy.org/>`_ there are methods
for getting the session or the engine:

.. autofunction:: mendeleev.mendeleev.get_session

.. autofunction:: mendeleev.mendeleev.get_engine


Classes
=======


.. _element-class:

Element
-------

.. currentmodule:: mendeleev.tables

.. autoclass:: mendeleev.tables.Element
   :members:

.. _ionicradius-class:

IonicRadius
-----------

.. currentmodule:: mendeleev.tables

.. autoclass:: mendeleev.tables.IonicRadius
   :members:

.. _ionizationenergy-class:

IonizationEnergy
----------------

.. currentmodule:: mendeleev.tables

.. autoclass:: mendeleev.tables.IonizationEnergy
   :members:

.. _isotope-class:

Isotope
-------

.. currentmodule:: mendeleev.tables

.. autoclass:: mendeleev.tables.Isotope
   :members:

.. _screeningconstant-class:

ScreeningConstant
-----------------

.. currentmodule:: mendeleev.tables

.. autoclass:: mendeleev.tables.ScreeningConstant
   :members:

.. _series-class:

Series
------

.. currentmodule:: mendeleev.tables

.. autoclass:: mendeleev.tables.Series
   :members:

.. _group-class:

Group
-----

.. currentmodule:: mendeleev.tables

.. autoclass:: mendeleev.tables.Group
   :members:

.. _oxidationstate-class:

OxidationState
--------------

.. currentmodule:: mendeleev.tables

.. autoclass:: mendeleev.tables.OxidationState
   :members:


.. _econf-class:

ElectronicConfiguration
-----------------------

.. currentmodule:: mendeleev.econf

.. autoclass:: mendeleev.econf.ElectronicConfiguration
   :members:
