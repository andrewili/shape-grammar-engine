from package.scripts import grammar as g
import nakata as n
import rhinoscriptsyntax as rs
from package.tests import utilities as u

def test___init__():
    method_name = '__init__'
    try_name = 'try_good'
    g.Grammar.clear_all()
    nakata = n.Nakata()
    actual_value = rs.IsBlock('zigzag')
    expected_value = True
    if not actual_value == expected_value:
        u.Utilities.print_test_error_message(
            method_name, try_name, expected_value, actual_value)

def test__draw_zigzag():
    g.Grammar.clear_all()
    guids = n.Nakata._draw_zigzag()
    rs.SelectObjects(guids)

def test_draw_prototiles():
    g.Grammar.clear_all()
    nakata = n.Nakata()
    nakata.draw_prototiles()

def test__get_t_quad():
    def try_bad_value_ix_small():
        try_name = 'bad_value_ix_small'
        g.Grammar.clear_all()
        nakata = n.Nakata()
        actual_value = nakata._get_t_quad(bad_value_small, good_value_mid)
        expected_value = None
        if not actual_value == expected_value:
            u.Utilities.print_test_error_message(
                method_name, try_name, expected_value, actual_value)

    def try_bad_value_ix_large():
        try_name = 'bad_value_ix_large'
        g.Grammar.clear_all()
        nakata = n.Nakata()
        actual_value = nakata._get_t_quad(bad_value_large, good_value_mid)
        expected_value = None
        if not actual_value == expected_value:
            u.Utilities.print_test_error_message(
                method_name, try_name, expected_value, actual_value)

    def try_bad_value_iy_small():
        try_name = 'bad_value_iy_small'
        g.Grammar.clear_all()
        nakata = n.Nakata()
        actual_value = nakata._get_t_quad(good_value_mid, bad_value_small)
        expected_value = None
        if not actual_value == expected_value:
            u.Utilities.print_test_error_message(
                method_name, try_name, expected_value, actual_value)

    def try_bad_value_iy_large():
        try_name = 'bad_value_iy_large'
        g.Grammar.clear_all()
        nakata = n.Nakata()
        actual_value = nakata._get_t_quad(good_value_mid, bad_value_large)
        expected_value = None
        if not actual_value == expected_value:
            u.Utilities.print_test_error_message(
                method_name, try_name, expected_value, actual_value)

    def try_good_value_ix_min():
        try_name = 'good_value_ix_min'
        g.Grammar.clear_all()
        nakata = n.Nakata()
        actual_value = nakata._get_t_quad(good_value_min, good_value_mid)
        expected_value = (0, 0, 1, 3)
        if not actual_value == expected_value:
            u.Utilities.print_test_error_message(
                method_name, try_name, expected_value, actual_value)

    def try_good_value_ix_max():
        try_name = 'good_value_ix_max'
        g.Grammar.clear_all()
        nakata = n.Nakata()
        actual_value = nakata._get_t_quad(good_value_max, good_value_mid)
        expected_value = (3, 3, 1, 3)
        if not actual_value == expected_value:
            u.Utilities.print_test_error_message(
                method_name, try_name, expected_value, actual_value)

    def try_good_value_iy_min():
        try_name = 'good_value_iy_min'
        g.Grammar.clear_all()
        nakata = n.Nakata()
        actual_value = nakata._get_t_quad(good_value_mid, good_value_min)
        expected_value = (1, 3, 0, 0)
        if not actual_value == expected_value:
            u.Utilities.print_test_error_message(
                method_name, try_name, expected_value, actual_value)

    def try_good_value_iy_max():
        try_name = 'good_value_iy_max'
        g.Grammar.clear_all()
        nakata = n.Nakata()
        actual_value = nakata._get_t_quad(good_value_mid, good_value_max)
        expected_value = (1, 3, 3, 3)
        if not actual_value == expected_value:
            u.Utilities.print_test_error_message(
                method_name, try_name, expected_value, actual_value)

    def try_good_values_mid():
        try_name = 'good_value_ix_mid'
        g.Grammar.clear_all()
        nakata = n.Nakata()
        actual_value = nakata._get_t_quad(good_value_mid, good_value_mid)
        expected_value = (1, 3, 1, 3)
        if not actual_value == expected_value:
            u.Utilities.print_test_error_message(
                method_name, try_name, expected_value, actual_value)
        
    method_name = '_get_t_quad'
    bad_value_small = -1
    bad_value_large = 16
    good_value_min = 0
    good_value_mid = 7
    good_value_max = 15
    try_bad_value_ix_small()
    try_bad_value_ix_large()
    try_bad_value_iy_small()
    try_bad_value_iy_large()
    try_good_value_ix_min()
    try_good_value_ix_max()
    try_good_value_iy_min()
    try_good_value_iy_max()
    try_good_values_mid()

