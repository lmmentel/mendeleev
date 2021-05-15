from mendeleev.fetch import fetch_table
from plotly.graph_objects import Figure
from bokeh.plotting import figure
from mendeleev.vis import create_vis_dataframe, add_tile_coordinates
from mendeleev.vis import (
    periodic_table_plotly,
    periodic_table_bokeh,
    heatmap,
)


def test_add_tile_coordinates():

    table = fetch_table("elements")
    coords = add_tile_coordinates(table)

    assert "x" in coords.columns
    assert "y" in coords.columns


def test_periodic_table_plotly():

    elements = create_vis_dataframe()
    fig = periodic_table_plotly(elements)

    assert isinstance(fig, Figure)


def test_periodic_table_bokeh():

    elements = create_vis_dataframe()
    fig = periodic_table_bokeh(elements)

    assert isinstance(fig, figure)


def test_periodic_table_seaborn():

    elements = create_vis_dataframe()
    fig = heatmap(elements, "c6")

    assert isinstance(fig, Figure)