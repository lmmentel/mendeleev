# -*- coding: utf-8 -*-

#The MIT License (MIT)
#
#Copyright (c) 2015 Lukasz Mentel
#
#Permission is hereby granted, free of charge, to any person obtaining a copy
#of this software and associated documentation files (the "Software"), to deal
#in the Software without restriction, including without limitation the rights
#to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#copies of the Software, and to permit persons to whom the Software is
#furnished to do so, subject to the following conditions:
#
#The above copyright notice and this permission notice shall be included in all
#copies or substantial portions of the Software.
#
#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#SOFTWARE.

'''tables module'''

import math
import re
from collections import OrderedDict
from operator import attrgetter
import numpy as np

from sqlalchemy import Column, Boolean, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship, reconstructor
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.hybrid import hybrid_property, hybrid_method

import mendeleev

__all__ = ['Element', 'IonizationEnergy', 'IonicRadius', 'OxidationState',
           'Isotope', 'Series', 'ScreeningConstant']

ORBITALS = ('s', 'p', 'd', 'f', 'g', 'h', 'i', 'j', 'k')
SHELLS = ('K', 'L', 'M', 'N', 'O', 'P', 'Q')


def get_l(shell):
    'Return the orbital angular momentum quantum number for a given shell'

    if shell in ORBITALS:
        return ORBITALS.index(shell.lower())
    else:
        raise ValueError('"{}" is not a proper shell label'.format(shell))


Base = declarative_base()


