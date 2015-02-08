from package.model import frame_block as fb
from package.model import grammar as g
from package.model import initial_shape as ish
from package.model import shape_layer as sl
import rhinoscriptsyntax as rs

existing_name = 'existing_shape'
name = 'initial_shape'
position = [0, 0, 0]
bad_type_name = 37
bad_type_position = 37
bad_value_name = existing_name
bad_value_position = [0, 0, 5]

def test__first_initial_shape_name_exists():
    method_name = '_first_initial_shape_name_exists'

    def try_false():
        try_name = 'false'
        g.Grammar.clear_all()
        fb.FrameBlock.new()
        actual_value = ish.InitialShape._first_initial_shape_name_exists()
        expected_value = False
        if not actual_value == expected_value:
            g.Grammar.print_test_error_message(
                method_name, try_name, expected_value, actual_value)

    def try_true():
        try_name = 'true'
        g.Grammar.clear_all()
        fb.FrameBlock.new()
        sl.ShapeLayer._record_name(ish.InitialShape.first_initial_shape_name)
        actual_value = ish.InitialShape._first_initial_shape_name_exists()
        expected_value = True
        if not actual_value == expected_value:
            g.Grammar.print_test_error_message(
                method_name, try_name, expected_value, actual_value)

    try_false()
    try_true()

def test_add_first():
    method_name = 'add_first'

    def try_bad_state():
        try_name = 'bad state'
        g.Grammar.clear_all()
        fb.FrameBlock.new()
        sl.ShapeLayer._record_name(ish.InitialShape.first_initial_shape_name)
        actual_value = ish.InitialShape.add_first()
        expected_value = None
        if not actual_value == expected_value:
            g.Grammar.print_test_error_message(
                method_name, try_name, expected_value, actual_value)

    def try_good_state():
        try_name = 'good_state'
        g.Grammar.clear_all()
        fb.FrameBlock.new()
        actual_value = ish.InitialShape.add_first()
        expected_value = ish.InitialShape.first_initial_shape_name
        if not actual_value == expected_value:
            g.Grammar.print_test_error_message(
                method_name, try_name, expected_value, actual_value)
        
    try_bad_state()
    try_good_state()

def test_add_subsequent():
    method_name = 'add_subsequent'
    
    def try_good_state():
        try_name = 'good_state'
        g.Grammar.clear_all()
        fb.FrameBlock.new()
        actual_value = ish.InitialShape.add_subsequent()
        expected_value = 'subsequent_initial_shape'
        if not actual_value == expected_value:
            g.Grammar.print_test_error_message(
                method_name, try_name, expected_value, actual_value)

    try_good_state()

test__first_initial_shape_name_exists()
test_add_first()
test_add_subsequent()
