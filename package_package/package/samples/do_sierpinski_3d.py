import rhinoscriptsyntax as rs

p000000 = (0, 0, 0)
p000012 = (0, 0, 12)
p000024 = (0, 0, 24)
p000800 = (0, 8, 0)
p000812 = (0, 8, 12)
p001600 = (0, 16, 0)
p020202 = (2, 2, 2)
p020214 = (2, 2, 14)
p021002 = (2, 10, 2)
p040404 = (4, 4, 4)
p080000 = (8, 0, 0)
p080012 = (8, 0, 12)
p080800 = (8, 8, 0)
p100202 = (10, 2, 2)
p160000 = (16, 0, 0)
lines = [
    (p000000, p000024),
    (p000000, p001600),
    (p000000, p160000),
    (p000012, p000800),
    (p000012, p000812),
    (p000012, p080000),
    (p000012, p080012),
    (p000024, p001600),
    (p000024, p160000),
    (p000800, p000812),
    (p000800, p080000),
    (p000800, p080800),
    (p000812, p080012),
    (p000812, p080800),
    (p001600, p160000),
    (p080000, p080012),
    (p080000, p080800),
    (p080012, p080800),
]
textdots = [
    ('a', p020202),
    ('a', p020214),
    ('a', p021002),
    ('a', p040404),
    ('a', p100202),
]

def do_sierpinski_3d():
    """Prompts for a point. Draws a right-angled 3d sierpinski gasket 
    (combined before and after) at that point
    """
    message = 'Select the base point'
    base_point = rs.GetPoint(message)
    _draw_sierpinski_3d(base_point)

def _draw_sierpinski_3d(base_point):
    _draw_lines(lines, base_point)
    _draw_textdots(textdots, base_point)

def _draw_lines(lines, base_point):
    for line in lines:
        p0, p1 = line
        q0 = rs.PointAdd(p0, base_point)
        q1 = rs.PointAdd(p1, base_point)
        rs.AddLine(q0, q1)

def _draw_textdots(textdots, base_point):
    for textdot in textdots:
        label, p = textdot
        q = rs.PointAdd(p, base_point)
        rs.AddTextDot(label, q)

do_sierpinski_3d()
