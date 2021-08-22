from collections import OrderedDict

import pandas as pd
from pandas.api.types import is_float_dtype

from bokeh.plotting import figure
from bokeh.models import HoverTool, ColumnDataSource, FixedTicker

from .utils import colormap_column


def periodic_table_bokeh(
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
):
    """
    Use Bokeh to plot the periodic table data contained in the `df`

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

    # additional columns for positioning of the text

    elements.loc[:, "y_anumber"] = elements["y"] - 0.3
    elements.loc[:, "y_name"] = elements["y"] + 0.2

    if attribute:
        elements.loc[elements[attribute].notnull(), "y_prop"] = (
            elements.loc[elements[attribute].notnull(), "y"] + 0.35
        )
    else:
        elements.loc[:, "y_prop"] = elements["y"] + 0.35

    ac = "display_attribute"
    if is_float_dtype(elements[attribute]):
        elements[ac] = elements[attribute].round(decimals=decimals)
    else:
        elements[ac] = elements[attribute]

    if colorby == "attribute":
        colored = colormap_column(elements, attribute, cmap=cmap, missing=missing)
        elements.loc[:, "attribute_color"] = colored
        colorby = "attribute_color"

    # bokeh configuration

    source = ColumnDataSource(data=elements)

    TOOLS = "hover,save,reset"

    fig = figure(
        title=title,
        tools=TOOLS,
        x_axis_location="above",
        x_range=(elements.x.min() - 0.5, elements.x.max() + 0.5),
        y_range=(elements.y.max() + 0.5, elements.y.min() - 0.5),
        width=width,
        height=height,
        toolbar_location="above",
        toolbar_sticky=False,
    )

    fig.rect("x", "y", 0.9, 0.9, source=source, color=colorby, fill_alpha=0.6)

    # adjust the ticks and axis bounds
    fig.yaxis.bounds = (1, 7)
    fig.axis[1].ticker.num_minor_ticks = 0
    if wide_layout:
        # Turn off tick labels
        fig.axis[0].major_label_text_font_size = "0pt"
        # Turn off tick marks
        fig.axis[0].major_tick_line_color = None  # turn off major ticks
        fig.axis[0].ticker.num_minor_ticks = 0  # turn off minor ticks
    else:
        fig.axis[0].ticker = FixedTicker(ticks=list(range(1, 19)))

    text_props = {
        "source": source,
        "angle": 0,
        "color": "black",
        "text_align": "center",
        "text_baseline": "middle",
    }

    fig.text(
        x="x",
        y="y",
        text="symbol",
        text_font_style="bold",
        text_font_size="15pt",
        **text_props
    )
    fig.text(
        x="x", y="y_anumber", text="atomic_number", text_font_size="9pt", **text_props
    )
    fig.text(x="x", y="y_name", text="name", text_font_size="6pt", **text_props)
    fig.text(x="x", y="y_prop", text=ac, text_font_size="7pt", **text_props)

    fig.grid.grid_line_color = None

    hover = fig.select(dict(type=HoverTool))
    hover.tooltips = OrderedDict(
        [
            ("name", "@name"),
            ("atomic number", "@atomic_number"),
            ("atomic weight", "@atomic_weight"),
            ("EN Pauling", "@en_pauling"),
            ("Electron affinity", "@electron_affinity"),
            ("CPK color", "$color[hex, swatch]:cpk_color"),
            ("Jmol color", "$color[hex, swatch]:jmol_color"),
            ("Molcas GV color", "$color[hex, swatch]:molcas_gv_color"),
            ("electronic configuration", "@electronic_configuration"),
        ]
    )

    return fig
