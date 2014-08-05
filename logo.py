"""Animate a moving polygon similar to fast codesign logo"""
import random

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

    #def Angular_move(self):

class map_to_2D(object):
    """gets a frame of the 3D object and projects it on to a 2D screen.
       compute and arrange points according to how the edges will be plotted"""
    def __init__(self):
        polygon = polygon3D()

    def find_edges(self, points):
        """compute all edges in such a way that theu can be drawn continuously (like in air, repeated edges is ok)"""


    def map_to_xy(self):
        vertices_on_xy = [(x, y) for x, y, z in self.polygon.vertices]


class Animate_logo(object):
    """gets a 2D map of the logo, links the points and updates frames of the animator object"""
    pass