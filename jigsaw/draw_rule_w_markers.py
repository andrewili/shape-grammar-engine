#   draw_rule_w_markers.py

import rhinoscriptsyntax as rs

def draw_rule_w_markers():
    p0 = [10, 10, 0]
    p01 = [11, 9, 0]
    p02 = [13, 9, 0]
    p03 = [13, 11, 0]
    p04 = [15, 11, 0]
    p05 = [15, 9, 0]
    p06 = [17, 9, 0]
    p07 = [17, 11, 0]
    p08 = [19, 11, 0]
    p1 = [20, 10, 0]
    p2 = [18, 11, 0]

    def draw_marked_line():
        rs.AddLine(p0, p1)
        rs.AddLine(p1, p2)

    def draw_zigzag():
        rs.AddLine(p0, p01)
        rs.AddLine(p01, p02)
        rs.AddLine(p02, p03)
        rs.AddLine(p03, p04)
        rs.AddLine(p04, p05)
        rs.AddLine(p05, p06)
        rs.AddLine(p06, p07)
        rs.AddLine(p07, p08)
        rs.AddLine(p08, p1)

    draw_marked_line()
    draw_zigzag()

draw_rule_w_markers()