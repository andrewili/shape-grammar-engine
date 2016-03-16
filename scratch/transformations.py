import math
import numpy as np

almost_equal = np.allclose

TAU = math.pi * 2
p01 = np.array([0, 1, 0, 1])

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
translate_point_2d()
























