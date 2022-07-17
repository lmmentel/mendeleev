import pytest
from pytest import approx
from mendeleev import element
from mendeleev.ion import Ion


@pytest.mark.parametrize("atomic_number", list(range(1, 119)))
def test_inherited_attrs(atomic_number):
    """
    Check if properties inherited from Element are properly passed on
    """

    elm = element(atomic_number)
    ion = Ion(atomic_number)

    assert ion.charge == ion.q
    assert ion.Z == ion.atomic_number == elm.atomic_number
    assert ion.electrons == ion.Z - ion.charge

    for attr in Ion.__element_attributes__:
        if attr != "group":
            assert getattr(elm, attr) == getattr(ion, attr)


@pytest.fixture
def he():
    return Ion("He", 1)


@pytest.fixture
def fe2():
    return Ion("Fe", 2)


def test_basic_he_properties(he):
    assert he.symbol == "He"
    assert he.name == "Helium 1+ ion"
    assert he.charge == 1
    assert he.electrons == 1


def test_zero_charge():
    with pytest.raises(ValueError):
        Ion("He", 0)


def test_charge_too_large():
    with pytest.raises(ValueError):
        Ion("He", 3)


def test_forbidden_attribute(he):
    with pytest.raises(AttributeError):
        getattr(he, "electronegativity")


def test_ionic_potential(fe2):
    assert fe2.ionic_potential() == approx(2 / 78.0)
    assert fe2.ionic_potential(radius_most_reliable=False) == approx(2 / 71.6)


def test_ea(fe2):
    assert approx(fe2.ea) == 16.1992


def test_ie(fe2):
    assert approx(fe2.ie) == 30.651


def test_repr(fe2):
    assert repr(fe2) == "Fe²⁺"
    assert str(fe2) == "Fe²⁺"
