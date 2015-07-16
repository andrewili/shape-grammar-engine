from package.view import container as c
from package.view import frame as f
from package.view import grammar as g
from package.view import initial_shape as ish
from package.view import layer as l
from package.view import rule as r
from package.view import settings as s
import rhinoscriptsyntax as rs

class Utilities(object):
    labeled_right_triangle_spec = (
        [   ((4, 4, 0), (4, 28, 0)),
            ((4, 4, 0), (22, 4, 0)),
            ((4, 28, 0), (22, 4, 0))],
        [   ('a', (8, 8, 0))])
    labeled_h_spec = (
        [   ((8, 8, 0), (8, 24, 0)),
            ((8, 16, 0), (24, 16, 0)),
            ((24, 8, 0), (24, 24, 0))],
        [   ('a', (8, 6, 0)),
            ('a', (8, 26, 0)),
            ('a', (24, 6, 0)),
            ('a', (24, 26, 0))])
    labeled_h_is_string = '\n'.join([
        'shape    labeled_h_spec',
        '    name',
        '    coords 0 8 6 0',
        '    coords 1 8 8 0',
        '    coords 2 8 16 0',
        '    coords 3 8 24 0',
        '    coords 4 8 26 0',
        '    coords 5 24 6 0',
        '    coords 6 24 8 0',
        '    coords 7 24 16 0',
        '    coords 8 24 24 0',
        '    coords 9 24 26 0',
        '',
        '    line 0 1 3',
        '    line 1 2 7',
        '    line 2 6 8',
        '    point 0 0 a'
        '    point 1 4 a'
        '    point 2 5 a'
        '    point 3 9 a'
    ])
    labeled_square_spec = (
        [   ((4, 4, 0), (4, 28, 0)),
            ((4, 4, 0), (28, 4, 0)),
            ((4, 28, 0), (28, 28, 0)),
            ((28, 4, 0), (28, 28, 0))],
        [   ('a', (8, 24, 0))])
    subdivide_triangle_spec = (
        (   [   ((4, 4, 0), (4, 28, 0)),
                ((4, 4, 0), (22, 4, 0)),
                ((4, 28, 0), (22, 4, 0))],
            [   ('a', (8, 8, 0))]),
        (   [   ((4, 4, 0), (4, 28, 0)),
                ((4, 4, 0), (22, 4, 0)),
                ((4, 16, 0), (13, 16, 0)),
                ((4, 16, 0), (13, 4, 0)),
                ((4, 28, 0), (22, 4, 0)),
                ((13, 4, 0), (13, 16, 0))],
            [   ('a', (6, 6, 0)),
                ('a', (6, 18, 0)),
                ('a', (15, 6, 0))]))
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
    delete_labeled_point_spec = (
        ([], [('a', (10, 10, 0))]),
        ([], []))

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
            'subdivide_triangle_spec', cls.subdivide_triangle_spec)
        cls._add_subsequent_rule(
            'add_h_to_h_spec', cls.add_h_to_h_spec, (60, -80, 0))
        cls._add_subsequent_rule(
            'add_h_in_square_spec', cls.add_h_in_square_spec, (60, -120, 0))
        
    @classmethod
    def make_grammar_3_initial_shapes_0_rules(cls):
        """Adds 3 initial shapes
        """
        g.Grammar.clear_all()
        cls._add_first_initial_shape(
            'labeled_right_triangle_spec', cls.labeled_right_triangle_spec)
        cls._add_subsequent_initial_shape(
            'labeled_h_spec', 
            cls.labeled_h_spec, 
            (0, -80, 0))
        cls._add_subsequent_initial_shape(
            'labeled_square_spec', cls.labeled_square_spec, (0, -120, 0))

    @classmethod
    def make_grammar_3_initial_shapes_3_rules(cls):
        """Adds 3 initial shapes and 3 rules
        """
        g.Grammar.clear_all()
        cls._add_first_initial_shape(
            'labeled_right_triangle_spec', cls.labeled_right_triangle_spec)
        cls._add_subsequent_initial_shape(
            'labeled_h_spec', 
            cls.labeled_h_spec, 
            (0, -80, 0))
        cls._add_subsequent_initial_shape(
            'labeled_square_spec', cls.labeled_square_spec, (0, -120, 0))
        cls._add_first_rule(
            'subdivide_triangle_spec', cls.subdivide_triangle_spec)
        cls._add_subsequent_rule(
            'add_h_to_h_spec', cls.add_h_to_h_spec, (60, -80, 0))
        cls._add_subsequent_rule(
            'add_h_in_square_spec', cls.add_h_in_square_spec, (60, -120, 0))

    @classmethod
    def make_grammar_3_initial_shapes_4_rules(cls):
        """Adds 3 initial shapes and 4 rules (including delete label rule)
        """
        g.Grammar.clear_all()
        cls._add_first_initial_shape(
            'labeled_right_triangle_spec', cls.labeled_right_triangle_spec)
        cls._add_subsequent_initial_shape(
            'labeled_h_spec', 
            cls.labeled_h_spec, 
            (0, -80, 0))
        cls._add_subsequent_initial_shape(
            'labeled_square_spec', cls.labeled_square_spec, (0, -120, 0))
        cls._add_first_rule(
            'subdivide_triangle_spec', cls.subdivide_triangle_spec)
        cls._add_subsequent_rule(
            'add_h_to_h_spec', cls.add_h_to_h_spec, (60, -80, 0))
        cls._add_subsequent_rule(
            'add_h_in_square_spec', cls.add_h_in_square_spec, (60, -120, 0))
        cls._add_subsequent_rule(
            'delete_labeled_point_spec',
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

