from package.model import block as b
from package.model import frame as f
from package.model import frame_block as fb
from package.model import layer as l
import rhinoscriptsyntax as rs

class RuleFrameBlock(b.Block):                  ##  child class of Block
    block_name = 'rule frame block'

    def __init__(self):
        pass

    @classmethod
    def new(cls):                               ##  Came from 
                                                ##  Grammar._set_up
        """Draws a rule frame block on the frames layer and converts it to a
        block. Returns:
            str             the name of the block, if successful
            None            otherwise
        """
        frames_layer_exists = l.Layer.layer_name_is_in_use(
            fb.FrameBlock.layer_name)
        if not frames_layer_exists:
            return_value = None
        else:
            rs.CurrentLayer(b.Block.layer_name)
            size = [32, 32, 32]
            gap = 16
            x0, y0, z0 = [0, 0, 0]
            offset = [size[0] + gap, 0, 0]
            left_frame_position = [x0, y0, z0]
            right_frame_position = rs.PointAdd(left_frame_position, offset)
            left_frame_guids = f.Frame.new(left_frame_position)
            right_frame_guids = f.Frame.new(right_frame_position)
            frame_guids = left_frame_guids
            frame_guids.append(right_frame_guids)
            # create block: Block.new()
            base_point = [0, 0, 0]
            delete_input = True
            return_value = b.Block.new(         ##  gone drilling
                frame_guids, base_point, cls.block_name, delete_input)
            # set layer
            rs.CurrentLayer('Default')
        return return_value

    # @classmethod
    # def delete(cls):
    #     """
    #     """
    #     print("Pretending to delete the rule frame block")
