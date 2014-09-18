import numpy as np
import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection
# Make random number generation consistent between runs
np.random.seed(5)

def main():
    numlines, numpoints = 1, 15
    #lines = np.random.random((numlines, numpoints, 2))
    x = [1, 2, 3]
    y = [3, 2, 5]
    lines = np.array([zip(x, y)])
    fig, ax = plt.subplots()
    for line in lines:
        # Add "num" additional segments to the line
        segments, color_scalar = interp(line, num=20)
        coll = LineCollection(segments)
        coll.set_array(color_scalar)
        ax.add_collection(coll)
    plt.show()

def interp(data, num=20):
    """Add "num" additional points to "data" at evenly spaced intervals and
    separate into individual segments."""
    x, y = data.T
    dist = np.hypot(np.diff(x - x.min()), np.diff(y - y.min())).cumsum()
    t = np.r_[0, dist] / dist.max()

    ti = np.linspace(0, 1, num, endpoint=True)
    xi = np.interp(ti, t, x)
    yi = np.interp(ti, t, y)

    # Insert the original vertices
    indices = np.searchsorted(ti, t)
    xi = np.insert(xi, indices, x)
    yi = np.insert(yi, indices, y)

    return reshuffle(xi, yi), ti

def reshuffle(x, y):
    """Reshape the line represented by "x" and "y" into an array of individual
    segments."""
    points = np.vstack([x, y]).T.reshape(-1,1,2)
    points = np.concatenate([points[:-1], points[1:]], axis=1)
    return points

if __name__ == '__main__':
    main()
