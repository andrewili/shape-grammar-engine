from package.view import frame as f
from package.view import grammar as g
from package.view import layer as l
import rhinoscriptsyntax as rs
from package.view import settings as s
from package.tests import utilities as u

def test_new():
    def try_good_args():
        try_name = 'good_args'
        g.Grammar.clear_all()
        name = 'gaudi'
        actual_value = l.Layer.new(name)
        expected_value = name
        if not actual_value == expected_value:
            u.Utilities.print_test_error_message(
                method_name, try_name, expected_value, actual_value)

    method_name = 'new'
    try_good_args()

def test_get_layer_name_from_user():
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

def test_get_frame_positions_from_layer_name(): ##  06-26 14:20
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
        actual_value = l.Layer.get_frame_positions_from_layer_name(layer_name)
        expected_value = position
        if not actual_value == expected_value:
            u.Utilities.print_test_error_message(
                method_name, try_name, expected_value, actual_value)

    def try_good_state_two_frames():
        try_name = 'good_state_two_frames'

    method_name = 'get_frame_positions_from_layer_names'
    # try_bad_type_layer_name()                   ##  done
    # try_bad_value_no_layer_name()               ##  done
    # try_bad_state_no_frame()                    ##  done
    try_good_state_one_frame()
    # try_good_state_two_frames()

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

# test_new()                                      ##  done
# test_get_layer_name_from_user()                 ##  done
# test__is_well_formed()                          ##  done
# test__is_available()                            ##  done
test_get_frame_positions_from_layer_name()     ##  kilroy is waiting
# test__get_frames()                              ##  done

# test__add_lines()                               ##  done
# test__add_lpoints()                             ##  done
# test__add_two_frames()                          ##  done

