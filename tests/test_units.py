import pytest
from pint import Quantity
from mendeleev.models import Element, IonicRadius, IonizationEnergy


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
def element():
    return Element(
        atomic_number=1,
        symbol="H",
        name="Hydrogen",
        atomic_weight=1.008,
        group=1,
        period=1,
        block="s",
        atomic_radius=53.0,
        covalent_radius_pyykko=31.0,
        vdw_radius=120.0,
    )


def test_element_w_units(element):
    """Test that attributes return appropriate Python objects when accessed normally."""
    assert isinstance(element.atomic_radius_u, Quantity)
    assert isinstance(element.covalent_radius_pyykko_u, Quantity)
    assert isinstance(element.vdw_radius_u, Quantity)
    # properties
    # hybrid_properties
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
