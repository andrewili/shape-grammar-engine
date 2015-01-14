from package.model import frame as f
from package.model import frame_block as fb
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

def _set_all():
    _set_frame_block()

def _set_frame_block():
    layer_name = fb.FrameBlock.layer_name
    rs.AddLayer(layer_name)
    rs.CurrentLayer(layer_name)
    frame_guids = f.Frame.new()
    base_point = fb.FrameBlock.base_point
    block_name = fb.FrameBlock.block_name
    rs.AddBlock(frame_guids, base_point, block_name)
    rs.CurrentLayer('Default')

def test_new():
    def try_bad_state_block_exists():
        _clear_all()
        _set_frame_block()
        actual_name = fb.FrameBlock.new()
        expected_name = None
        if not actual_name == expected_name:
            print("new: bad_state_block_exists: expected '%s'; got '%s'" % (
                expected_name, actual_name))

    def try_good_state():
        _clear_all()
        frame_block_name = 'frame block'
        actual_name = fb.FrameBlock.new()
        expected_name = frame_block_name
        if not actual_name == expected_name:
            print("new: good_state: expected '%s'; got '%s'" % (
                expected_name, actual_name))

    try_bad_state_block_exists()
    try_good_state()

def test_delete():
    def try_no_block():
        _clear_all()
        actual_value = fb.FrameBlock.delete()
        expected_value = False
        if not actual_value == expected_value:
            print("delete: no_block: expected '%s'; got '%s'" % (
                expected_value, actual_value))

    def try_no_layer():
        _clear_all()
        frame_guids = f.Frame.new()
        base_point = fb.FrameBlock.base_point
        block_name = fb.FrameBlock.block_name
        rs.AddBlock(frame_guids, base_point, block_name)
        actual_value = fb.FrameBlock.delete()
        expected_value = False
        if not actual_value == expected_value:
            print("delete: no_layer: expected '%s'; got '%s'" % (
                expected_value, actual_value))

    def try_true():
        _clear_all()
        _set_frame_block()
        actual_value = fb.FrameBlock.delete()
        # expected_value = True
        # if not actual_value == expected_value:
        #     print("delete: try_true: expected '%s'; got '%s'" % (
        #         expected_value, actual_value))

    # try_no_block()
    # try_no_layer()
    try_true()

# _clear_all()
# test_new()
test_delete()
