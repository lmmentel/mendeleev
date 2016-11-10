# -*- coding: utf-8 -*-

#The MIT License (MIT)
#
#Copyright (c) 2015 Lukasz Mentel
#
#Permission is hereby granted, free of charge, to any person obtaining a copy
#of this software and associated documentation files (the "Software"), to deal
#in the Software without restriction, including without limitation the rights
#to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#copies of the Software, and to permit persons to whom the Software is
#furnished to do so, subject to the following conditions:
#
#The above copyright notice and this permission notice shall be included in all
#copies or substantial portions of the Software.
#
#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#SOFTWARE.

import seaborn as sns
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.colors as colors
import matplotlib.cm as cmx
from bokeh.plotting import figure, show, output_file
from bokeh.models import HoverTool, ColumnDataSource, FixedTicker
from collections import OrderedDict
from .mendeleev import get_table


def heatmap(prop, style='whitegrid', figsize=(16, 10), cmap='RdBu_r', lw=1,
            output=None, **kwargs):
    '''
    Plot a heatmap of the given property

    Args:
      prop : str
        Name of the attribute of Element object that is available from the
        elements table
      style : str
        Seaborn style option, default='whitegrid
      figsize : tuple
        Size of the plot, default=(16, 10)
      cmap : str
        Colormap to use, default='RdBu_r'
      lw : int
        Seaborn heatmap linewidths argumentm default=1,
        see http://stanford.edu/~mwaskom/software/seaborn/generated/seaborn.heatmap.html
      output : str
        File name to save the plot, by default nothing is saved
    '''

    ptable = get_table('elements')

    # add lanthanides and actinides

    keys = ['period', 'group_id', prop]
    els = ptable[keys].dropna()
    elements_rect = els.pivot(*keys)

    sns.set(font_scale=1.5, style=style, rc={"figure.figsize": figsize})
    mask = np.asarray(elements_rect.isnull())
    ax = sns.heatmap(elements_rect, cmap=cmap, mask=mask, linewidths=lw,
                     **kwargs)
    n = len(ax.xaxis.get_ticklabels())
    ax.set_yticklabels(elements_rect.index[::-1], rotation=0)
    ax.set_xticklabels(list(range(1, n + 1)))
    ax.xaxis.tick_top()
    ax.xaxis.set_label_position('top')
    ax.set_xlabel('Group')
    ax.set_ylabel('Period')
    if output is not None:
        plt.savefig(output)
    return ax


def colormap_column(df, column, cmap='RdBu_r', missing='#ffffff'):
    '''
    Return a new DataFrame with the same size (and index) as `df` with a column
    `cmap` containing HEX color mapping from `cmap` colormap.

    Args:
      df : DataFrmae
        Pandas DataFrame with the data
      column : str
        Name of the column to be color mapped
      cmap : str
        Name of the colormap, see matplotlib.org
      missing : str
        HEX color for the missing values (NaN or None)
    '''

    colormap = plt.get_cmap(cmap)
    cnorm = colors.Normalize(vmin=df[column].min(), vmax=df[column].max())
    scalarmap = cmx.ScalarMappable(norm=cnorm, cmap=colormap)
    out = pd.DataFrame(index=df.index)
    mask = df[column].isnull()
    rgba = scalarmap.to_rgba(df[column])
    out.loc[:, 'cmap'] = [colors.rgb2hex(row) for row in rgba]
    out.loc[mask, 'cmap'] = missing

    return out


