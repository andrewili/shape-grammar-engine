from numpy import linalg as la
import math
import numpy as np
# from package.model import point
import point

class Triad(object):
    ### construct
    def __init__(self, p1_in, p2_in, p3_in):    ##  2016-03-03 19:42
        """Receives non-collinear points:
            p1_in           Point
            p2_in           Point
            p3_in           Point
        """
        method_name = '__init__'
        try:
            if not (
                type(p1_in) == point.Point and
                type(p2_in) == point.Point and
                type(p3_in) == point.Point
            ):
                raise TypeError
            elif self.__class__._points_are_collinear(p1_in, p2_in, p3_in):
                raise ValueError
            else:
                pass
        except TypeError:
            message = "The arguments must all be Point objects"
            self.__class__._print_error_message(method_name, message)
        except ValueError:
            message = "The points must not be collinear"
            self.__class__._print_error_message(method_name, message)
        else:
            pass
            # self.clockwise_points = self.__class__._get_clockwise_points(
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
        almost_equal = np.allclose
        v10 = p1 - p0
        v20 = p2 - p0
        v21 = p2 - p1
        if (almost_equal(v10.length, (v20.length + v21.length)) or
            almost_equal(v20.length, (v10.length + v21.length)) or
            almost_equal(v21.length, (v10.length + v20.length))
        ):
            value = True
        else:
            value = False
        return value

    @classmethod                                ##  2016-03-07 08:23
    def _get_clockwise_points(cls, pa, pb, pc):
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
        points_ordered_by_angle = cls._order_points_by_angle(pa, pb, pc)
        p0, p1, p2 = clockwise_points = cls._order_remaining_points_clockwise(
            points_ordered_by_angle)
        return clockwise_points

    @classmethod
    def _order_points_by_angle(cls, pa, pb, pc):
        """Receives non-collinear points:
            pa              Point. z = 0
            pb              Point. z = 0
            pc              Point. z = 0
        Orders the points by the angle at each: from smallest to largest. In 
        case of a tie, the lesser point (by point ordering) is taken. Returns:
            points          [Point, Point, Point]
        """
        vertex_triples = [
            (pa, pb, pc),
            (pb, pc, pa),
            (pc, pa, pb)]
        angle_vertex_pairs = []
        for triple in vertex_triples:
            vertex, p1, p2 = triple
            ang = cls._find_angle_from_points(vertex, p1, p2)
            pair = (ang, vertex)
            angle_vertex_pairs.append(pair)
        # print('sorted angle_vertex_pairs: %s' % sorted(angle_vertex_pairs))
        points = []
        for pair in sorted(angle_vertex_pairs):
            points.append(pair[1])
        # print('points: %s' % points)
        return points

    @classmethod
    def _find_angle_from_points(cls, p0, p1, p2):
        """FOR NOW: the points are all in the xy-plane
        Receives non-collinear points:
            p0              Point. z = 0
            p1              Point. z = 0
            p2              Point. z = 0
        Finds the angle p1p0p2 in radians. Returns:
            angle_in_radians
                            Angle. 0 < angle_in_radians < tau / 2
            # angle_in_radians
                            # float. 0 < angle_in_radians < tau / 2
        """
        v01 = p1 - p0
        v02 = p2 - p0
        angle_in_radians = abs(v02.bearing - v01.bearing) # Angle
        return angle_in_radians

    @classmethod
    def _order_remaining_points_clockwise(cls, points_in):
        """Receives 3 non-collinear points:
            points_in       [Point]. z = 0. The first has the smallest angle 
                            and, if there is more than one, the lesser
        Orders the points clockwise. Returns:
            clockwise_points
                            [Point]
        """
        pa, pb, pc = points_in
        vab = pb - pa
        vac = pc - pa
        if vab.bearing < vac.bearing:
            clockwise_points = [pa, pb, pc]
        else:
            clockwise_points = [pa, pc, pb]
        return clockwise_points

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
