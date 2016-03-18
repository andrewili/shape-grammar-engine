import math
import numpy as np
import point
from numpy import linalg as la

almost_equal = np.allclose

TAU = math.pi * 2
p00 = point.Point(0, 0, 0)

class Transformations(object):
    def __init__(self):
        pass

    @classmethod        
    def make_x(cls, tri, destination):
        """Receives:
            tri             [Point, Point, Point]
            destination     Point
        Finds the transformation that translates the root point of tri to the 
        destination. Returns:
            array           np.ndarray
        """
        p1 = destination
        p0 = tri[0]
        v01 = p1 - p0
        x, y, z = v01.x, v01.y, v01.z
        array = np.array([
            [1, 0, 0, x],
            [0, 1, 0, y],
            [0, 0, 1, z],
            [0, 0, 0, 1]])
        return array

    @classmethod
    def make_r(cls, angle):
        """Angle clockwise in radians
        """
        cos_a = math.cos(angle)
        sin_a = math.sin(angle)
        array = np.array([
            [ cos_a, sin_a, 0, 0],
            [-sin_a, cos_a, 0, 0],
            [     0,     0, 1, 0],
            [     0,     0, 0, 1]])
        return array

    @classmethod
    def make_s(cls, tri1, tri2):
        p10, p11, p12 = tri1
        p20, p21, p22 = tri2
        v1011 = p11 - p10
        v2021 = p21 - p20
        s = v2021.length / v1011.length
        array = np.array([
            [s, 0, 0, 0],
            [0, s, 0, 0],
            [0, 0, s, 0],
            [0, 0, 0, 1]])
        return array

    @classmethod
    def make_f(cls):
        array = np.array([
            [-1, 0, 0, 0],
            [ 0, 1, 0, 0],
            [ 0, 0, 1, 0],
            [ 0, 0, 0, 1]])
        return array

    @classmethod
    def transform_tri(cls, t, tri1):
        tri2 = []
        for p1 in tri1:
            p2 = np.cross(t, p1)
            tri2.append(p2)
        return tri2

def test2():
    def print_t(transformation, name):
        string = '    %s:\n%s' % (name, str(transformation))
        print(string)

    def transform_tri(t, tri_in):
        tri_out = []
        for p in tri_in:
            tp = t * p
            tri_out.append(tp)
        return tri_out

    # p10 = np.array([-3,  8, 0, 1])
    # p11 = np.array([-6,  4 ,0, 1])
    # p12 = np.array([-3,  4, 0, 1])
    # p20 = np.array([12, 14, 0, 1])
    # p21 = np.array([ 4,  8, 0, 1])
    # p22 = np.array([ 4, 14, 0, 1])
    # tri1 = [p10, p11, p12]
    # tri2 = [p20, p21, p22]

    x1 = make_x(tri1, p00)
    x2 = make_x(tri2, p00)
    r = make_r(TAU/4)
    s = make_s(tri1, tri2)
    f = make_f()
    x2i = la.inv(x2)

    x1_tri1 = transform_tri(x1, tri1)
    rx1_tri1 = transform_tri(r, x1_tri1)
    srx1_tri1 = transform_tri(s, rx1_tri1)
    fsrx1_tri1 = transform_tri(f, srx1_tri1)
    t_tri1 = x2ifsrx1_tri1 = transform_tri(x2i, fsrx1_tri1)

    # print_t(x1, 'x1')
    # print_t(x2, 'x2')
    # print_t(r, 'r')
    # print_t(s, 's')
    # print_t(f, 'f')
    # print_t(x2i, 'x2i')

    print_t(tri1, 'tri1')
    print_t(tri2, 'tri2')
    print_t(x2ifsrx1_tri1, 't_tri1')
    print('t_tri1 == tri2? %s' % almost_equal(t_tri1, tri2))


