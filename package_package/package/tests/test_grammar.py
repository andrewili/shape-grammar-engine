from package.scripts import frame as f
from package.scripts import grammar as g
import rhinoscriptsyntax as rs
from package.scripts import settings as s
from package.tests import utilities as u

def test_set_up_grammar():
    method_name = 'set_up_grammar'
    g.Grammar.clear_all()
    g.Grammar.set_up_grammar()

def test__set_up_first_initial_shape():
    def try_bad_state_layer_exists():
        try_name = 'bad_state_layer_exists'
        g.Grammar.clear_all()
        rs.AddLayer(s.Settings.first_initial_shape_layer_name)
        actual_value = g.Grammar._set_up_first_initial_shape()
        expected_value = None
        if not actual_value == expected_value:
            u.Utilities.print_test_error_message(
                method_name, try_name, expected_value, actual_value)
        
    def try_good_state():
        try_name = 'good_state'
        g.Grammar.clear_all()
        actual_value = g.Grammar._set_up_first_initial_shape()
        expected_value = s.Settings.first_initial_shape_layer_name
        if not actual_value == expected_value:
            u.Utilities.print_test_error_message(
                method_name, try_name, expected_value, actual_value)
        
    method_name = '_set_up_first_initial_shape'
    try_bad_state_layer_exists()
    try_good_state()

def test_set_up_subsequent_initial_shape():
    def try_good_state():
        try_name = 'good_state'
        g.Grammar.clear_all()
        existing_name = 'existing_name'
        rs.AddLayer(existing_name)
        ill_formed_name = 'bob#'
        good_name = 'good_name'
        print("Enter: 1, '%s'; 2, '%s'; 3, '%s'" % (
            existing_name, ill_formed_name, good_name))
        actual_value = g.Grammar.set_up_subsequent_initial_shape()
        expected_value = good_name
        if not actual_value == expected_value:
            u.Utilities.print_test_error_message(
                method_name, try_name, expected_value, actual_value)

    method_name = 'set_up_subsequent_initial_shape'
    try_good_state()

def test__set_up_initial_shape():
    def try_good_args():
        try_name = 'good_args'
        g.Grammar.clear_all()
        (   good_name, 
            position
        ) = (
            'sam',
            (20, 20, 0))
        actual_value = g.Grammar._set_up_initial_shape(good_name, position)
        expected_value = good_name
        if not actual_value == expected_value:
            u.Utilities.print_test_error_message(
                method_name, try_name, expected_value, actual_value)

    method_name = '_set_up_initial_shape'
    try_good_args()

def test__set_up_first_rule():
    def try_bad_state_layer_exists():
        try_name = 'bad_state_layer_exists'
        g.Grammar.clear_all()
        rs.AddLayer(s.Settings.first_rule_layer_name)
        actual_value = g.Grammar._set_up_first_rule()
        expected_value = None
        if not actual_value == expected_value:
            u.Utilities.print_test_error_message(
                method_name, try_name, expected_value, actual_value)

    def try_good_state():
        try_name = 'good_state'
        g.Grammar.clear_all()
        actual_value = g.Grammar._set_up_first_rule()
        expected_value = s.Settings.first_rule_layer_name
        if not actual_value == expected_value:
            u.Utilities.print_test_error_message(
                method_name, try_name, expected_value, actual_value)

    method_name = '_set_up_first_rule'
    try_bad_state_layer_exists()
    try_good_state()

def test_set_up_subsequent_rule():
    def try_good_state():
        try_name = 'good_state'
        g.Grammar.clear_all()
        existing_name = 'existing_name'
        rs.AddLayer(existing_name)
        ill_formed_name = 'bob#'
        good_name = 'good_name'
        print("Enter: 1, '%s'; 2, '%s'; 3, '%s'" % (
            existing_name, ill_formed_name, good_name))
        actual_value = g.Grammar.set_up_subsequent_rule()
        expected_value = good_name
        if not actual_value == expected_value:
            u.Utilities.print_test_error_message(
                method_name, try_name, expected_value, actual_value)

    method_name = 'set_up_subsequent_rule'
    try_good_state()