class Element(Base):
    '''
    Chemical element.

    Attributes:
      abundance_crust : float
        Abundance in the earth's crust in mg/kg
      abundance_sea : float
        Abundance in the seas in mg/L
      annotation : str
        Annotations regarding the data
      atomic_number : int
        Atomic number
      atomic_radius : float
        Atomic radius in pm
      atomic_volume : float
        Atomic volume in cm3/mol
      atomic_weight : float
        Relative atomic weight as the ratio of the average mass of atoms
        of the element to 1/12 of the mass of an atom of 12C
      block : int
        Block in periodic table, s, p, d, f
      boiling_point : float
        Boiling temperature in K
      c6 : float
        C_6 dispersion coefficient in a.u. from X. Chu & A. Dalgarno, J. Chem. Phys.,
        121(9), 4083–4088 (2004) doi:10.1063/1.1779576, and the value for
        Hydrogen was taken from K. T. Tang, J. M. Norbeck and P. R. Certain,
        J. Chem. Phys. 64, 3063 (1976), doi:10.1063/1.432569
      c6_gb : float
        C_6 dispersion coefficient in a.u. from Gould, T., & Bučko, T. (2016).
        JCTC, 12(8), 3603–3613. http://doi.org/10.1021/acs.jctc.6b00361
      covalent_radius_bragg : float
        Covalent radius in pm from
      covalent_radius_cordero : float
        Covalent radius in pm from Cordero, B., Gómez, V., Platero-Prats, A.
        E., Revés, M., Echeverría, J., Cremades, E., … Alvarez, S. (2008).
        Covalent radii revisited. Dalton Transactions, (21), 2832.
        doi:10.1039/b801115j
      covalent_radius_pyykko : float
        Covalent radius in pm Pyykkö, P., & Atsumi, M. (2009). Molecular
        Single-Bond Covalent Radii for Elements 1-118. Chemistry - A European
        Journal, 15(1), 186–197. doi:10.1002/chem.200800987
      covalent_radius_slater : float
        Covalent radius in pm from
      cpk_color : str
        CPK color of the atom in HEX,
        see http://jmol.sourceforge.net/jscolors/#color_U
      density : float
        Density at 295K in g/cm3
      description : str
        Short description of the element
      dipole_polarizability : float
        Dipole polarizability in atomic units from P. Schwerdtfeger "Table of
        experimental and calculated static dipole polarizabilities for the
        electronic ground states of the neutral elements (in atomic units)",
        February 11, 2014
      electron_affinity : float
        Electron affinity in eV
      en_allen : float
        Allen's scale of electronegativity (Configurational energy)
      en_ghosh : float
        Ghosh's scale of enectronegativity
      en_pauling : float
        Pauling's scale of electronegativity
      econf : str
        Ground state electron configuration
      evaporation_heat : float
        Evaporation heat in kJ/mol
      fusion_heat : float
        Fusion heat in kJ/mol
      gas_basicity : Float
        Gas basicity
      group : int
        Group in periodic table
      heat_of_formation : float
        Heat of formation in kJ/mol
      is_monoisotopic : bool
        A flag marking if the element is monoisotopic
      jmol_color : str
        Color of the atom as used in Jmol, in HEX,
        see http://jmol.sourceforge.net/jscolors/#color_U
      lattice_constant : float
        Lattice constant in ang
      lattice_structure : str
        Lattice structure code
      mass : float
        Relative atomic mass. Ratio of the average mass of atoms
        of the element to 1/12 of the mass of an atom of 12C
      melting_point : float
        Melting temperature in K
      molcas_gv_color : str
        Color of an atom in HEX from MOLCAS GV http://www.molcas.org/GV/
      name : str
        Name in english
      period : int
        Period in periodic table
      proton_affinity : Float
        Proton affinity
      series : int
        Index to chemical series
      specific_heat : float
        Specific heat in J/g mol @ 20 C
      symbol : str of length 1 or 2
        Chemical symbol
      thermal_conductivity : float
        Thermal conductivity in @/m K @25 C
      vdw_radius : float
        Van der Waals radius in pm from W. M. Haynes, Handbook of Chemistry and
        Physics 95th Edition, CRC Press, New York, 2014, ISBN-10: 1482208679,
        ISBN-13: 978-1482208672.
      vdw_radius_bondi : float
        Van der Waals radius according to Bondi in pm
      vdw_radius_truhlar : float
        Van der Waals radius according to Truhlar in pm
      vdw_radius_rt : float
        Van der Waals radius according to Rowland and Taylor in pm
      vdw_radius_batsanov : float
        Van der Waals radius according to Batsanov in pm
      vdw_radius_dreiding : float
        Van der Waals radius from the DREIDING force field in pm
      vdw_radius_uff : float
        Van der Waals radius from the UFF in pm
      vdw_radius_mm3 : float
        Van der Waals radius from MM3 in pm
      oxistates : list
        Oxidation states
      ionenergy : dict
        Ionization energies in eV parsed from
        http://physics.nist.gov/cgi-bin/ASD/ie.pl on April 13, 2015
    '''

    __tablename__ = 'elements'

    abundance_crust = Column(Float)
    abundance_sea = Column(Float)
    annotation = Column(String)
    atomic_number = Column(Integer, primary_key=True)
    atomic_radius = Column(Float)
    atomic_volume = Column(Float)
    atomic_weight = Column(Float)
    atomic_weight_uncertainty = Column(Float)
    block = Column(String)
    boiling_point = Column(Float)
    covalent_radius_bragg = Column(Float)
    covalent_radius_cordero = Column(Float)
    covalent_radius_pyykko = Column(Float)
    covalent_radius_slater = Column(Float)
    c6 = Column(Float)
    c6_gb = Column(Float)
    cpk_color = Column(String)
    density = Column(Float)
    description = Column(String)
    dipole_polarizability = Column(Float)
    electron_affinity = Column(Float)
    en_allen = Column(Float)
    en_ghosh = Column(Float)
    en_pauling = Column(Float)
    econf = Column('electronic_configuration', String)
    evaporation_heat = Column(Float)
    fusion_heat = Column(Float)
    gas_basicity = Column(Float)
    group_id = Column(Integer, ForeignKey("groups.group_id"))
    group = relationship("Group", uselist=False)
    heat_of_formation = Column(Float)
    is_monoisotopic = Column(Boolean)
    is_radioactive = Column(Boolean)
    jmol_color = Column(String)
    lattice_constant = Column(Float)
    lattice_structure = Column(String)
    melting_point = Column(Float)
    molcas_gv_color = Column(String)
    name = Column(String)
    period = Column(Integer)
    proton_affinity = Column(Float)
    _series_id = Column("series_id", Integer, ForeignKey("series.id"))
    _series = relationship("Series", uselist=False)
    series = association_proxy("_series", "name")
    specific_heat = Column(Float)
    symbol = Column(String)
    thermal_conductivity = Column(Float)
    vdw_radius = Column(Float)
    vdw_radius_alvarez = Column(Float)
    vdw_radius_bondi = Column(Float)
    vdw_radius_truhlar = Column(Float)
    vdw_radius_rt = Column(Float)
    vdw_radius_batsanov = Column(Float)
    vdw_radius_dreiding = Column(Float)
    vdw_radius_uff = Column(Float)
    vdw_radius_mm3 = Column(Float)

    ionic_radii = relationship("IonicRadius")
    _ionization_energies = relationship("IonizationEnergy")
    _oxidation_states = relationship("OxidationState")
    isotopes = relationship("Isotope")
    screening_constants = relationship('ScreeningConstant')

    @reconstructor
    def init_on_load(self):
        'Initialize the ElectronicConfiguration class as attribute of self'

        self.ec = ElectronicConfiguration(self.econf)

    @hybrid_property
    def ionenergies(self):
        '''
        Return a dict with ionization degree as keys and ionization energies
        in eV as values.
        '''

        return {ie.degree: ie.energy for ie in self._ionization_energies}

    @hybrid_property
    def oxistates(self):
        '''Return the oxidation states as a list of ints'''

        return [os.oxidation_state for os in self._oxidation_states]

    @hybrid_property
    def sconst(self):
        '''
        Return a dict with screening constants with tuples (n, s) as keys and
        screening constants as values'''

        return {(x.n, x.s): x.screening for x in self.screening_constants}

    @hybrid_property
    def electrons(self):
        '''Return the number of electrons.'''

        return self.atomic_number

    @hybrid_property
    def neutrons(self):
        '''
        Return the number of neutrons of the most abundant natural stable
        isotope.
        '''

        return self.mass_number - self.protons

    @hybrid_property
    def protons(self):
        '''Return the number of protons.'''

        return self.atomic_number

    @hybrid_property
    def mass(self):
        '''
        Return the `atomic_weight` if defined or mass number otherwise.
        '''

        return self.atomic_weight

    @hybrid_property
    def mass_number(self):
        '''
        Return the mass number of the most abundant natural stable isotope
        '''

        return max(self.isotopes, key=attrgetter("abundance")).mass_number

    @hybrid_property
    def covalent_radius(self):
        '''
        Return the default covalent radius which is covalent_radius_pyykko
        '''

        return self.covalent_radius_pyykko

    @hybrid_method
    def hardness(self, charge=0):
        '''
        Return the absolute hardness, calculated as

        .. math::

           \eta = \\frac{I - A}{2}

        where I is the ionization energy and A is the electron affinity

        Args:
          charge: int
            Charge of the cation for which the hardness will be calculated
        '''

        if charge == 0:
            if self.ionenergies.get(1, None) is not None and self.electron_affinity is not None:
                return (self.ionenergies[1] - self.electron_affinity) * 0.5
            else:
                return None
        elif charge > 0:
            if self.ionenergies.get(charge + 1, None) is not None and\
               self.ionenergies.get(charge, None) is not None:
                return (self.ionenergies[charge + 1] - self.ionenergies[charge]) * 0.5
            else:
                return None
        elif charge < 0:
            raise ValueError('Charge has to be a non-negative integer, got: {}'.format(charge))

    @hybrid_method
    def softness(self, charge=0):
        '''
        Return the absolute softness, calculated as

        .. math::

           S = \\frac{1}{2\eta}

        where :math:`\eta` is the absolute hardness

        Args:
          charge: int
            Charge of the cation for which the hardness will be calculated
        '''

        eta = self.hardness(charge=charge)

        if eta is None:
            return None
        else:
            return 1.0 / (2.0 * eta)

    @hybrid_property
    def exact_mass(self):
        '''Return the mass calculated from isotopic composition.'''

        return sum(iso.mass * iso.abundance for iso in self.isotopes)

    def zeff(self, n=None, o=None, method='slater', alle=False):
        '''
        Return the effective nuclear charge for ``(n, s)``

        Args:
          method : str
            Method to calculate the screening constant, the choices are
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
          n : int
            Principal quantum number
          o : str
            Orbital label, (s, p, d, ...)
          alle : bool
            Use all the valence electrons, i.e. calculate screening for an extra
            electron when method='slater', if method='clementi' this option is
            ignored
        '''

        # identify th valence s,p vs d,f
        if n is None:
            n = self.ec.maxn()
        else:
            if not isinstance(n, int):
                raise ValueError('<n> should be an integer, got: {}'.format(type(n)))

        if o is None:
            # take the shell with max `l` for a given `n`
            o = ORBITALS[max([get_l(x[1]) for x in self.ec.conf.keys() if x[0] == n])]
        else:
            if o not in ORBITALS:
                raise ValueError('<s> should be one of {}'.format(", ".join(ORBITALS)))

        if method.lower() == 'slater':
            return self.atomic_number - self.ec.slater_screening(n=n, o=o,
                                                                 alle=alle)
        elif method.lower() == 'clementi':
            sc = self.sconst.get((n, o), None)
            if sc is not None:
                return self.atomic_number - self.sconst.get((n, o), None)
            else:
                return sc
        else:
            raise ValueError('<method> should be one of {}'.format("slater, clementi"))

    def electronegativity(self, scale='pauling', charge=0):
        '''
        Calculate the electronegativity using one of the methods

        Args:
          scale : str
           Name of the electronegativity scale, one of

           - `allen`
           - `allred-rochow`
           - `cottrell-sutton`
           - `gordy`
           - `li-xue`
           - `martynov-batsanov`
           - `mulliken`
           - `nagle`
           - `pauling`
           - `sanderson`
        '''

        #TODO:
        #        add an option to convert the value to Pauling units
        #        pu : bool
        #            Convert to Pauling's units

        if scale == 'allen':
            return self.en_allen
        elif scale == 'allred-rochow':
            return self.zeff(alle=True)/math.pow(self.covalent_radius, 2)
        elif scale == 'cottrell-sutton':
            return math.sqrt(self.zeff(alle=True)/self.covalent_radius)
        elif scale == 'gordy':
            return self.zeff(alle=True)/self.covalent_radius
        elif scale == 'li-xue':
            return self.en_li_xue(charge=charge)
        elif scale == 'martynov-batsanov':
            return self.en_martynov_batsanov()
        elif scale == 'mulliken':
            return self.en_mulliken()
        elif scale == 'nagle':
            if self.dipole_polarizability is not None:
                return math.pow(self.nvalence()/self.dipole_polarizability, 1.0/3.0)
            else:
                return None
        elif scale == 'pauling':
            return self.en_pauling
        elif scale == 'sanderson':
            return self.calc_en_sanderson()
        else:
            raise ValueError('unknown <scale> value: {}'.format(scale))

    def en_mulliken(self, charge=0, missingIsZero=False, useNegativeEA=False):
        '''
        Return the absolute electronegativity (Mulliken scale), calculated as

        .. math::

           \chi = \\frac{I + A}{2}

        where :math:`I` is the ionization energy and :math:`A` is the electron
        affinity
        '''

        if charge == 0:
            ip = self.ionenergies.get(1, None)
            ea = self.electron_affinity
        elif charge > 0:
            ip = self.ionenergies.get(charge + 1, None)
            ea = self.ionenergies.get(charge, None)
        else:
            raise ValueError('Charge has to be a non-negative integer, got: {}'.format(charge))

        if ip is not None:
            if ea is not None:
                if ea < 0.0 and useNegativeEA:
                    return (ip + ea) * 0.5
                else:
                    return ip * 0.5
            elif ea is None and missingIsZero:
                return ip * 0.5
        else:
            return None

    def en_calc(self, radius='covalent_radius_pyykko', rpow=1, apow=1,
                **zeffkwargs):
        '''
        Calculate the electronegativity from a general formula

        .. math::

           \chi = \left(\\frac{Z_{\\text{eff}}}{r^{\\beta}}\\right)^{\\alpha}

        where

        - :math:`Z_{\\text{eff}}` is the effective nuclear charge
        - :math:`r` is the covalent radius
        - :math:`\\alpha,\\beta` parameters
        '''

        zeff = self.zeff(**zeffkwargs)
        r = getattr(self, radius)

        return math.pow(zeff / math.pow(r, rpow), apow)

    def en_martynov_batsanov(self):
        '''
        Calculates the electronegativity value according to Martynov and
        Batsanov as the average of the ionization energies of the valence
        electrons

        .. math::

           \chi_{MB} = \sqrt{\\frac{1}{n_{v}}\sum^{n_{v}}_{k=1} I_{k}}

        where: :math:`n_{v}` is the number of valence electrons and :math:`I_{k}`
        is the :math:`k` th ionization potential.
        '''

        ionenergies = [self.ionenergies.get(i, None) for i in range(1, self.nvalence(method='simple') + 1)]

        if all(ionenergies):
            return np.sqrt(np.array(ionenergies).mean())
        else:
            return None

    def en_li_xue(self, charge=0, radius='crystal_radius'):
        '''
        Calculate the electronegativity of an atom according to the definition
        of Li and Xue

        Args:
            charge : int
                Charge of the ion
            radius : str
                Type of radius to be used in the calculation, either
                `crystal_radius` as recommended in the paper or `ionic_radius`

        Returns:
            out : dict
                A dictionary with electronegativities as values and
                coordination string as keys or tuple of coordination and spin
                if the ion is LS or HS
        '''

        if charge is None or not isinstance(charge, int) or charge == 0:
            raise ValueError('charge should be a nonzero  initeger')

        neff = {1: 0.85, 2: 1.99, 3: 2.89, 4: 3.45, 5: 3.85, 6: 4.36, 7: 4.99}
        RY = 13.605693009

        if charge == 0:
            Ie = self.electron_affinity
        elif charge > 0:
            Ie = self.ionenergies.get(charge, None)

        crs = [(IR.coordination, IR.spin, getattr(IR, radius)) for IR in self.ionic_radii if IR.charge == charge]

        out = {}
        for coord, spin, cr in crs:
            # the 100.0 factor converts picometers to Angstroms
            eneg = neff[self.ec.maxn()] * math.sqrt(Ie / RY) * 100.0 / cr
            if len(spin) < 1:
                out[coord] = eneg
            else:
                out[(coord, spin)] = eneg

        return out

    def calc_en_sanderson(self, radius='covalent_radius_pyykko'):
        '''Sanderson electronegativity

        .. math::

           \chi = \\frac{AD}{AD_{\\text{ng}}}

        Args:
            radius : str
                Radius to use in the calcualtion
        '''

        r = getattr(self, radius)
        rng = mendeleev.interpolate(self.atomic_number, radius)

        return math.pow(rng / r, 3)

    def nvalence(self, method=None):
        '''Return the number of valence electrons'''

        return self.ec.nvalence(self.block, method=method)

    def mass_str(self):
        '''String representation of atomic weight'''

        if self.atomic_weight_uncertainty is None:
            if self.is_radioactive:
                return '[{aw:.0f}]'.format(aw=self.atomic_weight)
            else:
                return '{aw:.3f}'.format(aw=self.atomic_weight)
        else:
            dec = np.abs(np.floor(np.log10(np.abs(self.atomic_weight_uncertainty)))).astype(int)
            if dec > 5:
                dec = 5
            if self.is_radioactive:
                return '[{aw:.{dec}f}]'.format(aw=self.atomic_weight, dec=dec)
            else:
                return '{aw:.{dec}f}'.format(aw=self.atomic_weight, dec=dec)

    def __str__(self):
        return "{0} {1} {2}".format(self.atomic_number, self.symbol, self.name)

    def __repr__(self):
        return "%s(\n%s)" % (
            (self.__class__.__name__),
            ' '.join(["\t%s=%r,\n" % (key, getattr(self, key))
                      for key in sorted(self.__dict__.keys())
                      if not key.startswith('_')]))


