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
returns either a single :py:class:`Element <mendeleev.models.Element>` instance or a tuple of those instances depending on the input. It provides a more flexible interface
since it accepts element names, atomic numbers and symbols as well as their combinations.

.. autofunction:: element

Tables
------

.. currentmodule:: mendeleev.fetch

If you want a whole set of data you can retrieve one of the tables from the
database as `pandas <http://pandas.pydata.org/>`_
`DataFrame <http://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.html>`_ through the :py:func:`get_table <mendeleev.mendeleev.get_table>`. The following
tables are available:
                         
- :ref:`elements <element-class>`
- :ref:`ions <ion-class>`
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

.. autofunction:: fetch_electronegativities


Database session and engine
---------------------------

For those how want to interact with the database through
a layer of `SQLAlchemy <http://www.sqlalchemy.org/>`_ there are methods
for getting the session or the engine:

.. autofunction:: mendeleev.db.get_session

.. autofunction:: mendeleev.db.get_engine


Classes
=======

.. _element-class:

Element
-------

.. currentmodule:: mendeleev.models

.. autoclass:: mendeleev.models.Element
   :members:


.. _ion-class:

Ion
---

.. currentmodule:: mendeleev.ion

.. autoclass:: mendeleev.ion.Ion
   :members:


.. _ionicradius-class:

IonicRadius
-----------

.. currentmodule:: mendeleev.models

.. autoclass:: mendeleev.models.IonicRadius
   :members:

.. _ionizationenergy-class:

IonizationEnergy
----------------

.. currentmodule:: mendeleev.models

.. autoclass:: mendeleev.models.IonizationEnergy
   :members:

.. _isotope-class:

Isotope
-------

.. currentmodule:: mendeleev.models

.. autoclass:: mendeleev.models.Isotope
   :members:

.. _screeningconstant-class:

ScreeningConstant
-----------------

.. currentmodule:: mendeleev.models

.. autoclass:: mendeleev.models.ScreeningConstant
   :members:

.. _series-class:

Series
------

.. currentmodule:: mendeleev.models

.. autoclass:: mendeleev.models.Series
   :members:

.. _group-class:

Group
-----

.. currentmodule:: mendeleev.models

.. autoclass:: mendeleev.models.Group
   :members:

.. _oxidationstate-class:

OxidationState
--------------

.. currentmodule:: mendeleev.models

.. autoclass:: mendeleev.models.OxidationState
   :members:


.. _econf-class:

ElectronicConfiguration
-----------------------

.. currentmodule:: mendeleev.econf

.. autoclass:: mendeleev.econf.ElectronicConfiguration
   :members:


Modules
=======

.. automodule:: mendeleev.electronegativity
   :members:

.. automodule:: mendeleev.plotting
   :members:

.. automodule:: mendeleev.utils
   :members:
