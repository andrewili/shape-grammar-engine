import copy
from package.scripts import frame as f
from package.scripts import grammar as g
from package.controller import guids_to_dat as gd
from package.scripts import layer as l
import rhinoscriptsyntax as rs
from package.scripts import settings as s
from package.tests import utilities as u

def test_get_dat_string():                      ##  done 08-16
    def try_grammar_1_empty_rule():
        try_name = 'grammar_1_empty_rule'
        u.Utilities.make_grammar_3_initial_shapes_4_rules()
        (   empty_rule) = 'empty_rule'
        print("Add '%s'" % empty_rule)
        g.Grammar.set_up_subsequent_rule()
        (   initial_shapes) = u.Utilities.three_initial_shapes
        (   rules) = copy.copy(u.Utilities.four_rules)
        (   rules.append(empty_rule))
        actual_value = gd.GuidsToDat.get_dat_string(initial_shapes, rules)
        expected_value = u.Utilities.grammar_3_4_dat_string
        if not actual_value == expected_value:
            u.Utilities.print_test_error_message(
                method_name, try_name, expected_value, actual_value)

    def try_grammar_1_empty_initial_shape():
        try_name = 'grammar_1_empty_initial_shape'
        u.Utilities.make_grammar_3_initial_shapes_4_rules()
        (   empty_initial_shape) = 'empty_initial_shape'
        print("Add '%s'" % empty_initial_shape)
        g.Grammar.set_up_subsequent_initial_shape()
        (   initial_shapes) = copy.copy(u.Utilities.three_initial_shapes)
        (   initial_shapes.append(empty_initial_shape))
        (   rules) = u.Utilities.four_rules
        actual_value = gd.GuidsToDat.get_dat_string(initial_shapes, rules)
        expected_value = u.Utilities.grammar_3_4_dat_string
        if not actual_value == expected_value:
            u.Utilities.print_test_error_message(
                method_name, try_name, expected_value, actual_value)

    def try_good_grammar():
        try_name = 'good_grammar'
        u.Utilities.make_grammar_3_initial_shapes_4_rules()
        (   initial_shapes, 
            rules
        ) = (
            u.Utilities.three_initial_shapes,
            u.Utilities.four_rules)
        actual_value = gd.GuidsToDat.get_dat_string(
            initial_shapes, rules)
        expected_value = u.Utilities.grammar_3_4_dat_string
        if not actual_value == expected_value:
            u.Utilities.print_test_error_message(
                method_name, try_name, expected_value, actual_value)

    method_name = 'get_dat_string'
    # try_grammar_1_empty_rule()
    # try_grammar_1_empty_initial_shape()
    # try_good_grammar()

def test__make_initial_shape_frame_dict():      ##  done 08-08
    def try_3_ishapes():
        try_name = '3_ishapes'
        u.Utilities.make_grammar_3_initial_shapes_3_rules()
        initial_shapes = u.Utilities.three_initial_shapes
        actual_value = gd.GuidsToDat._make_initial_shape_frame_dict(
            initial_shapes)
        expected_value = (
            u.Utilities.prompt_for_initial_shape_frame_dict(initial_shapes))
        if not actual_value == expected_value:
            u.Utilities.print_test_error_message(
                method_name, try_name, expected_value, actual_value)

    method_name = '_make_initial_shape_frame_dict'
    try_3_ishapes()

def test__make_rule_frame_pair_dict():          ##  done 08-08
    def try_3_rules():
        try_name = '3_rules'

        u.Utilities.make_grammar_3_initial_shapes_3_rules()
        rules = u.Utilities.three_rules
        actual_value = gd.GuidsToDat._make_rule_frame_pair_dict(rules)
        expected_value = (
            u.Utilities.prompt_for_rule_frame_pair_dict(rules))
        if not actual_value == expected_value:
            u.Utilities.print_test_error_message(
                method_name, try_name, expected_value, actual_value)

    method_name = '_make_rule_frame_pair_dict'
    try_3_rules()

