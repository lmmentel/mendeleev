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
import matplotlib.pyplot as plt
from .mendeleev import get_table

def heatmap(prop, style='whitegrid', figsize=(16, 10), cmap='RdBu_r', lw=1, output=None, **kwargs):
    '''
    Plot a heatmap of the given property

    Args:
      prop : str
        Name of the attribute of Element object that is available from the elements table
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
    ax = sns.heatmap(elements_rect, cmap=cmap, mask=mask, linewidths=lw, **kwargs)
    n = len(ax.xaxis.get_ticklabels())
    ax.set_yticklabels(elements_rect.index[::-1], rotation=0)
    ax.set_xticklabels(range(1, n+1))
    ax.xaxis.tick_top()
    ax.xaxis.set_label_position('top')
    ax.set_xlabel('Group')
    ax.set_ylabel('Period')
    if output is not None:
        plt.savefig(output)
    return ax
