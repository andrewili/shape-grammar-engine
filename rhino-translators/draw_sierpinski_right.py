#   draw_sierpinski_right.py

import rhinoscriptsyntax as rs 

def draw_sierpinski_right():
    p0000 = [7, 4, 0]
    p0012 = [7, 16, 0]
    p0024 = [7, 28, 0]
    p0304 = [10, 8, 0]
    p0316 = [10, 20, 0]
    p0608 = [13, 12, 0]
    p0900 = [16, 4, 0]
    p0912 = [16, 16, 0]
    p1204 = [19, 8, 0]
    p1800 = [25, 4, 0]
    rs.AddLine(p0000, p0024)
    rs.AddLine(p0000, p1800)
    rs.AddLine(p0012, p0900)
    rs.AddLine(p0012, p0912)
    rs.AddLine(p0024, p1800)
    rs.AddLine(p0900, p0912)
    rs.AddTextDot('a', p0304)
    rs.AddTextDot('a', p0316)
    rs.AddTextDot('a', p0608)
    rs.AddTextDot('a', p1204)

draw_sierpinski_right()