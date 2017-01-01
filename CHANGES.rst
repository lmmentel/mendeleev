*******************
mendeleev Changelog
*******************

v0.2.13 (01-01-2017)
====================

* Updated atomic weight with the newest IUPAC and CIAAW recommendations.
* Added `is_radioactive` and `is_monoisotopic` attributes.
* Updated the docs.

v0.2.12 (21-12-2016)
====================

* Got rid of the scipy dependency.

v0.2.11 (10-11-2016)
====================

* Updated the names and symbols of elements 113, 115, 117, 118.
* Updated the docs.

v0.2.10 (18-10-2016)
====================

* Added the C6 coefficients from Gould and Bucko.
* Added van der Waals radii from Alvarez.

v0.2.9 (16-10-2016)
===================

* Added a scale of electronegativities by Ghosh.

v0.2.8 (29-08-2016)
===================

* Updated the electron affinity of Pb and Co.
* Updates of the docs.

v0.2.7 (02-04-2016)
===================

* Maintenance.

v0.2.6 (02-04-2016)
===================

* Mainly maintenance updates to docs, sphinx `conf.py`, `setup.py`, requirements.

v0.2.5 (02-04-2016)
===================

Features added
--------------

* Added calculation of Martynov and Batsanov scale of electronegativity in 
  ``en_martynov_batsanov`` method in the ``Element`` class

* Added ``abundance_crust`` and ``abundance_sea`` with element abundancies in
  the crust and seas

* Added ``molcas_gv_color`` attribute with `MOLCAS GV <http://www.molcas.org/GV/>`_
  colors

Bugs fixed
----------

* Restored Python 3.x compatibility


v0.2.4 (05-02-2016)
===================

Features added
--------------

* Extended and corrected the documentation and Jupyter notebook tutorials on
  basic usage electronegativities, plotting and tables

Bugs fixed
----------

* Corrected ``raise`` to ``return`` when calling ``en_sanderson`` from
  ``electronegativity``

* Fixed and tested the formula for calculating the Li and Xue scale of
  electronegativity in ``en_lie-xue``

v0.2.3 (27-01-2016)
===================

Features added
--------------

* Added new vdW radii: ``vdw_radius_batsanov``, ``vdw_radius_bondi``,
  ``vdw_radius_dreiding``, ``vdw_radius_mm3``, ``vdw_radius_rt``,
  ``vdw_radius_truhlar``, ``vdw_radius_uff``

* Added an option to plot the long (wide) version of the periodic table in
  ``periodic_plot``

Bugs fixed
----------

* Typos in the docstrings

v0.2.2 (29-11-2015)
===================

Features added
--------------

* Added new covalent radii: ``covalent_radius_bragg``,
  ``covalent_radius_slater``

* Added the ``c6`` dispersion coefficients

* Added ``gas_basicity``, ``proton_affinity`` and ``heat_of_formation``

* Added ``periodic_plot`` function for producing ``Bokeh`` based plots of the
  periodic table

* Added ``jmol_color`` and ``cpk_color`` with different coloring schemes for
  atoms

Bug fixes
---------

* Changed the series of elements 113, 114, 115, 116 to poor metals

v0.2.1 (26-10-2015)
===================

Features added
--------------

* Extended the list of options for calculating Mulliken electronegativities in
  ``en_mulliken``

* Added ``electrons_per_shell`` method

* Added a function to calculate linear interpolation of radii required for
  calculation of Sandersons electronegativity

* Added hybrid attributes ``electrons``, ``protons``, ``neutrons`` and
  ``mass_number``

Bug fixes
---------

* Changed the type of the ``melting_point`` from ``str`` to ``float``

v0.2.0 (22-10-2015)
===================

Features added
--------------

* Instead of ``covalent_radius`` added ``covalent_radius_2008`` and
  ``covalent_radius_2009``

* Instead of ``electronegativity`` added ``en_pauling`` and ``en_mulliken``

* Added a method for getting ionic radii

* Improved the method for calculating the nuclear screening constants

* Added ``ElectronicConfiguration`` class initialized as ``Element`` attribute

* Added nuclear screening constants from Clementi and Raimondi

* Added a method to calculate the absolute softness, absolute hardness and
  absolute electronegativity

* Added ``get_table`` method to retrieve the tables as ``pandas``
  ``DataFrames``

Bug fixes
---------

* Added missing electronic configurations

* Converted ionic radii from Angstrom to pico meters

v0.1.0 (11-07-2015)
===================

First tagged version with the initial structure of the package and first
version of the database and the python interface
