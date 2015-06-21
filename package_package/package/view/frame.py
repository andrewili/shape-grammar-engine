from package.view import layer as l
import rhinoscriptsyntax as rs
from package.view import settings as s

class Frame(object):
    def __init__(self):
        pass

    @classmethod                                ##  06-22 06:19
    def new_instance(cls, frame_name, layer_name, origin):
        """Receives:
            frame_name      str. The name of the frame block: {
                                <layer name> | 
                                <layer name>_L | 
                                <layer name>_R}
            layer_name      str. The name of the layer containing the frame 
                            block
            origin          Point3D. The origin of the frame block
        Creates a frame block definition, if there is not already one. Inserts 
        a frame block instance at the specified point on the specified layer. 
        Returns:
            guid            the guid of the new frame block instance, if 
                            successful
            None            otherwise
        """
        method_name = 'insert'
        if not cls._definition_exists():
            cls._new_definition()
        rs.CurrentLayer(layer_name)
        frame_name = s.Settings.frame_name
        return_value = rs.InsertBlock(frame_name, origin)
        default_layer_name = s.Settings.default_layer_name
        rs.CurrentLayer(default_layer_name)
        return return_value

    @classmethod
    def _definition_exists(cls):
        """Returns:
            value           boolean. True, if a block definition exists. 
                            False, otherwise
        """
        block_name = s.Settings.frame_name
        value = rs.IsBlock(block_name)
        return value

    @classmethod
    def _new_definition(cls):
        """Creates a frame definition on its own layer. Returns:
            name            str. The name of the frame, if successful
            None            otherwise
        """
        layer_name = s.Settings.frame_layer_name
        color_name = s.Settings.frame_color_name
        rs.AddLayer(layer_name, color_name)
        rs.CurrentLayer(layer_name)
        base_point = s.Settings.frame_base_point
        line_guids = cls._get_guids()
        frame_name = s.Settings.frame_name
        delete_input = True
        actual_frame_name = rs.AddBlock(
            line_guids, base_point, frame_name, delete_input)
        default_layer_name = s.Settings.default_layer_name
        rs.CurrentLayer(default_layer_name)
        layer_names = rs.LayerNames()
        if (
            layer_name in layer_names and
            actual_frame_name == frame_name
        ):
            return_value = actual_frame_name
        return return_value
        
    @classmethod
    def _get_guids(cls):
        """Receives:
            base_point      (num, num, num)
        Draws a shape frame. Returns:
            line_guids      [guid, ...]. A list of the guids of the lines in 
                            the frame, if successful
            None            otherwise
        """
        base_point = (0, 0, 0)
        opposite_point = rs.PointAdd(base_point, s.Settings.frame_block_size)
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
        if len(line_guids) == len(point_pairs):
            return_value = line_guids
        else:
            return_value = None
        return return_value

    # @classmethod
    # def new(cls):
        # """Creates a frame block definition on a frame block layer. Returns:
        #     name            str. The name of the block, if successful
        #     None            otherwise
        # """
        # if cls._frame_block_exists():
        #     return_value = None
        # else:
        #     layer_name = s.Settings.frame_block_layer_name
        #     color_name = s.Settings.frame_block_color_name
        #     base_point = s.Settings.frame_block_base_point
        #     block_name = s.Settings.frame_block_name
        #     default_layer = s.Settings.default_layer_name
        #     l.Layer.new(layer_name, color_name)
        #     rs.CurrentLayer(layer_name)
        #     line_guids = f.Frame.new(base_point)
        #     delete_input = True
        #     actual_block_name = rs.AddBlock(
        #         line_guids, base_point, block_name, delete_input)
        #     rs.CurrentLayer(default_layer)
        #     layer_names = rs.LayerNames()
        #     if (
        #         layer_name in layer_names and
        #         actual_block_name == block_name
        #     ):
        #         return_value = actual_block_name
        #     else:
        #         return_value = None
        # return return_value

    # @classmethod
    # def delete(cls):                            ##  not needed?
        # """Deletes the frame block and its layer. Returns:
        #     boolean         True if successful; False otherwise
        # """
        # if not (
        #     cls._frame_block_exists() and
        #     l.Layer.layer_name_is_in_use(cls.layer_name)
        # ):
        #     return_value = False
        # else:
        #     block_was_deleted = rs.DeleteBlock(cls.block_name)
        #     guids = rs.ObjectsByLayer(cls.layer_name)
        #     rs.DeleteObjects(guids)
        #     actual_value = l.Layer.delete(cls.layer_name)
        #     expected_value = True
        #     if (
        #         block_was_deleted and
        #         actual_value == expected_value
        #     ):
        #         return_value = True
        #     else:
        #         return_value = False
        # return return_value

    # @classmethod
    # def _frame_block_exists(cls):
        # block_names = rs.BlockNames()
        # return_value = cls.block_name in block_names
        # return return_value

