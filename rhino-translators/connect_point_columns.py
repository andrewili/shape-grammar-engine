import rhinoscriptsyntax as rs

def connect_point_columns():
    c1 = create_column(10)
    c2 = create_column(20)
    for p1 in c1:
        for p2 in c2:
            rs.AddLine(p1, p2)

def create_column(x):
    ps = []
    for i in range(5):
        y = 10 + (i * 4)
        p = [x, y, 0]
        ps.append(p)
    return ps

connect_point_columns()