from package.model import frame_block as fb
from package.model import grammar as g
from package.model import layer as l
from package.model import shape_layer as sl

def test_new():
    method_name = 'new'
    existing_shape_name = 'existing shape'
    position = [0, 0, 0]
    bad_type_shape_name = 37
    bad_type_position = 29
    bad_value_shape_name = existing_shape_name
    bad_value_position = [1, 1, 5]
    new_shape_name = 'new shape'

    def try_bad_type_shape_name():
        try_name = 'bad_type_shape_name'
        g.Grammar.clear_all()
        actual_value = sl.ShapeLayer.new(bad_type_shape_name, position)
        expected_value = None
        if not actual_value == expected_value:
            g.Grammar.print_test_error_message(
                method_name, try_name, expected_value, actual_value)

    def try_bad_type_position():
        try_name = 'bad_type_position'
        g.Grammar.clear_all()
        actual_value = sl.ShapeLayer.new(
            existing_shape_name, bad_type_position)
        expected_value = None
        if not actual_value == expected_value:
            g.Grammar.print_test_error_message(
                method_name, try_name, expected_value, actual_value)

    def try_bad_value_shape_name():
        try_name = 'bad_value_shape_name'
        g.Grammar.clear_all()
        l.Layer.new(existing_shape_name)
        actual_value = sl.ShapeLayer.new(bad_value_shape_name, position)
        expected_value = None
        if not actual_value == expected_value:
            g.Grammar.print_test_error_message(
                method_name, try_name, expected_value, actual_value)

    def try_bad_value_position():
        try_name = 'bad_value_position'
        g.Grammar.clear_all()
        l.Layer.new(existing_shape_name)
        actual_value = sl.ShapeLayer.new(new_shape_name, bad_value_position)
        expected_value = None
        if not actual_value == expected_value:
            g.Grammar.print_test_error_message(
                method_name, try_name, expected_value, actual_value)

    def try_good_args():
        try_name = 'good_args'
        g.Grammar.clear_all()
        fb.FrameBlock.new()
        actual_value = sl.ShapeLayer.new(new_shape_name, position)
        expected_value = new_shape_name
        if not actual_value == expected_value:
            g.Grammar.print_test_error_message(
                method_name, try_name, expected_value, actual_value)

    try_bad_type_shape_name()
    try_bad_type_position()
    try_bad_value_shape_name()
    try_bad_value_position()
    try_good_args()

test_new()