def test__make_labeled_shape_elements_dict():   ##  done 08-15
    def try_non_empty_and_empty_initial_shapes_and_rules_0_1_0_1():
        try_name = 'non_empty_and_empty_initial_shapes_and_rules_0_1_0_1'
        g.Grammar.set_up_grammar()
        (   actual_initial_shape_frame_dict) = (
            _prompt_for_actual_initial_shape_frame_dict())
        (   actual_rule_frame_pair_dict) = (
            _prompt_for_actual_rule_frame_pair_dict())
        actual_value = gd.GuidsToDat._make_labeled_shape_elements_dict(
            actual_initial_shape_frame_dict, actual_rule_frame_pair_dict)
        expected_value = {}
        if not actual_value == expected_value:
            u.Utilities.print_test_error_message(
                method_name, try_name, expected_value, actual_value)

    def try_non_empty_and_empty_initial_shapes_and_rules_3_0_4_1():
        try_name = 'non_empty_and_empty_initial_shapes_and_rules_3_0_4_1'
        u.Utilities.make_grammar_3_initial_shapes_4_rules()
        print("Add 'empty_rule'")
        g.Grammar.set_up_subsequent_rule()
        (   actual_initial_shape_frame_dict) = (
            _prompt_for_actual_initial_shape_frame_dict())
        (   actual_rule_frame_pair_dict) = (
            _prompt_for_actual_rule_frame_pair_dict())
        actual_dict = gd.GuidsToDat._make_labeled_shape_elements_dict(
            actual_initial_shape_frame_dict, actual_rule_frame_pair_dict)
        expected_dict = _prompt_for_expected_labeled_shape_elements_dict()
        actual_value = _compare_dicts(actual_dict, expected_dict)
        expected_value = True
        print(actual_dict)
        if not actual_value == expected_value:
            u.Utilities.print_test_error_message(
                method_name, try_name, expected_value, actual_value)

    def try_non_empty_and_empty_initial_shapes_and_rules_3_1_4_0():
        try_name = 'non_empty_and_empty_initial_shapes_and_rules_3_1_4_0'
        u.Utilities.make_grammar_3_initial_shapes_4_rules()
        print("Add 'empty_initial_shape'")
        g.Grammar.set_up_subsequent_initial_shape()
        (   actual_initial_shape_frame_dict) = (
            _prompt_for_actual_initial_shape_frame_dict())
        (   actual_rule_frame_pair_dict) = (
            _prompt_for_actual_rule_frame_pair_dict())
        actual_dict = gd.GuidsToDat._make_labeled_shape_elements_dict(
            actual_initial_shape_frame_dict, actual_rule_frame_pair_dict)
        expected_dict = _prompt_for_expected_labeled_shape_elements_dict()
        actual_value = _compare_dicts(actual_dict, expected_dict)
        expected_value = True
        if not actual_value == expected_value:
            u.Utilities.print_test_error_message(
                method_name, try_name, expected_value, actual_value)

    def try_non_empty_and_empty_initial_shapes_and_rules_3_0_4_0():
        try_name = 'non_empty_and_empty_initial_shapes_and_rules_3_0_4_0'
        u.Utilities.make_grammar_3_initial_shapes_4_rules()
        (   actual_initial_shape_frame_dict) = (
            _prompt_for_actual_initial_shape_frame_dict())
        (   actual_rule_frame_pair_dict) = (
            _prompt_for_actual_rule_frame_pair_dict())
        actual_dict = gd.GuidsToDat._make_labeled_shape_elements_dict(
            actual_initial_shape_frame_dict, actual_rule_frame_pair_dict)
        expected_dict = _prompt_for_expected_labeled_shape_elements_dict()
        actual_value = _compare_dicts(actual_dict, expected_dict)
        expected_value = True
        if not actual_value == expected_value:
            u.Utilities.print_test_error_message(
                method_name, try_name, expected_value, actual_value)

    method_name = '_make_labeled_shape_elements_dict'
    # try_non_empty_and_empty_initial_shapes_and_rules_0_1_0_1()  ##  done
    try_non_empty_and_empty_initial_shapes_and_rules_3_0_4_1()  ##  done / manual
    # try_non_empty_and_empty_initial_shapes_and_rules_3_1_4_0()  ##  done / manual
    # try_non_empty_and_empty_initial_shapes_and_rules_3_0_4_0()  ##  done / manual

def test__get_elements():
    def try_empty_frame():
        try_name = 'empty_frame'
        u.Utilities.make_grammar_1_initial_shape_1_delete_rule()
        message = "%s %s" % (
            "Select the empty frame instance.",
            "Nothing will be selected")
        frame_instance = rs.GetObject(
            message, s.Settings.block_instance_filter)
        actual_value = gd.GuidsToDat._get_elements(frame_instance)
        rs.SelectObjects(actual_value)

    def try_good_args():
        try_name = 'good_args'
        u.Utilities.make_grammar_3_initial_shapes_4_rules()
        message = "%s %s" % (
            "Select a frame instance.",
            "The elements in the frame will be selected")
        frame_instance_in = rs.GetObject(
            message, s.Settings.block_instance_filter)
        actual_value = gd.GuidsToDat._get_elements(frame_instance_in)
        rs.SelectObjects(actual_value)

    method_name = '_get_elements'
    try_empty_frame()
    try_good_args()

