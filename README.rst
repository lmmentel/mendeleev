#################
mendeleev package
#################

.. image:: https://readthedocs.org/projects/mendeleev/badge/
   :target: https://mendeleev.readthedocs.org
   :alt: Documentation Status

This package provides an API for accessing various properties of elements from
the periodic table of elements.

****
Data
****

Following electronegativity scales are available either as stored values or
computed on request from other properties:

* Allen
* Allred & Rochow
* Cottrell & Sutton
* Ghosh
* Gordy
* Li & Xue
* Nagle
* Martynov & Batsanov
* Mulliken
* Pauling
* Sanderson


The following data are currently available:

+---------------------------+-------+------------------------------------------------------+----------+-------------+
| Name                      | Type  | Comment                                              | Unit     | Data Source |
+===========================+=======+======================================================+==========+=============+
| abundance_crust           | float | Abundance in the Earth's crust                       | mg/kg    | [8]_        |
+---------------------------+-------+------------------------------------------------------+----------+-------------+
| abundance_sea             | float | Abundance in the seas                                | mg/L     | [8]_        |
+---------------------------+-------+------------------------------------------------------+----------+-------------+
| annotation                | str   | Annotations regarding the data                       |          |             |
+---------------------------+-------+------------------------------------------------------+----------+-------------+
| atomic_number             | int   | Atomic number                                        |          |             |
+---------------------------+-------+------------------------------------------------------+----------+-------------+
| atomic_radius             | float | Atomic radius                                        | pm       |             |
+---------------------------+-------+------------------------------------------------------+----------+-------------+
| atomic_volume             | float | Atomic volume                                        | cm3/mol  |             |
+---------------------------+-------+------------------------------------------------------+----------+-------------+
| atomic_weight             | float | Atomic weight                                        |          | [36]_, [37]_|
+---------------------------+-------+------------------------------------------------------+----------+-------------+
| atomic_weight_uncertainty | float | Atomic volume                                        |          | [36]_, [37]_|
+---------------------------+-------+------------------------------------------------------+----------+-------------+
| block                     | int   | Block in periodic table                              |          |             |
+---------------------------+-------+------------------------------------------------------+----------+-------------+
| boiling_point             | float | Boiling temperature                                  | K        |             |
+---------------------------+-------+------------------------------------------------------+----------+-------------+
| c6                        | float | C_6 dispersion coefficient in a.u.                   | a.u.     | [1]_, [2]_  |
+---------------------------+-------+------------------------------------------------------+----------+-------------+
| c6_gb                     | float | C_6 dispersion coefficient in a.u. (Gould & Bučko)   | a.u.     | [35]_       |
+---------------------------+-------+------------------------------------------------------+----------+-------------+
| covalent_radius_bragg     | float | Covalent radius by Bragg                             | pm       | [3]_        |
+---------------------------+-------+------------------------------------------------------+----------+-------------+
| covalent_radius_cordero   | float | Covalent radius by Cerdero et al.                    | pm       | [4]_        |
+---------------------------+-------+------------------------------------------------------+----------+-------------+
| covalent_radius_pyykko    | float | Covalent radius by Pyykko et al.                     | pm       | [5]_        |
+---------------------------+-------+------------------------------------------------------+----------+-------------+
| covalent_radius_slater    | float | Covalent radius by Slater                            | pm       | [6]_        |
+---------------------------+-------+------------------------------------------------------+----------+-------------+
| cpk_color                 | str   | Element color in CPK convention                      | HEX      | [24]_       |
+---------------------------+-------+------------------------------------------------------+----------+-------------+
| density                   | float | Density at 295K                                      | g/cm3    |             |
+---------------------------+-------+------------------------------------------------------+----------+-------------+
| description               | str   | Short description of the element                     |          |             |
+---------------------------+-------+------------------------------------------------------+----------+-------------+
| dipole_polarizability     | float | Dipole polarizability                                | a.u.     | [7]_        |
+---------------------------+-------+------------------------------------------------------+----------+-------------+
| electron_affinity         | float | Electron affinity                                    | eV       | [8]_, [9]_  |
+---------------------------+-------+------------------------------------------------------+----------+-------------+
| electrons                 | int   | Number of electrons                                  |          |             |
+---------------------------+-------+------------------------------------------------------+----------+-------------+
| en_allen                  | float | Allen's scale of electronegativity                   | eV       | [10]_, [11]_|
+---------------------------+-------+------------------------------------------------------+----------+-------------+
| en_ghosh                  | float | Ghosh's scale of electronegativity                   |          | [32]_       |
+---------------------------+-------+------------------------------------------------------+----------+-------------+
| en_mulliken               | float | Mulliken's scale of electronegativity                | eV       | [12]_       |
+---------------------------+-------+------------------------------------------------------+----------+-------------+
| en_pauling                | float | Pauling's scale of electronegativity                 |          | [8]_        |
+---------------------------+-------+------------------------------------------------------+----------+-------------+
| econf                     | str   | Ground state electron configuration                  |          |             |
+---------------------------+-------+------------------------------------------------------+----------+-------------+
| evaporation_heat          | float | Evaporation heat                                     | kJ/mol   |             |
+---------------------------+-------+------------------------------------------------------+----------+-------------+
| fusion_heat               | float | Fusion heat                                          | kJ/mol   |             |
+---------------------------+-------+------------------------------------------------------+----------+-------------+
| gas_basicity              | float | Gas basicity                                         | kJ/mol   | [8]_        |
+---------------------------+-------+------------------------------------------------------+----------+-------------+
| group                     | int   | Group in periodic table                              |          |             |
+---------------------------+-------+------------------------------------------------------+----------+-------------+
| heat_of_formation         | float | Heat of formation                                    | kJ/mol   | [8]_        |
+---------------------------+-------+------------------------------------------------------+----------+-------------+
| ionenergy                 | tuple | Ionization energies                                  | eV       | [13]_       |
+---------------------------+-------+------------------------------------------------------+----------+-------------+
| ionic_radii               | list  | Ionic and crystal radii in pm                        | pm       | [14]_       |
+---------------------------+-------+------------------------------------------------------+----------+-------------+
| is_monoisotopic           | bool  | Is the element monoisotopic                          |          |             |
+---------------------------+-------+------------------------------------------------------+----------+-------------+
| is_radioactive            | bool  | Is the element radioactive                           |          |             |
+---------------------------+-------+------------------------------------------------------+----------+-------------+
| isotopes                  | list  | Isotopes                                             |          |             |
+---------------------------+-------+------------------------------------------------------+----------+-------------+
| jmol_color                | str   | Element color in Jmol convention                     | HEX      | [25]_       |
+---------------------------+-------+------------------------------------------------------+----------+-------------+
| lattice_constant          | float | Lattice constant                                     | Angstrom |             |
+---------------------------+-------+------------------------------------------------------+----------+-------------+
| lattice_structure         | str   | Lattice structure code                               |          |             |
+---------------------------+-------+------------------------------------------------------+----------+-------------+
| mass_number               | int   | Mass number (most abundant isotope)                  |          |             |
+---------------------------+-------+------------------------------------------------------+----------+-------------+
| melting_point             | float | Melting temperature                                  | K        |             |
+---------------------------+-------+------------------------------------------------------+----------+-------------+
| molcas_gv_color           | str   | Element color in MOCAS GV convention                 | HEX      | [26]_       |
+---------------------------+-------+------------------------------------------------------+----------+-------------+
| name                      | str   | Name in English                                      |          |             |
+---------------------------+-------+------------------------------------------------------+----------+-------------+
| neutrons                  | int   | Number of neutrons (most abundant isotope)           |          |             |
+---------------------------+-------+------------------------------------------------------+----------+-------------+
| oxistates                 | list  | Oxidation states                                     |          |             |
+---------------------------+-------+------------------------------------------------------+----------+-------------+
| period                    | int   | Period in periodic table                             |          |             |
+---------------------------+-------+------------------------------------------------------+----------+-------------+
| proton_affinity           | float | Proton affinity                                      | kJ/mol   | [8]_        |
+---------------------------+-------+------------------------------------------------------+----------+-------------+
| protons                   | int   | Number of protons                                    |          |             |
+---------------------------+-------+------------------------------------------------------+----------+-------------+
| sconst                    | float | Nuclear charge screening constants                   |          | [15]_, [16]_|
+---------------------------+-------+------------------------------------------------------+----------+-------------+
| series                    | int   | Index to chemical series                             |          |             |
+---------------------------+-------+------------------------------------------------------+----------+-------------+
| specific_heat             | float | Specific heat @ 20 C                                 | J/(g mol)|             |
+---------------------------+-------+------------------------------------------------------+----------+-------------+
| symbol                    | str   | Chemical symbol                                      |          |             |
+---------------------------+-------+------------------------------------------------------+----------+-------------+
| thermal_conductivity      | float | Thermal conductivity @25 C                           | W/(m K)  |             |
+---------------------------+-------+------------------------------------------------------+----------+-------------+
| vdw_radius                | float | Van der Waals radius                                 | pm       | [8]_        |
+---------------------------+-------+------------------------------------------------------+----------+-------------+
| vdw_radius_alvarez        | float | Van der Waals radius according to Alvarez            | pm       | [33]_, [34]_|
+---------------------------+-------+------------------------------------------------------+----------+-------------+
| vdw_radius_batsanov       | float | Van der Waals radius according to Batsanov           | pm       | [17]_       |
+---------------------------+-------+------------------------------------------------------+----------+-------------+
| vdw_radius_bondi          | float | Van der Waals radius according to Bondi              | pm       | [18]_       |
+---------------------------+-------+------------------------------------------------------+----------+-------------+
| vdw_radius_dreiding       | float | Van der Waals radius from the DREIDING FF            | pm       | [19]_       |
+---------------------------+-------+------------------------------------------------------+----------+-------------+
| vdw_radius_mm3            | float | Van der Waals radius from the MM3 FF                 | pm       | [20]_       |
+---------------------------+-------+------------------------------------------------------+----------+-------------+
| vdw_radius_rt             | float | Van der Waals radius according to Rowland and Taylor | pm       | [21]_       |
+---------------------------+-------+------------------------------------------------------+----------+-------------+
| vdw_radius_truhlar        | float | Van der Waals radius according to Truhlar            | pm       | [22]_       |
+---------------------------+-------+------------------------------------------------------+----------+-------------+
| vdw_radius_uff            | float | Van der Waals radius from the UFF                    | pm       | [23]_       |
+---------------------------+-------+------------------------------------------------------+----------+-------------+


