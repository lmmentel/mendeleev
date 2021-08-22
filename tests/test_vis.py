import pytest
from mendeleev.fetch import fetch_table
from plotly.graph_objects import Figure as PlotlyFigure
from bokeh.plotting import Figure as BokehFigure
from mendeleev.vis import create_vis_dataframe, add_tile_coordinates
from mendeleev.vis import (
    periodic_table_plotly,
    periodic_table_bokeh,
    heatmap,
    periodic_table,
)


def test_add_tile_coordinates():

    table = fetch_table("elements")
    coords = add_tile_coordinates(table)

    assert "x" in coords.columns
    assert "y" in coords.columns


def test_periodic_table_plotly():

    elements = create_vis_dataframe()
    fig = periodic_table_plotly(elements)

    assert isinstance(fig, PlotlyFigure)


def test_periodic_table_bokeh():

    elements = create_vis_dataframe()
    fig = periodic_table_bokeh(elements)

    assert isinstance(fig, BokehFigure)


def test_periodic_table_seaborn():

    elements = create_vis_dataframe()
    fig = heatmap(elements, "c6")


@pytest.mark.parametrize("attribute", ["atomic_weight", "atomic_radius"])
@pytest.mark.parametrize("colorby", ["color", "jmol_color", "attribute"])
@pytest.mark.parametrize("wide_layout", [False, True])
@pytest.mark.parametrize("backend", ["plotly", "bokeh"])
def test_periodic_table(attribute, colorby, wide_layout, backend):

    fig = periodic_table(
        attribute=attribute, colorby=colorby, wide_layout=wide_layout, backend=backend
    )
