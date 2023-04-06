from mendeleev.vis.bokeh import periodic_table_bokeh
from mendeleev.vis.plotly import periodic_table_plotly
from mendeleev.vis.utils import create_vis_dataframe


def periodic_table(
    attribute: str = "atomic_weight",
    height: int = 800,
    width: int = 1200,
    decimals: int = 3,
    colorby: str = "color",
    missing: str = "#ffffff",
    title: str = "Periodic Table",
    cmap: str = "RdBu_r",
    wide_layout: bool = False,
    include_f_block: bool = True,
    backend="plotly",
):
    """High level api for visualizing periodic tables.

    Currently supports plotting backends:
        - bokeh
        - plotly

    Args:
        attribute (str, optional): Name of the attribute to display. Defaults to "atomic_weight".
        height (int, optional): Height of the figure in pixels. Defaults to 800.
        width (int, optional): Width of the figure in pixels. Defaults to 1200.
        decimals (int, optional): Number of decimals to be displayed for `attribute`. Defaults to 3.
        colorby (str, optional): Name of the columns that contains color values. Defaults to "color".
        missing (str, optional): Hex code for the color to be used for missing values. Defaults to "#ffffff".
        title (str, optional): Title. Defaults to "Periodic Table".
        cmap (str, optional): Colormap name. Defaults to "RdBu_r".
        wide_layout (bool, optional): If `True` wide layout is used with *f* block
            between *s* and *d* blocks. Defaults to False.
        include_f_block (bool, optional): Flag indicating whether to include the _f_ block. Defaults to True.
        backend (str, optional): Plotting backennd. Defaults to "plotly".

    Raises:
        ValueError: upon specifying unsupported ploting backend.

    Returns:
        fig: figure instance, either `plotly.Figure` or `bokeh.plotting.figure`
    """
    elements = create_vis_dataframe(
        include_f_block=include_f_block, wide_layout=wide_layout
    )

    backends = {
        "plotly": periodic_table_plotly,
        "bokeh": periodic_table_bokeh,
    }

    if backend not in backends:
        raise ValueError(f"unsupported plotting backend: {backend}")

    plotter = backends[backend]
    return plotter(
        elements,
        attribute=attribute,
        height=height,
        width=width,
        decimals=decimals,
        colorby=colorby,
        missing=missing,
        title=title,
        cmap=cmap,
        wide_layout=wide_layout,
    )
