from package.model import block as b
from package.model import frame as f
from package.model import frame_block as fb
from package.model import layer as l
import rhinoscriptsyntax as rs

class RuleFrameBlock(b.Block):                  ##  based on Block
    block_name = 'rule frame block'

    def __init__(self):
        pass

    @classmethod
    def new(cls):
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
            rs.CurrentLayer(fb.FrameBlock.layer_name)
            frame_guids = f.Frame.new()
            base_point = [0, 0, 0]
            delete_input = True
            return_value = rs.AddBlock(
                frame_guids, base_point, cls.block_name, delete_input)
            rs.CurrentLayer('Default')
        return return_value

    # @classmethod
    # def delete(cls):
    #     """
    #     """
    #     print("Pretending to delete the rule frame block")
