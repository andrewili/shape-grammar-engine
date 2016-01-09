from System.Drawing import Color
import rhinoscriptsyntax as rs

class Settings(object):
    dark_gray = Color.FromArgb(105, 105, 105)
    frame_size = (32, 32, 32)
    font_style_normal = 0
    justified_center = 2

    arrow_base_point = (0, 0, 0)
    arrow_color_name = dark_gray
    arrow_label_offset_from_arrow = (0, 4, 0)   ##  rethink
    arrow_length = frame_size[0] / 4
    arrow_name = 'arrow'    
    block_instance_filter = 4096    
    block_type = 4096
    curve_filter = 4
    default_layer_name = 'Default'
    double_arrow_base_point = (0, 0, 0)
    double_arrow_color_name = dark_gray
    double_arrow_name = 'double_arrow'
    double_arrow_length = frame_size[0]/4
    first_initial_shape_layer_name = 'initial_shape_1'
    first_initial_shape_frame_position = (0, -40, 0)
    first_rule_layer_name = 'rule_1'
    first_rule_left_frame_position = (60, -40, 0)
    frame_base_point = (0, 0, 0)                ##  Point3D
    frame_color_name = dark_gray
    frame_layer_name = 'frames'
    frame_name = 'frame block'
    hatch_annotation_text_height = 1.5
    hatch_annotation_text_offset = (0.5, 0.5, 0)
    hatch_radius = 0.25
    hidden_text_dot_group = 'hidden text dot group'
    right_frame_offset_factor = 1.5
    rule_name_text_height = 2
    rule_name_text_font = 'Arial'
    rule_name_text_font_style = font_style_normal
    rule_name_text_justification = justified_center
    text_dot_filter = 8192

    derivation_array_position = (0, 0, 0)
    derivation_cell_offset_factor_x = 1.5
    derivation_cell_offset_factor_y = 2
    derivation_layer_name = 'derivation'
    derivation_n_columns = 5
    derivation_labeled_shape_offset = (0, 0, 0)
    derivation_arrow_offset = (
        (   (   (   derivation_cell_offset_factor_x - 1) / 
                2) + 
            1) * 
            frame_size[0], 
        frame_size[1] * 0.5, 
        0)
    derivation_rule_name_offset = (
        (   (   (   derivation_cell_offset_factor_x - 1) / 
                2) + 
            1) * 
            frame_size[0], 
        frame_size[1] * 0.75, 
        0)

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
    def get_arrow_position(cls, left_frame_position):       ##  rule arrow
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

    @classmethod
    def get_derivation_cell_position_triples(cls, n_shapes):##  09-21 17:52
        """Receives:
            n_shapes        int >= 2. The number of labeled shapes in the 
                            derivation
        Calculates the positions of labeled shapes, arrows, and rule names 
        arranged in an array. Returns:
            derivation_cell_position_triples
                            [(triple)]. A list of n triples, n = n_shapes, 
                            each of the form:
                                (   labeled_shape_position,
                                    arrow_position, 
                                    rule_name_position)
                            where each position is a triple of the form: 
                                (num, num, num)
        """
        labeled_shape_offset = cls.derivation_labeled_shape_offset
        arrow_offset = cls.derivation_arrow_offset
        rule_name_offset = cls.derivation_rule_name_offset
        cell_positions = (cls._get_derivation_array_cell_positions(n_shapes))
        derivation_cell_position_triples = []
        for i in range(n_shapes):
            derivation_array_cell_position = (
                cell_positions[i])
            labeled_shape_position = rs.PointAdd(
                derivation_array_cell_position,
                labeled_shape_offset)
            arrow_position = rs.PointAdd(
                derivation_array_cell_position,
                arrow_offset)
            rule_name_position = rs.PointAdd(
                derivation_array_cell_position, 
                rule_name_offset)
            position_triple = (
                labeled_shape_position, 
                arrow_position, 
                rule_name_position)
            derivation_cell_position_triples.append(position_triple)
        return derivation_cell_position_triples

    @classmethod
    def _get_derivation_array_cell_positions(cls, n_shapes):
        """Receives:
            n_shapes        int >= 2
        Calculates the position of each cell in the derivation array. Returns:
            derivation_array_cell_positions
                            [(num, num, num)]. A list of n triples of numbers,
                            n = n_shapes
        """
        derivation_array_cell_positions = []
        cell_positions_x = cls._get_derivation_cell_positions_x(n_shapes)
        cell_positions_y = cls._get_derivation_cell_positions_y(n_shapes)
        for i in range(n_shapes):
            x = cell_positions_x[i]
            y = cell_positions_y[i]
            z = 0
            position = (x, y, z)
            derivation_array_cell_positions.append(position)
        return derivation_array_cell_positions

    @classmethod
    def _get_derivation_cell_positions_x(cls, n_shapes):
        """Receives:
            n_shapes        int >= 2. The number of labeled_shapes
        Returns:
            cell_positions_x
                            [num]. A list of the x-coordinates of the 
                            derivation cell positions
        """
        cell_positions_x = []
        n_columns = cls.derivation_n_columns
        frame_width_x = cls.frame_size[0]
        cell_offset_factor_x = cls.derivation_cell_offset_factor_x
        cell_offset_x = frame_width_x * cell_offset_factor_x
        for i in range(n_shapes):
            column_index = i % n_columns
            xi = cell_offset_x * column_index
            cell_positions_x.append(xi)
        return cell_positions_x

    @classmethod
    def _get_derivation_cell_positions_y(cls, n_shapes):
        """Receives:
            n_shapes        int >= 2. The number of labeled shapes
        Returns:
            cell_positions_y
                            [num]. A list of the y-coordinates of the 
                            derivation cell positions
        """
        n_columns = cls.derivation_n_columns
        n_full_rows = n_shapes // n_columns
        n_remaining_shapes = n_shapes % n_columns
        if n_remaining_shapes == 0:
            n_remaining_rows = 0
        else:
            n_remaining_rows = 1
        n_rows = n_full_rows + n_remaining_rows
        first_row_index = n_rows - 1
        n_columns = cls.derivation_n_columns
        frame_height_y = cls.frame_size[1]
        cell_offset_factor_y = cls.derivation_cell_offset_factor_y
        cell_offset_y = frame_height_y * cell_offset_factor_y
        cell_positions_y = []
        for i in range(n_shapes):
            row_index = first_row_index - (i // n_columns)
            yi = cell_offset_y * row_index
            cell_positions_y.append(yi)
        return cell_positions_y

