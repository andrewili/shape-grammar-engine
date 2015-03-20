from package.translators import exporter2 as e2
from package.view import frame_block as fb
from package.view import grammar as g
from package.view import initial_shape as ish
import rhinoscriptsyntax as rs

method_name = '_write_file'
bad_type_file_type = 37
bad_type_string = 37
bad_value_file_type = 'txt'
file_type = 'is'
shape_name = 'test name'
string = 'test string'

### rule methods
def test__get_selected_rule_name():
    method_name = '_get_rule_name_selection'

    def try_bad_selection():
        try_name = 'bad_selection'

        def set_up_bad_selection():
            g.Grammar.clear_all()
            line = rs.AddLine([0, 0, 0], [10, 10, 0])
            rs.SelectObject(line)
            rs.AddText('rule name', [0, 10, 0], 2)

        set_up_bad_selection()
        my_exporter2 = e2.Exporter2()
        actual_value = my_exporter2._get_rule_name_selection()
        expected_value = 'rule name'
        if not actual_value == expected_value:
            g.Grammar.print_test_error_message(
                expected_value, actual_value, method_name, try_name)

    def try_good_selection():
        pass

    def try_no_selection():
        pass

    try_bad_selection()
    # try_good_selection()
    # try_no_selection()

def test__write_file():
    method_name = '_write_file'

    def try_bad_type_file_type():
        try_name = 'bad_type_file_type'
        my_exporter2 = e2.Exporter2()
        actual_value = my_exporter2._write_file(
            bad_type_file_type, shape_name, string)
        expected_value = None
        if not actual_value == expected_value:
            g.Grammar.print_test_error_message(
                method_name, try_name, expected_value, actual_value)
        
    def try_bad_type_string():
        try_name = 'bad_type_file_string'
        my_exporter2 = e2.Exporter2()
        actual_value = my_exporter2._write_file(
            file_type, shape_name, bad_type_string)
        expected_value = None
        if not actual_value == expected_value:
            g.Grammar.print_test_error_message(
                method_name, try_name, expected_value, actual_value)
        
    def try_bad_value_file_type():
        try_name = 'bad_value_file_type'
        my_exporter2 = e2.Exporter2()
        actual_value = my_exporter2._write_file(
            bad_value_file_type, shape_name, string)
        expected_value = None
        if not actual_value == expected_value:
            g.Grammar.print_test_error_message(
                method_name, try_name, expected_value, actual_value)

    def try_good_args():
        try_name = 'good_args'
        my_exporter2 = e2.Exporter2()
        actual_value = my_exporter2._write_file(file_type, shape_name, string)
        expected_value = string
        if not actual_value == expected_value:
            g.Grammar.print_test_error_message(
                method_name, try_name, expected_value, actual_value)

    try_bad_type_file_type()
    try_bad_type_string()
    try_bad_value_file_type()
    try_good_args()

def test__get_filter_from_file_type():
    method_name = '_get_filter_from_file_type'

    def try_good_arg():
        try_name = 'good_arg'
        my_exporter2 = e2.Exporter2()
        actual_value = my_exporter2._get_filter_from_file_type(file_type)
        expected_value = "IS file (*.is)|*.is|All files (*.*)|*.*||"
        if not actual_value == expected_value:
            g.Grammar.print_test_error_message(
                method_name, try_name, expected_value, actual_value)

    try_good_arg()

### shared methods
def test__get_labeled_shape_from_labeled_shape_name():
    method_name = "_get_labeled_shape_from_labeled_shape_name"

    def try_bad_value_labeled_shape_name():
        try_name = 'bad_value_labeled_shape_name'
        bad_value_labeled_shape_name = "bad_value_labeled_shape_name"
        _set_up_labeled_shapes()
        my_exporter2 = e2.Exporter2()
        actual_value = (
            my_exporter2._get_labeled_shape_from_labeled_shape_name(
                bad_value_labeled_shape_name))
        expected_value = None
        if not actual_value == expected_value:
            g.Grammar.print_test_error_message(
                method_name, try_name, expected_value, actual_value)

    def try_good_arg():
        try_name = "good_arg"
        _set_up_labeled_shapes()
        my_exporter2 = e2.Exporter2()
        the_labeled_shape_name = rs.GetString("Enter the labeled shape name")
        actual_value = (
            my_exporter2._get_labeled_shape_from_labeled_shape_name(
                the_labeled_shape_name))
        expected_value = the_labeled_shape
        if not actual_value == expected_value:
            g.Grammar.print_test_error_message(
                method_name, try_name, expected_value, actual_value)
        
    # try_bad_value_labeled_shape_name()
    try_good_arg()