def test__get_point():
    def try_ix_under():
        try_name = 'good_ix_under'
        g.Grammar.clear_all()
        nakata = n.Nakata()
        actual_value = nakata._get_point(under, mid)
        expected_value = (expected_under, expected_mid, 0)
        if not actual_value == expected_value:
            u.Utilities.print_test_error_message(
                method_name, try_name, expected_value, actual_value)

    def try_ix_min():
        try_name = 'ix_min'
        g.Grammar.clear_all()
        nakata = n.Nakata()
        actual_value = nakata._get_point(mmin, mid)
        expected_value = (expected_min, expected_mid, 0)
        if not actual_value == expected_value:
            u.Utilities.print_test_error_message(
                method_name, try_name, expected_value, actual_value)

    def try_ix_max():
        try_name = 'ix_max'
        g.Grammar.clear_all()
        nakata = n.Nakata()
        actual_value = nakata._get_point(mmax, mid)
        expected_value = (expected_max, expected_mid, 0)
        if not actual_value == expected_value:
            u.Utilities.print_test_error_message(
                method_name, try_name, expected_value, actual_value)

    def try_ix_over():
        try_name = 'ix_over'
        g.Grammar.clear_all()
        nakata = n.Nakata()
        actual_value = nakata._get_point(over, mid)
        expected_value = (expected_over, expected_mid, 0)
        if not actual_value == expected_value:
            u.Utilities.print_test_error_message(
                method_name, try_name, expected_value, actual_value)

    def try_iy_under():
        try_name = 'iy_under'
        g.Grammar.clear_all()
        nakata = n.Nakata()
        actual_value = nakata._get_point(mid, under)
        expected_value = (expected_mid, expected_under, 0)
        if not actual_value == expected_value:
            u.Utilities.print_test_error_message(
                method_name, try_name, expected_value, actual_value)

    def try_iy_min():
        try_name = 'iy_min'
        g.Grammar.clear_all()
        nakata = n.Nakata()
        actual_value = nakata._get_point(mid, mmin)
        expected_value = (expected_mid, expected_min, 0)
        if not actual_value == expected_value:
            u.Utilities.print_test_error_message(
                method_name, try_name, expected_value, actual_value)

    def try_iy_max():
        try_name = 'iy_max'
        g.Grammar.clear_all()
        nakata = n.Nakata()
        actual_value = nakata._get_point(mid, mmax)
        expected_value = (expected_mid, expected_max, 0)
        if not actual_value == expected_value:
            u.Utilities.print_test_error_message(
                method_name, try_name, expected_value, actual_value)

    def try_iy_over():
        try_name = 'iy_over'
        g.Grammar.clear_all()
        nakata = n.Nakata()
        actual_value = nakata._get_point(mid, over)
        expected_value = (expected_mid, expected_over, 0)
        if not actual_value == expected_value:
            u.Utilities.print_test_error_message(
                method_name, try_name, expected_value, actual_value)

    def try_mid():
        try_name = 'mid'
        g.Grammar.clear_all()
        nakata = n.Nakata()
        actual_value = nakata._get_point(mid, mid)
        expected_value = (expected_mid, expected_mid, 0)
        if not actual_value == expected_value:
            u.Utilities.print_test_error_message(
                method_name, try_name, expected_value, actual_value)

    def _get_expected(i, naka_chan):
        expected = (
            (naka_chan.prototile_center_center_x * i) + 
            naka_chan.zigzag_side)
        return expected

    method_name = '_get_point'
    under = -2
    mmin = 0
    mmax = 15
    over = 17
    mid = 7
    naka_chan = n.Nakata()
    expected_under = _get_expected(under, naka_chan)
    expected_min = _get_expected(mmin, naka_chan)
    expected_max = _get_expected(mmax, naka_chan)
    expected_over = _get_expected(over, naka_chan)
    expected_mid = _get_expected(mid, naka_chan)
    try_ix_under()
    try_ix_min()
    try_ix_max()
    try_ix_over()
    try_iy_under()
    try_iy_min()
    try_iy_max()
    try_iy_over()
    try_mid()

def test__draw_prototile():
    g.Grammar.clear_all()
    p = (0, 0, 0)
    t_quad = (0, 1, 2, 3)
    nakata = n.Nakata()
    nakata._draw_prototile(p, t_quad)

def test__insert_zigzag():
    g.Grammar.clear_all()
    nakata = n.Nakata()
    p = (0, 0, 0)
    message_reflect = "Reflect? 'y' or 'n'"
    message_rotate = "Rotate? 'y' or 'n'"
    reflect = rs.GetString(message_reflect)
    rotate = rs.GetString(message_rotate)
    if reflect == 'n' and rotate == 'n':
        t = 0
    elif reflect == 'n' and rotate == 'y':
        t = 1
    elif reflect == 'y' and rotate == 'n':
        t = 2
    elif reflect == 'y' and rotate == 'y':
        t = 3
    else:
        pass
    nakata._insert_zigzag(p, t)

# test___init__()                                 ##  done
# test__draw_zigzag()                             ##  done
test_draw_prototiles()
# test__get_t_quad()                              ##  done
# test__get_point()                               ##  done
# test__draw_prototile()                          ##  done
# test__insert_zigzag()                           ##  done
