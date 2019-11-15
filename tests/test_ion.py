
import pytest
from mendeleev import Ion


def test_H():

    hplus = Ion('He', +1)

    assert hplus.name == 'Hydrogen'
    assert hplus.electrons == 0
    assert hplus.charge == 1
