# -*- coding: utf-8 -*-

"""module specifying the database models"""

from typing import Any, Dict, List, Tuple
from operator import attrgetter

import numpy as np
from sqlalchemy import Column, Boolean, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship, reconstructor
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.hybrid import hybrid_property, hybrid_method

from .electronegativity import (
    allred_rochow,
    cottrell_sutton,
    gordy,
    nagle,
    li_xue,
    martynov_batsanov,
    mulliken,
    sanderson,
)
from .db import get_session
from .econf import ElectronicConfiguration, get_l, ORBITALS
from .utils import coeffs


__all__ = [
    "Element",
    "IonizationEnergy",
    "IonicRadius",
    "OxidationState",
    "Isotope",
    "Series",
    "ScreeningConstant",
]


Base = declarative_base()


class Element(Base):
    """
    Chemical element.

    For full list of available data with references see :doc:`data`.

    Args:
        abundance_crust (float): Abundance in the earth's crust in mg/kg
        abundance_sea (float): Abundance in the seas in mg/L
        annotation (str): Annotations regarding the data
        atomic_number (int): Atomic number
        atomic_radius (float): Atomic radius in pm
        atomic_radius_rahm (float): Atomic radius by Rahm et al. in pm
        atomic_volume (float): Atomic volume in cm3/mol
        atomic_weight (float): Relative atomic weight as the ratio of the average mass of atoms
            of the element to 1/12 of the mass of an atom of 12C
        block (str): Block in periodic table, s, p, d, f
        boiling_point (float): Boiling temperature in K
        c6 (float): C_6 dispersion coefficient in a.u. from X. Chu & A. Dalgarno, J. Chem. Phys.,
            121(9), 4083–4088 (2004) doi:10.1063/1.1779576, and the value for
            Hydrogen was taken from K. T. Tang, J. M. Norbeck and P. R. Certain,
            J. Chem. Phys. 64, 3063 (1976), doi:10.1063/1.432569
        c6_gb (float): C_6 dispersion coefficient in a.u. from Gould, T., & Bučko, T. (2016).
            JCTC, 12(8), 3603–3613. http://doi.org/10.1021/acs.jctc.6b00361
        cas (str): Chemical Abstracts Service identifier
        covalent_radius_bragg (float): Covalent radius in pm from
        covalent_radius_cordero (float): Covalent radius in pm from Cordero, B., Gómez, V., Platero-Prats, A.
            E., Revés, M., Echeverría, J., Cremades, E., … Alvarez, S. (2008).
            Covalent radii revisited. Dalton Transactions, (21), 2832.
            doi:10.1039/b801115j
        covalent_radius_pyykko (float): Single bond covalent radius in pm Pyykkö, P., & Atsumi, M. (2009).
            Molecular Single-Bond Covalent Radii for Elements 1-118.
            Chemistry - A European Journal, 15(1), 186–197.
            doi:10.1002/chem.200800987
        covalent_radius_pyykko_double (float): Double bond covalent radius in pm from P. Pyykkö et al.
        covalent_radius_pyykko_triple (float): Triple bond covalent radius in pm from P. Pyykkö et al.
        cpk_color (str): CPK color of the atom in HEX, see http://jmol.sourceforge.net/jscolors/#color_U
        density (float): Density at 295K in g/cm3
        description (str): Short description of the element
        dipole_polarizability (float): Dipole polarizability in atomic units
        dipole_polarizability_unc (float): Uncertainty of the dipole polarizability
        discoverers (str): The discoverers of the element
        discovery_location (str): The location where the element was discovered
        discovery_year (int): The year the element was discovered
        electron_affinity (float): Electron affinity in eV
        electrophilicity (float): Parr's electrophilicity index
        econf (str): Ground state electron configuration
        evaporation_heat (float): Evaporation heat in kJ/mol
        fusion_heat (float): Fusion heat in kJ/mol
        gas_basicity (float): Gas basicity
        geochemical_class (str): Geochemical classification of the elements
        glawe_number (int): Glawe number (scale)
        goldschmidt_class (str): Goldschmidt classification of the elements
        group_id (int): Group number
        heat_of_formation (float): Heat of formation in kJ/mol
        is_monoisotopic (bool): A flag marking if the element is monoisotopic
        jmol_color (str): Color of the atom as used in Jmol, in HEX,
            see http://jmol.sourceforge.net/jscolors/#color_U
        lattice_constant (float): Lattice constant in ang
        lattice_structure (str): Lattice structure code
        mass (float): Relative atomic mass. Ratio of the average mass of atoms
            of the element to 1/12 of the mass of an atom of 12C
        mendeleev_number (int): Mendeleev number
        melting_point (float): Melting temperature in K
        metallic_radius (float): Single-bond metallic radius or metallic radius, have been
            calculated by Pauling using interatomic distances and an
            equation relating such distances with bond number
        metallic_radius_c12 (float): Metallic radius obtained by Pauling with an assumed number of
            nearest neighbors equal to 12
        molcas_gv_color (str): Color of an atom in HEX from MOLCAS GV http://www.molcas.org/GV/
        name (str): Name in English
        name_origin (str): Origin of the name
        period (int): Period in periodic table
        pettifor_number (int): Pettifor scale
        proton_affinity (Float): Proton affinity
        series (int): Index to chemical series
        sources (str): Sources of the element
        specific_heat (float): Specific heat in J/g mol @ 20 C
        symbol (str): Chemical symbol
        thermal_conductivity (float): Thermal conductivity in @/m K @25 C
        uses (str): Uses of the element
        vdw_radius (float): Van der Waals radius in pm from W. M. Haynes, Handbook of Chemistry and
            Physics 95th Edition, CRC Press, New York, 2014, ISBN-10: 1482208679,
            ISBN-13: 978-1482208672.
        vdw_radius_bondi (float): Van der Waals radius according to Bondi in pm
        vdw_radius_truhlar (float): Van der Waals radius according to Truhlar in pm
        vdw_radius_rt (float): Van der Waals radius according to Rowland and Taylor in pm
        vdw_radius_batsanov (float): Van der Waals radius according to Batsanov in pm
        vdw_radius_dreiding (float): Van der Waals radius from the DREIDING force field in pm
        vdw_radius_uff (float): Van der Waals radius from the UFF in pm
        vdw_radius_mm3 (float): Van der Waals radius from MM3 in pm
        oxistates (list): Oxidation states
        ionenergies (dict): Ionization energies in eV parsed from
            http://physics.nist.gov/cgi-bin/ASD/ie.pl on April 13, 2015
    """

    __tablename__ = "elements"

    abundance_crust = Column(Float)
    abundance_sea = Column(Float)
    annotation = Column(String)
    atomic_number = Column(Integer, primary_key=True)
    atomic_radius = Column(Float)
    atomic_radius_rahm = Column(Float)
    atomic_volume = Column(Float)
    atomic_weight = Column(Float)
    atomic_weight_uncertainty = Column(Float)
    block = Column(String)
    boiling_point = Column(Float)
    cas = Column(String)
    covalent_radius_bragg = Column(Float)
    covalent_radius_cordero = Column(Float)
    covalent_radius_pyykko = Column(Float)
    covalent_radius_pyykko_double = Column(Float)
    covalent_radius_pyykko_triple = Column(Float)
    c6 = Column(Float)
    c6_gb = Column(Float)
    cpk_color = Column(String)
    density = Column(Float)
    description = Column(String)
    dipole_polarizability = Column(Float)
    dipole_polarizability_unc = Column(Float)
    discoverers = Column(String)
    discovery_location = Column(String)
    discovery_year = Column(Integer)
    electron_affinity = Column(Float)
    en_allen = Column(Float)
    en_ghosh = Column(Float)
    en_pauling = Column(Float)
    econf = Column("electronic_configuration", String)
    evaporation_heat = Column(Float)
    fusion_heat = Column(Float)
    gas_basicity = Column(Float)
    geochemical_class = Column(String)
    glawe_number = Column(Integer)
    goldschmidt_class = Column(String)
    group_id = Column(Integer, ForeignKey("groups.group_id"))
    group = relationship("Group", uselist=False, lazy="subquery")
    heat_of_formation = Column(Float)
    is_monoisotopic = Column(Boolean)
    is_radioactive = Column(Boolean)
    jmol_color = Column(String)
    lattice_constant = Column(Float)
    lattice_structure = Column(String)
    melting_point = Column(Float)
    mendeleev_number = Column(Integer)
    metallic_radius = Column(Float)
    metallic_radius_c12 = Column(Float)
    molcas_gv_color = Column(String)
    name = Column(String)
    name_origin = Column(String)
    period = Column(Integer)
    pettifor_number = Column(Integer)
    proton_affinity = Column(Float)
    _series_id = Column("series_id", Integer, ForeignKey("series.id"))
    _series = relationship("Series", uselist=False, lazy="subquery")
    series = association_proxy("_series", "name")
    sources = Column(String)
    specific_heat = Column(Float)
    symbol = Column(String)
    thermal_conductivity = Column(Float)
    uses = Column(String)
    vdw_radius = Column(Float)
    vdw_radius_alvarez = Column(Float)
    vdw_radius_bondi = Column(Float)
    vdw_radius_truhlar = Column(Float)
    vdw_radius_rt = Column(Float)
    vdw_radius_batsanov = Column(Float)
    vdw_radius_dreiding = Column(Float)
    vdw_radius_uff = Column(Float)
    vdw_radius_mm3 = Column(Float)

    ionic_radii = relationship("IonicRadius", lazy="subquery")
    _ionization_energies = relationship("IonizationEnergy", lazy="subquery")
    _oxidation_states = relationship("OxidationState", lazy="subquery")
    isotopes = relationship("Isotope", lazy="subquery")
    screening_constants = relationship("ScreeningConstant", lazy="subquery")

    @reconstructor
    def init_on_load(self):
        "Initialize the ElectronicConfiguration class as attribute of self"

        self.ec = ElectronicConfiguration(self.econf)

    @hybrid_property
    def ionenergies(self) -> Dict[int, float]:
        """
        Return a dict with ionization degree as keys and ionization energies
        in eV as values.
        """

        return {ie.degree: ie.energy for ie in self._ionization_energies}

    @hybrid_property
    def oxistates(self) -> List[int]:
        """Return the oxidation states as a list of ints"""

        return [os.oxidation_state for os in self._oxidation_states]

    @hybrid_property
    def sconst(self) -> Dict[Tuple[int], float]:
        """
        Return a dict with screening constants with tuples (n, s) as keys and
        screening constants as values"""

        return {(x.n, x.s): x.screening for x in self.screening_constants}

    @hybrid_property
    def electrons(self) -> int:
        """Return the number of electrons."""

        return self.atomic_number

    @hybrid_property
    def neutrons(self) -> int:
        """
        Return the number of neutrons of the most abundant natural stable
        isotope.
        """

        return self.mass_number - self.protons

    @hybrid_property
    def protons(self) -> int:
        """Return the number of protons."""

        return self.atomic_number

    @hybrid_property
    def mass(self) -> float:
        """
        Return the `atomic_weight` if defined or mass number otherwise.
        """

        return self.atomic_weight

    @hybrid_property
    def mass_number(self) -> int:
        """
        Return the mass number of the most abundant natural stable isotope
        """

        if len(self.isotopes) <= 0:
            return int(self.atomic_weight)

        lwithabu = [i for i in self.isotopes if i.abundance is not None]
        if lwithabu:
            return max(lwithabu, key=attrgetter("abundance")).mass_number
        else:
            return self.isotopes[0].mass_number

    def mass_str(self) -> str:
        """String representation of atomic weight"""

        if self.atomic_weight_uncertainty is None:
            if self.is_radioactive:
                return "[{aw:.0f}]".format(aw=self.atomic_weight)
            else:
                return "{aw:.3f}".format(aw=self.atomic_weight)
        else:
            dec = np.abs(
                np.floor(np.log10(np.abs(self.atomic_weight_uncertainty)))
            ).astype(int)
            dec = min(dec, 5)
            if self.is_radioactive:
                return "[{aw:.{dec}f}]".format(aw=self.atomic_weight, dec=dec)
            else:
                return "{aw:.{dec}f}".format(aw=self.atomic_weight, dec=dec)

    @hybrid_property
    def covalent_radius(self) -> float:
        """
        Return the default covalent radius which is covalent_radius_pyykko
        """

        return self.covalent_radius_pyykko

    @hybrid_method
    def hardness(self, charge: int = 0) -> float:
        """
        Return the absolute hardness, calculated as

        Args:
          charge:  Charge of the cation for which the hardness will be calculated

        .. math::

           \eta = \\frac{IE - EA}{2}

        where:

        - :math:`IE` is the ionization energy,
        - :math`EA` is the electron affinity

        """

        if charge == 0:
            if (
                self.ionenergies.get(1, None) is not None
                and self.electron_affinity is not None
            ):
                return (self.ionenergies[1] - self.electron_affinity) * 0.5
            else:
                return None
        elif charge > 0:
            if (
                self.ionenergies.get(charge + 1, None) is not None
                and self.ionenergies.get(charge, None) is not None
            ):
                return (self.ionenergies[charge + 1] - self.ionenergies[charge]) * 0.5
            else:
                return None
        elif charge < 0:
            raise ValueError(
                "Charge has to be a non-negative integer, got: {}".format(charge)
            )

    @hybrid_method
    def softness(self, charge: int = 0) -> float:
        """
        Return the absolute softness, calculated as

        Args:
          charge: Charge of the cation for which the hardness will be calculated

        .. math::

           S = \\frac{1}{2\eta}

        where :

        - :math:`\eta` is the absolute hardness

        """

        eta = self.hardness(charge=charge)

        if eta is None:
            return None
        else:
            return 1.0 / (2.0 * eta)

    def zeff(
        self, n: int = None, o: str = None, method: str = "slater", alle: bool = False
    ) -> float:
        """
        Return the effective nuclear charge for ``(n, s)``

        Args:
            method: Method to calculate the screening constant, the choices are

                - `slater`, for Slater's method as in Slater, J. C. (1930).
                    Atomic Shielding Constants. Physical Review, 36(1), 57–64.
                    `doi:10.1103/PhysRev.36.57 <http://www.dx.doi.org/10.1103/PhysRev.36.57>`_
                - `clementi` for values of screening constants from Clementi, E.,
                    & Raimondi, D. L. (1963). Atomic Screening Constants from SCF
                    Functions. The Journal of Chemical Physics, 38(11), 2686.
                    `doi:10.1063/1.1733573 <http://www.dx.doi.org/10.1063/1.1733573>`_
                    and Clementi, E. (1967). Atomic Screening Constants from SCF
                    Functions. II. Atoms with 37 to 86 Electrons. The Journal of
                    Chemical Physics, 47(4), 1300.
                    `doi:10.1063/1.1712084 <http://www.dx.doi.org/10.1063/1.1712084>`_

            n: Principal quantum number

            o: Orbital label, (s, p, d, ...)

            alle: Use all the valence electrons, i.e. calculate screening for an
                extra electron when method='slater', if method='clementi' this
                option is ignored
        """

        # identify the valence s,p vs d,f
        if n is None:
            n = self.ec.max_n()
        elif not isinstance(n, int):
            raise ValueError("<n> should be an integer, got: {}".format(type(n)))

        if o is None:
            # take the shell with max `l` for a given `n`
            o = ORBITALS[max(get_l(x[1]) for x in self.ec.conf.keys() if x[0] == n)]
        elif o not in ORBITALS:
            raise ValueError("<s> should be one of {}".format(", ".join(ORBITALS)))

        if method.lower() == "slater":
            return self.atomic_number - self.ec.slater_screening(n=n, o=o, alle=alle)
        elif method.lower() == "clementi":
            sc = self.sconst.get((n, o), None)
            if sc is not None:
                return self.atomic_number - self.sconst.get((n, o), None)
            else:
                return sc
        else:
            raise ValueError("<method> should be one of {}".format("slater, clementi"))

    def electrophilicity(self) -> float:
        """
        Calculate electrophilicity index

        .. math::

           \\omega = \\frac{\\mu}{2\eta}
        """

        ip = self.ionenergies.get(1, None)
        ea = self.electron_affinity

        if ip is not None and ea is not None:
            return (ip + ea) ** 2 / (8.0 * (ip - ea))
        else:
            return None

    def electronegativity_scales(self, name: str = None) -> List[str]:
        "Available electronegativity scales"

        scales = {
            "allen": self.electronegativity_allen,
            "allred-rochow": self.electronegativity_allred_rochow,
            "cottrell-sutton": self.electronegativity_cottrell_sutton,
            "ghosh": self.electronegativity_ghosh,
            "gordy": self.electronegativity_gordy,
            "li-xue": self.electronegativity_li_xue,
            "martynov-batsanov": self.electronegativity_martynov_batsanov,
            "mulliken": self.electronegativity_mulliken,
            "nagle": self.electronegativity_nagle,
            "pauling": self.electronegativity_pauling,
            "sanderson": self.electronegativity_sanderson,
        }

        if name:
            if name in scales:
                return scales[name]
            else:
                raise ValueError(
                    f"scale: '{name}' not found, available scales are: {', '.join(scales.keys())}"
                )

        return list(sorted(scales.keys()))

    def electronegativity(self, scale: str = "pauling", **kwargs) -> float:
        """
        Calculate the electronegativity using one of the methods

        Args:
            scale : Name of the electronegativity scale, one of
            kwargs: keyword arguments that are passed to compute a specific electronegativity

        """

        return self.electronegativity_scales(name=scale)(**kwargs)

    def electronegativity_allen(self) -> float:
        "Allen's electronegativity"
        return self.en_allen

    def electronegativity_allred_rochow(self, radius="covalent_radius_pyykko") -> float:
        "Allred-Rochow's electronegativity"
        return allred_rochow(self.zeff(), getattr(self, radius))

    def electronegativity_cottrell_sutton(
        self, radius="covalent_radius_pyykko"
    ) -> float:
        "Cottrell-Sutton's electronegativity"
        return cottrell_sutton(self.zeff(), getattr(self, radius))

    def electronegativity_gordy(self, radius="covalent_radius_pyykko") -> float:
        "Gordy's electronegativity"
        return gordy(self.zeff(), getattr(self, radius))

    def electronegativity_ghosh(self) -> float:
        "Ghosh's electronegativity"
        return self.en_ghosh

    def electronegativity_li_xue(
        self, charge: int = 1, radius: str = "crystal_radius"
    ) -> float:
        """
        Calculate the electronegativity of an atom according to the definition
        of Li and Xue

        Args:
            charge : charge of the ion
            radius : type of radius to be used in the calculation, either
                `crystal_radius` as recommended in the paper or `ionic_radius`

        Returns:
            out (dict): dictionary with electronegativities as values and
                coordination string as keys or tuple of coordination and spin
                if the ion is LS or HS
        """

        if (not isinstance(charge, int)) or (charge == 0):
            raise ValueError(
                "charge should be a nonzero initeger, got: {}".format(charge)
            )

        if radius not in ["ionic_radius", "crystal_radius"]:
            raise ValueError(
                f"radius: '{radius}' not found, available values are: 'ionic_radius', 'crystal_radius'"
            )

        ie = self.ionenergies.get(charge, None)

        radii = [
            (ir.coordination, ir.spin, getattr(ir, radius))
            for ir in self.ionic_radii
            if ir.charge == charge
        ]

        return {
            (coordination_number, spin): li_xue(ie, crystal_radius, self.ec.max_n())
            for coordination_number, spin, crystal_radius in radii
        }

    def electronegativity_martynov_batsanov(self) -> float:
        """
        Calculates the electronegativity value according to Martynov and
        Batsanov as the average of the ionization energies of the valence
        electrons

        .. math::

           \chi_{MB} = \sqrt{\\frac{1}{n_{v}}\sum^{n_{v}}_{k=1} I_{k}}

        where:

        - :math:`n_{v}` is the number of valence electrons
        - :math:`I_{k}` is the :math:`k` th ionization potential.

        """

        ionenergies = [
            self.ionenergies.get(i, None)
            for i in range(1, self.nvalence(method="simple") + 1)
        ]

        if all(ionenergies):
            return martynov_batsanov(ionenergies)
        else:
            return None

    def electronegativity_mulliken(
        self,
        charge: int = 0,
        missing_is_zero: bool = False,
        allow_negative_ea: bool = False,
    ) -> float:
        """
        Return the absolute electronegativity (Mulliken scale), calculated as

        Args:
            charge: charge of the ion
            missing_is_zero: missing values are substituted with zero
            allow_negative_ea: if `True` negative EA values will be allowed

        .. math::

           \chi = \\frac{I + A}{2}

        where :math:`I` is the ionization energy and :math:`A` is the electron
        affinity
        """

        if charge == 0:
            ip = self.ionenergies.get(1, None)
            ea = self.electron_affinity
        elif charge > 0:
            ip = self.ionenergies.get(charge + 1, None)
            ea = self.ionenergies.get(charge, None)
        else:
            raise ValueError(
                "Charge has to be a non-negative integer, got: {}".format(charge)
            )
        return mulliken(
            ip, ea, missing_is_zero=missing_is_zero, allow_negative_ea=allow_negative_ea
        )

    def electronegativity_nagle(self) -> float:
        "Nagle's electronegativity"

        if self.dipole_polarizability is not None:
            return nagle(self.nvalence(), self.dipole_polarizability)

    def electronegativity_pauling(self) -> float:
        "Pauling's electronegativity"
        return self.en_pauling

    def electronegativity_sanderson(self, radius="covalent_radius_pyykko") -> float:
        """
        Sanderson electronegativity

        Args:
            radius : radius to use in the calculation
        """
        # estimate the radius of a corresponding noble gas
        noble_gas_radius = estimate_from_group(self.atomic_number, radius)
        return sanderson(getattr(self, radius), noble_gas_radius)

    def nvalence(self, method=None) -> int:
        """
        Return the number of valence electrons
        """

        return self.ec.nvalence(self.block, method=method)

    def oxides(self) -> List[str]:
        """
        Return a lsit of possible oxides based on the oxidation number
        """

        oxide_coeffs = [coeffs(ox) for ox in self.oxistates if ox > 0]
        # convert to strings and replace 1 with empty string
        normal_coeffs = [[str(c) if c != 1 else "" for c in t] for t in oxide_coeffs]
        return [f"{self.symbol}{cme}O{co}" for cme, co in normal_coeffs]

    def __str__(self):
        return "{0} {1} {2}".format(self.atomic_number, self.symbol, self.name)

    def __repr__(self):
        return "%s(\n%s)" % (
            self.__class__.__name__,
            " ".join(
                "\t%s=%r,\n" % (key, getattr(self, key))
                for key in sorted(self.__dict__.keys())
                if not key.startswith("_")
            ),
        )


