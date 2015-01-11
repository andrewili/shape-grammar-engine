from package.model import frame as f
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
    for name in layer_names:
        rs.DeleteLayer(name)

def _clear_dictionaries():
    rs.DeleteDocumentData()

def test_new():
    _clear_all()
    guids = f.Frame.new()
    actual_value = len(guids)
    expected_value = len(f.Frame.point_pairs)
    if not actual_value == expected_value:
        print("new: expected %i; got %i" % (expected_value, actual_value))

test_new()
