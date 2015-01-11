# from package.model import block as b
from package.model import frame as f
from package.model import layer as l
import rhinoscriptsyntax as rs

class FrameBlock(object):
    base_point = [0, 0, 0]
    block_name = 'frame block'
    color_name = 'dark gray'
    layer_name = 'frames'

    def __init__(self):
        pass

    @classmethod
    def new(cls):                               ##  called by 
                                                ##  Grammar._clear_settings()
        """Creates a frame layer, draws a shape frame there, and converts the
        shape frame to a block. Returns:
            str             the name of the block, if successful
            None            otherwise
        """
        if cls._frame_block_exists():
            return_value = None
        else:
            l.Layer.new(cls.layer_name, cls.color_name)
            rs.CurrentLayer('frames')
            frame_guids = f.Frame.new()
            actual_block_name = rs.AddBlock(
                frame_guids, cls.base_point, cls.block_name)
            rs.CurrentLayer('Default')
            layer_names = rs.LayerNames()
            if (
                cls.layer_name in layer_names and
                actual_block_name == cls.block_name
            ):
                return_value = actual_block_name
            else:
                return_value = None
        return return_value

    @classmethod
    def delete(cls):                            ##  Came from 
                                                ##  Grammar._clear_settings()
        """Deletes the frame block and its layer. Returns:
            boolean         True if successful; False otherwise
        """
        if not cls._frame_block_exists():
            return_value = False
        else:
            block_was_deleted = rs.DeleteBlock(cls.block_name)
            layer_was_deleted = l.Layer.delete(cls.layer_name)
            if (
                block_was_deleted and
                layer_was_deleted
            ):
                return_value = True
            else:
                return_value = False
        return return_value

    @classmethod
    def _frame_block_exists(cls):
        block_names = rs.BlockNames()
        return_value = cls.block_name in block_names
        return return_value

    # @classmethod
    # def delete(cls):
    #     """Deletes the frame block and its layer. Returns the success value:
    #         boolean
    #     """
    #     block_was_deleted = False
    #     no_such_block = False
    #     block_name = 'Frame'
    #     block_names = b.Block.get_names()
    #     if not block_name in block_names:
    #         no_such_block = True
    #     if no_such_block == True:
    #         message = 'No frame block to delete'
    #     else:
    #         block_was_deleted = b.Block.delete(block_name)
    #         if block_was_deleted:
    #             message = 'Deleted frame block'
    #         else:
    #             message = "Didn't delete frame block"
    #     print(message)
    #     return block_was_deleted

    # @classmethod
    # def _draw_frame(cls, layer_name):
    #     """Receives a layer name:
    #         str
    #     Draws a frame on the named layer. Returns the lines:
    #         [guid, ...]
    #     """
    #     guids = []
    #     print('Pretended to draw a frame')
    #     return guids

