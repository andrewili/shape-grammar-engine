from package.model import frame_block as fb
from package.model import grammar as g
from package.model import rule_frame_block as rfb
import rhinoscriptsyntax as rs

position = [0, 0, 0]
existing_shape_name = 'existing shape'
bad_type_name = 37
bad_value_name = existing_shape_name
new_shape_name = 'new_shape'

def test_add_initial_shape():
    method_name = 'add_unnamed_initial_shape_frame'

    # def try_good_state():
    #     try_name = 'good_state'
    #     g.Grammar.clear_all()
    #                                             # fb.FrameBlock
    #     rfb.RuleFrameBlock.new()                ##  outside methods
    #     rfb.RuleFrameBlock.insert(position, existing_shape_name)
    #     actual_value = g.Grammar.add_unnamed_initial_shape_frame()
    #     print("%s: %s: actual_value: %s" % (
    #         method_name, try_name, actual_value))

    # try_good_state()

def test__add_named_initial_shape_frame():
    method_name = '_add_named_initial_shape_frame'

    def try_bad_type():
        try_name = 'bad_type_name'
        g.Grammar.clear_all()
        actual_value = g.Grammar._add_named_initial_shape_frame(bad_type_name)
        expected_value = None
        if not actual_value == expected_value:
            g.Grammar.print_test_error_message(
                method_name, try_name, expected_value, actual_value)

    def try_bad_value():
        try_name = 'bad_value_name'
        g.Grammar.clear_all()
        fb.FrameBlock.new()
        actual_value = g.Grammar._add_named_initial_shape_frame(
            bad_value_name)
        expected_value = None
        if not actual_value == expected_value:
            g.Grammar.print_test_error_message(
                method_name, try_name, expected_value, actual_value)

    def try_good_args():
        try_name = 'good_args'
        g.Grammar.clear_all()
        fb.FrameBlock.new()
        actual_value = g.Grammar._add_named_initial_shape_frame(
            new_shape_name)
        expected_value = new_shape_name
        if not actual_value == expected_value:
            g.Grammar.print_test_error_message(
                method_name, try_name, expected_value, actual_value)

    try_bad_type()
    try_bad_value()
    try_good_args()

# test_add_initial_shape()                      ##  pending _add_named_i_shape
test__add_named_initial_shape_frame()
