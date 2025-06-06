import pytest
from pint import Quantity
from mendeleev.models import Element, IonicRadius, IonizationEnergy, Isotope


@pytest.fixture
def ionic_radius():
    """Pytest fixture to create a mock IonicRadius instance with sample data."""
    return IonicRadius(
        id=1,
        atomic_number=11,  # Sodium (Na)
        charge=1,
        econf="[Ne] 3s1",
        coordination="octahedral",
        spin="HS",  # High spin
        crystal_radius=102.0,  # in pm
        ionic_radius=95.0,  # in pm
        origin="Shannon, 1976",
        most_reliable=True,
    )


@pytest.fixture
def ionization_energy():
    """Pytest fixture to create a mock IonizationEnergy instance with sample data."""
    return IonizationEnergy(
        atomic_number=14,
        ground_configuration="3s2.3p2",
        ground_level="3P0",
        ground_shells="[Ne].3s2.3p2",
        id=92,
        ion_charge=0,
        ionization_energy=8.15168,
        ionized_level="3p 2P*<1/2>",
        is_semi_empirical=False,
        is_theoretical=False,
        isoelectonic_sequence="Si",
        references="L5815",
        species_name="Si I",
        uncertainty=3e-05,
    )


@pytest.fixture
def isotope():
    return Isotope(
        atomic_number=1,
        mass=1.00782503189799999,
        abundance=99.9855000000000018,
        mass_number=1,
        mass_uncertainty=1.40000000000000001e-11,
        is_radioactive=0,
        half_life=None,
        half_life_unit=None,
        spin="1/2",
        g_factor=5.58569470199999962,
        quadrupole_moment=0.0,
        parity="+",
        discovery_year=1920,
        g_factor_uncertainty=1.80000000000000023e-08,
        abundance_uncertainty=0.0078000000000000005,
        half_life_uncertainty=None,
        quadrupole_moment_uncertainty=0.0,
    )


@pytest.fixture
def element():
    return Element(
        abundance_crust=1400.0,
        abundance_sea=108000.0,
        atomic_number=1,
        atomic_radius_rahm=154.0,
        atomic_radius=25.0,
        atomic_weight_uncertainty=None,
        atomic_weight=1.008,
        block="s",
        c6_gb=6.50999999999999978,
        c6=6.49902670500000034,
        cas="1333-74-0",
        covalent_radius_bragg=None,
        covalent_radius_cordero=31.0,
        covalent_radius_pyykko_double=None,
        covalent_radius_pyykko_triple=None,
        covalent_radius_pyykko=32.0,
        cpk_color="#ffffff",
        density=8.20000000000000009e-05,
        description="Colourless, odourless gaseous chemical element. Lightest and most abundant element in the universe. Present in water and in all organic compounds. Chemically reacts with most elements. Discovered by Henry Cavendish in 1776.",
        dipole_polarizability_unc=3.00000000000000007e-05,
        dipole_polarizability=4.50710999999999994,
        discoverers="Henry Cavendish",
        discovery_location="England",
        discovery_year=1766,
        electron_affinity=0.754194999999999948,
        en_allen=13.6099999999999994,
        en_ghosh=0.263799999999999978,
        en_gunnarsson_lundqvist=5.74000000000000021,
        en_miedema=5.20000000000000017,
        en_pauling=2.20000000000000017,
        en_robles_bartolotti=5.26999999999999957,
        evaporation_heat=0.904000000000000025,
        fusion_heat=0.117000000000000006,
        gas_basicity=None,
        geochemical_class="volatile",
        glawe_number=103,
        goldschmidt_class="atmophile",
        group_id=1,
        heat_of_formation=217.99799999999999,
        is_monoisotopic=None,
        is_radioactive=0,
        jmol_color="#ffffff",
        lattice_constant=3.75,
        lattice_structure="HEX",
        mendeleev_number=105,
        metallic_radius_c12=78.0,
        metallic_radius=None,
        miedema_electron_density=3.37999999999999989,
        miedema_molar_volume=1.69999999999999995,
        molar_heat_capacity=28.8359999999999985,
        molcas_gv_color="#f2f2f2",
        name_origin="Greek=hydro (water) and genes (generate)",
        name="Hydrogen",
        period=1,
        pettifor_number=103,
        political_stability_of_top_producer=None,
        political_stability_of_top_reserve_holder=None,
        production_concentration=None,
        proton_affinity=None,
        recycling_rate=None,
        relative_supply_risk=None,
        reserve_distribution=None,
        sources="Commercial quantities are produced by reacting superheated steam with methane or carbon. In lab work from reaction of metals with acid solutions or electrolysis.",
        specific_heat_capacity=14.3040000000000002,
        substitutability=None,
        symbol="H",
        thermal_conductivity=0.181499999999999994,
        top_3_producers=None,
        top_3_reserve_holders=None,
        uses="Most hydrogen is used in the production of ammonia. Also used in balloons and in metal refining. Also used as fuel in rockets. Its two heavier isotopes are=deuterium (D) and tritium (T) used respectively for nuclear fission and fusion.",
        vdw_radius_alvarez=120.0,
        vdw_radius_batsanov=None,
        vdw_radius_bondi=120.0,
        vdw_radius_dreiding=319.5,
        vdw_radius_mm3=162.0,
        vdw_radius_rt=110.000000000000014,
        vdw_radius_truhlar=None,
        vdw_radius_uff=288.600000000000022,
        vdw_radius=110.000000000000014,
    )


