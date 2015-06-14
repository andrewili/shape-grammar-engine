from package.view import container as c
from package.view import component_name as cn
from package.view import frame_block as fb
from package.view import grammar as g
from package.view import initial_shape as ish
from package.view import llist as ll
from package.view import rule as r
import rhinoscriptsyntax as rs
from package.tests import utilities as u

name = 'test_name'
rule_name = 'rule'
shape_name = 'shape'
initial_shape_name = 'initial_shape'

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

def test__get_new_from_user():
    def try_good_arg():
        try_name = 'good_arg'
        _set_up()
        _add_name_to_initial_shape_group()
        _add_name_to_rule_group()
        message = "Enter '%s'" % rule_name
        print(message)
        actual_value = cn.ComponentName._get_new_from_user(
            r.Rule.component_type)
        expected_value = rule_name
        if not actual_value == expected_value:
            u.Utilities.print_test_error_message(
                method_name, try_name, expected_value, actual_value)

    method_name = '_get_new_from_user'
    try_good_arg()

def test__is_well_formed():
    method_name = '_is_well_formed'

    def try_false():
        try_name = 'false'
        g.Grammar.clear_all()
        ill_formed_name = 'kil#roy'
        actual_value = cn.ComponentName._is_well_formed(ill_formed_name)
        expected_value = False
        if not actual_value == expected_value:
            u.Utilities.print_test_error_message(
                method_name, try_name, expected_value, actual_value)

    def try_good():
        try_name = 'true'
        g.Grammar.clear_all()
        well_formed_name = name
        actual_value = cn.ComponentName._is_well_formed(
            well_formed_name)
        expected_value = True
        if not actual_value == expected_value:
            u.Utilities.print_test_error_message(
                method_name, try_name, expected_value, actual_value)

    try_false()
    try_good()

def _set_up():
    g.Grammar.clear_all()
    fb.FrameBlock.new()
    rs.AddGroup(ish.InitialShape.component_type)
    rs.AddGroup(r.Rule.component_type)

def _add_name_to_initial_shape_group():
    rs.AddGroup(ish.InitialShape.component_type)
    initial_shape_name_guid = rs.AddText(
        ish.InitialShape.first_initial_shape_name, 
        ish.InitialShape.first_initial_shape_insertion_point)
    rs.AddObjectToGroup(
        initial_shape_name_guid, ish.InitialShape.component_type)

def _add_name_to_rule_group():
    rs.AddGroup(r.Rule.component_type)
    rule_name_guid = rs.AddText(
        r.Rule.first_rule_name, r.Rule.first_rule_insertion_point)
    rs.AddObjectToGroup(rule_name_guid, r.Rule.component_type)

def _add_preexisting_name_tag(name, ttype):
    origin = (0, 0, 0)
    tag_guid = rs.AddText(name, origin)
    rs.AddObjectToGroup(tag_guid, ttype)

def test__is_available():
    def try_false_ishape_name_exists():
        try_name = 'false_ishape_name_exists'
        _set_up()
        name = 'kilroy'
        ttype = ish.InitialShape.component_type
        _add_preexisting_name_tag(name, ttype)
        actual_value = cn.ComponentName._is_available(name)
        expected_value = False
        if not actual_value == expected_value:
            u.Utilities.print_test_error_message(
                method_name, try_name, expected_value, actual_value)

    def try_false_rule_name_exists():
        try_name = 'false_rule_name_exists'
        _set_up()
        name = 'kilroy'
        ttype = r.Rule.component_type
        _add_preexisting_name_tag(name, ttype)
        actual_value = cn.ComponentName._is_available(name)
        expected_value = False
        if not actual_value == expected_value:
            u.Utilities.print_test_error_message(
                method_name, try_name, expected_value, actual_value)

    def try_true():
        try_name = 'true'
        _set_up()
        name = 'kilroy'
        actual_value = cn.ComponentName._is_available(name)
        expected_value = True
        if not actual_value == expected_value:
            u.Utilities.print_test_error_message(
                method_name, try_name, expected_value, actual_value)

    method_name = '_is_available'
    try_false_ishape_name_exists()
    try_false_rule_name_exists()
    try_true()

test_get_initial_shape_name_from_user()
test_get_rule_name_from_user()
test__get_new_from_user()
test__is_well_formed()
test__is_available()

# def test__component_name_is_listed():
    # method_name = '_component_name_is_listed'

    # def try_bad_value_component_type():
    #     try_name = 'bad_value_component_type'
    #     actual_value = cn.ComponentName._component_name_is_listed(
    #         name, bad_value_component_type)
    #     expected_value = False
    #     if not actual_value == expected_value:
    #         u.Utilities.print_test_error_message(
    #             method_name, try_name, expected_value, actual_value)

    # def try_good_args_false():
    #     try_name = 'false'
    #     g.Grammar.clear_all()
    #     actual_value = cn.ComponentName._component_name_is_listed(
    #         name, component_type)
    #     expected_value = False
    #     if not actual_value == expected_value:
    #         u.Utilities.print_test_error_message(
    #             method_name, try_name, expected_value, actual_value)

    # def try_good_args_true():
    #     try_name = 'good_args_true'
    #     _set_up()
    #     ll.Llist.set_entry(g.Grammar.rules, name)
    #     actual_value = cn.ComponentName._component_name_is_listed(
    #         name, component_type)
    #     expected_value = True
    #     if not actual_value == expected_value:
    #         u.Utilities.print_test_error_message(
    #             method_name, try_name, expected_value, actual_value)

    # try_bad_value_component_type()
    # try_good_args_false()
    # try_good_args_true()

# test__component_name_is_listed()
