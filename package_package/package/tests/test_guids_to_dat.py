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

def test__make_labeled_shape_elements_dict():
    def try_0_ishapes_0_rules():
        try_name = '0_ishapes_0_rules'
        u.Utilities.make_grammar_0_initial_shapes_0_rules()
        initial_shape_frame_dict = {}
        rule_frame_pair_dict = {}
        actual_value = gd.GuidsToDat._make_labeled_shape_elements_dict(
            initial_shape_frame_dict, rule_frame_pair_dict)
        expected_value = {}
        if not actual_value == expected_value:
            u.Utilities.print_test_error_message(
                method_name, try_name, expected_value, actual_value)

    def try_3_ishapes_4_rules():
        try_name = '3_ishapes_4_rules'
        u.Utilities.make_grammar_3_initial_shapes_4_rules()
        initial_shapes, rules = g.Grammar.get_initial_shapes_and_rules()
        initial_shape_frame_dict = _prompt_for_initial_shape_elements(
            initial_shapes)
        rule_frame_pair_dict = _prompt_for_rule_elements(rules)
        labeled_shape_elements_dict = (
            gd.GuidsToDat._make_labeled_shape_elements_dict(
                initial_shape_frame_dict, rule_frame_pair_dict))
        for labeled_shape in labeled_shape_elements_dict:
            elements = labeled_shape_elements_dict[labeled_shape]
            frame_guid = elements.pop(0)
            message_show_frame = (
                "Show the frame of the labeled shape '%s'" % labeled_shape)
            rs.MessageBox(message_show_frame)
            rs.UnselectAllObjects()
            rs.SelectObject(frame_guid)
            message_show_elements = (
                "Show the elements in the labeled shape '%s'" % labeled_shape)
            rs.MessageBox(message_show_elements)
            rs.UnselectAllObjects()
            rs.SelectObjects(elements)

    method_name = '_make_labeled_shape_elements_dict'
    try_0_ishapes_0_rules()                     ##  automatic test
    try_3_ishapes_4_rules()                     ##  manual test

def test__get_elements():
    def try_empty_frame():
        try_name = 'empty_frame'
        u.Utilities.make_grammar_1_initial_shape_1_delete_rule()
        message = "%s %s" % (
            "Select the empty frame instance.",
            "Nothing will be selected")
        block_instance_filter = 4096
        frame_instance = rs.GetObject(message, block_instance_filter)
        actual_value = gd.GuidsToDat._get_elements(frame_instance)
        rs.SelectObjects(actual_value)

    def try_good_args():
        try_name = 'good_args'
        u.Utilities.make_grammar_3_initial_shapes_4_rules()
        message = "%s %s" % (
            "Select a frame instance.",
            "The elements in the frame will be selected")
        block_instance_filter = 4096
        frame_instance_in = rs.GetObject(message, block_instance_filter)
        actual_value = gd.GuidsToDat._get_elements(frame_instance_in)
        rs.SelectObjects(actual_value)

    method_name = '_get_elements'
    try_empty_frame()
    try_good_args()

def test__get_ordered_labeled_shapes_string():  ##  07-17 09:20
    def try_0_ishapes_0_rules():
        try_name = '0_ishapes_0_rules'
        u.Utilities.make_grammar_0_initial_shapes_0_rules()
        name_elements_dict = {}
        actual_value = gd.GuidsToDat._get_ordered_labeled_shapes_string(
            name_elements_dict)
        expected_value = None
        if not actual_value == expected_value:
            u.Utilities.print_test_error_message(
                method_name, try_name, expected_value, actual_value)

    def try_1_ishape_1_delete_rule():
        try_name = '1_ishape_1_delete_rule'
        u.Utilities.make_grammar_1_initial_shape_1_delete_rule()
        labeled_shape_name_elements_dict = (
            _prompt_for_labeled_shape_name_elements_dict())
        actual_value = gd.GuidsToDat._get_ordered_labeled_shapes_string(
            labeled_shape_name_elements_dict)
        expected_value = u.Utilities.ordered_labeled_shapes_1_1_string
        if not actual_value == expected_value:
            u.Utilities.print_test_error_message(
                method_name, try_name, expected_value, actual_value)

    def try_3_ishapes_4_rules():
        try_name = '3_ishapes_4_rules'
        u.Utilities.make_grammar_3_initial_shapes_4_rules()
        labeled_shape_name_elements_dict = (
            _prompt_for_labeled_shape_name_elements_dict())
        actual_value = gd.GuidsToDat._get_ordered_labeled_shapes_string(
            labeled_shape_name_elements_dict)
        expected_value = u.Utilities.ordered_labeled_shapes_3_4_string
        if not actual_value == expected_value:
            u.Utilities.print_test_error_message(
                method_name, try_name, expected_value, actual_value)

    method_name = '_get_ordered_labeled_shapes_string'
    # try_0_ishapes_0_rules()                     ##  done
    try_1_ishape_1_delete_rule()                ##  
    # try_3_ishapes_4_rules()                     ##  fix me