def test1():
    """
    tri1: (-3, 8), (-6, 4), (-3, 4)
    tri2: (12, 14), (4, 8), (4, 14)
    Map tri1 to tri2
    """
    p10 = np.array([-3,  8, 0, 1])
    p11 = np.array([-6,  4 ,0, 1])
    p12 = np.array([-3,  4, 0, 1])
    p20 = np.array([12, 14, 0, 1])
    p21 = np.array([ 4,  8, 0, 1])
    p22 = np.array([ 4, 14, 0, 1])
    tri1 = [p10, p11, p12]
    tri2 = [p20, p21, p22]

    def x1_translate(triple, destination):
        """Receives:
            tri             [Point, Point, Point]. p0 is the smallest vertex. 
                            p1 is the farthest point.
        Finds the triangle with the root translated to the destination. 
        Returns:
            x_tri           [Point, Point, Point]. Ordered triple
        """
        x = np.array
        x_triple = x * triple
        return x_triple

    def rotate_to_y_axis(tri1):
        pass

    def scale_to_match_long_side(tri1):
        pass

    def reflect_to_match_3rd_point(tri):
        pass

    def print_tri(tri, name):
        p0, p1, p2 = tri
        p0_str = str(p0)
        p1_str = str(p1)
        p2_str = str(p2)
        string = '%s: [%s, %s, %s]' % (name, p0_str, p1_str, p2_str)
        print(string)

    print_tri(tri1, 'tri1')
    x1_tri1 = x1_translate(tri1, p00)
    x2 = translate(tri2, p00)
    # x2_inv = x2.inverse()
    r = rotate_to_y_axis(tri1)
    s = scale_to_match_long_side(tri1)
    f = reflect_to_match_3rd_point(tri1)
    translate(tri1, x2_inv)

def transform_triangle_2d():
    p0000 = np.array([0, 0, 1])
    p0003 = np.array([0, 3, 1])
    p0400 = np.array([4, 0, 1])

    tri = [p0000, p0003, p0400]
    print('tri:\n%s' % tri)
    tritp = [p0000.T, p0003.T, p0400.T]
    print('tritp:\n%s' % tritp)

    t_s = np.array([[-1, 0, 0], [0, 1, 0], [0, 0, 1]])
    t_t = np.array([[1, 0, 1], [0, 1, 2], [0, 0, 1]])
    print('t_s:\n%s' % t_s)
    print('t_t:\n%s' % t_t)

    tri_r = []
    for p in tri:
        p_r = np.dot(t_s, p)
        tri_r.append(p_r)
    print('tri_r:\n%s' % tri_r)

    tri_t = []
    for p in tri:
        p_t = np.dot(t_t, p)
        tri_t.append(p_t)
    print('tri_t:\n%s' % tri_t)

    tritp_r = []
    for p in tritp:
        p_r = np.dot(t_s, p)
        tritp_r.append(p_r)
    print('tritp_r:\n%s' % tritp_r)

    tritp_s = []
    for p in tritp:
        p_t = np.dot(t_t, p)
        tritp_s.append(p_t)
    print('tritp_s:\n%s' % tritp_s)

def rotate_point_z_2d():
    def rotate_0():
        r_p01_exp = p01
        r = np.array([
            [1, 0, 0, 0],
            [0, 1, 0, 0],
            [0, 0, 1, 0],
            [0, 0, 0, 1]])
        r_p01_got = np.dot(r, p01)
        report('rotate_0', r_p01_exp, r_p01_got)

    def rotate_90():
        r_p01_exp = np.array([1, 0, 0, 1])
        r = np.array([
            [ math.cos(TAU/4), math.sin(TAU/4), 0, 0],
            [-math.sin(TAU/4), math.cos(TAU/4), 0, 0],
            [               0,               0, 1, 0],
            [               0,               0, 0, 1]])
        r_p01_got = np.dot(r, p01)
        report('rotate_90', r_p01_exp, r_p01_got)

    def rotate_180():
        r_p01_exp = np.array([0, -1, 0, 1])
        r = np.array([
            [ math.cos(TAU/2), math.sin(TAU/2), 0, 0],
            [-math.sin(TAU/2), math.cos(TAU/2), 0, 0],
            [               0,               0, 1, 0],
            [               0,               0, 0, 1]])
        r_p01_got = np.dot(r, p01)
        report('rotate_180', r_p01_exp, r_p01_got)

    def rotate_270():
        r_p01_exp = np.array([-1, 0, 0, 1])
        r = np.array([
            [ math.cos(TAU * 3/4), math.sin(TAU * 3/4), 0, 0],
            [-math.sin(TAU * 3/4), math.cos(TAU * 3/4), 0, 0],
            [                   0,                   0, 1, 0],
            [                   0,                   0, 0, 1]])
        r_p01_got = np.dot(r, p01)
        report('rotate_270', r_p01_exp, r_p01_got)

    def rotate_360():
        r_p01_exp = np.array([0, 1, 0, 1])
        r = np.array([
            [ math.cos(TAU), math.sin(TAU), 0, 0],
            [-math.sin(TAU), math.cos(TAU), 0, 0],
            [             0,             0, 1, 0],
            [             0,             0, 0, 1]])
        r_p01_got = np.dot(r, p01)
        report('rotate_360', r_p01_exp, r_p01_got)

    rotate_0()
    rotate_90()
    rotate_180()
    rotate_270()
    rotate_360()

