import rhinoscriptsyntax as rs

p = rs.AddPoint(10, 10, 10)
q = (10, 10, 10)

coords_p = rs.PointCoordinates(p)
# x, y, z = p                                     ##  "not iterable"
p_plus_q = rs.PointAdd(p, q)
# coords_p_plus_q = rs.PointCoordinates(p_plus_q) ##  "must be a guid"

print("p: %s" % p)                              ##  guid
print("type(p): %s" % type(p))                  ##  guid
print("type(q): %s" % type(q))                  ##  tuple
print("coords_p: %s" % coords_p)                ##  10,10,10
print("type(coords_p): %s" % type(coords_p))    ##  Point3d
# print("tuple(p): %s" % tuple(p))
print("type(p_plus_q): %s" % type(p_plus_q))    ##  Point3d
print("p_plus_q: %s" % p_plus_q)                ##  30,30,30
print("p_plus_q[0]: %s" % p_plus_q[0])          ##
print("p_plus_q[1]: %s" % p_plus_q[1])          ##
print("p_plus_q[2]: %s" % p_plus_q[2])          ##
# print("coords_p_plus_q: %s" % coords_p_plus_q)                ##  
# print("p == q" % p == q)
print("rs.PointCompare(p, q): %s" % rs.PointCompare(p, q))
# print("coords_p == q" % coords_p == q)
# print("rs.PointCompare(coords_p, q)" % rs.PointCompare(coords_p, q))
# print("len(p) = %i"% len(p))
# print('tuple(coords_p) %s' % tuple(coords_p))
print('p[x]: %s' % coords_p[0]) 				##  10.0

print('rs.IsPoint(p): %s' % rs.IsPoint(p)) 		##	True
print('rs.IsPoint(coords_p): %s' % rs.IsPoint(coords_p))
												##	False
print(coords_p)									##	10,10,10
xyz = tuple(coords_p)
print(xyz) 										##	(10.0, 10.0, 10.0)
print('coords_p_x = %s' % coords_p[0]) 			##	10.0
