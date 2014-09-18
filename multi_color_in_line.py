# Topics: line, color, LineCollection, cmap, colorline, codex
'''
Defines a function colorline that draws a (multi-)colored 2D line with coordinates x and y.
The color is taken from optional data in z, and creates a LineCollection.

z can be:
- empty, in which case a default coloring will be used based on the position along the input arrays
- a single number, for a uniform color [this can also be accomplished with the usual plt.plot]
- an array of the length of at least the same length as x, to color according to this data
- an array of a smaller length, in which case the colors are repeated along the curve

The function colorline returns the LineCollection created, which can be modified afterwards.

See also: plt.streamplot
'''

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection
from matplotlib.colors import ListedColormap, BoundaryNorm


# Data manipulation:

def make_segments(x, y):
    '''
    Create list of line segments from x and y coordinates, in the correct format for LineCollection:
    an array of the form   numlines x (points per line) x 2 (x and y) array
    '''

    points = np.array([x, y]).T.reshape(-1, 1, 2)
    segments = np.concatenate([points[:-1], points[1:]], axis=1)

    return segments


# Interface to LineCollection:

def colorline(x, y, z=None, cmap=plt.get_cmap('copper'), norm=plt.Normalize(0.0, 1.0), linewidth=3, alpha=1.0):
    '''
    Plot a colored line with coordinates x and y
    Optionally specify colors in the array z
    Optionally specify a colormap, a norm function and a line width
    '''

    # Default colors equally spaced on [0,1]:
    if z is None:
        z = np.linspace(0.0, 1.0, len(x))

    # Special case if a single number:
    if not hasattr(z, "__iter__"):  # to check for numerical input -- this is a hack
        z = np.array([z])

    z = np.asarray(z)

    segments = make_segments(x, y)
    lc = LineCollection(segments, array=z, cmap=cmap, norm=norm, linewidth=linewidth, alpha=alpha)

    ax = plt.gca()
    ax.add_collection(lc)

    return lc


def clear_frame(ax=None):
    # Taken from a post by Tony S Yu
    if ax is None:
        ax = plt.gca()
    ax.xaxis.set_visible(False)
    ax.yaxis.set_visible(False)
    for spine in ax.spines.itervalues():
        spine.set_visible(False)

def segmenter(x, y, N=20):
    """Takes consecutive (x, y) points and creates N points inbetween them"""
    x1 = x[0]
    y1 = y[0]
    x = x[1:]
    y = y[1:]
    x_segmented = []
    y_segmented = []
    for x2, y2 in zip(x, y):
        x_incr = float((x2 - x1) / (N-1))
        y_incr = float((y2 - y1) / (N-1))
        x_segmented.extend([x1 + x_incr*i for i in range(N)])
        y_segmented.extend([y1 + y_incr*i for i in range(N)])
        x1 = x2
        y1 = y2
    return (x_segmented, y_segmented)

x = [-1.0, 1.0, -1.0, 2.0, -1.0, 0.0, -1.0, 2.0, 1.0, 2.0, 1.0, 0.0, 1.0, 2.0, 2.0, 0.0, 2.0, 2.0, 0.0, 2.0]
y = [4.0, 3.0, 4.0, -4.0, 4.0, -3.0, 4.0, 4.0, 3.0, -4.0, 3.0, -3.0, 3.0, 4.0, -4.0, -3.0, -4.0, 4.0, -3.0, 4.0]
# Sine wave colored by time

#x = np.linspace(0, 4.*np.pi, 1000)
#y = np.sin(x)
x, y = segmenter(x, y)

NPOINTS = len(x)
COLOR='blue'
RESFACT=10
MAP='winter'
#MAP = 'prism'

fig, axes = plt.subplots()
ax = fig.add_subplot(111)
cm = plt.get_cmap(MAP)
ax.set_color_cycle([cm(1.*i/(NPOINTS-1)) for i in range(NPOINTS-1)])
for i in range(NPOINTS-1):
    ax.plot(x[i:i+2], y[i:i+2])


#colorline(x, y)

plt.xlim(np.min(x), np.max(x))
plt.ylim(np.min(y), np.max(y))
#plt.ylim(-1.0, 1.0)
plt.show()
