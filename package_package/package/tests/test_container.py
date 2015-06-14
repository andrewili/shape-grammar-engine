from package.view import container as c
from package.view import frame_block as fb
from package.view import grammar as g
from package.view import initial_shape as ish
from package.view import rule as r
import rhinoscriptsyntax as rs
from package.tests import utilities as u

def test_new():
    def try_good_args_initial_shape():
        try_name = 'good_args_initial_shape'
        _set_up()
        name = 'initial shape'
        origin = (0, 0, 0)
        ttype = ish.InitialShape.component_type
        actual_value = c.Container.new(name, origin, ttype)
        expected_value = name
        if not actual_value == expected_value:
            u.Utilities.print_test_error_message(
                method_name, try_name, expected_value, actual_value)

    def try_good_args_rule():
        try_name = 'good_args_rule'
        _set_up()
        rule_name = 'rule'
        origin = (0, 0, 0)
        ttype = r.Rule.component_type
        actual_value = c.Container.new(rule_name, origin, ttype)
        expected_value = rule_name
        if not actual_value == expected_value:
            u.Utilities.print_test_error_message(
                method_name, try_name, expected_value, actual_value)

    method_name = 'new'
    try_good_args_initial_shape()
    try_good_args_rule()

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
        name = 'shape'
        ttype = ish.InitialShape.component_type
        position = (0, 0, 0)
        guid = c.Container._add_name_tag(name, ttype, position)
        guid_matches_name = _guid_matches_name(guid, name)
        tag_is_in_group = _tag_is_in_group(guid, ttype)
        actual_value = (guid_matches_name, tag_is_in_group)
        expected_value = (True, True)
        if not actual_value == expected_value:
            u.Utilities.print_test_error_message(
                method_name, try_name, expected_value, actual_value)

    method_name = '_add_name_tag'
    try_good_args()

def _set_up():
    g.Grammar.clear_all()
    fb.FrameBlock.new()
    rs.AddGroup(ish.InitialShape.component_type)

def _guid_matches_name(guid, name):
    guid_text = rs.TextObjectText(guid)
    value = guid_text == name
    return value

def _tag_is_in_group(guid, group):
    groups = rs.ObjectGroups(guid)
    value = group in groups
    return value

test_new()
# test__add_initial_shape_frame_block()
# test__add_rule_frame_blocks()
# test__add_name_tag()
