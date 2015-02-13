from package.model import component_name as cn
from package.model import grammar as g
from package.model import llist as ll
from package.model import rule as r
# import rhinoscriptsyntax as rs

component_type = 'rule'
name = 'test_name'
rule_name = 'rule'
shape_name = 'shape'
initial_shape_name = 'initial_shape'
bad_value_component_type = 'bad_value_component_type'
bad_value_component_name = 'bad_value_component_name'
ill_formed_component_name = 'kil#roy'
well_formed_component_name = name

def test__component_name_is_listed():
    method_name = '_component_name_is_listed'

    def try_bad_value_component_type():
        try_name = 'bad_value_component_type'
        actual_value = cn.ComponentName._component_name_is_listed(
            bad_value_component_type, name)
        expected_value = False
        if not actual_value == expected_value:
            g.Grammar.print_test_error_message(
                method_name, try_name, expected_value, actual_value)

    def try_good_args_false():
        try_name = 'false'
        g.Grammar.clear_all()
        actual_value = cn.ComponentName._component_name_is_listed(
            component_type, name)
        expected_value = False
        if not actual_value == expected_value:
            g.Grammar.print_test_error_message(
                method_name, try_name, expected_value, actual_value)

    def try_good_args_true():
        try_name = 'good_args_true'
        g.Grammar.clear_all()
        ll.Llist.set_entry(r.Rule.rule_name_list_name, name)
        actual_value = cn.ComponentName._component_name_is_listed(
            component_type, name)
        expected_value = True
        if not actual_value == expected_value:
            g.Grammar.print_test_error_message(
                method_name, try_name, expected_value, actual_value)

    try_bad_value_component_type()
    try_good_args_false()
    try_good_args_true()

def test__component_name_is_well_formed():
    method_name = '_component_name_is_well_formed'

    def try_false():
        try_name = 'false'
        g.Grammar.clear_all()
        actual_value = cn.ComponentName._component_name_is_well_formed(
            ill_formed_component_name)
        expected_value = False
        if not actual_value == expected_value:
            g.Grammar.print_test_error_message(
                method_name, try_name, expected_value, actual_value)

    def try_good():
        try_name = 'true'
        g.Grammar.clear_all()
        actual_value = cn.ComponentName._component_name_is_well_formed(
            well_formed_component_name)
        expected_value = True
        if not actual_value == expected_value:
            g.Grammar.print_test_error_message(
                method_name, try_name, expected_value, actual_value)

    try_false()
    try_good()

def test_get_component_name_from_user():
    method_name = 'get_component_name_from_user'

    def try_good_arg():
        try_name = 'good_arg'
        g.Grammar.clear_all()
        actual_value = cn.ComponentName.get_component_name_from_user(
            component_type)
        expected_value = rule_name
        if not actual_value == expected_value:
            g.Grammar.print_test_error_message(
                method_name, try_name, expected_value, actual_value)

    try_good_arg()

def test_get_shape_name_from_user():
    method_name = 'get_shape_name_from_user'

    def try_good_arg():
        try_name = 'good_arg'
        g.Grammar.clear_all()
        actual_value = cn.ComponentName.get_shape_name_from_user()
        expected_value = shape_name
        if not actual_value == expected_value:
            g.Grammar.print_test_error_message(
                method_name, try_name, expected_value, actual_value)

    try_good_arg()

def test_get_rule_name_from_user():
    method_name = 'get_rule_name_from_user'

    def try_good_arg():
        try_name = 'good_arg'
        g.Grammar.clear_all()
        actual_value = cn.ComponentName.get_rule_name_from_user()
        expected_value = rule_name
        if not actual_value == expected_value:
            g.Grammar.print_test_error_message(
                method_name, try_name, expected_value, actual_value)

    try_good_arg()

def test_get_initial_shape_name_from_user():
    method_name = 'get_initial_shape_name_from_user'
    def try_good_arg():
        try_name = 'good_arg'
        g.Grammar.clear_all()
        actual_value = cn.ComponentName.get_initial_shape_name_from_user()
        expected_value = initial_shape_name
        if not actual_value == expected_value:
            g.Grammar.print_test_error_message(
                method_name, try_name, expected_value, actual_value)

    try_good_arg()

test__component_name_is_well_formed()
test__component_name_is_listed()
test_get_component_name_from_user()
test_get_shape_name_from_user()
test_get_rule_name_from_user()
test_get_initial_shape_name_from_user()

