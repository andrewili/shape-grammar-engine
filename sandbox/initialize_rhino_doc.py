#   initialize_rhino_doc.py

import rhinoscriptsyntax as rs

def initialize_layers():
    rs.AddLayer('left')
    rs.AddLayer('right')
    rs.AddLayer('infrastructure')

def initialize_blocks():
    initialize_shape_frame_block()

def initialize_shape_frame_block():
    rs.CurrentLayer('infrastructure')
    x, y, z = [0, 0, 0]
    frame_lines = draw_shape_frame(x, y, z)
    rs.AddBlock(frame_lines, [x, y, z], 'shape frame', True)
    rs.CurrentLayer('Default')

def draw_shape_frame(x0, y0, z0):
    """Draws a shape frame of side = 32 at [x0, y0, z0]
    """
    canvas_side = 32
    dx, dy, dz = canvas_side, canvas_side, canvas_side
    x1, y1, z1 = x0 + dx, y0 + dy, z0 + dz

    p0 = [x0, y0, z0]
    p1 = [x0, y0, z1]
    p2 = [x0, y1, z0]
    p3 = [x0, y1, z1]
    p4 = [x1, y0, z0]
    p5 = [x1, y0, z1]
    p6 = [x1, y1, z0]
    p7 = [x1, y1, z1]

    point_pairs = [
        (p0, p1), (p0, p2), (p0, p4), (p1, p3), (p1, p5), (p2, p3), 
        (p2, p6), (p3, p7), (p4, p5), (p4, p6), (p5, p7), (p6, p7)]

    lines = []
    for point_pair in point_pairs:
        lines.append(rs.AddLine(point_pair[0], point_pair[1]))
    return lines

def insert_rule_frames():
    rs.CurrentLayer('infrastructure')
    rs.InsertBlock('shape frame', [0, 0, 0])
    rs.InsertBlock('shape frame', [50, 0, 0])
    rs.CurrentLayer('Default')

initialize_layers()
initialize_blocks()
insert_rule_frames()
