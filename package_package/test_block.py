from package.view import block as b
from package.view import grammar as g
from package.view import layer as l
from package.view import rule_frame_block as rfb
import rhinoscriptsyntax as rs

def test_new():
    method_name = 'new'
    bad_type_frame_guids = 37
    bad_type_base_point = 37
    bad_type_block_name = 37
    bad_type_delete_input = 37

    def try_bad_type_frame_guids():
        try_name = 'bad_type_frame_guids'
        g.Grammar.clear_all()
        position = [0, 0, 0]
        block_name = 'test block'
        delete_input = True
        actual_value = b.Block.new(
            bad_type_frame_guids, position, block_name, delete_input)
        expected_value = None
        if not actual_value == expected_value:
            g.Grammar.print_test_error_message(
                method_name, try_name, expected_value, actual_value)

    def try_bad_type_base_point():
        try_name = 'bad_type_base_point'
        g.Grammar.clear_all()
        frame_guid = rs.AddLine([0, 0, 0], [5, 5, 0])
        frame_guids = [frame_guid]
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
        position = [0, 0, 0]
        delete_input = True
        actual_value = b.Block.new(
            frame_guids, position, bad_type_block_name, delete_input)
        expected_value = None
        if not actual_value == expected_value:
            g.Grammar.print_test_error_message(
                method_name, try_name, expected_value, actual_value)

    def try_bad_type_delete_input():
        try_name = 'bad_type_delete_input'
        g.Grammar.clear_all()
        frame_guid = rs.AddLine([0, 0, 0], [5, 5, 0])
        frame_guids = [frame_guid]
        position = [0, 0, 0]
        block_name = 'test block'
        actual_value = b.Block.new(
            frame_guids, position, block_name, bad_type_delete_input)
        expected_value = None
        if not actual_value == expected_value:
            g.Grammar.print_test_error_message(
                method_name, try_name, expected_value, actual_value)

    def try_good_args():
        try_name = 'good_args'
        g.Grammar.clear_all()
        frame_guid = rs.AddLine([0, 0, 0], [5, 5, 0])
        frame_guids = [frame_guid]
        position = [0, 0, 0]
        block_name = 'test block'
        delete_input = True
        actual_value = b.Block.new(
            frame_guids, position, block_name, delete_input)
        expected_value = block_name
        if not actual_value == expected_value:
            g.Grammar.print_test_error_message(
                method_name, try_name, expected_value, actual_value)

    try_bad_type_frame_guids()
    try_bad_type_base_point()
    try_bad_type_block_name()
    try_bad_type_delete_input()
    try_good_args()

def test_insert():
    method_name = 'insert'
    bad_type_position = 37
    bad_type_block_name = 37
    bad_value_frame_type = 'kilroy'
    bad_value_position = [0, 0, 5]
    bad_value_block_name = 'bad_value_block_name'
    frame_type = 'rule'
    position = [5, 5, 0]                        ##  'base point'?

    def try_bad_type_block_name():
        try_name = 'bad_type_block_name'
        g.Grammar.clear_all()
        actual_value = b.Block.insert(bad_type_block_name, position)
        expected_value = None
        if not actual_value == expected_value:
            g.Grammar.print_test_error_message(
                method_name, try_name, expected_value, actual_value)

    def try_bad_type_position():
        try_name = 'bad_type_position'
        g.Grammar.clear_all()
        block_name = rfb.RuleFrameBlock.new()   ##  method from other class
        actual_value = b.Block.insert(block_name, bad_type_position)
        expected_value = None
        if not actual_value == expected_value:
            g.Grammar.print_test_error_message(
                method_name, try_name, expected_value, actual_value)

    def try_bad_value_position():
        try_name = 'bad_value_position'
        g.Grammar.clear_all()
        block_name = rfb.RuleFrameBlock.new()   ##  method from other class
        actual_value = b.Block.insert(
            block_name, bad_value_position)
        expected_value = None
        if not actual_value == expected_value:
            g.Grammar.print_test_error_message(
                method_name, try_name, expected_value, actual_value)

    def try_bad_value_block_name():
        try_name = 'bad_value_block_name'
        g.Grammar.clear_all()
        l.Layer.new(bad_value_block_name)       ##  method from other class
        actual_value = b.Block.insert(
            bad_value_block_name, position)
        expected_value = None
        if not actual_value == expected_value:
            g.Grammar.print_test_error_message(
                method_name, try_name, expected_value, actual_value)

    def try_good_args():
        try_name = 'good_args'
        g.Grammar.clear_all()
        block_name = rfb.RuleFrameBlock.new()   ##  method from other class
        actual_value = b.Block.insert(block_name, position)
        expected_value = block_name
        if not actual_value == expected_value:
            g.Grammar.print_test_error_message(
                method_name, try_name, expected_value, actual_value)

    try_bad_type_block_name()
    try_bad_type_position()
    try_bad_value_position()
    try_bad_value_block_name()
    try_good_args()

test_new()
test_insert()