from package.view import frame as f
from package.view import grammar as g
from package.view import layer as l
from package.view import llist as ll
import rhinoscriptsyntax as rs
from package.view import settings as s
from package.tests import utilities as u

origin = [0, 0, 0]
bad_type_point = 37
bad_value_point = [0, 0, 5]
point = [0, 0, 0]

def test_new_instance():                        ##  done 08-06
    def try_good_state_no_block_definition():
        try_name = 'good_state_no_block_definition'
        g.Grammar.clear_all()
        (   layer_name,
            position
        ) = (
            'gaudi',
            (20, 20, 0))
        rs.AddLayer(layer_name)
        guid_out = f.Frame.new_instance(layer_name, position)
        actual_value = rs.ObjectLayer(guid_out)
        expected_value = layer_name
        if not actual_value == expected_value:
            u.Utilities.print_test_error_message(
                method_name, try_name, expected_value, actual_value)

    def try_good_state_has_block_definition():
        try_name = 'good_state_has_block_definition'
        g.Grammar.clear_all()
        (   layer_name, 
            position
        ) = (
            'gaudi', 
            (10, 10, 0))
        rs.AddLayer(layer_name)
        rs.CurrentLayer(layer_name)
        guid_out = f.Frame.new_instance(layer_name, position)
        actual_value = rs.ObjectLayer(guid_out)
        expected_value = layer_name
        if not actual_value:
            g.Grammar.print_test_error_message(
                method_name, try_name, expected_value, actual_value)

    method_name = 'new_instance'
    try_good_state_no_block_definition()
    try_good_state_has_block_definition()

def test__new_definition():                     ##  done 08-05
    def try_good_state():
        try_name = 'good_state'
        g.Grammar.clear_all()
        actual_value = f.Frame._new_definition()
        expected_value = s.Settings.frame_name
        if not actual_value == expected_value:
            u.Utilities.print_test_error_message(
                method_name, try_name, expected_value, actual_value)

    method_name = '_new_definition'
    try_good_state()

def test__get_guids():                          ##  done 08-06
    g.Grammar.clear_all()
    position = (0, 0, 0)
    guids = f.Frame._get_guids()
    rs.SelectObjects(guids)

def test_get_frame_position_from_user():        ##  done 08-06
    def try_something():
        try_name = 'something'
        g.Grammar.clear_all()
        good_point = (20, 20, 0)
        print("Enter %s" % str(good_point))
        x, y, z = f.Frame.get_frame_position_from_user()
        actual_value = (x, y, z)
        expected_value = good_point
        if not actual_value == expected_value:
            u.Utilities.print_test_error_message(
                method_name, try_name, expected_value, actual_value)

    method_name = 'get_frame_position_from_user'
    try_something()

test_new_instance()                             ##  done 08-06
# test__definition_exists()                       ##  trivial
# test__new_definition()                          ##  done 08-05
# test__get_guids()                               ##  done 08-06 / manual test
# test_get_instance_position()                    ##  trivial
# test_get_frame_position_from_user()             ##  done 08-06 / manual test