def fetch_attrs_for_group(attrs: List[str], group: int = 18) -> Tuple[List[Any]]:
    """
    A convenience function for getting a specified attribute for all
    the memebers of a given group.

    Args:
        attr : Attribute of `Element` to retrieve for all group members

    Returns:
        data (dict): Dictionary with noble gas atomic numbers as keys and values of the
            `attr` as values
    """

    session = get_session()
    members = (
        session.query(Element)
        .filter(Element.group_id == group)
        .order_by(Element.atomic_number)
        .all()
    )

    results = tuple([getattr(member, attr) for member in members] for attr in attrs)
    session.close()
    return results


def estimate_from_group(
    atomic_number, attr_name, group: int = 18, deg: int = 1
) -> float:
    """
    Evaluate a value `attribute` for element by interpolation or
    extrapolation of the data points from elements from `group`.

    Args:
        atomic_number: value for which the property will be evaluated
        attr_name: attribute to be estimated
        group: periodic table group number
        deg: degree of the polynomial used in the extrapolation beyond
            the provided data points
    """

    xref, yref = fetch_attrs_for_group(["atomic_number", attr_name], group=group)

    x = atomic_number
    xref = np.array(xref)
    yref = np.array(yref)
    if xref.min() <= x <= xref.max():
        return np.interp([x], xref, yref)

    if x < xref.min():
        xslice = xref[:3]
        yslice = yref[:3]
    elif x > xref.max():
        xslice = xref[-3:]
        yslice = yref[-3:]

    fit = np.polyfit(xslice, yslice, deg)
    fn = np.poly1d(fit)
    return fn(x)


