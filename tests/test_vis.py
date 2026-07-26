import pandas as pd
import pytest
from mendeleev.fetch import fetch_table
from plotly.graph_objects import Figure as PlotlyFigure
from plotly.graph_objs.layout import Shape
from bokeh.plotting import figure as BokehFigure
from mendeleev.vis import create_vis_dataframe, add_tile_coordinates
from mendeleev.vis import (
    periodic_table_plotly,
    periodic_table_bokeh,
    heatmap,
    periodic_table,
)
from mendeleev.vis.plotly import create_tile


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
    heatmap(elements, "c6")


@pytest.mark.parametrize("attribute", ["atomic_weight", "atomic_radius"])
@pytest.mark.parametrize("colorby", ["color", "jmol_color", "attribute"])
@pytest.mark.parametrize("wide_layout", [False, True])
@pytest.mark.parametrize("backend", ["plotly", "bokeh"])
def test_periodic_table(attribute, colorby, wide_layout, backend):
    fig = periodic_table(
        attribute=attribute, colorby=colorby, wide_layout=wide_layout, backend=backend
    )
    if backend == "plotly":
        assert isinstance(fig, PlotlyFigure)
    elif backend == "bokeh":
        assert isinstance(fig, BokehFigure)


class TestCreateTile:
    def _make_element(self, color_value):
        return pd.Series({"x": 5, "y": 3, "color": color_value})

    def test_valid_hex_color(self):
        element = self._make_element("#ff0000")
        tile = create_tile(element, color="color")
        assert isinstance(tile, Shape)
        assert tile.fillcolor == "#ff0000"
        assert tile.line["color"] == "#ff0000"

    def test_nan_color_uses_default(self):
        element = self._make_element(float("nan"))
        tile = create_tile(element, color="color")
        assert tile.fillcolor == "#ffffff"
        assert tile.line["color"] == "#ffffff"

    def test_nan_color_uses_custom_default(self):
        element = self._make_element(float("nan"))
        tile = create_tile(element, color="color", default_color="#cccccc")
        assert tile.fillcolor == "#cccccc"
        assert tile.line["color"] == "#cccccc"

    def test_none_color_uses_default(self):
        element = self._make_element(None)
        tile = create_tile(element, color="color")
        assert tile.fillcolor == "#ffffff"

    def test_tile_shape_bounds(self):
        element = self._make_element("#000000")
        tile = create_tile(element, color="color", x_offset=0.5, y_offset=0.5)
        assert tile.x0 == 4.5
        assert tile.y0 == 2.5
        assert tile.x1 == 5.5
        assert tile.y1 == 3.5
