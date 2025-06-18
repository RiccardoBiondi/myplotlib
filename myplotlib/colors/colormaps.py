import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap, ListedColormap

#define dracula color map
# dracula
dracula = ListedColormap([
    "#282a36",
    "#44475a",
    "#6272a4",
    "#8be9fd",
    "#50fa7b",
    "#ffb86c",
    "#ff79c6",
    "#bd93f9",
    "#ff5555",
    "#f1fa8c"])
# freesurfer = ListedColormap([])

# here the definition of the color map composed by a single
# colour. That are useful to visualize segmentations.

# create the dict with all the created color maps
# that will be used to register all the maps to 
# matplotlib when this module is called 

CMAPS = {
    "dracula": dracula
}