from package.view import frame as f
from package.view import grammar as g
from package.controller import guids_to_dat as gd
from package.view import layer as l
import rhinoscriptsyntax as rs
from package.tests import utilities as u

def test_get_dat_string():                      ##  07-10 13:32
    def try_no_initial_shape_layer():
        try_name = 'no_initial_shape_layer'

    def try_no_rule_layer():
        try_name = 'no_rule_layer'

    def try_empty_initial_shape():
        try_name = 'empty_initial_shape'

    def try_empty_left_rule_shape():
        try_name = 'empty_left_rule_shape'

    def try_good_grammar():
        try_name = 'good_grammar'

    method_name = 'get_dat_string'
    try_no_initial_shape_layer()
    try_no_rule_layer()
    try_empty_initial_shape()
    try_empty_left_rule_shape()
    try_good_grammar()

def test__make_initial_shape_frame_dict():
    def try_0_ishapes():
        try_name = '0_ishapes'
        g.Grammar.clear_all()
        f.Frame._new_definition()
        initial_shapes = []
        actual_value = gd.GuidsToDat._make_initial_shape_frame_dict(
            initial_shapes)
        expected_value = {}
        if not actual_value == expected_value:
            u.Utilities.print_test_error_message(
                method_name, try_name, expected_value, actual_value)

    def try_3_ishapes():
        try_name = '3_ishapes'
        u.Utilities.make_grammar_3_initial_shapes_3_rules()
        initial_shapes = [
            'labeled_right_triangle_spec',
            'labeled_h_spec',
            'labeled_square_spec']
        actual_value = gd.GuidsToDat._make_initial_shape_frame_dict(
            initial_shapes)
        frames = actual_value.values()
        rs.SelectObjects(frames)

    method_name = '_make_initial_shape_frame_dict'
    try_0_ishapes()
    try_3_ishapes()

def test__make_rule_frame_pair_dict():
    def try_0_rules():
        try_name = '0_rules'
        g.Grammar.clear_all()
        f.Frame._new_definition()
        rules = []
        actual_value = gd.GuidsToDat._make_rule_frame_pair_dict(rules)
        expected_value = {}
        if not actual_value == expected_value:
            u.Utilities.print_test_error_message(
                method_name, try_name, expected_value, actual_value)

    def try_3_rules():
        try_name = '0_rules'
        u.Utilities.make_grammar_3_initial_shapes_3_rules()
        rules = [
            'subdivide_triangle_spec',
            'add_h_to_h_spec',
            'add_h_in_square_spec']
        actual_value = gd.GuidsToDat._make_rule_frame_pair_dict(rules)
        frame_pairs = actual_value.values()
        for pair in frame_pairs:
            rs.SelectObject(pair[0])

    method_name = '_make_rule_frame_pair_dict'
    try_0_rules()
    try_3_rules()

def test__make_labeled_shape_elements_dict():   ##  07-16 07:48
    def try_0_ishapes_0_rules():
        try_name = '0_ishapes_0_rules'
        g.Grammar.clear_all
        f.Frame._new_definition()
        initial_shape_frame_dict = {}
        rule_frame_pair_dict = {}
        actual_value = gd.GuidsToDat._make_labeled_shape_elements_dict(
            initial_shape_frame_dict, rule_frame_pair_dict)
        expected_value = {}
        if not actual_value == expected_value:
            u.Utilities.print_test_error_message(
                method_name, try_name, expected_value, actual_value)

    def try_0_ishapes_3_rules():
        try_name = '0_ishapes_3_rules'

    def try_3_ishapes_0_rules():
        try_name = '3_ishapes_0_rules'

    def try_3_ishapes_3_rules():
        try_name = '3_ishapes_3_rules'

    method_name = '_make_labeled_shape_elements_dict'
    try_0_ishapes_0_rules()
    try_0_ishapes_3_rules()
    try_3_ishapes_0_rules()
    try_3_ishapes_3_rules()

