import fuzzy_number as fn
from numpy.linalg import inv
# from numpy import linalg as la
import math
import numpy as np
# from package.model import point
import point
import vector

almost_equal = np.allclose
ORIGIN = point.Point(0, 0, 0)
TAU = math.pi * 2

class Triad(object):
    ### construct
    def __init__(self, pa, pb, pc):
        """Receives non-collinear points:
            pa, pb, pc      Point. z = 0
        First, orders the points as follows:
            p0              The point with the smallest angle
            p1              The point such that the vector v01 is longer than 
                            v02. If equal, v01 has the smaller bearing
            p2              The remaining point
        Second, constructs a standard description of the triad as the `
        transformation of a standard triad: 
            q0              (0, 0, 0)
            q1              (0, 1, 0)
            q2              (x, y, 0), such that for the vector v02, 
                            length <= 1, bearing (clockwise from north) <= 60 
                            degrees
        The standard description consists of a combined rotation-scaling-
        reflection and a translation:
            rsf             Matrix. Combined clockwise rotation, scaling, and 
                            reflection
            l               Vector. Translation from the origin to p0
        Thus, to specify a triad, it suffices to specify:
            q2
            rsf
            l
        Thus: 
            l . rsf . (q0, q1, q2) = (p0, p1, p2)
            rsf_inv . l_inv . (p0, p1, p2) = (q0, q1, q2)
        q2 specifies a set of similar triads. To transform triad1 into the 
        similar triad2:
            l2 . rsf2 . rsf1_inv . l1_inv . triad1 = triad2
            l_inv . pi = rsf . qi
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
            point_angle_pairs = self._find_point_angle_pairs(pa, pb, pc)
            point_length_pairs = self._find_point_length_pairs(pa, pb, pc)
            self.p0, self.p1, self.p2 = p_points = (
                self._find_ordered_points(pa, pb, pc))
            self.l = translation_vector = (
                self._find_translation_vector(self.p0))
            self.l_inv = vector.Vector.inv(self.l)
            pq0, pq1, pq2 = self._find_pq_points(self.l_inv, p_points)
            self.rsf = rotation_scaling_reflection_matrix = (
                self._find_rotation_scaling_reflection_matrix(pq1, pq2))
            self.rsf_inv = inv(self.rsf)
            self.q2 = self._find_q2(self.rsf_inv, self.l_inv, self.p2)
            self.standard_description = [self.l, self.rsf, self.q2]

    @classmethod                                ##  called
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
        if (almost_equal(v10.length, (v20.length + v21.length)) or
            almost_equal(v20.length, (v10.length + v21.length)) or
            almost_equal(v21.length, (v10.length + v20.length))
        ):
            value = True
        else:
            value = False
        return value

    @classmethod                                ##  called
    def _find_point_angle_pairs(cls, pa, pb, pc):
        """Receives:
            pa, pb, pc      Point. z = 0
        For each point pi finds the angle a in radians at pi. Returns an 
        ordered list [(pa, aa), (pb, ab), (pc, ac)]:
            pairs           [(Point, num)]
        """
        triples = [
            (pa, pb, pc),
            (pb, pc, pa),
            (pc, pa, pb)]
        pairs = []
        for triple in triples:
            pd, pe, pf = triple
            ad = cls._find_interior_angle_from_points(pd, pe, pf)
            pair = (pd, ad)
            pairs.append(pair)
        return pairs

    @classmethod                                ##  called
    def _find_point_length_pairs(cls, pa, pb, pc):
        """Receives:
            pa              Point, z = 0. The point opposite the side
            pb, pc          Point, z = 0. The end points of the side
        For each point pi finds the length li of the opposite side. Returns an 
        ordered list [(pa, la), (pb, lb), (pc, lc)]:
            pairs           [(Point, num)]
        """
        triples = [
            (pa, pb, pc),
            (pb, pc, pa),
            (pc, pa, pb)]
        pairs = []
        for triple in triples:
            pd, pe, pf = triple
            vef = pf - pe
            pair = (pd, vef.length)
            pairs.append(pair)
        return pairs

    @classmethod                                ##  called
    def _find_ordered_points(cls, pa, pb, pc):
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
            cls._order_points_smallest_first(pa, pb, pc))
        points_smallest_then_farthest = (
            cls._order_remaining_points_farthest_first(
                points_smallest_first))
        return points_smallest_then_farthest

    @classmethod                                ##  called
    def _find_translation_vector(cls, p):
        """Receives:
            p               Point
        Finds the translation that maps the origin to the reference point. 
        Returns:
            v               Vector
        """
        p00 = point.Point(0, 0, 0)
        v = p - p00
        return v

    @classmethod
    def _find_pq_points(cls, l_inv, p_points):
        """Receives:
            l_inv           Vector. The translation from p0 to the origin
            p_points        [p0, p1, p2], pi is a Point
        Finds the triad inversely translated to the origin. Returns:
            pq_points       [pq0, pq1, pq2], pqi is a Point
        """
        pq_points = []
        for pi in p_points:
            pqi = pi + l_inv
            pq_points.append(pqi)
        return pq_points

    @classmethod
    def translate_points(cls, v, points):
        """Receives:
            v               Vector
            points          [Point, Point, Point], z = 0
        Finds the translations of the points. Returns:
            v_points        [Point, Point, Point]
        """
        v_points = []
        for point in points:
            v_point = cls.translate_point(v, point)
            # v_point = point + v
            v_points.append(v_point)
        return v_points

    @classmethod
    def translate_point(cls, v, point):
        """Receives:
            v               Vector. The translation
            point           Point. The point before translation
        Returns:
            v_point         Point. The point after translation.
        """
        v_point = point + v
        return v_point

    @classmethod                                ##  called
    def _find_rotation_scaling_reflection_matrix(cls, pq1, pq2):
        """Receives:
            pq1             Point. pq1 = rsf . q1 = l_inv . p1. The rotation-
                            scaling-reflection maps q1:(0, 1, 0) to this point
            pq2             Point. pq2 = rsf . q2 = l_inv . p2. The rotation-
                            scaling-reflection maps q2 to this point
        Finds the matrix of the clockwise rotation-scaling-reflection that 
        maps the standard triad (q0, q1, q2) to the translated triad 
        (pq0, pq1, pq2). Returns:
            rsf_mx          np.array
        """
        r = cls._find_rotation_matrix(pq1)
        s = cls._find_scaling_matrix(pq1)
        f = cls._find_reflection_matrix(r, pq2)
        sf = np.dot(s, f)
        rsf_mx = np.dot(r, sf)
        return rsf_mx

    @classmethod                                ##  called
    def _find_rotation_matrix(cls, pq1):
        """Receives:
            pq1             Point. pq1 = rsf . q1 = l_inv . p1
        Finds the matrix that rotates q1:(0, 1, 0) clockwise about the origin 
        to fall onto the line through the origin and pq1. Returns:
            r_mx            np.array
        """
        v1 = pq1 - ORIGIN
        a = v1.bearing
        cos_a = math.cos(a)
        sin_a = math.sin(a)
        r_mx = np.array([
            [ cos_a, sin_a, 0],
            [-sin_a, cos_a, 0],
            [     0,     0, 1]])
        return r_mx

    @classmethod                                ##  called
    def _find_scaling_matrix(cls, pq1):
        """Receives:
            pq1             Point. pq1 = l_inv . p1 = rsf . q1
        Finds the matrix that scales the vector of q1 to pq1. Ignores 
        rotation. Returns:
            s_mx            np.array
        """
        v = pq1 - ORIGIN
        length = v.length
        s_mx = np.array([
            [length,      0,      0],
            [     0, length,      0],
            [     0,      0, length]])
        return s_mx

    @classmethod                                ##  called
    def _find_reflection_matrix(cls, rotation, pq2):
        """Receives:
            rotation        np.array. Clockwise rotation in radians to be 
                            applied to pq2
            pq2             Point. pq2 = l_inv . p1 = rsf . q1
        Finds the matrix of the reflection that maps pq2 to the positive-x 
        side of the y-axis. Returns:
            f_mx            np.array if successful. None otherwise
        """
        r_inv = inv(rotation)
        rinv_pq2 = cls.transform_point(r_inv, pq2)
        if rinv_pq2.x > 0:
            x = 1
        elif rinv_pq2.x < 1:
            x = -1
        else:
            x = None
        f_mx = np.array([
            [x, 0, 0],
            [0, 1, 0],
            [0, 0, 1]])
        return f_mx

    @classmethod
    def _find_q2(cls, rsf_inv, l_inv, p2):
        """Receives:
            rsf_inv         np.array
            l_inv           Vector
            p2              Point
        Returns:
            q2              Point
        """
        l_inv_p2 = p2 + l_inv
        q2 = cls.transform_point(rsf_inv, l_inv_p2)
        return q2

    @classmethod
    def _find_ordered_angles(cls, pa, pb, pc):
        """Returns:
            ordered_angles  [num, num, num]. The angles in order of increasing 
                            size
        """
        angles = []
        for p in [pa, pb, pc]:
            a = cls._find_angle_at_point(p)
            angles.append(a)
        ordered_angles = sorted(angles)
        return ordered_angles

    @classmethod                                ##  called
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
            fuzzy_angle = fn.FuzzyNumber(angle)
            pair = (fuzzy_angle, vertex)
            fuzzy_angle_vertex_pairs.append(pair)
        points = []
        for pair in sorted(fuzzy_angle_vertex_pairs):
            points.append(pair[1])
        return points

    @classmethod                                ##  called
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

    @classmethod                                ##  called
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

    @classmethod                                ##  called by test
    def transform_points(cls, t, points):
        """Receives:
            t               np.array. A transformation (combined rotation and 
                            scaling)
            points          [np.array]
        Returns:
            t_points        [Point]
        """
        t_points = []
        for p in points:
            t_point = cls.transform_point(t, p)
            t_points.append(t_point)
        return t_points

    @classmethod                                ##  called by test
    def transform_point(cls, t, p):
        """Receives:
            t               np.array. The rotation-scaling to be applied
            p               Point. The point to be rotated-scaled
        Returns:
            tp              Point. The point after rotation-scaling
        """
        tp_matrix = np.dot(t, p.matrix)
        tp = point.Point.from_matrix(tp_matrix)
        return tp

    @classmethod                                ##  called by test
    def translate_point(cls, l, p):
        """Receives:
            l               Vector. The translation to be applied
            p               Point. Before translation
        Returns:
            l_p             Point. After translation
        """
        l_p = p + l
        return l_p

    ### compare                                 ##  same as Engine method
    def is_similar_to(self, other):
        """Receives:
            other           Triad
        Returns:
            value           boolean. True if self and other are similar. False 
                            otherwise
        """
        value = almost_equal(self.ordered_angles, other.ordered_angles)
        return value

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
