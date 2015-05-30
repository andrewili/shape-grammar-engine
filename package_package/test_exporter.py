from package.view import frame_block as fb
from package.view import grammar as g
from package.view import initial_shape as ish
from package.view import rule as r
from package.view import shape_layer as sl
import rhinoscriptsyntax as rs

### utility methods
def draw_small_grammar():                       ##  05-24 11:49
    set_up()
    draw_ishape_sierpinski_triangle()
    draw_ishape_hash()
    draw_rule_subdivide_sierpinski_triangle()
    draw_rule_delete_labeled_point()

def set_up():
    g.Grammar.clear_all()
    fb.FrameBlock.new()

def draw_ishape_sierpinski_triangle():
    sierpinski_triangle_spec = (
        [   ((0, 0, 0), (12, 0, 0)),
            ((0, 0, 0), (0, 16, 0)),
            ((0, 16, 0), (12, 0, 0))],
        [('x', (2, 2, 0))])
    name = 'sierpinski_triangle'
    position = (0, 0, 0)
    sl.ShapeLayer.new(name, position)
    ish.InitialShape._record(name)
    draw_labeled_shape(
        sierpinski_triangle_spec,
        name,
        position)

def draw_ishape_hash():
    hash_spec = (
        [   ((0, 10, 0), (30, 10, 0)),
            ((0, 20, 0), (30, 20, 0)),
            ((10, 0, 0), (10, 30, 0)),
            ((20, 0, 0), (20, 30, 0))],
        [])
    name = 'hash'
    position = (0, 50, 0)
    sl.ShapeLayer.new(name, position)
    ish.InitialShape._record(name)
    draw_labeled_shape(
        hash_spec,
        name,
        position)

def draw_rule_subdivide_sierpinski_triangle():
    sierpinski_triangle = (
        [   ((0, 0, 0), (12, 0, 0)),
            ((0, 0, 0), (0, 16, 0)),
            ((0, 16, 0), (12, 0, 0))],
        [('x', (2, 2, 0))])
    sierpinski_triangle_subdivided = (
        [   ((0, 0, 0), (0, 16, 0)),
            ((0, 0, 0), (12, 0, 0)),
            ((0, 8, 0), (6, 0, 0)),
            ((0, 8, 0), (6, 8, 0)),
            ((0, 16, 0), (12, 0, 0)),
            ((6, 0, 0), (6, 8, 0))],
        [   ('x', (1, 1, 0)),
            ('x', (1, 9, 0)),
            ('x', (7, 1, 0))])
    name = 'subdivide_sierpinski_triangle'
    position = (0, -50, 0)
    r.Rule._new(name, position)
    draw_rule(
        sierpinski_triangle,
        sierpinski_triangle_subdivided,
        name,
        position)

def draw_rule_delete_labeled_point():
    labeled_point = ([], [('x', (16, 16, 0))])
    empty_shape = ([], [])
    name = 'delete_labeled_point'
    position = (0, -100, 0)
    r.Rule._new(name, position)
    draw_rule(
        labeled_point,
        empty_shape,
        name,
        position)

def draw_rule(left_shape_spec, right_shape_spec, rule_layer, rule_position):
    left_shape_position = rule_position
    right_shape_position = r.Rule._get_right_shape_position(
        left_shape_position)
    left_shape_layer = r.Rule._get_shape_name_from_rule_name(
        rule_layer, 'left')
    right_shape_layer = r.Rule._get_shape_name_from_rule_name(
        rule_layer, 'right')
    draw_labeled_shape(
        left_shape_spec, left_shape_layer, left_shape_position)
    draw_labeled_shape(
        right_shape_spec, right_shape_layer, right_shape_position)

def draw_labeled_shape(lshape_spec, lshape_name, lshape_origin):
    rs.CurrentLayer(lshape_name)
    line_specs, lpoint_specs = lshape_spec
    for spec in line_specs:
        draw_line(spec, lshape_origin)
    for spec in lpoint_specs:
        draw_lpoint(spec, lshape_origin)
    rs.CurrentLayer('Default')

def draw_line(spec, lshape_origin):
    p1, p2 = spec
    q1 = rs.PointAdd(p1, lshape_origin)
    q2 = rs.PointAdd(p2, lshape_origin)
    rs.AddLine(q1, q2)

def draw_lpoint(spec, lshape_origin):
    label, p = spec
    q = rs.PointAdd(p, lshape_origin)
    rs.AddTextDot(label, q)


draw_small_grammar()