class IonicRadius(Base):
    '''
    Effective ionic radii and crystal radii in pm retrieved from [1].

    .. [1] Shannon, R. D. (1976). Revised effective ionic radii and systematic
       studies of interatomic distances in halides and chalcogenides. Acta
       Crystallographica Section A.
       `doi:10.1107/S0567739476001551 <http://www.dx.doi.org/10.1107/S0567739476001551>`_

    Attributes:
      atomic_number : int
        Atomic number
      charge : int
        Charge of the ion
      econf : str
        Electronic configuration of the ion
      coordination : str
        Type of coordination
      spin : str
        Spin state: HS - high spin, LS - low spin
      crystal_radius : float
        Crystal radius in pm
      ionic_radius : float
        Ionic radius in pm
      origin : str
        Source of the data
      most_reliable : bool
        Most reliable value (see reference)
    '''

    __tablename__ = 'ionicradii'

    id = Column(Integer, primary_key=True)
    atomic_number = Column(Integer, ForeignKey('elements.atomic_number'))
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
        keys = ['charge', 'coordination', 'crystal_radius', 'ionic_radius']
        return ", ".join([o.format(k, getattr(self, k)) for o, k in zip(out, keys)])

    def __repr__(self):
        return "%s(\n%s)" % (
            (self.__class__.__name__),
            ' '.join(["\t%s=%r,\n" % (key, getattr(self, key))
                      for key in sorted(self.__dict__.keys())
                      if not key.startswith('_')]))


