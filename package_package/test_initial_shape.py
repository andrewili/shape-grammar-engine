from package.view import frame_block as fb
from package.view import grammar as g
from package.view import initial_shape as ish
from package.view import labeled_point as lp
import rhinoscriptsyntax as rs

existing_name = 'existing_shape'
name = 'initial_shape'
position = (0, 0, 0)
bad_type_name = 37
bad_type_position = 37
bad_value_name = existing_name
bad_value_position = (0, 0, 5)

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

def test_export_unspecified():
    method_name = 'export_unspecified'

    def try_labeled_shape_text_dot():
        try_name = 'labeled_shape_text_dot'
        g.Grammar.clear_all()
        fb.FrameBlock.new()
        _draw_labeled_x_text_dot()
        ish.InitialShape.export_unspecified()

    def try_labeled_shape_text_object():
        try_name = 'labeled_shape_text_object'
        g.Grammar.clear_all()
        fb.FrameBlock.new()
        _draw_labeled_x_text_object()
        ish.InitialShape.export_unspecified()

    def try_labeled_shape_text_dot_and_object():
        try_name = 'labeled_shape_text_dot_and_object'
        g.Grammar.clear_all()
        fb.FrameBlock.new()
        _draw_labeled_x_text_object_text_dot()
        ish.InitialShape.export_unspecified()

    def _draw_labeled_x_text_dot():
        _draw_x()
        _draw_text_dot()

    def _draw_labeled_x_text_object():
        _draw_x()
        _draw_text_object()

    def _draw_labeled_x_text_object_text_dot():
        _draw_x()
        _draw_text_object()
        _draw_text_dot()

    def _draw_x():
        p00 = (0, 0, 0)
        p02 = (0, 32, 0)
        p20 = (32, 0, 0)
        p22 = (32, 32, 0)
        point_pairs = [(p00, p22), (p02, p20)]
        for pair in point_pairs:
            rs.AddLine(pair[0], pair[1])
            
    def _draw_text_dot():
        p11 = (16, 16, 0)
        lpoints = [('d', p11)]
        text_height = 2
        for lpoint in lpoints:
            label = lpoint[0]
            point = lpoint[1]
            rs.AddTextDot(label, point)

    def _draw_text_object():
        p00 = (0, 0, 0)
        lpoints = [('o', p00)]
        text_height = 2
        for lpoint in lpoints:
            rs.AddText(lpoint[0], lpoint[1], text_height)

    try_labeled_shape_text_dot()
    try_labeled_shape_text_object()
    try_labeled_shape_text_dot_and_object()

def test_export_specified():
    method_name = 'export_specified'
    ish.InitialShape.export_specified()

# test_add_first()
# test_add_subsequent()
# test__record()

test_export_unspecified()
##  test_export_specified()
# _draw_initial_shape()

