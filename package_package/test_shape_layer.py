from package.model import frame_block as fb
from package.model import grammar as g
from package.model import llist as ll
from package.model import shape_layer as sl

existing_shape_name = 'existing_shape'
new_shape_name = 'new_shape'
position = [0, 0, 0]

bad_type_shape_name = 37
good_arg_false_hash = 'kil#roy'
good_arg_false_space = 'kil roy'
good_arg_true_string = 'kilroy'

def test__shape_layer_list_name_exists():
    method_name = '_shape_layer_list_name_exists'

    def try_false():
        try_name = 'false'
        g.Grammar.clear_all()
        actual_value = sl.ShapeLayer._shape_layer_list_name_exists()
        expected_value = False
        if not actual_value == expected_value:
            g.Grammar.print_test_error_message(
                method_name, try_name, expected_value, actual_value)

    def try_true():
        try_name = 'true'
        g.Grammar.clear_all()
        ll.Llist.set_entry(
            sl.ShapeLayer.shape_layer_list_name, existing_shape_name)
        actual_value = sl.ShapeLayer._shape_layer_list_name_exists()
        expected_value = True
        if not actual_value == expected_value:
            g.Grammar.print_test_error_message(
                method_name, try_name, expected_value, actual_value)

    try_false()
    try_true()

def test_shape_name_is_listed():
    pass
    # try_name = 

def test__shape_name_is_available():
    method_name = '_shape_name_is_available'

    def try_good_state_false():
        try_name = 'good_state_false'
        g.Grammar.clear_all()
        ll.Llist.set_entry(
            sl.ShapeLayer.shape_layer_list_name, existing_shape_name)
        actual_value = sl.ShapeLayer._shape_name_is_available(
            existing_shape_name)
        expected_value = False
        if not actual_value == expected_value:
            g.Grammar.print_test_error_message(
                method_name, try_name, expected_value, actual_value)

    def try_good_state_true():
        try_name = 'good_state_true'
        g.Grammar.clear_all()
        ll.Llist.set_entry(
            sl.ShapeLayer.shape_layer_list_name, new_shape_name)
        actual_value = sl.ShapeLayer._shape_name_is_available(new_shape_name)
        expected_value = False
        if not actual_value == expected_value:
            g.Grammar.print_test_error_message(
                method_name, try_name, expected_value, actual_value)

    try_good_state_false()
    try_good_state_true()

def test__shape_name_is_well_formed():
    method_name = '_shape_name_is_well_formed'

    def try_bad_type_shape_name():
        try_name = 'bad_type_shape_name'
        g.Grammar.clear_all()
        actual_value = sl.ShapeLayer._shape_name_is_well_formed(
            bad_type_shape_name)
        expected_value = False
        if not actual_value == expected_value:
            g.Grammar.print_test_error_message(
                method_name, try_name, expected_value, actual_value)

    def try_good_arg_false_space():
        try_name = 'good_arg_false_space'
        g.Grammar.clear_all()
        actual_value = sl.ShapeLayer._shape_name_is_well_formed(
            good_arg_false_space)
        expected_value = False
        if not actual_value == expected_value:
            g.Grammar.print_test_error_message(
                method_name, try_name, expected_value, actual_value)

    def try_good_arg_false_hash():
        try_name = 'good_arg_false_hash'
        g.Grammar.clear_all()
        fb.FrameBlock.new()
        sl.ShapeLayer.new(existing_shape_name, position)
        actual_value = sl.ShapeLayer._shape_name_is_well_formed(
            good_arg_false_hash)
        expected_value = False
        if not actual_value == expected_value:
            g.Grammar.print_test_error_message(
                method_name, try_name, expected_value, actual_value)

    def try_good_arg_true_string():
        try_name = 'good_arg_true_string'
        g.Grammar.clear_all()
        actual_value = sl.ShapeLayer._shape_name_is_well_formed(
            good_arg_true_string)
        expected_value = True
        if not actual_value == expected_value:
            g.Grammar.print_test_error_message(
                method_name, try_name, expected_value, actual_value)

    try_bad_type_shape_name()
    try_good_arg_false_space()
    try_good_arg_false_hash()
    try_good_arg_true_string()

def test_get_shape_name_from_user():
    method_name = 'get_shape_name_from_user'

    def try_good_state():
        try_name = 'good_state'
        g.Grammar.clear_all()
        ll.Llist.set_entry(
            sl.ShapeLayer.shape_layer_list_name, existing_shape_name)
        sl.ShapeLayer.get_shape_name_from_user()

    try_good_state()

def test_new():
    method_name = 'new'
    position = [0, 0, 0]
    new_shape_name = 'new shape'

    def try_good_args():
        try_name = 'good_args'
        g.Grammar.clear_all()
        fb.FrameBlock.new()
        actual_value = sl.ShapeLayer.new(new_shape_name, position)
        expected_value = new_shape_name
        if not actual_value == expected_value:
            g.Grammar.print_test_error_message(
                method_name, try_name, expected_value, actual_value)

    try_good_args()

test__shape_layer_list_name_exists()
test_shape_name_is_listed()
test__shape_name_is_available()
test__shape_name_is_well_formed()
test_get_shape_name_from_user()
test_new()
