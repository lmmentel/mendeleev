import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.colors as colors
import matplotlib.cm as cmx

from mendeleev.fetch import fetch_table


def add_tile_coordinates(
    df: pd.DataFrame,
    x_attr: str = "group_id",
    y_attr: str = "period",
    show_fblock: bool = True,
    long_version: bool = False,
) -> pd.DataFrame:
    """
    Calculate coordinates for the tile centers

    Args:
        df: dataframe
        x_attr: attribute to use as x coordinate
        y_attr: attribute to use as y coordinate
        long_version : Show the long version of the periodic table with the f block between
            the s and d blocks
        show_fblock : Show the elements from the f block
    """

    elements = df.copy().sort_values("atomic_number")

    # calculate x and y coordinates of the main group/row elements
    elements.loc[elements[x_attr].notnull(), "x"] = elements.loc[
        elements[x_attr].notnull(), x_attr
    ].astype(int)
    elements.loc[elements[y_attr].notnull(), "y"] = elements.loc[
        elements[y_attr].notnull(), y_attr
    ].astype(int)

    if show_fblock:
        f_mask = elements["block"] == "f"
        elements.loc[f_mask, "x"] = (
            elements[f_mask]
            .groupby("period")
            .apply(lambda x: x["atomic_number"] - x["atomic_number"].min())
            .to_numpy()
            + 3
        )

        if long_version:
            mask = (
                (elements["x"] > 2)
                & (elements["block"] != "f")
                & (~elements["symbol"].isin(["La", "Ac"]))
            )
            elements.loc[f_mask, "x"] += 1
            elements.loc[mask, "x"] = elements.loc[mask, "x"] + 14
            elements.loc[f_mask, "y"] = elements.loc[f_mask, "period"]
        else:
            elements.loc[f_mask, "y"] = elements.loc[f_mask, "period"] + 2.5

    return elements


def create_vis_dataframe(
    x_attr: str = "group_id",
    y_attr: str = "period",
    show_f_block: bool = True,
    long_version: bool = False,
):
    """
    Base DataFrame for visualizations

    Args:
        x_attr: attribute to use as x coordinate
        y_attr: attribute to use as y coordinate
        long_version : Show the long version of the periodic table with the f block between
            the s and d blocks
        show_f_block : Show the elements from the f block
    """
    elements = fetch_table("elements")
    series = fetch_table("series")
    df = pd.merge(
        elements,
        series,
        left_on="series_id",
        right_on="id",
        suffixes=("", "_series"),
    ).sort_values(by="atomic_number")
    return add_tile_coordinates(
        df,
        x_attr=x_attr,
        y_attr=y_attr,
        show_fblock=show_f_block,
        long_version=long_version,
    )


def colormap_column(
    df: pd.DataFrame, column: str, cmap: str = "RdBu_r", missing: str = "#ffffff"
):
    """
    Return a new DataFrame with the same size (and index) as `df` with a column
    `cmap` containing HEX color mapping from `cmap` colormap.

    Args:
        df : DataFrame with the data
        column : Name of the column to be color mapped
        cmap : Name of the colormap, see matplotlib.org
        missing : HEX color for the missing values (NaN or None)
    """

    colormap = plt.get_cmap(cmap)
    cnorm = colors.Normalize(vmin=df[column].min(), vmax=df[column].max())
    scalarmap = cmx.ScalarMappable(norm=cnorm, cmap=colormap)
    out = pd.DataFrame(index=df.index)
    mask = df[column].isnull()
    rgba = scalarmap.to_rgba(df[column])
    out.loc[:, "cmap"] = [colors.rgb2hex(row) for row in rgba]
    out.loc[mask, "cmap"] = missing

    return out
