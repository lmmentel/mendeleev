from typing import Union, Tuple
import math


def coeffs(a: int, b: int = 2) -> Tuple[int]:
    """
    Return stoichometric coefficients from oxidation states

    Args:
        a: oxidation state of the first element
        b: oxidation state  of the second element
    """
    lcm = abs(a * b) // math.gcd(a, b)
    return lcm // a, lcm // b


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

    if source not in numbers.keys():
        raise ValueError(
            f"source '{source}' not found, available sources are: {', '.join(numbers.keys())}"
        )

    return numbers.get(source).get(n, None)
