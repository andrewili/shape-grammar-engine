from package.view import grammar as g
import rhinoscriptsyntax as rs

def test_types():
    g.Grammar.clear_all()
    _try_line()
    _try_textdot()

def _try_line():
    p1 = (10, 10, 0)
    p2 = (40, 40, 0)
    l1 = rs.AddLine(p1, p2)
    name = 'l1'
    _test_line(name, l1)
    _test_textdot(name, l1)

def _try_textdot():
    p1 = (10, 10, 0)
    text = 'td1'
    td1 = rs.AddTextDot(text, p1)
    name = 'td1'
    # _test_line(name, td1)                     ##  bombs with textdot
    _test_textdot(name, td1)

def _test_line(name, guid):
    if rs.IsLine(guid):
        value = 'is'
    else:
        value = 'is not'
    print ("%s %s a line" % (name, value))

def _test_textdot(name, guid):
    if rs.IsTextDot(guid):
        value = 'is'
    else:
        value = 'is not'
    print ("%s %s a textdot" % (name, value))

def test_objects_by_type():
    g.Grammar.clear_all()
    objects = _make_objects()
    lines = _extract_lines(objects)
    lpoints = _extract_labeled_points(objects)
    if _objects_are_all_lines(lines):
        lines_verb = 'are all'
    else:
        lines_verb = 'are not all'
    print("objects in lines %s lines" % lines_verb)
    if _objects_are_all_labeled_points(lpoints):
        lpoints_verb = 'are all'
    else:
        lpoints_verb = 'are not all'
    print("objects in lpoints %s labeled points" % lpoints)

def _make_objects():
    objects = []
    lines = _make_lines()
    lpoints = _make_labeled_points()
    others = _make_others()
    objects.extend(lines)
    objects.extend(lpoints)
    objects.extend(others)
    return objects    

def _make_lines():
    p11 = (10, 10, 0)
    p15 = (10, 50, 0)
    p51 = (50, 10, 0)
    p55 = (50, 50, 0)
    l1155 = rs.AddLine(p11, p55)
    l1551 = rs.AddLine(p15, p51)
    return [l1155, l1551]

def _make_labeled_points():
    p31 = (30, 10, 0)
    p35 = (30, 50, 0)
    td31 = rs.AddTextDot('td31', p31)
    td35 = rs.AddTextDot('td35', p35)
    return [td31, td35]

def _make_others():
    p13 = (10, 30, 0)
    p53 = (50, 30, 0)
    diam = 0.5
    s13 = rs.AddSphere(p13, diam)
    s53 = rs.AddSphere(p53, diam)
    return [s13, s53]

def _objects_are_all_lines(objects):
    value = True
    for object_i in objects:
        if not rs.IsLine(object_i):
            value = False
            break
    return value

def _objects_are_all_labeled_points(objects):
    value = True
    for object_i in lpoints:
        if rs.IsTextDot(object_i):
            value = False
            break
    return value

def _extract_lines(objects):
    lines = []
    for object_i in objects:
        if rs.IsLine(object_i):
            lines.append(object_i)
    return lines

def _extract_labeled_points(objects):
    lpoints = []
    for object_i in objects:
        if rs.IsTextDot(object_i):
            lpoints.append(object_i)
    return lpoints

# test_types()
test_objects_by_type()

