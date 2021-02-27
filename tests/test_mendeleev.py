from mendeleev import get_table
import pytest


expected = [
    ("elements", 118),
    ("isotopes", 406),
    ("ionicradii", 507),
    ("ionizationenergies", 5837),
    ("groups", 18),
    ("series", 10),
    ("oxidationstates", 231),
]


@pytest.mark.parametrize("table_name,nrows", expected)
def test_get_table(table_name, nrows):

    table = get_table(table_name)
    assert table.shape[0] == nrows
