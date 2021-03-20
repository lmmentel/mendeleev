.. **Sanderson electronegativity**

..   The values of Sanderson's electronegativity are taken from from as *revised
   values* from Table 3.1 in ref. :cite:`Sanderson1976`. The
   electronegativities for noble gases are taken from :cite:`Allen1980`.

*******************
Electronegativities
*******************

Since electronegativity is useful concept rather than a physical observable,
several scales of electronegativity exist and some of them are available in
:ref:`mendeleev <mendeleev>`. Depending on the definition of a particular
scale the values are either stored directly or recomputed on demand with
appropriate formulas. The following scales are stored:

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

The electronegativity scale proposed by Allen in ref :cite:`Allen1989` is defined as:

.. math::

   \chi_{A} = \frac{\sum_{x} n_{x}\varepsilon_{x}}{\sum_{x}n_{x}}

where: :math:`\varepsilon_{x}` is the multiplet-averaged one-electron energy of
the subshell :math:`x` and :math:`n_{x}` is the number of electrons in subshell
:math:`x` and the summation runs over the valence shell.

The values that are tabulated were obtained from refs. :cite:`Mann2000a` and :cite:`Mann2000`.

Example::

    >>> Si.en_allen
    11.33
    >>> Si.electronegativity('allen')
    11.33

.. _allred-rochow_en:

Allred and Rochow
=================

The scale of Allred and Rochow :cite:`Allred1958` introduces the electronegativity as the
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

The scale proposed by Cottrell and Sutton :cite:`Cottrell1951` is derived from the equation:

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

Ghosh :cite:`Ghosh2005` presented a scale of electronegativity based on the absolute radii of atoms computed as

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

Gordy's scale :cite:`Gordy1946` is based on the potential that measures the work necessary
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

Li and Xue :cite:`Li2006,Li2009` proposed a scale that takes into account
different valence states and coordination environment of atoms and is
calculated according to the following formula:

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

Martynov and Batsanov :cite:`Batsanov1982` used the square root of the
averaged valence ionization energy as a measure of electronegativity:

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

Mulliken scale :cite:`Mulliken1934` is defined as the arithmetic average of the ionization
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

Nagle :cite:`Nagle1990` derived his scale from the atomic dipole polarizability:

.. math::

   \chi_{N} = \sqrt[3]{\frac{n}{\alpha}} \notag

Example::

    >>> Si.electronegativity('nagle')
    0.47505611644667534

.. _pauling_en:

Pauling
=======

Pauling's thermochemical scale was introduced in :cite:`Pauling1932` as a relative scale based
on electronegativity differences:

.. math::

   \chi_{A} - \chi_{B} = \sqrt{E_{d}(AB) - \frac{1}{2}\left[E_{d}(AA) + E_{d}(BB)\right] }

where: :math:`E_{d}(XY)` is the bond dissociation energy of a diatomic :math:`XY`.
The values available in :ref:`mendeleev <mendeleev>` are taken from ref. :cite:`haynes2014crc`.

Example::

    >>> Si.en_pauling
    1.9
    >>> Si.electronegativity('pauling')
    1.9

.. _sanderson_en:

Sanderson
=========

Sanderson :cite:`Sanderson1951,Sanderson1952` established his scale of electronegativity based on the
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


Fetching all electronegativities
================================

If you want to fetch all the available scales for all elements you can use the
:py:func:`fetch_electronegativities <mendeleev.fetch.fetch_electronegativities>` function,
that collect all the values into a ``DataFrame``.


.. Hinze and Jaffe
   ===============

.. Politzer
.. ========

.. .. math::

..    I(\boldsymbol{r}) = \frac{\sum_{i}\rho_{i}(\boldsymbol{r})\left|\varepsilon_{i}\right|}{\rho(\boldsymbol{r})}


.. [] Leach, M. R. (2013). Concerning electronegativity as a basic elemental property
   and why the periodic table is usually represented in its medium form.
   Foundations of Chemistry, 15(1), 13–29.
   `doi:10.1007/s10698-012-9151-3 <http://www.dx.doi.org/10.1007/s10698-012-9151-3>`_

.. [] Smith, D. W. (1990). Electronegativity in two dimensions: Reassessment and
    resolution of the Pearson-Pauling paradox. Journal of Chemical Education,
    67(11), 911. doi:10.1021/ed067p911