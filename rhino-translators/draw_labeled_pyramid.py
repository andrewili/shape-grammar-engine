import rhinoscriptsyntax as rs

def draw_labeled_pyramid():
    p000 = [0, 0, 0]
    p020 = [0, 20, 0]
    p111 = [10, 10, 10]
    p200 = [20, 0, 0]
    p220 = [20, 20, 0]
    rs.AddLine(p000, p020)
    rs.AddLine(p000, p111)
    rs.AddLine(p000, p200)
    rs.AddLine(p020, p111)
    rs.AddLine(p020, p220)
    rs.AddLine(p111, p200)
    rs.AddLine(p111, p220)
    rs.AddLine(p200, p220)
    rs.AddTextDot('p000', p000)
    rs.AddTextDot('p111', p111)

draw_labeled_pyramid()
