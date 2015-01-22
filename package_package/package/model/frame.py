import rhinoscriptsyntax as rs

class Frame(object):
    size = [32, 32, 32]

    def __init__(self):
        pass

    @classmethod
    def new(cls, base_point):
        """Receives:
            position        [num, num, num]
        Draws a shape frame. Returns:
            [guid, ...]     if successful
            None            otherwise
        """
        opposite_point = rs.PointAdd(base_point, cls.size)
        x0, y0, z0 = base_point
        x1, y1, z1 = opposite_point
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
        guids = []
        for pair in point_pairs:
            guid = rs.AddLine(pair[0], pair[1])
            guids.append(guid)
        if len(guids) == len(point_pairs):
            return_value = guids
        else:
            return_value = None
        return return_value