class IonizationEnergy(Base):
    '''
    Ionization energy of an element

    Attributes:
      atomic_number : int
        Atomic number
      degree : int
        Degree of ionization with respect to neutral atom
      energy : float
        Ionization energy in eV parsed from
        http://physics.nist.gov/cgi-bin/ASD/ie.pl on April 13, 2015
    '''

    __tablename__ = 'ionizationenergies'

    id = Column(Integer, primary_key=True)
    atomic_number = Column(Integer, ForeignKey('elements.atomic_number'))
    degree = Column(Integer)
    energy = Column(Float)

    def __str__(self):

        return "{1:5d} {2:10.5f}".format(self.degree, self.energy)

    def __repr__(self):

        return "<IonizationEnergy(atomic_number={a:5d}, degree={d:3d}, energy={e:10.5f})>".format(
            a=self.atomic_number, d=self.degree, e=self.energy)


class OxidationState(Base):
    '''
    Oxidation states of an element

    Attributes:
      atomic_number : int
        Atomic number
      oxidation_state : int
        Oxidation state
    '''

    __tablename__ = 'oxidationstates'

    id = Column(Integer, primary_key=True)
    atomic_number = Column(Integer, ForeignKey("elements.atomic_number"))
    oxidation_state = Column(Integer)

    def __repr__(self):

        return "<OxidationState(atomic_number={a:5d}, oxidation_state={o:5d})>".format(
            a=self.atomic_number, o=self.oxidation_state)


