from numpy import linalg as la
import math
import numpy as np
# from package.model import point
import point

class Triad(object):
    ### construct
    def __init__(self, p1_in, p2_in, p3_in):    ##  2016-03-03 19:42
        """Receives:
            p1_in           Point
            p2_in           Point
            p3_in           Point. p1_in, p2_in, and p3_in are not 
                            collinear 
        """
        method_name = '__init__'
        try:
            if not (
                p1_in.__class__ == point.Point and
                p2_in.__class__ == point.Point and
                p3_in.__class__ == point.Point
            ):
                raise TypeError
            elif self.__class__._points_are_collinear(p1_in, p2_in, p3_in):
                raise ValueError
            else:
                pass
        except TypeError:
            message = 'The arguments must all be Point objects'
            self.__class__._print_error_message(method_name, message)
        except ValueError:
            message = 'The points must not be collinear'
            self.__class__._print_error_message(method_name, message)
        else:
            pass
            # self.clockwise_points = self.__class__._order_points_clockwise(
            #     p1_in, p2_in, p3_in)

            # self.p0 = self.clockwise_points[0]
            # self.p1 = self.clockwise_points[1]
            # self.p2 = self.clockwise_points[2]
            # self.clockwise_angles = self._find_clockwise_angles()
            # self.p0 = smallest_vertex = self._find_smallest_vertex()
            # a0: smallest angle: float
            # p0: smallest vertex: Point
            # p1: next vertex clockwise
            # p2: remaining vertex
            # s0: side opposite p0: (Point, Point)
            # s1: side opposite p1
            # s2: side opposite p2
            # longest side (clockwise from p0): either s1 or s2

    @classmethod
    def _points_are_collinear(cls, p0, p1, p2):
        """Receives:
            p0              Point
            p1              Point
            p2              Point
        Returns:
            value           boolean. True if the points are collinear. False 
                            otherwise
        """
        v10 = p1 - p0
        v20 = p2 - p0
        v21 = p2 - p1
        v10_length = la.norm(v10)
        v20_length = la.norm(v20)
        v21_length = la.norm(v21)
        if (v10_length == v20_length + v21_length or
            v20_length == v10_length + v21_length or
            v21_length == v10_length + v20_length
        ):
            value = True
        else:
            value = False
        return value

    @classmethod                                ##  2016-03-07 08:23
    def _order_points_clockwise(cls, pa, pb, pc):
        """FOR NOW: the points are in the xy-plane
        Receives non-collinear points:
            pa              Point. z = 0
            pb              Point. z = 0
            pc              Point. z = 0
        Returns:
            (p0, p1, p2)    (Point). p0 is the least point (by point ordering) 
                            with the smallest angle; p1 is the next point 
                            clockwise; and p2 is the remaining point
        """
        class_ = self.__class__
        p0 = first_clockwise_point = class_._find_smallest_vertex(
            pa, pb, pc)
        p1 = next_clockwise_point = class_._find_next_clockwise_point()
        p2 = last_clockwise_point = class_._find_last_clockwise_point()
        clockwise_points = (p0, p1, p2)
        return clockwise_points

    @classmethod
    def _find_smallest_vertex(cls, pa, pb, pc):
        """FOR NOW: For points in the xy-plane
        Receives non-collinear points:
            pa              Point. z = 0
            pb              Point. z = 0
            pc              Point. z = 0
        Finds the vertex with the smallest angle and the least point (by point 
        ordering). Returns:
            smallest_vertex Point
        """
        vertex_triples = (
            (pa, pb, pc),
            (pb, pc, pa),
            (pc, pa, pb))
        angle_vertex_pairs = []
        for triple in vertex_triples:
            vertex, p1, p2 = triple
            angle = cls._find_angle(vertex, p1, p2)
            pair = (angle, vertex)
            angle_vertex_pairs.append(pair)
        smallest_angle, smallest_vertex = min(angle_vertex_pairs)
        return smallest_vertex

    @classmethod
    def _find_angle(cls, p0, p1, p2):
        """FOR NOW: the points are all in the xy-plane
        Receives non-collinear points:
            p0              Point. z = 0
            p1              Point. z = 0
            p2              Point. z = 0
        Finds the angle p1p0p2 in degrees. Returns:
            angle           float. 0 < angle < 180
        """
        p0x, p0y, p0z = p0.x, p0.y, p0.z
        p1x, p1y, p1z = p1.x, p1.y, p1.z
        p2x, p2y, p2z = p2.x, p2.y, p2.z
        v01 = np.array([(p1x - p0x), (p1y - p0y), (p1z - p0z)])
        v02 = np.array([(p2x - p0x), (p2y - p0y), (p2z - p0z)])
        uv01 = unit_vector_01 = v01 / la.norm(v01)
        uv02 = unit_vector_02 = v02 / la.norm(v02)
        angle = math.degrees(math.acos(np.dot(uv01, uv02)))
        return angle

    @classmethod
    def new(cls, point_triple):
        """Receives:
            point_triple    (Point, Point, Point)
        Returns:
            triad           Triad
        """
        pass

    ###
    def _find_clockwise_angles(self):
        """FOR NOW: For points in the xy-plane
        Finds the angle at each vertex. Returns:
            (a0, a1, a2)    (float). a0 is the smallest angle at the least 
                            point (by point ordering). a1 and a2 follow 
                            clockwise
        """
        return angles

    ### utility
    @classmethod
    def _print_error_message(cls, method_name, message):
        print '%s.%s:\n    %s' % (cls.__name__, method_name, message)

if __name__ == '__main__':
    import doctest
    doctest.testfile('tests/triad_test.txt')
