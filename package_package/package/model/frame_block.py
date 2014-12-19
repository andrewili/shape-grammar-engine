from package.model import block as b
from package.model import frame as f
from package.model import layer as l
import rhinoscriptsyntax as rs

class FrameBlock(object):
    def __init__(self):
        pass

    @classmethod
    def new(cls):
        """Creates a frame layer, draws a shape frame there, and converts it
        to a block. Returns the name of the block:
            str
        """
        layer_name = l.Layer.new('Frame', 'dark gray')
        frame = f.Frame.new(layer_name)
        new_block_name = b.Block.new(frame, [0, 0, 0], 'frame')
        print('Pretended to create a frame block')
        return new_block_name

    @classmethod
    def _draw_frame(cls, layer_name):
        """Receives a layer name:
            str
        Draws a frame on the named layer. Returns the lines:
            [guid, ...]
        """
        guids = []
        print('Pretended to draw a frame')
        return guids

    @classmethod
    def delete(cls):
        """Deletes the frame block and its layer. Returns the success value:
            boolean
        """
        success = False
        block_name = 'Frame'
        layer_name = 'Frames'
        block_names = rs.BlockNames()
        if block_name not in block_names:
            message = 'No such frame'
            block_was_deleted = False
        else:
            block_was_deleted = rs.DeleteBlock(block_name)
            layer_was_purged = rs.PurgeLayer(layer_name)  ##  why not use Layer object?
        if block_was_deleted and layer_was_purged:
            success = True
            message = 'Deleted the frame block and its layer'
        else:
            message = 'Did not delete both the frame block and its layer'
        print(message)
        return success