import rhinoscriptsyntax as rs

td = rs.AddTextDot('x', [10, 10, 0])
p = rs.TextDotPoint(td)
t = rs.TextDotText(td)

print("type(td): %s" % type(td))
print("t: %s" % t)
print("p: %s" % p)
print("type(p): %s" % type(p))
print("len(p): %i" % len(p))
print("p is list: %s" % (type(p) == list))
print("p is tuple: %s" % (type(p) == tuple))
p_tuple = tuple(p)
print("type(p_tuple): %s" % type(p_tuple))
print(p_tuple)
# print("p coordinates: %s" % rs.PointCoordinates(p))
print("td coordinates: %s" % rs.PointCoordinates(td))   ##  None