References
----------

.. [1] Chu, X., & Dalgarno, A. (2004). Linear response time-dependent density
   functional theory for van der Waals coefficients. The Journal of Chemical
   Physics, 121(9), 4083. `doi:10.1063/1.1779576 <http://dx.doi.org/10.1063/1.1779576>`_
.. [2] Tang, K. T., Norbeck, J. M., & Certain, P. R. (1976). Upper and lower bounds of
   two- and three-body dipole, quadrupole, and octupole van der Waals coefficients
   for hydrogen, noble gas, and alkali atom interactions. The Journal of Chemical
   Physics, 64(7), 3063. `doi:10.1063/1.432569 <http://dx.doi.org/10.1063/1.432569>`_
.. [3] Bragg, W. L. (1920). The arrangement of atoms in crystals. Philosophical
   Magazine, 40(236), 169-189.
   `doi:10.1080/14786440808636111 <http://dx.doi.org/10.1080/14786440808636111>`_
.. [4] Cordero, B., Gomez, V., Platero-Prats, A. E., Reves, M., Echeverria, J.,
   Cremades, E., ... Alvarez, S. (2008). Covalent radii revisited. Dalton
   Transactions, (21), 2832. `doi:10.1039/b801115j <http://www.dx.doi.org/10.1039/b801115j>`_
