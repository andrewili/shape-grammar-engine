#	draw_sierpinski_3d.py

import rhinoscriptsyntax as rs

def draw_sierpinski_3d():
	rs.AddLine([0, 0, 0], [0, 18, 0])
	rs.AddLine([0, 0, 0], [18, 0, 0])
	rs.AddLine([0, 18, 0], [18, 0, 0])
	rs.AddLine([0, 0, 0], [0, 0, 24])
	rs.AddLine([0, 0, 24], [0, 18, 0])
	rs.AddLine([0, 0, 24], [18, 0, 0])
	rs.AddTextDot('a', [6, 6, 8])

	rs.AddLine([0, 0, 12], [0, 9, 0])
	rs.AddLine([0, 0, 12], [9, 0, 0])
	rs.AddLine([0, 9, 0], [9, 0, 0])
	rs.AddTextDot('a', [3, 3, 4])

	rs.AddLine([0, 9, 0], [0, 9, 12])
	rs.AddLine([0, 9, 0], [9, 9, 0])
	rs.AddLine([0, 9, 12], [9, 9, 0])
	rs.AddTextDot('a', [3, 12, 4])

	rs.AddLine([9, 0, 0], [9, 0, 12])
	rs.AddLine([9, 0, 0], [9, 9, 0])
	rs.AddLine([9, 0, 12], [9, 9, 0])
	rs.AddTextDot('a', [12, 3, 4])

	rs.AddLine([0, 0, 12], [0, 9, 12])
	rs.AddLine([0, 0, 12], [9, 0, 12])
	rs.AddLine([0, 9, 12], [9, 0, 12])
	rs.AddTextDot('a', [3, 3, 16])

draw_sierpinski_3d()
