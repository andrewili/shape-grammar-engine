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

def test_get_derivation_element_positions():                ##  done 08-29
    def try_2_labeled_shapes():
        try_name = '2_labeled_shapes'
        n = 2
        p3d_triples = s.Settings.get_derivation_cell_position_triples(n)
        actual_value = _get_xyz_triples(p3d_triples)
        expected_value = [
            ((0, 0, 0), (40, 16, 0), (40, 24, 0)),
            ((48, 0, 0), (88, 16, 0), (88, 24, 0))]
        if not actual_value == expected_value:
            u.Utilities.print_test_error_message(
                method_name, try_name, expected_value, actual_value)

    def try_4_labeled_shapes():
        try_name = '4_labeled_shapes'
        n = 4
        p3d_triples = s.Settings.get_derivation_cell_position_triples(n)
        actual_value = _get_xyz_triples(p3d_triples)
        expected_value = [
            ((0, 0, 0), (40, 16, 0), (40, 24, 0)),
            ((48, 0, 0), (88, 16, 0), (88, 24, 0)),
            ((96, 0, 0), (136, 16, 0), (136, 24, 0)),
            ((144, 0, 0), (184, 16, 0), (184, 24, 0))]
        if not actual_value == expected_value:
            u.Utilities.print_test_error_message(
                method_name, try_name, expected_value, actual_value)

    def try_8_labeled_shapes():
        try_name = '8_labeled_shapes'
        n = 8
        p3d_triples = s.Settings.get_derivation_cell_position_triples(n)
        actual_value = _get_xyz_triples(p3d_triples)
        expected_value = [
            ((0, 64, 0), (40, 80, 0), (40, 88, 0)),
            ((48, 64, 0), (88, 80, 0), (88, 88, 0)),
            ((96, 64, 0), (136, 80, 0), (136, 88, 0)),
            ((144, 64, 0), (184, 80, 0), (184, 88, 0)),
            ((192, 64, 0), (232, 80, 0), (232, 88, 0)),
            ((0, 0, 0), (40, 16, 0), (40, 24, 0)),
            ((48, 0, 0), (88, 16, 0), (88, 24, 0)),
            ((96, 0, 0), (136, 16, 0), (136, 24, 0))]
        if not actual_value == expected_value:
            u.Utilities.print_test_error_message(
                method_name, try_name, expected_value, actual_value)

    def try_16_labeled_shapes():
        try_name = '16_labeled_shapes'
        n = 16
        p3d_triples = s.Settings.get_derivation_cell_position_triples(n)
        actual_value = _get_xyz_triples(p3d_triples)
        expected_value = [
            ((0, 192, 0), (40, 208, 0), (40, 216, 0)),
            ((48, 192, 0), (88, 208, 0), (88, 216, 0)),
            ((96, 192, 0), (136, 208, 0), (136, 216, 0)),
            ((144, 192, 0), (184, 208, 0), (184, 216, 0)),
            ((192, 192, 0), (232, 208, 0), (232, 216, 0)),
            ((0, 128, 0), (40, 144, 0), (40, 152, 0)),
            ((48, 128, 0), (88, 144, 0), (88, 152, 0)),
            ((96, 128, 0), (136, 144, 0), (136, 152, 0)),
            ((144, 128, 0), (184, 144, 0), (184, 152, 0)),
            ((192, 128, 0), (232, 144, 0), (232, 152, 0)),
            ((0, 64, 0), (40, 80, 0), (40, 88, 0)),
            ((48, 64, 0), (88, 80, 0), (88, 88, 0)),
            ((96, 64, 0), (136, 80, 0), (136, 88, 0)),
            ((144, 64, 0), (184, 80, 0), (184, 88, 0)),
            ((192, 64, 0), (232, 80, 0), (232, 88, 0)),
            ((0, 0, 0), (40, 16, 0), (40, 24, 0))]
        if not actual_value == expected_value:
            u.Utilities.print_test_error_message(
                method_name, try_name, expected_value, actual_value)

    def _get_xyz_triples(p3d_triples):
        """Receives:
            p3d_triples     [p3d_triple], where p3d_triple is of the form:
                                (point3d, point3d, point3d)
        Returns:
            xyz_triples     [xyz_triple], where xyz_triple is of the form:
                                (xyz, xyz, xyz)
                            where xyz is of the form:
                                (num, num, num)
        """
        xyz_triples = []
        for p3d_triple in p3d_triples:
            p3d_0, p3d_1, p3d_2 = p3d_triple
            xyz_0, xyz_1, xyz_2 = tuple(p3d_0), tuple(p3d_1), tuple(p3d_2)
            xyz_triple = (xyz_0, xyz_1, xyz_2)
            xyz_triples.append(xyz_triple)
        return xyz_triples

    method_name = 'get_derivation_cell_position_triples'
    try_2_labeled_shapes()
    try_4_labeled_shapes()
    try_8_labeled_shapes()
    try_16_labeled_shapes()

def test__get_derivation_cell_positions_x():
    def try_16_labeled_shapes():
        try_name = '16_labeled_shapes'
        actual_value = s.Settings._get_derivation_cell_positions_x(16)
        expected_value = [
            0, 48, 96, 144, 192, 
            0, 48, 96, 144, 192, 
            0, 48, 96, 144, 192, 
            0]
        if not actual_value == expected_value:
            u.Utilities.print_test_error_message(
                method_name, try_name, expected_value, actual_value)

    method_name = '_get_derivation_cell_positions_x'
    try_16_labeled_shapes()

def test__get_derivation_cell_positions_y():
    def try_16_labeled_shapes():
        try_name = '16_labeled_shapes'
        actual_value = s.Settings._get_derivation_cell_positions_y(16)
        expected_value = [
            192, 192, 192, 192, 192,
            128, 128, 128, 128, 128,
            64, 64, 64, 64, 64,
            0]
        if not actual_value == expected_value:
            u.Utilities.print_test_error_message(
                method_name, try_name, expected_value, actual_value)

    method_name = '_get_derivation_cell_positions_y'
    try_16_labeled_shapes()

# test_get_right_frame_position()
test_get_derivation_element_positions()
# test__get_derivation_cell_positions_x()
# test__get_derivation_cell_positions_y()
# test__get_triple_from_point3d()

