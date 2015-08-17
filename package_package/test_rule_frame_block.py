from System.Drawing import Color
from package.scripts import frame as f
from package.scripts import grammar as g
from package.scripts import layer as l
from package.scripts import llist as ll
from package.scripts import rule_frame_block as rfb
import rhinoscriptsyntax as rs

position = [0, 0, 0]
user_assigned_name = 'test rule'

def _add_frames_layer():
    layer_name = f.Frame.layer_name
    dark_gray = Color.FromArgb(105, 105, 105)
    rs.AddLayer(layer_name, dark_gray)
    layer_name_list_name = l.Layer.layer_name_list_name
    layer_name = f.Frame.layer_name
    layer_value = ll.Llist.dummy_value
    rs.SetDocumentData(layer_name_list_name, layer_name, layer_value)

def test_new():
    method_name = 'new'

    def try_good_state_layer_does_not_exist():
        try_name = 'bad_state_no_layer'
        g.Grammar.clear_all()
        actual_value = rfb.RuleFrameBlock.new()
        expected_value = rfb.RuleFrameBlock.block_name
        if not actual_value == expected_value:
            g.Grammar.print_test_error_message(
                method_name, try_name, expected_value, actual_value)

    def try_good_state_layer_exists():
        try_name = 'good_state'
        g.Grammar.clear_all()
        _add_frames_layer()
        actual_value = rfb.RuleFrameBlock.new()
        expected_value = rfb.RuleFrameBlock.block_name
        if not actual_value == expected_value:
            g.Grammar.print_test_error_message(
                method_name, try_name, expected_value, actual_value)

    try_good_state_layer_does_not_exist()
    try_good_state_layer_exists()

def test_insert():
    method_name = 'insert'

    def try_bad_type_position():
        try_name = 'bad_type_position'
        g.Grammar.clear_all()
        bad_type_position = 37
        actual_value = rfb.RuleFrameBlock.insert(
            bad_type_position, user_assigned_name)
        expected_value = None
        if not actual_value == expected_value:
            g.Grammar.print_test_error_message(
                method_name, try_name, expected_value, actual_value)

    def try_bad_type_user_assigned_name():
        try_name = 'bad_type_user_assigned_name'
        g.Grammar.clear_all()
        bad_type_user_assigned_name = 37
        actual_value = rfb.RuleFrameBlock.insert(
            position, bad_type_user_assigned_name)
        expected_value = None
        if not actual_value == expected_value:
            g.Grammar.print_test_error_message(
                method_name, try_name, expected_value, actual_value)

    def try_bad_value_position():
        try_name = 'bad_value_position'
        g.Grammar.clear_all()
        bad_value_position = [0, 0, -5]
        actual_value = rfb.RuleFrameBlock.insert(
            bad_value_position, user_assigned_name)
        expected_value = None
        if not actual_value == expected_value:
            g.Grammar.print_test_error_message(
                method_name, try_name, expected_value, actual_value)

    def try_bad_value_user_assigned_name():     ##  pending list handling
        pass

    def try_good_args():
        try_name = 'good_args'
        g.Grammar.clear_all()
        rfb.RuleFrameBlock.new()
        actual_value = rfb.RuleFrameBlock.insert(
            position, user_assigned_name)
        expected_value = user_assigned_name
        if not actual_value == expected_value:
            g.Grammar.print_test_error_message(
                method_name, try_name, expected_value, actual_value)

    try_bad_type_position()
    try_bad_type_user_assigned_name()
    try_bad_value_position()
    try_bad_value_user_assigned_name()
    try_good_args()

test_new()
test_insert()
