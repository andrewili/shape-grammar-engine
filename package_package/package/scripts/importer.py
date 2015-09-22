import copy
from package.scripts import double_arrow as da
import rhinoscriptsyntax as rs
from package.scripts import rule as r
from package.scripts import settings as s
from package.scripts import shape

# move to Controller?
# rename DatToGuids? DatToDrawing?
# cf Grammar.export_grammar: class methods

class Importer(object):
    def __init__(self):
        pass

    ###
    def import_derivation(self):
        """Prompts the user for a drv file. Draws the derivation: one shape 
        per layer (name?); rule name. Layout? 
            ##  At least two labeled shapes
        """
        drv_file_text_lines = self._get_text_lines_from_drv_file()
                            ##  what if not well-formed?
        derivation_text_lines = self._extract_derivation_text_lines(
            drv_file_text_lines)                ##  cf. import_final_shape
        labeled_shape_string_list_list, rule_names = (
            self._get_labeled_shape_strings_and_rule_names(
                derivation_text_lines))
        shapes = []
        for labeled_shape_string_list in labeled_shape_string_list_list:
            new_shape = shape.Shape.new_from_is_text_lines(
                labeled_shape_string_list)
            shapes.append(new_shape)
        self._draw_derivation(shapes, rule_names)

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
                            [str]. A list of the text lines (without line 
                            feeds) making up the drv file. 
        """
        filter = "Derivation files (*.drv)|*.drv|All files (*.*)|*.*||"
        filename = rs.OpenFileName('Open derivation file', filter)
        if not filename:
            return
        file = open(filename, 'r')
        untrimmed_drv_file_text_lines = file.readlines()
        file.close()
        trimmed_drv_file_text_lines = self._trim(untrimmed_drv_file_text_lines)
        return trimmed_drv_file_text_lines

    def _trim(self, untrimmed_drv_file_text_lines):
        """Receives:
            untrimmed_drv_file_text_lines
                            [str]. A list of drv file text lines with line 
                            feeds
        Returns:
            trimmed_drv_file_text_lines
                            [str]. A list of drv file text lines without line 
                            feeds
        """
        trimmed_drv_file_text_lines = []
        for untrimmed_text_line in untrimmed_drv_file_text_lines:
            if untrimmed_text_line.endswith('\n'):
                trimmed_text_line = untrimmed_text_line[:-1]
                trimmed_drv_file_text_lines.append(trimmed_text_line)
                # text_line = text_line[:-1]
            else:
                pass
        return trimmed_drv_file_text_lines

    def _extract_derivation_text_lines(self, drv_file_text_lines):
        """Receives:
            drv_file_text_lines 
                            [str]. A list of the text lines in the drv file, 
                            i.e., including the grammar

        Returns:
            derivation_text_lines
                            [str]. A list of the text lines in the derivation 
                            only, i.e., excluding the grammar
        """
        for text_line in drv_file_text_lines:
            if text_line == '# derivation record':
                drv_file_text_lines = drv_file_text_lines[1:]
                break
            else:
                drv_file_text_lines = drv_file_text_lines[1:]
        return drv_file_text_lines
    
    def _get_labeled_shape_strings_and_rule_names(
        self, derivation_text_lines
    ):
        """Receives:
            derivation_text_lines
                            [str]. A list of text lines of a derivation
        Sorts the lines into labeled shapes and rules. Returns:
            labeled_shape_string_list_list
                            [[str]]. A list of lists of labeled shape .is 
                            strings
            rule_names      [str]. A list of rule names
        """
        labeled_shape_string_list_list = []
        rule_names = []
        for text_line in derivation_text_lines:
            first_4_chars = text_line[:4]
            if first_4_chars == 'shap':
                labeled_shape_string_list = [text_line]
            elif first_4_chars == '    ':
                labeled_shape_string_list.append(text_line)
            elif first_4_chars == '':
                labeled_shape_string_list.append(text_line)
            elif first_4_chars == 'rule':
                labeled_shape_string_list_list.append(
                    labeled_shape_string_list)
                rule_name = text_line[8:]
                rule_names.append(rule_name)
            else:
                pass
        labeled_shape_string_list_list.append(
            labeled_shape_string_list)
        return (labeled_shape_string_list_list, rule_names)

    def _extract_raw_derivation_text_lines(self, drv_file_text_lines):
        """Receives:
            drv_file_text_lines
                            [str]. A list of drv_file_text_lines (with line 
                            feeds)
        Returns:
           raw_derivation_text_lines
                            [str]. A list of the derivation text lines (with 
                            line feeds) composing the derivation 
        """
        raw_derivation_text_lines = []
        return raw_derivation_text_lines

    def _trim_raw_derivation_text_lines(self, raw_derivation_text_lines):
        """Receives:
            raw_derivation_text_lines
                            [str]. A list of derivation text lines (with line 
                            feeds)
        Returns:
            derivation_text_lines
                            [str]. A list of trimmed derivation text lines 
                            (without line feeds)
        """
        derivation_text_lines = []
        return derivation_text_lines

    def _draw_derivation(self, labeled_shapes, rule_names):
        """Receives:
            labeled_shapes  [Shape]. A list of labeled shape objects, n >= 2
            rule_names      [str]. A list of rule names, n >= 1
        Draws the derivation, i.e., the labeled shapes, rule names, and 
        arrows
        """
        layer_name = s.Settings.default_layer_name
        rs.CurrentLayer(layer_name)
        i = 0
        n = len(labeled_shapes)
        derivation_element_positions = (
            s.Settings.get_derivation_cell_position_triples(n))
        for i in range(n - 1):
            (   labeled_shape_position_i,
                arrow_position_i, 
                rule_name_position_i) = derivation_element_positions[i]
            labeled_shape_i = labeled_shapes[i]
            rule_name_i = rule_names[i]
            self._draw_double_arrow(arrow_position_i)
            self._write_rule_name(rule_name_i, rule_name_position_i)
            self._draw_labeled_shape(
                labeled_shape_i, labeled_shape_position_i)
        final_labeled_shape = labeled_shapes[-1]
        final_labeled_shape_position = derivation_element_positions[-1][0]
        self._draw_labeled_shape(
            final_labeled_shape, final_labeled_shape_position)

    def _draw_double_arrow(self, position):
        """Receives:
            arrow_position  Point3d
        Inserts a double arrow block instance at the specified position 
        """
        da.DoubleArrow.new_instance(position)

    def _write_rule_name(self, name, position):
        """Receives:
            name            str. The name of the rule
            position        Point3d
        Writes the rule name at the given position
        """
        height = 2
        font = 'Arial'
        font_style = 0
        justified_center = 2
        rs.AddText(name, position, height, font, font_style, justified_center)

    def _draw_labeled_shape(self, labeled_shape, labeled_shape_position):
        """Receives:
            labeled_shape   Shape
            labeled_shape_position
                            Point3d
        Draws a labeled shape at the given position
        """
        po = labeled_shape_position
        line_specs = labeled_shape.get_line_specs()
        labeled_point_specs = labeled_shape.get_lpoint_specs()
        for line_spec in line_specs:
            p0, p1 = line_spec
            po0 = rs.PointAdd(po, p0)
            po1 = rs.PointAdd(po, p1)
            rs.AddLine(po0, po1)
        for labeled_point_spec in labeled_point_specs:
            p0, label = labeled_point_spec
            po0 = rs.PointAdd(po, p0)
            rs.AddTextDot(label, po0)

    def _draw_square_32(self, position):
        """Receives:
            position        Point3d
        Draws a square of 32 units at the given position
        """
        po = position
        p00 = (0, 0, 0)
        p01 = (0, 32, 0)
        p10 = (32, 0, 0)
        p11 = (32, 32, 0)
        po00 = rs.PointAdd(po, p00)
        po01 = rs.PointAdd(po, p01)
        po10 = rs.PointAdd(po, p10)
        po11 = rs.PointAdd(po, p11)
        rs.AddLine(po00, po01)
        rs.AddLine(po00, po10)
        rs.AddLine(po01, po11)
        rs.AddLine(po10, po11)

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

        new_rule = r.Rule.new_from_rul_text_lines(contents)
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

