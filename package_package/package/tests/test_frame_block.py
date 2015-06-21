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

def test_insert():
    def try_good_state_no_block_definition():
        try_name = 'good_state_no_block_definition'
        g.Grammar.clear_all()
        layer_name = s.Settings.first_initial_shape_layer_name
        rs.AddLayer(layer_name)
        block_name = s.Settings.first_initial_shape_layer_name
        origin = (0, -50, 0)
        guid = fb.FrameBlock.insert_instance(block_name, layer_name, origin)
        actual_value = rs.ObjectLayer(guid)
        expected_value = layer_name
        if not actual_value == expected_value:
            u.Utilities.print_test_error_message(
                method_name, try_name, expected_value, actual_value)

    def try_bad_value_origin():
        try_name = 'bad_value_point'
        g.Grammar.clear_all()
        fb.FrameBlock.new()
        rs.CurrentLayer('Default')
        actual_value = fb.FrameBlock.insert_instance(bad_value_point)
        expected_value = None
        if not actual_value == expected_value:
            g.Grammar.print_test_error_message(
                method_name, try_name, expected_value, actual_value)

    def try_good_args():
        try_name = 'good_args'
        g.Grammar.clear_all()
        layer_name = 'gaudi'
        rs.AddLayer(layer_name)
        rs.CurrentLayer(layer_name)
        block_name = layer_name
        origin = (10, 10, 0)
        guid = fb.FrameBlock.insert_instance(block_name, layer_name, origin)
        actual_value = rs.ObjectLayer(guid)
        expected_value = layer_name
        if not actual_value:
            g.Grammar.print_test_error_message(
                method_name, try_name, expected_value, actual_value)

    method_name = 'insert_instance'
    try_good_state_no_block_definition()
    try_good_args()

def test__new_definition():
    def try_good_state():
        try_name = 'good_state'
        g.Grammar.clear_all()
        actual_value = fb.FrameBlock._new_definition()
        expected_value = s.Settings.frame_block_name
        if not actual_value == expected_value:
            u.Utilities.print_test_error_message(
                method_name, try_name, expected_value, actual_value)

    method_name = '_new_definition'
    try_good_state()

# def test_new():
    # def try_bad_state_definition_exists():
    #     try_name = 'bad_state_definition_exists'
    #     g.Grammar.clear_all()
    #     _set_frame_block()
    #     actual_value = fb.FrameBlock.new()
    #     expected_value = None
    #     if not actual_value == expected_value:
    #         u.Utilities.print_test_error_message(
    #             method_name, try_name, expected_value, actual_value)

    # def try_good_state():
    #     try_name = 'good_state'
    #     g.Grammar.clear_all()
    #     frame_block_name = s.Settings.frame_block_name
    #     actual_value = fb.FrameBlock.new()
    #     expected_value = frame_block_name
    #     if not actual_value == expected_value:
    #         u.Utilities.print_test_error_message(
    #             method_name, try_name, expected_value, actual_value)

    # method_name = 'new'
    # try_bad_state_definition_exists()
    # try_good_state()

# def test__definition_exists():
    # def try_no_definition():
    #     try_name = 'no_definition'
    #     g.Grammar.clear_all()
    #     actual_value = fb.FrameBlock._definition_exists()
    #     expected_value = False
    #     if not actual_value == expected_value:
    #         u.Utilities.print_test_error_message(
    #             method_name, try_name, expected_value, actual_value)

    # def try_definition():
    #     try_name = 'definition'
    #     g.Grammar.clear_all()
    #     fb.FrameBlock.new()
    #     actual_value = fb.FrameBlock._definition_exists()
    #     expected_value = True
    #     if not actual_value == expected_value:
    #         u.Utilities.print_test_error_message(
    #             method_name, try_name, expected_value, actual_value)
        
    # method_name = '_definition_exists'
    # try_no_definition()
    # try_definition()

# def _set_frame_block():
    # _add_layer()
    # _record_layer()
    # _add_block()

# def _add_layer():
    # rs.AddLayer(s.Settings.frame_block_layer_name)

# def _record_layer():
    # rs.SetDocumentData(
    #     l.Layer.layer_name_list_name, 
    #     s.Settings.frame_block_layer_name, 
    #     ll.Llist.dummy_value)

# def _add_block():
    # rs.CurrentLayer(s.Settings.frame_block_layer_name)
    # frame_guids = f.Frame.new(origin)
    # base_point = s.Settings.frame_block_base_point
    # block_name = s.Settings.frame_block_name
    # rs.AddBlock(frame_guids, base_point, block_name)
    # rs.CurrentLayer('Default')

# def test_delete():
    # method_name = 'delete'

    # def try_bad_state_no_block():
    #     try_name = 'bad_state_no_block'
    #     g.Grammar.clear_all()
    #     actual_value = fb.FrameBlock.delete()
    #     expected_value = False
    #     if not actual_value == expected_value:
    #         g.Grammar.print_test_error_message(
    #             method_name, try_name, expected_value, actual_value)

    # def try_bad_state_no_layer():
    #     try_name = 'bad_state_no_layer'
    #     g.Grammar.clear_all()
    #     frame_guids = f.Frame.new(origin)
    #     base_point = s.Settings.frame_block_base_point
    #     block_name = s.Settings.frame_block_name
    #     rs.AddBlock(frame_guids, base_point, block_name)
    #     actual_value = fb.FrameBlock.delete()
    #     expected_value = False
    #     if not actual_value == expected_value:
    #         g.Grammar.print_test_error_message(
    #             method_name, try_name, expected_value, actual_value)

    # def try_good_state():
    #     try_name = 'good_state'
    #     g.Grammar.clear_all()
    #     _set_frame_block()
    #     actual_value = fb.FrameBlock.delete()
    #     expected_value = True
    #     if not actual_value == expected_value:
    #         g.Grammar.print_test_error_message(
    #             method_name, try_name, expected_value, actual_value)

    # try_bad_state_no_block()
    # try_bad_state_no_layer()
    # try_good_state()

test_insert()                                   ##  done
test__new_definition()                          ##  done

# test_new()                                    ##  done
# test__definition_exists()                     ##  done
# test_delete()