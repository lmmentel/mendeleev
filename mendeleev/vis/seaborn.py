from typing import Tuple
import seaborn as sns
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def heatmap(
    elements: pd.DataFrame,
    prop: str,
    style: str = "whitegrid",
    figsize: Tuple[int] = (16, 10),
    cmap: str = "RdBu_r",
    lw: int = 1,
    output: str = None,
    **kwargs
):
    """
    Plot a heatmap of the given property

    Args:
        elements: DataFrame with data about elements
        prop : Name of the attribute of Element object that is available from the
            elements table
        style : Seaborn style option, default='whitegrid
        figsize : Size of the plot, default=(16, 10)
        cmap : Colormap to use, default='RdBu_r'
        lw : Seaborn heatmap `linewidths` argumentm default=1,
            see http://stanford.edu/~mwaskom/software/seaborn/generated/seaborn.heatmap.html
        output : File name to save the plot, by default nothing is saved
    """

    # add lanthanides and actinides

    keys = ["period", "group_id", prop]
    els = elements[keys].dropna()
    elements_rect = els.pivot(*keys)

    sns.set(font_scale=1.5, style=style, rc={"figure.figsize": figsize})
    mask = np.asarray(elements_rect.isnull())
    ax = sns.heatmap(elements_rect, cmap=cmap, mask=mask, linewidths=lw, **kwargs)
    n = len(ax.xaxis.get_ticklabels())
    ax.set_yticklabels(elements_rect.index[::-1], rotation=0)
    ax.set_xticklabels(list(range(1, n + 1)))
    ax.xaxis.tick_top()
    ax.xaxis.set_label_position("top")
    ax.set_xlabel("Group")
    ax.set_ylabel("Period")
    if output is not None:
        plt.savefig(output)
    return ax
