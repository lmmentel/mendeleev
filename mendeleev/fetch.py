import pandas as pd
from sqlalchemy.dialects import sqlite

from mendeleev import element, get_table
from mendeleev import __version__ as version

from .db import get_engine, get_session
from .tables import IonizationEnergy


def get_zeff(an, method="slater") -> float:
    "A helper function to calculate the effective nuclear charge"

    e = element(an)
    return e.zeff(method=method)


def get_neutral_data() -> pd.DataFrame:
    """
    Get extensive set of data from multiple database tables as pandas.DataFrame
    """

    elements = get_table("elements")
    series = get_table("series")
    groups = get_table("groups")

    elements = pd.merge(
        elements,
        series,
        left_on="series_id",
        right_on="id",
        how="left",
        suffixes=("", "_series"),
    )
    elements = pd.merge(
        elements,
        groups,
        left_on="group_id",
        right_on="group_id",
        how="left",
        suffixes=("", "_group"),
    )

    elements.rename(columns={"color": "series_colors"}, inplace=True)

    en_scales = [
        "allred-rochow",
        "cottrell-sutton",
        "gordy",
        "martynov-batsanov",
        "mulliken",
        "nagle",
        "sanderson",
    ]

    for scale in en_scales:
        elements["en_" + scale] = [
            element(row.symbol).electronegativity(scale=scale)
            for i, row in elements.iterrows()
        ]

    for attr in ["hardness", "softness"]:
        elements[attr] = [
            getattr(element(row.symbol), attr)() for i, row in elements.iterrows()
        ]

    elements["mass"] = [
        element(row.symbol).mass_str() for i, row in elements.iterrows()
    ]

    elements.loc[:, "zeff_slater"] = elements.apply(
        lambda x: get_zeff(x["atomic_number"], method="slater"), axis=1
    )
    elements.loc[:, "zeff_clementi"] = elements.apply(
        lambda x: get_zeff(x["atomic_number"], method="clementi"), axis=1
    )

    session = get_session()
    engine = get_engine()

    query = (
        session.query(IonizationEnergy)
        .filter(IonizationEnergy.degree == 1)
        .filter(IonizationEnergy.atomic_number.in_(list(range(1, 119))))
    )
    out = pd.read_sql_query(query.statement.compile(dialect=sqlite.dialect()), engine)
    out = out[["atomic_number", "energy"]]
    out.columns = ["atomic_number", "ionization_energy"]
    elements = pd.merge(elements, out, on="atomic_number", how="left")

    return elements


def add_plot_columns(elements: pd.DataFrame) -> pd.DataFrame:
    """
    Add columns needed for the creating the plots

    Args:
        elements: pd.DataFrame
    """

    mask = elements["group_id"].notnull()

    elements.loc[mask, "x"] = elements.loc[mask, "group_id"].astype(int)
    elements.loc[:, "y"] = elements.loc[:, "period"].astype(int)

    elements.loc[mask, "group_name"] = (
        elements.loc[mask, "group_id"].astype(int).astype(str)
    )
    elements.loc[~mask, "group_name"] = "f block"

    for period in [6, 7]:
        mask = (elements["block"] == "f") & (elements["period"] == period)
        elements.loc[mask, "x"] = (
            elements.loc[mask, "atomic_number"]
            - elements.loc[mask, "atomic_number"].min()
            + 3
        )
        elements.loc[mask, "y"] = elements.loc[mask, "period"] + 2.5

    # additional columns for positioning of the text

    elements.loc[:, "y_symbol"] = elements["y"] - 0.05
    elements.loc[:, "y_anumber"] = elements["y"] - 0.3
    elements.loc[:, "y_name"] = elements["y"] + 0.18

    return elements


def get_app_data():
    "write a file with the neutral data"

    data = get_neutral_data()
    data = add_plot_columns(data)
    fname = "neutral_{0:s}.pkl".format(version)
    data.to_pickle(fname)
    print("wrote file: ", fname)