.. [5] Pyykko, P., & Atsumi, M. (2009). Molecular Single-Bond Covalent Radii
   for Elements 1-118. Chemistry - A European Journal, 15(1), 186-197.
   `doi:10.1002/chem.200800987 <http://www.dx.doi.org/10.1002/chem.200800987>`_
.. [6] Slater, J. C. (1964). Atomic Radii in Crystals. The Journal of Chemical
   Physics, 41(10), 3199. `doi:10.1063/1.1725697 <http://dx.doi.org/10.1063/1.1725697>`_
.. [7] P. Schwerdtfeger "Table of experimental and calculated static dipole
   polarizabilities for the electronic ground states of the neutral elements
   (in atomic units)", February 11, 2014 `source <http://ctcp.massey.ac.nz/Tablepol2014.pdf>`_
.. [8] W. M. Haynes, Handbook of Chemistry and Physics 95th Edition, CRC Press,
   New York, 2014, ISBN-10: 1482208679, ISBN-13: 978-1482208672.
.. [9] Andersen, T. (2004). Atomic negative ions: structure, dynamics and collisions.
   Physics Reports, 394(4-5), 157-313.
   `doi:10.1016/j.physrep.2004.01.001 <http://www.dx.doi.org/10.1016/j.physrep.2004.01.001>`_
