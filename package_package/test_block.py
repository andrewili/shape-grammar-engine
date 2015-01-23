from package.model import block as b
from package.model import grammar as g
import rhinoscriptsyntax as rs

# def g.Grammar.print_test_error_message(method_name, try_name, expected_value, actual_value):
#     message = "%s: %s:\n    expected '%s'; got '%s'" % (
#         method_name, try_name, expected_value, actual_value)
#     print(message)

def test_new():
    method_name = 'new'

    def try_bad_type_frame_guids():
        try_name = 'bad_type_frame_guids'
        g.Grammar.clear_all()
        bad_type_frame_guids = 37
        base_point = [0, 0, 0]
        block_name = 'test block'
        delete_input = True
        actual_value = b.Block.new(
            bad_type_frame_guids, base_point, block_name, delete_input)
        expected_value = None
        if not actual_value == expected_value:
            g.Grammar.print_test_error_message(
                method_name, try_name, expected_value, actual_value)

    def try_bad_type_base_point():
        try_name = 'bad_type_base_point'
        g.Grammar.clear_all()
        frame_guid = rs.AddLine([0, 0, 0], [5, 5, 0])
        frame_guids = [frame_guid]
        bad_type_base_point = 37
        block_name = 'test block'
        delete_input = True
        actual_value = b.Block.new(
            frame_guids, bad_type_base_point, block_name, delete_input)
        expected_value = None
        if not actual_value == expected_value:
            g.Grammar.print_test_error_message(
                method_name, try_name, expected_value, actual_value)

    def try_bad_type_block_name():
        try_name = 'bad_type_block_name'
        g.Grammar.clear_all()
        frame_guid = rs.AddLine([0, 0, 0], [5, 5, 0])
        frame_guids = [frame_guid]
        base_point = [0, 0, 0]
        bad_type_block_name = 37
        delete_input = True
        actual_value = b.Block.new(
            frame_guids, base_point, bad_type_block_name, delete_input)
        expected_value = None
        if not actual_value == expected_value:
            g.Grammar.print_test_error_message(
                method_name, try_name, expected_value, actual_value)

    def try_bad_type_delete_input():
        try_name = 'bad_type_delete_input'
        g.Grammar.clear_all()
        frame_guid = rs.AddLine([0, 0, 0], [5, 5, 0])
        frame_guids = [frame_guid]
        base_point = [0, 0, 0]
        block_name = 'test block'
        delete_input = 37
        actual_value = b.Block.new(
            frame_guids, base_point, block_name, delete_input)
        expected_value = None
        if not actual_value == expected_value:
            g.Grammar.print_test_error_message(
                method_name, try_name, expected_value, actual_value)

    def try_good_args():
        try_name = 'good_args'
        g.Grammar.clear_all()
        frame_guid = rs.AddLine([0, 0, 0], [5, 5, 0])
        frame_guids = [frame_guid]
        base_point = [0, 0, 0]
        block_name = 'test block'
        delete_input = True
        actual_value = b.Block.new(
            frame_guids, base_point, block_name, delete_input)
        expected_value = block_name
        if not actual_value == expected_value:
            g.Grammar.print_test_error_message(
                method_name, try_name, expected_value, actual_value)

    try_bad_type_frame_guids()
    try_bad_type_base_point()
    try_bad_type_block_name()
    try_bad_type_delete_input()
    try_good_args()

test_new()
