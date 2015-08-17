from package.translators import exporter as e
from package.scripts import frame as f
from package.scripts import grammar as g
from package.scripts import rule as r
from package.scripts import initial_shape as ish
import rhinoscriptsyntax as rs

method_name = '_write_file'
bad_type_file_type = 37
bad_type_string = 37
bad_value_file_type = 'txt'
file_type = 'is'
shape_name = 'test name'
string = 'test string'

### initial shape methods
# def test_export_initial_shape():
    # pass

### rule methods
# def test_export_rule():
    # pass

def test__get_rule_name():
    method_name = '_get_rule_name'

    def try_bad_type_preselection():
        def set_up_bad_type_preselection():
            g.Grammar.clear_all()
            f.Frame.new()
            r.Rule.add_first()
            line = rs.AddLine((0, 0, 0), (20, 20, 0))
            text = rs.AddText('label', (10, 10, 0), 2)
            rs.SelectObject(line)

        try_name = 'bad_type_preselection'
        set_up_bad_type_preselection()
        my_ex = e.Exporter()
        actual_value = my_ex._get_rule_name()
        expected_value = 'rule_1'
        if not actual_value == expected_value:
            g.Grammar.print_test_error_message(
                method_name, try_name, expected_value, actual_value)

    def try_bad_value_preselection():
        pass

    def try_good_type_preselection():
        def set_up_good_type_selection():
            g.Grammar.clear_all()
            f.Frame.new()
            r.Rule.add_first()

        try_name = 'good_type_selection'
        set_up_good_type_selection()
        # my_ex = e.Exporter()
        # actual_value = my_ex._get_rule_name()
        # expected_value = 'rule_name'
        # if not actual_value == expected_value:
        #     g.Grammar.print_test_error_message(
        #         method_name, try_name, expected_value, actual_value)

    def try_no_selection():
        pass

    try_bad_type_preselection()
    # try_bad_value_preselection()
    # try_good_type_preselection()
    # try_no_selection()

def test__a_rule_name_tag_is_selected():
    method_name = "_a_rule_name_is_selected"

    def try_bad_type():
        def set_up_bad_type_selection():
            g.Grammar.clear_all()
            f.Frame.new()
            r.Rule.add_first()
            line = rs.AddLine((0, 0, 0), (10, 10, 0))
            lpoint = rs.AddTextDot('textdot', (5, 5, 0))
            rs.SelectObject(line)

        try_name = "bad_type"
        set_up_bad_type_selection()
        my_ex = e.Exporter()
        actual_value = my_ex._a_rule_name_tag_is_selected()
        expected_value = False
        if not actual_value == expected_value:
            g.Grammar.print_test_error_message(
                method_name, try_name, expected_value, actual_value)

    def try_bad_value():
        def set_up_bad_value_selection():
            g.Grammar.clear_all()
            f.Frame.new()
            r.Rule.add_first()
            line = rs.AddLine((0, 0, 0), (10, 10, 0))
            lpoint = rs.AddTextDot('textdot', (10, 10, 0))
            text = rs.AddText('text', (5, 5, 0), 2)
            rs.SelectObject(text)

        try_name = "bad_value"
        set_up_bad_value_selection()
        my_ex = e.Exporter()
        actual_value = my_ex._a_rule_name_tag_is_selected()
        expected_value = False
        if not actual_value == expected_value:
            g.Grammar.print_test_error_message(
                method_name, try_name, expected_value, actual_value)

    def try_no_selection():
        def set_up_no_selection():
            g.Grammar.clear_all()
            f.Frame.new()
            r.Rule.add_first()
            line = rs.AddLine((0, 0, 0), (10, 10, 0))
            lpoint = rs.AddTextDot('textdot', (10, 10, 0))
            text = rs.AddText('text', (5, 5, 0), 2)

        try_name = "none"
        set_up_no_selection()
        my_ex = e.Exporter()
        actual_value = my_ex._a_rule_name_tag_is_selected()
        expected_value = False
        if not actual_value == expected_value:
            g.Grammar.print_test_error_message(
                method_name, try_name, expected_value, actual_value)

    def try_good_arg():
        def set_up_good_arg():
            g.Grammar.clear_all()
            f.Frame.new()
            r.Rule.add_first()
            line = rs.AddLine((0, 0, 0), (10, 10, 0))
            lpoint = rs.AddTextDot('textdot', (10, 10, 0))
            text = rs.AddText('text', (5, 5, 0), 2)
            message = "Select the rule name tag"
            rule_name_tag = rs.GetObject(message)
            rs.SelectObject(rule_name_tag)

        try_name = "good_value"
        set_up_good_arg()
        my_ex = e.Exporter()
        actual_value = my_ex._a_rule_name_tag_is_selected()
        expected_value = True
        if not actual_value == expected_value:
            g.Grammar.print_test_error_message(
                method_name, try_name, expected_value, actual_value)

    try_bad_type()
    try_bad_value()
    try_no_selection()
    try_good_arg()