.. [10] Mann, J. B., Meek, T. L., & Allen, L. C. (2000). Configuration Energies of the
   Main Group Elements. Journal of the American Chemical Society, 122(12),
   2780-2783. `doi:10.1021/ja992866e <http://dx.doi.org/10.1021/ja992866e>`_
.. [11] Mann, J. B., Meek, T. L., Knight, E. T., Capitani, J. F., & Allen, L. C.
   (2000). Configuration Energies of the d-Block Elements. Journal of the American
   Chemical Society, 122(21), 5132-5137.
   `doi:10.1021/ja9928677 <http://dx.doi.org/10.1021/ja9928677>`_
.. [12] Mulliken, R. S. (1934). A New Electroaffinity Scale; Together with Data on
   Valence States and on Valence Ionization Potentials and Electron Affinities.
   The Journal of Chemical Physics, 2(11), 782.
   `doi:10.1063/1.1749394 <http://dx.doi.org/10.1063/1.1749394>`_
.. [13] `NIST Atomic Database <http://physics.nist.gov/cgi-bin/ASD/ie.pl>`_
   accessed on April 13, 2015
.. [14] Shannon, R. D. (1976). Revised effective ionic radii and systematic
   studies of interatomic distances in halides and chalcogenides.
   Acta Crystallographica Section A.
   `doi:10.1107/S0567739476001551 <http://www.dx.doi.org/10.1107/S0567739476001551>`_
.. [15] Clementi, E., & Raimondi, D. L. (1963). Atomic Screening Constants from
   SCF Functions. The Journal of Chemical Physics, 38(11), 2686.
   `doi:10.1063/1.1733573 <http://www.dx.doi.org/10.1063/1.1733573>`_
.. [16] Clementi, E. (1967). Atomic Screening Constants from SCF Functions. II.
   Atoms with 37 to 86 Electrons. The Journal of Chemical Physics, 47(4), 1300.
   `doi:10.1063/1.1712084 <http://www.dx.doi.org/10.1063/1.1712084>`_
.. [17] Batsanov, S. S. (2001). Van der Waals radii of elements. Inorganic Materials,
   37(9), 871-885.
   `doi:10.1023/A:1011625728803 <http://www.dx.doi.org/10.1023/A:1011625728803>`_
.. [18] Bondi, A. (1964). van der Waals Volumes and Radii. The Journal of Physical
   Chemistry, 68(3), 441-451.
   `doi:10.1021/j100785a001 <http://www.dx.doi.org/10.1021/j100785a001>`_
.. [19] Mayo, S. L., Olafson, B. D., & Goddard, W. A. (1990). DREIDING: a generic force
   field for molecular simulations. The Journal of Physical Chemistry, 94(26), 8897-8909.
   `doi:10.1021/j100389a010 <http://www.dx.doi.org/10.1021/j100389a010>`_
.. [20] Allinger, N. L., Zhou, X., & Bergsma, J. (1994). Molecular mechanics
   parameters. Journal of Molecular Structure: THEOCHEM, 312(1), 69-83.
   `doi:10.1016/S0166-1280(09)80008-0 <http://www.dx.doi.org/10.1016/S0166-1280(09)80008-0>`_
.. [21] Rowland, R. S., & Taylor, R. (1996). Intermolecular Nonbonded Contact Distances
   in Organic Crystal Structures: Comparison with Distances Expected from van der
   Waals Radii. The Journal of Physical Chemistry, 100(18), 7384-7391.
   `doi:10.1021/jp953141+ <http://www.dx.doi.org/10.1021/jp953141+>`_
.. [22] Mantina, M., Chamberlin, A. C., Valero, R., Cramer, C. J., & Truhlar, D. G.
   (2009). Consistent van der Waals Radii for the Whole Main Group. The Journal of
   Physical Chemistry A, 113(19), 5806-5812.
   `doi:10.1021/jp8111556 <http://dx.doi.org/10.1021/jp8111556>`_
.. [23] Rappe, A. K., Casewit, C. J., Colwell, K. S., Goddard, W. A., & Skiff, W. M.
   (1992). UFF, a full periodic table force field for molecular mechanics and
   molecular dynamics simulations. Journal of the American Chemical Society,
   114(25), 10024-10035.
   `doi:10.1021/ja00051a040 <http://www.dx.doi.org/10.1021/ja00051a040>`_
