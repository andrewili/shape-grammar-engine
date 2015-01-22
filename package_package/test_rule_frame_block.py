from System.Drawing import Color
from package.model import frame_block as fb
from package.model import layer as l
from package.model import llist as ll
from package.model import rule_frame_block as rfb
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

def _add_frames_layer():
    layer_name = fb.FrameBlock.layer_name
    dark_gray = Color.FromArgb(105, 105, 105)
    rs.AddLayer(layer_name, dark_gray)
    layer_name_list_name = l.Layer.layer_name_list_name
    layer_name = fb.FrameBlock.layer_name
    layer_value = ll.Llist.dummy_value
    rs.SetDocumentData(layer_name_list_name, layer_name, layer_value)

def _print_error_message(method_name, try_name, expected_value, actual_value):
    message = "%s: %s:\n    expected '%s'; got '%s'" % (
        method_name, try_name, expected_value, actual_value)
    print(message)

def test_new():
    method_name = 'new'

    def try_bad_state_no_layer():
        try_name = 'bad_state_no_layer'
        _clear_all()
        actual_value = rfb.RuleFrameBlock.new()
        expected_value = None
        if not actual_value == expected_value:
            _print_error_message(
                method_name, try_name, expected_value, actual_value)

    def try_good_state():
        try_name = 'good_state'
        _clear_all()
        _add_frames_layer()
        actual_value = rfb.RuleFrameBlock.new()
        expected_value = rfb.RuleFrameBlock.block_name
        if not actual_value == expected_value:
            _print_error_message(
                method_name, try_name, expected_value, actual_value)

    try_bad_state_no_layer()
    try_good_state()

test_new()
