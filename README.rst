
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

.. image:: https://anaconda.org/conda-forge/github3.py/badges/installer/conda.svg
    :target: https://anaconda.org/lmmentel/mendeleev

.. image:: https://travis-ci.org/lmmentel/mendeleev.svg?branch=master
    :target: https://travis-ci.org/lmmentel/mendeleev

.. image:: https://img.shields.io/lgtm/alerts/g/lmmentel/mendeleev.svg?logo=lgtm&logoWidth=18
    :target: https://lgtm.com/projects/g/lmmentel/mendeleev/alerts/
    :alt: Total alerts

.. image:: https://img.shields.io/lgtm/grade/python/g/lmmentel/mendeleev.svg?logo=lgtm&logoWidth=18
    :target: https://lgtm.com/projects/g/lmmentel/mendeleev/context:python
    :alt: Language grade: Python

.. image:: https://pepy.tech/badge/mendeleev
    :target: https://pepy.tech/project/mendeleev


#########################################################
Important! This package has been migrated from bitbucket.
#########################################################

The bitbucket repo is no longer being maintaned and development will continue at github.

########
Overview
########

This package provides a convenient python API for accessing various properties
of elements, ions and isotopes in the periodic table of elements.

Moreover it provides an easy to use interface to `pandas <http://pandas.pydata.org/>`_
and convenient visualization functionality through `bokeh <http://bokeh.pydata.org/en/latest/>`_
that enables you to create customized periodic tables displaying various properties.

.. image:: docs/source/_static/img/mendeleev_periodic_series.png
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


.. image:: docs/source/_static/img/mendeleevapp_periodic.png
    :width: 800px
    :align: center
    :alt: Periodic table view

.. image:: docs/source/_static/img/mendeleevapp_correlations.png
    :width: 800px
    :align: center
    :alt: Correlations view

****
Data
****

A comprehensive list of the available data together with appropriate references are available in the
`documentation <mendeleev_>`_. Here the most important entries are listed:


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

The preferred installation method is with conda_ and you can install
the package from `my anaconda channel <https://anaconda.org/lmmentel/mendeleev>`_ by

.. code-block:: bash

   conda install -c lmmentel mendeleev=0.6.1

The package can also be installed using `pip <https://pypi.python.org/pypi/pip>`_

.. code-block:: bash

   pip install mendeleev

You can also install the most recent version from the repository:

.. code-block:: bash

   pip install git+https://github.com/lmmentel/mendeleev.git



*************
Documentation
*************


Documentation is hosted on `Read the Docs <http://mendeleev.readthedocs.org/en/latest/>`_.

*****
Usage
*****

The simplest way of accessing the element data is by importing elements directly from
the `mendeleev` package by their symbols. For example consider iron (Fe)::

   >>> from mendeleev import Fe
   >>> Fe.name
   'Iron'
   >>> Fe.atomic_number
   26
   >>> Fe.thermal_conductivity
   80.4


Another, more flexible way is through the ``element`` method that returns
the ``Element`` object::

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

Tables and the database
=======================

mendeleev_ offers also methods for accessing whole tables of data, e.g. table
with the data on all isotopes and methods for interacting directly with the
database engine, for more details see the `API documentation <https://mendeleev.readthedocs.io/en/stable/code.html#accessing-data>`_
and `this tutorial <https://mendeleev.readthedocs.io/en/stable/notebooks/02_tables.html>`_.

CLI utility
===========

For those who work in the terminal there is a simple command line interface
(CLI) for printing the information about a given element. The script name is
`element.py` and it accepts either the symbol or name of the element or it's
atomic number as an argument and prints the data about it. For example, to
print the properties of silicon type

