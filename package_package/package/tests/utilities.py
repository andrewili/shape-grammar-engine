from package.scripts import frame as f
from package.scripts import grammar as g
from package.controller import guids_to_dat as gd
from package.scripts import layer as l
from package.scripts import settings as s
import rhinoscriptsyntax as rs

class Utilities(object):
    add_h_in_square_spec = (
        (   [   ((4, 4, 0), (4, 28, 0)),
                ((4, 4, 0), (28, 4, 0)),
                ((4, 28, 0), (28, 28, 0)),
                ((28, 4, 0), (28, 28, 0))],
            [   ('a', (8, 24, 0))]),
        (   [   ((4, 4, 0), (4, 28, 0)),
                ((4, 4, 0), (28, 4, 0)),
                ((4, 16, 0), (16, 28, 0)),
                ((4, 28, 0), (28, 28, 0)),
                ((10, 22, 0), (22, 10, 0)),
                ((16, 4, 0), (28, 16, 0)),
                ((28, 4, 0), (28, 28, 0))],
            []))
    add_h_in_square_L_string = '\n'.join([
        'shape    add_h_in_square_L',
        '    name',
        '    coords 0 4.0 4.0 0.0',
        '    coords 1 4.0 28.0 0.0',
        '    coords 2 8.0 24.0 0.0',
        '    coords 3 28.0 4.0 0.0',
        '    coords 4 28.0 28.0 0.0',
        '',
        '    line 0 0 1',
        '    line 1 0 3',
        '    line 2 1 4',
        '    line 3 3 4',
        '    point 2 a'
    ])
    add_h_in_square_R_string = '\n'.join([
        'shape    add_h_in_square_R',
        '    name',
        '    coords 0 4.0 4.0 0.0',
        '    coords 1 4.0 16.0 0.0',
        '    coords 2 4.0 28.0 0.0',
        '    coords 3 10.0 22.0 0.0',
        '    coords 4 16.0 4.0 0.0',
        '    coords 5 16.0 28.0 0.0',
        '    coords 6 22.0 10.0 0.0',
        '    coords 7 28.0 4.0 0.0',
        '    coords 8 28.0 16.0 0.0',
        '    coords 9 28.0 28.0 0.0',
        '',
        '    line 0 0 2',
        '    line 1 0 7',
        '    line 2 1 5',
        '    line 3 2 9',
        '    line 4 3 6',
        '    line 5 4 8',
        '    line 6 7 9'
    ])
    add_h_in_square_string = '\n'.join([
        add_h_in_square_L_string,
        add_h_in_square_R_string
    ])

    add_h_to_h_spec = (
        (   [   ((10, 6, 0), (10, 22, 0)),
                ((10, 14, 0), (26, 14, 0))],
            [   ('a', (10, 27, 0))]),
        (   [   ((6, 18, 0), (6, 26, 0)),
                ((6, 22, 0), (14, 22, 0)),
                ((10, 6, 0), (10, 22, 0)),
                ((10, 14, 0), (26, 14, 0)),
                ((14, 18, 0), (14, 26, 0))],
            [   ('a', (6, 17, 0)),
                ('a', (6, 27, 0)),
                ('a', (14, 17, 0)),
                ('a', (14, 27, 0))]))
    add_h_to_h_L_string = '\n'.join([
        'shape    add_h_to_h_L',
        '    name',
        '    coords 0 10.0 6.0 0.0',
        '    coords 1 10.0 14.0 0.0',
        '    coords 2 10.0 22.0 0.0',
        '    coords 3 10.0 27.0 0.0',
        '    coords 4 26.0 14.0 0.0',
        '',
        '    line 0 0 2',
        '    line 1 1 4',
        '    point 3 a',
    ])
    add_h_to_h_R_string = '\n'.join([
        'shape    add_h_to_h_R',
        '    name',
        '    coords 0 6.0 17.0 0.0',
        '    coords 1 6.0 18.0 0.0',
        '    coords 2 6.0 22.0 0.0',
        '    coords 3 6.0 26.0 0.0',
        '    coords 4 6.0 27.0 0.0',
        '    coords 5 10.0 6.0 0.0',
        '    coords 6 10.0 14.0 0.0',
        '    coords 7 10.0 22.0 0.0',
        '    coords 8 14.0 17.0 0.0',
        '    coords 9 14.0 18.0 0.0',
        '    coords 10 14.0 22.0 0.0',
        '    coords 11 14.0 26.0 0.0',
        '    coords 12 14.0 27.0 0.0',
        '    coords 13 26.0 14.0 0.0',
        '',
        '    line 0 1 3',
        '    line 1 2 10',
        '    line 2 5 7',
        '    line 3 6 13',
        '    line 4 9 11',
        '    point 0 a',
        '    point 4 a',
        '    point 8 a',
        '    point 12 a'
    ])
    add_h_to_h_string = '\n'.join([
        add_h_to_h_L_string, 
        add_h_to_h_R_string
    ])

    delete_labeled_point_spec = (
        ([], [('a', (10, 10, 0))]),
        ([], []))
    delete_labeled_point_L_string = '\n'.join([
        'shape    delete_labeled_point_L',
        '    name',
        '    coords 0 10.0 10.0 0.0',
        '',
        '    point 0 a'
    ])
    delete_labeled_point_R_string = '\n'.join([
        'shape    delete_labeled_point_R',
        '    name'
    ])
    delete_labeled_point_string = '\n'.join([
        delete_labeled_point_L_string,
        delete_labeled_point_R_string
    ])

    labeled_h_spec = (
        [   ((8, 8, 0), (8, 24, 0)),
            ((8, 16, 0), (24, 16, 0)),
            ((24, 8, 0), (24, 24, 0))],
        [   ('a', (8, 6, 0)),
            ('a', (8, 26, 0)),
            ('a', (24, 6, 0)),
            ('a', (24, 26, 0))])
    labeled_h_string = '\n'.join([
        'shape    labeled_h',
        '    name',
        '    coords 0 8.0 6.0 0.0',
        '    coords 1 8.0 8.0 0.0',
        '    coords 2 8.0 16.0 0.0',
        '    coords 3 8.0 24.0 0.0',
        '    coords 4 8.0 26.0 0.0',
        '    coords 5 24.0 6.0 0.0',
        '    coords 6 24.0 8.0 0.0',
        '    coords 7 24.0 16.0 0.0',
        '    coords 8 24.0 24.0 0.0',
        '    coords 9 24.0 26.0 0.0',
        '',
        '    line 0 1 3',
        '    line 1 2 7',
        '    line 2 6 8',
        '    point 0 a',
        '    point 4 a',
        '    point 5 a',
        '    point 9 a'
    ])
    labeled_h_is_string = '\n'.join([
        'shape    labeled_h_spec',
        '    name',
        '    coords 0 8.0 6.0 0.0',
        '    coords 1 8.0 8.0 0.0',
        '    coords 2 8.0 16.0 0.0',
        '    coords 3 8.0 24.0 0.0',
        '    coords 4 8.0 26.0 0.0',
        '    coords 5 24.0 6.0 0.0',
        '    coords 6 24.0 8.0 0.0',
        '    coords 7 24.0 16.0 0.0',
        '    coords 8 24.0 24.0 0.0',
        '    coords 9 24.0 26.0 0.0',
        '',
        '    line 0 1 3',
        '    line 1 2 7',
        '    line 2 6 8',
        '    point 0 0 a'
        '    point 1 4 a'
        '    point 2 5 a'
        '    point 3 9 a'
    ])

    labeled_right_triangle_spec = (
        [   ((4, 4, 0), (4, 28, 0)),
            ((4, 4, 0), (22, 4, 0)),
            ((4, 28, 0), (22, 4, 0))],
        [   ('a', (8, 8, 0))])
    labeled_right_triangle_string = '\n'.join([
        'shape    labeled_right_triangle',
        '    name',
        '    coords 0 4.0 4.0 0.0',
        '    coords 1 4.0 28.0 0.0',
        '    coords 2 8.0 8.0 0.0',
        '    coords 3 22.0 4.0 0.0',
        '',
        '    line 0 0 1',
        '    line 1 0 3',
        '    line 2 1 3',
        '    point 2 a'
    ])

    labeled_square_spec = (
        [   ((4, 4, 0), (4, 28, 0)),
            ((4, 4, 0), (28, 4, 0)),
            ((4, 28, 0), (28, 28, 0)),
            ((28, 4, 0), (28, 28, 0))],
        [   ('a', (8, 24, 0))])
    labeled_square_string = '\n'.join([
        'shape    labeled_square',
        '    name',
        '    coords 0 4.0 4.0 0.0',
        '    coords 1 4.0 28.0 0.0',
        '    coords 2 8.0 24.0 0.0',
        '    coords 3 28.0 4.0 0.0',
        '    coords 4 28.0 28.0 0.0',
        '',
        '    line 0 0 1',
        '    line 1 0 3',
        '    line 2 1 4',
        '    line 3 3 4',
        '    point 2 a'
    ])

    subdivide_triangle_spec = (
        (   [   ((4, 4, 0), (4, 28, 0)),
                ((4, 4, 0), (22, 4, 0)),
                ((4, 28, 0), (22, 4, 0))],
            [   ('a', (8, 8, 0))]),
        (   [   ((4, 4, 0), (4, 28, 0)),
                ((4, 4, 0), (22, 4, 0)),
                ((4, 16, 0), (13, 4, 0)),
                ((4, 16, 0), (13, 16, 0)),
                ((4, 28, 0), (22, 4, 0)),
                ((13, 4, 0), (13, 16, 0))],
            [   ('a', (6, 6, 0)),
                ('a', (6, 18, 0)),
                ('a', (15, 6, 0))]))
    subdivide_triangle_L_string = '\n'.join([
        'shape    subdivide_triangle_L',
        '    name',
        '    coords 0 4.0 4.0 0.0',
        '    coords 1 4.0 28.0 0.0',
        '    coords 2 8.0 8.0 0.0',
        '    coords 3 22.0 4.0 0.0',
        '',
        '    line 0 0 1',
        '    line 1 0 3',
        '    line 2 1 3',
        '    point 2 a',
    ])
    subdivide_triangle_R_string = '\n'.join([
        'shape    subdivide_triangle_R',
        '    name',
        '    coords 0 4.0 4.0 0.0',
        '    coords 1 4.0 16.0 0.0',
        '    coords 2 4.0 28.0 0.0',
        '    coords 3 6.0 6.0 0.0',
        '    coords 4 6.0 18.0 0.0',
        '    coords 5 13.0 4.0 0.0',
        '    coords 6 13.0 16.0 0.0',
        '    coords 7 15.0 6.0 0.0',
        '    coords 8 22.0 4.0 0.0',
        '',
        '    line 0 0 2',
        '    line 1 0 8',
        '    line 2 1 5',
        '    line 3 1 6',
        '    line 4 2 8',
        '    line 5 5 6',
        '    point 3 a',
        '    point 4 a',
        '    point 7 a'
    ])
    subdivide_triangle_string = '\n'.join([
        subdivide_triangle_L_string,
        subdivide_triangle_R_string
    ])

    three_initial_shapes = [
        'labeled_h',
        'labeled_right_triangle',
        'labeled_square']
    three_rules = [
        'add_h_in_square',
        'add_h_to_h',
        'subdivide_triangle']
    four_rules = [
        'add_h_in_square',
        'add_h_to_h',
        'subdivide_triangle',
        'delete_labeled_point']

    ordered_labeled_shapes_1_1_string = '\n'.join([
        delete_labeled_point_string,
        labeled_right_triangle_string
    ])
    delete_labeled_point_name = 'delete_labeled_point'
    subdivide_triangle_name = 'subdivide_triangle'
    ordered_labeled_shapes_3_4_string = '\n'.join([
        add_h_in_square_L_string,
        add_h_in_square_R_string,
        add_h_to_h_L_string,
        add_h_to_h_R_string,
        delete_labeled_point_L_string,
        delete_labeled_point_R_string,
        labeled_h_string,
        labeled_right_triangle_string,
        labeled_square_string,
        subdivide_triangle_L_string,
        subdivide_triangle_R_string
    ])
    ordered_initial_shape_names_3_string = '\n'.join([
        'initial    labeled_h',
        'initial    labeled_right_triangle',
        'initial    labeled_square',
    ])
    ordered_rule_names_4_string = '\n'.join([
        'rule    %s    %s_L -> %s_R' % (
            'add_h_in_square', 'add_h_in_square', 'add_h_in_square'),
        'rule    %s    %s_L -> %s_R' % (
            'add_h_to_h', 'add_h_to_h', 'add_h_to_h'),
        'rule    %s    %s_L -> %s_R' % (
            'delete_labeled_point', 
            'delete_labeled_point', 
            'delete_labeled_point'),
        'rule    %s    %s_L -> %s_R' % (
            'subdivide_triangle', 'subdivide_triangle', 'subdivide_triangle')
    ])
    grammar_3_4_dat_string = '\n'.join([
        gd.GuidsToDat.dat_header,
        ordered_labeled_shapes_3_4_string,
        gd.GuidsToDat.blank_line,
        ordered_initial_shape_names_3_string,
        ordered_rule_names_4_string,
        gd.GuidsToDat.blank_line
    ])

    def __init__(self):
        pass

    @classmethod
    def make_grammar_0_initial_shapes_0_rules(cls):
        """Adds nothing
        """
        g.Grammar.clear_all()

    @classmethod
    def make_grammar_0_initial_shapes_3_rules(cls):
        """Adds 3 rules
        """
        g.Grammar.clear_all()
        cls._add_first_rule(
            'subdivide_triangle', cls.subdivide_triangle_spec)
        cls._add_subsequent_rule(
            'add_h_to_h', cls.add_h_to_h_spec, (60, -80, 0))
        cls._add_subsequent_rule(
            'add_h_in_square', cls.add_h_in_square_spec, (60, -120, 0))

    @classmethod
    def make_grammar_1_initial_shape_1_delete_rule(cls):
        """Adds 1 initial shape and 1 delete rule
        """
        g.Grammar.clear_all()
        cls._add_first_initial_shape(
            'labeled_right_triangle', cls.labeled_right_triangle_spec)
        cls._add_first_rule(
            'delete_labeled_point',
            cls.delete_labeled_point_spec)

    @classmethod
    def make_grammar_3_initial_shapes_0_rules(cls):
        """Adds 3 initial shapes
        """
        g.Grammar.clear_all()
        cls._add_first_initial_shape(
            'labeled_right_triangle', cls.labeled_right_triangle_spec)
        cls._add_subsequent_initial_shape(
            'labeled_h', 
            cls.labeled_h_spec, 
            (0, -80, 0))
        cls._add_subsequent_initial_shape(
            'labeled_square', cls.labeled_square_spec, (0, -120, 0))

    @classmethod
    def make_grammar_3_initial_shapes_3_rules(cls):
        """Adds 3 initial shapes and 3 rules
        """
        g.Grammar.clear_all()
        cls._add_first_initial_shape(
            'labeled_right_triangle', cls.labeled_right_triangle_spec)
        cls._add_subsequent_initial_shape(
            'labeled_h', 
            cls.labeled_h_spec, 
            (0, -80, 0))
        cls._add_subsequent_initial_shape(
            'labeled_square', cls.labeled_square_spec, (0, -120, 0))
        cls._add_first_rule(
            'subdivide_triangle', cls.subdivide_triangle_spec)
        cls._add_subsequent_rule(
            'add_h_to_h', cls.add_h_to_h_spec, (60, -80, 0))
        cls._add_subsequent_rule(
            'add_h_in_square', cls.add_h_in_square_spec, (60, -120, 0))

    @classmethod
    def make_grammar_0_initial_shapes_3_rules_1_3_frame(cls):
        """Adds 3 initial shapes, 3 rules, and 1 layer with 3 frames
        """
        g.Grammar.clear_all()
        cls._add_first_initial_shape(
            'labeled_right_triangle', cls.labeled_right_triangle_spec)
        cls._add_subsequent_initial_shape(
            'labeled_h', 
            cls.labeled_h_spec, 
            (0, -80, 0))
        cls._add_subsequent_initial_shape(
            'labeled_square', cls.labeled_square_spec, (0, -120, 0))
        cls._add_first_rule(
            'subdivide_triangle', cls.subdivide_triangle_spec)
        cls._add_subsequent_rule(
            'add_h_to_h', cls.add_h_to_h_spec, (60, -80, 0))
        cls._add_subsequent_rule(
            'add_h_in_square', cls.add_h_in_square_spec, (60, -120, 0))
        cls._add_3_frame_layer(
            '3_frame_layer', cls.delete_labeled_point_spec, (60, -160, 0))

    @classmethod
    def make_grammar_3_initial_shapes_4_rules(cls):
        """Adds 3 initial shapes and 4 rules (including delete label rule)
        """
        g.Grammar.clear_all()
        cls._add_first_initial_shape(
            'labeled_right_triangle', cls.labeled_right_triangle_spec)
        cls._add_subsequent_initial_shape(
            'labeled_h', 
            cls.labeled_h_spec, 
            (0, -80, 0))
        cls._add_subsequent_initial_shape(
            'labeled_square', cls.labeled_square_spec, (0, -120, 0))
        cls._add_first_rule(
            'subdivide_triangle', cls.subdivide_triangle_spec)
        cls._add_subsequent_rule(
            'add_h_to_h', cls.add_h_to_h_spec, (60, -80, 0))
        cls._add_subsequent_rule(
            'add_h_in_square', cls.add_h_in_square_spec, (60, -120, 0))
        cls._add_subsequent_rule(
            'delete_labeled_point',
            cls.delete_labeled_point_spec,
            (60, -160, 0))
        point_1_inside_labeled_point_frame = (75, -145, 15)
        rs.AddPointLight(point_1_inside_labeled_point_frame)
        text = 'text'
        point_2_inside_labeled_point_frame = (65, -155, 5)
        rs.AddText(text, point_2_inside_labeled_point_frame)

    @classmethod
    def _add_first_initial_shape(cls, layer_name, initial_shape_spec):
        """Receives:
            layer_name      str. The name of the layer containing the initial 
                            shape
            initial_shape_spec
                            (line_specs, labeled_point_specs)
        Adds a new layer named layer_name. Inserts an initial shape frame. 
        Draws the initial shape. Returns:
            layer_name      str. If successful
            None            otherwise
        """
        set_up_okay = g.Grammar._set_up_first_initial_shape()
        rs.RenameLayer(s.Settings.first_initial_shape_layer_name, layer_name)
        frame_position = s.Settings.first_initial_shape_frame_position
        draw_okay = cls._draw_initial_shape(
            initial_shape_spec, layer_name, frame_position)
        if set_up_okay and draw_okay:
            return_value = layer_name
        else:
            return_value = None
        return return_value

    @classmethod
    def _add_subsequent_initial_shape(
        cls, layer_name, initial_shape_spec, frame_position
    ):
        """Receives:
            layer_name      str. The name of the layer containing the labeled 
                            shape
            initial_shape_spec
                            (line_specs, labeled_point_specs)
            frame_position  (num, num, num) or Point3d. The position of the 
                            initial shape frame
        Adds a new layer named layer_name. Inserts an initial shape frame. 
        Draws the initial shape. Returns:
            layer_name      str. If successful
            None            otherwise
        """
        g.Grammar._set_up_initial_shape(layer_name, frame_position)
        draw_okay = cls._draw_initial_shape(
            initial_shape_spec, layer_name, frame_position)
        if draw_okay:
            return_value = layer_name
        else:
            return_value = None
        return return_value

    @classmethod
    def _draw_initial_shape(
        cls, initial_shape_spec, layer_name, frame_position
    ):
        """Receives:
            initial_shape_spec
                            (line_specs, labeled_point_specs)
            layer_name      str. The name of the layer containing the initial 
                            shape
            frame_position  (num, num, num) or Point3d. The position of the 
                            initial shape frame
        Draws the initial shape at the frame position on the specified 
        layer. Returns:
            layer_name      str. If successful
            None            otherwise
        """
        rs.CurrentLayer(layer_name)
        draw_okay = cls._draw_labeled_shape(initial_shape_spec, frame_position)
        rs.CurrentLayer(s.Settings.default_layer_name)
        if draw_okay:
            return_value = layer_name
        else:
            return_value = None
        return return_value

    @classmethod
    def _add_first_rule(cls, layer_name, rule_spec):
        """Receives:
            layer_name      str. The name of the layer containing the rule
            rule_spec       (labeled_shape_spec, labeled_shape_spec)
        Adds a new layer named layer_name. Inserts left and right frame 
        instances. Draws the left and right labeled shapes. Returns:
            layer_name_out  str. If successful
            None            otherwise
        """
        set_up_okay = g.Grammar._set_up_first_rule()
        rs.RenameLayer(s.Settings.first_rule_layer_name, layer_name)
        left_frame_position = s.Settings.first_rule_left_frame_position
        draw_okay = cls._draw_rule(rule_spec, layer_name, left_frame_position)
        if set_up_okay and draw_okay:
            return_value = layer_name
        else:
            return_value = None
        return return_value

    @classmethod
    def _add_subsequent_rule(cls, layer_name, rule_spec, left_frame_position):
        """Receives:
            layer_name      str. The name of the layer containing the rule
            rule_spec       (labeled_shape_spec, labeled_shape_spec)
            left_frame_position
                            (num, num, num) or Point3d. The position of the 
                            left frame
        Adds a new layer named layer_name. Inserts left and right frame 
        instances. Draws the left and right labeled shapes. Returns:
            layer_name_out  str. If successful
            None            otherwise
        """
        set_up_okay = g.Grammar._set_up_rule(
            layer_name, left_frame_position)
        draw_okay = cls._draw_rule(
            rule_spec, layer_name, left_frame_position)
        if set_up_okay and draw_okay:
            return_value = layer_name
        else:
            return_value = None
        return return_value

    @classmethod
    def _draw_rule(cls, rule_spec, layer_name, left_frame_position):
        """Receives:
            rule_spec       (   left_labeled_shape_spec, 
                                right_labeled_shape_spec)
            layer_name      str. The name of the layer
        Draws the left and right shapes at the specified position on the 
        specified layer. Returns:
            layer_name      str. The name of the layer, if successful
            None            otherwise
        """
        left_labeled_shape_spec, right_labeled_shape_spec = rule_spec
        right_frame_position = s.Settings.get_right_frame_position(
            left_frame_position)
        rs.CurrentLayer(layer_name)
        left_okay = cls._draw_labeled_shape(
            left_labeled_shape_spec, left_frame_position)
        right_okay = cls._draw_labeled_shape(
            right_labeled_shape_spec, right_frame_position)
        rs.CurrentLayer(s.Settings.default_layer_name)
        all_okay = left_okay and right_okay
        if all_okay:
            return_value = layer_name
        else:
            return_value = None
        return return_value

    @classmethod
    def _add_3_frame_layer(cls, layer_name, rule_spec, left_frame_position):
        """Receives:
            layer_name      str
            left_frame_position
                            Point3d. The location of the leftmost frame 
                            instance
        Draws 3 frame instances on the specified layer
        """
        cls._add_subsequent_rule(layer_name, rule_spec, left_frame_position)
        frame_name = s.Settings.frame_name
        right_frame_offset = (100, 0, 0)
        right_frame_position = rs.PointAdd(
            left_frame_position, right_frame_offset)
        f.Frame.new_instance(frame_name, layer_name, right_frame_position)

    @classmethod                                ##  07-24 09:32
    def _make_grammar_3_4_dat_string(cls):
        pass
        # dat_header = gd.GuidsToDat.dat_header
        # cls.ordered_labeled_shapes_3_4_string,
        # blank_line = gd.GuidsToDat.blank_line

        # ordered_initial_shape_names_string = '\n'.join([
        #     initial_shape_i_name_string
        # ])
        # ordered_rule_names_string = '\n'.join([
        #     rule_i_name_string
        # ])
        # grammar_3_4_dat_string = '\n'.join([
        #     dat_header,
        #     ordered_labeled_shapes_3_4_string,
        # '',
        # 'initial    labeled_h',
        # 'initial    labeled_right_triangle',
        # 'initial    labeled_square',
        # 'rule    add_h_in_square    add_h_in_square_L -> add_h_in_square_R',
        # 'rule    add_h_to_h    add_h_to_h_L -> add_h_to_h_R',
        # 'rule    %s    %s_L -> %s_R' % (
        #     delete_labeled_point_name,
        #     delete_labeled_point_name,
        #     delete_labeled_point_name)
        # 'rule    %s    %s_L -> %s_R' % (
        #     subdivide_triangle_name,
        #     subdivide_triangle_name,
        #     subdivide_triangle_name)


        #     blank_line,
        #     ordered_initial_shape_names_string,
        #     ordered_rule_names_string
        # ])
        # return grammar_3_4_dat_string

    @classmethod
    def _draw_labeled_shape_in_container(cls, labeled_shape_spec, layer_name):
        rs.CurrentLayer(layer_name)
        frame_position = get_frame_position_from_layer_name(layer_name)
        cls._draw_labeled_shape(labeled_shape_spec, frame_position)
        rs.CurrentLayer(s.Settings.default_layer_name)

    @classmethod
    def _draw_labeled_shape(cls, labeled_shape_spec, position):
        """Receives:
            labeled_shape_spec
                            (line_specs, labeled_point_specs)
            position        (num, num, num) or Point3d
        Draws the labeled shape at the specified position. Returns:
            boolean         True, if successful
            None            otherwise
        """
        line_specs, lpoint_specs = labeled_shape_spec
        return_value = True
        for line_spec in line_specs:
            tail, head = line_spec
            offset_tail = cls._offset_point(tail, position)
            offset_head = cls._offset_point(head, position)
            line_guid = rs.AddLine(offset_tail, offset_head)
            if not line_guid:
                return_value = None
                break
        for lpoint_spec in lpoint_specs:
            text, point = lpoint_spec
            offset_point = cls._offset_point(point, position)
            text_dot_guid = rs.AddTextDot(text, offset_point)
            if not text_dot_guid:
                return_value = None
                break
        return return_value

    @classmethod
    def _offset_point(cls, point, offset):
        """Receives:
            point           (num, num, num)
            offset          (num, num, num)
        Returns:
            offset_point    Point3d. The offset point
        """
        offset_point = rs.PointAdd(point, offset)
        return offset_point

    @classmethod
    def prompt_for_initial_shape_frame_dict(cls, initial_shapes):
        block_instance_filter = s.Settings.block_instance_filter
        initial_shape_frame_dict = {}
        for initial_shape in initial_shapes:
            message = (
                "Select the frame instance on the layer '%s'" % initial_shape)
            frame_instance = rs.GetObject(message, block_instance_filter)
            initial_shape_frame_dict[initial_shape] = frame_instance
        return initial_shape_frame_dict

    @classmethod
    def prompt_for_rule_frame_pair_dict(cls, rules):
        block_instance_filter = s.Settings.block_instance_filter
        rule_frame_pair_dict = {}
        for rule in rules:
            message_left = (
                "Select the left frame instance on the layer '%s'" % rule)
            message_right = (
                "Select the right frame instance on the layer '%s'" % rule)
            frame_instance_left = rs.GetObject(
                message_left, block_instance_filter)
            frame_instance_right = rs.GetObject(
                message_right, block_instance_filter)
            rule_frame_pair_dict[rule] = (
                frame_instance_left, frame_instance_right)
        return rule_frame_pair_dict

    @classmethod
    def make_grammar_3_3_containers(cls):
        g.Grammar.clear_all()
        f.Frame.new()
        rs.AddGroup(ish.InitialShape.component_type)
        rs.AddGroup(r.Rule.component_type)
        ish.InitialShape.add_first()            ##  'add_first_container'?
        r.Rule.add_first()
        cls._add_2_ishape_containers()
        cls._add_2_rule_containers()

    @classmethod
    def _add_2_ishape_containers(cls):
        ishapes = [
            ('a_ishape', (100, -40, 0)), 
            ('z_ishape', (200, -40, 0))]
        ttype = ish.InitialShape.component_type
        for ishape in ishapes:
            name, origin = ishape
            c.Container.new(name, origin, ttype)

    @classmethod
    def _add_2_rule_containers(cls):
        rules = [
            ('a_rule', (100, -100, 0)), 
            ('z_rule', (200, -100, 0))]
        ttype = r.Rule.component_type
        for rule in rules:
            name, origin = rule
            c.Container.new(name, origin, ttype)

    @classmethod
    def print_test_error_message(
        cls, method_name, try_name, expected_value, actual_value
    ):
        message = "%s: %s:\n    expected '%s'; got '%s'" % (
            method_name, try_name, expected_value, actual_value)
        print(message)

