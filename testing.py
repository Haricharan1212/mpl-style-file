import matplotlib.pyplot as plt
import numpy as np
np.random.seed(0)
plt.style.use('stuff.mplstyle')

def construct_properties_dict(names, labels):

    """

    names: data variables
    labels: Corresponding consistent labels to be used for them throughout

    """

    linestyles = ['solid', 'dashed', 'dashdot', 'dotted', 'solid', 'solid']
    colors = ['blue', 'brown', 'purple', 'cyan', 'green', 'red']
    markers = ['o', '^', 's', 'P', 'X', '*']

    properties_dict = {}

    for i, name in enumerate(names):
        properties_dict[name] = {
            'color': colors[i],
            'linestyle': linestyles[i],
            'marker': markers[i],
            'label': labels[i]            
        }

    return properties_dict

