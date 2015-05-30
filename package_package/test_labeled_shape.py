from package.view import grammar as g
from package.view import labeled_shape as ls
import rhinoscriptsyntax as rs

def test_get_spec_from_lshape_guids():          ##  05-26 09:28
    def get_origin():
        message = "Select the origin"
        origin = rs.GetPoint(message)
        return origin

    def get_guids():
        message = "Select the objects"
        guids = rs.GetObjects(message)
        return guids

    method_name = 'method_name'
    try_name = 'try_name'
    g.Grammar.clear_all()
    origin = get_origin()
    draw_labeled_triangle_345(origin)
    guids = get_guids()
    actual_value = ls.LabeledShape.get_spec_from_lshape_guids(guids, origin)
    expected_value = (
        [   ((0, 0, 0), (0, 24, 0)),
            ((0, 0, 0), (18, 0, 0)),
            ((0, 24, 0), (18, 0, 0))],
        [('x', (2, 2, 0))])
    if not actual_value == expected_value:
        g.Grammar.print_test_error_message(
            method_name, try_name, expected_value, actual_value)

def test_classify_guids():                      ##  05-28 09:10
    def try_empty():
        try_name = 'empty'
        empty = []
        actual_value = ls.LabeledShape.classify_guids(empty)
        expected_value = ([], [])
        if not actual_value == expected_value:
            g.Grammar.print_test_error_message(
                method_name, try_name, expected_value, actual_value)

    def try_lines_lpoints_text():
        # def test_guid_types(guids):
        #     line_value = test_line_guids(line_guids)
        #     lpoint_value = 
        #     text_value = 
        #     return (line_value, lpoint_value, text_value)
        try_name = 'lines_lpoints_text_frames'
        g.Grammar.clear_all()
        origin = get_origin()
        labeled_triangle_guids = draw_labeled_triangle_345(origin)
        actual_guids = ls.LabeledShape.classify_guids(labeled_triangle_guids)
        # actual_value = test_guid_types(actual_guids)
        expected_value = (True, True, True)
        if not actual_value == expected_value:
            g.Grammar.print_test_error_message(
                method_name, try_name, expected_value, actual_value)

    method_name = 'classify_guids'
    try_empty()
    try_lines_lpoints_text()
    # try_lines_lpoints_text_frames()

def get_origin():
    message = "Select local origin"
    origin = rs.GetPoint(message)
    return origin

def draw_labeled_triangle_345(origin=(0, 0, 0)):
    line_specs = [
        ((0, 0, 0), (0, 24, 0)),
        ((0, 0, 0), (18, 0, 0)),
        ((0, 24, 0), (18, 0, 0))]
    lpoint_specs = [('x', (2, 2, 0))]
    for line_spec in line_specs:
        p1, p2 = line_spec
        q1 = rs.PointAdd(p1, origin)
        q2 = rs.PointAdd(p2, origin)
        rs.AddLine(q1, q2)
    for lpoint_spec in lpoint_specs:
        label = lpoint_spec[0]
        p = lpoint_spec[1]
        q = rs.PointAdd(p, origin)
        rs.AddTextDot(label, q)
    line, lpoint, text = 4, 8192, 512
    lines = rs.ObjectsByType(line)
    lpoints = rs.ObjectsByType(lpoint)
    texts = rs.ObjectsByType(text)
    return (lines, lpoints, texts)

def test_get_end_points():
    def try_good_arg():
        try_name = 'good_arg'
        line_guid = get_line_30_10()
        actual_value = ls.LabeledShape.get_end_points(line_guid)
        actual_spec = get_spec_from_line_end_points(actual_value)
        expected_spec = ((10, 10, 0), (30, 30, 0))
        if not actual_value == expected_spec:
            g.Grammar.print_test_error_message(
                method_name, try_name, expected_spec, actual_value)

    method_name = 'get_end_points'
    try_good_arg()

def get_line_30_10():
    message1 = "Select the point (30, 30, 0)"
    message2 = "Select the point (10, 10, 0)"
    p1, p2 = rs.GetLine(0, None, message1, message2)
    line_30_10 = rs.AddLine(p1, p2)
    return line_30_10

def get_spec_from_line_end_points(line_end_points):
    tail, head = line_end_points
    tail_spec = rs.PointCoordinates(tail)       ##  "tail is not a point guid"
    head_spec = rs.PointCoordinates(head)
    return (tail_spec, head_spec)

test_get_spec_from_lshape_guids()
# test_classify_guids()
# draw_labeled_triangle_345()
# test_get_end_points()
