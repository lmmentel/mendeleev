import pytest
from mendeleev import element, get_all_elements, get_attribute_for_all_elements
from mendeleev.db import get_session
from mendeleev.models import Element


SYMBOLS = get_attribute_for_all_elements("symbol")
NAMES = get_attribute_for_all_elements("name")
ELEMENTS = get_all_elements()


@pytest.fixture
def session():
    return get_session()


def test_query(session):
    si = session.query(Element).filter(Element.symbol == "Si").one()
    assert si.name == "Silicon"


def test_element():
    si = element("Si")
    assert si.name == "Silicon"


def test_incorrect_element():
    with pytest.raises(ValueError, match="Element not found: si"):
        element("si")


@pytest.mark.parametrize("atomic_number", list(range(1, 119)))
def test_elements_get_by_atomic_number(atomic_number):
    e = element(atomic_number)
    assert e.atomic_number == atomic_number


@pytest.mark.parametrize("symbol", SYMBOLS)
def test_elements_get_by_symbol(symbol):
    e = element(symbol)
    assert e.symbol == symbol


@pytest.mark.parametrize("name", NAMES)
def test_elements_get_by_name(name):
    e = element(name)
    assert e.name == name


@pytest.mark.parametrize("symbol", SYMBOLS)
def test_elements_str(symbol):
    e = element(symbol)
    str(e)


@pytest.mark.parametrize("symbol", SYMBOLS)
def test_elements_repr(symbol):
    e = element(symbol)
    repr(e)


@pytest.mark.parametrize("symbol", SYMBOLS)
def test_isotopes_str(symbol):
    e = element(symbol)
    for i in e.isotopes:
        str(i)
        repr(i)


@pytest.mark.parametrize("symbol", SYMBOLS)
def test_electrophilicity(symbol):
    e = element(symbol)
    e.electrophilicity()


@pytest.mark.parametrize("element_obj", ELEMENTS)
def test__eq__(element_obj):
    clone = element(element_obj.symbol)
    assert clone == element_obj


def test__ne__():
    for e1, e2 in zip(ELEMENTS[:-1], ELEMENTS[1:]):
        assert e1 != e2


@pytest.mark.parametrize("e", ELEMENTS)
def test_melting_points_float_or_none(e):
    assert isinstance(e.melting_point, (float, type(None)))


@pytest.mark.parametrize("e", ELEMENTS)
def test_boiling_points_float_or_none(e):
    assert isinstance(e.boiling_point, (float, type(None)))
