#	draw_shape_test.py

import rhinoscriptsyntax as rs
import importer
import shape

importer_drone = importer.Importer()

def make_sierpinski_init():
	name = 'sierpinski-init'
	line_specs = [
		((0, 0, 0), (0, 0, 24)),
		((0, 0, 0), (0, 18, 0)),
		((0, 0, 0), (18, 0, 0)),
		((0, 0, 12), (0, 9, 0)),
		((0, 0, 12), (0, 9, 12)),
		((0, 0, 12), (9, 0, 0)),
		((0, 0, 12), (9, 0, 12)),
		((0, 0, 24), (0, 18, 0)),
		((0, 0, 24), (18, 0, 0)),
		((0, 9, 0), (0, 9, 12)),
		((0, 9, 0), (9, 0, 0)),
		((0, 9, 0), (9, 9, 0)),
		((0, 9, 12), (9, 0, 12)),
		((0, 9, 12), (9, 9, 0)),
		((0, 18, 0), (18, 0, 0)),
		((9, 0, 0), (9, 0, 12)),
		((9, 0, 0), (9, 9, 0)),
		((9, 0, 12), (9, 9, 0))]
	lpoint_specs = [
		((3, 12, 4), 'a'),
		((3, 3, 16), 'a'),
		((3, 3, 4), 'a'),
		((6, 6, 8), 'a'),
		((12, 3, 4), 'a')]
	shape_out = shape.Shape(name, line_specs, lpoint_specs)
	return shape_out

sierpinski_init = make_sierpinski_init()
importer_drone._draw_shape(sierpinski_init)
