from package.view import arrow as a
from package.view import grammar as g
import rhinoscriptsyntax as rs
from package.view import settings as s
from package.tests import utilities as u

def test_new_instance():                        ##  done 08-06
    def try_good_state_no_definition():
        try_name = 'good_state_no_definition'
        g.Grammar.clear_all()
        position = (10, 10, 0)
        layer_name = s.Settings.default_layer_name
        guid = a.Arrow.new_instance(layer_name, position)
        actual_value = rs.ObjectLayer(guid)
        expected_value = layer_name
        if not actual_value == expected_value:
            u.Utilities.print_test_error_message(
                method_name, try_name, expected_value, actual_value)

    def try_good_state_yes_definition():
        try_name = 'good_state_yes_definition'
        g.Grammar.clear_all()
        a.Arrow._new_definition()
        position = (20, 20, 0)
        layer_name = s.Settings.arrow_name
        guid = a.Arrow.new_instance(layer_name, position)
        actual_value = rs.ObjectLayer(guid)
        expected_value = layer_name
        if not actual_value == expected_value:
            u.Utilities.print_test_error_message(
                method_name, try_name, expected_value, actual_value)

    method_name = 'new_instance'
    try_good_state_no_definition()
    try_good_state_yes_definition()

def test__new_definition():
    method_name = '_new_definition'
    g.Grammar.clear_all()
    actual_value = a.Arrow._new_definition()

# test_new_instance()                             ##  done 08-06
# test__new_definition()                          ##  done / manual test