def test__set_up_rule():
    def try_good_args():
        try_name = 'good_args'
        g.Grammar.clear_all()
        good_name = 'bock'
        position = (20, 20, 0)
        actual_value = g.Grammar._set_up_rule(good_name, position)
        expected_value = good_name
        if not actual_value == expected_value:
            u.Utilities.print_test_error_message(
                method_name, try_name, expected_value, actual_value)

    method_name = '_set_up_rule'
    try_good_args()

def set_up_grammar_3_shapes_3_rules():
    def try_good_state():
        try_name = 'good_state'
        g.Grammar.set_up_grammar()
        n_initial_shapes, n_rules = range(2), range(2)
        for i in n_initial_shapes:
            g.Grammar.set_up_subsequent_initial_shape()
        for j in n_rules:
            g.Grammar.set_up_subsequent_rule()

    method_name = 'set_up_grammar_3_shapes_3_rules'
    try_good_state()

def test_change_text_dots_to_annotation_groups():   ##  01-04
    def try_no_dots():
        try_name = 'no_dots'
        g.Grammar.clear_all()
        actual_value = g.Grammar.change_text_dots_to_annotation_groups()
        expected_value = 0
        if not actual_value == expected_value:
            u.Utilities.print_test_error_message(
                method_name, try_name, expected_value, actual_value)

    def try_yes_dots():
        try_name = 'yes_dots'
        u.Utilities.make_grammar_3_initial_shapes_4_rules()
        actual_value = g.Grammar.change_text_dots_to_annotation_groups()
        n_dots_in_grammar = 17
        expected_value = n_dots_in_grammar
        if not actual_value == expected_value:
            u.Utilities.print_test_error_message(
                method_name, try_name, expected_value, actual_value)

    method_name = 'change_text_dots_to_annotation_groups'
    try_no_dots()
    try_yes_dots()

    try_no_visible_dots_no_hidden_dots_no_groups()
        ##  do nothing
    try_no_visible_dots_no_hidden_dots_yes_groups()
        ##  do nothing
    try_no_visible_dots_yes_hidden_dots_no_groups()
        ##  make groups
    try_no_visible_dots_yes_hidden_dots_yes_groups()
        ##  overwrite groups
    try_yes_visible_dots_no_hidden_dots_no_groups()
        ##  hide dots, make groups
    try_yes_visible_dots_no_hidden_dots_yes_groups()
        ##  hide dots, overwrite groups
    try_yes_visible_dots_yes_hidden_dots_no_groups()
        ##  hide dots, make groups
    try_yes_visible_dots_yes_hidden_dots_yes_groups()
        ##  hide dots, overwrite groups

def test_change_annotation_groups_to_text_dots():   ##  01-03
    def try_no_dots():
        try_name = 'no_dots'
        g.Grammar.clear_all()
        _draw_lines()
        _draw_text_dots()
        actual_value = g.Grammar.change_annotation_groups_to_text_dots()
        expected_value = 0
        if not actual_value == expected_value:
            u.Utilities.print_test_error_message(
                method_name, try_name, expected_value, actual_value)

    def try_yes_dots():
        try_name = 'yes_dots'
        u.Utilities.make_grammar_3_initial_shapes_4_rules()
        expected_value = g.Grammar.change_text_dots_to_annotation_groups()
        actual_value = g.Grammar.change_annotation_groups_to_text_dots()
        if not actual_value == expected_value:
            method_name, try_name, expected_value, actual_value

    method_name = 'change_annotation_groups_to_text_dots'
    try_no_dots()
    # try_yes_dots()

    try_no_visible_dots_no_hidden_dots_no_groups()
        ##  do nothing
    try_no_visible_dots_no_hidden_dots_yes_groups()
        ##  hide / delete groups, make visible dots
    try_no_visible_dots_yes_hidden_dots_no_groups()
        ##  do nothing
    try_no_visible_dots_yes_hidden_dots_yes_groups()
        ##  hide / delete groups, show hidden dots, make visible dots
    try_yes_visible_dots_no_hidden_dots_no_groups()
        ##  do nothing
    try_yes_visible_dots_no_hidden_dots_yes_groups()
        ##  hide / delete groups, overwrite? / add to? dots
    try_yes_visible_dots_yes_hidden_dots_no_groups()
        ##  do nothing
    try_yes_visible_dots_yes_hidden_dots_yes_groups()
        ##  hide / delete groups, show hidden dots, make visible dots
    # different numbers of groups and dots
    # groups and dots don't match 

