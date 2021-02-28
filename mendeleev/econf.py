"""
Class abstracting the elctronic configuration
"""

from collections import OrderedDict
import math
import re

import six


ORBITALS = ("s", "p", "d", "f", "g", "h", "i", "j", "k")
SHELLS = ("K", "L", "M", "N", "O", "P", "Q")


def get_l(subshell):
    "Return the orbital angular momentum quantum number for a given subshell"

    if subshell.lower() in ORBITALS:
        return ORBITALS.index(subshell.lower())
    else:
        raise ValueError(
            'wrong subshell label: "{}",'.format(subshell)
            + " should be one of: {}".format(", ".join(ORBITALS))
        )


def subshell_degeneracy(subshell):
    "Return the degeneracy of a given subshell"

    return 2 * get_l(subshell) + 1


def subshell_capacity(subshell):
    """
    Return the subshell capacity (max number of electrons)
    """

    return 2 * subshell_degeneracy(subshell)


def shell_capactity(shell):
    """
    Return the shell capacity (max number of electrons)

    The capacity is :math:`N=2n^{2}`, where :math:`n` is the principal
    quantum number.
    """

    if shell.upper() in SHELLS:
        return 2 * (SHELLS.index(shell.upper()) + 1) ** 2
    else:
        raise ValueError(
            'wrong shell label: "{}",'.format(shell)
            + " should be one of: {}".format(", ".join(SHELLS))
        )