.. code-block:: bash

    $ element.py Si
                                _  _  _  _      _
                              _(_)(_)(_)(_)_   (_)
                             (_)          (_)_  _
                             (_)_  _  _  _  (_)(_)
                               (_)(_)(_)(_)_   (_)
                              _           (_)  (_)
                             (_)_  _  _  _(_)_ (_) _
                               (_)(_)(_)(_) (_)(_)(_)



    Description
    ===========

      Metalloid element belonging to group 14 of the periodic table. It is
      the second most abundant element in the Earth's crust, making up 25.7%
      of it by weight. Chemically less reactive than carbon. First
      identified by Lavoisier in 1787 and first isolated in 1823 by
      Berzelius.

    Sources
    =======

      Makes up major portion of clay, granite, quartz (SiO2), and sand.
      Commercial production depends on a reaction between sand (SiO2) and
      carbon at a temperature of around 2200 °C.

    Uses
    ====

      Used in glass as silicon dioxide (SiO2). Silicon carbide (SiC) is one
      of the hardest substances known and used in polishing. Also the
      crystalline form is used in semiconductors.

    Properties
    ==========

    Abundance crust                                         282000
    Abundance sea                                              2.2
    Annotation
    Atomic number                                               14
    Atomic radius                                              132
    Atomic radius rahm                                         232
    Atomic volume                                             12.1
    Atomic weight                                           28.085
    Atomic weight uncertainty                                  NaN
    Block                                                        p
    Boiling point                                             2628
    C6                                                         305
    C6 gb                                                      308
    Cas                                                  7440-21-3
    Covalent radius bragg                                      117
    Covalent radius cordero                                    111
    Covalent radius pyykko                                     116
    Covalent radius pyykko double                              107
    Covalent radius pyykko triple                              102
    Covalent radius slater                                     110
    Cpk color                                              #daa520
    Density                                                   2.33
    Dipole polarizability                                    37.31
    Discoverers                                     Jöns Berzelius
    Discovery location                                      Sweden
    Discovery year                                            1824
    Electron affinity                                      1.38952
    Electronic configuration                          [Ne] 3s2 3p2
    En allen                                                 11.33
    En ghosh                                              0.178503
    En pauling                                                 1.9
    Evaporation heat                                           383
    Fusion heat                                               50.6
    Gas basicity                                             814.1
    Geochemical class                                        major
    Goldschmidt class                                    litophile
    Group id                                                    14
    Heat of formation                                          450
    Is monoisotopic                                           None
    Is radioactive                                           False
    Jmol color                                             #f0c8a0
    Lattice constant                                          5.43
    Lattice structure                                          DIA
    Melting point                                             1683
    Metallic radius                                            117
    Metallic radius c12                                        138
    Molcas gv color                                        #f0c8a0
    Name                                                   Silicon
    Name origin                    Latin: silex, silicus, (flint).
    Period                                                       3
    Proton affinity                                            837
    Series id                                                    5
    Specific heat                                            0.703
    Symbol                                                      Si
    Thermal conductivity                                       149
    Vdw radius                                                 210
    Vdw radius alvarez                                         219
    Vdw radius batsanov                                        210
    Vdw radius bondi                                           210
    Vdw radius dreiding                                        427
    Vdw radius mm3                                             229
    Vdw radius rt                                              NaN
    Vdw radius truhlar                                         NaN
    Vdw radius uff                                           429.5



************
Contributing
************

All contributions are welcome!

Issues_
=======

Feel free to submit issues_ regarding:

- data updates and recommendations
- enhancement requests and new useful features
- code bugs
- data or citation inconsistencies or errors

`Pull requests <pull request_>`_
================================

- before stating to work on your pull request please `submit an issue <issues_>`_ first
- fork the repo on `github <source_>`_
- clone the project to your own machine
- commit changes to your own branch
- push your work back up to your fork
- submit a `pull request`_ so that your changes can be reviewed


*******
License
*******

MIT, see `LICENSE <https://github.com/lmmentel/mendeleev/blob/master/LICENSE>`_


******
Citing
******

If you use mendeleev_ in a scientific publication, please consider citing the software as

|    L. M. Mentel, *mendeleev* - A Python resource for properties of chemical elements, ions and isotopes. , 2014-- . Available at: `https://github.com/lmmentel/mendeleev <https://github.com/lmmentel/mendeleev>`_.



Here's the reference in the `BibLaTeX <https://www.ctan.org/pkg/biblatex?lang=en>`_ format

.. code-block:: latex

   @software{mendeleev2014,
      author = {Mentel, Łukasz},
      title = {{mendeleev} -- A Python resource for properties of chemical elements, ions and isotopes},
      url = {https://github.com/lmmentel/mendeleev},
      version = {0.6.1},
      date = {2014--},
  }

or the older `BibTeX <http://www.bibtex.org/>`_ format

.. code-block:: latex

   @misc{mendeleev2014,
      auhor = {Mentel, Łukasz},
      title = {mendeleev} -- A Python resource for properties of chemical elements, ions and isotopes, ver. 0.6.1},
      howpublished = {\url{https://github.com/lmmentel/mendeleev}},
      year  = {2014--},
   }


*******
Funding
*******

This project is supported by the RCN (The Research Council of Norway) project
number 239193.


.. _conda: https://conda.io/docs/intro.html
.. _issues: https://github.com/lmmentel/mendeleev/issues
.. _mendeleev: http://mendeleev.readthedocs.org
.. _pull request: https://github.com/lmmentel/mendeleev/pulls
.. _source: https://github.com/lmmentel/mendeleev
