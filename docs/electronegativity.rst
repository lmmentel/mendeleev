=================
Electronegativity
=================

Since electronegativity is useful concept rather than a physical observable,
several scales of electronegativity exist and some of them are available in
:ref:`mendeleev <mendeleev>`. Depending on the definition of a particular scale the values are
either stored directly or recomputed on demand with appropriate formulas. The
following scales are stored:

- :ref:`Pauling <pauling_en>`
- :ref:`Allen <allen_en>`

Moreover there are electronegativity scales that can be computed from their
respective definition and the atomic properties available in :ref:`mendeleev <mendeleev>`:

- :ref:`Mulliken <mulliken_en>`
- :ref:`Gordy <gordy_en>`
- :ref:`Allred-Rochow <allred-rochow_en>`
- :ref:`Nagle <nagle_en>`
- :ref:`Cottrell-Sutton <cottrell-sutton_en>`
- :ref:`Sanderson <sanderson_en>`

For a short overview on electronegativity see this `presentation <https://speakerdeck.com/lmmentel/electronegativity>`_.

.. _allen_en:

Allen
=====

The electronegativity scale proposed by Allen in ref [1]_ can be defined as:

.. math::

   \chi_{A} = \frac{\sum_{x} n_{x}\varepsilon_{x}}{\sum_{x}n_{x}}

where: :math:`\varepsilon_{x}` is the multiplet-averaged one-electron energy of
the subshell :math:`x` and :math:`n_{x}` is the number of electrons in subshell
:math:`x` and the summation runs over the valence shell.

The values that are tabulated were obtained from refs. [2]_ and [3]_.


.. _pauling_en:

Pauling
=======

Pauling's thermochemical scale was introduced in [4]_ as a relative scale based
on electronegativity differences:

.. math::

   \chi_{A} - \chi_{B} = \sqrt{E_{d}(AB) - \frac{1}{2}\left[E_{d}(AA) + E_{d}(BB)\right] }

where: :math:`E_{d}(XY)` is the bond dissociation energy of a diatomic :math:`XY`.
The values available in :ref:`mendeleev <mendeleev>` are taken from ref. [5]_.

.. _mulliken_en:

Mulliken
========

Mulliken scale [6]_ is defined as the arithmetic average of the ionization
potential (:math:`IP`) and the electron affinity (:math:`EA`):

.. math::

   \chi_{M} = \frac{IP + EA}{2}

.. _cottrell-sutton_en:

Cottrell and Sutton
===================

.. math::

  \chi_{CS} = \sqrt{\frac{Z_{\text{eff}}}{r}}

.. _gordy_en:

Gordy
=====

.. math::

   \chi_{G} = \frac{eZ_{\text{eff}}}{r}

.. _allred-rochow_en:

Allred and Rochow
=================

.. math::

   \chi_{AR} = \frac{e^{2}Z_{\text{eff}}}{r^{2}} \notag

.. _nagle_en:

Nagle
=====

.. math::

   \chi_{N} = \sqrt[3]{\frac{n}{\alpha}} \notag


.. _sanderson_en:

Sanderson
==========

.. math::

   \chi_{S} = \frac{\rho}{\rho_{\text{ng}}}



Smith
=====

[2]_

Hinze and Jaffe
===============

Li and Xue
==========

Politzer
========

.. math::

   I(\boldsymbol{r}) = \frac{\sum_{i}\rho_{i}(\boldsymbol{r})\left|\varepsilon_{i}\right|}{\rho(\boldsymbol{r})}

References
==========

.. [1] Allen, L. C. (1989). Electronegativity is the average one-electron energy of
   the valence-shell electrons in ground-state free atoms. Journal of the American
   Chemical Society, 111(25), 9003–9014.
   `doi:10.1021/ja00207a003 <http://dx.doi.org/10.1021/ja00207a003>`_
.. [2] Mann, J. B., Meek, T. L., & Allen, L. C. (2000). Configuration Energies of the
   Main Group Elements. Journal of the American Chemical Society, 122(12),
   2780–2783. `doi:10.1021/ja992866e <http://dx.doi.org/10.1021/ja992866e>`_
.. [3] Mann, J. B., Meek, T. L., Knight, E. T., Capitani, J. F., & Allen, L. C.
   (2000). Configuration Energies of the d-Block Elements. Journal of the American
   Chemical Society, 122(21), 5132–5137.
   `doi:10.1021/ja9928677 <http://dx.doi.org/10.1021/ja9928677>`_
.. [4] Pauling, L. (1932). THE NATURE OF THE CHEMICAL BOND. IV. THE ENERGY OF
   SINGLE BONDS AND THE RELATIVE ELECTRONEGATIVITY OF ATOMS. Journal of the
   American Chemical Society, 54(9), 3570–3582. doi:10.1021/ja01348a011
.. [5] W. M. Haynes, Handbook of Chemistry and Physics 95th Edition, CRC Press,
   New York, 2014, ISBN-10: 1482208679, ISBN-13: 978-1482208672.
.. [7] Smith, D. W. (1990). Electronegativity in two dimensions: Reassessment and
   resolution of the Pearson-Pauling paradox. Journal of Chemical Education,
   67(11), 911. doi:10.1021/ed067p911
.. [6] Mulliken, R. S. (1934). A New Electroaffinity Scale; Together with Data on
   Valence States and on Valence Ionization Potentials and Electron Affinities.
   The Journal of Chemical Physics, 2(11), 782.
   `doi:10.1063/1.1749394 <http://dx.doi.org/10.1063/1.1749394>`_

.. [] Allred, A. L., & Rochow, E. G. (1958). A scale of electronegativity based on
   electrostatic force. Journal of Inorganic and Nuclear Chemistry, 5(4), 264–268.
   `doi:10.1016/0022-1902(58)80003-2 <http://dx.doi.org/10.1016/0022-1902(58)80003-2>`_
