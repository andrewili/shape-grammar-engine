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

def test_get_is_text():
    method_name = 'get_is_text'

    def try_good_state_empty():                 ##  02-14 18:37 3
        pass

    def try_good_state_non_maximal():           ##  02-14 18:37 2
        pass

    def try_good_state_maximal():               ##  02-14 18:37 1
        

    try_good_state_empty()
    try_good_state_non_maximal()
    try_good_state_maximal()


def test__add_tag():
    method_name = '_add_tag'

    def try_good_state():
        try_name = 'good_state'
        g.Grammar.clear_all()
        actual_value = sl.ShapeLayer._add_tag(new_shape_name, tag_position)
        expected_value = 'guid'
        if not actual_value == expected_value:
            g.Grammar.print_test_error_message(
                method_name, try_name, expected_value, actual_value)

    try_good_state()

def test_record_name():
    pass

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

test_get_is_text()
# test__add_tag()
# test_record_name()
test_new()
