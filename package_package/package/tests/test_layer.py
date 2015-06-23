from package.view import grammar as g
from package.view import layer as l
import rhinoscriptsyntax as rs
from package.tests import utilities as u

def test_new():
    def try_good_args():
        try_name = 'good_args'
        g.Grammar.clear_all()
        name = 'gaudi'
        actual_value = l.Layer.new(name)
        expected_value = name
        if not actual_value == expected_value:
            u.Utilities.print_test_error_message(
                method_name, try_name, expected_value, actual_value)

    method_name = 'new'
    try_good_args()

def test_get_layer_name_from_user():
    def try_something():
        try_name = 'something'
        g.Grammar.clear_all()
        used_name = 'used_name'
        rs.AddLayer(used_name)
        good_name = 'good_name'
        print("Enter: 1, '%s'; 2, '%s'; 3, '%s'" % (
            'kil#roy', used_name, good_name))
        actual_value = l.Layer.get_layer_name_from_user()
        expected_value = good_name
        if not actual_value == expected_value:
            u.Utilities.print_test_error_message(
                method_name, try_name, expected_value, actual_value)

    method_name = 'get_layer_name_from_user'
    try_something()

def test__is_well_formed():
    def try_ill_formed():
        try_name = 'ill_formed'
        g.Grammar.clear_all()
        ill_formed_name = 'kil#roy'
        actual_value = l.Layer._is_well_formed(ill_formed_name)
        expected_value = False
        if not actual_value == expected_value:
            u.Utilities.print_test_error_message(
                method_name, try_name, expected_value, actual_value)

    def try_well_formed():
        try_name = 'well_formed'
        g.Grammar.clear_all()
        well_formed_name = 'good_name'
        actual_value = l.Layer._is_well_formed(well_formed_name)
        expected_value = True
        if not actual_value == expected_value:
            u.Utilities.print_test_error_message(
                method_name, try_name, expected_value, actual_value)

    method_name = '_is_well_formed'
    try_ill_formed()
    try_well_formed()

def test__is_available():
    def try_used_name():
        try_name = 'used_name'
        used_name = 'used_name'
        g.Grammar.clear_all()
        rs.AddLayer(used_name)
        actual_value = l.Layer._is_available(used_name)
        expected_value = False
        if not actual_value == expected_value:
            u.Utilities.print_test_error_message(
                method_name, try_name, expected_value, actual_value)

    def try_unused_name():
        try_name = 'unused_name'
        unused_name = 'unused_name'
        g.Grammar.clear_all()
        actual_value = l.Layer._is_available(unused_name)
        expected_value = True
        if not actual_value == expected_value:
            u.Utilities.print_test_error_message(
                method_name, try_name, expected_value, actual_value)

    method_name = '_is_available'
    try_used_name()
    try_unused_name()

def test_new_1_frame_block():
    def try_good_args():
        try_name = 'good_args'
        g.Grammar.clear_all()
        name = 'gaudi'
        origin = (10, 10, 0)
        actual_value = l.Layer.new_1_frame_block(name, origin)
        expected_value = name
        if not actual_value == expected_value:
            u.Utilities.print_test_error_message(
                method_name, try_name, expected_value, actual_value)

    method_name = 'new_1_frame_block'
    try_good_args()

def test_new_2_frame_blocks():
    try_good_args()

# test_new()
test_get_layer_name_from_user()
test__is_well_formed()
test__is_available()

# test_new_1_frame_block()
# test_new_2_frame_blocks()