class Group(Base):
    '''Name of the group in the periodic table.'''

    __tablename__ = 'groups'

    group_id = Column(Integer, primary_key=True)
    symbol = Column(String)
    name = Column(String)

    def __repr__(self):

        return "<Group(symbol={s:s}, name={n:s})>".format(
            s=self.symbol, n=self.name)


class Series(Base):
    '''
    Name of the series in the periodic table.

    Attributes:
      name : str
        Name of the series
      color : str
        The HEX representation of a color of the series, the colors we obtained
        from `ColorBrewer <http://colorbrewer2.org/?type=qualitative&scheme=Paired&n=10>`_
        the qualitative 10-class paired colormap
    '''

    __tablename__ = 'series'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    color = Column(String)

    def __repr__(self):

        return "<Series(name={n:s}, color={c:s})>".format(n=self.name,
                                                          c=self.color)


class Isotope(Base):
    '''
    Isotope

    Attributes:
      abundance : float
        Abundance of the isotope
      atomic_number : int
        Atomic number
      half_life : float
        Half life time
      half_life_unit : str
        Unit for the half life time
      is_radioactive : bool
        A flag marking wheather the isotope is radioactive
      mass : float
        Mass of the isotope
      mass_number : int
        Mass number of the isotope
      mass_uncertainty : float
        Uncertainty of the mass
    '''

    __tablename__ = "isotopes"

    id = Column(Integer, primary_key=True)
    abundance = Column(Float)
    atomic_number = Column(Integer, ForeignKey("elements.atomic_number"))
    half_life = Column(Float)
    half_life_unit = Column(String)
    is_radioactive = Column(Boolean)
    mass = Column(Float)
    mass_number = Column(Integer)
    mass_uncertainty = Column(Float)

    def __str__(self):

        return "{0:5d} {1:10.5f} {2:6.2f}% {3:5d}".format(
            self.atomic_number, self.mass, self.abundance * 100.0,
            self.mass_number)

    def __repr__(self):

        return "<Isotope(mass={}, abundance={}, mass_number={})>".format(
            self.mass, self.abundance, self.mass_number)