####

def test_export():
    def try_0_initial_shapes_0_rules():
        try_name = '0_initial_shapes_0_rules'
        u.Utilities.make_grammar_0_initial_shapes_0_rules()
        actual_value = g.Grammar.export()
        expected_value = None
        if not actual_value == expected_value:
            u.Utilities.print_test_error_message(
                method_name, try_name, expected_value, actual_value)

    def try_0_initial_shapes_3_rules():
        try_name = '0_initial_shapes_3_rules'
        u.Utilities.make_grammar_0_initial_shapes_3_rules()
        actual_value = g.Grammar.export()
        expected_value = None
        if not actual_value == expected_value:
            u.Utilities.print_test_error_message(
                method_name, try_name, expected_value, actual_value)

    def try_3_initial_shapes_0_rules():
        try_name = '3_initial_shapes_0_rules'
        u.Utilities.make_grammar_3_initial_shapes_0_rules()
        actual_value = g.Grammar.export()
        expected_value = None
        if not actual_value == expected_value:
            u.Utilities.print_test_error_message(
                method_name, try_name, expected_value, actual_value)

    def try_3_initial_shapes_4_rules():         ##  manual
        try_name = '3_initial_shapes_4_rules'
        u.Utilities.make_grammar_3_initial_shapes_4_rules()
        actual_value = g.Grammar.export()
        expected_value = u.Utilities.grammar_3_4_dat_string
        if not actual_value == expected_value:
            u.Utilities.print_test_error_message(
                method_name, try_name, expected_value, actual_value)

    method_name = 'export'
    try_0_initial_shapes_0_rules()
    try_0_initial_shapes_3_rules()
    try_3_initial_shapes_0_rules()
    try_3_initial_shapes_4_rules()              ##  manual

def test__get_element_layers():
    def try_0_ishapes_0_rules():
        try_name = '0_ishapes_0_rules'
        g.Grammar.clear_all()
        f.Frame._new_definition()
        actual_value = g.Grammar._get_element_layers()
        expected_value = [], []
        if not (
            set(actual_value[0]) == set(expected_value[0]) and
            set(actual_value[1]) == set(expected_value[1])
        ):
            u.Utilities.print_test_error_message(
                method_name, try_name, expected_value, actual_value)

    def try_0_ishapes_3_rules():
        try_name = '0_ishapes_3_rules'
        u.Utilities.make_grammar_0_initial_shapes_3_rules()
        actual_value = g.Grammar._get_element_layers()
        expected_value = (
            [],
            [   'subdivide_triangle',
                'add_h_to_h',
                'add_h_in_square'])
        if not (
            set(actual_value[0]) == set(expected_value[0]) and
            set(actual_value[1]) == set(expected_value[1])
        ):
            u.Utilities.print_test_error_message(
                method_name, try_name, expected_value, actual_value)


    def try_3_ishapes_0_rules():
        try_name = '3_ishapes_0_rules'
        u.Utilities.make_grammar_3_initial_shapes_0_rules()
        actual_value = g.Grammar._get_element_layers()
        expected_value = (
            [   'labeled_right_triangle',
                'labeled_h',
                'labeled_square'],
            [])
        if not (
            set(actual_value[0]) == set(expected_value[0]) and
            set(actual_value[1]) == set(expected_value[1])
        ):
            u.Utilities.print_test_error_message(
                method_name, try_name, expected_value, actual_value)

    def try_3_ishapes_3_rules():
        try_name = '3_ishapes_3_rules'
        u.Utilities.make_grammar_3_initial_shapes_3_rules()
        actual_value = g.Grammar._get_element_layers()
        expected_value = (
            [   'labeled_right_triangle',
                'labeled_h',
                'labeled_square'],
            [   'subdivide_triangle',
                'add_h_to_h',
                'add_h_in_square'])
        if not (
            set(actual_value[0]) == set(expected_value[0]) and
            set(actual_value[1]) == set(expected_value[1])
        ):
            u.Utilities.print_test_error_message(
                method_name, try_name, expected_value, actual_value)

    method_name = '_get_element_layers'
    try_0_ishapes_0_rules()
    try_0_ishapes_3_rules()
    try_3_ishapes_0_rules()
    try_3_ishapes_3_rules()

