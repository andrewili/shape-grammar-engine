import rhinoscriptsyntax as rs
from package.scripts import settings as s

class DoubleArrow(object):
    def __init__(self):
        pass

    @classmethod
    def new_instance(cls, position):
        """Receives:
            position        Point3d or (num, num, num). The center point of 
                            the arrow
        Creates a double arrow definition, if there is not one already. 
        Inserts an instance at the specified location on the specified layer. 
        Returns:
            return_value    guid. The guid of the new instance if successful. 
                            None otherwise
        """
        if not cls._definition_exists():
            cls._new_definition()
        arrow_name = s.Settings.double_arrow_name
        return_value = rs.InsertBlock(arrow_name, position)
        return return_value

    @classmethod
    def _definition_exists(cls):
        """Returns:
            value           boolean. True, if a double arrow definition 
                            exists. False, otherwise
        """
        arrow_name = s.Settings.double_arrow_name
        value = rs.IsBlock(arrow_name)
        return value

    @classmethod
    def _new_definition(cls):
        """Creates a new double arrow definition on its own layer. Returns:
            name            str. The name of the definition, if successful. 
                            None otherwise
        """
        layer_name = s.Settings.double_arrow_name
        color_name = s.Settings.double_arrow_color_name
        rs.AddLayer(layer_name, color_name)
        rs.CurrentLayer(layer_name)
        base_point = s.Settings.double_arrow_base_point
        line_guids = cls._get_guids(base_point)
        arrow_name = s.Settings.double_arrow_name
        delete_input = True
        actual_arrow_name = rs.AddBlock(
            line_guids, base_point, arrow_name, delete_input)
        default_layer_name = s.Settings.default_layer_name
        rs.CurrentLayer(default_layer_name)
        layer_names = rs.LayerNames()
        if (layer_name in layer_names and
            actual_arrow_name == arrow_name
        ):
            return_value = actual_arrow_name
        else:
            return_value = None
        return return_value

    @classmethod
    def _get_guids(cls, base_point):
        """Receives:
            base_point      Point3d or (num, num, num). The base point of the 
                            arrow
        Draws an arrow. Returns:
            guids           [guid]. A list of the guids of the lines in the 
                            double arrow, if successful. None otherwise
        """
        xo, yo, zo = base_point
        half_length = s.Settings.double_arrow_length / 2.0
        quarter_length = s.Settings.double_arrow_length / 4.0
        sixteenth_length = s.Settings.double_arrow_length / 16.0
        p0 = [xo - half_length, yo - sixteenth_length, zo]
        p1 = [xo - half_length, yo + sixteenth_length, zo]
        p2 = [xo + quarter_length, yo - quarter_length, zo]
        p3 = [xo + quarter_length, yo + quarter_length, zo]
        p4 = [xo + half_length - sixteenth_length, yo - sixteenth_length, zo]
        p5 = [xo + half_length - sixteenth_length, yo + sixteenth_length, zo]
        p6 = [xo + half_length, yo, zo]
        point_pairs = [(p0, p4), (p1, p5), (p2, p6), (p3, p6)]
        line_guids = []
        for pair in point_pairs:
            guid = rs.AddLine(pair[0], pair[1])
            line_guids.append(guid)
        if len(line_guids) == len(point_pairs):
            return_value = line_guids
        else:
            return_value = None
        return return_value

