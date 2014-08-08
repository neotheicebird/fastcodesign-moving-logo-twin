"""Animate a moving polygon similar to fast codesign logo"""
import random
import itertools

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

    #def angular_move(self, rzx = 0, rxy = 0):

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
        vertices_on_xy = [(x, y) for x, y, z in self.polygon.vertices]


class Animate_logo(object):
    """gets a 2D map of the logo, links the points and updates frames of the animator object"""
    def __init__(self):
        self.animated = map_to_2D()
        print "Len: ", len(self.animated.find_edges()), self.animated.find_edges()


def main():
    Animate_logo()

if __name__ == "__main__":
    main()