def test__extract_elements_in_frame():          ##  done 08-08
    def try_no_objects():
        try_name = 'no_objects'
        g.Grammar.clear_all()
        layer_name = 'layer_x'
        l.Layer.new(layer_name)
        frame_name = layer_name
        frame_position = (0, 0, 0)
        frame_guid = f.Frame.new_instance(
            layer_name, frame_position)
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
            layer_name, frame_position)
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

def test__is_element():                         ##  trivial
    pass

def test__object_is_in_box():                   ##  trivial
    pass

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

def test__get_components():                     ##  done 08-16
    def try_empty_dict():
        try_name = 'empty_dict'
        empty_dict = {}
        actual_value = gd.GuidsToDat._get_components(empty_dict)
        expected_value = ([], [])
        if not actual_value == expected_value:
            u.Utilities.print_test_error_message(
                method_name, try_name, expected_value, actual_value)

    def try_good_dict():
        try_name = 'good_dict'
        good_dict = {
            'initial_shape_2': ['c', 'd'],
            'initial_shape_1': ['a', 'b'],
            'rule_2_R': ['k'],
            'rule_1_R': ['g', 'h'],
            'rule_2_L': ['i', 'j'],
            'rule_1_L': ['e', 'f']}
        actual_initial_shapes, actual_rules = (
            gd.GuidsToDat._get_components(good_dict))
        actual_value = (
            sorted(actual_initial_shapes), 
            sorted(actual_rules))
        expected_value = (
            ['initial_shape_1', 'initial_shape_2'],
            ['rule_1', 'rule_2'])
        if not actual_value == expected_value:
            u.Utilities.print_test_error_message(
                method_name, try_name, expected_value, actual_value)

    method_name = '_get_components'
    try_empty_dict()
    try_good_dict()

def test__get_ordered_labeled_shapes_string():
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
    # print('tests disabled')
    # try_0_ishapes_0_rules()                     ##  done
    # try_1_ishape_1_delete_rule()                ##  done
    # try_3_ishapes_4_rules()                     ##  done

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
    block_instance_filter = s.Settings.block_instance_filter
    text_dot_filter = 8192
    print('tests disabled')
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

    def try_5_line_5_labeled_point_specs():
        try_name = '5_line_5_labeled_point_specs'
        line_and_labeled_point_specs = (
            [l4, l3, l2, l1, l0],
            [lp4, lp3, lp2, lp1, lp0])
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
            '    coords 9 30 40 0',
            '    coords 10 35 35 0',
            '    coords 11 40 30 0',
            '    coords 12 40 50 0',
            '    coords 13 45 45 0',
            '    coords 14 50 40 0',
            '',
            '    line 0 0 2',
            '    line 1 3 5',
            '    line 2 6 8',
            '    line 3 9 11',
            '    line 4 12 14',
            '    point 1 a',
            '    point 4 a',
            '    point 7 a',
            '    point 10 a',
            '    point 13 a',
        ])
        if not actual_value == expected_value:
            u.Utilities.print_test_error_message(
                method_name, try_name, expected_value, actual_value)

    method_name = '_get_labeled_shape_string'
    g.Grammar.clear_all()
    l0 = ((0, 10, 0), (10, 0, 0))
    l1 = ((10, 20, 0), (20, 10, 0))
    l2 = ((20, 30, 0), (30, 20, 0))
    l3 = ((30, 40, 0), (40, 30, 0))
    l4 = ((40, 50, 0), (50, 40, 0))
    lp0 = ('a', (5, 5, 0))
    lp1 = ('a', (15, 15, 0))
    lp2 = ('a', (25, 25, 0))
    lp3 = ('a', (35, 35, 0))
    lp4 = ('a', (45, 45, 0))
    try_0_line_0_labeled_point_specs()
    try_0_line_1_labeled_point_specs()
    try_1_line_0_labeled_point_specs()
    try_3_line_3_labeled_point_specs()
    try_5_line_5_labeled_point_specs()

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

