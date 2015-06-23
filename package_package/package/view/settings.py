from System.Drawing import Color
import rhinoscriptsyntax as rs

class Settings(object):
    dark_gray = Color.FromArgb(105, 105, 105)
    
    default_layer_name = 'Default'
    first_initial_shape_layer_name = 'initial_shape_1'
    first_initial_shape_frame_position = (0, -40, 0)
    first_rule_layer_name = 'rule_1'
    first_rule_left_frame_position = (0, -100, 0)
    frame_base_point = (0, 0, 0)
    frame_color_name = dark_gray
    frame_layer_name = 'frames'
    frame_name = 'frame block'
    frame_size = (32, 32, 32)
    layer_color = Color.Black
    layer_tag_offset = (-10, 0, 0)
    layer_tag_text_height = 2
    right_frame_instance_offset_factor = 1.5

    def __init__(self):
        pass

    @classmethod
    def get_right_frame_position(cls, left_instance_origin):
        """Receives:
            left_instance_origin
                            Point3d. The origin of the left frame block
        Returns:
            right_instance_origin
                            Point3d. The origin of the right frame block
        """
        frame_side_x = cls.frame_size[0]
        right_instance_offset_x = (
            frame_side_x * cls.right_frame_instance_offset_factor)
        right_instance_offset = (right_instance_offset_x, 0, 0)
        # right_instance_offset = rs.VectorScale(
        #     frame_side_x, cls.right_frame_instance_offset_factor)
        right_instance_origin = rs.PointAdd(
            left_instance_origin, right_instance_offset)
        return right_instance_origin
