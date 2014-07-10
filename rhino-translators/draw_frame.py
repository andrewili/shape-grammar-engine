#	draw_frame.py

import rhinoscriptsyntax as rs

def draw_frame():
	side = 31
	x0 = 1
	y0 = 0
	x1 = x0 + side
	y1 = y0 + side
	z = 0
	p00 = [x0, y0, z]
	p01 = [x0, y1, z]
	p10 = [x1, y0, z]
	p11 = [x1, y1, z]
	rs.AddLine(p00, p01)
	rs.AddLine(p00, p10)
	rs.AddLine(p01, p11)
	rs.AddLine(p10, p11)
    # rs.AddPlane(p00, p11)

draw_frame()
