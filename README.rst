
Installation_ | Documentation_  | Usage_ | Contributing_ | License_

##################
mendeleev_ package
##################

.. image:: https://readthedocs.org/projects/mendeleev/badge/
   :target: https://mendeleev.readthedocs.org
   :alt: Documentation Status

.. image:: https://img.shields.io/pypi/v/mendeleev.svg?style=flat-square&label=PYPI%20version
   :target: https://pypi.python.org/pypi/mendeleev
   :alt: Latest version released on PyPi

.. image:: https://img.shields.io/badge/License-MIT-yellow.svg
   :target: https://opensource.org/licenses/MIT
   :alt: MIT license


This package provides a convenient python API for accessing various properties
of elements, ions and isotopes in the periodic table of elements.

Moreover it provides an easy to use interface to `pandas <http://pandas.pydata.org/>`_
and convenient visualization functionality through `bokeh <http://bokeh.pydata.org/en/latest/>`_
that enables you to create customized periodic tables displaying various properties.

.. image:: docs/source/img/mendeleev_periodic_series.png
    :width: 800px
    :align: center
    :alt: alternate text


The ``mendeleev`` package also supplies convenient tools for dealing with electronic configurations, calculating
functions of atomic properties, exploring the periodic trends in the periodic tables. If you want
to look at some examples there are a few `tutorials <http://mendeleev.readthedocs.io/en/stable/tutorials.html>`_
available as `jupyter notebooks <http://jupyter.org/>`_.

*******************
Interactive web app
*******************

If you would like to explore the data available in mendeleev_
check out the interactive web app at `mendeleev.herokuapp.com <http://mendeleev.herokuapp.com/>`_
where you can create your own periodic tables and visualize the relations between various properties
of elements.


****
Data
****

A compre


Basic properties
================

- atomic number 
- atomic weight
- block
- cas
- electrons
- electronic configuration
- group
- name
- neutrons
- period
- protons
- series
- symbol

Standardized colors schemes
===========================

- cpk_color 
- jmol_color
- molcas_gv_color

Size related properties
=======================

- atomic radius
- covalent radius (Bragg, Cordero, Pyykko, Slater)
- ionic radius
- metallic radius
- van der Waals radius (Alvarez, Batsanov, Bondi, Dreiding, MM3, RT, Truhlar, UFF)

Electronegativity scales
========================

- Allen
- Allred & Rochow
- Cottrell & Sutton
- Ghosh
- Gordy
- Li & Xue
- Nagle
- Martynov & Batsanov
- Mulliken
- Pauling
- Sanderson

Descriptive properties
======================

- discoverers
- discovery location
- dipole year
- description
- name origin
- sources
- uses

Physical properties
===================

- boiling point
- C<sub>6</sub>
- density
- dipole polarizability
- electron affinity
- evaporation heat
- gas basicity
- ionization energies
- lattice structure
- melting point
- oxidation states
- proton affinity
- specific heat
- thermal conductivity
- nuclear screening constants (Slater & Clementi) 

Isotope properties
==================

- abundance
- g_factor
- half_life
- radioactivity
- mass
- mass number
- spin
- quadrupole_moment


************
Installation
************

The preferred isntalltion method is with ``

The package can be installed using `pip <https://pypi.python.org/pypi/pip>`_

.. code-block:: bash

   pip install mendeleev

You can also install the most recent version from the repository:

.. code-block:: bash

   pip install https://bitbucket.org/lukaszmentel/mendeleev/get/tip.tar.gz

If you use `conda <https://conda.io/docs/intro.html>`_ you can install 
the package from `my anaconda channel <https://anaconda.org/lmmentel/mendeleev>`_ by 

.. code-block:: bash

   conda install -c lmmentel mendeleev=0.4.0


*************
Documentation
*************


Documentation is hosted on `Read the Docs <http://mendeleev.readthedocs.org/en/latest/>`_.

*****
Usage
*****

The simple interface to the data is through the ``element`` method that returns
the ``Element`` objects::

   >>> from mendeleev import element

The ``element`` method accepts unique identifiers: atomic number, atomic
symbol or element's name in english. To retrieve the entries on Silicon by
symbol type

