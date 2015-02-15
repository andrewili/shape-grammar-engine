from package.view import frame_block as fb
from package.view import grammar as g
from package.view import initial_shape as ish

existing_name = 'existing_shape'
name = 'initial_shape'
position = [0, 0, 0]
bad_type_name = 37
bad_type_position = 37
bad_value_name = existing_name
bad_value_position = [0, 0, 5]

def test__record():
    method_name = '_record'

    def try_bad_type():
        try_name = 'bad_type'
        actual_value = ish.InitialShape._record(bad_type_name)
        expected_value = None
        if not actual_value == expected_value:
            g.Grammar.print_test_error_message(
                method_name, try_name, expected_value, actual_value)

    def try_good_state():
        try_name = 'good_state'
        g.Grammar.clear_all()
        actual_value = ish.InitialShape._record(name)
        expected_value = name
        if not actual_value == expected_value:
            g.Grammar.print_test_error_message(
                method_name, try_name, expected_value, actual_value)

    try_bad_type()
    try_good_state()

def test_add_first():
    method_name = 'add_first'

    def try_bad_state_first_initial_shape_exists():
        try_name = 'bad_state_first_initial_shape_exists'
        g.Grammar.clear_all()
        fb.FrameBlock.new()
        ish.InitialShape._record(ish.InitialShape.first_initial_shape_name)
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
        
    try_bad_state_first_initial_shape_exists()
    try_good_state()

def test_add_subsequent():
    method_name = 'add_subsequent'
    
    def try_good_state():
        try_name = 'good_state'
        g.Grammar.clear_all()
        fb.FrameBlock.new()
        ish.InitialShape.add_first()
        actual_value = ish.InitialShape.add_subsequent()
        expected_value = 'subsequent_initial_shape'
        if not actual_value == expected_value:
            g.Grammar.print_test_error_message(
                method_name, try_name, expected_value, actual_value)

    try_good_state()

test__record()
test_add_first()
test_add_subsequent()

