Tutorial
========

Basic interactive usage
-----------------------

The simple interface to the data is through the :py:func:`element <mendeleev.mendeleev.element>`
method that returns the :py:class:`Element <mendeleev.tables.Element>` objects::

   >>> from mendeleev import element

The :py:func:`element <mendeleev.mendeleev.element>` method accepts unique
identifiers: atomic number, atomic symbol or element's name in English. To
retrieve the entries on Silicon by symbol type

.. code-block:: python

   >>> si = element('Si')
   >>> si
   Element(
       annotation=u'',
       atomic_number=14,
       atomic_radius=132.0,
       atomic_volume=12.1,
       block=u'p',
       boiling_point=2628.0,
       covalent_radius_2008=111.00000000000001,
       covalent_radius_2009=115.99999999999999,
       density=2.33,
       description=u"Metalloid element belonging to group 14 of the periodic table. It is the second most abundant element in the Earth's crust, making up 25.7% of it by weight. Chemically less reactive than carbon. First identified by Lavoisier in 1787 and first isolated in 1823 by Berzelius.",
       dipole_polarizability=37.31,
       ec=1s2 2s2 2p6 3s2 3p2,
       econf=u'[Ne] 3s2 3p2',
       electron_affinity=1.3895211,
       en_allen=11.33,
       en_pauling=1.9,
       evaporation_heat=383.0,
       fusion_heat=50.6,
       group_id=14,
       lattice_constant=5.43,
       lattice_structure=u'DIA',
       mass=28.0855,
       melting_point=u'1683',
       name=u'Silicon',
       period=3,
       specific_heat=0.703,
       symbol=u'Si',
       thermal_conductivity=149.0,
       vdw_radius=210.0,
   )

Similarly to access the data by atomic number or element names type

.. code-block:: python

   >>> al = element(13)
   >>> al.name
   'Aluminium'
   >>> o = element('Oxygen')
   >>> o.atomic_number
   8

Lists of elements
+++++++++++++++++

The :py:func:`element <mendeleev.mendeleev.element>` method also accepts list
or tuple  of identifiers and then returns a list of :py:class:`Element <mendeleev.tables.Element>`
objects

.. code-block:: python

   >>> c, h, o = element(['C', 'Hydrogen', 8])
   >>> c.name, h.name, o.name
   ('Carbon', 'Hydrogen', 'Oxygen')

Composite Attributes
++++++++++++++++++++

Currently four of the attributes are more complex object than :class:`str`,
:class:`int` or :class:`float`, those are:

* ``oxistates``, returns a list of oxidation states
* ``ionenergies``, returns a dictionary of ionization energies
* ``isotopes``, returns a list of :py:class:`Isotope <mendeleev.tables.Isotope>` objects
* ``ionic_radii`` returns a list of :py:class:`IonicRadius <mendeleev.tables.IonicRadius>` objects

Oxidation states
^^^^^^^^^^^^^^^^

For examples :py:attr:`oxistates <mendeleev.tables.Element.oxistates>` returns
a list of oxidation states for a given element

.. code-block:: python

   >>> fe = element('Fe')
   >>> fe.oxistates
   [6, 3, 2, 0, -2]

Ionization energies
^^^^^^^^^^^^^^^^^^^

The :py:attr:`ionenergies <mendeleev.tables.Element.ionenergies>` returns a
dictionary with ionization energies as values and degrees of ionization as keys

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
^^^^^^^^

The :py:attr:`isotopes <mendeleev.tables.Element.isotopes>` attribute returns a
list of :py:class:`Isotope <mendeleev.tables.Isotope>` objects with the
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
^^^^^^^^^^^

Another composite attribute is ``ionic_radii`` which returns a list of
:py:class:`IonicRadius <mendeleev.tables.IonicRadius>` object with the following
attributes

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
-----------

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


Jupyter notebooks
-----------------

A series of short tutorials is available as `Jupyter <https://jupyter.org/>`_
(former `IPython notebook <http://ipython.org/notebook.html>`_) notebooks that
present the main functionality and provide real-life examples

* `Retrieving tables into DataFrames <http://nbviewer.ipython.org/url/bitbucket.org/lukaszmentel/mendeleev/raw/tip/docs/ipynb/tables.ipynb>`_
* `Plotting periodic tables <http://nbviewer.ipython.org/url/bitbucket.org/lukaszmentel/mendeleev/raw/tip/docs/ipynb/plotting_tutorial.ipynb>`_
