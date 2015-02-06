from package.model import grammar as g
import rhinoscriptsyntax as rs

g.Grammar.clear_all()
point = rs.GetPoint("Click somewhere")
print("point: %s" % point)
print("len(point): %i" % len(point))
print("point[0], point[1], point[2]: %i, %i, %i" % (
    point[0], point[1], point[2]))
# print("rs.IsObject(point): %s" % rs.IsObject(point))
print("type(point) == list: %s" % (type(point) == list))
print("rs.IsPoint(point): %s" % rs.IsPoint(point))
print("type(point): %s" % type(point))
print("type(point) == Point3d: %s" % (type(point) == 'Point3d'))
print("type(point) == rs.Geometry.Point3d: %s" % (
    type(point) == 'rs.Geometry.Point3d'))
# print("type(point) == rs.Geometry.Point3d: %s" % (
#     type(point) == rs.Geometry.Point3d))
print("point[2]: %s" % point[2])
