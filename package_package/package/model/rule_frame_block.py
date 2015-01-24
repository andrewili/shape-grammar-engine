from package.model import block as b
from package.model import frame as f
from package.model import frame_block as fb
from package.model import layer as l
import rhinoscriptsyntax as rs

class RuleFrameBlock(b.Block):                  ##  child class of Block
    block_name = 'rule frame block'
    left_frame_position = [0, 0, 0]
    gap = 16
    offset = [f.Frame.size[0] + gap, 0, 0]
    right_frame_position = rs.PointAdd(left_frame_position, offset)

    def __init__(self):
        pass

    @classmethod
    def new(cls):
        """Draws a rule frame block on the frames layer and converts it to a
        block. Returns:
            str             the name of the block, if successful
            None            otherwise
        """
        if not cls._frames_layer_exists():
            cls._add_frames_layer()
        rs.CurrentLayer(b.Block.layer_name)
        frame_guids = cls._new_frame_pair()
        return_value = cls._new_block(frame_guids)
        rs.CurrentLayer('Default')
        return return_value

    @classmethod
    def _frames_layer_exists(cls):
        return_value = l.Layer.layer_name_is_in_use(b.Block.layer_name)
        return return_value

    @classmethod
    def _add_frames_layer(cls):
        l.Layer.new(b.Block.layer_name, b.Block.color_name)

    @classmethod
    def _new_frame_pair(cls):
        left_frame_guids = f.Frame.new(cls.left_frame_position)
        right_frame_guids = f.Frame.new(cls.right_frame_position)
        frame_guids = left_frame_guids
        frame_guids.extend(right_frame_guids)
        return frame_guids

    @classmethod
    def _new_block(cls, frame_guids):
        base_point = [0, 0, 0]
        delete_input = True
        return_value = b.Block.new(
            frame_guids, base_point, cls.block_name, delete_input)
        return return_value

    # @classmethod
    # def delete(cls):
    #     """
    #     """
    #     print("Pretending to delete the rule frame block")
