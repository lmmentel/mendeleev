=================
Electronegativity
=================

Since electronegativity is useful concept rather than a physical observable,
several scales of electronegativity exist and some of them are available in
:ref:`mendeleev <mendeleev>`. Depending on the definition of a particular scale the values are
either stored directly or recomputed on demand with appropriate formulas. The
following scales are stored:

- :ref:`Allen <allen_en>`
- :ref:`Ghosh <ghosh_en>`
- :ref:`Pauling <pauling_en>`

Moreover there are electronegativity scales that can be computed from their
respective definition and the atomic properties available in :ref:`mendeleev <mendeleev>`:

- :ref:`Allred-Rochow <allred-rochow_en>`
- :ref:`Cottrell-Sutton <cottrell-sutton_en>`
- :ref:`Gordy <gordy_en>`
- :ref:`Li and Xue <li_xue_en>`
- :ref:`Martynov and Batsanov <martynov_batsanov_en>`
- :ref:`Mulliken <mulliken_en>`
- :ref:`Nagle <nagle_en>`
- :ref:`Sanderson <sanderson_en>`

For a short overview on electronegativity see this `presentation <https://speakerdeck.com/lmmentel/electronegativity>`_.

All the examples shown below are for Silicon::

    >>> from mendeleev import element
    >>> Si = element('Si')

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

Example::

    >>> Si.en_allen
    11.33
    >>> Si.electronegativity('allen')
    11.33

.. _allred-rochow_en:

Allred and Rochow
=================

The scale of Allred and [4]_ Rochow introduces the electronegativity as the
electrostatic force exerted on the electron by the nuclear charge:

.. math::

   \chi_{AR} = \frac{e^{2}Z_{\text{eff}}}{r^{2}} \notag

where: :math:`Z_{\text{eff}}` is the effective nuclear charge and :math:`r` is
the covalent radius.

Example::

    >>> Si.electronegativity('allred-rochow')
    0.00028240190249702736

.. _cottrell-sutton_en:

Cottrell and Sutton
===================

The scale proposed by Cottrell and Sutton [5]_ is derived from the equation:

.. math::

  \chi_{CS} = \sqrt{\frac{Z_{\text{eff}}}{r}}

where: :math:`Z_{\text{eff}}` is the effective nuclear charge and :math:`r` is
the covalent radius.

Example::

    >>> Si.electronegativity('cottrell-sutton')
    0.18099342720014772

.. _ghosh_en:

Ghosh
=====

Ghosh [16]_ presented a scale of electronegativity based on the absolute radii of atoms computed as

.. math::

   \chi_{GH} = a \cdot (1/R) + b

where: :math:`R` is the absolute atomic radius and :math:`a` and :math:`b` are
empirical parameters.

Example::

    >>> Si.en_ghosh
    0.178503


.. _gordy_en:

Gordy
=====

Gordy's scale [6]_ is based on the potential that measures the work necessary
to achieve the charge separation, according to:

.. math::

   \chi_{G} = \frac{eZ_{\text{eff}}}{r}

where: :math:`Z_{\text{eff}}` is the effective nuclear charge and :math:`r` is
the covalent radius.

Example::

    >>> Si.electronegativity('gordy')
    0.03275862068965517

.. _li_xue_en:

Li and Xue
==========

Li and Xue [7]_, [8]_ proposed a scale that takes into account different valence states and
coordination environment of atoms and is calculated according to the following
formula:

.. math::

    \chi_{LX} = \frac{n^{*}\sqrt{I_{j}/Ry}}{r}

where: :math:`n^{*}` is the effective principal quantum number, :math:`I_{j}`
is the `j`'th ionization energy in `eV`, :math:`Ry` is the Rydberg constant in
`eV` and :math:`r` is either the crystal radius or ionic radius.

Example::

    >>> Si.en_li_xue(charge=4)
    {u'IV': 13.16033405547733, u'VI': 9.748395596649873}
    >>> Si.electronegativity('li-xue', charge=4)
    {u'IV': 13.16033405547733, u'VI': 9.748395596649873}

.. _martynov_batsanov_en:

Martynov and Batsanov
=====================

Martynov and Batsanov [9]_ used the square root of the averaged valence
ionization energy as a measure of electronegativity:

.. math::

   \chi_{MB} = \sqrt{\frac{1}{n_{v}}\sum^{n_{v}}_{k=1} I_{k}}

where: :math:`n_{v}` is the number of valence electrons and :math:`I_{k}`
is the :math:`k` th ionization potential.

Example::

    >>> Si.en_martynov_batsanov()
    5.0777041564076963
    >>> Si.electronegativity(scale='martynov-batsanov')
    5.0777041564076963

.. _mulliken_en:

Mulliken
========

Mulliken scale [10]_ is defined as the arithmetic average of the ionization
potential (:math:`IP`) and the electron affinity (:math:`EA`):

.. math::

   \chi_{M} = \frac{IP + EA}{2}

Example::

    >>> Si.en_mulliken()
    4.0758415
    >>> Si.electronegativity('mulliken')
    4.0758415

.. _nagle_en:

Nagle
=====

Nagle [11]_ derived his scale from the atomic dipole polarizability:

.. math::

   \chi_{N} = \sqrt[3]{\frac{n}{\alpha}} \notag

Example::

    >>> Si.electronegativity('nagle')
    0.47505611644667534

.. _pauling_en:

Pauling
=======

Pauling's thermochemical scale was introduced in [12]_ as a relative scale based
on electronegativity differences:

.. math::

   \chi_{A} - \chi_{B} = \sqrt{E_{d}(AB) - \frac{1}{2}\left[E_{d}(AA) + E_{d}(BB)\right] }

