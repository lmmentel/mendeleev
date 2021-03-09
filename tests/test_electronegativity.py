import pytest

from mendeleev import Element


def test_scales_exception():

    e = Element()
    with pytest.raises(ValueError):
        e.electronegativity(scale="unknown")