def test__get_rule_name_tag():
    def set_up():
        g.Grammar.clear_all()
        f.Frame.new()
        r.Rule.add_first()

    method_name = "_get_rule_name_tag"
    try_name = 'try_any'
    set_up()
    my_ex = e.Exporter()
    actual_guid = my_ex._get_rule_name_tag()
    actual_value = rs.TextObjectText(actual_guid)
    expected_value = 'rule_1'
    if not actual_value == expected_value:
        g.Grammar.print_test_error_message(
            method_name, try_name, expected_value, actual_value)

def test__get_rule_name_from():
    def set_up_rule_name_tag():
        g.Grammar.clear_all()
        f.Frame.new()
        r.Rule.add_first()
        message = "Test: select the rule name tag"
        text_filter = 512
        rule_name_tag = rs.GetObject(message, text_filter)
        return rule_name_tag

    method_name = '_get_rule_name_from'
    try_name = 'try_any'
    rule_name_tag = set_up_rule_name_tag()
    my_ex = e.Exporter()
    actual_value = my_ex._get_rule_name_from(rule_name_tag)
    expected_value = 'rule_1'
    if not actual_value == expected_value:
        g.Grammar.print_test_error_message(
            method_name, try_name, expected_value, actual_value)

def test__get_spec_from_rule_name():            ##  05-02 07:03
    def try_good_arg():
        try_name = 'good_arg'
        g.Grammar.clear_all()
        f.Frame.new()
        r.Rule.add_first()
        my_ex = e.Exporter()
        good_arg = 'rule_1'
        actual_value = my_ex._get_spec_from_rule_name(good_arg)
        expected_value = good_arg
        if not actual_value == expected_value:
            g.Grammar.print_test_error_message(
                method_name, try_name, expected_value, actual_value)
        
    method_name = '_get_spec_from_rule_name'
    try_good_arg()

def test__get_shape_guids_from_rule_name():     ##  05-02 10:19
    def set_up():
        g.Grammar.clear_all()
        f.Frame.new()
        r.Rule.add_first()
        sierpinski_before_spec = _make_sierpinski_before_spec()
        sierpinski_after_spec = _make_sierpinski_after_spec()
        left_shape_origin = (0, -100, 0)
        right_shape_origin = (48, -100, 0)
        _draw_labeled_shape(sierpinski_before_spec, left_shape_origin)
        _draw_labeled_shape(sierpinski_after_spec, right_shape_origin)

    method_name = '_get_guids_from_rule_name'
    try_name = 'good_arg'
    set_up()
    my_ex = e.Exporter()
    rule_name = 'rule_1'
    left_guids, right_guids = my_ex._get_shape_guids_from_rule_name(rule_name)
    actual_value = my_ex._get_shape_guids_from_rule_name(rule_name)
    expected_value = ''
    if not actual_value == expected_value:
        g.Grammar.print_test_error_message(
            method_name, try_name, expected_value, actual_value)

