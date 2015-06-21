from System.Drawing import Color
import rhinoscriptsyntax as rs

class Settings(object):
    dark_gray = Color.FromArgb(105, 105, 105)
    
    default_layer_name = 'Default'
    first_initial_shape_layer_name = 'initial_shape_1'
    first_initial_shape_layer_origin = (0, -40, 0)
    first_rule_layer_name = 'rule_1'
    first_rule_layer_origin = (0, -100, 0)
    frame_base_point = (0, 0, 0)
    frame_color_name = dark_gray
    frame_layer_name = 'frames'
    frame_name = 'frame block'
    frame_block_size = (32, 32, 32)
    layer_color = Color.Black
    layer_tag_offset = (-10, 0, 0)
    layer_tag_text_height = 2
    right_frame_block_offset_factor = 1.5

    def __init__(self):
        pass

    @classmethod
    def get_right_frame_block_origin(cls, left_block_origin):
        """Receives:
            left_block_origin
                            Point3d. The origin of the left frame block
        Returns:
            right_block_origin
                            Point3d. The origin of the right frame block
        """
        frame_block_side_x = cls.frame_block_size[0]
        right_block_offset = rs.VectorScale(
            frame_block_side_x, cls.right_frame_block_offset_factor)
        right_block_origin = rs.PointAdd(
            left_block_origin, right_block_offset)
        return right_block_origin
