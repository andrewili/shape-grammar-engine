from package.view import container as c
from package.view import frame_block as fb
from package.view import grammar as g
import rhinoscriptsyntax as rs
from package.tests import utilities as u

def test_add_initial_shape_frame_block():
    method_name = 'add_initial_shape_frame_block'
    try_name = 'try_name'
    g.Grammar.clear_all()
    fb.FrameBlock.new()
    name = 'initial shape'
    message = "Select the origin of the initial shape container. z = 0"
    origin = rs.GetPoint(message)
    actual_value = c.Container.add_initial_shape_frame_block(
        name, origin)
    expected_value = name
    if not actual_value == expected_value:
        u.Utilities.print_test_error_message(
            method_name, try_name, expected_value, actual_value)

def test_add_rule_frame_blocks():
    method_name = 'add_rule_frame_blocks'
    try_name = 'try_name'
    g.Grammar.clear_all()
    fb.FrameBlock.new()
    name = 'rule 1'
    message = "Select the origin of the rule container. z = 0"
    origin = rs.GetPoint(message)
    actual_value = c.Container.add_rule_frame_blocks(name, origin)
    expected_value = name
    if not actual_value == expected_value:
        u.Utilities.print_test_error_message(
            method_name, try_name, expected_value, actual_value)

test_add_initial_shape_frame_block()
test_add_rule_frame_blocks()
