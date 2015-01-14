from package.model import dictionary as d
from package.model import layer as l
import rhinoscriptsyntax as rs

layer_dict_name = l.Layer.layer_dict_name
layer_name = 'layer name'
layer_value = l.Layer.layer_value
good_layer_name = 'good layer'
# color_name

def _clear_all():
    layer_names = rs.LayerNames()
    for name in layer_names:
        rs.DeleteLayer(name)
    rs.DeleteDocumentData()

def _set_test_layer():
    rs.AddLayer(layer_name)
    rs.SetDocumentData(layer_dict_name, layer_name, layer_value)

def _initialize_test():                         ##  revise as _clear_all
    layer_names = rs.LayerNames(True)
    for layer_name in layer_names:
        rs.DeleteLayer(layer_name)
    rs.DeleteDocumentData()
    rs.AddLayer(layer_name)
    rs.SetDocumentData(layer_dict_name, layer_name, layer_value)

def test_new():
    def try_bad_type_layer_name():
        _initialize_test()
        bad_type_layer_name = 37
        actual_value = l.Layer.new(bad_type_layer_name)
        expected_value = None
        if not actual_value == expected_value:
            print("new: bad_type_layer_name: expected '%s'; got '%s'" % (
                expected_value, actual_value))

    def try_bad_type_color_name():
        _initialize_test()
        bad_type_color_name = 37
        actual_value = l.Layer.new(good_layer_name, bad_type_color_name)
        expected_value = None
        if not actual_value == expected_value:
            print("new: bad_type_color_name: expected '%s'; got '%s'" % (
                expected_value, actual_value))

    def try_bad_value_layer_name():
        _initialize_test()
        bad_value_layer_name = layer_name
        actual_value = l.Layer.new(bad_value_layer_name)
        expected_value = None
        if not actual_value == expected_value:
            print("new: bad_value_layer_name: expected '%s'; got '%s'" % (
                expected_value, actual_value))

    def try_good_args():
        _initialize_test()
        actual_value = l.Layer.new(good_layer_name)
        expected_value = good_layer_name
        if not actual_value == expected_value:
            print("new: good_args: expected '%s'; got '%s'" % (
                expected_value, actual_value))

    try_bad_type_layer_name()
    try_bad_type_color_name()
    try_bad_value_layer_name()
    try_good_args()

def test__layer_name_is_in_use():
    def try_bad_type_layer_name():
        _initialize_test()
        bad_type_layer_name = 37
        actual_value = l.Layer._layer_name_is_in_use(bad_type_layer_name)
        expected_value = False
        if not actual_value == expected_value:
            print("%s %s" % (
                "_layer_name_is_in_use: bad_type_layer_name:",
                "expected: '%s'; got: '%s'" % (expected_value, actual_value)))

    def try_good_arg_false():
        _initialize_test()
        good_arg_false = 'kilroy'
        actual_value = l.Layer._layer_name_is_in_use(good_arg_false)
        expected_value = False
        # if actual_value == expected_value:
        if not actual_value == expected_value:
            print("%s %s" % (
                "_layer_name_is_in_use: good_arg_false:",
                "expected '%s'; got '%s'" % (expected_value, actual_value)))

    def try_good_arg_true():                    ##  I am here
        _clear_all()
        _set_test_layer()
        good_arg_true = layer_name
        actual_value = l.Layer._layer_name_is_in_use(good_arg_true)
        expected_value = True
        if not actual_value == expected_value:
            print("%s %s" % (
                "_layer_name_is_in_use: good_arg_true:",
                "expected '%s'; got '%s'" % (expected_value, actual_value)))

    try_bad_type_layer_name()
    try_good_arg_false()
    try_good_arg_true()

def test_delete():
    def try_bad_type_layer_name():
        _initialize_test()
        bad_type_layer_name = 37
        actual_value = l.Layer.delete(bad_type_layer_name)
        expected_value = None
        if not actual_value == expected_value:
            print("delete: bad_type_layer_name: expected '%s'; got '%s'" % (
                expected_value, actual_value))

    def try_bad_value_layer_name():
        _initialize_test()
        bad_value_layer_name = 'kilroy'
        actual_value = l.Layer.delete(bad_value_layer_name)
        expected_value = None
        if not actual_value == expected_value:
            print("delete: bad_value_layer_name: expected '%s'; got '%s'" % (
                expected_value, actual_value))

    def try_good_arg():
        good_arg = layer_name
        actual_value = l.Layer.delete(layer_name)
        expected_value = True
        if not actual_value == expected_value:
            print("delete: good_arg: expected '%s'; got '%s'" % (
                expected_value, actual_value))

    try_bad_type_layer_name()
    try_bad_value_layer_name()
    try_good_arg()

test__layer_name_is_in_use()
test_new()
test_delete()


# def test_get_dict_name():
    # actual_dict_name = l.Layer._get_dict_name()
    # expected_dict_name = 'user layer names'
    # if not actual_dict_name == expected_dict_name:
    #     print("%s %s" % (
    #         "actual_dict_name: expected '%s';" % expected_dict_name,
    #         "got %s" % actual_dict_name))

# def test_add_layer():
    # def clear_layers():
        # user_layer_dict_name = l.Layer._get_dict_name()
        # user_layer_names_before = rs.GetDocumentData(user_layer_dict_name)
        # system_layer_names = rs.LayerNames()
        # for user_layer_name in user_layer_names_before:
        #     if user_layer_name in system_layer_names:
        #         rs.DeleteLayer(user_layer_name)
        # rs.DeleteDocumentData(user_layer_dict_name)

    # def add_layer(layer_name, color_name):
        # layer_name_out = l.Layer._add_layer(layer_name, color_name)
        # if not layer_name_out == layer_name:
        #     print("layer_name_out: expected '%s'; got %s" % (
        #         layer_name, layer_name_out))

    # def check_dict_layer_names():
        # expected_value = l.Layer._get_layer_value()
        # actual_value = d.Dictionary.get_value(
        #     user_layer_dict_name, layer_name)
        # if not expected_value == actual_value:
        #     print("actual_value: expected '%s'; got '%s'" % (
        #         expected_value, actual_value))

    # user_layer_dict_name = l.Layer._get_dict_name()
    # layer_name = 'layer name'
    # color_name = 'dark gray'
    # clear_layers()
    # add_layer(layer_name, color_name)
    # check_dict_layer_names()

# def test_record_layer_name():
    # l.Layer._record_layer_name("user layer name")