class IonicRadius(Base):
    """
    Effective ionic radii and crystal radii in pm retrieved from [1]_.

    .. [1] Shannon, R. D. (1976). Revised effective ionic radii and systematic
       studies of interatomic distances in halides and chalcogenides. Acta
       Crystallographica Section A.
       `doi:10.1107/S0567739476001551 <http://www.dx.doi.org/10.1107/S0567739476001551>`_

    Args:
        atomic_number (int): Atomic number
        charge (int):  Charge of the ion
        econf (str): Electronic configuration of the ion
        coordination (str): Type of coordination
        spin (str): Spin state: HS - high spin, LS - low spin
        crystal_radius (float): Crystal radius in pm
        ionic_radius (float): Ionic radius in pm
        origin (str): Source of the data
        most_reliable (bool): Most reliable value (see reference)
    """

    __tablename__ = "ionicradii"

    id = Column(Integer, primary_key=True)
    atomic_number = Column(Integer, ForeignKey("elements.atomic_number"))
    charge = Column(Integer)
    econf = Column(String)
    coordination = Column(String)
    spin = Column(String)
    crystal_radius = Column(Float)
    ionic_radius = Column(Float)
    origin = Column(String)
    most_reliable = Column(Boolean)

    def __str__(self):
        out = ["{0}={1:>4d}", "{0}={1:5s}", "{0}={1:>6.3f}", "{0}={1:>6.3f}"]
        keys = ["charge", "coordination", "crystal_radius", "ionic_radius"]
        return ", ".join(o.format(k, getattr(self, k)) for o, k in zip(out, keys))

    def __repr__(self):
        return "%s(\n%s)" % (
            self.__class__.__name__,
            " ".join(
                "\t%s=%r,\n" % (key, getattr(self, key))
                for key in sorted(self.__dict__.keys())
                if not key.startswith("_")
            ),
        )


