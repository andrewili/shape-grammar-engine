from package.scripts import grammar as g
import rhinoscriptsyntax as rs
from package.scripts import settings as s
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

test_get_right_frame_position()
