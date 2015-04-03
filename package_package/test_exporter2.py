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
                                                ##  pending
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
        labeled_shape_name = rs.GetString("Enter the labeled shape name")
        actual_value = (
            my_exporter2._get_labeled_shape_from_labeled_shape_name(
                labeled_shape_name))
        expected_value = the_labeled_shape
        if not actual_value == expected_value:
            g.Grammar.print_test_error_message(
                method_name, try_name, expected_value, actual_value)
        
    # try_bad_value_labeled_shape_name()
    try_good_arg()

def test__get_elements_from_labeled_shape_name():
                                                ##  03-21 08:44
    method_name = '_get_elements_from_labeled_shape_name'

    def try_lines_textdots_annotations_other():
        try_name = 'lines_textdots_annotations_other'
        g.Grammar.clear_all()
        _set_up_labeled_shapes()
        my_e2 = e2.Exporter2()
        labeled_shape_name = rs.GetString(
            "Enter the name of the 3-4-5 triangle")
        actual_value = my_e2._get_elements_from_labeled_shape_name(
            labeled_shape_name)
        expected_value = (
            [   ((0, 0, 0), (0, 20, 0)),
                ((0, 0, 0), (15, 0, 0)),
                ((0, 20, 0), (15, 0, 0))], 
            [((5, 5, 0), 'p11')])
        if not actual_value == expected_value:
            g.Grammar.print_test_error_message(
                method_name, try_name, expected_value, actual_value)

    def try_empty():
        pass

    try_lines_textdots_annotations_other()      ##  under construction
    # try_empty()                                 ##  pending

def test__sort_guids():
    method_name = '_sort_guids'

    def try_lines_textdots_annotations_other():
        try_name = 'lines_textdots_annotations_other'
        g.Grammar.clear_all()
        guids = _make_lines_labeled_points_other()
        my_e2 = e2.Exporter2()
        lines, lpoints = my_e2._sort_guids(guids)
        guids_are_lines = _are_lines(lines)
        guids_are_textdots = _are_textdots(lpoints)
        actual_value = (guids_are_lines, guids_are_textdots)
        expected_value = (True, True)
        if actual_value == expected_value:
            g.Grammar.print_test_error_message(
                method_name, try_name, expected_value, actual_value)

    def try_empty():
        try_name = 'empty'
        g.Grammar.clear_all()
        empty_guids = []
        my_e2 = e2.Exporter2()
        actual_value = my_e2._sort_guids(empty_guids)
        expected_value = ([], [])
        if not actual_value == expected_value:
            g.Grammar.print_test_error_message(
                method_name, try_name, expected_value, actual_value)

    try_lines_textdots_annotations_other()
    try_empty()

def test__get_line_specs():
    method_name = '_get_line_specs'

    def try_bad_type_non_list():
        try_name = "bad_type_non_list"
        g.Grammar.clear_all()
        bad_type_non_list = 37
        my_e2 = e2.Exporter2()
        actual_value = my_e2._get_line_specs(bad_type_non_list)
        expected_value = None
        if not actual_value == expected_value:
            g.Grammar.print_test_error_message(
                method_name, try_name, expected_value, actual_value)

    def try_bad_type_non_lines():
        try_name = "bad_type_non_lines"
        g.Grammar.clear_all()
        bad_type_non_lines = [23, 37]
        my_e2 = e2.Exporter2()
        actual_value = my_e2._get_line_specs(bad_type_non_lines)
        expected_value = None
        if not actual_value == expected_value:
            g.Grammar.print_test_error_message(
                method_name, try_name, expected_value, actual_value)

    def try_good_arg_empty():
        try_name = "good_arg_empty"
        g.Grammar.clear_all()
        good_arg_empty = []
        my_e2 = e2.Exporter2()
        actual_value = my_e2._get_line_specs(good_arg_empty)
        expected_value = []
        if not actual_value == expected_value:
            g.Grammar.print_test_error_message(
                method_name, try_name, expected_value, actual_value)

    def try_good_arg_lines():
        try_name = 'good_arg_lines'
        g.Grammar.clear_all()
        my_e2 = e2.Exporter2()
        l1155 = rs.AddLine((1, 1, 0), (5, 5, 0))
        l1551 = rs.AddLine((1, 5, 0), (5, 1, 0))
        good_arg_lines = [l1155, l1551]
        actual_value = my_e2._get_line_specs(good_arg_lines)
        expected_value = [((1, 1, 0), (5, 5, 0)), ((1, 5, 0), (5, 1, 0))]
        if not actual_value == expected_value:
            g.Grammar.print_test_error_message(
                method_name, try_name, expected_value, actual_value)

    try_bad_type_non_list()                     ##  done
    try_bad_type_non_lines()                    ##  done
    try_good_arg_empty()                        ##  done
    try_good_arg_lines()                        ##  done

