#   importer.py

import rhinoscriptsyntax as rs
import rule
import shape

class Importer(object):
    def __init__(self):
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

        new_rule = rule.Rule.new_from_rul_text(contents)
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

    def _draw_shape(self, shape):
        """Receives: 
            Shape
        Draws the shape in Rhino
        """
        rhino_lines = shape.get_line_specs_as_lists()
        for rhino_line in rhino_lines:
            rhino_p1, rhino_p2 = rhino_line
            rs.AddLine(rhino_p1, rhino_p2)
        rhino_dots = shape.get_rhino_dots()
        for rhino_dot in rhino_dots:
            label, rhino_point = rhino_dot
            rs.AddTextDot(label, rhino_point)
