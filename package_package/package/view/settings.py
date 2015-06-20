from System.Drawing import Color
import rhinoscriptsyntax as rs

class Settings(object):
    default_layer_name = 'Default'
    first_initial_shape_name = 'initial_shape_1'
    first_initial_shape_origin = (0, -40, 0)
    first_rule_name = 'rule_1'
    first_rule_lshape_origin = (0, -100, 0)
    frame_block_base_point = (0, 0, 0)
    frame_block_layer_name = 'frames'
    frame_block_color_name = 'dark gray'
    frame_block_name = 'frame block'
    frame_block_size = (32, 32, 32)
    layer_color = Color.Black
    right_lshape_offset_factor = 1.5

    def __init__(self):
        pass

    @classmethod
    def get_right_lshape_position(cls, left_lshape_position):
        """Receives:
            left_lshape_position
                            Point3d. The position of the left rule labeled 
                            shape
        Returns:
            right_lshape_position
                            Point3d. The position of the right rule labeled 
                            shape
        """
        frame_block_side_x = cls.frame_block_size[0]
        right_lshape_offset = rs.VectorScale(
            frame_block_side_x, cls.right_lshape_offset_factor)
        right_lshape_position = rs.PointAdd(
            left_lshape_position, right_lshape_offset)
        return right_lshape_position
