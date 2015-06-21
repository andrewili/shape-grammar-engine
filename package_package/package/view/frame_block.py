from package.view import frame as f
from package.view import layer as l
import rhinoscriptsyntax as rs
from package.view import settings as s

class FrameBlock(object):
    def __init__(self):
        pass

    @classmethod
    def insert_instance(cls, block_name, layer_name, origin):
        """Receives:
            block_name      str. The name of the frame block: {
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
        block_name = s.Settings.frame_block_name
        return_value = rs.InsertBlock(block_name, origin)
        default_layer_name = s.Settings.default_layer_name
        rs.CurrentLayer(default_layer_name)
        return return_value

    @classmethod
    def _definition_exists(cls):
        """Returns:
            value           boolean. True, if a block definition exists. 
                            False, otherwise
        """
        block_name = s.Settings.frame_block_name
        value = rs.IsBlock(block_name)
        return value

    @classmethod
    def _new_definition(cls):
        """Creates a frame block definition on its own layer. Returns:
            name            str. The name of the block, if successful
            None            otherwise
        """
        layer_name = s.Settings.frame_block_layer_name
        color_name = s.Settings.frame_block_color_name
        rs.AddLayer(layer_name, color_name)
        rs.CurrentLayer(layer_name)
        base_point = s.Settings.frame_block_base_point
        line_guids = f.Frame.new(base_point)
        block_name = s.Settings.frame_block_name
        delete_input = True
        actual_block_name = rs.AddBlock(
            line_guids, base_point, block_name, delete_input)
        default_layer_name = s.Settings.default_layer_name
        rs.CurrentLayer(default_layer_name)
        layer_names = rs.LayerNames()
        if (
            layer_name in layer_names and
            actual_block_name == block_name
        ):
            return_value = actual_block_name
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