def test__get_elements():
    def try_good_args():
        try_name = 'good_value_empty_frame'
        u.Utilities.make_grammar_3_initial_shapes_4_rules()
        message = "Select a frame instance"
        block_instance_filter = 4096
        frame_instance = rs.GetObject(message, block_instance_filter)
        actual_value = gd.GuidsToDat._get_elements(frame_instance)
        rs.SelectObjects(actual_value)

    method_name = '_get_elements'
    try_good_args()

####

def text__extract_elements_in_frame():          ##  07-12 07:59
    def try_no_objects():
        try_name = 'no_objects'
        g.Grammar.clear_all()
        layer_name = 'layer_x'
        l.Layer.new(layer_name)
        frame_name = layer_name
        frame_position = (0, 0, 0)
        frame_guid = f.Frame.new_instance(
            frame_name, layer_name, frame_position)
        object_guids_on_layer =[]
        actual_value = gd.GuidsToDat._extract_elements_in_frame(
            frame_guid, object_guids_on_layer)
        expected_value = []
        if not actual_value == expected_value:
            u.Utilities.print_test_error_message(
                method_name, try_name, expected_value, actual_value)

    def try_objects():
        try_name = 'objects'
        g.Grammar.clear_all()
        layer_name = 'layer_x'
        l.Layer.new(layer_name)
        frame_name = layer_name
        frame_position = (0, 0, 0)
        frame_guid = f.Frame.new_instance(
            frame_name, layer_name, frame_position)
        object_guids_on_layer = _make_objects_on_layer(layer_name)
        actual_value = gd.GuidsToDat._extract_elements_in_frame(
            frame_guid, object_guids_on_layer)
        rs.SelectObjects(actual_value)
        # expected_value = ?
        # if not set(actual_value) == set(expected_value):
        #     u.Utilities.print_test_error_message(
        #         method_name, try_name, expected_value, actual_value)

    method_name = '_extract_elements_in_frame'
    try_no_objects()
    try_objects()

def test__point_is_in_box():
    def try_point_outside():
        try_name = 'point_is_outside'
        point = (30, -30, 0)
        actual_value = gd.GuidsToDat._point_is_in_box(
            point, box_position, box_size)
        expected_value = False
        if not actual_value == expected_value:
            u.Utilities.print_test_error_message(
                method_name, try_name, expected_value, actual_value)

    def try_point_on_surface():
        try_name = 'point_is_on_surface'
        point = (-10, 10, -25)
        actual_value = gd.GuidsToDat._point_is_in_box(
            point, box_position, box_size)
        expected_value = True
        if not actual_value == expected_value:
            u.Utilities.print_test_error_message(
                method_name, try_name, expected_value, actual_value)

    def try_point_on_edge():
        try_name = 'point_is_on_edge'
        point = (0, -25, 25)
        actual_value = gd.GuidsToDat._point_is_in_box(
            point, box_position, box_size)
        expected_value = True
        if not actual_value == expected_value:
            u.Utilities.print_test_error_message(
                method_name, try_name, expected_value, actual_value)

    def try_point_on_vertex():
        try_name = 'point_is_on_vertex'
        point = (-25, 25, -25)
        actual_value = gd.GuidsToDat._point_is_in_box(
            point, box_position, box_size)
        expected_value = True
        if not actual_value == expected_value:
            u.Utilities.print_test_error_message(
                method_name, try_name, expected_value, actual_value)

    def try_point_inside():
        try_name = 'point_is_inside'
        point = (5, -10, 15)
        actual_value = gd.GuidsToDat._point_is_in_box(
            point, box_position, box_size)
        expected_value = True
        if not actual_value == expected_value:
            u.Utilities.print_test_error_message(
                method_name, try_name, expected_value, actual_value)

    method_name = '_point_is_in_box'
    g.Grammar.clear_all()
    box_position = (-25, -25, -25)
    box_size = (50, 50, 50)
    try_point_outside()
    try_point_on_surface()
    try_point_on_edge()
    try_point_on_vertex()
    try_point_inside()

