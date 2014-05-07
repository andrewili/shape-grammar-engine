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

def draw_rect(x0=0, y0=0, dx=10, dy=5):
    x1 = x0 + dx
    y1 = y0 + dy
    z = 0
    p00 = [x0, y0, z]
    p01 = [x0, y1, z]
    p10 = [x1, y0, z]
    p11 = [x1, y1, z]
    rs.AddLine(p00, p01)
    rs.AddLine(p00, p10)
    rs.AddLine(p01, p11)
    rs.AddLine(p10, p11)

draw_hash()
# draw_rect(0, 0, 3, 12)