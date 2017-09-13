.. currentmodule:: mendeleev.mendeleev
.. _api:

*************
API Reference
*************

Accessing data
==============

Elements
--------

The most straightforward access is through the :py:func:`element` function that
returns either a single :py:class:`Element <mendeleev.tables.Element>` instance or a tuple of those instances
depending on the input. 

.. autofunction:: element

Tables
------

If you want a whole set of data you can retrieve one of the tables from the
database as `pandas <http://pandas.pydata.org/>`_
`DataFrame <http://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.html>`_ through the :py:func:`get_table <mendeleev.mendeleev.get_table>`. The following
tables are available:
                         
- elements              
- groups                  
- ionicradii        
- ionizationenergies
- isotopes          
- oxidationstates
- screeningconstants
- series

.. autofunction:: get_table


Database session and engine
---------------------------

For those how want to interact with the database through
a layer of `SQLAlchemy <http://www.sqlalchemy.org/>`_ there are methods
for getting the session or the engine:

.. autofunction:: mendeleev.mendeleev.get_session

.. autofunction:: mendeleev.mendeleev.get_engine



Element class
=============

.. currentmodule:: mendeleev.tables

.. autoclass:: mendeleev.tables.Element
   :members:
