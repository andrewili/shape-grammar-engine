from package.view import frame as f
from package.view import grammar as g
from package.view import layer as l
import rhinoscriptsyntax as rs
from package.view import settings as s
from package.tests import utilities as u

def test_new():                                 ##  done 08-05
    def try_good_value():
        try_name = 'good_value'
        g.Grammar.clear_all()
        name = 'gaudi'
        actual_value = l.Layer.new(name)
        expected_value = name
        if not actual_value == expected_value:
            u.Utilities.print_test_error_message(
                method_name, try_name, expected_value, actual_value)

    method_name = 'new'
    try_good_value()

def test_get_layer_name_from_user():            ##  done 08-06
    def try_something():
        try_name = 'something'
        g.Grammar.clear_all()
        used_name = 'used_name'
        rs.AddLayer(used_name)
        good_name = 'good_name'
        print("Enter: 1, '%s'; 2, '%s'; 3, '%s'" % (
            'kil#roy', used_name, good_name))
        actual_value = l.Layer.get_layer_name_from_user()
        expected_value = good_name
        if not actual_value == expected_value:
            u.Utilities.print_test_error_message(
                method_name, try_name, expected_value, actual_value)

    method_name = 'get_layer_name_from_user'
    try_something()

def test__is_well_formed():
    def try_ill_formed():
        try_name = 'ill_formed'
        g.Grammar.clear_all()
        ill_formed_name = 'kil#roy'
        actual_value = l.Layer._is_well_formed(ill_formed_name)
        expected_value = False
        if not actual_value == expected_value:
            u.Utilities.print_test_error_message(
                method_name, try_name, expected_value, actual_value)

    def try_well_formed():
        try_name = 'well_formed'
        g.Grammar.clear_all()
        well_formed_name = 'good_name'
        actual_value = l.Layer._is_well_formed(well_formed_name)
        expected_value = True
        if not actual_value == expected_value:
            u.Utilities.print_test_error_message(
                method_name, try_name, expected_value, actual_value)

    method_name = '_is_well_formed'
    try_ill_formed()
    try_well_formed()

def test__is_available():
    def try_used_name():
        try_name = 'used_name'
        used_name = 'used_name'
        g.Grammar.clear_all()
        rs.AddLayer(used_name)
        actual_value = l.Layer._is_available(used_name)
        expected_value = False
        if not actual_value == expected_value:
            u.Utilities.print_test_error_message(
                method_name, try_name, expected_value, actual_value)

    def try_unused_name():
        try_name = 'unused_name'
        unused_name = 'unused_name'
        g.Grammar.clear_all()
        actual_value = l.Layer._is_available(unused_name)
        expected_value = True
        if not actual_value == expected_value:
            u.Utilities.print_test_error_message(
                method_name, try_name, expected_value, actual_value)

    method_name = '_is_available'
    try_used_name()
    try_unused_name()

def test_get_frame_instance():
    def try_bad_value_non_existent_layer():
        try_name = 'try_bad_state_non_existent_layer'
        u.Utilities.make_grammar_3_initial_shapes_4_rules()
        initial_shape = 'no_such_layer'
        actual_value = l.Layer.get_frame_instance(initial_shape)
        expected_value = None
        if not actual_value == expected_value:
            u.Utilities.print_test_error_message(
                method_name, try_name, expected_value, actual_value)

    def try_bad_state_0_frame_instances():
        try_name = 'bad_state_0_frame_instances'
        u.Utilities.make_grammar_3_initial_shapes_4_rules()
        initial_shape = 'frames'
        actual_value = l.Layer.get_frame_instance(initial_shape)
        expected_value = None
        if not actual_value == expected_value:
            u.Utilities.print_test_error_message(
                method_name, try_name, expected_value, actual_value)

    def try_bad_state_2_frame_instances():
        try_name = 'bad_state_2_frame_instances'
        u.Utilities.make_grammar_3_initial_shapes_4_rules()
        initial_shape = 'subdivide_triangle'
        actual_value = l.Layer.get_frame_instance(initial_shape)
        expected_value = None
        if not actual_value == expected_value:
            u.Utilities.print_test_error_message(
                method_name, try_name, expected_value, actual_value)

    def try_good_state_1_frame_instance():
        try_name = 'good_arg'
        u.Utilities.make_grammar_3_initial_shapes_4_rules()
        initial_shape = 'labeled_square'
        actual_value = l.Layer.get_frame_instance(initial_shape)
        rs.SelectObject(actual_value)

    method_name = 'get_frame_instance'
    try_bad_value_non_existent_layer()
    try_bad_state_0_frame_instances()
    try_bad_state_2_frame_instances()
    try_good_state_1_frame_instance()

def test_get_frame_instance_pair():
    def try_good_arg():
        method_name = 'good_arg'
        u.Utilities.make_grammar_3_initial_shapes_3_rules()
        actual_value = l.Layer.get_frame_instance_pair('add_h_in_square_spec')
        # rs.SelectObject(actual_value[0])
        rs.SelectObjects(actual_value)

    method_name = 'get_frame_instance_pair'
    try_good_arg()

def test_contains_initial_shape():
    pass

def test_contains_rule():
    pass

def test__get_number_of_frames():
    def try_bad_state_no_frame_definition():
        try_name = 'bad_state_no_frame_definition'
        g.Grammar.clear_all()
        l.Layer.new(layer_name)
        actual_value = l.Layer._get_number_of_frames(layer_name)
        expected_value = 0
        if not actual_value == expected_value:
            u.Utilities.print_test_error_message(
                method_name, try_name, expected_value, actual_value)

    def try_good_state_0_frames_0_others():
        try_name = 'good_state_0_frames_0_others'
        g.Grammar.clear_all()
        l.Layer.new(layer_name)
        actual_value = l.Layer._get_number_of_frames(layer_name)
        expected_value = 0
        if not actual_value == expected_value:
            u.Utilities.print_test_error_message(
                method_name, try_name, expected_value, actual_value)

    def try_good_state_0_frames_2_others():
        try_name = 'good_state_0_frames_2_others'
        g.Grammar.clear_all()
        l.Layer.new(layer_name)
        _insert_other_block(other_block_name, layer_name, p4)
        _insert_other_block(other_block_name, layer_name, p5)
        actual_value = l.Layer._get_number_of_frames(layer_name)
        expected_value = 0
        if not actual_value == expected_value:
            u.Utilities.print_test_error_message(
                method_name, try_name, expected_value, actual_value)

    def try_good_state_1_frames_0_others():
        try_name = 'good_state_1_frames_0_others'
        g.Grammar.clear_all()
        l.Layer.new(layer_name)
        f.Frame.new_instance(frame_name, layer_name, p1)
        actual_value = l.Layer._get_number_of_frames(layer_name)
        expected_value = 1
        if not actual_value == expected_value:
            u.Utilities.print_test_error_message(
                method_name, try_name, expected_value, actual_value)

    def try_good_state_1_frames_2_others():
        try_name = 'good_state_1_frames_2_others'
        g.Grammar.clear_all()
        l.Layer.new(layer_name)
        f.Frame.new_instance(frame_name, layer_name, p1)
        _insert_other_block(other_block_name, layer_name, p4)
        _insert_other_block(other_block_name, layer_name, p5)
        actual_value = l.Layer._get_number_of_frames(layer_name)
        expected_value = 1
        if not actual_value == expected_value:
            u.Utilities.print_test_error_message(
                method_name, try_name, expected_value, actual_value)

    def try_good_state_2_frames_0_others():
        try_name = 'good_state_2_frames_0_others'
        g.Grammar.clear_all()
        l.Layer.new(layer_name)
        f.Frame.new_instance(frame_name, layer_name, p1)
        f.Frame.new_instance(frame_name, layer_name, p2)
        actual_value = l.Layer._get_number_of_frames(layer_name)
        expected_value = 2
        if not actual_value == expected_value:
            u.Utilities.print_test_error_message(
                method_name, try_name, expected_value, actual_value)

    def try_good_state_2_frames_2_others():
        try_name = 'good_state_2_frames_2_others'
        g.Grammar.clear_all()
        l.Layer.new(layer_name)
        f.Frame.new_instance(frame_name, layer_name, p1)
        f.Frame.new_instance(frame_name, layer_name, p2)
        _insert_other_block(other_block_name, layer_name, p4)
        _insert_other_block(other_block_name, layer_name, p5)
        actual_value = l.Layer._get_number_of_frames(layer_name)
        expected_value = 2
        if not actual_value == expected_value:
            u.Utilities.print_test_error_message(
                method_name, try_name, expected_value, actual_value)

    def try_good_state_3_frames_0_others():
        try_name = 'good_state_3_frames_0_others'
        g.Grammar.clear_all()
        l.Layer.new(layer_name)
        f.Frame.new_instance(frame_name, layer_name, p1)
        f.Frame.new_instance(frame_name, layer_name, p2)
        f.Frame.new_instance(frame_name, layer_name, p3)
        actual_value = l.Layer._get_number_of_frames(layer_name)
        expected_value = 3
        if not actual_value == expected_value:
            u.Utilities.print_test_error_message(
                method_name, try_name, expected_value, actual_value)

    def try_good_state_3_frames_2_others():
        try_name = 'good_state_3_frames_2_others'
        g.Grammar.clear_all()
        l.Layer.new(layer_name)
        f.Frame.new_instance(frame_name, layer_name, p1)
        f.Frame.new_instance(frame_name, layer_name, p2)
        f.Frame.new_instance(frame_name, layer_name, p3)
        _insert_other_block(other_block_name, layer_name, p4)
        _insert_other_block(other_block_name, layer_name, p5)
        actual_value = l.Layer._get_number_of_frames(layer_name)
        expected_value = 3
        if not actual_value == expected_value:
            u.Utilities.print_test_error_message(
                method_name, try_name, expected_value, actual_value)

    method_name = '_get_number_of_frames'
    g.Grammar.clear_all()
    layer_name = 'layer_i'
    frame_name = f.Frame._new_definition()
    other_block_name = _define_other_block()
    p1 = (0, 0, 0)
    p2 = (50, 0, 0)
    p3 = (100, 0, 0)
    p4 = (0, 50, 0)
    p5 = (50, 50, 0)
    try_bad_state_no_frame_definition()
    try_good_state_0_frames_0_others()
    try_good_state_0_frames_2_others()
    try_good_state_1_frames_0_others()
    try_good_state_1_frames_2_others()
    try_good_state_2_frames_0_others()
    try_good_state_2_frames_2_others()
    try_good_state_3_frames_0_others()
    try_good_state_3_frames_2_others()

def test__get_initial_labeled_shape_string():   ##  07-06 15:56
    def try_bad_value_non_existent_initial_labeled_shape():
        try_name = 'bad_value_no_initial_labeled_shape'
        actual_value = g.Grammar._get_initial_labeled_shape_string(
            non_existent_initial_shape_layer_name)
        expected_value = None
        if not actual_value == expected_value:
            u.Utilities.print_test_error_message(
                method_name, try_name, expected_value, actual_value)

    def try_good_value():
        try_name = 'good_state'
        actual_value = g.Grammar._get_initial_labeled_shape_string(
            u.Utilities.labeled_h_spec)
        expected_value = u.Utilities.labeled_h_is_string
        if not actual_value == expected_value:
            u.Utilities.print_test_error_message(
                method_name, try_name, expected_value, actual_value)

    method_name = '_get_initial_labeled_shape_string'
    g.Grammar.clear_all()
    initial_shape_string = _add_initial_labeled_shape()
    try_bad_value_non_existent_initial_labeled_shape()
    try_good_value()

def test_get_frame_positions_from_layer_name():
    def try_bad_type_layer_name():
        try_name = 'bad_type_layer_name'
        layer_name = 37
        actual_value = l.Layer.get_frame_positions_from_layer_name(layer_name)
        expected_value = None
        if not actual_value == expected_value:
            u.Utilities.print_test_error_message(
                method_name, try_name, expected_value, actual_value)

    def try_bad_value_no_layer_name():
        try_name = 'bad_state_no_layer_name'
        g.Grammar.clear_all()
        layer_name = s.Settings.first_rule_layer_name
        actual_value = l.Layer.get_frame_positions_from_layer_name(layer_name)
        expected_value = None
        if not actual_value == expected_value:
            u.Utilities.print_test_error_message(
                method_name, try_name, expected_value, actual_value)

    def try_bad_state_no_frame():
        try_name = 'bad_state_no_frame'
        g.Grammar.clear_all()
        layer_name = s.Settings.first_rule_layer_name
        l.Layer.new(layer_name)
        actual_value = l.Layer.get_frame_positions_from_layer_name(layer_name)
        expected_value = None
        if not actual_value == expected_value:
            u.Utilities.print_test_error_message(
                method_name, try_name, expected_value, actual_value)

    def try_good_state_one_frame():
        try_name = 'good_state_one_frame'
        g.Grammar.clear_all()
        layer_name = s.Settings.first_initial_shape_layer_name
        l.Layer.new(layer_name)
        rs.CurrentLayer(layer_name)
        position = s.Settings.first_initial_shape_frame_position
        f.Frame.new_instance(layer_name, layer_name, position)
        rs.CurrentLayer(s.Settings.default_layer_name)
        actual_guids = l.Layer.get_frame_positions_from_layer_name(layer_name)
        actual_coords = actual_guids.pop()
        actual_value = tuple(actual_coords)
        expected_value = position
        if not actual_value == expected_value:
            u.Utilities.print_test_error_message(
                method_name, try_name, expected_value, actual_value)

    def try_good_state_two_frames():
        try_name = 'good_state_two_frames'
        g.Grammar.clear_all()
        layer_name = s.Settings.first_rule_layer_name
        l.Layer.new(layer_name)
        rs.CurrentLayer(layer_name)
        left_frame_name = "%s_L" % layer_name
        right_frame_name = "%s_R" % layer_name
        left_frame_position = s.Settings.first_rule_left_frame_position
        right_frame_position = s.Settings.get_right_frame_position(
            left_frame_position)
        f.Frame.new_instance(left_frame_name, layer_name, left_frame_position)
        f.Frame.new_instance(
            right_frame_name, layer_name, right_frame_position)
        rs.CurrentLayer(s.Settings.default_layer_name)
        actual_value = l.Layer.get_frame_positions_from_layer_name(layer_name)
        expected_value = (left_frame_position, right_frame_position)
        if not (
            rs.PointCompare(actual_value[0], expected_value[0]) and
            rs.PointCompare(actual_value[1], expected_value[1])
        ):
            u.Utilities.print_test_error_message(
                method_name, try_name, expected_value, actual_value)

    method_name = 'get_frame_positions_from_layer_names'
    try_bad_type_layer_name()                   ##  done
    try_bad_value_no_layer_name()               ##  done
    try_bad_state_no_frame()                    ##  done
    try_good_state_one_frame()                  ##  done
    try_good_state_two_frames()                 ##  done