class IonizationEnergy(Base):
    """
    Ionization energy of an element

    Args:
        atomic_number (int): Atomic number
        degree (int): Degree of ionization with respect to neutral atom
        energy (float): Ionization energy in eV parsed from
            http://physics.nist.gov/cgi-bin/ASD/ie.pl on April 13, 2015
    """

    __tablename__ = "ionizationenergies"

    id = Column(Integer, primary_key=True)
    atomic_number = Column(Integer, ForeignKey("elements.atomic_number"))
    degree = Column(Integer)
    energy = Column(Float)

    def __str__(self):

        return "{0:5d} {1:10.5f}".format(self.degree, self.energy)

    def __repr__(self):

        return "<IonizationEnergy(atomic_number={a:5d}, degree={d:3d}, energy={e:10.5f})>".format(
            a=self.atomic_number, d=self.degree, e=self.energy
        )


class OxidationState(Base):
    """
    Oxidation states of an element

    Args:
      atomic_number (int): Atomic number
      oxidation_state (int): Oxidation state
    """

    __tablename__ = "oxidationstates"

    id = Column(Integer, primary_key=True)
    atomic_number = Column(Integer, ForeignKey("elements.atomic_number"))
    oxidation_state = Column(Integer)

    def __repr__(self):

        return "<OxidationState(atomic_number={a:5d}, oxidation_state={o:5d})>".format(
            a=self.atomic_number, o=self.oxidation_state
        )


