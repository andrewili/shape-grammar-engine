from package.model import layer as l
from package.model import llist as ll
import rhinoscriptsyntax as rs

layer_name_list_name = l.Layer.layer_name_list_name
layer_name = 'layer'
dummy_value = ll.Llist.dummy_value
good_layer_name = 'good layer'

def _clear_all():
    layer_names = rs.LayerNames()
    for name in layer_names:
        rs.DeleteLayer(name)
    rs.DeleteDocumentData()

def _set_test_layer():
    rs.AddLayer(layer_name)
    rs.SetDocumentData(layer_name_list_name, layer_name, dummy_value)

def _print_error_message(
        method_name, try_name, expected_value, actual_value):
    message = "%s: %s:\n    expected '%s'; got '%s'" % (
        method_name, try_name, expected_value, actual_value)
    print(message)

def test_layer_name_is_in_use():
    method_name = 'layer_name_is_in_use'

    def try_bad_type_layer_name():
        try_name = 'bad_type_layer_name'
        _clear_all()
        _set_test_layer()
        bad_type_layer_name = 37
        actual_value = l.Layer.layer_name_is_in_use(bad_type_layer_name)
        expected_value = False
        if not actual_value == expected_value:
            _print_error_message(
                method_name, try_name, expected_value, actual_value)

    def try_good_arg_false():
        try_name = 'layer_name_false'
        _clear_all()
        _set_test_layer()
        false_layer_name = 'nonexistent layer'
        actual_value = l.Layer.layer_name_is_in_use(false_layer_name)
        expected_value = False
        if not actual_value == expected_value:
            _print_error_message(
                method_name, try_name, expected_value, actual_value)

    def try_good_arg_true():
        try_name = 'good_arg_true'
        _clear_all()
        _set_test_layer()
        good_arg_true = layer_name
        actual_value = l.Layer.layer_name_is_in_use(good_arg_true)
        expected_value = True
        if not actual_value == expected_value:
            _print_error_message(
                method_name, try_name, expected_value, actual_value)

    try_bad_type_layer_name()
    try_good_arg_false()
    try_good_arg_true()

def test__color_name_is_known():
    method_name = '_color_name_is_known'

    def try_bad_type_color_name():
        try_name = 'bad_type_color_name'
        _clear_all()
        bad_type_color_name = 37
        actual_value = l.Layer._color_name_is_known(bad_type_color_name)
        expected_value = False
        if not actual_value == expected_value:
            _print_error_message(
                method_name, try_name, expected_value, actual_value)

    def try_good_arg_false():
        try_name = 'good_arg_false'
        _clear_all()
        good_arg_false = 'chartreuse'
        actual_value = l.Layer._color_name_is_known(good_arg_false)
        expected_value = False
        if not actual_value == expected_value:
            _print_error_message(
                method_name, try_name, expected_value, actual_value)

    def try_good_arg_true():
        try_name = 'good_arg_true'
        _clear_all()
        good_arg_true = 'dark gray'
        actual_value = l.Layer._color_name_is_known(good_arg_true)
        expected_value = True
        if not actual_value == expected_value:
            _print_error_message(
                method_name, try_name, expected_value, actual_value)

    try_bad_type_color_name()
    try_good_arg_false()
    try_good_arg_true()

def test__layer_name_list_exists():
    method_name = '_layer_name_list_name_exists'

    def try_good_state_false():
        try_name = 'try_good_state_false'
        _clear_all()
        actual_value = l.Layer._layer_name_list_name_exists()
        expected_value = False
        if not actual_value == expected_value:
            _print_error_message(
                method_name, try_name, expected_value, actual_value)

    def try_good_state_true():
        try_name = 'good_state_true'
        _clear_all()
        _set_test_layer()
        actual_value = l.Layer._layer_name_list_name_exists()
        expected_value = True
        if not actual_value == expected_value:
            _print_error_message(
                method_name, try_name, expected_value, actual_value)

    try_good_state_false()
    try_good_state_true()

def test__layer_name_list_contains_name():
    method_name = '_layer_name_list_contains_name'
    def try_bad_type_layer_name():
        try_name = 'bad_type_layer_name'
        _clear_all()
        bad_type_layer_name = 37
        actual_value = l.Layer._layer_name_list_contains_name(
            bad_type_layer_name)
        expected_value = False
        if not actual_value == expected_value:
            _print_error_message(
                method_name, try_name, expected_value, actual_value)

    def try_good_arg_nonexistent_list_name():
        try_name = 'good_arg_nonexistent_list_name'
        _clear_all()
        actual_value = l.Layer._layer_name_list_contains_name(layer_name)
        expected_value = False
        if not actual_value == expected_value:
            _print_error_message(
                method_name, try_name, expected_value, actual_value)

    def try_good_arg_false():
        try_name = 'good_arg_false'
        _clear_all()
        _set_test_layer()
        false_layer_name = 'kilroy'
        actual_value = l.Layer._layer_name_list_contains_name(
            false_layer_name)
        expected_value = False
        if not actual_value == expected_value:
            _print_error_message(
                method_name, try_name, expected_value, actual_value)

    def try_good_arg_true():
        try_name = 'good_arg_true'
        _clear_all()
        _set_test_layer()
        true_layer_name = layer_name
        actual_value = l.Layer._layer_name_list_contains_name(true_layer_name)
        expected_value = True
        if not actual_value == expected_value:
            _print_error_message(
                method_name, try_name, expected_value, actual_value)

    try_bad_type_layer_name()
    try_good_arg_nonexistent_list_name()
    try_good_arg_false()
    try_good_arg_true()

