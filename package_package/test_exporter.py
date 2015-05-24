from package.translators import exporter as e
from package.view import frame_block as fb
from package.view import grammar as g
from package.view import initial_shape as ish
from package.view import rule as r
from package.view import shape_layer as sl
import rhinoscriptsyntax as rs

def test___request_rule_item():
    def try_preselected_items():
        try_name = 'preselected_items'
        g.Grammar.clear_all()
        fb.FrameBlock.new()
        _draw_two_rules()
        message = "Preselect some objects"
        preselected_objects = rs.GetObjects(message, 0, True, False, True)
        exp = e.Exporter()
        item = exp._request_rule_item()
        actual_value = rs.IsObject(item)
        expected_value = True
        if not actual_value == expected_value:
            g.Grammar.print_test_error_message(
                method_name, try_name, expected_value, actual_value)

    method_name = '_request_rule_item'
    try_preselected_items()

# def test__one_rule_is_specified_by():
    # def try_good_value_no_items():
    #     try_name = 'good_value_no_items'
    #     exp = e.Exporter()
    #     good_value_no_items = []
    #     actual_value = exp._one_rule_is_specified_by(good_value_no_items)
    #     expected_value = False
    #     if not actual_value == expected_value:
    #         g.Grammar.print_test_error_message(
    #             method_name, try_name, expected_value, actual_value)

    # def try_good_value_one_item():
    #     try_name = 'good_value_one_item'
    #     _draw_two_rules()
    #     exp = e.Exporter()
    #     message = "Select one item in the rule"
    #     good_value_one_item = rs.GetObjects(message)
    #     actual_value = exp._one_rule_is_specified_by(good_value_one_item)
    #     expected_value = True
    #     if not actual_value == expected_value:
    #         g.Grammar.print_test_error_message(
    #             method_name, try_name, expected_value, actual_value)

    # def try_good_value_items_in_two_shapes_one_rule():
    #     try_name = 'good_value_items_in_two_shapes_one_rule'
    #     _draw_two_rules()
    #     exp = e.Exporter()
    #     message = "Select one item in each of the left and right shapes"
    #     good_value_items_in_two_shapes_one_rule = rs.GetObjects(message)
    #     actual_value = exp._one_rule_is_specified_by(
    #         good_value_items_in_two_shapes_one_rule)
    #     expected_value = True
    #     if not actual_value == expected_value:
    #         g.Grammar.print_test_error_message(
    #             method_name, try_name, expected_value, actual_value)

    # def try_good_value_items_in_two_rules():
    #     try_name = 'good_value_items_in_two_rules'
    #     _draw_two_rules()
    #     exp = e.Exporter()
    #     message = "Select items in two different rules"
    #     good_value_items_in_two_rules = rs.GetObjects(message)
    #     actual_value = exp._one_rule_is_specified_by(
    #         good_value_items_in_two_rules)
    #     expected_value = False
    #     if not actual_value == expected_value:
    #         g.Grammar.print_test_error_message(
    #             method_name, try_name, expected_value, actual_value)

    # method_name = '_one_rule_is_specified_by'
    # try_good_value_no_items()
    # try_good_value_one_item()
    # try_good_value_items_in_two_shapes_one_rule()
    # try_good_value_items_in_two_rules()

# def test__get_rule_from_guid():
    # def try_good_value():
    #     try_name = "try_good_value"
    #     g.Grammar.clear_all()
    #     fb.FrameBlock.new()
    #     _draw_two_rules()
    #     exp = e.Exporter()
    #     message = "Select one item in rule 1"
    #     guid = rs.GetObject(message)
    #     actual_value = exp._get_rule_from_guid(guid)
    #     expected_value = "rule_1"
    #     if not actual_value == expected_value:
    #         g.Grammar.print_test_error_message(
    #             method_name, try_name, expected_value, actual_value)

    # method_name = "_get_rule_from_guid"
    # try_good_value()

def test__get_name_from_rule_item():           ##  05-18 12:19
    def _request_initial_shape_item():
        message = "Select an item in an initial shape"
        item = rs.GetObject(message)
        return item
    
    def try_bad_item():
        try_name = 'bad_item'
        g.Grammar.clear_all()
        fb.FrameBlock.new()
        _draw_two_initial_shapes()
        _draw_two_rules()
        exp = e.Exporter()
        bad_item = _request_initial_shape_item()
        actual_value = exp._get_name_from_rule_item(bad_item)
        expected_value = None
        if not actual_value == expected_value:
            g.Grammar.print_test_error_message(
                method_name, try_name, expected_value, actual_value)

    method_name = "_get_name_from_rule_item"
    try_bad_item()

