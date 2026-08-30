import pytest
from mendeleev.mendeleev import deltaN


def test_deltaN():
    assert isinstance(deltaN("H", "O"), float)
    assert isinstance(deltaN("Na", "Cl"), float)
    assert isinstance(deltaN(11, 17), float)


def test_deltaN_sign_symmetry():
    assert deltaN("O", "H") == pytest.approx(-deltaN("H", "O"))


def test_deltaN_charged():
    # charge1=1 needs IE1 and IE2 of O (both present); H stays neutral
    assert isinstance(deltaN("O", "H", charge1=1), float)


def test_deltaN_missing_hardness_returns_none():
    # Ne has no stored electron affinity, so its hardness is undefined
    assert deltaN("H", "Ne") is None


def test_deltaN_missing_is_zero_false():
    # With missingIsZero=False the Mulliken electronegativity of Ne is None
    assert deltaN("H", "Ne", missingIsZero=False) is None


def test_deltaN_missing_is_zero_default_matches_true():
    assert deltaN("H", "Ne") == deltaN("H", "Ne", missingIsZero=True)
