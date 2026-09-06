from mendeleev import isotope
from mendeleev.db import get_session
from mendeleev.models import Isotope


def test_get_isotope():
    # Hydrogen
    result = isotope(1, 1)
    assert result.atomic_number == 1
    assert result.mass_number == 1

    result = isotope("H", 3)
    assert result.atomic_number == 1
    assert result.mass_number == 3


def test_isotope_half_life_u():
    from pint import Quantity

    t = isotope("H", 3).half_life_u
    assert isinstance(t, Quantity)
    assert t.magnitude == 12.32
    assert str(t.units) == "year"


def test_isotope_half_life_u_none():
    assert isotope("H", 1).half_life_u is None


def test_isotopes_half_life_units():
    reference_units = (
        None,
        "asec",
        "day",
        "Eyear",
        "Gyear",
        "hour",
        "kyear",
        "minute",
        "msec",
        "Myear",
        "nsec",
        "psec",
        "Pyear",
        "sec",
        "Tyear",
        "usec",
        "year",
        "ysec",
        "Yyear",
        "zsec",
        "Zyear",
    )

    sess = get_session()
    units = sess.query(Isotope.half_life_unit).distinct().all()
    units = [u[0] for u in units]
    assert set(units) == set(reference_units)
