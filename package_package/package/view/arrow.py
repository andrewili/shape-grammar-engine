import rhinoscriptsyntax as rs
from package.view import settings as s

class Arrow(object):
    def __init__(self):
        pass

    @classmethod
    def new_instance(cls, position, layer_name):
        """Receives:
            position        Point3d or (num, num, num). The center point of 
                            the arrow
            layer_name      str. The name of the layer to contain the arrow 
                            instance
        Returns:
            instance        guid. The guid of the new arrow instance, if 
                            successful. None otherwise
        """
        if not cls._definition_exists():
            cls._new_definition()
        rs.CurrentLayer(layer_name)
        arrow_name = s.Settings.arrow_name
        return_value = rs.InsertBlock(arrow_name, position)
        default_layer_name = s.Settings.default_layer_name
        rs.CurrentLayer(default_layer_name)
        return return_value

    @classmethod
    def _definition_exists(cls):
        """Returns:
            value           boolean. True, if an arrow definition exists. 
                            False, otherwise
        """
        arrow_name = s.Settings.arrow_name
        value = rs.IsBlock(arrow_name)
        return value

    @classmethod
    def _new_definition(cls):
        """Creates an arrow definition on its own layer. Returns:
            name            str. The name of the arrow, if successful. None 
                            otherwise
        """
        layer_name = s.Settings.arrow_name
        color_name = s.Settings.arrow_color_name
        rs.AddLayer(layer_name, color_name)
        rs.CurrentLayer(layer_name)
        base_point = s.Settings.arrow_base_point
        line_guids = cls._get_guids(base_point)
        arrow_name = s.Settings.arrow_name
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
        return return_value

    @classmethod
    def _get_guids(cls, base_point):
        """Receives:
            base_point      Point3d or (num, num, num). The base point of the 
                            arrow
        Draws an arrow. Returns:
            guids           [guid]. A list of the guids of the lines in the 
                            arrow, if successful. None otherwise
        """
        x0, y0, z0 = base_point
        half_length = s.Settings.arrow_length / 2
        quarter_length = s.Settings.arrow_length / 4
        p0 = [x0 - half_length, 0, 0]
        p1 = [x0 + quarter_length, quarter_length, 0]
        p2 = [x0 + quarter_length, -quarter_length, 0]
        p3 = [x0 + half_length, 0, 0]
        point_pairs = [(p0, p3), (p1, p3), (p2, p3)]
        line_guids = []
        for pair in point_pairs:
            guid = rs.AddLine(pair[0], pair[1])
            line_guids.append(guid)
        if len(line_guids) == len(point_pairs):
            return_value = line_guids
        else:
            return_value = None
        return return_value
