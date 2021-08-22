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