def test__make_labeled_shape_name_dat_dict():   ##  07-10 14:05
    method_name = '_make_lshape_name_dat_dict'
    try_no_labeled_shape_layers()
    try_no_frame_definition()
    try_empty_initial_shape()
    try_empty_left_rule_shape()
    try_0_initial_shapes_0_rules()
    try_0_initial_shapes_3_rules()
    try_3_initial_shapes_0_rules()
    try_3_initial_shapes_3_rules()

def test__get_ordered_labeled_shape_names():
    def try_bad_state_0_initial_shapes_0_rules():
        try_name = 'bad_state_0_initial_shapes_0_rules'
        u.Utilities.make_grammar_0_initial_shapes_0_rules()
        actual_value = gd.GuidsToDat._get_ordered_labeled_shape_names()
        expected_value = None
        if not actual_value == expected_value:
            u.Utilities.print_test_error_message(
                method_name, try_name, expected_value, actual_value)

    def try_bad_state_0_initial_shapes_3_rules():
        try_name = 'bad_state_no_initial_shapes_rules'
        u.Utilities.make_grammar_0_initial_shapes_3_rules()
        actual_value = gd.GuidsToDat._get_ordered_labeled_shape_names()
        expected_value = None
        if not actual_value == expected_value:
            u.Utilities.print_test_error_message(
                method_name, try_name, expected_value, actual_value)

    def try_bad_state_3_initial_shapes_0_rules():
        try_name = 'bad_state_initial_shapes_no_rules'
        u.Utilities.make_grammar_3_initial_shapes_0_rules()
        actual_value = gd.GuidsToDat._get_ordered_labeled_shape_names()
        expected_value = None
        if not actual_value == expected_value:
            u.Utilities.print_test_error_message(
                method_name, try_name, expected_value, actual_value)

    def try_good_state_3_initial_shapes_3_rules():
        try_name = 'good_state_initial_shapes_rules'
        u.Utilities.make_grammar_3_initial_shapes_3_rules()
        actual_value = gd.GuidsToDat._get_ordered_labeled_shape_names()
        expected_value = 'kilroy'
        if not actual_value == expected_value:
            u.Utilities.print_test_error_message(
                method_name, try_name, expected_value, actual_value)

    method_name = '_get_ordered_labeled_shape_names'
    try_bad_state_0_initial_shapes_0_rules()
    try_bad_state_0_initial_shapes_3_rules()
    try_bad_state_3_initial_shapes_0_rules()
    try_good_state_3_initial_shapes_3_rules()

def test__get_ordered_labeled_shapes_string():
    def try_no_ishapes_no_rules():
        try_name = 'no_ishapes_no_rules'
        g.Grammar.clear_all()
        f.Frame._new_definition()
        actual_value = g.Grammar._get_ordered_labeled_shapes_string()
        expected_value = ''
        if not actual_value == expected_value:
            u.Utilities.print_test_error_message(
                method_name, try_name, expected_value, actual_value)

    def try_no_ishapes_rules():
        try_name = 'no_ishapes_rules'
        pass

    def try_ishapes_no_rules():
        try_name = 'ishapes_no_rules'
        pass

    def try_ishapes_rules():
        try_name = 'ishapes_rules'
        pass

    method_name = '_get_ordered_labeled_shapes_string'
    try_no_ishapes_no_rules()
    # try_no_ishapes_rules()
    # try_ishapes_no_rules()
    # try_ishapes_rules()

