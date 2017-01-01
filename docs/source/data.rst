Data
====

The followig data are currently available:

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

Some notes on the data
----------------------

Atomic Weights
++++++++++++++

Atomic weights and their uncertainties were retrieved mainly from ref. [37]_. For
elements whose values were given as ranges the *conventional atomic weights* from
Table 3 in ref. [36]_ were taken. For radioactive elements the standard approach
was adopted where the weight is taken as the mass number of the most stable isotope.
The data was obtained from `CIAAW page on radioactive elements <http://www.ciaaw.org/radioactive-elements.htm>`_.
In cases where two isotopes were specified the one with the smaller standard deviation was chosen.
In case of Tc and Pm relative weights of their isotopes were used, for Tc isotope 98, and for Pm isotope 145 were taken
from `CIAAW <http://www.ciaaw.org/atomic-masses.htm>`_.


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

Electron affinities were taken from [8]_ for the elements for which the data was
available. For He, Be, N, Ar and Xe affinities were taken from [9]_ where they
were specified for metastable ions and therefore the values are negative.

Updates

  - Electron affinity of niobium was taken from [29]_.

  - Electron affinity of cobalt was taken from [30]_.

  - Electron affinity of lead was taken from [31]_.


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

Sanderson electronegativity
+++++++++++++++++++++++++++

The values of Sanderson's electronegativity are taken from from as *revised values*
from Table 3.1 in ref. [27]_. The electronegativities for noble gases are taken
from [28]_.


van der Waals radii according to Alvarez
++++++++++++++++++++++++++++++++++++++++

The bulk of the radii data was taken from Ref. [33]_, but the radii for noble gasses were
update according to the values in Ref. [34]_.


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
   