class ScreeningConstant(Base):
    '''
    Nuclear screening constants from Clementi, E., & Raimondi, D. L. (1963).
    Atomic Screening Constants from SCF Functions. The Journal of Chemical
    Physics, 38(11), 2686.  `doi:10.1063/1.1733573
    <http://www.dx.doi.org/10.1063/1.1733573>`_ and Clementi, E. (1967). Atomic
    Screening Constants from SCF Functions. II. Atoms with 37 to 86 Electrons.
    The Journal of Chemical Physics, 47(4), 1300.  `doi:10.1063/1.1712084
    <http://www.dx.doi.org/10.1063/1.1712084>`_

    Attributes:
      atomic_number : int
        Atomic number
      n : int
        Principal quantum number
      s : str
        Subshell label, (s, p, d, ...)
      screening : float
        Screening constant
    '''

    __tablename__ = 'screeningconstants'

    id = Column(Integer, primary_key=True)
    atomic_number = Column(Integer, ForeignKey("elements.atomic_number"))
    n = Column(Integer)
    s = Column(String)
    screening = Column(Float)

    def __str__(self):

        return "{0:4d} {1:3d} {2:s} {3:10.4f}".format(
            self.atomic_number, self.n, self.s, self.screening)

    def __repr__(self):

        return "<ScreeningConstant(Z={0:4d}, n={1:3d}, s={2:s}, screening={3:10.4f})>".format(
            self.atomic_number, self.n, self.s, self.screening)


