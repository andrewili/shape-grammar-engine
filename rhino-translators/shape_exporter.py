#   shape_exporter.py

import rhinoscriptsyntax as rs

class ShapeExporter(object):
    def __init__(self):
        self.tab = '    '
        self.is_string = ''

    def export_shape(self):
        guids_in = self._receive_guids()
        element_lists = self._make_indexed_element_lists(guids_in)
        is_string = self._compose_string(element_lists)
        self._write_file(is_string)

    def _receive_guids(self):
        """Prompts for curve and textdot guids
        Returns a non-empty list of all selected guids: 
            [guid, ...]
        """
        prompt_for_elements = 'Select curves and textdots'
        prompt_for_non_empty_elements = (
            'The shape may not be empty. Select curves and textdots')
        guids = rs.GetObjects(
            prompt_for_elements, 
            rs.filter.curve + rs.filter.textdot)
        while guids == None:
            guids = rs.GetObjects(
                prompt_for_non_empty_elements, 
                rs.filter.curve + rs.filter.textdot)
        return guids

    def _make_indexed_element_lists(self, guids_in):
        """Receives a list of guids:
            [guid, ...]
        Returns a tuple of ordered lists of coords, codex-codex pairs, and
        codex-label pairs:
            ([(num, num, num), ...], [(int, int), ...], [(int, string), ...])
        """
        self.coords, self.lines, self.lpoints = (
            self._make_element_lists(guids_in))
        self.ordered_coord_list = self._make_ordered_coord_list(self.coords)
        self.ordered_codex_codex_list = (
            self._make_ordered_codex_codex_list(self.lines))
        self.ordered_codex_label_list = (
            self._make_ordered_codex_label_list(self.lpoints))
        indexed_element_lists = (
            self.ordered_coord_list, 
            self.ordered_codex_codex_list, 
            self.ordered_codex_label_list)
        return indexed_element_lists

    def _make_element_lists(self, guids):
        """Receives a list of guids:
            [guid, ...]
        Returns lists of coords, lines, and textdots:
            (   [(num, num, num), ...], 
                [((num, num, num), (num, num, num)), ...],
                [((num, num, num), str), ...]
            )
        """
        coords, lines, lpoints = [], [], []
        line_type = 4
        textdot_type = 8192
        # if not type(guids) == list:
        #     guids = []
        for guid in guids:
            guid_type = rs.ObjectType(guid)
            if guid_type == line_type:
                line_coords = self._get_line_coords(guid)
                lines.append(line_coords)
                for coord in line_coords:
                    coords.append(coord)
            elif guid_type == textdot_type:
                coord = self._get_coord(guid)
                label = self._get_label(guid)
                coords.append(coord)
                lpoint = (coord, label)
                lpoints.append(lpoint)
        element_lists = (coords, lines, lpoints)
        return element_lists

    def _get_line_coords(self, line_guid):
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

    def _get_coord(self, textdot_guid):
        """Receives a textdot guid:
            guid
        Returns its coord:
            (num, num, num)
        """
        point = rs.TextDotPoint(textdot_guid)
        coord = (point.X, point.Y, point.Z)
        return coord

    def _get_label(self, textdot_guid):
        """Receives a textdot guid:
            guid
        Returns its text:
            str
        """
        string = rs.TextDotText(textdot_guid)
        return string
        
    def _make_ordered_coord_list(self, coords):
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

    def _make_ordered_codex_codex_list(self, lines):
        """Receives a list of coord-coord pairs:
            [((num, num, num), (num, num, num)), ...]
        Returns an ordered list of codex-codex pairs:
            [(int, int), ...]
        """
        codex_codex_list = []
        for line in lines:
            coord1, coord2 = line
            codex1 = self._get_coord_index(coord1)
            codex2 = self._get_coord_index(coord2)
            codex_codex = (codex1, codex2)
            codex_codex_list.append(codex_codex)
        return sorted(codex_codex_list)

    def _get_coord_index(self, coord):
        """Receives a coord:
            (num, num, num)
        Returns its index:
            int
        """
        cordex = self.ordered_coord_list.index(coord)
        return cordex
        
    def _make_ordered_codex_label_list(self, lpoints):
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

    def _compose_string(self, element_lists):
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
        indented_name_string = self._make_indented_name_string()
        indented_coord_entries_string = (
            self._make_indented_coord_entries_string(self.ordered_coord_list))
        blank_line = ''
        indented_line_entries_string = (
            self._make_indented_line_entries_string())
        indented_point_entries_string = (
            self._make_indented_lpoint_entries_string())
        substrings = [
            indented_name_string,
            indented_coord_entries_string,
            blank_line,
            indented_line_entries_string,
            indented_point_entries_string,
            blank_line]
        string = '\n'.join(substrings)
        return string

    def _make_header_string(self, shape_name='shape-name'):
        string = 'shape ' + shape_name
        return string

    def _make_indented_name_string(self, name='name'):
        string = self.tab + 'name'
        return string

    def _make_indented_coord_entries_string(self, ordered_coord_list):
        """Returns a string composed of indented coord entry strings:
            <tab><coord entry 1>\n...
        """
        indented_entry_strings = []
        for coord in ordered_coord_list:
            entry_string = (
                self._make_coord_entry_string(coord))
            indented_entry_string = self.tab + entry_string
            indented_entry_strings.append(indented_entry_string)
        indented_entries_string = '\n'.join(indented_entry_strings)
        return indented_entries_string

    def _make_coord_entry_string(self, coord):
        """Receives a coord:
            (num, num, num)
        Returns a coord entry string:
            coords <codex str> <x str> <y str> <z str>
        """
        codex = self.ordered_coord_list.index(coord)
        x, y, z = coord
        string = 'coords %i %s %s %s' % (codex, x, y, z)
        return string

    def _make_indented_line_entries_string(self):
        """Returns a string composed of indented line entry strings:
            <tab><line entry 1>\n...
        """
        entry_strings = []
        for codex_codex in self.ordered_codex_codex_list:
            entry_string = self._make_line_entry_string(codex_codex)
            indented_entry_string = self.tab + entry_string
            entry_strings.append(indented_entry_string)
        entries_string = '\n'.join(entry_strings)
        return entries_string

    def _make_line_entry_string(self, codex_codex):
        """Receives a codex-codex pair:
            (int, int)
        Returns a line entry string:
            line <linex str> <coord_index_1> <coord_index_2>
        """
        codex1, codex2 = codex_codex
        linex = self.ordered_codex_codex_list.index(codex_codex)
        line_entry_string = 'line %i %i %i' % (linex, codex1, codex2)
        return line_entry_string

    def _make_indented_lpoint_entries_string(self):
        """Returns a string composed of indented point entry strings:
            <tab><point entry 1>\n...
        """
        indented_lpoint_entry_strings = []
        for codex_label in self.ordered_codex_label_list:
            lpoint_entry_string = self._make_lpoint_entry_string(codex_label)
            indented_lpoint_entry_string = self.tab + lpoint_entry_string
            indented_lpoint_entry_strings.append(indented_lpoint_entry_string)
        lpoint_entries_string = '\n'.join(indented_lpoint_entry_strings)
        return lpoint_entries_string

    def _make_lpoint_entry_string(self, codex_label):
        """Receives a codex-label pair:
            (int, str)
        Returns an lpoint entry string:
            point <codex str> <label>
        """
        codex, label = codex_label
        lpoint_entry_string = 'point %i %s' % (codex, label)
        return lpoint_entry_string
        
    def _write_file(self, string):
        """Prompts for a file name with is extension. Writes the string to the
        file
        """
        shape_name = rs.GetString(
            'Enter the name of the shape', 'shape name')
        header = self._make_header_string(shape_name)
        headed_string = '\n'.join([header, string])
        filter = "IS file (*.is)|*.is|All files (*.*)|*.*||"
        file_name = (
            rs.SaveFileName('Save shape as', filter, '', shape_name))
        if not file_name: return
        file = open(file_name, "w" )
        file.write(headed_string)
        file.close()
        print(headed_string)

if __name__ == '__main__':
    shape_exporter = ShapeExporter()
    shape_exporter.export_shape()