def test__get_ordered_initial_shape_defs_string():
    def try_good_state_no_ishapes_no_rules():
        try_name = 'good_state_no_ishapes_no_rules'
        _set_up()
        actual_value = g.Grammar._get_ordered_named_initial_shape_defs_string()
        expected_value = ''
        # if actual_value == expected_value:
        if not actual_value == expected_value:
            u.Utilities.print_test_error_message(
                method_name, try_name, expected_value, actual_value)

    def try_good_state_no_ishapes_rules():
        try_name = 'good_state_no_ishapes_rules'
        _make_new_grammar_3_rules()
        actual_value = g.Grammar._get_ordered_named_initial_shape_defs_string()
        expected_value = ''
        if not actual_value == expected_value:
            u.Utilities.print_test_error_message(
                method_name, try_name, expected_value, actual_value)

    def try_good_state_ishapes_no_rules():
        try_name = 'good_state_ishapes_no_rules'
        _make_new_grammar_3_ishapes()
        name_1, name_2, name_3 = 'a_ishape', 'initial_shape_1', 'z_ishape'
        actual_value = g.Grammar._get_ordered_named_initial_shape_defs_string()
        expected_value = "%s\n%s\n%s" % (
            "shape    %s" % (name_1),
            "shape    %s" % (name_2),
            "shape    %s" % (name_3))
        if not actual_value == expected_value:
            u.Utilities.print_test_error_message(
                method_name, try_name, expected_value, actual_value)

    def try_good_state_ishapes_rules():
        try_name = 'good_state_ishapes_rules'
        _make_new_grammar_3_ishapes_3_rules()
        name_1, name_2, name_3 = 'a_ishape', 'initial_shape_1', 'z_ishape'
        actual_value = g.Grammar._get_ordered_named_initial_shape_defs_string()
        expected_value = "%s\n%s\n%s" % (
            "shape    %s" % (name_1),
            "shape    %s" % (name_2),
            "shape    %s" % (name_3))
        if not actual_value == expected_value:
            u.Utilities.print_test_error_message(
                method_name, try_name, expected_value, actual_value)

    method_name = '_get_ordered_named_initial_shape_defs_string'
    try_good_state_no_ishapes_no_rules()
    try_good_state_no_ishapes_rules()
    try_good_state_ishapes_no_rules()
    try_good_state_ishapes_rules()

def test__get_ordered_rule_defs_string():
    def try_good_state_no_ishapes_no_rules():
        try_name = 'good_state_no_ishapes_no_rules'
        _set_up()
        actual_value = g.Grammar._get_ordered_named_rule_defs_string()
        expected_value = ''
        if not actual_value == expected_value:
            u.Utilities.print_test_error_message(
                method_name, try_name, expected_value, actual_value)

    def try_good_state_no_ishapes_rules():
        try_name = 'good_state_no_ishapes_rules'
        _make_new_grammar_3_rules()
        name_1, name_2, name_3 = 'a_rule', 'rule_1', 'z_rule'
        actual_value = g.Grammar._get_ordered_named_rule_defs_string()
        expected_value = "%s\n%s\n%s" % (
            "rule    %s    %s_L -> %s_R" % (name_1, name_1, name_1),
            "rule    %s    %s_L -> %s_R" % (name_2, name_2, name_2),
            "rule    %s    %s_L -> %s_R" % (name_3, name_3, name_3))
        if not actual_value == expected_value:
            u.Utilities.print_test_error_message(
                method_name, try_name, expected_value, actual_value)

    def try_good_state_ishapes_no_rules():
        try_name = 'good_state_ishapes_no_rules'
        _make_new_grammar_3_ishapes()
        actual_value = g.Grammar._get_ordered_named_rule_defs_string()
        expected_value = ''
        if not actual_value == expected_value:
            u.Utilities.print_test_error_message(
                method_name, try_name, expected_value, actual_value)

    def try_good_state_ishapes_rules():
        try_name = 'good_state_ishapes_rules'
        _make_new_grammar_3_ishapes_3_rules()
        name_1, name_2, name_3 = 'a_rule', 'rule_1', 'z_rule'
        actual_value = g.Grammar._get_ordered_named_rule_defs_string()
        expected_value = "%s\n%s\n%s" % (
                    "rule    %s    %s_L -> %s_R" % (name_1, name_1, name_1),
                    "rule    %s    %s_L -> %s_R" % (name_2, name_2, name_2),
                    "rule    %s    %s_L -> %s_R" % (name_3, name_3, name_3))
        if not actual_value == expected_value:
            u.Utilities.print_test_error_message(
                method_name, try_name, expected_value, actual_value)

    method_name = '_get_ordered_named_rule_defs_string'
    try_good_state_no_ishapes_no_rules()
    try_good_state_no_ishapes_rules()
    try_good_state_ishapes_no_rules()
    try_good_state_ishapes_rules()