def test_new():
    method_name = 'new'

    def try_bad_type_layer_name():
        try_name = 'bad_type_layer_name'
        _clear_all()
        _set_test_layer()
        bad_type_layer_name = 37
        actual_value = l.Layer.new(bad_type_layer_name)
        expected_value = None
        if not actual_value == expected_value:
            _print_error_message(
                method_name, try_name, expected_value, actual_value)

    def try_bad_type_color_name():
        try_name = 'bad_type_color_name'
        _clear_all()
        _set_test_layer()
        bad_type_color_name = 37
        actual_value = l.Layer.new(good_layer_name, bad_type_color_name)
        expected_value = None
        if not actual_value == expected_value:
            _print_error_message(
                method_name, try_name, expected_value, actual_value)

    def try_bad_value_layer_name():
        try_name = 'bad_value_layer_name'
        _clear_all()
        _set_test_layer()
        bad_value_layer_name = layer_name
        actual_value = l.Layer.new(bad_value_layer_name)
        expected_value = None
        if not actual_value == expected_value:
            _print_error_message(
                method_name, try_name, expected_value, actual_value)

    def try_bad_value_color_name():
        try_name = 'bad_value_color_name'
        _clear_all()
        _set_test_layer()
        bad_value_color_name = 'pink'
        actual_value = l.Layer.new(good_layer_name, bad_value_color_name)
        expected_value = None
        if not actual_value == expected_value:
            _print_error_message(
                method_name, try_name, expected_value, actual_value)

    def try_good_args():
        try_name = 'good_args'
        _clear_all()
        _set_test_layer()
        good_color_name = 'dark gray'
        actual_value = l.Layer.new(good_layer_name, good_color_name)
        expected_value = good_layer_name
        if not actual_value == expected_value:
            _print_error_message(
                method_name, try_name, expected_value, actual_value)

    try_bad_type_layer_name()
    try_bad_type_color_name()
    try_bad_value_layer_name()
    try_bad_value_color_name()
    try_good_args()

def test_delete():
    method_name = 'delete'

    def try_bad_type_layer_name():
        try_name = 'bad_type_layer_name'
        _clear_all()
        _set_test_layer()
        bad_type_layer_name = 37
        actual_value = l.Layer.delete(bad_type_layer_name)
        expected_value = False
        if not actual_value == expected_value:
            _print_error_message(
                method_name, try_name, expected_value, actual_value)

    def try_bad_value_layer_name():
        try_name = 'bad_value_layer_name'
        _clear_all()
        _set_test_layer()
        bad_value_layer_name = 'kilroy'
        actual_value = l.Layer.delete(bad_value_layer_name)
        expected_value = False
        if not actual_value == expected_value:
            _print_error_message(
                method_name, try_name, expected_value, actual_value)

    def try_good_arg():
        _clear_all()
        _set_test_layer()
        try_name = 'good_arg'
        good_arg = layer_name
        actual_value = l.Layer.delete(layer_name)
        expected_value = True
        if not actual_value == expected_value:
            _print_error_message(
                method_name, try_name, expected_value, actual_value)

    try_bad_type_layer_name()
    try_bad_value_layer_name()
    try_good_arg()

def test__add_layer_name():
    method_name = '_add_layer_name'

    def try_bad_type_layer_name():
        _clear_all()
        _set_test_layer()
        try_name = 'bad_type_layer_name'
        bad_type_layer_name = 37
        actual_value = l.Layer._add_layer_name(bad_type_layer_name)
        expected_value = None
        if not actual_value == expected_value:
            _print_error_message(
                method_name, try_name, expected_value, actual_value)

    def try_bad_value_layer_name():
        try_name = 'bad_value_layer_name'
        _clear_all()
        _set_test_layer()
        bad_value_layer_name = layer_name
        actual_value = l.Layer._add_layer_name(bad_value_layer_name)
        expected_value = None
        if not actual_value == expected_value:
            _print_error_message(
                method_name, try_name, expected_value, actual_value)

    def try_good_arg():
        try_name = 'good_arg'
        _clear_all()
        _set_test_layer()
        good_arg = 'new name'
        actual_value = l.Layer._add_layer_name(good_arg)
        expected_value = good_arg
        if not actual_value == expected_value:
            _print_error_message(
                method_name, try_name, expected_value, actual_value)
        
    try_bad_type_layer_name()
    try_bad_value_layer_name()
    try_good_arg()

def test__delete_layer_name():
    method_name = '_delete_layer_name'

    def try_bad_type_layer_name():
        try_name = 'bad_type_layer_name'
        _clear_all()
        _set_test_layer()
        bad_type_layer_name = 37
        actual_value = l.Layer._delete_layer_name(bad_type_layer_name)
        expected_value = False
        if not actual_value == expected_value:
            _print_error_message(
                method_name, try_name, expected_value, actual_value)

    def try_bad_value_layer_name():
        try_name = 'bad_value_layer_name'
        _clear_all()
        _set_test_layer()
        bad_value_layer_name = 'bad layer'
        actual_value = l.Layer._delete_layer_name(bad_value_layer_name)
        expected_value = False
        if not actual_value == expected_value:
            _print_error_message(
                method_name, try_name, expected_value, actual_value)

    def try_good_arg():
        try_name = 'good_arg'
        _clear_all()
        _set_test_layer()
        good_arg = layer_name
        actual_value = l.Layer._delete_layer_name(good_arg)
        expected_value = True
        if not actual_value == expected_value:
            _print_error_message(
                method_name, try_name, expected_value, actual_value)

    try_bad_type_layer_name()
    try_bad_value_layer_name()
    try_good_arg()

test_layer_name_is_in_use()
test__color_name_is_known()
test__layer_name_list_exists()
test__layer_name_list_contains_name()
test_new()
test_delete()
test__add_layer_name()
test__delete_layer_name()
