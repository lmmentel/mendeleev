import pytest

from mendeleev.models import Element
from mendeleev.electronegativity import (
    n_effective,
    allred_rochow,
    cottrell_sutton,
    gordy,
    li_xue,
    martynov_batsanov,
    mulliken,
    nagle,
    sanderson,
    generic,
)


def test_scales_exception():
    e = Element()
    with pytest.raises(ValueError):
        e.electronegativity(scale="unknown")


def test_mulliken():
    assert mulliken(None, None) is None
    assert mulliken(None, 1.0) is None
    assert mulliken(2.0, None) == pytest.approx(1.0)
    assert mulliken(2.0, 1.0) == pytest.approx(1.5)


def test_n_effective():
    assert n_effective(1, "slater") == pytest.approx(1.0)
    assert n_effective(3, "zhang") == pytest.approx(2.89)
    with pytest.raises(ValueError):
        n_effective(2, "invalid")


def test_allred_rochow():
    assert allred_rochow(4.0, 1.0) == pytest.approx(4.0)
    assert allred_rochow(9.0, 3.0) == pytest.approx(1.0)


def test_cottrell_sutton():
    assert cottrell_sutton(4.0, 1.0) == pytest.approx(2.0)
    assert cottrell_sutton(9.0, 4.0) == pytest.approx(1.5)


def test_gordy():
    assert gordy(6.0, 2.0) == pytest.approx(3.0)
    assert gordy(8.0, 4.0) == pytest.approx(2.0)


def test_li_xue():
    assert li_xue(13.6, 1.0, 1) == pytest.approx(
        n_effective(1, "zhang") * 100.0, rel=1e-1
    )


def test_martynov_batsanov():
    assert martynov_batsanov([13.6, 24.6]) == pytest.approx(4.370354676682432)
    assert martynov_batsanov([10.0, 20.0, 30.0]) == pytest.approx(4.47213595499958)


def test_nagle():
    assert nagle(2, 4.0) == pytest.approx(0.7937005259840998)
    assert nagle(8, 64.0) == pytest.approx(0.5)


def test_sanderson():
    assert sanderson(1.0, 2.0) == pytest.approx(8.0)
    assert sanderson(2.0, 4.0) == pytest.approx(8.0)


def test_generic():
    assert generic(4.0, 2.0, 2, 1) == pytest.approx(1.0)
    assert generic(9.0, 3.0, 2, 0.5) == pytest.approx(1.0)