def _make_objects_on_layer(layer_name):
    rs.CurrentLayer(layer_name)
    objects = []
    lines = _make_lines()
    textdots = _make_textdots()
    annotations = _make_annotations()
    objects.extend(lines)
    objects.extend(textdots)
    objects.extend(annotations)
    return objects

def _make_lines():
    def _make_line_2_pts_outside():
        p1 = (-5, -5, -5)
        p2 = (40, 40, 40)
        line = rs.AddLine(p1, p2)
        return line

    def _make_line_1_pt_outside_1_pt_on_surface():
        p1 = (-5, -5, -5)
        p2 = (10, 10, 0)
        line = rs.AddLine(p1, p2)
        return line

    def _make_line_1_pt_outside_1_pt_on_edge():
        p1 = (-5, -5, -5)
        p2 = (0, 0, 32)
        line = rs.AddLine(p1, p2)
        return line

    def _make_line_1_pt_outside_1_pt_on_vertex():
        p1 = (-5, -5, -5)
        p2 = (32, 32, 32)
        line = rs.AddLine(p1, p2)
        return line

    def _make_line_1_pt_outside_1_pt_inside():
        p1 = (-5, -5, -5)
        p2 = (10, 10, 10)
        line = rs.AddLine(p1, p2)
        return line

    def _make_line_1_pt_on_surface_1_pt_on_same_surface():
        p1 = (5, 5, 0)
        p2 = (20, 20, 0)
        line = rs.AddLine(p1, p2)
        return line

    def _make_line_1_pt_on_surface_1_pt_on_different_surface():
        p1 = (5, 5, 0)
        p2 = (32, 20, 20)
        line = rs.AddLine(p1, p2)
        return line

    def _make_line_1_pt_on_surface_1_pt_on_adjoining_edge():
        p1 = (5, 5, 0)
        p2 = (32, 20, 0)
        line = rs.AddLine(p1, p2)
        return line

    def _make_line_1_pt_on_surface_1_pt_on_separate_edge():
        p1 = (5, 5, 0)
        p2 = (32, 20, 32)
        line = rs.AddLine(p1, p2)
        return line

    def _make_line_1_pt_on_surface_1_pt_on_adjoining_vertex():
        p1 = (5, 5, 0)
        p2 = (32, 32, 0)
        line = rs.AddLine(p1, p2)
        return line

    def _make_line_1_pt_on_surface_1_pt_on_separate_vertex():
        p1 = (5, 5, 0)
        p2 = (32, 32, 32)
        line = rs.AddLine(p1, p2)
        return line

    def _make_line_1_pt_on_edge_1_pt_on_same_edge():
        p1 = (10, 0, 0)
        p2 = (20, 0, 0)
        line = rs.AddLine(p1, p2)
        return line

    def _make_line_1_pt_on_edge_1_pt_on_different_edge():
        p1 = (10, 0, 0)
        p2 = (32, 20, 0)
        line = rs.AddLine(p1, p2)
        return line

    def _make_line_1_pt_on_edge_1_pt_on_adjoining_vertex():
        p1 = (10, 0, 0)
        p2 = (32, 0, 0)
        line = rs.AddLine(p1, p2)
        return line

    def _make_line_1_pt_on_edge_1_pt_on_separate_vertex():
        p1 = (10, 0, 0)
        p2 = (32, 32, 32)
        line = rs.AddLine(p1, p2)
        return line

    def _make_line_1_pt_on_vertex_1_pt_on_separate_vertex():
        p1 = (0, 0, 0)
        p2 = (32, 32, 32)
        line = rs.AddLine(p1, p2)
        return line

    def _make_line_2_pts_inside():
        p1 = (10, 10, 10)
        p2 = (20, 20, 20)
        line = rs.AddLine(p1, p2)
        return line
    
    line_methods = [
        _make_line_2_pts_outside,
        _make_line_1_pt_outside_1_pt_on_surface,
        _make_line_1_pt_outside_1_pt_on_edge,
        _make_line_1_pt_outside_1_pt_on_vertex,
        _make_line_1_pt_outside_1_pt_inside,
        _make_line_1_pt_on_surface_1_pt_on_same_surface,
        _make_line_1_pt_on_surface_1_pt_on_different_surface,
        _make_line_1_pt_on_surface_1_pt_on_adjoining_edge,
        _make_line_1_pt_on_surface_1_pt_on_separate_edge,
        _make_line_1_pt_on_surface_1_pt_on_adjoining_vertex,
        _make_line_1_pt_on_surface_1_pt_on_separate_vertex,
        _make_line_1_pt_on_edge_1_pt_on_same_edge,
        _make_line_1_pt_on_edge_1_pt_on_different_edge,
        _make_line_1_pt_on_edge_1_pt_on_adjoining_vertex,
        _make_line_1_pt_on_edge_1_pt_on_separate_vertex,
        _make_line_1_pt_on_vertex_1_pt_on_separate_vertex,
        _make_line_2_pts_inside]
    lines = []
    for method in line_methods:
        line = method()
        lines.append(line)
    return lines

