"""
Just a file to store all the utilities and dict for an efficient documentation management
"""
from seaborn._docstring import _core_params



__author__ = ["Riccardo Biondi"]
__email__ = ["riccardo.biondi7@unibo.it"]

# Definition of a string for the narrative of the 
PLOT_NARRATIVE = ""

_gantt_docs = {
    "data": "data : pandas dataframe with the task duration data.",
    "input_params": "x, y, duration : names of variables in `data`\n    One of x, y should represent the task starting point. duration represent each task duration",
    "hue": _core_params["hue"],
    "progression": "preogression : names of variable in `data`\n    Represents the task completion status. Must be in the same unit of measuire of duration.",
    "palette": _core_params["palette"],
    "hue_order": _core_params["hue_order"],
    "hue_norm": _core_params["hue_norm"],
    "color": _core_params["color"],
    "ax": _core_params["ax"]

}