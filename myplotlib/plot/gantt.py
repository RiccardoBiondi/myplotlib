import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

from textwrap import dedent
from seaborn.categorical import _CategoricalPlotter, _categorical_docs
from seaborn._core.typing import default, deprecated
from seaborn.utils import (
    desaturate,
    _check_argument,
    _draw_figure,
    _default_color,
    _get_patch_legend_artist,
    _get_transform_functions,
    _scatter_legend_artist,
    _version_predates,
)


__author__ = ["RiccardoBiondi"]
___email__ = ["riccardo.biondi7@unibo.it"]


# Here prepare the 

class _MyCategoricalPlotter(_CategoricalPlotter):
    

    def plot_gantt(self, fill, color, thick, plot_kws):

        # questo 
        #agg_var = {"x": "y", "y": "x"}[self.orient]
        iter_vars = ["hue"]

        ax = self.ax

        if not fill:
            plot_kws.setdefault("linewidth", 1.5 * mpl.rcParams["lines.linewidth"])
    
        for sub_vars, sub_data in self.iter_data(["hue"],from_comp_data=True, allow_empty=True):

            ax = self._get_axes(sub_vars)

            progression = "progression" in sub_data.columns

            if self.orient == "x":
                bar_func = ax.bar
                kws = dict(
                    bottom=sub_data["y"], height=sub_data["duration"], width=thick, x=sub_data["x"]
                )
            else:
                bar_func = ax.barh
                kws = dict(
                    y=sub_data["y"], width=sub_data["duration"], height=thick, left=sub_data["x"]
                )
            

            # here add the color choice
            main_color = self._hue_map(sub_vars["hue"]) if "hue" in sub_vars else color
            
            if fill:
                kws.update(color=main_color, facecolor=main_color)
            else:
                kws.update(color=main_color, edgecolor=main_color, facecolor="none")
            
            # here add the costruction for the subplot

            if progression:
                alpha = kws.get("alpha", 1.)
                kws.update(alpha=.4 * alpha)
                bar_func(**{**kws, **plot_kws})
                kws["alpha"] = alpha
                progression_var = "height" if self.orient == "x" else "width"
                kws[progression_var] = sub_data["progression"]

            bar_func(**{**kws, **plot_kws})

        legend_artist = _get_patch_legend_artist(fill)
        self._configure_legend(ax, legend_artist, plot_kws)



def ganttplot(
    data=None, *, x=None, y=None, hue=None,
    duration=None, progression=None, order=None, 
    hue_order=None, orient=None, palette=None,
    color=None, fill=True, saturation=.75,
    thick=.8, hue_norm=None, legend="auto",
    formatter=None, 
    ax=None, **kwargs):

    p = _MyCategoricalPlotter(
        data=data,
        variables=dict(x=x, y=y, hue=hue, duration=duration, progression=progression),
        order=order,
        orient=orient,
        color=color,
        legend=legend,
    )

    if ax is None:
        ax = plt.gca()

    if p.plot_data.empty:
        return ax

    if p.var_types.get(p.orient) == "categorical":
        p.scale_categorical(p.orient, order=order, formatter=formatter)

    p._attach(ax)


    hue_order = p._palette_without_hue_backcompat(palette, hue_order)
    palette, hue_order = p._hue_backcompat(color, palette, hue_order)

    saturation = saturation if fill else 1
    p.map_hue(palette=palette, order=hue_order, norm=hue_norm, saturation=saturation)
    color = _default_color(ax.bar, hue, color, kwargs, saturation=saturation)

    p.plot_gantt(fill, color, thick, plot_kws=kwargs)

    p._add_axis_labels(ax)
    p._adjust_cat_axis(ax, axis=p.orient)

    return ax