def periodic_plot(df, values=None, title='Periodic Table', width=1000,
                  height=800, missing='#ffffff', decimals=0,
                  colorby=None, output=None, cmap='RdBu_r',
                  showfblock=True, long_version=False):
    '''
    Use Bokeh to plot the periodic table data contained in the `df`

    Args:
      df : DataFrame
        Pandas DataFrame with the data on elements
      tile : str
        Title to appear above the periodic table
      colorby : str
        Name of the column containig the colors
      width : int
        Width of the figure in pixels
      height : int
        Height of the figure in pixels
      decimals : int
        Number of decimals to be displayed in the bottom row of each cell
      missing : str
        Hex code of the color to be used for the missing values
      output : str
        Name of the output file to store the plot, should end in .html
      cmap : str
        Colormap to use, see matplotlib colormaps
      long_version : bool
        Show the long version of the periodic table with the f block between
        the s and d blocks
      showfblock : bool
        Show the elements from the f block
    '''

    elements = df.copy()

    # calculate x and y of the main group/row elements

    elements.loc[elements['group_id'].notnull(), 'x'] = \
        elements.loc[elements['group_id'].notnull(), 'group_id'].astype(int)
    elements.loc[elements['period'].notnull(), 'y'] = \
        elements.loc[elements['period'].notnull(), 'period'].astype(int)

    if showfblock:
        if long_version:
            elements.loc[elements['x'] > 2, 'x'] = \
                elements.loc[elements['x'] > 2, 'x'] + 14
            for period in [6, 7]:
                mask = (elements['block'] == 'f') & (elements['period'] == period)
                elements.loc[mask, 'x'] = elements.loc[mask, 'atomic_number'] -\
                                             elements.loc[mask, 'atomic_number'].min() + 3
                elements.loc[mask, 'y'] = period
        else:
            for period in [6, 7]:
                mask = (elements['block'] == 'f') & (elements['period'] == period)
                elements.loc[mask, 'x'] = elements.loc[mask, 'atomic_number'] -\
                                             elements.loc[mask, 'atomic_number'].min() + 3
                elements.loc[mask, 'y'] = elements.loc[mask, 'period'] + 2.5

    elements['mass'] = elements['mass'].astype(str)

    # additional columns for positioning of the text

    elements.loc[:, 'y_anumber'] = elements['y'] - 0.3
    elements.loc[:, 'y_name'] = elements['y'] + 0.2
    if values:
        elements.loc[elements[values].notnull(), 'y_prop'] = elements.loc[elements[values].notnull(), 'y'] + 0.35
    else:
        elements.loc[:, 'y_prop'] = elements['y'] + 0.35

    if values:
        temp = colormap_column(elements, values, cmap=cmap, missing=missing)
        elements = pd.merge(elements, temp, left_index=True, right_index=True)
        elements[values] = elements[values].round(decimals=decimals)

    if colorby not in elements.columns:
        series = get_table('series')
        elements = pd.merge(elements, series, left_on='series_id',
                            right_on='id', suffixes=('', '_series'))
        colorby = 'color'

    source = ColumnDataSource(data=elements)

    TOOLS = "resize,hover,save"

    p = figure(title=title,
               tools=TOOLS,
               x_axis_location='above',
               x_range=(elements.x.min() - 0.5, elements.x.max() + 0.5),
               y_range=(elements.y.max() + 0.5, elements.y.min() - 0.5),
               width=width, height=height,
               toolbar_location='above',
               toolbar_sticky=False,
               )

    if values:
        colorby = 'cmap'

    p.rect("x", "y", 0.9, 0.9, source=source, color=colorby, fill_alpha=0.6)

    # adjust the ticks and axis bounds
    p.yaxis.bounds = (1, 7)
    p.axis[1].ticker.num_minor_ticks = 0
    if long_version:
        # Turn off tick labels
        p.axis[0].major_label_text_font_size = '0pt'
        # Turn off tick marks
        p.axis[0].major_tick_line_color = None  # turn off major ticks
        p.axis[0].ticker.num_minor_ticks = 0  # turn off minor ticks
    else:
        p.axis[0].ticker = FixedTicker(ticks=list(range(1, 19)))

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

    if values:
        column = values
    else:
        column = 'mass'

    p.text(x="x", y="y_prop", text=column,
           text_font_size="7pt", **text_props)

    p.grid.grid_line_color = None

    hover = p.select(dict(type=HoverTool))
    hover.tooltips = OrderedDict([
        ("name", "@name"),
        ("atomic number", "@atomic_number"),
        ("atomic mass", "@mass"),
        ('EN Pauling', '@en_pauling'),
        ('Electron affinity', '@electron_affinity'),
        ("CPK color", "$color[hex, swatch]:cpk_color"),
        ("Jmol color", "$color[hex, swatch]:jmol_color"),
        ("Molcas GV color", "$color[hex, swatch]:molcas_gv_color"),
        ("electronic configuration", "@electronic_configuration"),
    ])

    if output:
            output_file(output)

    show(p)
