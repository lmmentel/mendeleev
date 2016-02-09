
import os
import pandas as pd
import numpy as np

from bokeh.io import curdoc
from bokeh.models import VBox, HBox, Select
from bokeh.plotting import Figure
from bokeh.models import HoverTool, ColumnDataSource, FixedTicker
from bokeh.models.widgets import DataTable, DateFormatter, TableColumn
from collections import OrderedDict

import matplotlib.pyplot as plt
import matplotlib.colors as colors
import matplotlib.cm as cmx

from mendeleev import get_table, periodic_plot, element

def colormap_data(data, cmap='RdBu_r', missing='#ffffff'):
    '''
    Return a new DataFrame with the same size (and index) as `df` with a column
    `cmap` containing HEX color mapping from `cmap` colormap.

    Args:
      data : iterable
        Data to be mapped
      cmap : str
        Name of the colormap, see matplotlib.org
      missing : str
        HEX color for the missing values (NaN or None)
    '''

    try:
        vec = np.array(data, dtype=float)
    except ValueError:
        u, vec = np.unique(data, return_inverse=True)
    colormap = plt.get_cmap(cmap)
    cnorm = colors.Normalize(vmin=np.nanmin(vec), vmax=np.nanmax(vec))
    scalarmap = cmx.ScalarMappable(norm=cnorm, cmap=colormap)
    mask = np.isnan(vec)
    rgba = scalarmap.to_rgba(vec)
    out = np.array([colors.rgb2hex(row) for row in rgba])
    out[mask] = missing
    return out

def get_data():

    elements = get_table('elements')

    en_scales = ['allred-rochow', 'cottrell-sutton', 'gordy', 'martynov-batsanov', 'mulliken', 'nagle', 'sanderson',]
    for scale in en_scales:
        elements['en_' + scale] = [element(row.symbol).electronegativity(scale=scale) for i, row in elements.iterrows()]

    elements.loc[elements['group_id'].notnull(), 'x'] = \
        elements.loc[elements['group_id'].notnull(), 'group_id'].astype(int)
    elements.loc[elements['period'].notnull(), 'y'] = \
        elements.loc[elements['period'].notnull(), 'period'].astype(int)

    for period in [6, 7]:
        mask = (elements['block'] == 'f') & (elements['period'] == period)
        elements.loc[mask, 'x'] = elements.loc[mask, 'atomic_number'] -\
                                        elements.loc[mask, 'atomic_number'].min() + 3
        elements.loc[mask, 'y'] = elements.loc[mask, 'period'] + 2.5

    elements['mass'] = elements['mass'].astype(str)

    # additional columns for positioning of the text

    elements.loc[:, 'y_anumber'] = elements['y'] - 0.3
    elements.loc[:, 'y_name'] = elements['y'] + 0.2
    elements.loc[:, 'y_prop'] = elements['y'] + 0.35


    series = get_table('series')
    groups = get_table('groups')
    elements = pd.merge(elements, series, left_on='series_id', right_on='id',
                suffixes=('', '_series'))

    elements['property'] = ''

    return ColumnDataSource(data=elements)

def make_plot(source, title):

    p = Figure(title=title,
               x_axis_location='above',
               x_range=(0.5, 18.5),
               y_range=(10.0, 0.5),
               plot_width=1000,
               plot_height=800,
               toolbar_location='above',
               tools='hover'
              )

    p.rect("x", "y", 0.9, 0.9, source=source, color='color', fill_alpha=0.6)

    # adjust the ticks and axis bounds
    p.yaxis.bounds = (1, 7)
    p.axis[1].ticker.num_minor_ticks = 0
    p.axis[0].ticker = FixedTicker(ticks=range(1, 19))

    text_props = {
        "source": source,
        "angle": 0,
        "color": "black",
        "text_align": "center",
        "text_baseline": "middle"
    }

    p.text(x="x", y="y", text="symbol",
        text_font_style="bold", text_font_size="15pt", **text_props)

    p.text(x="x", y="y_anumber", text="atomic_number",
        text_font_size="9pt", **text_props)

    p.text(x="x", y="y_name", text="name",
        text_font_size="6pt", **text_props)

    p.text(x="x", y="y_prop", text='property',
        text_font_size="7pt", **text_props)

    p.grid.grid_line_color = None

    hover = p.select(dict(type=HoverTool))
    hover.tooltips = OrderedDict([
        ("symbol", "@symbol"),
        ("name", "@name"),
        ("atomic number", "@atomic_number"),
        ("CPK color", "$color[hex, swatch]:cpk_color"),
        ("Jmol color", "$color[hex, swatch]:jmol_color"),
        ("electronic configuration", "@electronic_configuration"),
        ("lattice structure", "@lattice_structure"),
    ])

    return p

def update_plot(attrname, old, new):

    categ = categ_select.value
    prop = prop_select.value
    cmap = cmap_select.value

    if categ != 'Property':
        plot.title = categories[categ]['title']
        data.data['color'] = colormap_data(data.data[categories[categ]['attrname']], cmap)
    else:
        plot.title = properties[prop]['title']
        data.data['property'] = data.data[properties[prop]['attrname']]
        data.data['color'] = colormap_data(data.data[properties[prop]['attrname']], cmap)
        #source.data.update()

data = get_data()

categattrs = ['block', 'group_id', 'period', 'series_id', 'property']

categories = {a.replace('_id', '').capitalize() : {'attrname' : a, 'title' : 'Periodic table by {}'.format(a.replace('_id', ''))} for a in categattrs}

propattrs = data.column_names

exclude = ['annotation', 'cpk_color', 'description', 'electronic_configuration',
           'jmol_color', 'lattice_structure', 'name', 'color', 'symbol', 'index',
           'id', 'x', 'y', 'y_anumber', 'y_name', 'y_prop',
           'symbol_group', 'name_group', 'name_series', 'color_series']

attrs = list(set(propattrs) - set(exclude) - set(categattrs))

properties = {p.replace('_', ' ') : {'attrname' : p, 'title' : p.replace('_', ' ').title()} for p in attrs}

for k, v in properties.items():
    if v['attrname'].startswith('en_'):
        v['title'] = 'Electronegativity Scale by {}'.format(v['attrname'].replace('en_', '').title().replace('-', ' and '))

prop_select = Select(title='Property:', value='mass', options=sorted(properties.keys()))

cmaps = ['viridis', 'inferno', 'magma', 'plasma'] + sorted(m for m in plt.cm.datad if not m.endswith("_r"))
cmap_select = Select(title='Colormap:', value='viridis', options=cmaps)

categ_select = Select(title='Categories:', value='Series', options=sorted(categories.keys()))
plot = make_plot(data, 'Periodic Table')

prop_select.on_change('value', update_plot)
categ_select.on_change('value', update_plot)
cmap_select.on_change('value', update_plot)


table_columns = [
    TableColumn(field="atomic_number", title="Atomic Number"),
    TableColumn(field="symbol", title="Symbol"),
    TableColumn(field="name", title="Name"),
    TableColumn(field="mass", title="Mass"),
]

data_table = DataTable(source=data, columns=table_columns, width=400, height=280)

controls = VBox(children=[prop_select, categ_select, cmap_select])
plotbox = HBox(children=[controls, plot], width=1200)

# add to document
#curdoc().add_root(HBox(children=[controls, plot], width=1200))
curdoc().add_root(VBox(children=[plotbox, data_table]))
