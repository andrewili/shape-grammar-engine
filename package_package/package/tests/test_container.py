from package.view import container as c
from package.view import frame_block as fb
from package.view import grammar as g
from package.view import initial_shape as ish
from package.view import rule as r
import rhinoscriptsyntax as rs
from package.tests import utilities as u

def test_new():
    def try_bad_value_name():
        try_name = 'bad_value_name'
        _set_up()
        ish.InitialShape.add_first()
        bad_value_name = ish.InitialShape.first_initial_shape_name
        origin = ish.InitialShape.first_initial_shape_origin
        ttype = ish.InitialShape.component_type
        actual_value = c.Container.new(bad_value_name, origin, ttype)
        expected_value = None
        if not actual_value == expected_value:
            u.Utilities.print_test_error_message(
                method_name, try_name, expected_value, actual_value)

    def try_good_args_initial_shape():
        try_name = 'good_args_initial_shape'
        _set_up()
        initial_shape_name = 'initial shape'
        origin = rs.GetPoint('Select origin')
        ttype = ish.InitialShape.component_type
        actual_value = c.Container.new(initial_shape_name, origin, ttype)
        expected_value = initial_shape_name
        if not actual_value == expected_value:
            u.Utilities.print_test_error_message(
                method_name, try_name, expected_value, actual_value)

    def try_good_args_rule():
        try_name = 'good_args_rule'
        _set_up()
        rule_name = 'rule'
        origin = rs.GetPoint('Select origin')
        ttype = r.Rule.component_type
        actual_value = c.Container.new(rule_name, origin, ttype)
        expected_value = rule_name
        if not actual_value == expected_value:
            u.Utilities.print_test_error_message(
                method_name, try_name, expected_value, actual_value)

    method_name = 'new'
    try_bad_value_name()
    # try_good_args_initial_shape()
    # try_good_args_rule()

def test__add_initial_shape_frame_block():
    method_name = '_add_initial_shape_frame_block'
    try_name = 'try_name'
    _set_up()
    name = 'initial shape'
    message = "Select the origin of the initial shape container. z = 0"
    origin = rs.GetPoint(message)
    actual_value = c.Container._add_initial_shape_frame_block(
        name, origin)
    expected_value = name
    if not actual_value == expected_value:
        u.Utilities.print_test_error_message(
            method_name, try_name, expected_value, actual_value)

def test__add_rule_frame_blocks():
    method_name = '_add_rule_frame_blocks'
    try_name = 'try_name'
    _set_up()
    name = 'rule 1'
    message = "Select the origin of the rule container. z = 0"
    origin = rs.GetPoint(message)
    actual_value = c.Container._add_rule_frame_blocks(name, origin)
    expected_value = name
    if not actual_value == expected_value:
        u.Utilities.print_test_error_message(
            method_name, try_name, expected_value, actual_value)

def test__add_name_tag():
    def try_good_args():
        try_name = 'good_args'
        _set_up()
        _add_name_not_in_group()
        name = 'in group'
        ttype = ish.InitialShape.component_type
        origin = (20, 0, 0)
        guid = c.Container._add_name_tag(name, ttype, origin)
        select_names_in_group(ttype)

        # name = 'name'
        # ttype = ish.InitialShape.component_type
        # message = 'Select point'
        # origin = rs.GetPoint(message)
        # c.Container._add_name_tag(name, ttype, origin)
        # items_in_group = rs.ObjectsByGroup(ttype)
        # for item in items_in_group:
        #     rs.SelectObject(item)

    method_name = '_add_name_tag'
    try_good_args()

def _set_up():
    g.Grammar.clear_all()
    fb.FrameBlock.new()
    rs.AddGroup(ish.InitialShape.component_type)

def _add_name_not_in_group():
    ttype = r.Rule.component_type
    rs.AddGroup(ttype)
    position = (0, 0, 0)
    c.Container._add_name_tag('not in group', ttype, position)

def select_names_in_group(ttype):
    items = rs.ObjectsByGroup(ttype)
    for item in items:
        rs.SelectObject(item)
    print('kilroy was here')

# test_new()
# test__add_initial_shape_frame_block()
# test__add_rule_frame_blocks()
test__add_name_tag()
