#	rhino-drawing-scratch.py

import rhinoscriptsyntax as rs

def draw_offset_line(p1, p2, offset_vector):
	p1a = map(offset_coord, p1, offset_vector)
	p2a = map(offset_coord, p2, offset_vector)
	rs.AddLine(p1a, p2a)

def offset_coord(coord, offset):
	return coord + offset

def draw_rhino():
	p00 = [0, 0, 0]
	p01 = [0, 10, 0]
	p10 = [10, 0, 0]
	p11 = [10, 10, 0]
	offset_vector = [4, 1, 0]

	draw_offset_line(p00, p01, offset_vector)
	draw_offset_line(p00, p10, offset_vector)
	draw_offset_line(p01, p11, offset_vector)
	draw_offset_line(p10, p11, offset_vector)

draw_rhino()