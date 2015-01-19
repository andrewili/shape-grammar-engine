from package.model import frame as f
from package.model import frame_block as fb
from package.model import layer as l
from package.model import llist as ll
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
        rs.DeleteLayer(layer_name)

def _clear_dictionaries():
    rs.DeleteDocumentData()

def _set_frame_block():
    _add_layer()
    _record_layer()
    _add_block()

def _add_layer():
    rs.AddLayer(fb.FrameBlock.layer_name)

def _record_layer():
    rs.SetDocumentData(
        l.Layer.layer_dict_name, 
        fb.FrameBlock.layer_name, 
        ll.Llist.dummy_value)

def _add_block():
    rs.CurrentLayer(fb.FrameBlock.layer_name)
    frame_guids = f.Frame.new()
    base_point = fb.FrameBlock.base_point
    block_name = fb.FrameBlock.block_name
    rs.AddBlock(frame_guids, base_point, block_name)
    rs.CurrentLayer('Default')

def _print_error_message(method_name, try_name, expected_value, actual_value):
    message = "%s: %s:\n    expected '%s'; got '%s'" % (
        method_name, try_name, expected_value, actual_value)
    print(message)

def test_new():
    method_name = 'new'

    def try_bad_state_block_exists():
        try_name = 'bad_state_block_exists'
        _clear_all()
        _set_frame_block()
        actual_value = fb.FrameBlock.new()
        expected_value = None
        if not actual_value == expected_value:
            _print_error_message(
                method_name, try_name, expected_value, actual_value)

    def try_good_state():
        try_name = 'good_state'
        _clear_all()
        frame_block_name = fb.FrameBlock.block_name
        actual_value = fb.FrameBlock.new()
        expected_value = frame_block_name
        if not actual_value == expected_value:
            _print_error_message(
                method_name, try_name, expected_value, actual_value)

    try_bad_state_block_exists()
    try_good_state()

def test_delete():
    method_name = 'delete'

    def try_bad_state_no_block():
        try_name = 'bad_state_no_block'
        _clear_all()
        actual_value = fb.FrameBlock.delete()
        expected_value = False
        if not actual_value == expected_value:
            _print_error_message(
                method_name, try_name, expected_value, actual_value)

    def try_bad_state_no_layer():
        try_name = 'bad_state_no_layer'
        _clear_all()
        frame_guids = f.Frame.new()
        base_point = fb.FrameBlock.base_point
        block_name = fb.FrameBlock.block_name
        rs.AddBlock(frame_guids, base_point, block_name)
        actual_value = fb.FrameBlock.delete()
        expected_value = False
        if not actual_value == expected_value:
            _print_error_message(
                method_name, try_name, expected_value, actual_value)

    def try_good_state():
        try_name = 'good_state'
        _clear_all()
        _set_frame_block()
        actual_value = fb.FrameBlock.delete()
        expected_value = True
        if not actual_value == expected_value:
            _print_error_message(
                method_name, try_name, expected_value, actual_value)

    try_bad_state_no_block()
    try_bad_state_no_layer()
    try_good_state()

test_new()
test_delete()
