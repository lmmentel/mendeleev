
Some notes on the data
======================

Electron affinity
-----------------

Electron affinites we taken from [2]_ for the elements for which the data was
available. For He, Be, N, Ar and Xe afinities were taken from [3]_ where they
were specified for metastable ions and therefore the values are negative.


Nuclear charge screening constants
----------------------------------

The screening constants were calculated according to the following formula

.. math::

   \sigma_{n,l,m} = Z - n\cdot\zeta_{n,l,m}

where :math:`n` is the pricipal quantum number, :math:`Z` is the atomic number,
:math:`\sigma_{n,l,m}` is the screening constant, :math:`\zeta_{n,l,m}` si the
optimized exponent from [6]_, [7]_.

For elements Nb, Mo, Ru, Rh, Pd and Ag the exponent values corresponding to the
ground state electronic configuration were taken (entries with superscript `a`
in Table II in [7]_).

For elements La, Pr, Nd and Pm two exponent were reported for 4f shell denoted
4f and 4f' in [7]_. The value corresponding to 4f were used since according to
the authors these are the dominant ones.

.. [2] W. M. Haynes, Handboob of Chemistry and Physics 95th Edition, CRC Press,
   New York, 2014, ISBN-10: 1482208679, ISBN-13: 978-1482208672.
.. [3] Andersen, T. (2004). Atomic negative ions: structure, dynamics and collisions.
   Physics Reports, 394(4-5), 157–313.
   `doi:10.1016/j.physrep.2004.01.001 <http://www.dx.doi.org/10.1016/j.physrep.2004.01.001>`_
.. [6] Clementi, E., & Raimondi, D. L. (1963). Atomic Screening Constants from
   SCF Functions. The Journal of Chemical Physics, 38(11), 2686.
   `doi:10.1063/1.1733573 <http://www.dx.doi.org/10.1063/1.1733573>`_
.. [7] Clementi, E. (1967). Atomic Screening Constants from SCF Functions. II.
   Atoms with 37 to 86 Electrons. The Journal of Chemical Physics, 47(4), 1300.
   `doi:10.1063/1.1712084 <http://www.dx.doi.org/10.1063/1.1712084>`_
