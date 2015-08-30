import copy
import rhinoscriptsyntax as rs
from package.scripts import rule
from package.scripts import shape

# move to Controller?
# rename DatToGuids? DatToDrawing?
# cf Grammar.export_grammar: class methods

class Importer(object):
    def __init__(self):
        pass

    ###
    def import_final_shape(self):
        """Prompts the user for a drv file. Draws the final shape in the 
        derivation.
        """
        drv_file_text_lines = self._get_text_lines_from_drv_file()
        final_shape_text_lines = (
            shape.Shape.get_final_shape_text_lines_from_drv_text_lines(
                drv_file_text_lines))
        final_shape = shape.Shape.new_from_is_text_lines(
            final_shape_text_lines)
        self._draw_shape(final_shape)

    def _get_text_lines_from_drv_file(self):
        """Prompts the user for a drv file. Returns: 
            [drv_text_line, ...]
                            [str]. A list of the text lines making up the drv 
                            file
        """
        filter = "Derivation files (*.drv)|*.drv|All files (*.*)|*.*||"
        filename = rs.OpenFileName('Open derivation file', filter)
        if not filename:
            return
        file = open(filename, 'r')
        drv_file_text_lines = file.readlines()
        file.close()
        return drv_file_text_lines

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

    def _draw_shape(self, shape):
        """Receives: 
            Shape
        Draws the shape in Rhino at (0, 0, 0)
        """
        rhino_lines = shape.get_line_specs_as_lists()
        for rhino_line in rhino_lines:
            rhino_p1, rhino_p2 = rhino_line
            rs.AddLine(rhino_p1, rhino_p2)
        rhino_dots = shape.get_rhino_dots()
        for rhino_dot in rhino_dots:
            label, rhino_point = rhino_dot
            rs.AddTextDot(label, rhino_point)

    def import_derivation(self):                            ##  08-19 05:56
        """Prompts the user for a drv file. Draws the derivation: one shape 
        per layer (name?); rule name. Layout? 
            ##  At least two labeled shapes
        """
        drv_file_text_lines = self._get_text_lines_from_drv_file()
                                                            ##  here
                            ##  what if not well-formed?
        labeled_shape_string_list_list, rule_names = (
            self._get_labeled_shape_strings_and_rule_names(
                drv_file_text_lines))
        shapes = []
        for labeled_shape_string_list in labeled_shape_string_list_list:
            new_shape = Shape.new_from_is_text_lines(
                labeled_shape_string_list)
            shapes.append(new_shape)
        self._draw_derivation(shapes, rule_names)

    def _get_labeled_shape_strings_and_rule_names(
        self, drv_file_text_lines
    ):                                                      ##  08-23 09:40
        """Receives:
            drv_file_text_lines
                            [str]. A list of text lines of a .drv file
        Sorts the lines into labeled shapes and rules. Returns:
            labeled_shape_string_list_list
                            [[str]]. A list of lists of labeled shape .is 
                            strings
            rule_names      [str]. A list of rule names
        """
        derivation_record = self._extract_derivation_text_lines(
            drv_file_text_lines)
                            ##  'shape    <shape_name>'
                            ##      ...
                            ##  'rule    <rule_name>'
                            ##  ...
        labeled_shape_string_list_list = []
        rule_names = []
        for text_line in derivation_record:
            first_4_chars = text_line[:4]
            if first_4_chars == 'shap':
                labeled_shape_string_list = [text_line]
            elif first_4_chars == '    ':
                labeled_shape_string_list.append(text_line)
            elif first_4_chars == '':
                pass
            elif first_4_chars == 'rule':
                labeled_shape_string_list.append(text_line)
                labeled_shape_string_list_list.append(
                    labeled_shape_string_list)
                rule_name = text_line[8:]
                rule_names.append(rule_name)
            else:
                pass
        labeled_shape_string_list_list.append(
            labeled_shape_string_list)
        return (labeled_shape_string_list_list, rule_names)

    def _extract_derivation_text_lines(self, drv_file_text_lines):# 08-30 09:40
        """Receives:
            drv_file_text_lines 
                            [str]. A list of the text lines in the drv file, 
                            i.e., including the grammar
        Returns:
            derivation_text_lines
                            [str]. A list of the text lines in the derivation 
                            only, i.e., excluding the grammar
        """
        derivation_text_lines = copy.copy(drv_file_text_lines)
        for text_line in derivation_text_lines:
            if not text_line == '# derivation record':
                derivation_text_lines.remove(text_line)
            else:
                derivation_text_lines.remove(text_line)
                break
        return derivation_text_lines
    
    def _draw_derivation(self, labeled_shapes, rule_names): ##  08-26 05:14
        """Receives:
            labeled_shapes  [Shape]. A list of labeled shape objects, n >= 2
            rule_names      [str]. A list of rule names, n >= 1
        Draws the derivation, i.e., the labeled shapes, rule names, and 
        arrows
        """
        i = 0
        n = len(labeled_shapes)
        derivation_element_positions = (
            s.Settings.get_derivation_cell_position_triples(n))
        for i in range(n):
            (   arrow_position_i, 
                rule_name_position_i, 
                labeled_shape_position_i) = derivation_element_positions[i]
            self._draw_arrow(arrow_position_i)
            self._write_rule_name(rule_name_position_i)
            self._draw_labeled_shape_at(
                labeled_shape_i, labeled_shape_position_i)
        final_labeled_shape = labeled_shapes[-1]
        final_labeled_shape_position = derivation_element_positions[-1]
        self._draw_labeled_shape_at(
            final_labeled_shape, final_labeled_shape_position)


