from package.model import grammar as g
from package.model import rule_frame_block as rfb
import rhinoscriptsyntax as rs

position = [0, 0, 0]
user_assigned_name = 'test'

def test_add_initial_shape():
    method_name = 'add_initial_shape'

    def try_bad_state():
        try_name = 'bad_state'

    def try_good_state():
        try_name = 'good_state'
        g.Grammar.clear_all()
        rfb.RuleFrameBlock.new()                ##  outside methods
        rfb.RuleFrameBlock.insert(position, user_assigned_name)
        actual_value = g.Grammar.add_initial_shape()
        print("%s: %s: actual_value: %s" % (
            method_name, try_name, actual_value))

    # try_bad_state()
    try_good_state()

test_add_initial_shape()
