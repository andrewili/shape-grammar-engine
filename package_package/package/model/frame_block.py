from package.model import block as b
from package.model import frame as f
import rhinoscriptsyntax as rs

# from package.model import layer as l

class FrameBlock(object):
    def __init__(self):
        pass

    @classmethod
    def new(cls):
        """Creates a frame layer, draws a shape frame there, and converts the
        shape frame to a block. Returns the name of the block:
            str
        """
        layer_name = l.Layer.new('Frames', 'dark gray')
        # frame = f.Frame.new(layer_name)
        # origin = [0, 0, 0]
        # new_block_name = b.Block.new(frame, origin, 'frame')
        # if new_block_name:
        #     print('Added frame block')
        # return new_block_name

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
