.. _data:

****
Data
****

To find out how to fetch data in bulk, check out the documentation about
:doc:`data access <notebooks/bulk_data_access>`.

Elements
========

Class: :py:class:`Element <mendeleev.models.Element>`

The following data are currently available:

{{ Element }}

Isotopes
========

Class: :py:class:`Isotope <mendeleev.models.Isotope>`

{{ Isotope }}

Isotope Decay Modes
===================

Class: :py:class:`IsotopeDecayMode <mendeleev.models.IsotopeDecayMode>`

{{ IsotopeDecayMode }}

The different modes in the table are stores as ASCII representations
for compatibility. The table below provides explanations of the symbols.

+---------+----------------------------+------------------------------------------------------------+
| ASCII   | Unicode                    | Description                                                |
+=========+============================+============================================================+
| A       | :math:`\alpha`             | :math:`\alpha` emission                                    |
+---------+----------------------------+------------------------------------------------------------+
| p       | p                          | proton emission                                            |
+---------+----------------------------+------------------------------------------------------------+
| 2p      | 2p                         | 2-proton emission                                          |
+---------+----------------------------+------------------------------------------------------------+
| n       | n                          | neutron emission                                           |
+---------+----------------------------+------------------------------------------------------------+
| 2n      | 2n                         | 2-neutron emission                                         |
+---------+----------------------------+------------------------------------------------------------+
| EC      | :math:`\epsilon`           | electron capture                                           |
+---------+----------------------------+------------------------------------------------------------+
| e+      | :math:`e^{+}`              | positron emission                                          |
+---------+----------------------------+------------------------------------------------------------+
| B+      | :math:`\beta^{+}`          | :math:`\beta^{+}` decay (:math:`\beta^{+}=\epsilon+e^{+}`) |
+---------+----------------------------+------------------------------------------------------------+
| B-      | :math:`\beta^{-}`          | :math:`\beta^{-}` decay                                    |
+---------+----------------------------+------------------------------------------------------------+
| 2B-     | 2\ :math:`\beta^{-}`       | double :math:`\beta^{-}` decay                             |
+---------+----------------------------+------------------------------------------------------------+
| 2B+     | 2\ :math:`\beta^{+}`       | double :math:`\beta^{+}` decay                             |
+---------+----------------------------+------------------------------------------------------------+
| B-n     | :math:`\beta^{-}` n        | :math:`\beta^{-}`-delayed neutron emission                 |
+---------+----------------------------+------------------------------------------------------------+
| B-2n    | :math:`\beta^{-}` 2n       | :math:`\beta^{-}`-delayed 2-neutron emission               |
+---------+----------------------------+------------------------------------------------------------+
| B-3n    | :math:`\beta^{-}` 3n       | :math:`\beta^{-}`-delayed 3-neutron emission               |
+---------+----------------------------+------------------------------------------------------------+
| B+p     | :math:`\beta^{+}` p        | :math:`\beta^{+}`-delayed proton emission                  |
+---------+----------------------------+------------------------------------------------------------+
| B+2p    | :math:`\beta^{+}` 2p       | :math:`\beta^{+}`-delayed 2-proton emission                |
+---------+----------------------------+------------------------------------------------------------+
| B+3p    | :math:`\beta^{+}` 3p       | :math:`\beta^{+}`-delayed 3-proton emission                |
+---------+----------------------------+------------------------------------------------------------+
| B-A     | :math:`\beta^{-}\alpha`    | :math:`\beta^{-}`-delayed :math:`\alpha` emission          |
+---------+----------------------------+------------------------------------------------------------+
| B+A     | :math:`\beta^{+}\alpha`    | :math:`\beta^{+}`-delayed :math:`\alpha` emission          |
+---------+----------------------------+------------------------------------------------------------+
| B-d     | :math:`\beta^{-}` d        | :math:`\beta^{-}`-delayed deuteron emission                |
+---------+----------------------------+------------------------------------------------------------+
| B-t     | :math:`\beta^{-}` t        | :math:`\beta^{-}`-delayed triton emission                  |
+---------+----------------------------+------------------------------------------------------------+
| IT      | IT                         | internal transition                                        |
+---------+----------------------------+------------------------------------------------------------+
| SF      | SF                         | spontaneous fission                                        |
+---------+----------------------------+------------------------------------------------------------+
| B+SF    | :math:`\beta^{+}` SF       | :math:`\beta^{+}`-delayed fission                          |
+---------+----------------------------+------------------------------------------------------------+
| B-SF    | :math:`\beta^{-}` SF       | :math:`\beta^{-}`-delayed fission                          |
+---------+----------------------------+------------------------------------------------------------+
| 24Ne    | 24Ne                       | heavy cluster emission                                     |
+---------+----------------------------+------------------------------------------------------------+

Atomic Scattering Factors
=========================

Class: :py:class:`ScatteringFactor <mendeleev.models.ScatteringFactor>`

{{ ScatteringFactor }}

Ionization Energies
===================

Class: :py:class:`IonizationEnergy <mendeleev.models.IonizationEnergy>`

{{ IonizationEnergy }}

Ionic Radii
===========

Class: :py:class:`IonicRadius <mendeleev.models.IonicRadius>`

{{ IonicRadius }}

Notes
-----

**Ionic radii for Actinoid (III) ions**

Ionic radii values for 3\ :sup:`+` Actinoids were with coordination number 9 were taken
from :cite:`Lundberg2016`. In addition, ``crystal_radius`` values were computed
by adding 14 pm to the ``ionic_radius`` values according to :cite:`Shannon1976`.

Oxidation States
================

Class: :py:class:`OxidationState <mendeleev.models.OxidationState>`

{{ OxidationState }}

Phase Transitions
=================

Class: :py:class:`PhaseTransition <mendeleev.models.PhaseTransition>`

{{ PhaseTransition }}

Screening Constants
===================

Class: :py:class:`ScreeningConstant <mendeleev.models.ScreeningConstant>`

{{ ScreeningConstant }}

.. rubric:: Data Footnotes

{{ footnotes }}
