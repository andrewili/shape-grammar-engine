from package.view import container as c
from package.view import frame as f
from package.view import grammar as g
from package.view import initial_shape as ish
from package.view import rule as r
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
                ((6, 22, 0), (18, 22, 0)),
                ((10, 6, 0), (10, 22, 0)),
                ((10, 14, 0), (26, 14, 0)),
                ((14, 18, 0), (14, 26, 0))],
            [   ('a', (10, 17, 0)),
                ('a', (10, 27, 0)),
                ('a', (14, 17, 0)),
                ('a', (14, 27, 0))]))
    add_h_in_square_spec = (
        (   [   ((4, 4, 0), (4, 28, 0)),
                ((4, 4, 0), (22, 4, 0)),
                ((4, 28, 0), (22, 4, 0))],
            [   ('a', (8, 24, 0))]),
        (   [   ((4, 4, 0), (4, 28, 0)),
                ((4, 4, 0), (28, 4, 0)),
                ((4, 16, 0), (16, 28, 0)),
                ((4, 28, 0), (28, 28, 0)),
                ((10, 20, 0), (20, 10, 0)),
                ((16, 4, 0), (28, 16, 0)),
                ((28, 4, 0), (28, 28, 0))],
            []))

    def __init__(self):
        pass

    @classmethod
    def make_grammar_3_ishapes_3_rules(cls):    ##  06-24 08:25
        """Adds 3 initial shapes and 3 rules. Returns:
            ?
        """
        g.Grammar.clear_all()
        cls._add_first_ishape(cls.labeled_right_triangle_spec)
        cls._add_first_rule(cls.labeled_h_spec)
        cls._add_subsequent_ishape(cls.labeled_square_spec)
        cls._add_subsequent_ishape(cls.subdivide_triangle_spec)
        cls._add_subsequent_rule(cls.add_h_to_h_spec)
        cls._add_subsequent_rule(cls.add_h_in_square_spec)

    @classmethod
    def _add_first_ishape(cls, labeled_shape_spec): ##  to do
        """Receives:
            labeled_shape_spec
                            ([line_specs], [labeled_point_specs])
        Returns:
            ?
        """
        layer_name = g.Grammar._set_up_first_initial_shape()
        cls._draw_labeled_shape_in_container(labeled_shape_spec, layer_name)

    @classmethod
    def _add_subsequent_ishape(cls, labeled_shape_spec):    ##  to do
        pass

    @classmethod
    def _add_first_rule(cls, rule_spec):        ##  to do
        pass

    @classmethod
    def _add_subsequent_rule(cls, layer_name, rule_spec):   ##  06-24 08:40
        """Receives:
            layer_name      str. The name of the layer containing the rule
            rule_spec       (labeled_shape_spec, labeled_shape_spec)
        Returns:
            ?
        """
        left_labeled_shape_spec, right_labeled_shape_spec = rule_spec
        left_position, right_position = (
            l.Layer.get_frame_positions_from_layer_name(layer_name))
        draw_labeled_shape(left_labeled_shape_spec, left_position)
        draw_labeled_shape(right_labeled_shape_spec, right_position)

    @classmethod
    def _draw_labeled_shape_in_container(cls, labeled_shape_spec, layer_name):
        rs.CurrentLayer(layer_name)
        frame_position = get_frame_position_from_layer_name(layer_name)
        cls._draw_labeled_shape(labeled_shape_spec, frame_position)
        rs.CurrentLayer(s.Settings.default_layer_name)

    @classmethod
    def _draw_labeled_shape(cls, labeled_shape_spec, position):
        line_specs, lpoint_specs = labeled_shape_spec
        for line_spec in line_specs:
            tail, head = line_spec
            rs.AddLine(tail, head)
        for lpoint_spec in lpoint_specs:
            text, point = lpoint_spec
            rs.AddTextDot(text, point)

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