def test__get_frames():
    def try_lines_lpoints_no_frames():
        try_name = 'lines_lpoints_no_frames'
        g.Grammar.clear_all()
        l.Layer.new(layer_name)
        rs.CurrentLayer(layer_name)
        _add_lines_lpoints_no_frames()
        rs.CurrentLayer(default_layer_name)
        actual_value = l.Layer._get_frames(layer_name)
        expected_value = None
        if not actual_value == expected_value:
            u.Utilities.print_test_error_message(
                method_name, try_name, expected_value, actual_value)

    def try_no_lines_no_lpoints_one_frame():
        try_name = 'no_lines_no_lpoints_one_frame'
        g.Grammar.clear_all()
        l.Layer.new(layer_name)
        rs.CurrentLayer(layer_name)
        frame_guid = _add_no_lines_no_lpoints_one_frame()
        rs.CurrentLayer(s.Settings.default_layer_name)
        actual_value = l.Layer._get_frames(layer_name)
        expected_value = [frame_guid]
        if not actual_value == expected_value:
            u.Utilities.print_test_error_message(
                method_name, try_name, expected_value, actual_value)

    def try_no_lines_no_lpoints_two_frames():
        try_name = 'no_lines_no_lpoints_two_frames'
        g.Grammar.clear_all()
        l.Layer.new(layer_name)
        rs.CurrentLayer(layer_name)
        frame_guids = _add_no_lines_no_lpoints_two_frames()
        rs.CurrentLayer(default_layer_name)
        actual_value = l.Layer._get_frames(layer_name)
        expected_value = frame_guids
        if not actual_value == expected_value:
            u.Utilities.print_test_error_message(
                method_name, try_name, expected_value, actual_value)

    def try_lines_lpoints_two_frames():
        try_name = 'lines_lpoints_two_frames'
        g.Grammar.clear_all()
        l.Layer.new(layer_name)
        rs.CurrentLayer(layer_name)
        frame_guids = _add_lines_lpoints_two_frames()
        rs.CurrentLayer(default_layer_name)
        actual_value = l.Layer._get_frames(layer_name)
        expected_value = frame_guids
        if not actual_value == expected_value:
            u.Utilities.print_test_error_message(
                method_name, try_name, expected_value, actual_value)

    method_name = '_get_frames'
    layer_name = s.Settings.first_rule_layer_name
    default_layer_name = s.Settings.default_layer_name
    try_lines_lpoints_no_frames()               ##  done
    try_no_lines_no_lpoints_one_frame()         ##  done
    try_no_lines_no_lpoints_two_frames()        ##  done
    try_lines_lpoints_two_frames()              ##  done

