# from package.model import block as b
from package.model import frame as f
from package.model import layer as l
import rhinoscriptsyntax as rs

class FrameBlock(object):
    layer_name = 'frames'
    color_name = 'dark gray'

    def __init__(self):
        pass

    @classmethod
    def new(cls):                               ##  called by 
                                                ##  Grammar._clear_settings()
        """Creates a frame layer, draws a shape frame there, and converts the
        shape frame to a block. Returns:
            str             the name of the block, if successful
        """
        l.Layer.new(cls.layer_name, cls.color_name)
        frame_guids = f.Frame.new(cls.layer_name)
        base_point = [0, 0, 0]
        block_name = 'frame block'
        actual_block_name = rs.AddBlock(frame_guids, base_point, block_name)
        return actual_block_name

    @classmethod
    def delete(cls):
        """Deletes the frame block and its layer. Returns:
            boolean         True if successful; False otherwise
        """
        rs.DeleteBlock(cls.layer_name)
        l.Layer.delete(cls.layer_name)          ##  You are here

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