def test__get_ordered_line_and_labeled_point_specs():
    def try_0_lines_0_labeled_points():
        try_name = '0_lines_0_labeled_points'
        g.Grammar.clear_all()
        element_guids = []
        actual_value = (
            gd.GuidsToDat._get_ordered_line_and_labeled_point_specs(
                element_guids))
        expected_value = None
        if not actual_value == expected_value:
            u.Utilities.print_test_error_message(
                method_name, try_name, expected_value, actual_value)

    def try_0_lines_4_labeled_points():
        try_name = '0_lines_4_labeled_points'

        u.Utilities.make_grammar_3_initial_shapes_4_rules()
        message_frame = "Select the frame instance of the labeled h"
        frame_instance = rs.GetObject(message_frame, block_instance_filter)
        message_labeled_points = "Select the labeled points in the labeled h"
        element_guids = rs.GetObjects(message_labeled_points, text_dot_filter)
        element_guids.insert(0, frame_instance)
        actual_value = (
            gd.GuidsToDat._get_ordered_line_and_labeled_point_specs(
                element_guids))
        expected_value = (
            [],
            [   ('a', (8, 6, 0)),
                ('a', (8, 26, 0)),
                ('a', (24, 6, 0)),
                ('a', (24, 26, 0))])
        if not actual_value == expected_value:
            u.Utilities.print_test_error_message(
                method_name, try_name, expected_value, actual_value)

    def try_3_lines_0_labeled_points():
        try_name = '3_lines_0_labeled_points'
        u.Utilities.make_grammar_3_initial_shapes_4_rules()

        message_frame = "Select the frame instance of the labeled square"
        frame_instance = rs.GetObject(message_frame, block_instance_filter)
        message_lines = "Select the lines in the labeled square"
        element_guids = rs.GetObjects(message_lines, curve_filter)
        element_guids.insert(0, frame_instance)
        actual_value = (
            gd.GuidsToDat._get_ordered_line_and_labeled_point_specs(
                element_guids))
        expected_value = (
            [   ((4, 4, 0), (4, 28, 0)),
                ((4, 4, 0), (28, 4, 0)),
                ((4, 28, 0), (28, 28, 0)),
                ((28, 4, 0), (28, 28, 0))],
            [])
        if not actual_value == expected_value:
            u.Utilities.print_test_error_message(
                method_name, try_name, expected_value, actual_value)

    def try_3_lines_3_labeled_points():
        try_name = '3_lines_3_labeled_points'
        u.Utilities.make_grammar_3_initial_shapes_4_rules()
        message_frame = "Select the frame instance of the labeled square"
        frame_instance = rs.GetObject(message_frame, block_instance_filter)
        message_elements = "Select the elements of the labeled square"
        element_filter = curve_filter + text_dot_filter
        element_guids = rs.GetObjects(message_elements, element_filter)
        element_guids.insert(0, frame_instance)
        actual_value = (
            gd.GuidsToDat._get_ordered_line_and_labeled_point_specs(
                element_guids))
        expected_value = u.Utilities.labeled_square_spec
        if not actual_value == expected_value:
            u.Utilities.print_test_error_message(
                method_name, try_name, expected_value, actual_value)

    method_name = '_get_ordered_line_and_labeled_point_specs'
    curve_filter = 4
    block_instance_filter = 4096
    text_dot_filter = 8192
    # try_0_lines_0_labeled_points()              ##  done
    # try_0_lines_4_labeled_points()              ##  done
    # try_3_lines_0_labeled_points()              ##  done
    # try_3_lines_3_labeled_points()              ##  done

