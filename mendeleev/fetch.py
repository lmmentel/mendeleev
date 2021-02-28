from typing import List, Union

import pandas as pd
from sqlalchemy.dialects import sqlite

from mendeleev import element
from mendeleev import __version__ as version

from .db import get_engine, get_session
from .models import Element, IonizationEnergy


def get_zeff(an, method="slater") -> float:
    "A helper function to calculate the effective nuclear charge"

    e = element(an)
    return e.zeff(method=method)


def fetch_table(table: str, **kwargs) -> pd.DataFrame:
    """
    Return a table from the database as `pandas <http://pandas.pydata.org/>`_
    `DataFrame <http://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.html>`_

    Args:
      table: Name of the table from the database
      kwargs: A dictionary of keyword arguments to pass to the `pandas.read_qsl`

    Returns:
      df: pandas.DataFrame
        Pandas DataFrame with the contents of the table

    Example:
        >>> from mendeleev.fetch import fetch_table
        >>> df = fetch_table('elements')
        >>> type(df)
        pandas.core.frame.DataFrame

    """

    tables = {
        "elements",
        "groups",
        "isotopes",
        "ionicradii",
        "ionizationenergies",
        "oxidationstates",
        "screeningconstants",
        "series",
    }

    if table not in tables:
        raise ValueError(
            f"Table '{table}' not found, available tables are: {', '.join(sorted(tables))}"
        )

    engine = get_engine()
    return pd.read_sql(table, engine, **kwargs)


def fetch_neutral_data() -> pd.DataFrame:
    """
    Get extensive set of data from multiple database tables as pandas.DataFrame
    """

    elements = fetch_table("elements")
    series = fetch_table("series")
    groups = fetch_table("groups")

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


def fetch_ionic_radii(radius: str = "ionic_radius") -> pd.DataFrame:
    """
    Fetch a pandas DataFrame with ionic radii for all the elements.

    Args:
      radius: The radius to be returned either `ionic_radius` or `crystal_radius`

    Returns:
      df: DataFrame
        Pandas DataFrame with atomic numbers, symbols and ionic radii for all
        coordinations
    """

    if radius not in ["ionic_radius", "crystal_radius"]:
        raise ValueError('wrong values, should be "ionic_radius" or "crystal_radius"')

    ir = fetch_table("ionicradii")
    ir = ir[ir.spin != "HS"]
    # create new temporary pseudo multiindex
    ir["idx"] = ir.atomic_number.astype(str) + "(" + ir.charge.astype(str) + ")"
    df = ir.pivot(index="idx", columns="coordination", values="ionic_radius")
    # get back the atomic_number and charge columns from idx
    df["atomic_number"] = df.index.str.extract(r"^(\d+)")
    df["charge"] = df.index.str.extract(r"^\d+\((-?\d+)\)")
    df.reset_index(inplace=True)
    df.drop("idx", axis=1, inplace=True)

    return df


def fetch_ionization_energies(degree: Union[List[int], int] = 1) -> pd.DataFrame:
    """
    Fetch a pandas DataFrame with ionization energies for all elements indexed by atomic_number

    Args:
        degree: Degree of ionization, either as int or a list of ints. If a list is
            passed then the output will contain ionization energies corresponding
            to particalr degrees in columns.

    Returns:
        df: pandas DataFrame with ionization energies, indexed by `index_by`
    """

    # validate degree
    if isinstance(degree, (list, tuple, set)):
        if not all(isinstance(d, int) for d in degree) or any(d <= 0 for d in degree):
            raise ValueError("degree should be a list of positive ints")
    elif isinstance(degree, int):
        if degree <= 0:
            raise ValueError(f"degree should be positive")
        degree = [degree]
    else:
        raise ValueError(
            f"degree should be either a positive int or a collection of positive ints, got: {degree}"
        )

    session = get_session()
    engine = get_engine()

    query = session.query(Element.atomic_number).order_by("atomic_number")
    df = pd.read_sql_query(query.statement.compile(dialect=sqlite.dialect()), engine)

    for d in degree:
        query = session.query(IonizationEnergy).filter(IonizationEnergy.degree == d)
        energies = pd.read_sql_query(
            query.statement.compile(dialect=sqlite.dialect()), engine
        )

        df = pd.merge(
            df,
            energies.loc[:, ["atomic_number", "energy"]].rename(
                columns={"energy": "IE{0:d}".format(d)}
            ),
            on="atomic_number",
            how="left",
        )

    return df.set_index("atomic_number")


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

    data = fetch_neutral_data()
    data = add_plot_columns(data)
    fname = "neutral_{0:s}.pkl".format(version)
    data.to_pickle(fname)
    print("wrote file: ", fname)
