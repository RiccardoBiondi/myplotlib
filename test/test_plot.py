"""
Here a serues of test inspired and derived by seaborn to check
the plot function.
"""

import pytest
import itertools
from pytest import approx
from myplotlib.plot.gantt import ganttplot
import matplotlib.pyplot as plt



PLOT_FUNCS  = [ganttplot] # plot functions that should perform the generic nd basic tests


class TestPlotterNew:

    #@pytest.mark.parametrize(
    #    "func,kwargs",
    #    itertools.product(
    #        PLOT_FUNCS,
    #        [
    #            {"x": "x", "y": "a"},
    #            {"x": "a", "y": "y"},
    #            {"x": "y"},
    #            {"y": "x"},
    #        ],
    #    ),
    #)
    #def test_axis_labels(self, long_df, func, kwargs):
#
    #    func(data=long_df, **kwargs)
#
    #    ax = plt.gca()
    #    for axis in "xy":
    #        val = kwargs.get(axis, "")
    #        label_func = getattr(ax, f"get_{axis}label")
    #        assert label_func() == val

    @pytest.mark.parametrize("func", PLOT_FUNCS)
    def test_empty(self, func):

        func()
        ax = plt.gca()
        assert not ax.collections
        assert not ax.patches
        assert not ax.lines

        func(x=[], y=[])
        ax = plt.gca()
        assert not ax.collections
        assert not ax.patches
        assert not ax.lines
