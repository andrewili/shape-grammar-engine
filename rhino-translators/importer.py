#   importer.py

from . import derivation
from . import grammar
# import numpy                                  ##  consider
##### import rhinoscriptsyntax as rs
from . import rule
from . import shape
# import text_test

##  Labels. Use text objects? 
##  Implement abort method

class Importer(object):
    def __init__(self):
        self.shape_size = [32, 32, 0]
        self.arrow_size = [16, 8, 0]
        self.padding = [8, 8, 0]
        self.padded_shape_size = self._add_vectors(
            self.shape_size, 
            self.padding)
        self.padded_arrow_size = self._add_vectors(
            self.arrow_size,
            self.padding)
        self.padded_next_shape_size = [
            self.padded_arrow_size[0] + self.padded_shape_size[0], 
            self.padded_shape_size[1], 
            0]
        self.padded_rule_size = [
            (   self.padded_shape_size[0] + 
                self.padded_arrow_size[0] + 
                self.padded_shape_size[0]),
            self.padded_shape_size[1],
            0]

    ###
    def import_derivation(self):                ##  Draws the grammar?
        """Prompts for a drv file. Draws the derivation. 
        """
        drv_text_lines = self._get_text_lines_from_drv_file()
        derivation_in = (
            derivation.Derivation.new_from_drv_text_lines(drv_text_lines))
        self._draw_derivation(derivation_in)

    def _draw_derivation(self, derivation_in):  ##  _draw_simple_derivation
        """Receives: 
            Derivation
        Lays out and draws the derivation. For now, left to right in the upper 
        right quadrant.
        """
        origin = [0, 0, 0]                      ##  redundant
        double_arrow_width = 10
        shape_width = 32
        double_arrow_and_shape_width = double_arrow_width + shape_width
        offset_increment = [double_arrow_and_shape_width, 0, 0]
                                                ##  generalize for y-dim
        i = 0

        # for shape in derivation_in.next_shapes:
        #     offset = self._calculate_offset(offset_increment, i)
        #     if i == 0:
        #         self._draw_shape(shape, offset)
        #     else:
        #         self._draw_shape(shape, offset) ##  double arrow disabled
        #         # self._draw_derivation_arrow_and_shape(
        #         #     shape, offset, double_arrow_width)
        #         print('shape %i: %s' % (i, shape.name))
        #     i = i + 1

        for shape_i in derivation_in.derivation_shapes:
            position = self._get_item_position(origin, offset_increment, i)
            self._draw_shape(shape_i, position)
            i += 1

    def _calculate_offset(self, offset_increment, i):
        """Receives an offset increment and an index:
            [num, num, num]
            int
        Returns an offset, i.e., vector or local origin:
            [num, num, num]
        """
        offset = [coord_offset * i for coord_offset in offset_increment]
        return offset

    ###
    def import_grammar(self):
        """Prompts for a drv file. Draws the grammar.
        """
        drv_text_lines = self._get_text_lines_from_drv_file()
        grammar_in = grammar.Grammar.new_from_drv_text_lines(drv_text_lines)
        self._draw_grammar(grammar_in)

    def _draw_grammar(self, grammar_in):
        """Receives: 
            Grammar
        Draws the grammar. For now, top to bottom in the lower right quadrant.
        """
        origin = [0, 0, 0]
        offset_direction = [0, -1, 0]
        offset_increment = self._multiply_vectors(
            self.padded_rule_size, offset_direction)
        i = 1
                                                ##  Multiple initial shapes
        for shape_i in grammar_in.initial_shapes:
            position = self._get_item_position(origin, offset_increment, i)
            self._draw_shape(shape_i, position)
            i += 1
        for rule_i in grammar_in.rules:
            position = self._get_item_position(origin, offset_increment, i)
            self._draw_rule(rule_i, position)
            i += 1

        # initial_shapes_location = self._add_vectors(
        #     origin, 
        #     self._multiply_vector_scalar(offset_increment, i))
        # self._draw_shape(grammar_in.initial_shape, initial_shapes_location)
        # i = i + 1
        # for rule_i in grammar_in.rules:
        #     offset_multiplier = self._calculate_offset(offset_direction, i)
        #     rule_location = self._add_vectors(
        #         origin,
        #         self._multiply_vector_scalar(offset_increment, i))
        #     self._draw_rule(rule_i, rule_location)
        #     i = i + 1

    def _get_item_position(self, origin, offset_increment, i):
        """Receives origin, offset increment, and index:
            [num, num, num]
            [num, num, num]
            int
        Returns the position of the item:
            [num, num, num]
        """
        net_offset = self._multiply_vector_scalar(offset_increment, i)
        position = self._add_vectors(origin, net_offset)
        return position

    def _multiply_vectors(self, v1, v2):        ##  right name?
        """Receives two vectors:
            [num, num, num]
            [num, num, num]
        Returns a vector whose components are products of the corresponding 
        components:
            [num, num, num]
        """
        product = map(self._multiply, v1, v2)
        return product

    def _multiply(self, num1, num2):
        product = num1 * num2
        return product

    def _multiply_vector_scalar(self, vector_in, scalar):
        """Receives:
            [num, num, num]
            num
        Returns a vector:
            [num, num, num]
        """
        vector_out = []
        for coord_in in vector_in:
            coord_out = coord_in * scalar
            vector_out.append(coord_out)
        return vector_out

    def _get_initial_shape_location(self, i):
        """Receives:
            int
        Returns the origin of the initial shape:
            [num, num, num]
        """

        return [x, y, z]

    def _draw_rule(self, rule_in, location_rule=[0, 0, 0]):
        """Receives a rule and a location:
            Rule
            [num, num, num]
        Draws the rule at the location.
        """
        location_name, location_left, location_arrow, location_right = (
            self._calculate_rule_part_locations(location_rule))
        self._write_shape_name(rule_in.name, location_name)     ##
        self._draw_shape(rule_in.left_shape, location_left)
        self._draw_rule_arrow(location_arrow)                   ##
        self._draw_shape(rule_in.right_shape, location_right)

    def _calculate_rule_part_locations(self, location_rule):
        """Receives the rule's location:
            [num, num, num]
        Returns the origins of the rule's name, left shape, arrow, and 
        right shape:
            (   [num, num, num], 
                [num, num, num], 
                [num, num, num], 
                [num, num, num])
        """
        offset_rule_left = [0, 0, 0]
        offset_rule_name = [self.padded_shape_size[0], 0, 0]    ##  temp
        offset_rule_arrow = [
            self.padded_shape_size[0], 
            (self.shape_size[1] - self.arrow_size[1]) / 2, 
            0]
        offset_rule_right = [
            offset_rule_arrow[0] + self.padded_arrow_size[0], 
            0, 
            0]
        location_name = self._add_vectors(location_rule, offset_rule_name)
        location_left = self._add_vectors(location_rule, offset_rule_left)
        location_arrow = self._add_vectors(location_rule, offset_rule_arrow)
        location_right = self._add_vectors(location_rule, offset_rule_right)
        return (
            location_name, 
            location_left, 
            location_arrow, 
            location_right)

    def _add_vectors(self, v1, v2):
        """Receives two vectors or points:
            [num, num, num]
            [num, num, num]
        Returns the sum:
            [num, num, num]
        """
        vector_sum = map(self._add, v1, v2)
        return vector_sum

    def _add(self, num1, num2):
        total = num1 + num2
        return total

    ###
    def import_final_shape(self):
        """Prompts for a drv file. Draws the final shape in the derivation.
        """
        drv_text_lines = self._get_text_lines_from_drv_file()
        final_shape_text_lines = (
            shape.Shape.get_final_shape_text_lines_from_drv_text_lines(
                drv_text_lines))
        final_shape = shape.Shape.new_from_is_text_lines(
            final_shape_text_lines)
        self._draw_shape(final_shape)

    def _get_text_lines_from_drv_file(self):
        """Prompts for a drv file. Returns its text lines:
            [drv_text_line, ...]
        """
        filter = "Derivation files (*.drv)|*.drv|All files (*.*)|*.*||"
        filename = rs.OpenFileName('Open derivation file', filter)
        if not filename:
            return
        file = open(filename, 'r')
        drv_text_lines = file.readlines()
        file.close()
        return drv_text_lines

    ###
    def import_rule(self):
        rule_in = self._read_rule_file()
        source_shape = rule_in.get_source_shape()
        self._draw_shape(source_shape)

    def _read_rule_file(self):
        """Prompts for a file. Returns:
            Rule
        """
        #   prompt the user for a file to import
        filter = "Rule files (*.rul)|*.rul|All files (*.*)|*.*||"
        filename = rs.OpenFileName("Open rule file", filter)
        if not filename: 
            return
        
        #   read each line from the file
        file = open(filename, "r")
        contents = file.readlines()
        file.close()

        new_rule = rule.Rule.new_from_rul_text_lines(contents)
        return new_rule

    ###
    def import_initial_shape(self):
        shape_in = self._read_shape_file()
        self._draw_shape(shape_in)

    def _read_shape_file(self):
        """Prompts for a file. Returns:
            Shape
        """
        #   prompt the user for a file to import
        filter = "Shape files (*.is)|*.is|All files (*.*)|*.*||"
        filename = rs.OpenFileName("Open shape file", filter)
        if not filename: return
        
        #   read each line from the file
        file = open(filename, "r")
        contents = file.readlines()
        file.close()

        new_shape = shape.Shape.new_from_is_text_lines(contents)
        return new_shape

    def _write_shape_name(self, name, offset=[0, 0, 0]):
        """
        """
        print('In lieu of writing a shape name')

    def _draw_rule_arrow(self, location=[0, 0, 0]):
        """Receives the global location:
            [num, num, num]
        Draws a rule arrow at that location.
        """
        p12 = [0, 4, 0]
        p21 = [12, 0, 0]
        p23 = [12, 8, 0]
        p32 = [16, 4, 0]
        self._draw_line(p12, p32, location)
        self._draw_line(p21, p32, location)
        self._draw_line(p23, p32, location)
        print('In addition to drawing a rule arrow')

    def _draw_derivation_arrow_and_shape(       ##  not called
        self, shape, offset, double_arrow_width
    ):
        """Receives:
            Shape
            [num, num, num]
            num
        Draws a double arrow and the shape at the offset locations.
        """
        self._draw_derivation_arrow(offset)
        shape_offset = [offset[0] + double_arrow_width, offset[1], offset[2]]
        self._draw_shape(shape, shape_offset)   ##

    def _draw_derivation_arrow(self, offset):
        """Receives an offset:
            [num, num, num]
        Draws a derivation arrow at that offset.
        """
        p12 = [1, 2, 0]
        p14 = [1, 4, 0]
        p60 = [6, 0, 0]
        p66 = [6, 6, 0]
        p82 = [8, 2, 0]
        p84 = [8, 4, 0]
        p86 = [8, 8, 0]
        p93 = [9, 3, 0]
        self._draw_line(p12, p82, offset)
        self._draw_line(p14, p84, offset)
        self._draw_line(p60, p93, offset)
        self._draw_line(p66, p93, offset)

    def _draw_shape(self, shape, location=[0, 0, 0]):
        """Receives a shape and a list denoting the local origin: 
            Shape
            [num, num, num]
        Draws the shape in Rhino at the location.
        """
        rhino_lines = shape.get_line_specs_as_lists()
        for rhino_line in rhino_lines:
            rhino_p1, rhino_p2 = rhino_line
            self._draw_line(rhino_p1, rhino_p2, location)
        rhino_lpoints = shape.get_rhino_lpoints()
        for rhino_lpoint in rhino_lpoints:
            label, rhino_point = rhino_lpoint
            self._draw_rhino_lpoint(label, rhino_point, location)

    def _draw_shape_ground(self, location=[0, 0, 0]):
        """Receives a location:
            [num, num, num]
        Draws a square at the location.
        """
        dx = self.padded_shape_size[0]
        dy = self.padded_shape_size[1]
        p00 = [0, 0, 0]
        p01 = [0, dy, 0]
        p10 = [dx, 0, 0]
        p11 = [dx, dy, 0]
        self._draw_line(p00, p01, location)
        self._draw_line(p00, p10, location)
        self._draw_line(p01, p11, location)
        self._draw_line(p10, p11, location)

    def _draw_line(self, p1, p2, offset):
        p1a = map(self._offset_coord, p1, offset)
        p2a = map(self._offset_coord, p2, offset)
        rs.AddLine(p1a, p2a)

    def _draw_lpoint(self):                     ##  draw point
        pass

    def _draw_rhino_lpoint(self, label, rhino_point, offset):
        offset_rhino_point = map(self._offset_coord, rhino_point, offset)
        # rs.AddTextDot(label, offset_rhino_point)
        rs.AddText(label, offset_rhino_point)

    def _offset_coord(self, coord, offset):
        return coord + offset