def scale_point_2d():
    def scale_100():
        s100_p01_exp = p01
        s100 = np.array([
            [1, 0, 0, 0],
            [0, 1, 0, 0],
            [0, 0, 1, 0],
            [0, 0, 0, 1]])
        s100_p01_got = np.dot(s100, p01)
        report('scale_100', s100_p01_exp, s100_p01_got)

    def scale_050():
        s050_p01_exp = np.array([0, 0.5, 0, 1])
        s050 = np.array([
            [0.5, 0  , 0  , 0],
            [0  , 0.5, 0  , 0],
            [0  , 0  , 0.5, 0],
            [0  , 0  , 0  , 1]])
        s050_p01_got = np.dot(s050, p01)
        report('scale_050', s050_p01_exp, s050_p01_got)

    def scale_200():
        s200_p01_exp = np.array([0, 2, 0, 1])
        s200 = np.array([
            [2, 0, 0, 0],
            [0, 2, 0, 0],
            [0, 0, 2, 0],
            [0, 0, 0, 1]])
        s200_p01_got = np.dot(s200, p01)
        report('scale_200', s200_p01_exp, s200_p01_got)

    scale_100()
    scale_050()
    scale_200()

def translate_point_2d():
    def translate_0000():
        t0000_p01_exp = p01
        t0000 = np.array([
            [1, 0, 0, 0],
            [0, 1, 0, 0],
            [0, 0, 1, 0],
            [0, 0, 0, 1]])
        t0000_p01_got = np.dot(t0000, p01)
        report('translate_0000', t0000_p01_got, t0000_p01_exp)

    def translate_0102():
        t0102_p01_exp = np.array([1, 3, 0, 1])
        t0102 = np.array([
            [1, 0, 0, 1],
            [0, 1, 0, 2],
            [0, 0, 1, 0],
            [0, 0, 0, 1]])
        t0102_p01_got = np.dot(t0102, p01)
        report('translate_0102', t0102_p01_got, t0102_p01_exp)

    def translate__1_2():
        t_1_2_p01_exp = np.array([-1, -1, 0, 1])
        t_1_2 = np.array([
            [1, 0, 0, -1],
            [0, 1, 0, -2],
            [0, 0, 1, 0],
            [0, 0, 0, 1]])
        t_1_2_p01_got = np.dot(t_1_2, p01)
        report('translate__1_2', t_1_2_p01_got, t_1_2_p01_exp)

    translate_0000()
    translate_0102()
    translate__1_2()

def report(name, expected, got):
    indent = '  '
    print('%s%s\n%sExpected:\n%s\n%sGot:\n%s' % (
        indent, name, indent, expected, indent, got))
    if almost_equal(expected, got):
        message = 'Virtually equal'
    else:
        message = 'Not equal'
    print('%s%s' % (indent, message))

# transform_triangle_2d()
# rotate_point_z_2d()
# scale_point_2d()
# translate_point_2d()
# test1()

if __name__ == '__main__':
    import doctest
    doctest.testfile('tests/transformations_test.txt')
