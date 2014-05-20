import rhinoscriptsyntax as rs

def draw_square(side):
    mid = side / 2
    x0, y0, z = 0, 0, 0
    x1, y1 = side, side
    x2, y2, = mid, mid
    p00 = [x0, y0, z]
    p01 = [x0, y1, z]
    p10 = [x1, y0, z]
    p11 = [x1, y1, z]
    p22 = [x2, y2, z]
    rs.AddLine(p00, p01)
    rs.AddLine(p00, p10)
    rs.AddLine(p01, p11)
    rs.AddLine(p10, p11)
    dot00 = rs.AddTextDot('00', p00)
    dot22 = rs.AddTextDot('22', p22)
    dot_text = rs.TextDotText(dot22)
    dot_point = rs.TextDotPoint(dot22)
    print('dot text : %s' % dot_text)
    print('dot point: %s' % dot_point)

draw_square(32)