from package.model import frame_block as fb
from package.model import grammar as g
from package.model import initial_shape as ish
# from package.model import llist as ll
from package.model import rule as r
# import rhinoscriptsyntax as rs

position = [5, 5, 0]                            ##  check that all are used
existing_shape_name = 'existing_shape'
new_shape_name = 'new_shape'
bad_type_shape_name = 37
bad_value_name = existing_shape_name
good_arg_false_hash = 'kil#roy'
good_arg_false_space = 'kil roy'
good_arg_true_int = 37
good_arg_true_string = 'kilroy'
initial_shape_name = 'initial_shape'
first_initial_shape_name = ish.InitialShape.first_initial_shape_name

def test__add_first_initial_shape():
    method_name = '_add_first_initial_shape'

    def try_good_state():
        try_name = 'good_state'
        g.Grammar.clear_all()
        fb.FrameBlock.new()
        actual_value = g.Grammar._add_first_initial_shape()
        expected_value = ish.InitialShape.first_initial_shape_name
        if not actual_value == expected_value:
            g.Grammar.print_test_error_message(
                method_name, try_name, actual_value, expected_value)

    try_good_state()

def test__add_first_rule():
    method_name = '_add_first_rule'

    def try_good_state():
        try_name = 'good_state'
        g.Grammar.clear_all()
        fb.FrameBlock.new()
        actual_value = g.Grammar._add_first_rule()
        expected_value = r.Rule.first_rule_name
        if not actual_value == expected_value:
            g.Grammar.print_test_error_message(
                method_name, try_name, expected_value, actual_value)

    try_good_state()

def test_new():
    method_name = 'new'
    g.Grammar.clear_all()
    g.Grammar.new()

test__add_first_initial_shape()
test__add_first_rule()
test_new()