class ElectronicConfiguration(object):
    '''Electronic configuration handler'''

    def __init__(self, confstr, atomre=None, shellre=None):

        self.noble = {
            'He': '1s2',
            'Ne': '1s2 2s2 2p6',
            'Ar': '1s2 2s2 2p6 3s2 3p6',
            'Kr': '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6',
            'Xe': '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6',
            'Rn': '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f14 5d10 6p6'
        }

        self.confstr = confstr
        self.atomre = atomre
        self.shellre = shellre

        # parse the confstr and initialize core, valence and conf attributes
        self.parse()

    @property
    def atomre(self):
        'Regular expression for atomic symbols'
        return self._atomre

    @atomre.setter
    def atomre(self, value):

        if value is None:
            self._atomre = re.compile(r'\[([A-Z][a-z]*)\]')
        else:
            self._atomre = re.compile(value)

    @property
    def shellre(self):
        'Regular expression for the shell'
        return self._shellre

    @shellre.setter
    def shellre(self, value):

        if value is None:
            self._shellre = re.compile(r'(?P<n>\d)(?P<o>[spdfghijk])(?P<e>\d+)?')
        else:
            self._shellre = re.compile(value)

    def parse(self):
        '''
        Parse a string with electronic configuration into an OrderedDict
        representation
        '''

        citems = self.confstr.split()

        core = {}

        if self.atomre.match(citems[0]):
            symbol = str(self.atomre.match(citems[0]).group(1))
            citems = citems[1:]
            core = [self.shellre.match(o).group('n', 'o', 'e')
                    for o in self.noble[symbol].split() if self.shellre.match(o)]
        valence = [self.shellre.match(o).group('n', 'o', 'e')
                   for o in citems if self.shellre.match(o)]

        self.core = OrderedDict([((int(n), o), (int(e) if e is not None else 1)) for (n, o, e) in core])
        self.valence = OrderedDict([((int(n), o), (int(e) if e is not None else 1)) for (n, o, e) in valence])
        self.conf = OrderedDict(list(self.core.items()) + list(self.valence.items()))

    def sort(self, inplace=True):

        if inplace:
            self.conf = OrderedDict(sorted(self.conf.items(),
                                           key=lambda x: (x[0][0] +
                                           get_l(x[0][1]), x[0][0])))
        else:
            return OrderedDict(sorted(self.conf.items(),
                                      key=lambda x: (x[0][0] + get_l(x[0][1]),
                                      x[0][0])))

    def electrons_per_shell(self):

        return {s: sum([v for k, v in self.conf.items() if k[0] == n])
                for n, s in zip(range(1, self.maxn() + 1), SHELLS)}

    def __repr__(self):

        return self.conf2str(self.conf)

    def __str__(self):

        return self.conf2str(self.conf)

    @staticmethod
    def conf2str(dictlike):

        return " ".join(["{n:d}{s:s}{e:d}".format(n=k[0], s=k[1], e=v)
                         for k, v in dictlike.items()])

    def shell2int(self):

        return [(x[0], get_l(x[1]), x[2]) for x in self.conf]

    def maxn(self):
        'Return the largest value of pricncipal qunatum number for the atom'

        return max([shell[0] for shell in self.conf.keys()])

    def last_subshell(self, wrt='aufbau'):

        if wrt == 'aufbau':
            return sorted(self.conf.items(), key=lambda x: (x[0][0] + get_l(x[0][1]), x[0][0]))[-1]

    def nvalence(self, block, method=None):
        'Return the number of valence electrons'

        if block in ['s', 'p']:
            return sum([v for k, v in self.conf.items() if k[0] == self.maxn()])
        elif block == 'd':
            if method == 'simple':
                return 2
            else:
                return self.conf[(self.maxn(), 's')] + self.conf[(self.maxn() - 1, 'd')]
        elif block == 'f':
            return 2
        else:
            raise ValueError('wrong block: {}'.format(block))

    def slater_screening(self, n, o, alle=False):
        '''
        Calculate the screening constant using the papproach introduced by
        Slater in Slater, J. C. (1930). Atomic Shielding Constants. Physical
        Review, 36(1), 57–64.
        `doi:10.1103/PhysRev.36.57 <http://www.dx.doi.org/10.1103/PhysRev.36.57>`_

        Args:
          n : int
            Principal quantum number
          o : str
            orbtial label, (s, p, d, ...)
          alle : bool
            Use all the valence electrons, i.e. calculate screening for
            an extra electron
        '''

        if alle:
            ne = 0
        else:
            ne = 1

        if n == 1:
            coeff = 0.3
        else:
            coeff = 0.35

        if o in ['s', 'p']:
            # get the number of valence electrons - 1
            vale = float(sum([v for k, v in self.conf.items() if k[0] == n and k[1] in ['s', 'p']]) - ne)
            n1 = sum([v * 0.85 for k, v in self.conf.items() if k[0] == n - 1])
            n2 = sum([float(v) for k, v in self.conf.items() if k[0] in range(1, n - 1)])

        elif o in ['d', 'f']:
            # get the number of valence electrons - 1
            vale = float(sum([v for k, v in self.conf.items() if k[0] == n and k[1] == o]) - ne)
            n1 = sum([float(v) for k, v in self.conf.items() if k[0] == n and k[1] != o])
            n2 = sum([float(v) for k, v in self.conf.items() if k[0] in range(1, n)])

        else:
            raise ValueError('wrong valence subshell: ', o)

        return n1 + n2 + vale * coeff
