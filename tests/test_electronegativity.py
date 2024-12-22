import pytest

from mendeleev.models import Element
from mendeleev.electronegativity import mulliken


def test_scales_exception():
    e = Element()
    with pytest.raises(ValueError):
        e.electronegativity(scale="unknown")


def test_mulliken():
    assert mulliken(None, None) is None
    assert mulliken(None, 1.0) is None
    assert mulliken(2.0, None) == pytest.approx(1.0)
    assert mulliken(2.0, 1.0) == pytest.approx(1.5)
