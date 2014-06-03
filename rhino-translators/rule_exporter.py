#   rule_exporter.py

# import rhinoscriptsyntax as rs

class RuleExporter(object):
    def __init__(self):
        # self.ordered_coord_list = []          #   [(num, num, num), ...]
        # self.ordered_codex_codex_list = []    #   [(int, int), ...]
        # self.ordered_codex_label_list = []    #   [(int, str), ...]
        self.tab = '    '
        self.is_string = ''

    def export_rule(self):
        left_guids = self.get_guids('left')
        right_guids = self.get_guids('right')
        left_element_lists = self.make_indexed_element_lists(left_guids)
        right_element_lists = self.make_indexed_element_lists(right_guids)
        rul_string = self.compose_unnamed_rul_string(
            left_element_lists, right_element_lists)
        self.write_rul_file(rul_string)

    # def export_shape(self):
    #     guids_in = self.get_guids()
    #     element_lists = self.make_indexed_element_lists(guids_in)
    #     is_string = self.compose_string(element_lists)
    #     self.write_file(is_string)

    def get_guids(self, side):
        """Receives a string indicating the side of the rule:
            'left' or 'right'
        Prompts for the shape's curve guids, textdot guids, and name. Returns
        a triple consisting of the side, the name, and a list of all selected
        guids: 
            (str, str, [guid, ...])
        """
        # Check for empty shape
        if side == 'left':
            prompt_for_elements = (
                'Select the curves and textdots in the left shape')
            prompt_for_name = (
                'Enter the name of the left shape. It must be unique.')
        elif side == 'right':
            prompt_for_elements = (
                'Select the curves and textdots in the right shape')
            prompt_for_name = (
                'Enter the name of the right shape. It must be unique.')
        else:
            message = "The argument must be 'left' or 'right'"
            print(message)
        guids = rs.GetObjects(
            prompt_for_elements,
            rs.filter.curve + rs.filter.textdot)
        name = rs.GetString(prompt_for_name)
        side_name_guids = (side, name, guids)
        return side_name_guids

    def make_indexed_element_lists(self, side_name_guids):
        """Receives a triple: side; shape name; and list of guids:
            (   str,
                str,
                [guid, ...])
        Returns a 5-tuple: side; shape name; ordered lists of coords, 
        codex-codex pairs, and codex-label pairs:
            (   str,
                str,
                [(num, num, num), ...],
                [(int, int), ...],
                [(int, string), ...])
        """
        self.coords, self.lines, self.lpoints = (
            self.make_element_lists(side_name_guids))
        self.ordered_coord_list = self.make_ordered_coord_list(self.coords)
        self.ordered_codex_codex_list = (
            self.make_ordered_codex_codex_list(self.lines))
        self.ordered_codex_label_list = (
            self.make_ordered_codex_label_list(self.lpoints))
        indexed_element_lists = (
            self.ordered_coord_list, 
            self.ordered_codex_codex_list, 
            self.ordered_codex_label_list)
        return indexed_element_lists

    def make_element_lists(self, guids):
        """Receives a list of guids:
            [guid, ...]
        Returns a triple of lists of coords, lines, and textdots:
            (   [(num, num, num), ...], 
                [((num, num, num), (num, num, num)), ...],
                [((num, num, num), str), ...])
        """
        coords, lines, lpoints = [], [], []
        line_type = 4
        textdot_type = 8192
        for guid in guids:
            guid_type = rs.ObjectType(guid)
            if guid_type == line_type:
                # lines.append(guid)   #   adds a Guid!
                line_coords = self.get_line_coords(guid)
                lines.append(line_coords)
                for coord in line_coords:
                    coords.append(coord)
            elif guid_type == textdot_type:
                coord = self.get_coord(guid)
                label = self.get_label(guid)
                coords.append(coord)
                lpoint = (coord, label)
                lpoints.append(lpoint)
        element_lists = (coords, lines, lpoints)
        return element_lists

    def get_line_coords(self, line_guid):
        """Receives a line guid:
            guid
        Returns the line guid's coord pair:
            [(num, num, num), (num, num, num)]
        """
        point_pair = rs.CurvePoints(line_guid)
        coord_pair = []
        for point in point_pair:
            coord = (point.X, point.Y, point.Z)
            coord_pair.append(coord)
        return coord_pair

    def get_coord(self, textdot_guid):
        """Receives a textdot guid:
            guid
        Returns its coord:
            (num, num, num)
        """
        point = rs.TextDotPoint(textdot_guid)
        coord = (point.X, point.Y, point.Z)
        return coord

    def get_label(self, textdot_guid):
        """Receives a textdot guid:
            guid
        Returns its text:
            str
        """
        string = rs.TextDotText(textdot_guid)
        return string
        
    def make_ordered_coord_list(self, coords):
        """Receives a list of coords:
            [(num, num, num), ...]
        Returns an ordered list of unique coords:
            [(num, num, num), ...]
        """
        coord_list = []
        for coord in coords:
            if not coord in coord_list:
                coord_list.append(coord)
        # print('coords: %s' % coords)
        # print('ordered coord list: %s' % sorted(coord_list))
        return sorted(coord_list)

    def make_ordered_codex_codex_list(self, lines):
        """Receives a list of coord-coord pairs:
            [((num, num, num), (num, num, num)), ...]
        Returns an ordered list of codex-codex pairs:
            [(int, int), ...]
        """
        codex_codex_list = []
        for line in lines:
            coord1, coord2 = line
            codex1 = self.get_coord_index(coord1)
            codex2 = self.get_coord_index(coord2)
            codex_codex = (codex1, codex2)
            codex_codex_list.append(codex_codex)
        return sorted(codex_codex_list)

    def get_coord_index(self, coord):
        """Receives a coord:
            (num, num, num)
        Returns its index:
            int
        """
        cordex = self.ordered_coord_list.index(coord)
        return cordex
        
    def make_ordered_codex_label_list(self, lpoints):
        """Receives a list of labeled points:
            [((num, num, num), string), ...]
        Returns a list of codex-label pairs:
            [(int, string), ...]
        """
        codex_label_list = []
        for lpoint in lpoints:
            coord, label = lpoint
            codex = self.ordered_coord_list.index(coord)
            codex_label = (codex, label)
            codex_label_list.append(codex_label)
        return sorted(codex_label_list)

    def compose_unnamed_rul_string(
        self, left_element_lists, right_element_lists
    ):
        """Receives two element lists: one for each rule shape. Each list 
        contains a 5-tuple of 1) the side; 2) the name of the shape; 3) an 
        ordered list of coords; 4) an ordered list of codex-codex pairs; and 
        5) an ordered list of codex-label pairs:
            (   str,
                str,
                [(num, num, num), ...],
                [(int, int), ...],
                [(int, string), ...])
            )
            (   str,
                str,
                [(num, num, num), ...],
                [(int, int), ...],
                [(int, string), ...])
            )
        Returns an unnamed string in the rul format:
            shape <rule name>_L
            <tab><left shape name>
            <tab><left coord entry 1>
            ...
            <blank line>
            <tab><left line entry 1>
            ...
            <blank line>
            <tab><left point entry 1>
            ...
            shape <rule name>_R
            <tab><right shape name>
            <tab><right coord entry 1>
            ...
            <blank line>
            <tab><right line entry 1>
            ...
            <blank line>
            <tab><right point entry 1>
            ...
        """
        left_named_shape_string = self.make_named_shape_string(
            left_element_lists)
        right_named_shape_string = self.make_named_shape_string(
            right_element_lists)
        rul_substrings = [
            left_named_shape_string,
            right_named_shape_string]
        unnamed_rul_string = '\n'.join(rul_substrings)
        return unnamed_rul_string

    def make_named_shape_string(self, element_lists):
        """Receives a 5-tuple of 1) the side; 2) the name of the shape; 3) an 
        ordered list of coords; 4) a left-shape triple; and 5) a right_shape 
        triple:
            (   str,
                str,
                [(num, num, num), ...],
                [(int, int), ...],
                [(int, string), ...])
            )
        Returns a named shape string:
            shape <rule name>_<side>            #   need the rule name!
            <tab><left shape name>
            <tab><left coord entry 1>
            ...
            <blank line>
            <tab><left line entry 1>
            ...
            <blank line>
            <tab><left point entry 1>
            ...
        """
        return named_shape_string

    def compose_string(self, element_lists):
        """Receives a list of coordinates, a list of codex-codex pairs, and a
        list of codex-label pairs:
            ([(num, num, num), ...], [(int, int), ...], [(int, string), ...])
        Returns a string in IS format:
            <tab><name>
            <tab><coord entry 1>
            ...
            <blank line>
            <tab><line entry 1>
            ...
            <blank line>
            <tab><point entry 1>
            ...
        """
        # header_string = self.make_header_string()
        indented_name_string = self.make_indented_name_string()
        indented_coord_entries_string = (
            self.make_indented_coord_entries_string(self.ordered_coord_list))
        blank_line = ''
        indented_line_entries_string = (
            self.make_indented_line_entries_string())
        indented_point_entries_string = (
            self.make_indented_lpoint_entries_string())
        substrings = [
            # header_string,
            indented_name_string,
            indented_coord_entries_string,
            blank_line,
            indented_line_entries_string,
            indented_point_entries_string,
            blank_line]
        string = '\n'.join(substrings)
        return string

    def make_header_string(self, shape_name='shape-name'):
        string = 'shape ' + shape_name
        return string

    def make_indented_name_string(self, name='name'):
        string = self.tab + 'name'
        return string

    def make_indented_coord_entries_string(self, ordered_coord_list):
        """Returns a string composed of indented coord entry strings:
            <tab><coord entry 1>\n...
        """
        indented_entry_strings = []
        for coord in ordered_coord_list:
            entry_string = (
                self.make_coord_entry_string(coord))
            indented_entry_string = self.tab + entry_string
            indented_entry_strings.append(indented_entry_string)
        indented_entries_string = '\n'.join(indented_entry_strings)
        return indented_entries_string

    def make_coord_entry_string(self, coord):
        """Receives a coord:
            (num, num, num)
        Returns a coord entry string:
            coords <codex str> <x str> <y str> <z str>
        """
        codex = self.ordered_coord_list.index(coord)
        x, y, z = coord
        string = 'coords %i %s %s %s' % (codex, x, y, z)
        return string

    def make_indented_line_entries_string(self):
        """Returns a string composed of indented line entry strings:
            <tab><line entry 1>\n...
        """
        entry_strings = []
        for codex_codex in self.ordered_codex_codex_list:
            entry_string = self.make_line_entry_string(codex_codex)
            indented_entry_string = self.tab + entry_string
            entry_strings.append(indented_entry_string)
        entries_string = '\n'.join(entry_strings)
        return entries_string

    def make_line_entry_string(self, codex_codex):
        """Receives a codex-codex pair:
            (int, int)
        Returns a line entry string:
            line <linex str> <coord_index_1> <coord_index_2>
        """
        codex1, codex2 = codex_codex
        linex = self.ordered_codex_codex_list.index(codex_codex)
        line_entry_string = 'line %i %i %i' % (linex, codex1, codex2)
        return line_entry_string

    def make_indented_lpoint_entries_string(self):
        """Returns a string composed of indented point entry strings:
            <tab><point entry 1>\n...
        """
        indented_lpoint_entry_strings = []
        for codex_label in self.ordered_codex_label_list:
            lpoint_entry_string = self.make_lpoint_entry_string(codex_label)
            indented_lpoint_entry_string = self.tab + lpoint_entry_string
            indented_lpoint_entry_strings.append(indented_lpoint_entry_string)
        lpoint_entries_string = '\n'.join(indented_lpoint_entry_strings)
        return lpoint_entries_string

    def make_lpoint_entry_string(self, codex_label):
        """Receives a codex-label pair:
            (int, str)
        Returns an lpoint entry string:
            point <codex str> <label>
        """
        codex, label = codex_label
        lpoint_entry_string = 'point %i %s' % (codex, label)
        return lpoint_entry_string

    def write_rul_file(self, unnamed_rul_string):
        """Prompts for a file (rule) name with the rul extension. Appends the 
        rule name string. Fills in the rule shape names and writes the named 
        rul string to the file
            rule    <rule name>    <rule name>_L -> <rule name>_R
        """
        rule_name = '<rule name>'
        named_rul_string = self.make_named_rul_string(
            unnamed_rul_string, rule_name)
        print(named_rul_string)

    def make_named_rul_string(self, unnamed_rul_string, rule_name):
        """Receives an unnamed rule string and a rule name:
            str
            str
        Fills in the rule shape names and appends the named rul string. 
        Returns the resulting string in the rul format:
            str
        """
        named_rul_string = '<named rul string>'
        return named_rul_string

    # def write_file(self, string):
    #     """Prompts for a file name with is extension. Writes the string to the
    #     file
    #     """
    #     shape_name = rs.GetString(
    #         'Enter the name of the shape', 'shape name')
    #     header = self.make_header_string(shape_name)
    #     headed_string = '\n'.join([header, string])
    #     filter = "IS file (*.is)|*.is|All files (*.*)|*.*||"
    #     file_name = (
    #         rs.SaveFileName('Save shape as', filter, '', shape_name))
    #     if not file_name: return
    #     file = open(file_name, "w" )
    #     file.write(headed_string)
    #     file.close()
    #     print(headed_string)

if __name__ == '__main__':
    # rule_exporter = RuleExporter()
    # rule_exporter.export_rule()
    import doctest
    doctest.testfile('tests/rule_exporter_test.txt')