def test__get_lpoint_specs():                   ##  04-02 09:25
    method_name = '_get_lpoint_specs'

    def try_bad_type_non_list():
        try_name = 'bad_type_non_list'
        g.Grammar.clear_all()
        bad_type_non_list = 37
        my_e2 = e2.Exporter2()
        actual_value = my_e2._get_lpoint_specs(bad_type_non_list)
        expected_value = None
        if not actual_value == expected_value:
            g.Grammar.print_test_error_message(
                method_name, try_name, expected_value, actual_value)


    def try_bad_type_non_lpoints():
        try_name = 'bad_type_non_lpoints'
        g.Grammar.clear_all()
        bad_type_non_lpoints = [23, 37]
        my_e2 = e2.Exporter2()
        actual_value = my_e2._get_lpoint_specs(bad_type_non_lpoints)
        expected_value = None
        if not actual_value == expected_value:
            g.Grammar.print_test_error_message(
                method_name, try_name, expected_value, actual_value)

    def try_good_arg_empty():
        try_name = 'good_arg_empty'
        g.Grammar.clear_all()
        good_arg_empty = []
        my_e2 = e2.Exporter2()
        actual_value = my_e2._get_lpoint_specs(good_arg_empty)
        expected_value = []
        if not actual_value == expected_value:
            g.Grammar.print_test_error_message(
                method_name, try_name, expected_value, actual_value)

    def try_good_arg_lpoints():
        pass

    # try_bad_type_non_list()                     ##  done
    # try_bad_type_non_lpoints()                  ##  done
    try_good_arg_empty()
    # try_good_arg_lpoints()

### test methods
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
    textdot = rs.AddTextDot(label, p_world)
    return textdot
    
def _draw_point(center, radius=0.5):
    point = rs.AddSphere(center, radius)
    return point

def _draw_text(label, point, height=2):
    text = rs.AddText(label, point, height)
    return text

def _get_point_world_from_local(p_local, origin):
    """Converts a point to world coordinates from local coordinates. Receives:
        p_local             point3d. The point in local coordinates
        origin              point3d. The local origin
    Returns:
        point3d             The point in world coordinates
    """
    p_world = rs.PointAdd(p_local, origin)
    return p_world

def _make_lines_labeled_points_other():
    lines = _make_lines()
    lpoints = _make_labeled_points()
    others = _make_others()
    lines_lpoints_others = []
    lines_lpoints_others.extend(lines)
    lines_lpoints_others.extend(lpoints)
    lines_lpoints_others.extend(others)
    return lines_lpoints_others

def _make_lines():
    p11 = (10, 10, 0)
    p15 = (10, 50, 0)
    p51 = (50, 10, 0)
    p55 = (50, 50, 0)
    l1155 = rs.AddLine(p11, p55)
    l1551 = rs.AddLine(p15, p51)
    return [l1155, l1551]
    
def _make_labeled_points():
    p22 = (20, 20, 0)
    p44 = (40, 40, 0)
    td22 = rs.AddTextDot('td22', p22)
    td44 = rs.AddTextDot('td44', p44)
    return [td22, td44]
    
def _make_others():
    other1 = rs.AddSphere((10, 10, 0), 1)
    other2 = rs.AddSphere((50, 50, 0), 1)
    return [other1, other2]
        
def _are_lines(guids):
    value = True
    for guid in guids:
        if not rs.IsLine(guid):
            value = False
            break
    return value

def _are_textdots(guids):
    value = True
    for guid in guids:
        if not rs.IsTextDot(guid):
            value = False
            break
    return value

### rule methods
# test_export_rule()
# test__get_rule()
# test__get_selected_rule_name()
# test__get_rule_name_tag_from()
# test__get_labeled_shape_names_from_rule_name()
# test__get_labeled_shapes_from_labeled_shape_names()

### shared methods
# test__get_labeled_shape_from_labeled_shape_name()
                                                ##  03-19 09:18 pending
# test__get_elements_from_labeled_shape_name()    ##  pending
# test__sort_guids()                              ##  done
# test__get_line_specs()                          ##  done
test__get_lpoint_specs()                        ##  under construction
# test__write_file()                              ##  done
# test__get_filter_from_file_type()               ##  done

### test utility methods
# _set_up_labeled_shapes()                        ##  done
