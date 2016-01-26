Data
====

Available properties of the elements
------------------------------------

The following data is currently available:

+-------------------------+-------+---------------------------------------------+----------+-------------+
| Name                    | Type  | Comment                                     | Unit     | Data Source |
+=========================+=======+=============================================+==========+=============+
| annotation              | str   | Annotations regarding the data              |          |             |
+-------------------------+-------+---------------------------------------------+----------+-------------+
| atomic_number           | int   | Atomic number                               |          |             |
+-------------------------+-------+---------------------------------------------+----------+-------------+
| atomic_radius           | float | Atomic radius                               | pm       |             |
+-------------------------+-------+---------------------------------------------+----------+-------------+
| atomic_volume           | float | Atomic volume                               | cm3/mol  |             |
+-------------------------+-------+---------------------------------------------+----------+-------------+
| block                   | int   | Block in periodic table                     |          |             |
+-------------------------+-------+---------------------------------------------+----------+-------------+
| boiling_point           | float | Boiling temperature                         | K        |             |
+-------------------------+-------+---------------------------------------------+----------+-------------+
| c6                      | float | C_6 dispersion coefficient in a.u.          | a.u.     | [1]_, [2]_  |
+-------------------------+-------+---------------------------------------------+----------+-------------+
| covalent_radius_bragg   | float | Covalent radius by Bragg                    | pm       | [3]_        |
+-------------------------+-------+---------------------------------------------+----------+-------------+
| covalent_radius_cordero | float | Covalent radius by Cerdero et al.           | pm       | [4]_        |
+-------------------------+-------+---------------------------------------------+----------+-------------+
| covalent_radius_pyykko  | float | Covalent radius by Pyykko et al.            | pm       | [5]_        |
+-------------------------+-------+---------------------------------------------+----------+-------------+
| covalent_radius_slater  | float | Covalent radius by Slater                   | pm [6]_  |             |
+-------------------------+-------+---------------------------------------------+----------+-------------+
| density                 | float | Density at 295K                             | g/cm3    |             |
+-------------------------+-------+---------------------------------------------+----------+-------------+
| description             | str   | Short description of the element            |          |             |
+-------------------------+-------+---------------------------------------------+----------+-------------+
| dipole_polarizability   | float | Dipole polarizability                       | a.u.     | [7]_        |
+-------------------------+-------+---------------------------------------------+----------+-------------+
| electron_affinity       | float | Electron affinity                           | eV       | [8]_, [9]_  |
+-------------------------+-------+---------------------------------------------+----------+-------------+
| electrons               | int   | Number of electrons                         |          |             |
+-------------------------+-------+---------------------------------------------+----------+-------------+
| en_allen                | float | Allen's scale of electronegativity          | eV       | [10]_, [11]_|
+-------------------------+-------+---------------------------------------------+----------+-------------+
| en_mulliken             | float | Mulliken's scale of electronegativity       | eV       | [12]_       |
+-------------------------+-------+---------------------------------------------+----------+-------------+
| en_pauling              | float | Pauling's scale of electronegativity        |          | [8]_        |
+-------------------------+-------+---------------------------------------------+----------+-------------+
| econf                   | str   | Ground state electron configuration         |          |             |
+-------------------------+-------+---------------------------------------------+----------+-------------+
| evaporation_heat        | float | Evaporation heat                            | kJ/mol   |             |
+-------------------------+-------+---------------------------------------------+----------+-------------+
| fusion_heat             | float | Fusion heat                                 | kJ/mol   |             |
+-------------------------+-------+---------------------------------------------+----------+-------------+
| gas_basicity            | float | Gas basicity                                | kJ/mol   | [8]_        |
+-------------------------+-------+---------------------------------------------+----------+-------------+
| group                   | int   | Group in periodic table                     |          |             |
+-------------------------+-------+---------------------------------------------+----------+-------------+
| heat_of_formation       | float | Heat of formation                           | kJ/mol   | [8]_        |
+-------------------------+-------+---------------------------------------------+----------+-------------+
| ionenergy               | tuple | Ionization energies                         | eV       | [13]_       |
+-------------------------+-------+---------------------------------------------+----------+-------------+
| ionic_radii             | list  | Ionic and crystal radii in pm               | pm       | [14]_       |
+-------------------------+-------+---------------------------------------------+----------+-------------+
| isotopes                | list  | Isotopes                                    |          |             |
+-------------------------+-------+---------------------------------------------+----------+-------------+
| lattice_constant        | float | Lattice constant                            | Angstrom |             |
+-------------------------+-------+---------------------------------------------+----------+-------------+
| lattice_structure       | str   | Lattice structure code                      |          |             |
+-------------------------+-------+---------------------------------------------+----------+-------------+
| mass                    | float | Relative atomic mass                        |          |             |
+-------------------------+-------+---------------------------------------------+----------+-------------+
| mass_number             | int   | Mass number (most abundant isotope)         |          |             |
+-------------------------+-------+---------------------------------------------+----------+-------------+
| melting_point           | float | Melting temperature                         | K        |             |
+-------------------------+-------+---------------------------------------------+----------+-------------+
| name                    | str   | Name in English                             |          |             |
+-------------------------+-------+---------------------------------------------+----------+-------------+
| neutrons                | int   | Number of neutrons (most abundant isotope)  |          |             |
+-------------------------+-------+---------------------------------------------+----------+-------------+
| oxistates               | list  | Oxidation states                            |          |             |
+-------------------------+-------+---------------------------------------------+----------+-------------+
| period                  | int   | Period in periodic table                    |          |             |
+-------------------------+-------+---------------------------------------------+----------+-------------+
| proton_affinity         | float | Proton affinity                             | kJ/mol   | [8]_        |
+-------------------------+-------+---------------------------------------------+----------+-------------+
| protons                 | int   | Number of protons                           |          |             |
+-------------------------+-------+---------------------------------------------+----------+-------------+
| sconst                  | float | Nuclear charge screening constants          |          | [15]_, [16]_|
+-------------------------+-------+---------------------------------------------+----------+-------------+
| series                  | int   | Index to chemical series                    |          |             |
+-------------------------+-------+---------------------------------------------+----------+-------------+
| specific_heat           | float | Specific heat @ 20 C                        | J/(g mol)|             |
+-------------------------+-------+---------------------------------------------+----------+-------------+
| symbol                  | str   | Chemical symbol                             |          |             |
+-------------------------+-------+---------------------------------------------+----------+-------------+
| thermal_conductivity    | float | Thermal conductivity @25 C                  | W/(m K)  |             |
+-------------------------+-------+---------------------------------------------+----------+-------------+
| vdw_radius              | float | Van der Waals radius                        | pm       | [8]_        |
+-------------------------+-------+---------------------------------------------+----------+-------------+


