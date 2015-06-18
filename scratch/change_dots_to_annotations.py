import rhinoscriptsyntax as rs

def change_dots_to_annotations():
    text_dots = _get_text_dots()
    for text_dot in text_dots:
        text, point = _get_text_and_position_from_text_dot(text_dot)
        _delete_text_dot(text_dot)
        _add_labeled_point(text, point)

def _get_text_dots():
    text_dot_type = 8192
    text_dots = rs.ObjectsByType(text_dot_type)
    return text_dots

def _get_text_and_position_from_text_dot(text_dot):
    text = rs.TextDotText(text_dot)
    point = rs.TextDotPoint(text_dot)
    return (text, point)

def _delete_text_dot(text_dot):
    rs.DeleteObject(text_dot)

def _add_labeled_point(text, point):
    # _add_label(text, point)
    _add_point(point)

def _add_label(text, point):
    label_offset = (0, 0, 0)
    position = rs.PointAdd(point, label_offset)
    height = 1.5
    rs.AddText(text, position, height)

def _add_point(point):
    radius = 0.25
    rs.AddCircle(point, radius)

change_dots_to_annotations()
