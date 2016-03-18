import fuzzy_number as fn
from numpy import linalg as la
import math
import numpy as np
# from package.model import point
import point

TAU = math.pi * 2

class Triad(object):
    ### construct
    def __init__(self, pa, pb, pc):
        """Receives non-collinear points:
            pa              Point
            pb              Point
            pc              Point
        """
        method_name = '__init__'
        try:
            if not (
                type(pa) == point.Point and
                type(pb) == point.Point and
                type(pc) == point.Point
            ):
                raise TypeError
            elif self._points_are_collinear(pa, pb, pc):
                raise ValueError
            else:
                pass
        except TypeError:
            message = "The arguments must all be Point objects"
            self._print_error_message(method_name, message)
        except ValueError:
            message = "The points must not be collinear"
            self._print_error_message(method_name, message)
        else:
            self.ordered_points = self._get_ordered_points(
                pa, pb, pc)
            self.p0 = self.ordered_points[0]
            self.p1 = self.ordered_points[1]
            self.p2 = self.ordered_points[2]

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

    @classmethod
    def _get_ordered_points(cls, pa, pb, pc):
        """FOR NOW: the points are in the xy-plane
        Receives non-collinear points:
            pa              Point. z = 0
            pb              Point. z = 0
            pc              Point. z = 0
        Returns:
            points_smallest_then_farthest
                            (p0, p1, p2), (Point, Point, Point). p0 is the 
                            least point (by point ordering) with the smallest 
                            angle; p1 is the further point from p0; and p2 is 
                            the remaining point
        """
        points_smallest_first = (
            cls._order_points_smallest_first(pa, pb, pc))           # A.1
        points_smallest_then_farthest = (
            cls._order_remaining_points_farthest_first(
                points_smallest_first))                             # A.3
        return points_smallest_then_farthest

    @classmethod
    def _order_points_smallest_first(cls, pa, pb, pc):
        """Receives non-collinear points:
            pa              Point. z = 0
            pb              Point. z = 0
            pc              Point. z = 0
        Orders the points by the angle at each: from smallest to largest. In 
        case of a tie, the lesser point (by point ordering) is taken. Returns:
            points          [Point]
        """
        vertex_triples = [
            (pa, pb, pc),
            (pb, pc, pa),
            (pc, pa, pb)]
        fuzzy_angle_vertex_pairs = []
        for triple in vertex_triples:
            vertex, p1, p2 = triple
            angle = cls._find_interior_angle_from_points(vertex, p1, p2)
                                                # A.1.a
            fuzzy_angle = fn.FuzzyNumber(angle)
            pair = (fuzzy_angle, vertex)
            fuzzy_angle_vertex_pairs.append(pair)
        points = []
        for pair in sorted(fuzzy_angle_vertex_pairs):
            points.append(pair[1])
        return points

    @classmethod
    def _find_interior_angle_from_points(cls, p0, p1, p2):
        """FOR NOW: the points are all in the xy-plane
        Receives:
            p0              Point. z = 0
            p1              Point. z = 0
            p2              Point. z = 0
        Finds the interior angle p1p0p2 in radians. Returns:
            angle           float. 0 <= angle < tau / 2
        """
        v01 = p1 - p0
        v02 = p2 - p0
        directed_angle = abs(v02.bearing - v01.bearing)
        fuzzy_directed_angle = fn.FuzzyNumber(directed_angle)
        fuzzy_tau_2 = fn.FuzzyNumber(TAU / 2)
        if fuzzy_directed_angle > fuzzy_tau_2:
            angle = TAU - directed_angle
        else:
            angle = directed_angle
        return angle

    @classmethod                                # A.3
    def _order_remaining_points_farthest_first(cls, points_smallest_first):
        """Receives a list of non-collinear points [p0, pb, pc], where p0 has 
        the smallest angle and is the least (by point ordering):
            points_smallest_first
                            [Point]
        Orders the points as follows: p0, the point of the smallest angle; p1, 
        the point farthest from p0 (and, in case of a tie, the head of the 
        vector with the smaller bearing); p2, the remaining point. Returns:
            points          [Point, Point, Point] if successful. None 
                            otherwise
        """
        p0, pb, pc = points_smallest_first
        v0b = pb - p0
        v0c = pc - p0
        v0b_length_fz = fn.FuzzyNumber(v0b.length)
        v0c_length_fz = fn.FuzzyNumber(v0c.length)
        if v0b_length_fz < v0c_length_fz:
            points = [p0, pc, pb]
        elif v0b_length_fz > v0c_length_fz:
            points = [p0, pb, pc]
        elif v0b_length_fz == v0c_length_fz:
            if v0b.bearing < v0c.bearing:
                points = [p0, pb, pc]
            elif v0c.bearing < v0b.bearing:
                points = [p0, pc, pb]
            else:
                points = None
        return points

    ### represent
    def __str__(self):
        string = '(%s, %s, %s)' % (self.p0, self.p1, self.p2)
        return string
        
    ### utility
    @classmethod
    def _print_error_message(cls, method_name, message):
        print '%s.%s:\n    %s' % (cls.__name__, method_name, message)

if __name__ == '__main__':
    import doctest
    doctest.testfile('tests/triad_test.txt')
