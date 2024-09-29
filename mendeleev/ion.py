"""Module defining the database models for ions."""

from statistics import mean
from typing import List
from mendeleev import element


class Ion:
    """
    Class representating atomic ions
    """

    __element_attributes__ = [
        "atomic_number",
        "block",
        "group",
        "series",
        "period",
        "mass",
        "symbol",
    ]

    def __init__(self, label, q=1):
        self._element = element(label)
        self.q = q

    @property
    def q(self) -> int:
        return self._q

    @q.setter
    def q(self, value: int) -> None:
        if value == 0:
            raise ValueError(f"expecting change other than 0, got {value}")
        elif value > self.Z:
            raise ValueError(
                f"ionic charge ({value}) cannot be larger than atomic number ({self.Z})"
            )
        else:
            self._q = int(value)

    @property
    def Z(self) -> int:
        return self._element.atomic_number

    @property
    def charge(self) -> int:
        return self._q

    @property
    def electrons(self) -> int:
        return self.Z - self.q

    @property
    def name(self) -> str:
        sign = "+" if self.charge > 0 else "-"
        return f"{self._element.name} {self.charge}{sign} ion"

    @property
    def ie(self) -> float:
        return self._element.ionenergies[self.q + 1]

    @property
    def ea(self) -> float:
        return self._element.ionenergies[self.q]

    @property
    def radius(self) -> List[float]:
        return [r for r in self._element.ionic_radii if r.charge == self.charge]

    def unicode_ion_symbol(self) -> str:
        """
        Return a unicode string symbol of the ion
        """
        superscripts = {
            "+": "\u207a",
            "-": "\u207b",
            "0": "\u2070",
            "1": "\u00b9",
            "2": "\u00b2",
            "3": "\u00b3",
            "4": "\u2074",
            "5": "\u2075",
            "6": "\u2076",
            "7": "\u2077",
            "8": "\u2078",
            "9": "\u2079",
        }
        table = str.maketrans(superscripts)
        template = "+" if self.charge > 0 else "-"

        if abs(self.charge) != 1:
            template = str(abs(self.charge)) + template

        return self.symbol + template.translate(table)

    def ionic_potential(self, radius_most_reliable: bool = True) -> float:
        """
        Calculate the ionic potential

        Args:
            radius_most_reliable : flag to use the most reliable ionic radius,
                default is `True`

        """

        if radius_most_reliable:
            radius = mean([r.ionic_radius for r in self.radius if r.most_reliable])
        else:
            radius = mean([r.ionic_radius for r in self.radius])
        return self.q / radius

    def __getattr__(self, name):
        if name in Ion.__element_attributes__:
            return getattr(self._element, name)
        else:
            raise AttributeError(
                f"'{name}' is not an attribute of '{self.__class__.__name__}'"
            )

    def __repr__(self) -> str:
        return self.unicode_ion_symbol()
