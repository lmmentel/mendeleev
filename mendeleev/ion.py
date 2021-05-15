from statistics import mean
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
    def q(self):
        return self._q

    @q.setter
    def q(self, value):
        if value == 0:
            raise ValueError("expecting change other than 0, got {}".format(value))
        elif value > self.Z:
            raise ValueError(
                "ionic charge ({}) cannot be larger than atomic number ({})".format(
                    value, self.Z
                )
            )
        else:
            self._q = int(value)

    @property
    def Z(self):
        return self._element.atomic_number

    @property
    def charge(self):
        return self._q

    @property
    def electrons(self):
        return self.Z - self.q

    @property
    def name(self):
        sign = "+" if self.charge > 0 else "-"
        return "{} {}{} ion".format(self._element.name, self.charge, sign)

    @property
    def ie(self):
        return self._element.ionenergies[self.q + 1]

    @property
    def ea(self):
        return self._element.ionenergies[self.q]

    @property
    def radius(self):
        return [r for r in self._element.ionic_radii if r.charge == self.charge]

    def unicode_ion_symbol(self) -> str:
        """
        Return a unicode string symbol of the ion
        """

        superscripts = {
            "+": u"\u207A",
            "-": u"\u207B",
            "0": u"\u2070",
            "1": u"\u00B9",
            "2": u"\u00B2",
            "3": u"\u00B3",
            "4": u"\u2074",
            "5": u"\u2075",
            "6": u"\u2076",
            "7": u"\u2077",
            "8": u"\u2078",
            "9": u"\u2079",
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
                "'{}' is not an attribute of '{}'".format(name, self.__class__.__name__)
            )

    def __repr__(self):
        return self.unicode_ion_symbol()
