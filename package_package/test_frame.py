from package.model import frame as f
import rhinoscriptsyntax as rs

def test_new():
    _initialize_test()
    layer_name = 'test layer'
    rs.AddLayer(layer_name)
    f.Frame.new(layer_name)

def _initialize_test():
    guids = rs.AllObjects()
    rs.DeleteObjects(guids)
    layer_names = rs.LayerNames(True)
    for layer_name in layer_names:
        rs.DeleteLayer(layer_name)
    rs.DeleteDocumentData()

test_new()