.. [24] `CPK colors <https://en.wikipedia.org/wiki/CPK_coloring>`_
.. [25] `Jmol colors <http://jmol.sourceforge.net/jscolors/#color_U>`_
.. [26] `MOLCAS GV colors <http://www.molcas.org/GV/>`_
.. [27] R. T. Sanderson, Chemical Bonds and Bond Energy, Academic Press, New York,
   1976, ISBN: 0-12-618060-1
.. [28] Allen, L. C., & Huheey, J. E. (1980). The definition of electronegativity and
  the chemistry of the noble gases. Journal of Inorganic and Nuclear Chemistry,
  42(10), 1523-1524. doi:10.1016/0022-1902(80)80132-1
.. [29] Luo, Z., Chen, X., Li, J., & Ning, C. (2016). Precision measurement of
   the electron affinity of niobium. Physical Review A, 93(2), 020501.
   `doi:10.1103/PhysRevA.93.020501 <http://dx.doi.org/10.1103/PhysRevA.93.020501>`_
.. [30] Chen, X., & Ning, C. (2016). Accurate electron affinity of Co and
   fine-structure splittings of Co$^-$ via slow-electron velocity-map imaging.
   Physical Review A, 93(5), 052508. doi:10.1103/PhysRevA.93.052508
.. [31] Chen, X., & Ning, C. (2016). Accurate electron affinity of Pb and
   isotope shifts of binding energies of Pb−. The Journal of Chemical Physics,
   145(8), 84303. `doi:10.1063/1.4961654 <http://doi.org/10.1063/1.4961654>`_
.. [32] Ghosh, D. C. (2005). A New Scale of Electronegativity Based on Absolute Radii of Atoms.
   Journal of Theoretical and Computational Chemistry, 4(1), 21–33.
   `doi:10.1142/S0219633605001556 <http://doi.org/10.1142/S0219633605001556>`_
.. [33] Alvarez, S. (2013). A cartography of the van der Waals territories.
   Dalton Transactions, 42(24), 8617.
   `doi:10.1039/c3dt50599e <http://doi.org/10.1039/c3dt50599e>`_
.. [34] Vogt, J., & Alvarez, S. (2014). van der Waals Radii of Noble Gases.
   Inorganic Chemistry, 53(17), 9260–9266.
   `doi:10.1021/ic501364h <http://doi.org/10.1021/ic501364h>`_
.. [35] Gould, T., & Bučko, T. (2016). C 6 Coefficients and Dipole Polarizabilities
   for All Atoms and Many Ions in Rows 1–6 of the Periodic Table. Journal of
   Chemical Theory and Computation, 12(8), 3603–3613.
   `doi:10.1021/acs.jctc.6b00361 <http://doi.org/10.1021/acs.jctc.6b00361>`_
.. [36] Meija, J., Coplen, T. B., Berglund, M., Brand, W. A., De Bièvre, P.,
   Gröning, M., Holden, N., Irrgeher, J., Loss, R., Walczyk, T., Prohaska, T.
   (2016). Atomic weights of the elements 2013 (IUPAC Technical Report).
   Pure and Applied Chemistry, 88(3), 265–291.
   `doi:10.1515/pac-2015-0305 <http://doi.org/10.1515/pac-2015-0305>`_
.. [37] Standard Atomic Weights, IUPAC-CIAAW, http://www.ciaaw.org/atomic-weights.htm
   accessed Jan. 1st 2017.
   

************
Installation
************

The package can be installed using `pip <https://pypi.python.org/pypi/pip>`_

.. code-block:: bash

   pip install mendeleev

You can also install the most recent version from the repository:

.. code-block:: bash

   pip install https://bitbucket.org/lukaszmentel/mendeleev/get/tip.tar.gz

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

***********
CLI utility
***********

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


*************
Documentation
*************


Documentation can be found `here <http://mendeleev.readthedocs.org/en/latest/>`_.

******
Citing
******

If you use *mendeleev* in a scientific publication, please cite the software as

|    L. M. Mentel, *mendeleev*, 2014. Available at: `https://bitbucket.org/lukaszmentel/mendeleev <https://bitbucket.org/lukaszmentel/mendeleev>`_.


*******
Funding
*******

This project is supported by the RCN (The Research Council of Norway) project
number 239193.

