"""
Electronegativity scale formulas
"""

import math
from typing import List

import numpy as np

from .utils import n_effective


# Rydberg constant
RY = 13.605693009


def allred_rochow(zeff: float, radius: float) -> float:
    """
    Calculate the electronegativity of an atom according to the definition
    of Allred and Rochow

    Args:
        zeff: effective nuclear charge
        radius: value of the radius
    """

    return zeff / math.pow(radius, 2)


def cottrell_sutton(zeff: float, radius: float) -> float:
    """
    Calculate the electronegativity of an atom according to the definition
    of Allred and Rochow

    Args:
        zeff: effective nuclear charge
        radius: value of the radius
    """

    return math.sqrt(zeff / radius)


def gordy(zeff: float, radius: float) -> float:
    """
    Calculate the electronegativity of an atom according to the definition
    of Allred and Rochow

    Args:
        zeff: effective nuclear charge
        radius: value of the radius
    """

    return zeff / radius


def li_xue(ionization_energy: float, radius: float, valence_pqn: int) -> float:
    """
    Calculate the electronegativity of an atom according to the definition
    of Li and Xue

    Args:
        charge : int
            Charge of the ion
        radius : str
            Type of radius to be used in the calculation, either
            `crystal_radius` as recommended in the paper or `ionic_radius`
        valence_pqn: valence principal quantum number

    Returns:
        electronegativity
    """

    return (
        n_effective(valence_pqn, source="zhang")
        * math.sqrt(ionization_energy / RY)
        * 100.0
        / radius
    )


def martynov_batsanov(ionization_energies: List[float]) -> float:
    """
    Calculates the electronegativity value according to Martynov and
    Batsanov as the average of the ionization energies of the valence
    electrons

    Args:
        ionization_energies: ionization energies for the valence electrons

    Return:
        e: electronegativity value

    .. math::

        \chi_{MB} = \sqrt{\\frac{1}{n_{v}}\sum^{n_{v}}_{k=1} I_{k}}

    where: :math:`n_{v}` is the number of valence electrons and
    :math:`I_{k}` is the :math:`k` th ionization potential.
    """

    return np.sqrt(np.array(ionization_energies).mean())


def mulliken(
    ionization_energy: float,
    electron_affinity: float,
    missingIsZero=False,
    useNegativeEA=False,
) -> float:
    """
    Return the absolute electronegativity (Mulliken scale), calculated as

    Args:
        ionization_energy: ionization energy
        electron_affinity: electron affinity

    .. math::

        \chi = \\frac{I + A}{2}

    where :math:`I` is the ionization energy and :math:`A` is the electron
    affinity
    """

    if ionization_energy is not None:
        if electron_affinity is not None and electron_affinity < 0.0 and useNegativeEA:
            return (ionization_energy + electron_affinity) * 0.5
        elif electron_affinity is not None or missingIsZero:
            return ionization_energy * 0.5
    else:
        return None


def nagle(nvalence: int, polarizability: float) -> float:
    """
    Calculate the electronegativity of an atom according to the definition
    of Nagle

    Args:
        nvalence: number of valence electrons
        polarizability: dipole polarizability
    """

    return math.pow(nvalence / polarizability, 1.0 / 3.0)


def sanderson(radius: float, noble_gas_radius: float) -> float:
    """Sanderson electronegativity

    Args:
        radius: radius value for the element
        noble_gas_radius: value of the radius of a hypothetical noble gas with
            the atomic number of element for which electronegativity is calculated

    .. math::

        \chi = \\frac{AD}{AD_{\\text{ng}}}

    """

    return math.pow(noble_gas_radius / radius, 3)


def generic(zeff: float, radius: float, rpow=1, apow=1):
    """
    Calculate the electronegativity from a general formula

    .. math::

        \chi = \left(\\frac{Z_{\\text{eff}}}{r^{\\beta}}\\right)^{\\alpha}

    where

    - :math:`Z_{\\text{eff}}` is the effective nuclear charge
    - :math:`r` is the covalent radius
    - :math:`\\alpha,\\beta` parameters
    """

    return math.pow(zeff / math.pow(radius, rpow), apow)