def _set_up_labeled_shapes():
    """Draws two labeled shape and name tags
    """
    g.Grammar.clear_all()
    fb.FrameBlock.new()
    _draw_triangle_3_4_5_on_layer()
    _draw_triangle_1_2_on_layer()

def _draw_triangle_3_4_5_on_layer():
    name = ish.InitialShape.add_subsequent()
    rs.CurrentLayer(name)
    triangle_3_4_5 = _define_triangle_3_4_5()
    triangle_3_4_5_origin = (0, 0, 0)
    _draw_labeled_shape(triangle_3_4_5, triangle_3_4_5_origin)
    rs.CurrentLayer('Default')

def _define_triangle_3_4_5():
    p00 = (0, 0, 0)
    p11 = (5, 5, 0)
    p04 = (0, 20, 0)
    p30 = (15, 0, 0)
    lines = [(p00, p04), (p00, p30), (p04, p30)]
    labeled_points = [(p11, 'p11')]
    return (lines, labeled_points)

def _draw_triangle_1_2_on_layer():
    name = ish.InitialShape.add_subsequent()
    rs.CurrentLayer(name)
    triangle_1_2 = _define_triangle_1_2()
    triangle_1_2_origin = (0, 50, 0)
    _draw_labeled_shape(triangle_1_2, triangle_1_2_origin)
    rs.CurrentLayer('Default')

def _define_triangle_1_2():
    p00 = (0, 0, 0)
    p04 = (0, 20, 0)
    p11 = (5, 5, 0)
    p20 = (10, 0, 0)
    lines = [(p00, p04), (p00, p20), (p04, p20)]
    labeled_points = [(p11, 'p11')]
    return (lines, labeled_points)

def _draw_labeled_shape(labeled_shape, origin):
    """Draws a labeled shape. Receives:
        labeled_shape       ([(point3d, point3d), ...], [(point3d, str), ...])
        origin              point3d, z = 0
    """
    lines, labeled_points = labeled_shape
    _draw_lines(lines, origin)
    _draw_labeled_points(labeled_points, origin)

def _draw_lines(lines, origin):
    """Draws lines with the specified origin. Receives:
        [(point3d, point3d), ...]
                            a list of line end point pairs
        point3d             the origin of the shape
    """
    for line in lines:
        _draw_line(line, origin)

def _draw_line(line, origin):
    """Draws a line with the specified origin. Receives:
        line                (point3d, point3d). The end points of the line
        origin              point3d. The origin
    """
    p1_local, p2_local = line
    p1_world = _get_point_world_from_local(p1_local, origin)
    p2_world = _get_point_world_from_local(p2_local, origin)
    rs.AddLine(p1_world, p2_world)

def _draw_labeled_points(labeled_points, origin):
    """Draws labeled points with the specified origin. Receives:
        [(point3d, str), ...]
                            a list of point-label pairs
        origin              point3d
    """
    for labeled_point in labeled_points:
        _draw_labeled_point(labeled_point, origin)

def _draw_labeled_point(labeled_point, origin):
    """Draws a labeled point with the specified origin. Receives:
        labeled_point       point3d
        origin              point3d
    """
    p_local, label = labeled_point
    p_world = _get_point_world_from_local(p_local, origin)
    rs.AddTextDot(label, p_world)

def _get_point_world_from_local(p_local, origin):
    """Converts a point to world coordinates from local coordinates. Receives:
        p_local             point3d. The point in local coordinates
        origin              point3d. The local origin
    Returns:
        point3d             The point in world coordinates
    """
    p_world = rs.PointAdd(p_local, origin)
    return p_world

### rule methods
# test_export_rule()
# test__get_rule()
# test__get_selected_rule_name()
# test__get_rule_name_tag_from()
# test__get_labeled_shape_names_from_rule_name()
# test__get_labeled_shapes_from_labeled_shape_names()

### shared methods
test__get_labeled_shape_from_labeled_shape_name() ##  03-19 09:18
# test__write_file()                              ##  done
# test__get_filter_from_file_type()               ##  done

### test utility methods
# _set_up_labeled_shapes()                        ##  done