class ElectronicConfiguration(object):
    """Electronic configuration handler"""

    noble = OrderedDict(
        [
            ("He", "1s2"),
            ("Ne", "1s2 2s2 2p6"),
            ("Ar", "1s2 2s2 2p6 3s2 3p6"),
            ("Kr", "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6"),
            ("Xe", "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6"),
            ("Rn", "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f14 5d10 6p6"),
        ]
    )

    def __init__(self, conf=None, atomre=None, shellre=None):

        self.atomre = atomre
        self.shellre = shellre
        self.conf = conf

    @property
    def conf(self):
        "Return the configuration"
        return self._conf

    @conf.setter
    def conf(self, value):
        "Setter method for initializing the configuration"

        if isinstance(value, six.string_types):
            self.confstr = value
            self.parse(str(value))
        elif isinstance(value, dict):
            self._conf = OrderedDict(
                sorted(value.items(), key=lambda x: (x[0][0] + get_l(x[0][1]), x[0][0]))
            )
        else:
            raise ValueError("<conf> should be str or dict, got {}".format(type(value)))

    @property
    def atomre(self):
        "Regular expression for atomic symbols"
        return self._atomre

    @atomre.setter
    def atomre(self, value):

        if value is None:
            self._atomre = re.compile(r"\[([A-Z][a-z]*)\]")
        else:
            self._atomre = re.compile(value)

    @property
    def shellre(self):
        "Regular expression for the shell"
        return self._shellre

    @shellre.setter
    def shellre(self, value):

        if value is None:
            self._shellre = re.compile(r"(?P<n>\d)(?P<o>[spdfghijk])(?P<e>\d+)?")
        else:
            self._shellre = re.compile(value)

    def parse(self, string):
        """
        Parse a ``string`` with electronic configuration into an
        ``OrderedDict`` representation
        """

        core = {}
        citems = string.split()

        if self.atomre.match(citems[0]):
            symbol = str(self.atomre.match(citems[0]).group(1))
            citems = citems[1:]
            core = [
                self.shellre.match(o).group("n", "o", "e")
                for o in ElectronicConfiguration.noble[symbol].split()
                if self.shellre.match(o)
            ]
            core = OrderedDict(
                [((int(n), o), (int(e) if e is not None else 1)) for (n, o, e) in core]
            )

        valence = [
            self.shellre.match(o).group("n", "o", "e")
            for o in citems
            if self.shellre.match(o)
        ]
        valence = OrderedDict(
            [((int(n), o), (int(e) if e is not None else 1)) for (n, o, e) in valence]
        )

        self._conf = OrderedDict(list(core.items()) + list(valence.items()))

    def get_largest_core(self):
        """
        Find the largest noble gas core possible for the current
        configuration and return the symbol of the corresponding noble
        gas element.
        """

        confset = set(self.conf.items())

        for s, conf in reversed(ElectronicConfiguration.noble.items()):

            ec = ElectronicConfiguration(conf)
            nobleset = set(ec.conf.items())

            ans = confset.issuperset(nobleset)
            if ans:
                return (s, ec)

    def get_valence(self):
        """
        Find the valence configuration i.e. remove the largest noble gas
        core from the current configuration and return the result.
        """

        _, core_conf = self.get_largest_core()

        valence = OrderedDict(set(self.conf.items()) - set(core_conf.conf.items()))

        return ElectronicConfiguration(valence)

    def sort(self, inplace=True):
        "Sort the occupations OD"
        if inplace:
            self.conf = OrderedDict(
                sorted(
                    self.conf.items(), key=lambda x: (x[0][0] + get_l(x[0][1]), x[0][0])
                )
            )
        else:
            return OrderedDict(
                sorted(
                    self.conf.items(), key=lambda x: (x[0][0] + get_l(x[0][1]), x[0][0])
                )
            )

    def electrons_per_shell(self):
        "Return number of electrons per shell as dict"

        return {
            s: sum(v for k, v in self.conf.items() if k[0] == n)
            for n, s in zip(range(1, self.max_n() + 1), SHELLS)
        }

    def shell2int(self):
        "configuration as list of tuples (n, l, e)"
        return [(x[0], get_l(x[1]), x[2]) for x in self.conf]

    def max_n(self):
        "Return the largest value of principal quantum number for the atom"

        return max(shell[0] for shell in self.conf.keys())

    def max_l(self, n):
        """
        Return the largest value of azimutal quantum number for a given
        value of principal quantum number

        Args:
            n : int
                Principal quantum number
        """

        return ORBITALS[max(get_l(x[1]) for x in self.conf.keys() if x[0] == n)]

    def last_subshell(self, wrt="order"):
        "Return the valence shell"

        if wrt.lower() == "order":
            return list(self.conf.items())[-1]
        elif wrt.lower() == "aufbau":
            return sorted(
                self.conf.items(), key=lambda x: (x[0][0] + get_l(x[0][1]), x[0][0])
            )[-1]
        else:
            raise ValueError("wrong <wrt>: {}".format(wrt))

    def nvalence(self, block, method=None):
        "Return the number of valence electrons"

        if block in ["s", "p"]:
            return sum(v for k, v in self.conf.items() if k[0] == self.max_n())
        elif block == "d":
            if method == "simple":
                return 2
            else:
                return (
                    self.conf[(self.max_n(), "s")] + self.conf[(self.max_n() - 1, "d")]
                )
        elif block == "f":
            return 2
        else:
            raise ValueError("wrong block: {}".format(block))

    def ne(self):
        "Return the number of electrons"

        return sum(list(self.conf.values()))

    def unpaired_electrons(self):
        "Return the number of unpaired electrons"

        so = self.spin_occupations()

        return sum(v["unpaired"] for v in so.values())

    def ionize(self, n=1):
        """
        Remove `n` electrons from and return a new `ElectronicConfiguration`
        object"""

        newec = ElectronicConfiguration(str(self.__str__()))

        for _ in range(n):

            if not newec.conf:
                raise ValueError("Cannot ionize further, no more electrons!")

            (n, o), ne = newec.last_subshell()

            if ne > 1:
                newec.conf[(n, o)] = ne - 1
            elif ne == 1:
                newec.conf.pop((n, o))

        return newec

    def spin_occupations(self):
        """
        For each subshell calculate the number of `alpha`, `beta` electrons,
        electron pairs and unpaired electrons
        """

        so = OrderedDict()

        for (n, orb), nele in self.conf.items():

            ssc = subshell_capacity(orb)
            ssd = subshell_degeneracy(orb)

            if nele == ssc:
                so[(n, orb)] = {"pairs": ssd, "alpha": ssd, "beta": ssd, "unpaired": 0}
            else:
                pairs = (nele % ssd) * (nele // ssd)
                alpha = nele - pairs
                beta = nele - alpha
                unpaired = nele - pairs * 2

                so[(n, orb)] = {
                    "pairs": pairs,
                    "alpha": alpha,
                    "beta": beta,
                    "unpaired": unpaired,
                }

        return so

    def spin_only_magnetic_moment(self):
        """
        Return the magnetic moment insluding only spin of the electrons
        and not the angular momentum
        """

        ue = self.unpaired_electrons()

        return math.sqrt(ue * (ue + 2))

    def slater_screening(self, n, o, alle=False):
        """
        Calculate the screening constant using the approach introduced by
        Slater in Slater, J. C. (1930). Atomic Shielding Constants. Physical
        Review, 36(1), 57-64.
        `doi:10.1103/PhysRev.36.57 <http://www.dx.doi.org/10.1103/PhysRev.36.57>`_

        Args:
          n : int
            Principal quantum number
          o : str
            orbtial label, (s, p, d, ...)
          alle : bool
            Use all the valence electrons, i.e. calculate screening for
            an extra electron
        """

        ne = 0 if alle else 1
        coeff = 0.3 if n == 1 else 0.35
        if o in ["s", "p"]:
            # get the number of valence electrons - 1
            vale = float(
                sum(v for k, v in self.conf.items() if k[0] == n and k[1] in ["s", "p"])
                - ne
            )
            n1 = sum(v * 0.85 for k, v in self.conf.items() if k[0] == n - 1)
            n2 = sum(float(v) for k, v in self.conf.items() if k[0] in range(1, n - 1))

        elif o in ["d", "f"]:
            # get the number of valence electrons - 1
            vale = float(
                sum(v for k, v in self.conf.items() if k[0] == n and k[1] == o) - ne
            )

            n1 = sum(float(v) for k, v in self.conf.items() if k[0] == n and k[1] != o)
            n2 = sum(float(v) for k, v in self.conf.items() if k[0] in range(1, n))

        else:
            raise ValueError("wrong valence subshell: ", o)

        return n1 + n2 + vale * coeff

    def to_str(self):
        "Return a string with the configuration"

        return " ".join(
            "{n:d}{s:s}{e:d}".format(n=k[0], s=k[1], e=v) for k, v in self.conf.items()
        )

    def __repr__(self):

        return '<ElectronicConfiguration(conf="{}")>'.format(self.to_str())

    def __str__(self):

        return self.to_str()


def get_spin_strings(sodict, average=True):
    """
    spin strings as numpy arrays

    This should be called for valence only
    """

    alphas = []
    betas = []

    for (n, orb), occ in sodict.items():
        nss = subshell_degeneracy(orb)
        if average:
            alphas.extend([occ["alpha"] / nss] * nss)
            betas.extend([occ["beta"] / nss] * nss)
        else:
            alphas.extend([1.0] * occ["alpha"] + [0.0] * (nss - occ["alpha"]))
            betas.extend([1.0] * occ["beta"] + [0.0] * (nss - occ["beta"]))
    return alphas, betas


def print_spin_occupations(sodict, average=True):
    "Pretty format for the spin occupations"

    alphas = []
    betas = []

    for (n, orb), occ in sodict.items():
        nss = subshell_degeneracy(orb)
        if average:
            fmt = "10.8f"
            a = ", ".join(
                "{0:{fmt}}".format(x, fmt=fmt) for x in [occ["alpha"] / nss] * nss
            )

            b = ", ".join(
                "{0:{fmt}}".format(x, fmt=fmt) for x in [occ["beta"] / nss] * nss
            )

        else:
            a = ", ".join(
                "{0:3.1f}".format(x)
                for x in [1] * occ["alpha"] + [0] * (nss - occ["alpha"])
            )

            b = ", ".join(
                "{0:3.1f}".format(x)
                for x in [1] * occ["beta"] + [0] * (nss - occ["beta"])
            )

        alphas.append(a)
        betas.append(b)
        print("{} alpha: ".format(orb), a)
        print("{} beta : ".format(orb), b)
    return alphas, betas
