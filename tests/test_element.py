import pytest
from mendeleev import Element, element, get_all_elements
from mendeleev.db import get_session


ALL_ELEMENTS = {x.symbol: x for x in get_all_elements()}
SYMBOLS = list(ALL_ELEMENTS.keys())
NAMES = [x.name for x in ALL_ELEMENTS.values()]


@pytest.fixture
def session():
    return get_session()


def test_query(session):
    si = session.query(Element).filter(Element.symbol == "Si").one()
    assert si.name == "Silicon"


def test_element():
    si = element("Si")
    assert si.name == "Silicon"


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


def test__eq__():
    elements = get_all_elements()
    for e in elements:
        clone = element(e.symbol)
        assert clone == e


def test__ne__():
    elements = get_all_elements()
    for e1, e2 in zip(elements[:-1], elements[1:]):
        assert e1 != e2
