from package.view import grammar as g
import rhinoscriptsyntax as rs

def test_vector_compare():
    p1, p2 = set_up()
    value = rs.VectorCompare(p1, p2)
    if value == -1:
        relation = 'lt'
    elif value == 0:
        relation = 'eq'
    elif value == 1:
        relation = 'gt'
    else:
        pass
    print("relation: %s" % relation)

def test_curve_start_end_points():
    p1, p2 = set_up()
    line = rs.AddLine(p1, p2)
    start_point = rs.CurveStartPoint(line)
    end_point = rs.CurveEndPoint(line)
    start_point_spec = rs.PointCoordinates(start_point) ##  not a guid
    end_point_spec = rs.PointCoordinates(end_point)
    print("start point: %s" % start_point_spec)
    print("end point: %s" % end_point_spec)

def set_up():
    g.Grammar.clear_all()
    message1 = "Select point 1"
    message2 = "Select point 2"
    p1 = rs.GetPoint(message1)
    p2 = rs.GetPoint(message2)
    return [p1, p2]

# test_vector_compare()
test_curve_start_end_points()