class Group(Base):
    """
    Name of the group in the periodic table.

    Args:
        group_id (int): group number
        symbol: (str): group symbol
        name (str): group name
    """

    __tablename__ = "groups"

    group_id = Column(Integer, primary_key=True)
    symbol = Column(String)
    name = Column(String)

    def __repr__(self):

        return "<Group(symbol={s:s}, name={n:s})>".format(s=self.symbol, n=self.name)


class Series(Base):
    """
    Name of the series in the periodic table.

    Args:
        name (str): Name of the series
        color (str): The HEX representation of a color of the series, the colors were
            obtained from `ColorBrewer <http://colorbrewer2.org/?type=qualitative&scheme=Paired&n=10>`_
            the qualitative 10-class paired colormap
    """

    __tablename__ = "series"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    color = Column(String)

    def __repr__(self):

        return "<Series(name={n:s}, color={c:s})>".format(n=self.name, c=self.color)


class Isotope(Base):
    """
    Isotope

    Args:
        abundance (float): Abundance of the isotope
        atomic_number (int): Atomic number
        half_life (float): Half life time
        half_life_unit (str): Unit for the half life time
        is_radioactive (bool): A flag marking wheather the isotope is radioactive
        mass (float): Mass of the isotope
        mass_number (int): Mass number of the isotope
        mass_uncertainty (float): Uncertainty of the mass value
    """

    __tablename__ = "isotopes"

    id = Column(Integer, primary_key=True)
    abundance = Column(Float)
    atomic_number = Column(Integer, ForeignKey("elements.atomic_number"))
    g_factor = Column(Float)
    half_life = Column(Float)
    half_life_unit = Column(String)
    is_radioactive = Column(Boolean)
    mass = Column(Float)
    mass_number = Column(Integer)
    mass_uncertainty = Column(Float)
    spin = Column(Float)
    quadrupole_moment = Column(Float)

    def __str__(self):

        afmt = "5.3f"
        mfmt = "10.5f"

        if self.mass is None:
            mfmt = ""

        if self.abundance is None:
            afmt = ""

        return "{0:5d} {1:5d} {2:{mfmt}} {3:{afmt}}".format(
            self.atomic_number,
            self.mass_number,
            self.mass,
            self.abundance,
            mfmt=mfmt,
            afmt=afmt,
        )

    def __repr__(self):

        return "<Isotope(Z={}, A={}, mass={}, abundance={})>".format(
            self.atomic_number, self.mass_number, self.mass, self.abundance
        )