def test__get_ordered_initial_shape_names_string():
    def try_0_ishapes():
        try_name = '0_ishapes'
        initial_shapes = []
        actual_value = gd.GuidsToDat._get_ordered_initial_shape_names_string(
            initial_shapes)
        expected_value = ''
        if not actual_value == expected_value:
            u.Utilities.print_test_error_message(
                method_name, try_name, expected_value, actual_value)

    def try_3_ishapes():
        try_name = '3_ishapes_0_rules'
        initial_shapes = ['three', 'blind', 'mice']
        actual_value = gd.GuidsToDat._get_ordered_initial_shape_names_string(
            initial_shapes)
        expected_value = '\n'.join([
            'initial    blind',
            'initial    mice',
            'initial    three'
        ])
        if not actual_value == expected_value:
            u.Utilities.print_test_error_message(
                method_name, try_name, expected_value, actual_value)

    method_name = '_get_ordered_initial_shape_names_string'
    try_0_ishapes()
    try_3_ishapes()

def test__get_ordered_rule_names_string():
    def try_0_rules():
        try_name = '0_rules'
        rules = []
        actual_value = gd.GuidsToDat._get_ordered_rule_names_string(rules)
        expected_value = ''
        if not actual_value == expected_value:
            u.Utilities.print_test_error_message(
                method_name, try_name, expected_value, actual_value)

    def try_3_rules():
        try_name = '3_rules'
        rules = ['three', 'blind', 'mice']
        actual_value = gd.GuidsToDat._get_ordered_rule_names_string(rules)
        expected_value = '\n'.join([
            'rule    blind    blind_L -> blind_R',
            'rule    mice    mice_L -> mice_R',
            'rule    three    three_L -> three_R'
        ])
        if not actual_value == expected_value:
            u.Utilities.print_test_error_message(
                method_name, try_name, expected_value, actual_value)

    method_name = '_get_ordered_rule_names_string'
    try_0_rules()
    try_3_rules()

####

def _prompt_for_actual_initial_shape_frame_dict():
    """Prompts the user to select initial shape frame instances to construct 
    an actual initial shape name-frame dictionary. Returns:
        initial_shape_frame_dict
                            {str: guid}. A non-empty dictionary of initial 
                            shape names and frame instance guids
    """
    (   initial_shape_frame_dict) = {}
    (   message) = "Select the frames of all initial shapes" 
    (   block_instance_filter) = s.Settings.block_instance_filter
    (   frame_instances) = rs.GetObjects(message, block_instance_filter)
    for frame_instance in frame_instances:
        initial_shape = rs.ObjectLayer(frame_instance)
        initial_shape_frame_dict[initial_shape] = frame_instance
    return initial_shape_frame_dict

def _prompt_for_actual_rule_frame_pair_dict():
    """Prompts the user to select rule frame instance pairs to construct an 
    actual rule name-frame pair dictionary. Returns:
        rule_frame_pair_dict
                            {str: (guid, guid)}. A non-empty dictionary of 
                            rule names and frame instance guid pairs
    """
    (   message_1) = "Select the frames of all rules"
    print(message_1)
    (   rule_frame_pair_dict) = {}
    (   message_2) = "Select the frames of a rule: first left, then right"
    (   block_instance_filter) = s.Settings.block_instance_filter
    while True:
        frame_instance_pair = rs.GetObjects(message_2, block_instance_filter)
        if not frame_instance_pair:
            break
        else:
            left_frame_instance, right_frame_instance = frame_instance_pair
            rule = rs.ObjectLayer(left_frame_instance)
            rule_frame_pair_dict[rule] = (
                left_frame_instance, right_frame_instance)
    return rule_frame_pair_dict