def test__get_shape_names_from_rule_name():
    def set_up():
        g.Grammar.clear_all()
        f.Frame.new()
        r.Rule.add_first()

    method_name = '_get_shape_names_from_rule_name'
    try_name = 'good_arg'
    set_up()
    my_ex = e.Exporter()
    rule_name = 'rule_1'
    actual_value = my_ex._get_shape_names_from_rule_name(rule_name)
    expected_value = ('rule_1_L', 'rule_1_R')
    if not actual_value == expected_value:
        g.Grammar.print_test_error_message(
            try_name, method_name, expected_value, actual_value)

def test__get_guids_from_shape_name():
    def _are_5_objects(items):
        value = True
        if not len(items) == 5:
            value = False
        else: 
            for item in items:
                if not rs.IsObject(item):
                    value = False
                    break
        return value

    method_name = '_get_shape_guids_from_shape_name'
    try_name = 'good_arg'
    _set_up_labeled_shapes()
    my_ex = e.Exporter()
    message = "Enter name of 3-4-5 triangle"
    shape_name = rs.GetString(message)
    guids = my_ex._get_shape_guids_from_shape_name(shape_name)
    actual_value = _are_5_objects(guids)
    expected_value = True
    if not actual_value == expected_value:
        g.Grammar.print_test_error_message(
            method_name, try_name, expected_value, actual_value)

# def test__get_rule_repr_from_spec()

### shared methods
def test__get_labeled_shape_from_labeled_shape_name():  ##  04-14 08:54
    method_name = "_get_labeled_shape_from_labeled_shape_name"

    def try_bad_value_labeled_shape_name():
        try_name = 'bad_value_labeled_shape_name'
        bad_value_labeled_shape_name = "bad_value_labeled_shape_name"
        _set_up_labeled_shapes()
        my_exporter = e.Exporter()
        actual_value = (
            my_exporter._get_labeled_shape_from_labeled_shape_name(
                bad_value_labeled_shape_name))
        expected_value = None
        if not actual_value == expected_value:
            g.Grammar.print_test_error_message(
                method_name, try_name, expected_value, actual_value)

    def try_good_arg():
        try_name = "good_arg"
        _set_up_labeled_shapes()
        my_exporter = e.Exporter()
        labeled_shape_name = rs.GetString("Enter the labeled shape name")
        actual_value = (
            my_exporter._get_labeled_shape_from_labeled_shape_name(
                labeled_shape_name))
        expected_value = the_labeled_shape
        if not actual_value == expected_value:
            g.Grammar.print_test_error_message(
                method_name, try_name, expected_value, actual_value)
        
    # try_bad_value_labeled_shape_name()          ##  done
    try_good_arg()

def test__get_spec_from_labeled_shape_name():   ##  05-10 06:29
    pass