.. code-block:: python

   >>> si = element('Si')
   >>> si.name
   'Silicon'

Similarly to access the data by atomic number or element names type

.. code-block:: python

   >>> al = element(13)
   >>> al.name
   'Aluminium'
   >>> o = element('Oxygen')
   >>> o.atomic_number
   8

Lists of elements
=================

The ``element`` method also accepts list or tuple  of identifiers and then
returns a list of ``Element`` objects

.. code-block:: python

   >>> c, h, o = element(['C', 'Hydrogen', 8])
   >>> c.name, h.name, o.name
   ('Carbon', 'Hydrogen', 'Oxygen')

Composite Attributes
====================

Currently four of the attributes are more complex object than ``str``, ``int``
or ``float``, those are:

* ``oxistates``, returns a list of oxidation states
* ``ionenergies``, returns a dictionary of ionization energies
* ``isotopes``, returns a list of ``Isotope`` objects
* ``ionic_radii`` returns a list of ``IonicRadius`` objects

Oxidation states
----------------

For examples ``oxistates`` returns a list of oxidation states for
a given element

.. code-block:: python

   >>> fe = element('Fe')
   >>> fe.oxistates
   [6, 3, 2, 0, -2]

Ionization energies
-------------------

The ``ionenergies`` returns a dictionary with ionization energies as values and
degrees of ionization as keys.

.. code-block:: python

   >>> fe = element('Fe')
   >>> fe.ionenergies
   {1: 7.9024678,
    2: 16.1992,
    3: 30.651,
    4: 54.91,
    5: 75.0,
    6: 98.985,
    7: 125.0,
    8: 151.06,
    9: 233.6,
    10: 262.1,
    11: 290.9,
    12: 330.81,
    13: 361.0,
    14: 392.2,
    15: 456.2,
    16: 489.312,
    17: 1262.7,
    18: 1357.8,
    19: 1460.0,
    20: 1575.6,
    21: 1687.0,
    22: 1798.43,
    23: 1950.4,
    24: 2045.759,
    25: 8828.1875,
    26: 9277.681}

Isotopes
--------

The ``isotopes`` attribute returns a list of ``Isotope`` objects with the
following attributes per isotope

* ``atomic_number``
* ``mass``
* ``abundance``
* ``mass_number``

.. code-block:: python

   >>> fe = element('Fe')
   >>> for iso in fe.isotopes:
   ...     print(iso)
    26   55.93494  91.75%    56
    26   56.93540   2.12%    57
    26   57.93328   0.28%    58
    26   53.93961   5.85%    54

The columns represent the attributes ``atomic_number``, ``mass``,
``abundance`` and ``mass_number`` respectively.

Ionic radii
-----------

Another composite attribute is ``ionic_radii`` which returns a list of
``IonicRadius`` object with the following attributes

* ``atomic_number``, atomic number of the ion
* ``charge``, charge of the ion
* ``econf``, electronic configuration of the ion
* ``coordination``, coordination type of the ion
* ``spin``, spin state of the ion (*HS* or *LS*)
* ``crystal_radius``
* ``ionic_radius``
* ``origin``, source of the data
* ``most_reliable``, recommended value

.. code-block:: python

   >>> fe = element('Fe')
   >>> for ir in fe.ionic_radii:
   ...     print(ir)
   charge=   2, coordination=IV   , crystal_radius= 0.770, ionic_radius= 0.630
   charge=   2, coordination=IVSQ , crystal_radius= 0.780, ionic_radius= 0.640
   charge=   2, coordination=VI   , crystal_radius= 0.750, ionic_radius= 0.610
   charge=   2, coordination=VI   , crystal_radius= 0.920, ionic_radius= 0.780
   charge=   2, coordination=VIII , crystal_radius= 1.060, ionic_radius= 0.920
   charge=   3, coordination=IV   , crystal_radius= 0.630, ionic_radius= 0.490
   charge=   3, coordination=V    , crystal_radius= 0.720, ionic_radius= 0.580
   charge=   3, coordination=VI   , crystal_radius= 0.690, ionic_radius= 0.550
   charge=   3, coordination=VI   , crystal_radius= 0.785, ionic_radius= 0.645
   charge=   3, coordination=VIII , crystal_radius= 0.920, ionic_radius= 0.780
   charge=   4, coordination=VI   , crystal_radius= 0.725, ionic_radius= 0.585
   charge=   6, coordination=IV   , crystal_radius= 0.390, ionic_radius= 0.250