def test_get_name():
    def try_good_state():
        try_name = 'good_state'
        actual_value = g.Grammar.get_name()
        expected_value = ''
        if not actual_value == expected_value:
            u.Utilities.print_test_error_message(
                method_name, try_name, expected_value, actual_value)

    method_name = 'get_name'
    try_good_state()

def test_get_labeled_shape_names():
    def try_0_ishapes_0_rules():
        try_name = '0_ishapes_0_rules'
        u.Utilities.make_grammar_0_initial_shapes_0_rules()
        actual_value = g.Grammar.get_labeled_shape_names()
        expected_value = []
        if not actual_value == expected_value:
            u.Utilities.print_test_error_message(
                method_name, try_name, expected_value, actual_value)

    def try_0_ishapes_3_rules():
        try_name = '0_ishapes_3_rules'
        u.Utilities.make_grammar_0_initial_shapes_3_rules()
        actual_value = g.Grammar.get_labeled_shape_names()
        expected_value = [
            'subdivide_triangle_spec_L',
            'subdivide_triangle_spec_R',
            'add_h_to_h_spec_L',
            'add_h_to_h_spec_R',
            'add_h_in_square_spec_L',
            'add_h_in_square_spec_R']
        if not set(actual_value) == set(expected_value):
            u.Utilities.print_test_error_message(
                method_name, try_name, expected_value, actual_value)

    def try_3_ishapes_0_rules():
        try_name = '3_ishapes_0_rules'
        u.Utilities.make_grammar_3_initial_shapes_0_rules()
        actual_value = g.Grammar.get_labeled_shape_names()
        expected_value = [
            'labeled_right_triangle_spec',
            'labeled_h_spec',
            'labeled_square_spec']
        if not set(actual_value) == set(expected_value):
            u.Utilities.print_test_error_message(
                method_name, try_name, expected_value, actual_value)

    def try_3_ishapes_3_rules():
        try_name = '3_ishapes_3_rules'
        u.Utilities.make_grammar_3_initial_shapes_3_rules()
        actual_value = g.Grammar.get_labeled_shape_names()
        expected_value = [
            'subdivide_triangle_spec_L',
            'subdivide_triangle_spec_R',
            'add_h_to_h_spec_L',
            'add_h_to_h_spec_R',
            'add_h_in_square_spec_L',
            'add_h_in_square_spec_R',
            'labeled_right_triangle_spec',
            'labeled_h_spec',
            'labeled_square_spec']
        if not set(actual_value) == set(expected_value):
            u.Utilities.print_test_error_message(
                method_name, try_name, expected_value, actual_value)

    method_name = 'get_labeled_shape_names'
    try_0_ishapes_0_rules()
    try_0_ishapes_3_rules()
    try_3_ishapes_0_rules()
    try_3_ishapes_3_rules()

def test__clear_objects():
    def try_no_hidden_text_dots():
        try_name = 'no_hidden_text_dots'
        lines = _draw_lines()
        text_dots = _draw_text_dots()
        n_objects_drawn = len(lines) + len(text_dots)
        actual_value = g.Grammar._clear_objects()
        expected_value = n_objects_drawn
        if not actual_value == expected_value:
            u.Utilities.print_test_error_message(
                method_name, try_name, expected_value, actual_value)

    def try_yes_hidden_text_dots():
        try_name = 'yes_hidden_text_dots'
        lines = _draw_lines()
        text_dots = _draw_text_dots()
        hidden_text_dots = _draw_hidden_text_dots()
        rs.GetString("Drew 2 lines, 2 visible dots, 2 hidden dots")
        n_objects_drawn = len(lines) + len(text_dots) + len(hidden_text_dots)
        actual_value = g.Grammar._clear_objects()
        expected_value = n_objects_drawn
        if not actual_value == n_objects_drawn:
            u.Utilities.print_test_error_message(
                method_name, try_name, expected_value, actual_value)

    method_name = '_clear_objects'
    try_no_hidden_text_dots()
    # try_yes_hidden_text_dots()

