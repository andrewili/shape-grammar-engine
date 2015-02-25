import rhinoscriptsyntax as rs

def test_is_point():

    def try_triple():
        triple = [0, 0, 0]
        value = rs.IsPoint(triple)
        print("rs.IsPoint(triple): %s" % value)

    def try_rs_point_from_triple():
        triple = [0, 0, 0]
        rs_point_from_triple = rs.AddPoint(triple)
        value = rs.IsPoint(rs_point_from_triple)
        print("rs.IsPoint(rs_point_from_triple): %s" % value)

    def try_rs_point_from_singleton():
        singleton = 5
        rs_point_from_singleton = rs.AddPoint(singleton)
        value = rs.IsPoint(rs_point_from_singleton)
        print("rs.IsPoint(rs_point_from_singleton): %s" % value)

    def try_none():
        none_point = None
        value = rs.IsPoint(none_point)
        print("rs.IsPoint(none_point): %s" % value)

    try_triple()
    try_rs_point_from_triple()
    try_rs_point_from_singleton()
    try_none()

test_is_point()