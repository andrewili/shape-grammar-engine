from package.model import dictionary as d
from package.model import layer as l
import rhinoscriptsyntax as rs

### layer utilities
def test_get_dict_name():
    actual_dict_name = l.Layer._get_dict_name()
    expected_dict_name = 'user layer names'
    if not actual_dict_name == expected_dict_name:
        print("%s %s" % (
            "actual_dict_name: expected '%s';" % expected_dict_name,
            "got %s" % actual_dict_name))

def test_name_is_in_use():
    user_layer_dict_name = l.Layer._get_dict_name()
    layer_name = 'user layer name'
    layer_value = l.Layer._get_layer_value()
    d.Dictionary.set_value(user_layer_dict_name, layer_name, layer_value)
    name_is_in_use = l.Layer._name_is_in_use(layer_name)
    if not name_is_in_use == True:
        print("name_is_in_use: expected True; got %s" % name_is_in_use)

def test_add_layer():
    def clear_layers():
        user_layer_dict_name = l.Layer._get_dict_name()
        user_layer_names_before = rs.GetDocumentData(user_layer_dict_name)
        system_layer_names = rs.LayerNames()
        for user_layer_name in user_layer_names_before:
            if user_layer_name in system_layer_names:
                rs.DeleteLayer(user_layer_name)
        rs.DeleteDocumentData(user_layer_dict_name)
    def add_layer(layer_name, color_name):
        layer_name_out = l.Layer._add_layer(layer_name, color_name)
        if not layer_name_out == layer_name:
            print("layer_name_out: expected '%s'; got %s" % (
                layer_name, layer_name_out))
    def check_dict_layer_names():
        expected_value = l.Layer._get_layer_value()
        actual_value = d.Dictionary.get_value(
            user_layer_dict_name, layer_name)
        if not expected_value == actual_value:
            print("actual_value: expected '%s'; got '%s'" % (
                expected_value, actual_value))
    user_layer_dict_name = l.Layer._get_dict_name()
    layer_name = 'layer name'
    color_name = 'dark gray'
    clear_layers()
    add_layer(layer_name, color_name)
    check_dict_layer_names()

def test_record_layer_name():
    l.Layer._record_layer_name("user layer name")

def test_new():
    def clear_layers():
        pass
    def add_layer():
        pass
    def add_layer_again():
        pass
    clear_layers()
    add_layer()
    add_layer_again()

test_get_dict_name()
test_name_is_in_use()
test_add_layer()
test_record_layer_name()
# test_new()