def test__show_hidden_text_dots():
    def try_no_hidden_text_dots():
        try_name = 'no_hidden_text_dots'
        g.Grammar.clear_all()
        actual_value = g.Grammar._show_hidden_text_dots()
        expected_value = 0
        if not actual_value == expected_value:
            method_name, try_name, expected_value, actual_value

    def try_yes_hidden_text_dots():
        try_name = 'yes_hidden_text_dots'
        u.Utilities.make_grammar_3_initial_shapes_4_rules()
        g.Grammar.change_text_dots_to_annotation_groups()
        actual_value = g.Grammar._show_hidden_text_dots()
        n_hidden_text_dots = 17
        expected_value = n_hidden_text_dots
        if not actual_value == expected_value:
            method_name, try_name, expected_value, actual_value

    method_name = '_show_hidden_text_dots'
    try_no_hidden_text_dots()
    try_yes_hidden_text_dots()

##  Utilities  ##

def _draw_lines():
    p11, p12 = (10, 10, 0), (10, 20, 0)
    p21, p22 = (20, 10, 0), (20, 20, 0)
    line_1 = rs.AddLine(p11, p12)
    line_2 = rs.AddLine(p21, p22)
    if line_1 and line_2:
        message = 'Drew 2 lines'
    else:
        message = 'Did not draw 2 lines'
    print(message)
    lines = [line_1, line_2]
    return lines

def _draw_text_dots():
    text_1, text_2 = '1', '2'
    dot_1, dot_2 = (10, 0, 0), (20, 0, 0)
    text_dot_1 = rs.AddTextDot(text_1, dot_1)
    text_dot_2 = rs.AddTextDot(text_2, dot_2)
    if text_dot_1 and text_dot_2:
        message = 'Drew 2 visible text dots'
    else:
        message = 'Did not draw 2 visible text dots'
    print(message)
    text_dots = [text_dot_1, text_dot_2]
    return text_dots

def _draw_hidden_text_dots():
    text_3, text_4 = 'x3', 'x4'
    dot_3, dot_4 = (30, 0, 0), (40, 0, 0)
    text_dot_3 = rs.AddTextDot(text_3, dot_3)
    text_dot_4 = rs.AddTextDot(text_4, dot_4)
    hidden_text_dots = [text_dot_3, text_dot_4]
    hidden_group = s.Settings.hidden_text_dot_group
    rs.AddGroup(hidden_group)
    n_objects = rs.AddObjectsToGroup(hidden_text_dots, hidden_group)
    if n_objects:
        message = 'Added %i text dots to hidden group' % n_objects
    else:
        message = 'Did not add text dots to hidden group'
    rs.HideGroup(hidden_group)
    g.Grammar._update_display()
    rs.GetString('Updated display')
    return hidden_text_dots


# set_up_grammar_3_shapes_3_rules()               ##  done 08-07 / manual
# test_set_up_grammar()                           ##  done 08-06 / manual
# test__set_up_first_initial_shape()              ##  done 08-06
# test_set_up_subsequent_initial_shape()          ##  done 08-06 / manual
# test__set_up_initial_shape()                    ##  done 08-06
# test__set_up_first_rule()                       ##  done 08-06
# test_set_up_subsequent_rule()                   ##  done 08-06 / manual
# test__set_up_rule()                             ##  done 12-16
# test_change_text_dots_to_annotation_groups()    ##  done 01-03
test_change_annotation_groups_to_text_dots()    ##  

# test_export()                                   ##  done / manual
# test__get_element_layers()                      ##  done
# test_get_name()                                 ##  done

# test_get_labeled_shape_names()                  ##  done / for tests
# test__clear_objects()                           ##  done
# test__show_hidden_text_dots()                   ##  done
