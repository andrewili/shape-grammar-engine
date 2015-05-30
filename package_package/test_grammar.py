from package.view import frame_block as fb
from package.view import grammar as g
from package.view import initial_shape as ish
from package.view import rule as r

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

# test__add_first_initial_shape()
# test__add_first_rule()
test_new()

