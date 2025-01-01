.. _data-access:

Accessing data
==============

.. tip:: Data assets repository

    If you're looking for raw data behind ``mendeleev`` have a look at `mendeleev-data <https://github.com/lmmentel/mendeleev-data>`_ repo.

    You can find **all data assets** in multiple formats: 
    - csv, 
    - html,
    - json, 
    - sql,
    - markdown.

    All releases a tagged with the same version numbers as ``mendeeleev``.

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
- :ref:`isotopedecaymodes <isotopedecaymode-class>`
- :ref:`isotopes <isotope-class>`
- :ref:`oxidationstates <oxidationstate-class>`
- :ref:`phasetransitions <phasetransition-class>`
- :ref:`propertymetadata <propertymetadata-class>`
- :ref:`scattering_factors <scatteringfactor-class>`
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


Export data
-----------

The data can be exported to a number of formats using the CLI by invoking `inv export` command. The following formats are supported:

- csv
- json
- html
- markdown

The command will export all the tables from the database to a set of files in the specified format.

In order to use this functionality you'll need to clone the mendeleev repository and install the package in the development mode. Here's how you can do it:

.. code-block:: bash

    gh clone lmmentel/mendeleev
    cd mendeleev
    poetry install
    poetry run inv export


After the command is executed you'll find the exported files in the `data` directory. The
contents should look like this:

.. code-block:: bash

    data
    ├── csv
    │   ├── elements.csv
    │   ├── groups.csv
    │   ├── ionicradii.csv
    │   ├── ionizationenergies.csv
    │   ├── isotopedecaymodes.csv
    │   ├── isotopes.csv
    │   ├── oxidationstates.csv
    │   ├── phasetransitions.csv
    │   ├── screeningconstants.csv
    │   └── series.csv
    ├── html
    │   ├── elements.html
    │   ├── groups.html
    │   ├── ionicradii.html
    │   ├── ionizationenergies.html
    │   ├── isotopedecaymodes.html
    │   ├── isotopes.html
    │   ├── oxidationstates.html
    │   ├── phasetransitions.html
    │   ├── screeningconstants.html
    │   └── series.html
    ├── json
    │   ├── elements.json
    │   ├── groups.json
    │   ├── ionicradii.json
    │   ├── ionizationenergies.json
    │   ├── isotopedecaymodes.json
    │   ├── isotopes.json
    │   ├── oxidationstates.json
    │   ├── phasetransitions.json
    │   ├── screeningconstants.json
    │   └── series.json
    └── markdown
        ├── elements.markdown
        ├── groups.markdown
        ├── ionicradii.markdown
        ├── ionizationenergies.markdown
        ├── isotopedecaymodes.markdown
        ├── isotopes.markdown
        ├── oxidationstates.markdown
        ├── phasetransitions.markdown
        ├── screeningconstants.markdown
        └── series.markdown
