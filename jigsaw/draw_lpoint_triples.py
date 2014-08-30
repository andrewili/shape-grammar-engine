#   draw_lpoint_triples.py

import rhinoscriptsyntax as rs

def draw_lpoint_triples():
    """Prompts for label text and a point triple (or a line segment + 3rd 
    point) to identify line segments. Draws lpoint triples
    """
    offset = 0.1

    def get_points():
        """Prompts for a point triple. Returns a list of the points:
            [<iter>, ...]
        """
        points = rs.GetPoints(
            draw_lines=False, in_plane=False, 
            message1='Select tail, head, side', message2=None, 
            max_points=3, base_point=None)
        return points

    def draw_lpoint_triple(points):
        """Receives label text and a list of point triples:
            str
            [<iter>, ...]
        Draws text dots with <text>-a, -b, -c
        """
        text = 'r1'
        tail, head, side = points
        vector = rs.PointSubtract(head, tail)
        lpoint_tail = rs.VectorAdd(tail, vector * offset)
        lpoint_head = rs.VectorSubtract(head, vector * offset)
        tail_vector = rs.VectorSubtract(lpoint_tail, tail)
        lpoint_side = rs.VectorRotate(tail_vector, 0, [0, 0, 1])
        # label_side = rs.VectorAdd(tail, right-vector * offset)
        rs.AddTextDot(('%s-t' % text), lpoint_tail)
        rs.AddTextDot(('%s-h' % text), lpoint_head)
        rs.AddTextDot(('%s-s' % text), lpoint_side)

    points = get_points()
    draw_lpoint_triple(points)

draw_lpoint_triples()
