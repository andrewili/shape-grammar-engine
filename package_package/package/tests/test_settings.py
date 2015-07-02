from package.view import grammar as g
import rhinoscriptsyntax as rs
from package.view import settings as s
from package.tests import utilities as u

def test_get_right_frame_position():
    def try_good_type_triple():
        try_name = 'try_good_type_triple'
        g.Grammar.clear_all()
        good_type_triple = (10, 10, 0)
        actual_value = s.Settings.get_right_frame_position(good_type_triple)
        expected_value = rs.PointAdd(good_type_triple, (48, 0, 0))
        if not actual_value == expected_value:
            u.Utilities.print_test_error_message(
                method_name, try_name, expected_value, actual_value)

    def try_good_type_point3d():
        try_name = 'try_good_type_point3d'
        g.Grammar.clear_all()
        good_type_point3d = rs.PointAdd((10, 10, 0), (0, 0, 0))
        print("type: %s" % type(good_type_point3d))
        actual_value = s.Settings.get_right_frame_position(good_type_point3d)
        expected_value = rs.PointAdd(good_type_point3d, (48, 0, 0))
        if not actual_value == expected_value:
            u.Utilities.print_test_error_message(
                method_name, try_name, expected_value, actual_value)

    method_name = 'get_right_frame_position'
    try_good_type_triple()
    try_good_type_point3d()

def test_new_point():
    def try_good_value_zero():
        try_name = 'try_good_value_zero'
        zero = (0, 0, 0)
        output = s.Settings.new_point(zero)
        x, y, z = output[0], output[1], output[2]
        actual_value = (x, y, z)
        expected_value = (0, 0, 0)
        if not actual_value == expected_value:
            u.Utilities.print_test_error_message(
                method_name, try_name, expected_value, actual_value)

    def try_good_value_1010():
        try_name = 'try_good_value_1010'
        good_value_1010 = (10, 10, 0)
        output = s.Settings.new_point(good_value_1010)
        x, y, z = output[0], output[1], output[2]
        actual_value = (x, y, z)
        expected_value = (10, 10, 0)
        if not actual_value == expected_value:
            u.Utilities.print_test_error_message(
                method_name, try_name, expected_value, actual_value)

    method_name = 'new_point'
    try_good_value_zero()
    try_good_value_1010()

test_get_right_frame_position()
test_new_point()