### utility methods

def _draw_two_rules():
    """Sets up two rules, each with rule name, shapes, shape names, lines, and 
    labeled points.
    """
    # g.Grammar.clear_all()
    # fb.FrameBlock.new()
    _draw_rule_one()
    _draw_rule_two()

def _draw_rule_one():
    rule_name = 'rule_1'
    rule_position = (0, -50, 0)
    sierpinski_triangle_before = (
        [   ((0, 0, 0), (12, 0, 0)),
            ((0, 0, 0), (0, 16, 0)),
            ((0, 16, 0), (12, 0, 0))],
        [('x', (2, 2, 0))])
    sierpinski_triangle_after = (
        [   ((0, 0, 0), (0, 16, 0)),
            ((0, 0, 0), (12, 0, 0)),
            ((0, 8, 0), (6, 0, 0)),
            ((0, 8, 0), (6, 8, 0)),
            ((0, 16, 0), (12, 0, 0)),
            ((6, 0, 0), (6, 8, 0))],
        [   ('x', (1, 1, 0)),
            ('x', (1, 9, 0)),
            ('x', (7, 1, 0))])
    r.Rule._new(rule_name, rule_position)
    _draw_rule(
        sierpinski_triangle_before, 
        sierpinski_triangle_after, 
        rule_name, 
        rule_position)

def _draw_rule_two():
    rule_name = 'rule_2'
    rule_position = (0, -100, 0)
    cross = (
        [   ((10, 15, 0), (20, 15, 0)),
            ((15, 10, 0), (15, 20, 0))],
        [])
    shape_x = (
        [   ((10, 10, 0), (20, 20, 0)),
            ((10, 20, 0), (20, 10, 0))],
        [])
    r.Rule._new(rule_name, rule_position)
    _draw_rule(cross, shape_x, rule_name, rule_position)

def _draw_two_initial_shapes():
    _draw_sierpinski_triangle_before()
    _draw_cross()

def _draw_sierpinski_triangle_before():
    initial_shape_name = 'initial_shape_1'
    initial_shape_position = (0, 0, 0)
    sierpinski_triangle_before = (
        [   ((0, 0, 0), (12, 0, 0)),
            ((0, 0, 0), (0, 16, 0)),
            ((0, 16, 0), (12, 0, 0))],
        [('x', (2, 2, 0))])
    sl.ShapeLayer.new(initial_shape_name, initial_shape_position)
    ish.InitialShape._record(initial_shape_name)
    _draw_labeled_shape(
        sierpinski_triangle_before,
        initial_shape_position,
        initial_shape_name)

def _draw_cross():
    initial_shape_name = 'initial_shape_2'
    initial_shape_position = (0, 50, 0)
    cross = (
        [   ((10, 15, 0), (20, 15, 0)),
            ((15, 10, 0), (15, 20, 0))],
        [])
    sl.ShapeLayer.new(initial_shape_name, initial_shape_position)
    ish.InitialShape._record(initial_shape_name)
    _draw_labeled_shape(
        cross,
        initial_shape_position,
        initial_shape_name)

def _draw_rule(left_shape_spec, right_shape_spec, rule_layer, rule_position):
    left_shape_position = rule_position
    right_shape_position = r.Rule._get_right_shape_position(
        left_shape_position)
    left_shape_layer = r.Rule._get_shape_name_from_rule_name(
        rule_layer, 'left')
    right_shape_layer = r.Rule._get_shape_name_from_rule_name(
        rule_layer, 'right')
    _draw_labeled_shape(
        left_shape_spec, left_shape_position, left_shape_layer)
    _draw_labeled_shape(
        right_shape_spec, right_shape_position, right_shape_layer)

def _draw_labeled_shape(shape_spec, position, layer):
    rs.CurrentLayer(layer)
    line_specs, lpoint_specs = shape_spec
    for line_spec in line_specs:
        p1, p2 = line_spec
        q1 = rs.PointAdd(p1, position)
        q2 = rs.PointAdd(p2, position)
        rs.AddLine(q1, q2)
    for lpoint_spec in lpoint_specs:
        label, p = lpoint_spec
        q = rs.PointAdd(p, position)
        rs.AddTextDot(label, q)
    rs.CurrentLayer('Default')

# export_rule()
# test___request_rule_item()                      ##  done
test__get_name_from_rule_item()
# _is_a_shape_layer()
# _get_rule_name_from_shape_layer()

# test__get_spec_from_rule_name()               ##  to do

# test__get_repr_from_rule_spec()               ##  to do

# test__write_rule_file()                       ##  to do

### utility methods
# _draw_two_rules()
