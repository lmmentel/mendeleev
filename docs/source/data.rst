
****
Data
****

To find out how to fetch data in bulk, check out the documentation about :ref:`data access <notebooks/02_data_access.ipynb>`.

Elements
========

The followig data are currently available:

+-------------------------------+-------+------------------------------------------------------+----------+-----------------------------------------------------+
| Name                          | Type  | Comment                                              | Unit     | Data Source                                         |
+===============================+=======+======================================================+==========+=====================================================+
| abundance_crust               | float | Abundance in the Earth's crust                       | mg/kg    | :cite:`haynes2014crc`                               |
+-------------------------------+-------+------------------------------------------------------+----------+-----------------------------------------------------+
| abundance_sea                 | float | Abundance in the seas                                | mg/L     | :cite:`haynes2014crc`                               |
+-------------------------------+-------+------------------------------------------------------+----------+-----------------------------------------------------+
| annotation                    | str   | Annotations regarding the data                       |          |                                                     |
+-------------------------------+-------+------------------------------------------------------+----------+-----------------------------------------------------+
| atomic_number                 | int   | Atomic number                                        |          |                                                     |
+-------------------------------+-------+------------------------------------------------------+----------+-----------------------------------------------------+
| atomic_radius                 | float | Atomic radius                                        | pm       | :cite:`Slater1964`                                  |
+-------------------------------+-------+------------------------------------------------------+----------+-----------------------------------------------------+
| atomic_radius_rahm            | float | Atomic radius by Rahm et al.                         | pm       | :cite:`Rahm2016,Rahm2017`                           |
+-------------------------------+-------+------------------------------------------------------+----------+-----------------------------------------------------+
| atomic_volume                 | float | Atomic volume                                        | cm3/mol  |                                                     |
+-------------------------------+-------+------------------------------------------------------+----------+-----------------------------------------------------+
| atomic_weight                 | float | Atomic weight\ [#f1]_                                |          | :cite:`Meija2016,iupac-weights`                     |
+-------------------------------+-------+------------------------------------------------------+----------+-----------------------------------------------------+
| atomic_weight_uncertainty     | float | Atomic weight uncertainty\ [#f1]_                    |          | :cite:`Meija2016,iupac-weights`                     |
+-------------------------------+-------+------------------------------------------------------+----------+-----------------------------------------------------+
| block                         | str   | Block in periodic table                              |          |                                                     |
+-------------------------------+-------+------------------------------------------------------+----------+-----------------------------------------------------+
| boiling_point                 | float | Boiling temperature                                  | K        |                                                     |
+-------------------------------+-------+------------------------------------------------------+----------+-----------------------------------------------------+
| c6                            | float | C_6 dispersion coefficient in a.u.                   | a.u.     | :cite:`Chu2004,Tang1976`                            |
+-------------------------------+-------+------------------------------------------------------+----------+-----------------------------------------------------+
| c6_gb                         | float | C_6 dispersion coefficient in a.u. (Gould & Bučko)   | a.u.     | :cite:`Gould2016`                                   |
+-------------------------------+-------+------------------------------------------------------+----------+-----------------------------------------------------+
| cas                           | str   | Chemical Abstracts Serice identifier                 |          |                                                     |
+-------------------------------+-------+------------------------------------------------------+----------+-----------------------------------------------------+
| covalent_radius_bragg         | float | Covalent radius by Bragg                             | pm       | :cite:`Bragg1920`                                   |
+-------------------------------+-------+------------------------------------------------------+----------+-----------------------------------------------------+
| covalent_radius_cordero       | float | Covalent radius by Cerdero et al.\ [#f2]_            | pm       | :cite:`Cordero2008`                                 |
+-------------------------------+-------+------------------------------------------------------+----------+-----------------------------------------------------+
| covalent_radius_pyykko        | float | Single bond covalent radius by Pyykko et al.         | pm       | :cite:`Pyykko2009`                                  |
+-------------------------------+-------+------------------------------------------------------+----------+-----------------------------------------------------+
| covalent_radius_pyykko_double | float | Double bond covalent radius by Pyykko et al.         | pm       | :cite:`Pyykko2009a`                                 |
+-------------------------------+-------+------------------------------------------------------+----------+-----------------------------------------------------+
| covalent_radius_pyykko_triple | float | Triple bond covalent radius by Pyykko et al.         | pm       | :cite:`Pyykko2005`                                  |
+-------------------------------+-------+------------------------------------------------------+----------+-----------------------------------------------------+
| cpk_color                     | str   | Element color in CPK convention                      | HEX      | :cite:`wiki-cpk`                                    |
+-------------------------------+-------+------------------------------------------------------+----------+-----------------------------------------------------+
| density                       | float | Density at 295K                                      | g/cm3    |                                                     |
+-------------------------------+-------+------------------------------------------------------+----------+-----------------------------------------------------+
| description                   | str   | Short description of the element                     |          |                                                     |
+-------------------------------+-------+------------------------------------------------------+----------+-----------------------------------------------------+
| dipole_polarizability         | float | Dipole polarizability                                | a.u.     | :cite:`Schwerdtfeger2018`                           |
+-------------------------------+-------+------------------------------------------------------+----------+-----------------------------------------------------+
| dipole_polarizability_unc     | float | Dipole polarizability uncertainty                    | a.u.     | :cite:`Schwerdtfeger2018`                           |
+-------------------------------+-------+------------------------------------------------------+----------+-----------------------------------------------------+
| discoverers                   | str   | The discoverers of the element                       |          |                                                     |
+-------------------------------+-------+------------------------------------------------------+----------+-----------------------------------------------------+
| discovery_location            | str   | The location where the element was discovered        |          |                                                     |
+-------------------------------+-------+------------------------------------------------------+----------+-----------------------------------------------------+
| dipole_year                   | int   | The year the element was discovered                  |          |                                                     |
+-------------------------------+-------+------------------------------------------------------+----------+-----------------------------------------------------+
| electron_affinity             | float | Electron affinity\ [#f3]_                            | eV       | :cite:`haynes2014crc,Andersen2004`                  |
+-------------------------------+-------+------------------------------------------------------+----------+-----------------------------------------------------+
| electrons                     | int   | Number of electrons                                  |          |                                                     |
+-------------------------------+-------+------------------------------------------------------+----------+-----------------------------------------------------+
| electrophilicity              | flaot | Electrophilicity index                               | eV       | :cite:`Parr1999`                                    |
+-------------------------------+-------+------------------------------------------------------+----------+-----------------------------------------------------+
| en_allen                      | float | Allen's scale of electronegativity\ [#f4]_           | eV       | :cite:`Mann2000a,Mann2000`                          |
+-------------------------------+-------+------------------------------------------------------+----------+-----------------------------------------------------+
| en_ghosh                      | float | Ghosh's scale of electronegativity                   |          | :cite:`Ghosh2005`                                   |
+-------------------------------+-------+------------------------------------------------------+----------+-----------------------------------------------------+
| en_mulliken                   | float | Mulliken's scale of electronegativity                | eV       | :cite:`Mulliken1934`                                |
+-------------------------------+-------+------------------------------------------------------+----------+-----------------------------------------------------+
| en_pauling                    | float | Pauling's scale of electronegativity                 |          | :cite:`haynes2014crc`                               |
+-------------------------------+-------+------------------------------------------------------+----------+-----------------------------------------------------+
| econf                         | str   | Ground state electron configuration                  |          |                                                     |
+-------------------------------+-------+------------------------------------------------------+----------+-----------------------------------------------------+
| evaporation_heat              | float | Evaporation heat                                     | kJ/mol   |                                                     |
+-------------------------------+-------+------------------------------------------------------+----------+-----------------------------------------------------+
| fusion_heat                   | float | Fusion heat                                          | kJ/mol   |                                                     |
+-------------------------------+-------+------------------------------------------------------+----------+-----------------------------------------------------+
| gas_basicity                  | float | Gas basicity                                         | kJ/mol   | :cite:`haynes2014crc`                               |
+-------------------------------+-------+------------------------------------------------------+----------+-----------------------------------------------------+
| geochemical_class             | str   | Geochemical classification                           |          | :cite:`white2013geochemistry`                       |
+-------------------------------+-------+------------------------------------------------------+----------+-----------------------------------------------------+
| glawe_number                  | int   | Glawe's number (scale)                               |          | :cite:`Glawe2016`                                   |
+-------------------------------+-------+------------------------------------------------------+----------+-----------------------------------------------------+
| goldschmidt_class             | str   | Goldschmidt classification                           |          | :cite:`white2013geochemistry,wiki-goldschmidt`      |
+-------------------------------+-------+------------------------------------------------------+----------+-----------------------------------------------------+
| group                         | int   | Group in periodic table                              |          |                                                     |
+-------------------------------+-------+------------------------------------------------------+----------+-----------------------------------------------------+
| heat_of_formation             | float | Heat of formation                                    | kJ/mol   | :cite:`haynes2014crc`                               |
+-------------------------------+-------+------------------------------------------------------+----------+-----------------------------------------------------+
| ionenergy                     | tuple | Ionization energies                                  | eV       | :cite:`NIST-ASD`                                    |
+-------------------------------+-------+------------------------------------------------------+----------+-----------------------------------------------------+
| ionic_radii                   | list  | Ionic and crystal radii in pm\ [#f9]_                | pm       | :cite:`Shannon1976,Lundberg2016`                    |
+-------------------------------+-------+------------------------------------------------------+----------+-----------------------------------------------------+
| is_monoisotopic               | bool  | Is the element monoisotopic                          |          |                                                     |
+-------------------------------+-------+------------------------------------------------------+----------+-----------------------------------------------------+
| is_radioactive                | bool  | Is the element radioactive                           |          |                                                     |
+-------------------------------+-------+------------------------------------------------------+----------+-----------------------------------------------------+
| isotopes                      | list  | Isotopes                                             |          |                                                     |
+-------------------------------+-------+------------------------------------------------------+----------+-----------------------------------------------------+
| jmol_color                    | str   | Element color in Jmol convention                     | HEX      | :cite:`jmol-colors`                                 |
+-------------------------------+-------+------------------------------------------------------+----------+-----------------------------------------------------+
| lattice_constant              | float | Lattice constant                                     | Angstrom |                                                     |
+-------------------------------+-------+------------------------------------------------------+----------+-----------------------------------------------------+
| lattice_structure             | str   | Lattice structure code                               |          |                                                     |
+-------------------------------+-------+------------------------------------------------------+----------+-----------------------------------------------------+
| mass_number                   | int   | Mass number (most abundant isotope)                  |          |                                                     |
+-------------------------------+-------+------------------------------------------------------+----------+-----------------------------------------------------+
| melting_point                 | float | Melting temperature                                  | K        |                                                     |
+-------------------------------+-------+------------------------------------------------------+----------+-----------------------------------------------------+
| mendeleev_number              | int   | Mendeleev's number\ [#f5]_                           |          | :cite:`Pettifor1984,Villars2004`                    |
+-------------------------------+-------+------------------------------------------------------+----------+-----------------------------------------------------+
| metallic_radius               | float | Single-bond metallic radius                          | pm       | :cite:`kyleandlaby`                                 |
+-------------------------------+-------+------------------------------------------------------+----------+-----------------------------------------------------+
| metallic_radius_c12           | float | Metallic radius with 12 nearest neighbors            | pm       | :cite:`kyleandlaby`                                 |
+-------------------------------+-------+------------------------------------------------------+----------+-----------------------------------------------------+
| molcas_gv_color               | str   | Element color in MOCAS GV convention                 | HEX      | :cite:`molcas-colors`                               |
+-------------------------------+-------+------------------------------------------------------+----------+-----------------------------------------------------+
| name                          | str   | Name in English                                      |          |                                                     |
+-------------------------------+-------+------------------------------------------------------+----------+-----------------------------------------------------+
| name_origin                   | str   | Origin of the name                                   |          |                                                     |
+-------------------------------+-------+------------------------------------------------------+----------+-----------------------------------------------------+
| neutrons                      | int   | Number of neutrons (most abundant isotope)           |          |                                                     |
+-------------------------------+-------+------------------------------------------------------+----------+-----------------------------------------------------+
| oxistates                     | list  | Oxidation states                                     |          |                                                     |
+-------------------------------+-------+------------------------------------------------------+----------+-----------------------------------------------------+
| period                        | int   | Period in periodic table                             |          |                                                     |
+-------------------------------+-------+------------------------------------------------------+----------+-----------------------------------------------------+
| pettifor_number               | float | Pettifor scale                                       |          | :cite:`Pettifor1984`                                |
+-------------------------------+-------+------------------------------------------------------+----------+-----------------------------------------------------+
| proton_affinity               | float | Proton affinity                                      | kJ/mol   | :cite:`haynes2014crc`                               |
+-------------------------------+-------+------------------------------------------------------+----------+-----------------------------------------------------+
| protons                       | int   | Number of protons                                    |          |                                                     |
+-------------------------------+-------+------------------------------------------------------+----------+-----------------------------------------------------+
| sconst                        | float | Nuclear charge screening constants\ [#f6]_           |          | :cite:`Clementi1963,Clementi1967`                   |
+-------------------------------+-------+------------------------------------------------------+----------+-----------------------------------------------------+
| series                        | int   | Index to chemical series                             |          |                                                     |
+-------------------------------+-------+------------------------------------------------------+----------+-----------------------------------------------------+
| sources                       | str   | Sources of the element                               |          |                                                     |
+-------------------------------+-------+------------------------------------------------------+----------+-----------------------------------------------------+
| specific_heat                 | float | Specific heat @ 20 C                                 | J/(g mol)|                                                     |
+-------------------------------+-------+------------------------------------------------------+----------+-----------------------------------------------------+
| symbol                        | str   | Chemical symbol                                      |          |                                                     |
+-------------------------------+-------+------------------------------------------------------+----------+-----------------------------------------------------+
| thermal_conductivity          | float | Thermal conductivity @25 C                           | W/(m K)  |                                                     |
+-------------------------------+-------+------------------------------------------------------+----------+-----------------------------------------------------+
| uses                          | str   | Applications of the element                          |          |                                                     |
+-------------------------------+-------+------------------------------------------------------+----------+-----------------------------------------------------+
| vdw_radius                    | float | Van der Waals radius                                 | pm       | :cite:`haynes2014crc`                               |
+-------------------------------+-------+------------------------------------------------------+----------+-----------------------------------------------------+
| vdw_radius_alvarez            | float | Van der Waals radius according to Alvarez\ [#f7]_    | pm       | :cite:`Alvarez2013,Vogt2014`                        |
+-------------------------------+-------+------------------------------------------------------+----------+-----------------------------------------------------+
| vdw_radius_batsanov           | float | Van der Waals radius according to Batsanov           | pm       | :cite:`Batsanov2001`                                |
+-------------------------------+-------+------------------------------------------------------+----------+-----------------------------------------------------+
| vdw_radius_bondi              | float | Van der Waals radius according to Bondi              | pm       | :cite:`Bondi1964`                                   |
+-------------------------------+-------+------------------------------------------------------+----------+-----------------------------------------------------+
| vdw_radius_dreiding           | float | Van der Waals radius from the DREIDING FF            | pm       | :cite:`Mayo1990`                                    |
+-------------------------------+-------+------------------------------------------------------+----------+-----------------------------------------------------+
| vdw_radius_mm3                | float | Van der Waals radius from the MM3 FF                 | pm       | :cite:`Allinger1994`                                |
+-------------------------------+-------+------------------------------------------------------+----------+-----------------------------------------------------+
| vdw_radius_rt                 | float | Van der Waals radius according to Rowland and Taylor | pm       | :cite:`Rowland1996`                                 |
+-------------------------------+-------+------------------------------------------------------+----------+-----------------------------------------------------+
| vdw_radius_truhlar            | float | Van der Waals radius according to Truhlar            | pm       | :cite:`Mantina2009`                                 |
+-------------------------------+-------+------------------------------------------------------+----------+-----------------------------------------------------+
| vdw_radius_uff                | float | Van der Waals radius from the UFF                    | pm       | :cite:`Rappe1992`                                   |
+-------------------------------+-------+------------------------------------------------------+----------+-----------------------------------------------------+

Isotopes
========

+---------------------------+-------+------------------------------------------------------+--------------+-------------------------+
| Name                      | Type  | Comment                                              | Unit         | Data Source             |
+===========================+=======+======================================================+==============+=========================+
| abundance                 | float | Relative Abundance                                   |              | :cite:`iupac-abund`     |
+---------------------------+-------+------------------------------------------------------+--------------+-------------------------+
| g_factor                  | float | Nuclear g-factor\ [#f8]_                             |              | :cite:`Stone2014`       |
+---------------------------+-------+------------------------------------------------------+--------------+-------------------------+
| half_life                 | float | Half life of the isotope                             |              | :cite:`Meija2016`       |
+---------------------------+-------+------------------------------------------------------+--------------+-------------------------+
| half_life_unit            | str   | Unit in which the half life is given                 |              | :cite:`Meija2016`       |
+---------------------------+-------+------------------------------------------------------+--------------+-------------------------+
| is_radioactive            | bool  | Is the isotope radioactive                           |              | :cite:`iupac-masses`    |
+---------------------------+-------+------------------------------------------------------+--------------+-------------------------+
| mass                      | float | Atomic mass                                          | Da           | :cite:`iupac-masses`    |
+---------------------------+-------+------------------------------------------------------+--------------+-------------------------+
| mass_number               | int   | Mass number of the isotope                           |              | :cite:`iupac-masses`    |
+---------------------------+-------+------------------------------------------------------+--------------+-------------------------+
| mass_uncertainty          | float | Uncertainty of the atomic mass                       |              | :cite:`iupac-masses`    |
+---------------------------+-------+------------------------------------------------------+--------------+-------------------------+
| spin                      | float | Nuclear spin quantum number                          |              |                         |
+---------------------------+-------+------------------------------------------------------+--------------+-------------------------+
| quadrupole_moment         | float | Nuclear electric quadrupole moment\ [#f8]_           | b [100 fm^2] | :cite:`Stone2013`       |
+---------------------------+-------+------------------------------------------------------+--------------+-------------------------+


.. rubric:: Data Footnotes

.. [#f1] **Atomic Weights**

   Atomic weights and their uncertainties were retrieved mainly from ref. :cite:`iupac-weights`. For
   elements whose values were given as ranges the *conventional atomic weights* from
   Table 3 in ref. :cite:`Meija2016` were taken. For radioactive elements the standard approach
   was adopted where the weight is taken as the mass number of the most stable isotope.
   The data was obtained from `CIAAW page on radioactive elements <http://www.ciaaw.org/radioactive-elements.htm>`_.
   In cases where two isotopes were specified the one with the smaller standard deviation was chosen.
   In case of Tc and Pm relative weights of their isotopes were used, for Tc isotope 98, and for Pm isotope 145 were taken
   from `CIAAW <http://www.ciaaw.org/atomic-masses.htm>`_.

.. [#f2] **Covalent Radius by Cordero et al.**

   In order to have a more homogeneous data for covalent radii taken from ref.
   :cite:`Cordero2008` the values for 3 different valences for C, also the low
   and high spin values for Mn, Fe Co, were respectively averaged.

.. [#f3] **Electron affinity**

   Electron affinities were taken from :cite:`haynes2014crc` for the elements
   for which the data was available. For He, Be, N, Ar and Xe affinities were
   taken from :cite:`Andersen2004` where they were specified for metastable
   ions and therefore the values are negative.
   
   Updates
   
     - Electron affinity of niobium was taken from :cite:`Luo2016`.
     - Electron affinity of cobalt was taken from :cite:`Chen2016a`.
     - Electron affinity of lead was taken from :cite:`Chen2016`.

.. [#f4] **Allen's configuration energies**

   The values of configurational energies from refs. :cite:`Mann2000a` and
   :cite:`Mann2000` were taken as reported in eV without converting to Pauling
   units.

.. [#f5] **Mendeleev numbers**
    
   Mendeleev numbers were mostly taken from :cite:`Villars2004` but the range
   was extended to cover the whole periodic table following the prescription
   in the article of increasing the numbers going from top to bottom in each
   group and group by group from left to right in the periodic table.

.. [#f6] **Nuclear charge screening constants**

   The screening constants were calculated according to the following formula

   .. math::
   
      \sigma_{n,l,m} = Z - n\cdot\zeta_{n,l,m}
   
   where :math:`n` is the principal quantum number, :math:`Z` is the atomic number,
   :math:`\sigma_{n,l,m}` is the screening constant, :math:`\zeta_{n,l,m}` is the
   optimized exponent from :cite:`Clementi1963,Clementi1967`.
   
   For elements Nb, Mo, Ru, Rh, Pd and Ag the exponent values corresponding to the
   ground state electronic configuration were taken (entries with superscript `a`
   in Table II in :cite:`Clementi1967`).
   
   For elements La, Pr, Nd and Pm two exponent were reported for 4f shell denoted
   4f and 4f' in :cite:`Clementi1967`. The value corresponding to 4f were used
   since according to the authors these are the dominant ones.

.. [#f7] **van der Waals radii according to Alvarez**

   The bulk of the radii data was taken from Ref. :cite:`Alvarez2013`, but the
   radii for noble gasses were update according to the values in Ref.
   :cite:`Vogt2014`.

.. [#f8] **Isotope g-factors and quadrupole moments**

   The data regarding g-factors and electric quadrupole moments was parsed from
   `easyspin webpage <http://easyspin.org/documentation/isotopetable.html>`_
   (accessed 25.01.2017) where additional notes are mentioned:
   
   - Typo for Rh-103: Moment is factor of 10 too large
   - 237Np, 239Pu, 243Am magnetic moment data from :cite:`haynes2014crc`, section 11-2
   - In quadrupole moment data - a typo for Ac-227: sign should be +

.. [#f9] **Ionic radii for Actinoid (III) ions**

   Ionic raddi values for 3+ Actinoids were with coordination number 9 were taken
   from :cite:`Lundberg2016`. In addition ``crystal_radius`` values were computed
   by adding 14 pm to the ``ionic_radius`` values according to :cite:`Shannon1976`.