CLI utility
===========

For those who work in the terminal there is a simple command line interface
(CLI) for printing the information about a given element. The script name is
`element.py` and it accepts either the symbol or name of the element as an
argument and prints the data about it. For example, to print the properties of
silicon type

.. code-block:: bash

   $ element.py Si
      _  _  _  _      _
    _(_)(_)(_)(_)_   (_)
   (_)          (_)_  _
   (_)_  _  _  _  (_)(_)
     (_)(_)(_)(_)_   (_)
    _           (_)  (_)
   (_)_  _  _  _(_)_ (_)
     (_)(_)(_)(_) (_)(_)(_)



   Description
   ===========

     Metalloid element belonging to group 14 of the periodic table. It is
     the second most abundant element in the Earth's crust, making up 25.7%
     of it by weight. Chemically less reactive than carbon. First
     identified by Lavoisier in 1787 and first isolated in 1823 by
     Berzelius.

   Properties
   ==========

   Annotation
   Atomic number                       14
   Atomic radius                      132
   Atomic volume                     12.1
   Block                                p
   Boiling point                     2628
   Covalent radius 2008               111
   Covalent radius 2009               116
   Cpk color                      #daa520
   Density                           2.33
   Dipole polarizability            37.31
   Electron affinity              1.38952
   Electronic configuration  [Ne] 3s2 3p2
   En allen                         11.33
   En pauling                         1.9
   Evaporation heat                   383
   Fusion heat                       50.6
   Gas basicity                     814.1
   Group id                            14
   Heat of formation                  450
   Jmol color                     #f0c8a0
   Lattice constant                  5.43
   Lattice structure                  DIA
   Mass                           28.0855
   Melting point                     1683
   Name                           Silicon
   Period                               3
   Proton affinity                    837
   Series id                            5
   Specific heat                    0.703
   Symbol                              Si
   Thermal conductivity               149
   Vdw radius                         210


************
Contributing
************

Contributions are always welcome! 

`issues <https://bitbucket.org/lukaszmentel/mendeleev/issues>`_

`pull request <https://bitbucket.org/lukaszmentel/mendeleev/pull-requests/>`_ 

contact


*******
License
*******

MIT, see `LICENSE <https://bitbucket.org/lukaszmentel/mendeleev/src/tip/LICENSE>`_


******
Citing
******

If you use mendeleev_ in a scientific publication, please consider citing the software as

|    L. M. Mentel, *mendeleev* - A Python resource for properties of chemical elements, ions and isotopes. , 2014-- . Available at: `https://bitbucket.org/lukaszmentel/mendeleev <https://bitbucket.org/lukaszmentel/mendeleev>`_.



Here's the reference in the `BibLaTeX <https://www.ctan.org/pkg/biblatex?lang=en>`_ format

.. code-block:: latex

   @software{mendeleev2014,
      author = {Mentel, Łukasz},
      title = {{mendeleev} -- A Python resource for properties of chemical elements, ions and isotopes},
      url = {https://bitbucket.org/lukaszmentel/mendeleev},
      version = {0.4.0},
      date = {2014--},
  }

or the older `BibTeX <http://www.bibtex.org/>`_ format

.. code-block:: latex

   @misc{mendeleev2014,
      auhor = {Mentel, Łukasz},
      title = {mendeleev} -- A Python resource for properties of chemical elements, ions and isotopes, ver. 0.4.0},
      howpublished = {\url{https://bitbucket.org/lukaszmentel/mendeleev}},
      year  = {2014--},
   }


*******
Funding
*******

This project is supported by the RCN (The Research Council of Norway) project
number 239193.


.. _conda: https://conda.io/docs/intro.html
.. _mendeleev: http://mendeleev.readthedocs.org

