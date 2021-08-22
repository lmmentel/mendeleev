import pandas as pd
import plotly.graph_objects as go
from plotly.graph_objs.layout import Shape, Annotation
from pandas.api.types import is_float_dtype

from .utils import colormap_column


def create_tile(
    element: pd.Series, color: str, x_offset: float = 0.45, y_offset: float = 0.45
) -> Shape:
    """
    Create tile shape
    """
    return Shape(
        type="rect",
        x0=element["x"] - x_offset,
        y0=element["y"] - y_offset,
        x1=element["x"] + x_offset,
        y1=element["y"] + y_offset,
        line=dict(color=element[color]),
        fillcolor=element[color],
        opacity=0.8,
    )


def create_annotation(
    row: pd.Series,
    attr: str,
    size: int = 10,
    x_offset: float = 0.0,
    y_offset: float = 0.0,
) -> Annotation:
    """
    Create an annotation from pandas series
    """
    return Annotation(
        x=row["x"] + x_offset,
        y=row["y"] + y_offset,
        xref="x",
        yref="y",
        text=row[attr],
        showarrow=False,
        font=dict(family="Roboto", size=size, color="#333333"),
        align="center",
        opacity=0.9,
    )


def periodic_table_plotly(
    elements: pd.DataFrame,
    attribute: str = "atomic_weight",
    cmap: str = "RdBu_r",
    colorby: str = "color",
    decimals: int = 3,
    height: int = 800,
    missing: str = "#ffffff",
    title: str = "Periodic Table",
    wide_layout: bool = False,
    width: int = 1200,
) -> go.Figure:
    """
    Create a periodic table visualization with plotly.Figure

    Args:
        elements : Pandas DataFrame with the data about elements
        attribute : Name of the attribute to be displayed
        cmap : Colormap to use, see matplotlib colormaps
        colorby : Name of the column containig the colors
        decimals : Number of decimals to be displayed in the bottom row of each cell
        height : Height of the figure in pixels
        missing : Hex code of the color to be used for the missing values
        title : Title to appear above the periodic table
        wide_layout: wide layout variant of the periodic table
        width : Width of the figure in pixels
    """
    fig = go.Figure()

    if colorby == "attribute":
        colored = colormap_column(elements, attribute, cmap=cmap, missing=missing)
        elements.loc[:, "attribute_color"] = colored
        colorby = "attribute_color"

    # tiles
    tiles = [create_tile(row, color=colorby) for _, row in elements.iterrows()]
    fig.layout["shapes"] += tuple(tiles)

    # symbols
    fig.layout["annotations"] += tuple(
        elements.apply(create_annotation, axis=1, raw=False, args=("symbol",), size=16)
    )

    # atomic_number
    fig.layout["annotations"] += tuple(
        elements.apply(
            create_annotation, axis=1, raw=False, args=("atomic_number",), y_offset=-0.3
        )
    )

    # name
    fig.layout["annotations"] += tuple(
        elements.apply(
            create_annotation, axis=1, raw=False, args=("name",), y_offset=0.2, size=7
        )
    )

    ac = "display_attribute"
    if is_float_dtype(elements[attribute]):
        elements[ac] = elements[attribute].round(decimals=decimals)
    else:
        elements[ac] = elements[attribute]

    # attribute
    fig.layout["annotations"] += tuple(
        elements.apply(
            create_annotation,
            axis=1,
            raw=False,
            args=(ac,),
            y_offset=0.35,
            size=7,
        )
    )

    if wide_layout:
        tickvals = None
        xrange = [0.5, 32.5]
        yrange = [7.5, 0.5]
    else:
        tickvals = tuple(range(1, 19))
        xrange = [0.5, 18.5]
        yrange = [10.0, 0.5]

    fig.update_layout(
        template="plotly_white",
        height=height,
        width=width,
        title=title,
        xaxis={
            "range": xrange,
            "showgrid": False,
            "fixedrange": True,
            "side": "top",
            "tickvals": tickvals,
        },
        yaxis={
            "range": yrange,
            "showgrid": False,
            "fixedrange": True,
            "tickvals": tuple(range(1, 8)),
            "title": "Period",
        },
    )

    return fig