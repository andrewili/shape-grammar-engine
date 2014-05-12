import rhinoscriptsyntax as rs

def draw_hash():
    x0, x1, x2, x3 = 0, 10, 20, 30
    y0, y1, y2, y3 = 0, 10, 20, 30
    z = 0
    p01 = [x0, y1, z]
    p02 = [x0, y2, z]
    p10 = [x1, y0, z]
    p13 = [x1, y3, z]
    p20 = [x2, y0, z]
    p23 = [x2, y3, z]
    p31 = [x3, y1, z]
    p32 = [x3, y2, z]
    l0131 = rs.AddLine(p01, p31)
    l0232 = rs.AddLine(p02, p32)
    l1013 = rs.AddLine(p10, p13)
    l2023 = rs.AddLine(p20, p23)

def draw_lpoint(label='X', x=15, y=15, z=0):
    point = [x, y, z]
    lpoint = rs.AddTextDot(label, point)

draw_hash()
draw_lpoint()