class ScreeningConstant(Base):
    """
    Nuclear screening constants from Clementi, E., & Raimondi, D. L. (1963).
    Atomic Screening Constants from SCF Functions. The Journal of Chemical
    Physics, 38(11), 2686.  `doi:10.1063/1.1733573
    <http://www.dx.doi.org/10.1063/1.1733573>`_ and Clementi, E. (1967). Atomic
    Screening Constants from SCF Functions. II. Atoms with 37 to 86 Electrons.
    The Journal of Chemical Physics, 47(4), 1300.  `doi:10.1063/1.1712084
    <http://www.dx.doi.org/10.1063/1.1712084>`_

    Args::
        atomic_number (int): Atomic number
        n (int): Principal quantum number
        s (str): Subshell label, (s, p, d, ...)
        screening (float): Screening constant
    """

    __tablename__ = "screeningconstants"

    id = Column(Integer, primary_key=True)
    atomic_number = Column(Integer, ForeignKey("elements.atomic_number"))
    n = Column(Integer)
    s = Column(String)
    screening = Column(Float)

    def __str__(self):

        return "{0:4d} {1:3d} {2:s} {3:10.4f}".format(
            self.atomic_number, self.n, self.s, self.screening
        )

    def __repr__(self):

        return "<ScreeningConstant(Z={0:4d}, n={1:3d}, s={2:s}, screening={3:10.4f})>".format(
            self.atomic_number, self.n, self.s, self.screening
        )
