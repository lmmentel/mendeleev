
import seaborn as sns
from .mendeleev import get_table

def heatmap(prop, style='whitegrid', figsize=(16, 10), cmap='RdBu_r', lw=1, output=None):
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

    keys = ['period', 'group_id', prop]
    els = ptable[keys].dropna()
    elements_rect = els.pivot(*keys)

    sns.set(font_scale=1.5, style=style, rc={"figure.figsize": figsize})
    mask = np.asarray(elements_rect.isnull())
    ax = sns.heatmap(elements_rect, cmap=cmap, mask=mask, linewidths=lw)
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