def _add_lines_lpoints_no_frames():
    _add_lines()
    _add_lpoints()

def _add_no_lines_no_lpoints_one_frame():
    frame_guid = _add_one_frame()
    return frame_guid

def _add_no_lines_no_lpoints_two_frames():
    frame_guids = _add_two_frames()
    return frame_guids

def _add_lines_lpoints_two_frames():
    _add_lines()
    _add_lpoints()
    frame_guids = _add_two_frames()
    return frame_guids

def _add_lines():
    layer_name = s.Settings.first_rule_layer_name
    l.Layer.new(layer_name)
    rs.CurrentLayer(layer_name)
    line_specs = [
        ((0, 0, 0), (20, 20, 0)),
        ((0, 20, 0), (20, 0, 0))]
    for line_spec in line_specs:
        p1, p2 = line_spec
        rs.AddLine(p1, p2)
    rs.CurrentLayer(s.Settings.default_layer_name)

def _add_lpoints():
    lpoints = [
        ('a', (0, 10, 0)),
        ('a', (20, 10, 0))]
    layer_name = s.Settings.first_rule_layer_name
    l.Layer.new(layer_name)
    rs.CurrentLayer(layer_name)
    for lpoint in lpoints:
        text, point = lpoint
        rs.AddTextDot(text, point)
    rs.CurrentLayer(s.Settings.default_layer_name)
    
def _add_one_frame():
    layer_name = s.Settings.first_rule_layer_name
    frame_name = layer_name
    rs.CurrentLayer(layer_name)
    origin = (30, 30, 0)
    frame_guid = f.Frame.new_instance(frame_name, layer_name, origin)
    rs.CurrentLayer(s.Settings.default_layer_name)
    return frame_guid

def _add_two_frames():
    layer_name = s.Settings.first_rule_layer_name
    l.Layer.new(layer_name)
    frame_name = layer_name
    frame_specs = [
        ("%s_L" % frame_name, layer_name, (20, 20, 0)),
        ("%s_R" % frame_name, layer_name, (40, 40, 0))]
    rs.CurrentLayer(layer_name)
    frame_guids = []
    for frame_spec in frame_specs:
        frame_name, layer_name, origin = frame_spec
        frame_guid = f.Frame.new_instance(frame_name, layer_name, origin)
        frame_guids.append(frame_guid)
    rs.CurrentLayer(s.Settings.default_layer_name)
    return frame_guids

def test__add_lines():
    g.Grammar.clear_all()
    _add_lines()

def test__add_lpoints():
    g.Grammar.clear_all()
    _add_lpoints()

def test__add_two_frames():
    g.Grammar.clear_all()
    _add_two_frames()

def _define_other_block():
    guids = _draw_x()
    base_point = (0, 0, 0)
    name = 'x'
    delete_input = True
    rs.AddBlock(guids, base_point, name, delete_input)
    return name

def _draw_x():
    guid_1 = rs.AddLine((0, 0, 0), (40, 40, 0))
    guid_2 = rs.AddLine((0, 40, 0), (40, 0, 0))
    guids = [guid_1, guid_2]
    return guids

def _insert_other_block(other_block_name, layer_name, position):
    if not rs.IsBlock(other_block_name):
        _define_other_block()
    rs.CurrentLayer(layer_name)
    rs.InsertBlock(other_block_name, position)
    rs.CurrentLayer(s.Settings.default_layer_name)


# test_new()                                      ##  done 08-05
test_get_layer_name_from_user()                 ##  done 08-06 / manual test
# test__is_well_formed()                          ##  done
# test__is_available()                            ##  done

# test_get_frame_instance()                       ##  done / manual test
# test_get_frame_instance_pair()                  ##  done / manual test

# test_contains_initial_shape()                   ##  trivial
# test_contains_rule()                            ##  trivial
# test__get_number_of_frames()                    ##  done
# test__contains_guid()                           ##  trivial

# test_get_frame_positions_from_layer_name()      ##  done
# test__get_frames()                              ##  done
# test__order_left_right()                        ##  trivial

# test__get_initial_labeled_shape_string()
# test__get_rule_labeled_shape_strings()

# test__add_lines()                               ##  done
# test__add_lpoints()                             ##  done
# test__add_two_frames()                          ##  done

