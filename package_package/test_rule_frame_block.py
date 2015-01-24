from System.Drawing import Color
from package.model import frame_block as fb
from package.model import grammar as g
from package.model import layer as l
from package.model import llist as ll
from package.model import rule_frame_block as rfb
import rhinoscriptsyntax as rs

def _add_frames_layer():
    layer_name = fb.FrameBlock.layer_name
    dark_gray = Color.FromArgb(105, 105, 105)
    rs.AddLayer(layer_name, dark_gray)
    layer_name_list_name = l.Layer.layer_name_list_name
    layer_name = fb.FrameBlock.layer_name
    layer_value = ll.Llist.dummy_value
    rs.SetDocumentData(layer_name_list_name, layer_name, layer_value)

def test_new():
    method_name = 'new'

    def try_good_state_layer_does_not_exist():
        try_name = 'bad_state_no_layer'
        g.Grammar.clear_all()
        actual_value = rfb.RuleFrameBlock.new()
        expected_value = rfb.RuleFrameBlock.block_name
        if not actual_value == expected_value:
            g.Grammar.print_test_error_message(
                method_name, try_name, expected_value, actual_value)

    def try_good_state_layer_exists():
        try_name = 'good_state'
        g.Grammar.clear_all()
        _add_frames_layer()
        actual_value = rfb.RuleFrameBlock.new()
        expected_value = rfb.RuleFrameBlock.block_name
        if not actual_value == expected_value:
            g.Grammar.print_test_error_message(
                method_name, try_name, expected_value, actual_value)

    try_good_state_layer_does_not_exist()
    try_good_state_layer_exists()

test_new()
