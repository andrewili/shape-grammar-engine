from package.view import layer as l
import rhinoscriptsyntax as rs
from package.view import settings as s

class Frame(object):
    def __init__(self):
        pass

    @classmethod                                ##  done 08-06
    def new_instance(cls, layer_name, position):
        """Receives:
            layer_name      str. The name of an existing layer
            position        Point3d. The position of the frame block
        Creates a frame block definition, if there is not already one. Inserts 
        a frame block instance at the specified position on the specified 
        layer. Returns:
            frame_instance  guid. The guid of the new frame block instance
        """
        (   frame_name,
            default_layer_name
        ) = (
            s.Settings.frame_name,
            s.Settings.default_layer_name)
        if not cls._definition_exists():
            cls._new_definition()
        rs.CurrentLayer(layer_name)
        frame_instance = rs.InsertBlock(frame_name, position)
        rs.CurrentLayer(default_layer_name)
        return frame_instance

    @classmethod                                ##  done 08-06
    def _definition_exists(cls):
        """Returns:
            value           boolean. True, if a frame block definition exists. 
                            False, otherwise
        """
        block_name = s.Settings.frame_name
        value = rs.IsBlock(block_name)
        return value

    @classmethod                                ##  done 08-05
    def _new_definition(cls):
        """Requires:
            A frame definition does not already exist
            A layer named <frame_layer_name> does not already exist
        Creates a frame definition on its own layer. Returns:
            frame_name_out  str. The name of the frame definition
        """
        (   layer_name, 
            color_name
        ) = (
            s.Settings.frame_layer_name, 
            s.Settings.frame_color_name)
        rs.AddLayer(layer_name, color_name)
        rs.CurrentLayer(layer_name)
        (   line_guids, 
            base_point, 
            frame_name_in,
            delete_input
        ) = (
            cls._get_guids(), 
            s.Settings.frame_base_point,
            s.Settings.frame_name,
            True)
        frame_name_out = rs.AddBlock(
            line_guids, base_point, frame_name_in, delete_input)
        (   default_layer_name
        ) = (
            s.Settings.default_layer_name)
        rs.CurrentLayer(default_layer_name)
        return frame_name_out

    @classmethod                                ##  done 08-06
    def _get_guids(cls):
        """Receives:
            base_point      (num, num, num)
        Draws a shape frame. Returns:
            line_guids      [guid, ...]. A list of the guids of the lines in 
                            the frame
        """
        base_point = (0, 0, 0)
        opposite_point = rs.PointAdd(base_point, s.Settings.frame_size)
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
        line_guids = []
        for pair in point_pairs:
            guid = rs.AddLine(pair[0], pair[1])
            line_guids.append(guid)
        return line_guids

    @classmethod                                ##  called
    def get_instance_position(cls, guid):
        """Receives:
            guid            guid. The guid of the frame instance
        Returns:
            position        Point3d. The position of the frame instance
        """
        position = rs.BlockInstanceInsertPoint(guid)
        return position

    @classmethod                                ##  done 08-06
    def get_frame_position_from_user(cls):
        """Returns:
            origin          Point3d. The position of the frame instance. Must 
                            be in the xy plane
        """
        message_1 = "Select a point in the xy plane"
        message_2 = "The point must be in the xy plane. Try again"
        origin = rs.GetPoint(message_1)
        while not origin[2] == 0:
            origin = rs.GetPoint(message_2)
        return origin

