from package.view import grammar as g
import rhinoscriptsyntax as rs

class LabeledShape(object):
    def __init__(self):
        pass

    @classmethod                                ##  06-21 09:04
    def set_up(
        cls, component_name, component_base_point, lshape_type
    ):
        """Receives:
            component_name  str. The name of the initial shape or rule
            component_base_point
                            Point3d. The base point of the initial shape or 
                            rule
            lshape_type     str: {'initial' | 'left' | 'right'}. The group of 
                            the labeled shape
        Inserts a frame block. Assigns it to the appropriate lshape group. 
        Returns:
            lshape_name     str. The name of the labeled shape: <initial shape 
                            name> or <rule name>_L or <rule name>_R
        """
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

    @classmethod
    def get_string_from_named_lshape(cls, named_lshape):    ##  06-18 09:25
        """Receives:
            name            str. The name of a labeled shape of either an 
                            initial shape or a rule, i.e., either 
                            <ishape_name> or <rule_name>_L or <rule_name>_R. 
                            Type and value guaranteed
        Returns:
            named_lshape_string
                            str. The .is string of the labeled shape
        """
        named_lshape_string = 'kilroy'
        return named_lshape_string


    @classmethod
    def get_frame_position_from_labeled_shape_name(cls, name):  ##  06-19 16:27
        """Receives:
            name            str. The name of a labeled shape, i.e., <ishape>,
                            <rule>_L, or <rule>_R
        Returns:
            position        Point3d. The location of the frame block's origin
        """
        block = cls.get_frame_block()
        position = get_position(block)
        return position

    @classmethod
    def get_frame_block(cls):
        """Returns:
            block           guid. The guid of the labeled shape's frame block
        """
        layer_items = get_items_on_this_layer()
        frame_blocks_on_this_layer = get_frame_blocks(layer_items)
        return block
        

    @classmethod
    def name_is_available(cls, labeled_shape_name): ##  06-20 09:13
        """Receives:
            labeled_shape_name
                            str. The name of an initial shape or either of a 
                            rule's shapes
        Returns:
            value           boolean. True, if the name is available. False, 
                            otherwise
        """
        layer_name = cls._extract_layer_name(labeled_shape_name)
        initial_shape_names = g.Grammar.get_initial_shapes()
        rule_names = g.Grammar.get_rules()
        value = not (
            layer_name in initial_shape_names or
            layer_name in rule_names)
        return value

    @classmethod
    def _extract_layer_name(cls, labeled_shape_name):
        """Receives:
            labeled_shape_name
                            str. The name of a labeled shape
        Returns:
            layer_name      str. The name of the labeled shape's layer 
        """
        if labeled_shape_name[-2:] == '_L':
            layer_name = labeled_shape_name[:-2]
        elif labeled_shape_name[-2:] == '_R':
            layer_name = labeled_shape_name[:-2]
        else:
            layer_name = labeled_shape_name
        return layer_name


