"""Animate a moving polygon similar to fast codesign logo"""
import random
import itertools
from matplotlib import pyplot as plt
from matplotlib import animation

NUM_VERTICES = 4

class polygon3D(object):
    """initialize and update frames that will be fetched by other classes"""
    @staticmethod
    def random_vertices(num_vertices):
        vertices = []
        for coords in range(num_vertices):
            x = random.randrange(0, 10, 1)
            y = random.randrange(0, 10, 1)
            z = random.randrange(0, 10, 1)
            vertices.append((x, y, z))
        return vertices

    def __init__(self):
        self.vertices = self.random_vertices(NUM_VERTICES)

    def angular_move(self, rzx = 0, rxy = 0):
        """ create a rotation matrix and use the angle/frame found to rotate each point"""


class map_to_2D(object):
    """gets a frame of the 3D object and projects it on to a 2D screen.
       compute and arrange points according to how the edges will be plotted"""

    def __init__(self):
        self.polygon = polygon3D()

    def find_edges(self):
        """(generator) compute all edges in such a way that they can be drawn continuously
        (like on paper without taking the pen from it, repeated edges is ok (minimize it too))"""

        points = self.polygon.vertices
        edges = itertools.combinations(points, 2)

        return list(edges)


    def map_to_xy(self):
        """instead of vertices, the edges points-pairs has to be mapped"""
        self.polygon.edges = self.find_edges()
        vertices_on_xy = [((x1, y1), (x2, y2)) for (x1, y1, z1), (x2, y2, z2) in self.polygon.edges]
        #print "Vertices on XY plane: ", vertices_on_xy
        return vertices_on_xy




class Animate_logo(object):
    """gets a 2D map of the logo, links the points and updates frames of the animator object"""
    def __init__(self):
        self.animated = map_to_2D()
        print "Len: ", len(self.animated.find_edges()), self.animated.find_edges()
        print "Len: ", len(self.animated.map_to_xy()), self.animated.map_to_xy()
        self.init_canvas()  # Initialize the canvas where we are going to animate

    def init_canvas(self):
        self.fig = plt.figure()
        self.ax = plt.axes(xlim=(0, 2), ylim=(-2, 2))
        self.line, = self.ax.plot([], [], lw=2)
        self.line.set_data([], [])

    def animate(self):
        """
        anim = animation.FuncAnimation(fig, animate, init_func=init,
                               frames=100, interval=20, blit=True)

        # save the animation as an mp4.  This requires ffmpeg or mencoder to be
        # installed.  The extra_args ensure that the x264 codec is used, so that
        # the video can be embedded in html5.  You may need to adjust this for
        # your system: for more information, see
        # http://matplotlib.sourceforge.net/api/animation_api.html
        anim.save('basic_animation.mp4', fps=30, extra_args=['-vcodec', 'libx264'])

        plt.show()

        """
        pass


def main():
    Animate_logo()

if __name__ == "__main__":
    main()