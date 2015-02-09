from package.model import frame_block as fb
from package.model import grammar as g
from package.model import initial_shape as ish
from package.model import llist as ll
import rhinoscriptsyntax as rs

position = [5, 5, 0]                            ##  check that all are used
existing_shape_name = 'existing_shape'
new_shape_name = 'new_shape'
bad_type_shape_name = 37
bad_value_name = existing_shape_name
good_arg_false_hash = 'kil#roy'
good_arg_false_space = 'kil roy'
good_arg_true_int = 37
good_arg_true_string = 'kilroy'
initial_shape_name = 'initial_shape'
first_initial_shape_name = ish.InitialShape.first_initial_shape_name

# def test__shape_name_is_available():
#     pass

# def test__shape_name_is_well_formed():
    # method_name = '_shape_name_is_well_formed'

    # def try_good_arg_false_space():
    #     try_name = 'good_arg_false_space'
    #     g.Grammar.clear_all()
    #     actual_value = g.Grammar._shape_name_is_well_formed(
    #         good_arg_false_space)
    #     expected_value = False
    #     if not actual_value == expected_value:
    #         g.Grammar.print_test_error_message(
    #             method_name, try_name, expected_value, actual_value)

    # def try_good_arg_false_hash():
    #     try_name = 'good_arg_false_hash'
    #     g.Grammar.clear_all()
    #     fb.FrameBlock.new()
    #     sl.ShapeLayer.new(existing_shape_name, position)
    #     actual_value = g.Grammar._shape_name_is_well_formed(
    #         good_arg_false_hash)
    #     expected_value = False
    #     if not actual_value == expected_value:
    #         g.Grammar.print_test_error_message(
    #             method_name, try_name, expected_value, actual_value)

    # def try_good_arg_true_int():
    #     try_name = 'good_arg_true_int'
    #     g.Grammar.clear_all()
    #     actual_value = g.Grammar._shape_name_is_well_formed(
    #         good_arg_true_int)
    #     expected_value = True
    #     if not actual_value == expected_value:
    #         g.Grammar.print_test_error_message(
    #             method_name, try_name, expected_value, actual_value)

    # def try_good_arg_true_string():
    #     try_name = 'good_arg_true_string'
    #     g.Grammar.clear_all()
    #     actual_value = g.Grammar._shape_name_is_well_formed(
    #         good_arg_true_string)
    #     expected_value = True
    #     if not actual_value == expected_value:
    #         g.Grammar.print_test_error_message(
    #             method_name, try_name, expected_value, actual_value)

    # try_good_arg_false_space()
    # try_good_arg_false_hash()
    # try_good_arg_true_int()
    # try_good_arg_true_string()

# def test__add_named_positioned_shape_frame():
    # """Arguments are tested by the calling methods; no need to test here
    # """
    # method_name = '_add_named_positioned_shape_frame'

    # def try_good_args():
    #     try_name = 'good_args'
    #     g.Grammar.clear_all()
    #     fb.FrameBlock.new()
    #     actual_value = g.Grammar._add_named_positioned_shape_frame(
    #         new_shape_name, position)
    #     expected_value = new_shape_name
    #     if not actual_value == expected_value:
    #         g.Grammar.print_test_error_message(
    #             method_name, try_name, expected_value, actual_value)
        
    # try_good_args()

def test__record_initial_shape():
    method_name = '_record_initial_shape'

    def try_good_state():
        try_name = 'good_state'
        g.Grammar.clear_all()
        actual_value = g.Grammar._record_initial_shape(
            first_initial_shape_name)
        expected_value = first_initial_shape_name
        if not actual_value == expected_value:
            g.Grammar.print_test_error_message(
                method_name, try_name, expected_value, actual_value)

    try_good_state()

def test__add_first_initial_shape():
    method_name = '_add_first_initial_shape'

    def try_good_state():
        try_name = 'good_state'
        g.Grammar.clear_all()
        fb.FrameBlock.new()
        actual_value = g.Grammar._add_first_initial_shape()
        expected_value = ish.InitialShape.first_initial_shape_name
        if not actual_value == expected_value:
            g.Grammar.print_test_error_message(
                method_name, try_name, actual_value, expected_value)

    try_good_state()

def test__add_first_rule():
    method_name = '_add_first_rule'

    def try_good_state():
        try_name = 'good_state'
        g.Grammar.clear_all()
        fb.FrameBlock.new()
        actual_value = g.Grammar._add_first_rule()
        expected_value = g.Grammar.rule_name_list_name
        if not actual_value == expected_value:
            g.Grammar.print_test_error_message(
                method_name, try_name, expected_value, actual_value)

    try_good_state()

def test_new():
    method_name = 'new'
    g.Grammar.clear_all()
    g.Grammar.new()

# def test__add_subsequent_initial_shape_frame():
#     method_name = '_add_subsequent_initial_shape_frame'

    # def try_good_state():
    #     try_name = 'good_state'
    #     g.Grammar.clear_all()
    #     fb.FrameBlock.new()
    #     actual_value = g.Grammar._add_subsequent_initial_shape_frame()
    #                                             ##  use 'new_shape'
    #     expected_value = new_shape_name
    #     if not actual_value == expected_value:
    #         g.Grammar.print_test_error_message(
    #             method_name, try_name, expected_value, actual_value)

    # try_good_state()

# def test_add_unnamed_initial_shape_frame():
#     method_name = 'add_unnamed_initial_shape_frame'

    # def try_good_state():
    #     try_name = 'good_state'
    #     g.Grammar.clear_all()
    #     fb.FrameBlock.new()
    #     g.Grammar._add_named_initial_shape_frame(existing_shape_name)
    #     g.Grammar.add_unnamed_initial_shape_frame()

    # try_good_state()

# def test__add_named_initial_shape_frame():
    # method_name = '_add_named_initial_shape_frame'

    # def try_bad_type():
    #     try_name = 'bad_type_shape_name'
    #     g.Grammar.clear_all()
    #     actual_value = g.Grammar._add_named_initial_shape_frame(
    #         bad_type_shape_name)
    #     expected_value = None
    #     if not actual_value == expected_value:
    #         g.Grammar.print_test_error_message(
    #             method_name, try_name, expected_value, actual_value)

    # def try_bad_value():
    #     try_name = 'bad_value_name'
    #     g.Grammar.clear_all()
    #     fb.FrameBlock.new()
    #     actual_value = g.Grammar._add_named_initial_shape_frame(
    #         bad_value_name)
    #     expected_value = None
    #     if not actual_value == expected_value:
    #         g.Grammar.print_test_error_message(
    #             method_name, try_name, expected_value, actual_value)

    # def try_good_args():
    #     try_name = 'good_args'
    #     g.Grammar.clear_all()
    #     fb.FrameBlock.new()
    #     actual_value = g.Grammar._add_named_initial_shape_frame(
    #         new_shape_name)
    #     expected_value = new_shape_name
    #     if not actual_value == expected_value:
    #         g.Grammar.print_test_error_message(
    #             method_name, try_name, expected_value, actual_value)

    # try_bad_type()
    # try_bad_value()
    # try_good_args()

### utility methods
# test__shape_name_is_available()
# test__shape_name_is_well_formed()

# test__record_initial_shape()

### class methods
# test_new()
# test__add_first_initial_shape()
test__add_first_rule()

# test__add_named_positioned_shape_frame()
# test__add_subsequent_initial_shape_frame()
# test_add_unnamed_initial_shape_frame()
# test__add_named_initial_shape_frame()
