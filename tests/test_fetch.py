import pytest
import pandas as pd
from mendeleev.fetch import (
    fetch_electronegativities,
    fetch_ionic_radii,
    fetch_ionization_energies,
    fetch_neutral_data,
    fetch_table,
)


tables = [
    ("elements", 118),
    ("isotopes", 3557),
    ("ionicradii", 507),
    ("ionizationenergies", 5847),
    ("groups", 18),
    ("series", 10),
    ("oxidationstates", 579),
    ("phasetransitions", 108),
]


@pytest.mark.parametrize("table,nrows", tables)
def test_fetch_table(table, nrows):
    df = fetch_table(table)
    assert isinstance(df, pd.DataFrame)
    assert df.shape[0] == nrows


def test_fetch_neutral_data():
    df = fetch_neutral_data()
    assert isinstance(df, pd.DataFrame)


@pytest.mark.parametrize("radius", ("ionic_radius", "crystal_radius"))
def test_fetch_ionic_radii(radius):
    df = fetch_ionic_radii(radius)
    assert isinstance(df, pd.DataFrame)


@pytest.mark.parametrize(
    "degree,cols",
    ((1, ["IE1"]), ([1, 2], ["IE1", "IE2"]), ([1, 2, 6], ["IE1", "IE2", "IE6"])),
)
def test_fetch_ionization_energies(degree, cols):
    df = fetch_ionization_energies(degree)
    assert isinstance(df, pd.DataFrame)
    assert all(col in df.columns for col in cols)


def test_fetch_electronegativities():
    df = fetch_electronegativities()
    assert isinstance(df, pd.DataFrame)
