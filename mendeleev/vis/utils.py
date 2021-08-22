import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.colors as colors
import matplotlib.cm as cmx

from mendeleev.fetch import fetch_table


def add_tile_coordinates(
    df: pd.DataFrame,
    x_coord: str = "group_id",
    y_coord: str = "period",
    include_f_block: bool = True,
    wide_layout: bool = False,
) -> pd.DataFrame:
    """
    Calculate coordinates for the tile centers

    Args:
        df: dataframe
        x_coord: attribute to use as x coordinate
        y_coord: attribute to use as y coordinate
        wide_layout : Show the long version of the periodic table with the f block between
            the s and d blocks
        include_f_block : Show the elements from the f block
    """

    elements = df.copy().sort_values("atomic_number")

    # calculate x and y coordinates of the main group/row elements
    elements.loc[elements[x_coord].notnull(), "x"] = elements.loc[
        elements[x_coord].notnull(), x_coord
    ].astype(int)
    elements.loc[elements[y_coord].notnull(), "y"] = elements.loc[
        elements[y_coord].notnull(), y_coord
    ].astype(int)

    if include_f_block:
        f_mask = elements["block"] == "f"
        elements.loc[f_mask, "x"] = (
            elements[f_mask]
            .groupby("period")
            .apply(lambda x: x["atomic_number"] - x["atomic_number"].min())
            .to_numpy()
            + 3
        )

        if wide_layout:
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
    x_coord: str = "group_id",
    y_coord: str = "period",
    include_f_block: bool = True,
    wide_layout: bool = False,
):
    """
    Base DataFrame for visualizations

    Args:
        x_coord: attribute to use as x coordinate
        y_coord: attribute to use as y coordinate
        include_f_block : show the elements from the f block
        wide_layout : show the long version of the periodic table with the f block between
            the s and d blocks

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
        x_coord=x_coord,
        y_coord=y_coord,
        include_f_block=include_f_block,
        wide_layout=wide_layout,
    )


def colormap_column(
    elements: pd.DataFrame, column: str, cmap: str = "RdBu_r", missing: str = "#ffffff"
):
    """
    Return a new DataFrame with the same size (and index) as `elements` with a column
    `cmap` containing HEX color mapping from `cmap` colormap.

    Args:
        elements : DataFrame with the data
        column : Name of the column to be color mapped
        cmap : Name of the colormap, see matplotlib.org
        missing : HEX color for the missing values (NaN or None)
    """

    colormap = plt.get_cmap(cmap)
    cnorm = colors.Normalize(vmin=elements[column].min(), vmax=elements[column].max())
    scalarmap = cmx.ScalarMappable(norm=cnorm, cmap=colormap)

    rgba = scalarmap.to_rgba(elements[column])

    colored = pd.Series(
        index=elements.index, data=[colors.rgb2hex(row) for row in rgba]
    )
    mask = elements[column].isnull()
    colored.loc[mask] = missing

    return colored