def test__get_labeled_shape_string():
    def try_0_line_0_labeled_point_specs():
        try_name = '0_line_0_labeled_point_specs'
        line_and_labeled_point_specs = ([], [])
        actual_value = gd.GuidsToDat._get_labeled_shape_string(
            line_and_labeled_point_specs)
        expected_value = '\n'.join([
            '    name'
        ])
        if not actual_value == expected_value:
            u.Utilities.print_test_error_message(
                method_name, try_name, expected_value, actual_value)

    def try_0_line_1_labeled_point_specs():
        try_name = '0_line_1_labeled_point_specs'
        line_and_labeled_point_specs = ([], [lp0])
        actual_value = gd.GuidsToDat._get_labeled_shape_string(
            line_and_labeled_point_specs)
        expected_value = '\n'.join([
            '    name',
            '    coords 0 5 5 0',
            '',
            '    point 0 a'
        ])
        if not actual_value == expected_value:
            u.Utilities.print_test_error_message(
                method_name, try_name, expected_value, actual_value)

    def try_1_line_0_labeled_point_specs():
        try_name = '1_line_0_labeled_point_specs'
        line_and_labeled_point_specs = ([l0], [])
        actual_value = gd.GuidsToDat._get_labeled_shape_string(
            line_and_labeled_point_specs)
        expected_value = '\n'.join([
            '    name',
            '    coords 0 0 10 0',
            '    coords 1 10 0 0',
            '',
            '    line 0 0 1'
        ])
        if not actual_value == expected_value:
            u.Utilities.print_test_error_message(
                method_name, try_name, expected_value, actual_value)

    def try_3_line_3_labeled_point_specs():
        try_name = '3_line_3_labeled_point_specs'
        line_and_labeled_point_specs = ([l2, l1, l0], [lp2, lp1, lp0])
        actual_value = gd.GuidsToDat._get_labeled_shape_string(
            line_and_labeled_point_specs)
        expected_value = '\n'.join([
            '    name',
            '    coords 0 0 10 0',
            '    coords 1 5 5 0',
            '    coords 2 10 0 0',
            '    coords 3 10 20 0',
            '    coords 4 15 15 0',
            '    coords 5 20 10 0',
            '    coords 6 20 30 0',
            '    coords 7 25 25 0',
            '    coords 8 30 20 0',
            '',
            '    line 0 0 2',
            '    line 1 3 5',
            '    line 2 6 8',
            '    point 1 a',
            '    point 4 a',
            '    point 7 a'
        ])
        if not actual_value == expected_value:
            u.Utilities.print_test_error_message(
                method_name, try_name, expected_value, actual_value)

    method_name = '_get_labeled_shape_string'
    g.Grammar.clear_all()
    l0 = ((0, 10, 0), (10, 0, 0))
    l1 = ((10, 20, 0), (20, 10, 0))
    l2 = ((20, 30, 0), (30, 20, 0))
    lp0 = ('a', (5, 5, 0))
    lp1 = ('a', (15, 15, 0))
    lp2 = ('a', (25, 25, 0))
    try_0_line_0_labeled_point_specs()
    try_0_line_1_labeled_point_specs()
    try_1_line_0_labeled_point_specs()
    try_3_line_3_labeled_point_specs()

def test__make_ordered_point_specs():
    def try_0_line_specs_0_labeled_point_specs():
        try_name = '0_line_specs_0_labeled_point_specs'
        line_specs = []
        labeled_point_specs = []
        actual_value = gd.GuidsToDat._make_ordered_point_specs(
            line_specs, labeled_point_specs)
        expected_value = []
        if not actual_value == expected_value:
            u.Utilities.print_test_error_message(
                method_name, try_name, expected_value, actual_value)

    def try_0_line_specs_3_labeled_point_specs():
        try_name = '0_line_specs_3_labeled_point_specs'
        line_specs = []
        labeled_point_specs = [lp3, lp2, lp1, lp2]
        actual_value = gd.GuidsToDat._make_ordered_point_specs(
            line_specs, labeled_point_specs)
        expected_value = [p1, p2, p3]
        if not actual_value == expected_value:
            u.Utilities.print_test_error_message(
                method_name, try_name, expected_value, actual_value)
        

    def try_3_line_specs_0_labeled_point_specs():
        try_name = '3_line_specs_0_labeled_point_specs'
        line_specs = [l3, l2, l1, l2]
        labeled_point_specs = []
        actual_value = gd.GuidsToDat._make_ordered_point_specs(
            line_specs, labeled_point_specs)
        expected_value = [p0, p1, p2, p3]
        if not actual_value == expected_value:
            u.Utilities.print_test_error_message(
                method_name, try_name, expected_value, actual_value)

    def try_3_line_specs_3_labeled_point_specs():
        try_name = '3_line_specs_3_labeled_point_specs'
        line_specs = [l3, l2, l1, l2]
        labeled_point_specs = [lp3, lp2, lp1, lp2]
        actual_value = gd.GuidsToDat._make_ordered_point_specs(
            line_specs, labeled_point_specs)
        expected_value = [p0, p1, p2, p3]
        if not actual_value == expected_value:
            u.Utilities.print_test_error_message(
                method_name, try_name, expected_value, actual_value)

    method_name = '_make_ordered_point_specs'
    g.Grammar.clear_all()
    a = 'a'
    p0, p1, p2, p3 = (0, 0, 0), (10, 10, 10), (20, 20, 20), (30, 30, 30)
    l1, l2, l3 = (p0, p1), (p0, p2), (p0, p3)
    lp1, lp2, lp3 = (a, p1), (a, p2), (a, p3)
    try_0_line_specs_0_labeled_point_specs()
    try_0_line_specs_3_labeled_point_specs()
    try_3_line_specs_0_labeled_point_specs()
    try_3_line_specs_3_labeled_point_specs()