def _make_textdots():
    def _make_textdot_outside():
        label = 'a'
        point = (40, 40, 40)
        textdot = rs.AddTextDot(label, point)
        return textdot

    def _make_textdot_on_surface():
        label = 'a'
        point = (10, 10, 0)
        textdot = rs.AddTextDot(label, point)
        return textdot

    def _make_textdot_on_edge():
        label = 'a'
        point = (20, 0, 0)
        textdot = rs.AddTextDot(label, point)
        return textdot

    def _make_textdot_on_vertex():
        label = 'a'
        point = (32, 0, 0)
        textdot = rs.AddTextDot(label, point)
        return textdot

    def _make_textdot_inside():
        label = 'a'
        point = (30, 30, 30)
        textdot = rs.AddTextDot(label, point)
        return textdot

    textdot_methods = [
        _make_textdot_outside,
        _make_textdot_on_surface,
        _make_textdot_on_edge,
        _make_textdot_on_vertex,
        _make_textdot_inside]
    textdots = []
    for method in textdot_methods:
        textdot = method()
        textdots.append(textdot)
    return textdots
    
def _make_annotations():
    def _make_annotation_outside():
        text = 'b'
        position = (40, 20, 20)
        annotation = rs.AddText(text, position)
        return annotation

    def _make_annotation_on_surface():
        text = 'b'
        position = (0, 20, 20)
        annotation = rs.AddText(text, position)
        return annotation

    def _make_annotation_on_edge():
        text = 'b'
        position = (20, 32, 0)
        annotation = rs.AddText(text, position)
        return annotation

    def _make_annotation_on_vertex():
        text = 'b'
        position = (0, 32, 32)
        annotation = rs.AddText(text, position)
        return annotation

    def _make_annotation_inside():
        text = 'b'
        position = (25, 25, 25)
        annotation = rs.AddText(text, position)
        return annotation

    annotation_methods = [
        _make_annotation_outside,
        _make_annotation_on_surface,
        _make_annotation_on_edge,
        _make_annotation_on_vertex,
        _make_annotation_inside]
    annotations = []
    for method in annotation_methods:
        annotation = method()
        annotations.append(annotation)
    return annotations

####

# test_get_dat_string()
# test__make_initial_shape_frame_dict()           ##  manual test / done
# test__make_rule_frame_pair_dict()               ##  manual test / done
# test__make_labeled_shape_elements_dict()        ##  pending
# test__get_elements()                            ##  manual test / done

####

# test__get_ordered_rule_defs_string()