def test__get_elements_from_labeled_shape_name():
    method_name = '_get_elements_from_labeled_shape_name'

    def try_lines_textdots_annotations_other():
        try_name = 'lines_textdots_annotations_other'
        g.Grammar.clear_all()
        _set_up_labeled_shapes()
        my_ex = e.Exporter()
        labeled_shape_name = rs.GetString(
            "Enter the name of the 3-4-5 triangle")
        actual_value = my_ex._get_elements_from_labeled_shape_name(
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
        try_name = 'empty'
        g.Grammar.clear_all()
        _set_up_labeled_shapes()
        my_ex = e.Exporter()
        labeled_shape_name = rs.GetString(
            "Enter the name of the layer to clear")
        select = True
        items_to_clear = rs.ObjectsByLayer(labeled_shape_name)
        rs.DeleteObjects(items_to_clear)
        actual_value = my_ex._get_elements_from_labeled_shape_name(
            labeled_shape_name)
        expected_value = ([], [])
        if not actual_value == expected_value:
            g.Grammar.print_test_error_message(
                method_name, try_name, expected_value, actual_value)

    try_lines_textdots_annotations_other()      ##  done
    try_empty()                                 ##  done

def test__sort_guids():
    method_name = '_sort_guids'

    def try_lines_textdots_annotations_other():
        try_name = 'lines_textdots_annotations_other'
        g.Grammar.clear_all()
        guids = _make_lines_labeled_points_other()
        my_ex = e.Exporter()
        lines, lpoints = my_ex._sort_guids(guids)
        guids_are_lines = _are_lines(lines)
        guids_are_textdots = _are_textdots(lpoints)
        actual_value = (guids_are_lines, guids_are_textdots)
        expected_value = (True, True)
        if not actual_value == expected_value:
            g.Grammar.print_test_error_message(
                method_name, try_name, expected_value, actual_value)

    def try_empty():
        try_name = 'empty'
        g.Grammar.clear_all()
        empty_guids = []
        my_ex = e.Exporter()
        actual_value = my_ex._sort_guids(empty_guids)
        expected_value = ([], [])
        if not actual_value == expected_value:
            g.Grammar.print_test_error_message(
                method_name, try_name, expected_value, actual_value)

    try_lines_textdots_annotations_other()
    try_empty()

# test__extract_line_guids ?
# test__extract_lpoint_guids ?

def test__get_line_specs():
    method_name = '_get_line_specs'

    def try_bad_type_non_list():
        try_name = "bad_type_non_list"
        g.Grammar.clear_all()
        bad_type_non_list = 37
        my_ex = e.Exporter()
        actual_value = my_ex._get_line_specs(bad_type_non_list)
        expected_value = None
        if not actual_value == expected_value:
            g.Grammar.print_test_error_message(
                method_name, try_name, expected_value, actual_value)

    def try_bad_type_non_lines():
        try_name = "bad_type_non_lines"
        g.Grammar.clear_all()
        bad_type_non_lines = [23, 37]
        my_ex = e.Exporter()
        actual_value = my_ex._get_line_specs(bad_type_non_lines)
        expected_value = None
        if not actual_value == expected_value:
            g.Grammar.print_test_error_message(
                method_name, try_name, expected_value, actual_value)

    def try_good_arg_empty():
        try_name = "good_arg_empty"
        g.Grammar.clear_all()
        good_arg_empty = []
        my_ex = e.Exporter()
        actual_value = my_ex._get_line_specs(good_arg_empty)
        expected_value = []
        if not actual_value == expected_value:
            g.Grammar.print_test_error_message(
                method_name, try_name, expected_value, actual_value)

    def try_good_arg_lines():
        try_name = 'good_arg_lines'
        g.Grammar.clear_all()
        my_ex = e.Exporter()
        l1155 = rs.AddLine((1, 1, 0), (5, 5, 0))
        l1551 = rs.AddLine((1, 5, 0), (5, 1, 0))
        good_arg_lines = [l1155, l1551]
        actual_value = my_ex._get_line_specs(good_arg_lines)
        expected_value = [((1, 1, 0), (5, 5, 0)), ((1, 5, 0), (5, 1, 0))]
        if not actual_value == expected_value:
            g.Grammar.print_test_error_message(
                method_name, try_name, expected_value, actual_value)

    try_bad_type_non_list()                     ##  done
    try_bad_type_non_lines()                    ##  done
    try_good_arg_empty()                        ##  done
    try_good_arg_lines()                        ##  done

# test__are_line_guids ?
# test__get_line_spec_from ?
def test__get_lpoint_specs():
    method_name = '_get_lpoint_specs'

    def try_bad_type_non_list():
        try_name = 'bad_type_non_list'
        g.Grammar.clear_all()
        bad_type_non_list = 37
        my_ex = e.Exporter()
        actual_value = my_ex._get_lpoint_specs(bad_type_non_list)
        expected_value = None
        if not actual_value == expected_value:
            g.Grammar.print_test_error_message(
                method_name, try_name, expected_value, actual_value)


    def try_bad_type_non_lpoints():
        try_name = 'bad_type_non_lpoints'
        g.Grammar.clear_all()
        bad_type_non_lpoints = [23, 37]
        my_ex = e.Exporter()
        actual_value = my_ex._get_lpoint_specs(bad_type_non_lpoints)
        expected_value = None
        if not actual_value == expected_value:
            g.Grammar.print_test_error_message(
                method_name, try_name, expected_value, actual_value)

    def try_good_arg_empty():
        try_name = 'good_arg_empty'
        g.Grammar.clear_all()
        good_arg_empty = []
        my_ex = e.Exporter()
        actual_value = my_ex._get_lpoint_specs(good_arg_empty)
        expected_value = []
        if not actual_value == expected_value:
            g.Grammar.print_test_error_message(
                method_name, try_name, expected_value, actual_value)

    def try_good_arg_lpoints():
        try_name = 'good_arg_lpoints'
        my_ex = e.Exporter()
        lpoint_1 = rs.AddTextDot('lp1', [10, 10, 0])
        lpoint_2 = rs.AddTextDot('lp2', [20, 20, 0])
        lpoints = [lpoint_2, lpoint_1]
        actual_value = my_ex._get_lpoint_specs(lpoints)
        expected_value = [((10, 10, 0), 'lp1'), ((20, 20, 0), 'lp2')]
        if not actual_value == expected_value:
            g.Grammar.print_test_error_message(
                method_name, try_name, expected_value, actual_value)

    try_bad_type_non_list()                     ##  done
    try_bad_type_non_lpoints()                  ##  done
    try_good_arg_empty()                        ##  done
    try_good_arg_lpoints()                      ##  done

# test__are_lpoint_guids ?
# test__get_lpoint_spec ?
def test__write_file():
    method_name = '_write_file'

    def try_bad_type_file_type():
        try_name = 'bad_type_file_type'
        my_exporter = e.Exporter()
        actual_value = my_exporter._write_file(
            bad_type_file_type, shape_name, string)
        expected_value = None
        if not actual_value == expected_value:
            g.Grammar.print_test_error_message(
                method_name, try_name, expected_value, actual_value)
        
    def try_bad_type_string():
        try_name = 'bad_type_file_string'
        my_exporter = e.Exporter()
        actual_value = my_exporter._write_file(
            file_type, shape_name, bad_type_string)
        expected_value = None
        if not actual_value == expected_value:
            g.Grammar.print_test_error_message(
                method_name, try_name, expected_value, actual_value)
        
    def try_bad_value_file_type():
        try_name = 'bad_value_file_type'
        my_exporter = e.Exporter()
        actual_value = my_exporter._write_file(
            bad_value_file_type, shape_name, string)
        expected_value = None
        if not actual_value == expected_value:
            g.Grammar.print_test_error_message(
                method_name, try_name, expected_value, actual_value)

    def try_good_args():
        try_name = 'good_args'
        my_exporter = e.Exporter()
        actual_value = my_exporter._write_file(file_type, shape_name, string)
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
        my_exporter = e.Exporter()
        actual_value = my_exporter._get_filter_from_file_type(file_type)
        expected_value = "IS file (*.is)|*.is|All files (*.*)|*.*||"
        if not actual_value == expected_value:
            g.Grammar.print_test_error_message(
                method_name, try_name, expected_value, actual_value)

    try_good_arg()

### test methods
def _set_up_labeled_shapes():
    """Draws two labeled shape and name tags
    """
    g.Grammar.clear_all()
    f.Frame.new()
    _draw_triangle_345_on_layer()
    _draw_triangle_12_on_layer()

def _draw_triangle_345_on_layer():
    name = ish.InitialShape.add_subsequent()
    rs.CurrentLayer(name)
    tri_345 = _make_triangle_345_spec()
    tri_345_origin = (0, 0, 0)
    _draw_labeled_shape(tri_345, tri_345_origin)
    rs.CurrentLayer('Default')

def _make_triangle_345_spec():
    p00 = (0, 0, 0)
    p11 = (5, 5, 0)
    p04 = (0, 20, 0)
    p30 = (15, 0, 0)
    lines = [(p00, p04), (p00, p30), (p04, p30)]
    labeled_points = [(p11, 'p11')]
    return (lines, labeled_points)

def _draw_triangle_12_on_layer():
    name = ish.InitialShape.add_subsequent()
    rs.CurrentLayer(name)
    tri_12 = _make_triangle_12_spec()
    tri_12_origin = (0, 50, 0)
    _draw_labeled_shape(tri_12, tri_12_origin)
    rs.CurrentLayer('Default')

def _make_triangle_12_spec():
    p00 = (0, 0, 0)
    p04 = (0, 20, 0)
    p11 = (5, 5, 0)
    p20 = (10, 0, 0)
    lines = [(p00, p04), (p00, p20), (p04, p20)]
    labeled_points = [(p11, 'p11')]
    return (lines, labeled_points)

def _make_sierpinski_before_spec():
    p00 = (0, 0, 0)
    p08 = (0, 24, 0)
    p22 = (6, 6, 0)
    p60 = (18, 0, 0)
    label = 'x'
    line_specs = [(p08, p60), (p00, p08), (p00, p60)]
    lpoint_specs = [(p22, label)]
    return (line_specs, lpoint_specs)

def _make_sierpinski_after_spec():
    p00 = (0, 0, 0)
    p04 = (0, 12, 0)
    p08 = (0, 24, 0)
    p11 = (3, 3, 0)
    p15 = (3, 15, 0)
    p22 = (6, 6, 0)
    p30 = (9, 0, 0)
    p34 = (9, 12, 0)
    p41 = (12, 3, 0)
    p60 = (18, 0, 0)
    label = 'x'
    line_specs = [(p30, p34), (p00, p08), (p00, p60), (p04, p30), (p04, p34),
        (p08, p60)]
    lpoint_specs = [(p41, label), (p11, label), (p15, label)]
    return (line_specs, lpoint_specs)

def _draw_labeled_shape(labeled_shape_spec, origin):
    """Draws a labeled shape. Receives:
        labeled_shape_spec  ([(point3d, point3d), ...], [(point3d, str), ...])
        origin              point3d, z = 0
    """
    lines, labeled_points = labeled_shape_spec
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

# def _get_spec_set_from_guids(guids):                ##  05-08 09:18
    # spec = []
    # for guid in guids:
    #     if rs.IsTextDot(guid):
    #         label = rs.TextDotText(guid)
    #         point = rs.TextDotPoint(guid)
    #         spec_item = (label, point)
    #     elif rs.IsLine(guid):
    #         tail = rs.CurveStartPoint(guid)
    #         head = rs.CurveEndPoint(guid)
    #         spec_item = (tail, head)
    #     else:
    #         pass
    #     spec.append(spec_item)
    # spec_set = set(spec)
    # return spec_set

### rule methods
# test_export_initial_shape()
# test_export_rule()

# test__get_rule_name()                           ##  done
# test__a_rule_name_tag_is_selected()             ##  done
# test__get_rule_name_tag()
# test__get_rule_name_from()
# test__get_spec_from_rule_name()

# test__get_shape_guids_from_rule_name()          ##  suspend?
# test__get_shape_names_from_rule_name()          ##  done
# test__get_guids_from_shape_name()         ##  done

### shared methods
test__get_spec_from_labeled_shape_name()
# test__get_labeled_shape_from_labeled_shape_name()
# test__get_elements_from_labeled_shape_name()    ##  done _get_specs_from...?
# test__sort_guids()                              ##  done
# test__extract_line_guids() ?
# test__extract_lpoint_guids() ?
# test__get_line_specs()                          ##  done
# test__are_line_guids() ?
# test__get_line_spec_from() ?
# test__get_lpoint_specs()                        ##  done
# test__are_lpoint_guids() ?
# test__get_lpoint_spec() ?
# test__write_file()                              ##  done
# test__get_filter_from_file_type()               ##  done

### test utility methods
# _set_up_labeled_shapes()                        ##  done