def test__make_ordered_indented_coord_codex_xyz_polystring():
    def try_0_ordered_point_specs():
        try_name = '0_ordered_point_specs'
        ordered_point_specs = []
        actual_value = (
            gd.GuidsToDat._make_ordered_indented_coord_codex_xyz_polystring(
                ordered_point_specs))
        expected_value = ''
        if not actual_value == expected_value:
            u.Utilities.print_test_error_message(
                method_name, try_name, expected_value, actual_value)

    def try_3_ordered_point_specs():
        try_name = '3_ordered_point_specs'
        ordered_point_specs = [p0, p1, p2]
        actual_value = (
            gd.GuidsToDat._make_ordered_indented_coord_codex_xyz_polystring(
                ordered_point_specs))
        expected_value = '\n'.join([
            '    coords 0 0 0 0',
            '    coords 1 10 10 10',
            '    coords 2 20 20 20',
        ])
        if not actual_value == expected_value:
            u.Utilities.print_test_error_message(
                method_name, try_name, expected_value, actual_value)

    method_name = '_make_ordered_indented_coord_codex_xyz_polystring'
    p0, p1, p2 = (0, 0, 0), (10, 10, 10), (20, 20, 20)
    try_0_ordered_point_specs()
    try_3_ordered_point_specs()

def test__make_ordered_indented_line_lindex_codex_codex_polystring():
    def try_0_line_specs():
        try_name = '0_line_specs'
        line_specs = []
        actual_value = (
            gd.GuidsToDat._make_ordered_indented_line_lindex_codex_codex_polystring(
                line_specs, ordered_point_specs))
        expected_value = ''
        if not actual_value == expected_value:
            u.Utilities.print_test_error_message(
                method_name, try_name, expected_value, actual_value)

    def try_3_line_specs():
        try_name = '3_line_specs'
        line_specs = [l3, l2, l1]
        actual_value = (
            gd.GuidsToDat._make_ordered_indented_line_lindex_codex_codex_polystring(
                line_specs, ordered_point_specs))
        expected_value = '\n'.join([
            '    line 0 0 1',
            '    line 1 0 2',
            '    line 2 0 3',
        ])
        if not actual_value == expected_value:
            u.Utilities.print_test_error_message(
                method_name, try_name, expected_value, actual_value)

    method_name = '_make_ordered_indented_line_lindex_codex_codex_polystring'
    p0, p1, p2, p3 = (0, 0, 0), (0, 10, 0), (10, 0, 0), (10, 10, 0)
    l1, l2, l3 = (p0, p1), (p0, p2), (p0, p3)
    ordered_point_specs = [p0, p1, p2, p3]
    try_0_line_specs()
    try_3_line_specs()

def test__make_ordered_indented_point_codex_label_polystring():
    def try_0_labeled_point_specs():
        try_name = '0_labeled_point_specs'
        labeled_point_specs = []
        actual_value = (
            gd.GuidsToDat._make_ordered_indented_point_codex_label_polystring(
                labeled_point_specs, ordered_point_specs))
        expected_value = ''
        if not actual_value == expected_value:
            u.Utilities.print_test_error_message(
                method_name, try_name, expected_value, actual_value)

    def try_3_labeled_point_specs():
        try_name = '0_labeled_point_specs'
        labeled_point_specs = [lp3, lp2, lp1, lp0]
        actual_value = (
            gd.GuidsToDat._make_ordered_indented_point_codex_label_polystring(
                labeled_point_specs, ordered_point_specs))
        expected_value = '\n'.join([
            '    point 0 a',
            '    point 1 a',
            '    point 2 a',
            '    point 3 a'
        ])
        if not actual_value == expected_value:
            u.Utilities.print_test_error_message(
                method_name, try_name, expected_value, actual_value)

    method_name = '_make_ordered_indented_point_codex_label_polystring'
    p0, p1, p2, p3 = (0, 0, 0), (10, 10, 10), (20, 20, 20), (30, 30, 30) 
    ordered_point_specs = [p0, p1, p2, p3]
    a = 'a'
    lp0, lp1, lp2, lp3 = (a, p0), (a, p1), (a, p2), (a, p3)
    try_0_labeled_point_specs()
    try_3_labeled_point_specs()

