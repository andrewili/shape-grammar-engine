from package.view import container as c
from package.view import component_name as cn
from package.view import frame_block as fb
from package.view import grammar as g
from package.view import initial_shape as ish
from package.view import llist as ll
from package.view import rule as r
import rhinoscriptsyntax as rs
from package.tests import utilities as u

component_type = r.Rule.component_type
name = 'test_name'
rule_name = 'rule'
shape_name = 'shape'
initial_shape_name = 'initial_shape'
bad_value_component_type = 'bad_value_component_type'
bad_value_component_name = 'bad_value_component_name'
ill_formed_component_name = 'kil#roy'
well_formed_component_name = name

def test_get_initial_shape_name_from_user():
    def try_good_arg():
        try_name = 'good_arg'
        g.Grammar.clear_all()
        print("Enter '%s'" % initial_shape_name)
        actual_value = cn.ComponentName.get_initial_shape_name_from_user()
        expected_value = initial_shape_name
        if not actual_value == expected_value:
            u.Utilities.print_test_error_message(
                method_name, try_name, expected_value, actual_value)

    method_name = 'get_initial_shape_name_from_user'
    try_good_arg()

def test_get_rule_name_from_user():
    def try_good_arg():
        try_name = 'good_arg'
        g.Grammar.clear_all()
        print("Enter '%s'" % rule_name)
        actual_value = cn.ComponentName.get_rule_name_from_user()
        expected_value = rule_name
        if not actual_value == expected_value:
            u.Utilities.print_test_error_message(
                method_name, try_name, expected_value, actual_value)

    method_name = 'get_rule_name_from_user'
    try_good_arg()

def test_get_component_name_from_user():
    def try_good_arg():
        try_name = 'good_arg'
        _set_up()
        ish.InitialShape.add_first()
        r.Rule.add_first()
        message = "Enter: 1, '%s'; 2, '%s'; 3, %s; 4, '%s'" % (
            ish.InitialShape.first_initial_shape_name,
            r.Rule.first_rule_name,
            'an ill-formed name',
            'rule')
        print(message)
        actual_value = cn.ComponentName.get_component_name_from_user(
            component_type)
        expected_value = rule_name
        if not actual_value == expected_value:
            u.Utilities.print_test_error_message(
                method_name, try_name, expected_value, actual_value)

    method_name = 'get_component_name_from_user'
    try_good_arg()

def test__component_name_is_available():
    def try_good_state_false():
        try_name = 'good_state_false'
        _set_up()
        name = 'kilroy'
        origin = rs.GetPoint('Select origin')
        component_type = ish.InitialShape.component_type
        c.Container.new(name, origin, component_type)
        actual_value = cn.ComponentName._component_name_is_available(name)
        expected_value = False
        if not actual_value == expected_value:
            u.Utilities.print_test_error_message(
                method_name, try_name, expected_value, actual_value)

    def try_good_state_true():
        try_name = 'good_state_true'
        _set_up()
        name = 'kilroy'
        actual_value = cn.ComponentName._component_name_is_available(name)
        expected_value = True
        if not actual_value == expected_value:
            u.Utilities.print_test_error_message(
                method_name, try_name, expected_value, actual_value)

    method_name = '_component_name_is_available'
    try_good_state_false()
    try_good_state_true()

def test__component_name_is_listed():
    method_name = '_component_name_is_listed'

    def try_bad_value_component_type():
        try_name = 'bad_value_component_type'
        actual_value = cn.ComponentName._component_name_is_listed(
            name, bad_value_component_type)
        expected_value = False
        if not actual_value == expected_value:
            u.Utilities.print_test_error_message(
                method_name, try_name, expected_value, actual_value)

    def try_good_args_false():
        try_name = 'false'
        g.Grammar.clear_all()
        actual_value = cn.ComponentName._component_name_is_listed(
            name, component_type)
        expected_value = False
        if not actual_value == expected_value:
            u.Utilities.print_test_error_message(
                method_name, try_name, expected_value, actual_value)

    def try_good_args_true():
        try_name = 'good_args_true'
        _set_up()
        ll.Llist.set_entry(g.Grammar.rules, name)
        actual_value = cn.ComponentName._component_name_is_listed(
            name, component_type)
        expected_value = True
        if not actual_value == expected_value:
            u.Utilities.print_test_error_message(
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
            u.Utilities.print_test_error_message(
                method_name, try_name, expected_value, actual_value)

    def try_good():
        try_name = 'true'
        g.Grammar.clear_all()
        actual_value = cn.ComponentName._component_name_is_well_formed(
            well_formed_component_name)
        expected_value = True
        if not actual_value == expected_value:
            u.Utilities.print_test_error_message(
                method_name, try_name, expected_value, actual_value)

    try_false()
    try_good()

def _set_up():
    g.Grammar.clear_all()
    fb.FrameBlock.new()

# test_get_initial_shape_name_from_user()
test_get_rule_name_from_user()                ##  to do
# test_get_component_name_from_user()
# test__component_name_is_available()
# test__component_name_is_listed()
# test__component_name_is_well_formed()

# test_get_shape_name_from_user()
