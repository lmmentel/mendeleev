"""
Electronegativity scale formulas.
"""

import math
from typing import List, Union

import numpy as np


# Rydberg constant
RY = 13.605693009


def n_effective(n: int, source: str = "slater") -> Union[float, None]:
    """
    Effective principal quantum number

    Args:
        n: Principal quantum number
        source: either `slater` or `zhang`, for more information see note below.

    .. note::

       Slater's values are taken from J. A. Pople, D. L. Beveridge,
       "Approximate Molecular Orbital Theory", McGraw-Hill, 1970

       Zhang's values are taken from Zhang, Y. (1982). Electronegativities
       of elements in valence states and their applications.
       1. Electronegativities of elements in valence states.
       Inorganic Chemistry, 21(11), 3886–3889. https://doi.org/10.1021/ic00141a005
    """
    numbers = {
        "slater": {1: 1.0, 2: 2.0, 3: 3.0, 4: 3.7, 5: 4.0, 6: 4.2},
        "zhang": {1: 0.85, 2: 1.99, 3: 2.89, 4: 3.45, 5: 3.85, 6: 4.36, 7: 4.99},
    }

    if source in numbers:
        return numbers.get(source).get(n)
    else:
        raise ValueError(
            f"source '{source}' not found, available sources are: {', '.join(numbers.keys())}"
        )


def allred_rochow(zeff: float, radius: float) -> float:
    """
    Calculate the electronegativity of an atom according to the definition
    of Allred and Rochow

    Args:
        zeff: effective nuclear charge
        radius: value of the radius
    """

    return zeff / np.power(radius, 2)


def cottrell_sutton(zeff: float, radius: float) -> float:
    """
    Calculate the electronegativity of an atom according to the definition
    of Allred and Rochow

    Args:
        zeff: effective nuclear charge
        radius: value of the radius
    """

    return np.sqrt(zeff / radius)


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
        charge: Charge of the ion
        radius: Type of radius to be used in the calculation, either `crystal_radius` as recommended in the paper or `ionic_radius`
        valence_pqn: valence principal quantum number
    """

    return (
        n_effective(valence_pqn, source="zhang")
        * math.sqrt(ionization_energy / RY)
        * 100.0
        / radius
    )


def martynov_batsanov(ionization_energies: List[float]) -> float:
    r"""
    Calculates the electronegativity value according to Martynov and
    Batsanov as the average of the ionization energies of the valence
    electrons

    Args:
        ionization_energies: ionization energies for the valence electrons


    .. math::

       \chi_{MB} = \sqrt{\frac{1}{n_{v}}\sum^{n_{v}}_{k=1} I_{k}}

    where:

    - :math:`n_{v}` is the number of valence electrons and
    - :math:`I_{k}` is the :math:`k` th ionization potential.
    """

    return np.sqrt(np.array(ionization_energies).mean())


def mulliken(
    ionization_energy: float,
    electron_affinity: float,
) -> Union[float, None]:
    r"""
    Return the absolute electronegativity (Mulliken scale).

    Args:
        ionization_energy: ionization energy
        electron_affinity: electron affinity

    The value of electonegativity is calculated as:

    .. math::

       \chi = \frac{I + A}{2}

    where:

    - :math:`I` is the ionization energy,
    - :math:`A` is the electron affinity
    """

    if ionization_energy is None:
        return None

    if electron_affinity is None:
        return ionization_energy * 0.5

    return (ionization_energy + electron_affinity) * 0.5


def nagle(nvalence: int, polarizability: float) -> float:
    """
    Calculate the electronegativity of an atom according to the definition
    of Nagle

    Args:
        nvalence: number of valence electrons
        polarizability: dipole polarizability
    """

    return np.power(nvalence / polarizability, 1.0 / 3.0)


def sanderson(radius: float, noble_gas_radius: float) -> float:
    r"""
    Calculate Sanderson's electronegativity

    Args:
        radius: radius value for the element
        noble_gas_radius: value of the radius of a hypothetical noble gas with
        the atomic number of element for which electronegativity is calculated

    .. math::

        \chi = \frac{AD}{AD_{\text{ng}}}

    """

    return math.pow(noble_gas_radius / radius, 3)


def generic(zeff: float, radius: float, rpow: float = 1, apow: float = 1) -> float:
    r"""
    Calculate the electronegativity from a general formula

    Args:
        zeff: effective nuclear charge
        radius: radius value for the element
        rpow: power to raise the radius to (see equation below)
        apow: power to raise the fraction to (see equation below)

    .. math::

        \chi = \left(\frac{Z_{\text{eff}}}{r^{\beta}}\right)^{\alpha}

    where:

    - :math:`Z_{\text{eff}}` is the effective nuclear charge
    - :math:`r` is the covalent radius
    - :math:`\alpha,\beta` parameters
    """

    return np.power(zeff / np.power(radius, rpow), apow)