def _prompt_for_expected_labeled_shape_elements_dict():
    """Prompts the user to select frame instances and their elements to 
    construct an expected labeled shape elements dictionary. Returns:
        expected_labeled_shape_elements_dict
                            {str: [guid]}. A non-empty dictionary of labeled 
                            shape names and element lists
    """
    (   message_intro) = "%s %s" % (
        "Select the frame instance of a non-empty initial shape ('i'),", 
        "or the left ('l') or right ('r') shape of a non-empty rule")
    print(message_intro)
    (   message_type) = "Enter the type of frame: 'i', 'l', or 'r'"
    (   labeled_shape_elements_dict) = {}
    (   message_frame) = "Select a frame"
    (   block_instance_filter) = s.Settings.block_instance_filter
    (   message_elements) = "Select the elements in the frame"
    (       curve_filter) = s.Settings.curve_filter
    (       text_dot_filter) = s.Settings.text_dot_filter
    (   element_filter) = curve_filter + text_dot_filter
    while True:
        labeled_shape_type = rs.GetString(message_type)
        if not labeled_shape_type:
            break
        else:
            frame_instance = rs.GetObject(
                message_frame, block_instance_filter)
            layer = rs.ObjectLayer(frame_instance)
            if labeled_shape_type == 'i':
                labeled_shape = layer
            elif labeled_shape_type == 'l':
                labeled_shape = '%s_L' % layer
            elif labeled_shape_type == 'r':
                labeled_shape = '%s_R' % layer
            else:
                labeled_shape = 'bad_labeled_shape'
            element_list = [frame_instance]
            elements = rs.GetObjects(message_elements, element_filter)
            if elements:
                element_list.extend(elements)
            labeled_shape_elements_dict[labeled_shape] = element_list
    return labeled_shape_elements_dict

def _compare_dicts(actual_dict, expected_dict):
    """Receives:
        actual_dict
        expected_dict
    Returns:
        value               boolean. True, if the corresponding element lists 
                            contain the same elements
    """
    value = True
    actual_key_set = set(actual_dict.keys())
    expected_key_set = set(expected_dict.keys())
    if not actual_key_set == expected_key_set:
        print("keys don't match")
        value = False
    else:
        for key in actual_key_set:
            actual_elements = actual_dict[key]
            expected_elements = expected_dict[key]
            actual_element_set = set(actual_elements)
            expected_element_set = set(expected_elements)
            if actual_element_set == expected_element_set:
                pass
            else:
                value = False
                break
    return value

def _prompt_for_labeled_shape_frames():         ##  in process
    """Prompts the user to select the frame instances of labeled shapes to 
    construct a list of frame instance names. Returns:
        frame_instances     [str]. A list of names of frame instances
    """
    pass

def _prompt_for_labeled_shape_name_elements_dict():     ##  don't pick all!
    """Prompts the user to select the elements of labeled shapes to construct 
    the labeled shape name-elements dictionary. Returns:
        labeled_shape_name_elements_dict
                            {str: [guid]}. A dictionary of labeled shape names 
                            and lists of guids of (first) the frame instance 
                            and (then) the associated elements
    """
    labeled_shape_name_elements_dict = {}
    labeled_shape_names = g.Grammar.get_labeled_shape_names()
    for labeled_shape_name in labeled_shape_names:
        frame_instance = _prompt_for_frame_instance(labeled_shape_name)
        elements = _prompt_for_labeled_shape_elements(labeled_shape_name)
        elements.insert(0, frame_instance)
        labeled_shape_name_elements_dict[labeled_shape_name] = elements
    return labeled_shape_name_elements_dict

def _prompt_for_frame_instance(labeled_shape_name):
    """Receives:
        labeled_shape_name  str. The name of a labeled shape
    Returns:
        frame_instance      guid. The guid of the associated frame instance
    """
    message = "Select the frame instance of the labeled shape '%s'" % (
        labeled_shape_name)
    frame_instance = rs.GetObject(message, s.Settings.block_instance_filter)
    return frame_instance

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

test_get_dat_string()                           ##  done
# test__make_initial_shape_frame_dict()           ##  done / manual test
# test__make_rule_frame_pair_dict()               ##  done / manual test
# test__make_labeled_shape_elements_dict()        ##  done / manual test
# test__get_elements()                            ##  done / manual test
# test__extract_elements_in_frame()               ##  done
# test__is_element()                              ##  trivial
# test__object_is_in_box()                        ##  trivial
# test__point_is_in_box()                         ##  done
# test__get_components()
# test__get_ordered_labeled_shapes_string()       ##  done / manual test
# test__get_ordered_line_and_labeled_point_specs()##  done / manual test
# test__get_labeled_shape_string()                ##  done
# test__make_ordered_point_specs()                ##  done
# test__make_ordered_indented_coord_codex_xyz_polystring()
#                                                 ##  done
# test__make_ordered_indented_line_lindex_codex_codex_polystring()
#                                                 ##  done
# test__make_ordered_indented_point_codex_label_polystring()
#                                                 ##  done
# test__get_ordered_initial_shape_names_string()  ##  done
# test__get_ordered_rule_names_string()           ##  done

