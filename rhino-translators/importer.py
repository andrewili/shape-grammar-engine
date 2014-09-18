#   importer.py

import derivation
import rhinoscriptsyntax as rs
import rule
import shape

class Importer(object):
    def __init__(self):
        pass

    ###
    def import_derivation(self):
        """Prompts for a drv file. Draws the derivation. 
        ##  Draws the grammar?
        """
        drv_text_lines = self._get_text_lines_from_drv_file()
        derivation_in = (
            derivation.Derivation.new_from_drv_text_lines(drv_text_lines))
        self._draw_derivation(derivation_in)

    def _draw_derivation(self, derivation_in):
        """Receives a derivation: 
            [Shape, ...]
        Lays out and draws the derivation. For now, left to right in the upper 
        right quadrant.
        """
        double_arrow_width = 10
        shape_width = 32
        double_arrow_and_shape_width = double_arrow_width + shape_width
        offset_increment = [double_arrow_and_shape_width, 0, 0]
        i = 0
        for shape in derivation_in.next_shapes:
            offset = self._calculate_offset(offset_increment, i)
            if i == 0:
                self._draw_shape(shape, offset)
            else:
                self._draw_shape(shape, offset) ##  double arrow disabled
                # self._draw_double_arrow_and_shape(
                #     shape, offset, double_arrow_width)
                print('shape %i: %s' % (i, shape.name))
            i = i + 1

    def _calculate_offset(self, offset_increment, i):
        """Receives an offset increment and an index:
            [num, num, num]
            int
        Returns an offset, i.e., vector or local origin
        """
        offset = [coord_offset * i for coord_offset in offset_increment]
        return offset
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
    def import_grammar(self):                   ##  to do
        """Prompts for a drv file. Draws the grammar in the derivation.
        """
        pass
        
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
    def import_shape(self):
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

    def _draw_double_arrow_and_shape(
        self, shape, offset, double_arrow_width
    ):
        """Receives:
            Shape
            [num, num, num]
            num
        Draws a double arrow and the shape at the offset locations.
        """
        self._draw_double_arrow(offset)
        shape_offset = [offset[0] + double_arrow_width, offset[1], offset[2]]
        self._draw_shape(shape, shape_offset)

    def _draw_double_arrow(self, offset):
        """Receives an offset:
            [num, num, num]
        Draws a double arrow at that offset.
        """
        p12 = [1, 2, 0]
        p14 = [1, 4, 0]
        p60 = [6, 0, 0]
        p66 = [6, 6, 0]
        p82 = [8, 2, 0]
        p84 = [8, 4, 0]
        p86 = [8, 8, 0]
        p93 = [9, 3, 0]
        self._draw_offset_line(p12, p82, offset)
        self._draw_offset_line(p14, p84, offset)
        self._draw_offset_line(p60, p93, offset)
        self._draw_offset_line(p66, p93, offset)

    def _draw_shape(self, shape, offset=[0, 0, 0]):
        """Receives a shape and a list denoting the local origin: 
            Shape
            [num, num, num]
        Draws the shape in Rhino at the local origin
        """
        rhino_lines = shape.get_line_specs_as_lists()
        for rhino_line in rhino_lines:
            rhino_p1, rhino_p2 = rhino_line
            self._draw_offset_line(rhino_p1, rhino_p2, offset)
            # rs.AddLine(rhino_p1, rhino_p2)
        rhino_dots = shape.get_rhino_dots()
        for rhino_dot in rhino_dots:
            label, rhino_point = rhino_dot
            self._draw_offset_rhino_dot(label, rhino_point, offset)
            # rs.AddTextDot(label, rhino_point)

    def _draw_offset_line(self, p1, p2, offset):
        p1a = map(self._offset_coord, p1, offset)
        p2a = map(self._offset_coord, p2, offset)
        rs.AddLine(p1a, p2a)

    def _draw_offset_rhino_dot(self, label, rhino_point, offset):
        offset_rhino_point = map(self._offset_coord, rhino_point, offset)
        rs.AddTextDot(label, offset_rhino_point)

    def _offset_coord(self, coord, offset):
        return coord + offset
