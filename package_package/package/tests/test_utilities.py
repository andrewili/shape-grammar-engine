from package.scripts import grammar as g
from package.scripts import layer as l
from package.tests import utilities as u
import rhinoscriptsyntax as rs

def test_make_grammar_3_initial_shapes_3_rules():
    u.Utilities.make_grammar_3_initial_shapes_3_rules()

def test__add_first_initial_shape():
    def try_good_args():
        try_name = 'good_args'
        g.Grammar.clear_all()
        layer_name = 'labeled_h_spec'
        initial_shape_spec = u.Utilities.labeled_h_spec
        actual_value = u.Utilities._add_first_initial_shape(
            layer_name, initial_shape_spec)
        expected_value = layer_name
        if not actual_value == expected_value:
            u.Utilities.print_test_error_message(
                method_name, try_name, expected_value, actual_value)

    method_name = '_add_first_initial_shape'
    try_good_args()

def test__add_subsequent_initial_shape():
    def try_good_args():
        try_name = 'good_args'
        g.Grammar.clear_all()
        layer_name = 'labeled_square_spec'
        initial_shape_spec = u.Utilities.labeled_square_spec
        frame_position = (0, -40, 0)
        actual_value = u.Utilities._add_subsequent_initial_shape(
            layer_name, initial_shape_spec, frame_position)
        expected_value = layer_name
        if not actual_value == expected_value:
            u.Utilities.print_test_error_message(
                method_name, try_name, expected_value, actual_value)

    method_name = '_add_subsequent_initial_shape'
    try_good_args()

def test__draw_initial_shape():
    def try_good_args():
        try_name = 'good_args'
        g.Grammar.clear_all()
        initial_shape_spec = u.Utilities.labeled_right_triangle_spec
        layer_name = 'labeled_right_triangle_spec'
        l.Layer.new(layer_name)
        position = (0, -40, 0)
        actual_value = u.Utilities._draw_initial_shape(
            initial_shape_spec, layer_name, position)
        expected_value = layer_name
        if not actual_value == expected_value:
            u.Utilities.print_test_error_message(
                method_name, try_name, expected_value, actual_value)

    method_name = '_draw_initial_shape'
    try_good_args()

def test__add_first_rule():
    def try_good_args():
        try_name = 'good_args'
        g.Grammar.clear_all()
        layer_name = 'subdivide triangle'
        rule_spec = u.Utilities.subdivide_triangle_spec
        actual_value = u.Utilities._add_first_rule(layer_name, rule_spec)
        expected_value = layer_name
        if not actual_value == expected_value:
            u.Utilities.print_test_error_message(
                method_name, try_name, expected_value, actual_value)

    method_name = '_add_first_rule'
    try_good_args()

def test__add_subsequent_rule():
    def try_good_args():
        try_name = 'good_args'
        g.Grammar.clear_all()
        layer_name = 'layer i'
        rule_spec = u.Utilities.add_h_to_h_spec
        left_frame_position = (10, 10, 0)
        actual_value = u.Utilities._add_subsequent_rule(
            layer_name, rule_spec, left_frame_position)
        expected_value = layer_name
        if not actual_value == expected_value:
            u.Utilities.print_test_error_message(
                method_name, try_name, expected_value, actual_value)

    method_name = '_add_subsequent_rule'
    try_good_args()

def test__draw_rule():
    method_name = '_draw_rule'
    g.Grammar.clear_all()
    rule_spec = u.Utilities.add_h_to_h_spec
    layer_name = 'add_h_to_h_spec'
    l.Layer.new(layer_name)
    left_frame_position = (20, 20, 0)
    actual_value = u.Utilities._draw_rule(
        rule_spec, layer_name, left_frame_position)
    expected_value = layer_name
    if not actual_value == expected_value:
        u.Utilities.print_test_error_message(
            method_name, try_name, expected_value, actual_value)

def test__draw_labeled_shape():
    def try_good_args():
        try_name = 'good_args'
        g.Grammar.clear_all()
        labeled_shape_spec = u.Utilities.labeled_h_spec
        position = (10, 10, 0)
        actual_value = u.Utilities._draw_labeled_shape(
            labeled_shape_spec, position)
        expected_value = True
        if not actual_value == expected_value:
            u.Utilities.print_test_error_message(
                method_name, try_name, expected_value, actual_value)

    method_name = '_draw_labeled_shape'
    try_good_args()

test_make_grammar_3_initial_shapes_3_rules()           ##  done
# test__add_first_initial_shape()                 ##  done
# test__add_subsequent_initial_shape()            ##  done
# test__draw_initial_shape()                      ##  done
# test__add_first_rule()                          ##  done
# test__add_subsequent_rule()                     ##  done
# test__draw_rule()                               ##  done
# test__draw_labeled_shape()                      ##  done
