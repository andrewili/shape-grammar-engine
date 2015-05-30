import rhinoscriptsyntax as rs

class LabeledShape(object):
    def __init__(self):
        pass

    @classmethod                                ##  05-26 08:54
    def get_spec_from_lshape_guids(cls, lshape_guids, origin):
        """Receives:
            lshape_guids    [guid, ...]. A list of the guids of the elements 
                            in the labeled shape, i.e., name, lines, labeled 
                            points, frame
            origin          Point3d. The labeled shape's local origin
        Returns:
            lshape_spec     (name, [line_spec, ...], [lpoint_spec]). The 
                            labeled shape's (relative) spec
        """
        line_guids, lpoint_guids, text_guids, frame_guids = (
            cls.classify_guids(lshape_guids))
        relative_line_specs = []
        for line_guid in line_guids:
            relative_line_spec = (
                cls.get_relative_spec_from_line_guid(line_guid))
            relative_line_specs.append(relative_line_spec)
        relative_lpoint_specs = []
        for lpoint_guid in lpoint_guids:
            label, p = lpoint_guid
            q = cls.get_relative_spec_from_point_guid(p, origin)
            relative_lpoint_spec = (label, q)
            relative_lpoint_specs.append(relative_lpoint_spec)
        lshape_spec = (
            lshape_name,
            sorted(relative_line_specs),
            sorted(relative_lpoint_specs))
        return lshape_spec

    @classmethod
    def classify_guids(cls, guids):             ##  05-28 09:06
        """Receives:
            guids           [guid, ...]. A list of guids
        Classifies the guids by type. Returns:
            (line_guids, lpoint_guids, text_guids, frame_guid)
                            line_guids: [line_guid, ...]
                            lpoint_guids: [lpoint_guid, ...]
                            text_guids: [text_guid, ...]
                            frame_guid
        """
        line_guids, lpoint_guids, text_guids = [], [], []
        line_type, lpoint_type, text_type = 4, 8192, 512
        for guid in guids:
            guid_type = rs.ObjectType(guid)
            if guid_type == line_type:
                line_guids.append(guid)
            elif guid_type == lpoint_type:
                lpoint_guids.append(guid)
            elif guid_type == text_type:
                text_guids.append(guid)
            else:
                pass
        return (line_guids, lpoint_guids, text_guids, frame_guid)

    @classmethod
    def get_end_points(cls, line_guid):
        """Receives:
            line_guid       guid of a line
        Returns:
            tail            Point3d. The lower of the 2 end points
            head            Point3d. The higher of the 2 end points
        """
        p1 = rs.CurveStartPoint(line_guid)
        p2 = rs.CurveEndPoint(line_guid)
        tail, head = cls.direct_lines([p1, p2]) ##  write direct_line method
        return (tail, head)

    @classmethod
    def get_relative_spec_from_point_guid(cls, point, origin): ##  05-29 09:05
        """Receives:
            point           Point3d
        Returns:
            relative_point_spec
                            (num, num, num). The spec of the point, relative
                            to the origin
        """
        pass