### to deprecate

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

# def test__get_ordered_labeled_shapes_string():
    # def try_no_ishapes_no_rules():
    #     try_name = 'no_ishapes_no_rules'
    #     g.Grammar.clear_all()
    #     f.Frame._new_definition()
    #     actual_value = g.Grammar._get_ordered_labeled_shapes_string()
    #     expected_value = ''
    #     if not actual_value == expected_value:
    #         u.Utilities.print_test_error_message(
    #             method_name, try_name, expected_value, actual_value)

    # def try_no_ishapes_rules():
    #     try_name = 'no_ishapes_rules'
    #     pass

    # def try_ishapes_no_rules():
    #     try_name = 'ishapes_no_rules'
    #     pass

    # def try_ishapes_rules():
    #     try_name = 'ishapes_rules'
    #     pass

    # method_name = '_get_ordered_labeled_shapes_string'
    # try_no_ishapes_no_rules()
    # # try_no_ishapes_rules()
    # # try_ishapes_no_rules()
    # # try_ishapes_rules()

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

####

def _prompt_for_labeled_shape_name_elements_dict():
    """Prompts the user to select the elements of labeled shapes  to construct 
    the labeled shape name-elements dictionary. Returns:
        labeled_shape_name_elements_dict
                            {str: [guid, ...]}. A dictionary of labeled shape 
                            names and lists of guids of associated elements
    """
    labeled_shape_name_elements_dict = {}
    labeled_shape_names = g.Grammar.get_labeled_shape_names()
    for labeled_shape_name in labeled_shape_names:
        elements = _prompt_for_labeled_shape_elements(labeled_shape_name)
        labeled_shape_name_elements_dict[labeled_shape_name] = elements
    return labeled_shape_name_elements_dict

def _prompt_for_labeled_shape_elements(labeled_shape_name):
    """Receives:
        labeled_shape_name  str. The name of a labeled shape
    Prompts the user to select the elements belonging to the labeled shape. 
    Returns:
        elements            [guid, ...]. A list of guids of elements
    """
    message = "Select the elements in the labeled shape '%s'" % (
        labeled_shape_name)
    elements = rs.GetObjects(message)
    if not elements:
        elements = []
    return elements

def _prompt_for_initial_shape_elements(initial_shapes):
    """Receives:
        initial_shapes      [str, ...]. A list of initial shape layer names
    Prompts the user to select the frame instance of each initial shape in 
    turn. Returns:
        initial_shape_frame_dict
                            {str: guid}. A dictionary of initial shape 
                            names and frame instance guids
    """
    initial_shape_frame_dict = {}
    block_type = 4096
    for initial_shape in initial_shapes:
        message = "Select the frame instance for the labeled shape '%s'" % (
            initial_shape)
        frame_instance = rs.GetObject(message, block_type)
        initial_shape_frame_dict[initial_shape] = frame_instance
    return initial_shape_frame_dict

def _prompt_for_rule_elements(rules):
    """Receives:
        rules               [str, ...]. A list of rule layer names
    Prompts the user to select the elements of each rule in turn. Returns:
        rule_frame_pair_dict
                            {str: (guid, guid)}. A dictionary of rule names 
                            and frame instance pairs
    """
    rule_frame_pair_dict = {}
    block_type = 4096
    for rule in rules:
        message = (
            "Select the left and right frame instances for the rule '%s'" % (
                rule))
        guids = rs.GetObjects(message, block_type)
        rule_frame_pair_dict[rule] = guids
    return rule_frame_pair_dict

####

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
# test__make_initial_shape_frame_dict()           ##  done / manual test
# test__make_rule_frame_pair_dict()               ##  done / manual test
# test__make_labeled_shape_elements_dict()        ##  done / manual test
# test__get_elements()                            ##  done / manual test
# test__get_ordered_labeled_shapes_string()       ##  pending
# test__get_ordered_line_and_labeled_point_specs()##  done / manual test
# test__get_labeled_shape_string()                ##  done
# test__make_ordered_point_specs()                ##  done
# test__make_ordered_indented_coord_codex_xyz_polystring()
#                                                 ##  done
# test__make_ordered_indented_line_lindex_codex_codex_polystring()
#                                                 ##  done
# test__make_ordered_indented_point_codex_label_polystring()
#                                                 ##  done

### to deprecate

# test__get_ordered_rule_defs_string()
