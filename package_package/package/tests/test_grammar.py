from package.view import grammar as g
from package.tests import utilities as u

def test_new():
    method_name = 'new'
    g.Grammar.clear_all()
    g.Grammar.new()

def test_add_to_initial_shapes():
    def try_good_args():
        try_name = 'good_args'
        g.Grammar.clear_all()
        list_name = 'initial shapes'
        initial_shape_name = 'initial_shape'
        actual_value = g.Grammar.add_to_initial_shapes(initial_shape_name)
        expected_value = initial_shape_name
        if not actual_value == expected_value:
            u.Utilities.print_test_error_message(
                method_name, try_name, expected_value, actual_value)

    method_name = 'add_to_initial_shapes'
    try_good_args()

def test_add_to_rules():
    def try_good_args():
        try_name = 'good_args'
        g.Grammar.clear_all()
        list_name = 'rules'
        rule_name = 'rule'
        actual_value = g.Grammar.add_to_rules(rule_name)
        expected_value = rule_name
        if not actual_value == expected_value:
            u.Utilities.print_test_error_message(
                method_name, try_name, expected_value, actual_value)

    method_name = 'add_to_rules'
    try_good_args()

# test_new()
# test__add_first_initial_shape()               ##  not needed
# test__add_first_rule()
test_add_to_initial_shapes()
test_add_to_rules()
