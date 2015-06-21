from package.view import grammar as g
from package.view import layer as l
import rhinoscriptsyntax as rs
from package.tests import utilities as u

def test_new():
    def try_good_args():
        try_name = 'good_args'
        g.Grammar.clear_all()
        name = 'gaudi'
        actual_value = l.Layer.new(name)
        expected_value = name
        if not actual_value == expected_value:
            u.Utilities.print_test_error_message(
                method_name, try_name, expected_value, actual_value)

    method_name = 'new'
    try_good_args()

def test_new_1_frame_block():
    def try_good_args():
        try_name = 'good_args'
        g.Grammar.clear_all()
        name = 'gaudi'
        origin = (10, 10, 0)
        actual_value = l.Layer.new_1_frame_block(name, origin)
        expected_value = name
        if not actual_value == expected_value:
            u.Utilities.print_test_error_message(
                method_name, try_name, expected_value, actual_value)

    method_name = 'new_1_frame_block'
    try_good_args()

def test_new_2_frame_blocks():
    try_good_args()

test_new()
# test_new_1_frame_block()
# test_new_2_frame_blocks()