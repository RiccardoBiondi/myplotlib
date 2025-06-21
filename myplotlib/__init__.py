from myplotlib.colors.colormaps import *
from myplotlib.colors.namedcolors import *
from myplotlib.plot import *
import matplotlib.colors as mpc
import matplotlib.pyplot as plt


__author__ = ["Riccardo Biondi"]
__email__ = ["riccardo.biondi7@unibo.it"]

# register all the named colors
for k, v in MYCOLORS.items():
    mpc._colors_full_map[k] = v

# register all the custom color maps
for k, v in CMAPS.items():
    plt.register_cmap(name=k, cmap=v)