Some notes on the data
----------------------

Covalent Radii
++++++++++++++

In order to have a more homogeneous data for covalent radii taken from ref. [4]_
the values for 3 different valences for C, also the low and high spin values
for Mn, Fe Co, were respectively averaged.

Allen's configuration energies
++++++++++++++++++++++++++++++

The values of configurational energies from refs. [10]_ and [11]_ were taken as
reported in eV without converting to Pauling units.

Electron affinity
+++++++++++++++++

Electron affinities we taken from [8]_ for the elements for which the data was
available. For He, Be, N, Ar and Xe affinities were taken from [9]_ where they
were specified for metastable ions and therefore the values are negative.


Nuclear charge screening constants
++++++++++++++++++++++++++++++++++

The screening constants were calculated according to the following formula

.. math::

   \sigma_{n,l,m} = Z - n\cdot\zeta_{n,l,m}

where :math:`n` is the principal quantum number, :math:`Z` is the atomic number,
:math:`\sigma_{n,l,m}` is the screening constant, :math:`\zeta_{n,l,m}` is the
optimized exponent from [15]_, [16]_.

For elements Nb, Mo, Ru, Rh, Pd and Ag the exponent values corresponding to the
ground state electronic configuration were taken (entries with superscript `a`
in Table II in [16]_).

For elements La, Pr, Nd and Pm two exponent were reported for 4f shell denoted
4f and 4f' in [16]_. The value corresponding to 4f were used since according to
the authors these are the dominant ones.

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
   Magazine, 40(236), 169–189.
   `doi:10.1080/14786440808636111 <http://dx.doi.org/10.1080/14786440808636111>`_
.. [4] Cordero, B., Gómez, V., Platero-Prats, A. E., Revés, M., Echeverría, J.,
   Cremades, E., … Alvarez, S. (2008). Covalent radii revisited. Dalton
   Transactions, (21), 2832. `doi:10.1039/b801115j <http://www.dx.doi.org/10.1039/b801115j>`_
.. [5] Pyykkö, P., & Atsumi, M. (2009). Molecular Single-Bond Covalent Radii
   for Elements 1-118. Chemistry - A European Journal, 15(1), 186–197.
   `doi:10.1002/chem.200800987 <http://www.dx.doi.org/10.1002/chem.200800987>`_
.. [6] Slater, J. C. (1964). Atomic Radii in Crystals. The Journal of Chemical
   Physics, 41(10), 3199. `doi:10.1063/1.1725697 <http://dx.doi.org/10.1063/1.1725697>`_
.. [7] P. Schwerdtfeger "Table of experimental and calculated static dipole
   polarizabilities for the electronic ground states of the neutral elements
   (in atomic units)", February 11, 2014 `source <http://ctcp.massey.ac.nz/Tablepol2014.pdf>`_
.. [8] W. M. Haynes, Handbook of Chemistry and Physics 95th Edition, CRC Press,
   New York, 2014, ISBN-10: 1482208679, ISBN-13: 978-1482208672.
.. [9] Andersen, T. (2004). Atomic negative ions: structure, dynamics and collisions.
   Physics Reports, 394(4-5), 157–313.
   `doi:10.1016/j.physrep.2004.01.001 <http://www.dx.doi.org/10.1016/j.physrep.2004.01.001>`_
.. [10] Mann, J. B., Meek, T. L., & Allen, L. C. (2000). Configuration Energies of the
   Main Group Elements. Journal of the American Chemical Society, 122(12),
   2780–2783. `doi:10.1021/ja992866e <http://dx.doi.org/10.1021/ja992866e>`_
.. [11] Mann, J. B., Meek, T. L., Knight, E. T., Capitani, J. F., & Allen, L. C.
   (2000). Configuration Energies of the d-Block Elements. Journal of the American
   Chemical Society, 122(21), 5132–5137.
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

