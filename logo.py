"""Animate a moving polygon similar to fast codesign logo"""
import random
import itertools
from matplotlib import pyplot as plt
from matplotlib import animation

import numpy as np

NUM_VERTICES = 5


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
        self.move_centroid_to_zero()

    def move_centroid_to_zero(self):
        """Move the centroid of the polygon to (0,0,0)
        """
        # TODO Applying a simple centre finding formula, check it
        x_mid = 0
        y_mid = 0
        z_mid = 0
        for x, y, z in self.vertices:
            x_mid += x**2
            y_mid += y**2
            z_mid += z**2
        x_mid = np.sqrt(x_mid)
        y_mid = np.sqrt(y_mid)
        z_mid = np.sqrt(z_mid)

        n = len(self.vertices)
        x_mid = float(x_mid / n)
        y_mid = float(y_mid / n)
        z_mid = float(z_mid / n)

        new_vertices = []
        for x, y, z in self.vertices:
            x_new = x - x_mid
            y_new = y - y_mid
            z_new = z - z_mid
            new_vertices.append((x_new, y_new, z_new))

        self.vertices = new_vertices

    def angular_move(self, rzx = 0, rxy = 0):
        """ create a rotation matrix and use the angle/frame found to rotate each point"""
        new_vertices = []

        # Rotation ZX plane
        beta = float(rzx / 5)  # TODO the 5 is some dummy number, change it
        gamma = float(rxy / 5)
        for x, y, z in self.vertices:
            x_new_zx = np.cos(beta)*x - np.sin(beta)*z
            y_new_zx = y
            z_new_zx = np.sin(beta)*x + np.cos(beta)*z

            x_new_xy = np.cos(gamma)*x_new_zx + np.sin(gamma)*y_new_zx
            y_new_xy = -np.sin(gamma)*x_new_zx + np.cos(gamma)*y_new_zx
            z_new_xy = z_new_zx

            new_vertices.append((x_new_xy, y_new_xy, z_new_xy))

        self.vertices = new_vertices


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

        self.polygon.angular_move(rzx=0.25, rxy=0.25)  # TODO find if this line should come here, if so can we rename the func

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

        # set x, y limits
        self.ax.set_xlim([-10, 20])
        self.ax.set_ylim([-10, 20])

    def init_anim(self):
        self.line.set_data([], [])
        return self.line,

    def animate(self, i):
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
        vertices = self.animated.map_to_xy()
        print vertices
        x = []
        y = []
        for A, B in vertices:
            x.append(A[0])
            y.append(A[1])
            x.append(B[0])
            y.append(B[1])
        print x
        print y

        self.line.set_data(x, y)
        return self.line,

    def dummy_animate(self, i):
        x = np.linspace(0, 2, 1000)
        y = np.sin(2 * np.pi * (x - 0.01 * i))
        self.line.set_data(x, y)
        return self.line,

    def run(self):
        self.animate(1)
        self.animate(1)
        self.animate(1)
        self.anim = animation.FuncAnimation(self.fig, self.animate, init_func=self.init_anim,
                               frames=100, interval=20, blit=True)
        plt.show()


def main():
    animator = Animate_logo()
    animator.run()

if __name__ == "__main__":
    main()