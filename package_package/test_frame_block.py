from package.model import frame_block as fb
import rhinoscriptsyntax as rs


def test_new():
    _initialize_test()
    # layer_name = 'test_layer'
    # rs.AddLayer(layer_name)
    frame_block_name = 'frame block'
    actual_name = fb.FrameBlock.new()
    expected_name = frame_block_name
    if not actual_name == expected_name:
        print("new: frame_block_name: expected '%s'; got '%s'" % (
            expected_name, actual_name))

def _initialize_test():
    guids = rs.AllObjects()
    rs.DeleteObjects(guids)
    block_names = rs.BlockNames()
    for name in block_names:
        rs.DeleteBlock(name)
    layer_names = rs.LayerNames(True)
    for layer_name in layer_names:
        rs.DeleteLayer(layer_name)
    rs.DeleteDocumentData()


test_new()