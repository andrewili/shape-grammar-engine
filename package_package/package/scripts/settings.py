from System.Drawing import Color
import rhinoscriptsyntax as rs

class Settings(object):
    dark_gray = Color.FromArgb(105, 105, 105)
    frame_size = (32, 32, 32)

    arrow_base_point = (0, 0, 0)
    arrow_color_name = dark_gray
    arrow_length = frame_size[0] / 4
    arrow_name = 'arrow'    
    block_instance_filter = 4096    
    block_type = 4096
    curve_filter = 4
    default_layer_name = 'Default'
    first_initial_shape_layer_name = 'initial_shape_1'
    first_initial_shape_frame_position = (0, -40, 0)
    first_rule_layer_name = 'rule_1'
    first_rule_left_frame_position = (60, -40, 0)
    frame_base_point = (0, 0, 0)                ##  Point3D
    frame_color_name = dark_gray
    frame_layer_name = 'frames'
    frame_name = 'frame block'
    right_frame_offset_factor = 1.5
    text_dot_filter = 8192

    def __init__(self):
        pass

    @classmethod
    def get_right_frame_position(cls, left_frame_position):
        """Receives:
            left_frame_position
                            Point3d or (num, num, num). The origin of the left 
                            frame block
        Returns:
            right_frame_position
                            Point3d. The origin of the right frame block
        """
        frame_side_x = cls.frame_size[0]
        right_frame_offset_x = (
            frame_side_x * cls.right_frame_offset_factor)
        right_frame_offset = (right_frame_offset_x, 0, 0)
        right_frame_position = rs.PointAdd(
            left_frame_position, right_frame_offset)
        return right_frame_position

    @classmethod
    def get_arrow_position(cls, left_frame_position):
        """Receives:
            left_frame_position
                            Point3d or (num, num, num). The position of the 
                            left frame instance
        Returns:
            arrow_position  Point3d. The center point of the arrow
        """
        frame_gap_factor_x = (cls.right_frame_offset_factor - 1) / 2
        arrow_offset_x = cls.frame_size[0] * (frame_gap_factor_x + 1)
        arrow_offset_y = cls.frame_size[1] / 2
        arrow_offset_z = 0
        arrow_offset = (arrow_offset_x, arrow_offset_y, arrow_offset_z)
        arrow_position = rs.PointAdd(left_frame_position, arrow_offset)
        return arrow_position
