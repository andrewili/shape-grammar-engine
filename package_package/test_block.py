from package.model import block as b
import rhinoscriptsyntax as rs

def _clear_all():
    _clear_objects()
    _clear_blocks()
    _clear_layers()
    _clear_dictionaries()

def _clear_objects():
    guids = rs.AllObjects()
    rs.DeleteObjects(guids)

def _clear_blocks():
    block_names = rs.BlockNames()
    for name in block_names:
        rs.DeleteBlock(name)

def _clear_layers():
    layer_names = rs.LayerNames()
    for layer_name in layer_names:
        if not layer_name == 'Default':
            rs.DeleteLayer(layer_name)

def _clear_dictionaries():
    rs.DeleteDocumentData()

def _print_error_message(method_name, try_name, expected_value, actual_value):
    message = "%s: %s:\n    expected '%s'; got '%s'" % (
        method_name, try_name, expected_value, actual_value)
    print(message)

def test_new():
    method_name = 'new'

    def try_bad_type_frame_guids():
        try_name = 'bad_type_frame_guids'
        _clear_all()
        bad_type_frame_guids = 37
        base_point = [0, 0, 0]
        block_name = 'test block'
        delete_input = True
        actual_value = b.Block.new(
            bad_type_frame_guids, base_point, block_name, delete_input)
        expected_value = None
        if not actual_value == expected_value:
            _print_error_message(
                method_name, try_name, expected_value, actual_value)

    def try_bad_type_base_point():
        try_name = 'bad_type_base_point'
        _clear_all()
        frame_guid = rs.AddLine([0, 0, 0], [5, 5, 0])
        frame_guids = [frame_guid]
        bad_type_base_point = 37
        block_name = 'test block'
        delete_input = True
        actual_value = b.Block.new(
            frame_guids, bad_type_base_point, block_name, delete_input)
        expected_value = None
        if not actual_value == expected_value:
            _print_error_message(
                method_name, try_name, expected_value, actual_value)

    def try_bad_type_block_name():
        try_name = 'bad_type_block_name'
        _clear_all()
        frame_guid = rs.AddLine([0, 0, 0], [5, 5, 0])
        frame_guids = [frame_guid]
        base_point = [0, 0, 0]
        bad_type_block_name = 37
        delete_input = True
        actual_value = b.Block.new(
            frame_guids, base_point, bad_type_block_name, delete_input)
        expected_value = None
        if not actual_value == expected_value:
            _print_error_message(
                method_name, try_name, expected_value, actual_value)

    def try_bad_type_delete_input():
        try_name = 'bad_type_delete_input'
        _clear_all()
        frame_guid = rs.AddLine([0, 0, 0], [5, 5, 0])
        frame_guids = [frame_guid]
        base_point = [0, 0, 0]
        block_name = 'test block'
        delete_input = 37
        actual_value = b.Block.new(
            frame_guids, base_point, block_name, delete_input)
        expected_value = None
        if not actual_value == expected_value:
            _print_error_message(
                method_name, try_name, expected_value, actual_value)

    def try_good_args():
        try_name = 'good_args'
        _clear_all()
        frame_guid = rs.AddLine([0, 0, 0], [5, 5, 0])
        frame_guids = [frame_guid]
        base_point = [0, 0, 0]
        block_name = 'test block'
        delete_input = True
        actual_value = b.Block.new(
            frame_guids, base_point, block_name, delete_input)
        expected_value = block_name
        if not actual_value == expected_value:
            _print_error_message(
                method_name, try_name, expected_value, actual_value)

    try_bad_type_frame_guids()
    try_bad_type_base_point()
    try_bad_type_block_name()
    try_bad_type_delete_input()
    try_good_args()

test_new()