def test_element_w_units(element):
    """Test that attributes return appropriate Python objects when accessed normally."""
    assert isinstance(element.abundance_crust_u, Quantity)
    assert isinstance(element.abundance_sea_u, Quantity)
    assert isinstance(element.atomic_radius_u, Quantity)
    assert isinstance(element.atomic_weight_u, Quantity)
    assert isinstance(element.covalent_radius_pyykko_u, Quantity)
    assert isinstance(element.specific_heat_capacity_u, Quantity)
    assert isinstance(element.vdw_radius_alvarez_u, Quantity)
    assert isinstance(element.vdw_radius_batsanov_u, (Quantity, type(None)))
    assert isinstance(element.vdw_radius_bondi_u, Quantity)
    assert isinstance(element.vdw_radius_dreiding_u, Quantity)
    assert isinstance(element.vdw_radius_mm3_u, Quantity)
    assert isinstance(element.vdw_radius_rt_u, Quantity)
    assert isinstance(element.vdw_radius_truhlar_u, (Quantity, type(None)))
    assert isinstance(element.vdw_radius_uff_u, Quantity)
    assert isinstance(element.vdw_radius_u, Quantity)
    # properties
    # hybrid_properties
    assert isinstance(element.atomic_volume_u, Quantity)
    assert isinstance(element.boiling_point_u, (Quantity, type(None)))
    assert isinstance(element.melting_point_u, (Quantity, type(None)))
    assert isinstance(element.specific_heat_u, Quantity)
    # methods


def test_normal_attribute_access(ionic_radius):
    """Test that attributes return appropriate Python objects when accessed normally."""
    assert isinstance(ionic_radius.crystal_radius, float)
    assert isinstance(ionic_radius.ionic_radius, float)
    assert isinstance(ionic_radius.charge, int)


def test_unit_attribute_access(ionic_radius):
    """Test that attributes return pint.Quantity when accessed with '_u' suffix."""
    assert isinstance(ionic_radius.crystal_radius_u, Quantity)
    assert isinstance(ionic_radius.ionic_radius_u, Quantity)
    assert isinstance(ionic_radius.charge_u, Quantity)


def test_ionization_energy_wo_units(ionization_energy):
    """Test that attributes return appropriate Python objects when accessed normally."""
    assert isinstance(ionization_energy.ionization_energy, float)
    assert isinstance(ionization_energy.uncertainty, float)
    assert isinstance(ionization_energy.ion_charge, int)


def test_ionization_energy_units(ionization_energy):
    """Test that attributes return appropriate Python objects when accessed normally."""
    assert isinstance(ionization_energy.ionization_energy_u, Quantity)
    assert isinstance(ionization_energy.uncertainty_u, Quantity)
    assert isinstance(ionization_energy.ion_charge_u, Quantity)


def test_isotope_units(isotope):
    """Test that attributes return appropriate Python objects when accessed normally."""
    assert isinstance(isotope.mass_u, Quantity)
    assert isinstance(isotope.mass_uncertainty_u, Quantity)
    assert isinstance(isotope.quadrupole_moment_u, Quantity)
    assert isinstance(isotope.quadrupole_moment_uncertainty_u, Quantity)
