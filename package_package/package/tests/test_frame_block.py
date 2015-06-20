from package.view import frame as f
from package.view import frame_block as fb
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

def test_new():
    def try_bad_state_block_exists():
        try_name = 'bad_state_block_exists'
        g.Grammar.clear_all()
        _set_frame_block()
        actual_value = fb.FrameBlock.new()
        expected_value = None
        if not actual_value == expected_value:
            u.Utilities.print_test_error_message(
                method_name, try_name, expected_value, actual_value)

    def try_good_state():
        try_name = 'good_state'
        g.Grammar.clear_all()
        frame_block_name = fb.FrameBlock.block_name
        actual_value = fb.FrameBlock.new()
        expected_value = frame_block_name
        if not actual_value == expected_value:
            u.Utilities.print_test_error_message(
                method_name, try_name, expected_value, actual_value)

    method_name = 'new'
    try_bad_state_block_exists()
    try_good_state()

def test_insert():
    def try_bad_value_existing_lshape_name():
        try_name = 'bad_value_existing_lshape_name'
        bad_value_shape_name = s.Settings.first_initial_shape_name
        position = rs.PointAdd(
            s.Settings.first_initial_shape_origin, (0, -40, 0))
        layer_name = s.Settings.first_initial_shape_name
        actual_value = fb.FrameBlock.insert(
            bad_value_shape_name, position, layer_name)
        expected_value = None
        if not actual_value == expected_value:
            u.Utilities.print_test_error_message(
                method_name, try_name, expected_value, actual_value)

    def try_bad_value_position():
        try_name = 'bad_value_point'
        g.Grammar.clear_all()
        fb.FrameBlock.new()
        rs.CurrentLayer('Default')
        actual_value = fb.FrameBlock.insert(bad_value_point)
        expected_value = None
        if not actual_value == expected_value:
            g.Grammar.print_test_error_message(
                method_name, try_name, expected_value, actual_value)

    def try_good_args():
        try_name = 'good_args'
        g.Grammar.clear_all()
        fb.FrameBlock.new()
        rs.CurrentLayer('Default')
        position = rs.GetPoint("Click somewhere")
        actual_value = fb.FrameBlock.insert(position)
        expected_value = 'guid'
        if not actual_value:
            g.Grammar.print_test_error_message(
                method_name, try_name, expected_value, actual_value)

    method_name = 'insert'
    try_bad_value_existing_lshape_name()
    # try_bad_value_position()
    # try_bad_value_layer_name()
    # try_good_state_no_definition()
    # try_good_args()

def test__definition_exists():
    def try_no_definition():
        try_name = 'no_definition'
        g.Grammar.clear_all()
        actual_value = fb.FrameBlock._definition_exists()
        expected_value = False
        if not actual_value == expected_value:
            u.Utilities.print_test_error_message(
                method_name, try_name, expected_value, actual_value)

    def try_definition():
        try_name = 'definition'
        g.Grammar.clear_all()
        fb.FrameBlock.new()
        actual_value = fb.FrameBlock._definition_exists()
        expected_value = True
        if not actual_value == expected_value:
            u.Utilities.print_test_error_message(
                method_name, try_name, expected_value, actual_value)
        
    method_name = '_definition_exists'
    try_no_definition()
    try_definition()

def _set_frame_block():
    _add_layer()
    _record_layer()
    _add_block()

def _add_layer():
    rs.AddLayer(fb.FrameBlock.layer_name)

def _record_layer():
    rs.SetDocumentData(
        l.Layer.layer_name_list_name, 
        fb.FrameBlock.layer_name, 
        ll.Llist.dummy_value)

def _add_block():
    rs.CurrentLayer(fb.FrameBlock.layer_name)
    frame_guids = f.Frame.new(origin)
    base_point = fb.FrameBlock.base_point
    block_name = fb.FrameBlock.block_name
    rs.AddBlock(frame_guids, base_point, block_name)
    rs.CurrentLayer('Default')

def test_delete():
    method_name = 'delete'

    def try_bad_state_no_block():
        try_name = 'bad_state_no_block'
        g.Grammar.clear_all()
        actual_value = fb.FrameBlock.delete()
        expected_value = False
        if not actual_value == expected_value:
            g.Grammar.print_test_error_message(
                method_name, try_name, expected_value, actual_value)

    def try_bad_state_no_layer():
        try_name = 'bad_state_no_layer'
        g.Grammar.clear_all()
        frame_guids = f.Frame.new(origin)
        base_point = fb.FrameBlock.base_point
        block_name = fb.FrameBlock.block_name
        rs.AddBlock(frame_guids, base_point, block_name)
        actual_value = fb.FrameBlock.delete()
        expected_value = False
        if not actual_value == expected_value:
            g.Grammar.print_test_error_message(
                method_name, try_name, expected_value, actual_value)

    def try_good_state():
        try_name = 'good_state'
        g.Grammar.clear_all()
        _set_frame_block()
        actual_value = fb.FrameBlock.delete()
        expected_value = True
        if not actual_value == expected_value:
            g.Grammar.print_test_error_message(
                method_name, try_name, expected_value, actual_value)

    try_bad_state_no_block()
    try_bad_state_no_layer()
    try_good_state()

# test_new()                                    ##  done
test_insert()                                 ##  kilroy is here
# test__definition_exists()                     ##  done
# test_delete()