where: :math:`E_{d}(XY)` is the bond dissociation energy of a diatomic :math:`XY`.
The values available in :ref:`mendeleev <mendeleev>` are taken from ref. [13]_.

Example::

    >>> Si.en_pauling
    1.9
    >>> Si.electronegativity('pauling')
    1.9

.. _sanderson_en:

Sanderson
==========

Sanderson [14]_, [15]_ established his scale of electronegativity based on the
stability ratio:

.. math::

   \chi_{S} = \frac{\rho}{\rho_{\text{ng}}}

where: :math:`\rho` is the average electron density :math:`\rho=\frac{Z}{4\pi r^{3}/3}`,
and :math:`\rho_{\text{ng}}` is the average electron density of a hypothetical
noble gas atom with charge :math:`Z`.

Example::

    >>> Si.en_sanderson()
    0.3468157872145231
    >>> Si.electronegativity()
    0.3468157872145231

.. Hinze and Jaffe
   ===============

.. Politzer
.. ========

.. .. math::

..    I(\boldsymbol{r}) = \frac{\sum_{i}\rho_{i}(\boldsymbol{r})\left|\varepsilon_{i}\right|}{\rho(\boldsymbol{r})}

References
==========

.. [] Leach, M. R. (2013). Concerning electronegativity as a basic elemental property
   and why the periodic table is usually represented in its medium form.
   Foundations of Chemistry, 15(1), 13–29.
   `doi:10.1007/s10698-012-9151-3 <http://www.dx.doi.org/10.1007/s10698-012-9151-3>`_

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
.. [4] Allred, A. L., & Rochow, E. G. (1958). A scale of electronegativity based on
   electrostatic force. Journal of Inorganic and Nuclear Chemistry, 5(4), 264–268.
   `doi:10.1016/0022-1902(58)80003-2 <http://dx.doi.org/10.1016/0022-1902(58)80003-2>`_
.. [5] Cottrell, T. L., & Sutton, L. E. (1951). Covalency, Electrovalency and
   Electronegativity. Proceedings of the Royal Society A: Mathematical, Physical
   and Engineering Sciences, 207(1088), 49–63.
   `doi:10.1098/rspa.1951.0098 <http://dx.doi.org/10.1098/rspa.1951.0098>`_
.. [6] Gordy, W. (1946). A New Method of Determining Electronegativity from Other
   Atomic Properties. Physical Review, 69(11-12), 604–607.
   `doi:10.1103/PhysRev.69.604 <http://dx.doi.org/10.1103/PhysRev.69.604>`_
.. [7] Li, K., & Xue, D. (2006). Estimation of Electronegativity Values of Elements in
   Different Valence States. The Journal of Physical Chemistry A, 110(39),
   11332–11337. `doi:10.1021/jp062886k <http://dx.doi.org/10.1021/jp062886k>`_
.. [8] Li, K., & Xue, D. (2009). New development of concept of electronegativity.
   Chinese Science Bulletin, 54(2), 328–334.
   `doi:10.1007/s11434-008-0578-9 <http://dx.doi.org/10.1007/s11434-008-0578-9>`_
.. [9] Batsanov, S. S. (1982). Dielectric Methods of Studying the Chemical Bond
   and the Concept of Electronegativity. Russian Chemical Reviews, 51(7), 684–697.
   `doi:10.1070/RC1982v051n07ABEH002900 <http://dx.doi.org/10.1070/RC1982v051n07ABEH002900>`_
.. [10] Mulliken, R. S. (1934). A New Electroaffinity Scale; Together with Data on
   Valence States and on Valence Ionization Potentials and Electron Affinities.
   The Journal of Chemical Physics, 2(11), 782.
   `doi:10.1063/1.1749394 <http://dx.doi.org/10.1063/1.1749394>`_
.. [11] Nagle, J. K. (1990). Atomic polarizability and electronegativity. Journal of
   the American Chemical Society, 112(12), 4741–4747.
   `doi:10.1021/ja00168a019 <http://dx.doi.org/10.1021/ja00168a019>`_
.. [12] Pauling, L. (1932). THE NATURE OF THE CHEMICAL BOND. IV. THE ENERGY OF
   SINGLE BONDS AND THE RELATIVE ELECTRONEGATIVITY OF ATOMS. Journal of the
   American Chemical Society, 54(9), 3570–3582. doi:10.1021/ja01348a011
.. [13] W. M. Haynes, Handbook of Chemistry and Physics 95th Edition, CRC Press,
   New York, 2014, ISBN-10: 1482208679, ISBN-13: 978-1482208672.
.. [14] Sanderson, R. T. (1951). An Interpretation of Bond Lengths and a Classification
   of Bonds. Science, 114(2973), 670–672.
   `doi:10.1126/science.114.2973.670 <http://dx.doi.org/10.1126/science.114.2973.670>`_
.. [15] Sanderson, R. T. (1952). An Explanation of Chemical Variations within Periodic
   Major Groups. Journal of the American Chemical Society, 74(19), 4792–4794.
   `doi:10.1021/ja01139a020 <http://dx.doi.org/10.1021/ja01139a020>`_
.. [] Smith, D. W. (1990). Electronegativity in two dimensions: Reassessment and
    resolution of the Pearson-Pauling paradox. Journal of Chemical Education,
    67(11), 911. doi:10.1021/ed067p911
.. [16] Ghosh, D. C. (2005). A New Scale of Electronegativity Based on Absolute Radii of Atoms.
   Journal of Theoretical and Computational Chemistry, 4(1), 21–33.
   `doi:10.1142/S0219633605001556 <http://doi.org/10.1142/S0219633605001556>`_
