import rhinoscriptsyntax as rs

def draw_square(side):
    x0, y0, z = 0, 0, 0
    x1, y1 = side, side
    p00 = [x0, y0, z]
    p01 = [x0, y1, z]
    p10 = [x1, y0, z]
    p11 = [x1, y1, z]
    rs.AddLine(p00, p01)
    rs.AddLine(p00, p10)
    rs.AddLine(p01, p11)
    rs.AddLine(p10, p11)
    dot = rs.AddTextDot('x', p00)
    dot_text = rs.TextDotText(dot)
    dot_point = rs.TextDotPoint(dot)
    print('dot text : %s' % dot_text)
    print('dot point: %s' % dot_point)

draw_square(32)