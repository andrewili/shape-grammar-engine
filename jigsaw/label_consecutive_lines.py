#   label_consecutive_lines.py

import rhinoscriptsyntax as rs

def label_consecutive_lines():
    """Prompts for label text and a point triple (or a line segment + 3rd 
    point) to identify line segments. Draws scalene lpoint triples, which 
    have no reflections.
    """
    offset = 0.1

    def get_points():
        """Prompts for a point triple. Returns a list of the points:
            [<iter>, ...]
        """
        points = rs.GetPoints(
            draw_lines=False, in_plane=False, 
            message1='Select first tail', message2='Select heads', 
            max_points=None, base_point=None)
        return points

    def draw_lpoint_triple(text, tail, head):
        """Receives label text and a list of point triples:
            str
            [<iter>, ...]
        Draws text dots with <text>-a, -b, -c
        """
        line_vector = rs.PointSubtract(head, tail)
        offset_vector = line_vector * offset
        offset_tail = rs.VectorAdd(tail, offset_vector)
        offset_head = rs.VectorSubtract(head, offset_vector)
        axis = [0, 0, 1]
        angle = 90
        rotated_offset_vector = rs.VectorRotate(offset_vector, angle, axis)
        offset_side = rs.VectorAdd(offset_tail, rotated_offset_vector)
        rs.AddTextDot(('%s-a' % text), offset_tail)
        rs.AddTextDot(('%s-b' % text), offset_head)
        rs.AddTextDot(('%s-c' % text), offset_side)

    def side_is_same_as_rule(point):
        """Receives a point (i.e., a list):
            [num, num, num]
        Returns whether the point is on the same side as the side label in the
        rule
        """
        return False
        
    points = get_points()
    text = rs.StringBox('Enter label text')
    for i in range(len(points) - 1):
    # for point in points:
        tail = points[i]
        head = points[i + 1]
        draw_lpoint_triple(text, tail, head)

label_consecutive_lines()
