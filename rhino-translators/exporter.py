#   exporter.py
#   Continues is_file_exporter.py

# import rhinoscriptsyntax as rs

class Exporter(object):
    def __init__(self):
        self.sorted_coord_list = []
        self.sorted_line_coord_index_pair_list = []
        self.sorted_lpoint_coord_list = []      #
        self.tab = '    '

    def export_shape(self):
        """Prompts for labeled points, lines, and shape name. Writes a file in
        IS format
        """
        # selected_lines = rs.GetObjects('Select lines', rs.filter.curve)
        selected_elements = rs.GetObjects(
            'Select elements', 
            rs.filter.curve + rs.filter.textdot)
        selected_lines, selected_textdots = (
            self.sort_elements(selected_elements))
        self.coord_pair_list = self.make_coord_pair_list(selected_lines)
        self.coord_list = self.make_coord_list(selected_textdots)
        self.sorted_coord_list = (
            self.make_sorted_coord_list(
                self.coord_list, self.coord_pair_list)
            )
        # self.sorted_coord_list = (
        #     self.make_sorted_coord_list(self.coord_pair_list))
        self.sorted_line_coord_index_pair_list = (
            self.make_sorted_line_coord_index_pair_list(self.coord_pair_list))
        is_string = self.compose_is_string(
            self.sorted_coord_list, self.sorted_line_coord_index_pair_list)
        self.write_file(is_string)

    def sort_elements(self, elements):
        """Receives a list of line and textdot Guids:
            [Guid, ...]
        Returns a list of line Guids and a list of textdot Guids:
            [line_Guid, ...]
            [textdot_Guid, ...]
        """
        line_type = 4
        textdot_type = 8192
        lines = []
        textdots = []
        for element in elements:
            object_type = rs.ObjectType(element) 
            if object_type == line_type:
                lines.append(element)
            elif object_type == textdot_type:
                textdots.append(element)
        return (lines, textdots)

    def make_coord_pair_list(self, lines_in):
        """Receives a list of line Guids:
            [Guid, ...]
        Returns a list of (non-unique) line coord pairs:
            [((num, num, num), (num, num, num)), ...]
        """
        coord_pair_list = []
        for line in lines_in:
            coord_pair = self.get_coord_pair(line)
            coord_pair_list.append(coord_pair)
        return coord_pair_list

    def get_coord_pair(self, line_in):
        """Receives a line Guid:
            Guid
        Returns the line's coords:
            [(num, num, num), (num, num, num)]
        """
        point_pair = rs.CurvePoints(line_in)
        coord_pair = []
        for point in point_pair:
            coord = (point.X, point.Y, point.Z)
            coord_pair.append(coord)
        return coord_pair

    def make_coord_list(self, textdots):
        """Receives a list of textdot Guids:
            [Guid, ...]
        Returns a list of the textdots' coords:
            [(num, num, num), ...]
        """
        coord_list = []
        for textdot in textdots:
            point = rs.TextDotPoint(textdot)
            coord = point.X, point.Y, point.Z
            coord_list.append(coord)
        return coord_list

    def make_sorted_coord_list(self, coord_list_in, coord_pair_list):
        """Receives a list of line coord pairs and a list of coords:
            [((num, num, num), (num, num, num)), ...]
            [(num, num, num), ...]
        Returns an ordered list of unique coords:
            [(num, num, num), ...]
        """
        coord_list = []
        for coord in coord_list_in:
            if not coord in coord_list:
                coord_list.append(coord)
        for coord_pair in coord_pair_list:
            for coord in coord_pair:
                if not coord in coord_list:
                    coord_list.append(coord)
        return sorted(coord_list)

    # def make_sorted_coord_list(self, coord_pair_list):
    #     """Receives a list of line coord pairs:
    #         [((num, num, num), (num, num, num)), ...]
    #     Returns an ordered list of unique coords:
    #         [(num, num, num), ...]
    #     """
    #     coord_list = []
    #     for coord_pair in coord_pair_list:
    #         for coord in coord_pair:
    #             if not coord in coord_list:
    #                 coord_list.append(coord)
    #     return sorted(coord_list)

    def make_sorted_line_coord_index_pair_list(self, coord_pair_list):
        """Receives a list of line coord pairs:
            [((num, num, num), (num, num, num)), ...]
        Returns an ordered list of unique line coord index pairs from the
        coord list:
            [(int, int), ...]
        """
        index_pair_list = []
        for coord_pair in coord_pair_list:
            index_pair = (
                self.get_index_pair(self.sorted_coord_list, coord_pair))
            if not index_pair in index_pair_list:
                index_pair_list.append(index_pair)
        return sorted(index_pair_list)

    def get_index_pair(self, coord_list, coord_pair):
        """Receives an ordered list of unique coords and a coord pair:
            [((num, num, num), (num, num, num)), ...]
            ((num, num, num), (num, num, num))
        Returns the index of the coord pair in the coord pair list:
            int
        """
        coord1, coord2 = coord_pair
        index1 = coord_list.index(coord1)
        index2 = coord_list.index(coord2)
        index_pair = (index1, index2)
        return index_pair

    def compose_is_string(
        self, 
        coord_list, 
        line_coord_index_pair_list, 
        lpoint_coord_index_list
    ):
        """Receives 2 lists:
            [(num, num, num), ...]
            [(int, int), ...]
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
        indented_name_string = self.make_indented_name_string()
        indented_coord_entries_string = (
            self.make_indented_coord_entries_string())
        blank_line = ''
        indented_line_entries_string = (
            self.make_indented_line_entries_string())
        indented_lpoint_entries_string = (
            self.make_indented_lpoint_entries_string())
        substrings = [
            indented_name_string, 
            indented_coord_entries_string, 
            blank_line, 
            indented_line_entries_string,
            indented_lpoint_entries_string,
            blank_line] 
        string = '\n'.join(substrings)
        return string

    # def compose_is_string(self, coord_list, line_coord_index_pair_list):
    #     """Receives 2 lists:
    #         [(num, num, num), ...]
    #         [(int, int), ...]
    #     Returns a string in IS format:
    #         <tab><name>
    #         <tab><coord entry 1>
    #         ...
    #         <blank line>
    #         <tab><line entry 1>
    #         ...
    #         <blank line>
    #         <tab><point entry 1>
    #         ...
    #     """
    #     indented_name_string = self.make_indented_name_string()
    #     indented_coord_entries_string = (
    #         self.make_indented_coord_entries_string())
    #     blank_line = ''
    #     indented_line_entries_string = (
    #         self.make_indented_line_entries_string())
    #     substrings = [
    #         indented_name_string, 
    #         indented_coord_entries_string, 
    #         blank_line, 
    #         indented_line_entries_string,
    #         blank_line] 
    #     string = '\n'.join(substrings)
    #     return string

    def make_header(self, shape_name='<shape name>'):
        header = 'shape' + ' ' + shape_name
        return header

    def make_indented_name_string(self):
        indented_name_string = self.tab + 'name'
        return indented_name_string

    def make_indented_coord_entries_string(self):
        """Returns a string composed of indented coord entry strings:
            <tab><coord entry>\n<...>
        """
        indented_coord_entry_strings = []
        for coord in self.sorted_coord_list:
            indented_coord_entry_string = (
                self.make_indented_coord_entry_string(coord))
            indented_coord_entry_strings.append(indented_coord_entry_string)
        indented_coord_entries_string = (
            '\n'.join(indented_coord_entry_strings))
        return indented_coord_entries_string

    def make_indented_coord_entry_string(self, coord):
        """Receives a coord:
            (num, num, num)
        Returns an indented coord entry string:
            <tab>coords <i_str> <x_str> <y_str> <z_str>
        """
        i = self.sorted_coord_list.index(coord)
        i_str = str(i)
        x, y, z = coord[0], coord[1], coord[2]
        x_str, y_str, z_str = str(x), str(y), str(z)
        components = [self.tab + 'coords', i_str, x_str, y_str, z_str]
        indented_coord_entry_string = ' '.join(components)
        return indented_coord_entry_string

    def make_indented_line_entries_string(self):
        """Returns a string composed of indented line entry strings:
            <tab><line entry>\n<...>
        """
        indented_line_entry_strings = []
        for index_pair in self.sorted_line_coord_index_pair_list:
            indented_line_entry_string = (
                self.make_indented_line_entry_string(index_pair))
            indented_line_entry_strings.append(indented_line_entry_string)
        indented_line_entries_string = '\n'.join(indented_line_entry_strings)
        return indented_line_entries_string

    def make_indented_line_entry_string(self, index_pair):
        """Receives a line coord index pair:
            (int, int)
        Returns an indented line coord entry string:
            <tab>line <i_str> <coord_index_str_1> <coord_index_str_2>)
        """
        i = self.sorted_line_coord_index_pair_list.index(index_pair) + 1
        i_str = str(i)
        coord_index_1, coord_index_2 = index_pair[0], index_pair[1]
        coord_index_str_1, coord_index_str_2 = (
            str(coord_index_1), str(coord_index_2))
        components = [
            self.tab + 'line',
            i_str, 
            coord_index_str_1, 
            coord_index_str_2]
        indented_line_entry_string = ' '.join(components)
        return indented_line_entry_string

    def make_indented_lpoint_entries_string(self):
        """Returns a string composed of indented lpoint entry strings:
            <tab><lpoint entry>\n<...>
        """
        indented_lpoint_entry_strings = []
        for lpoint in self.sorted_lpoint_list:  #
            indented_lpoint_entry_string = '    Kilroy'
            indented_lpoint_entry_strings.append(indented_lpoint_entry_string)
        indented_lpoint_entries_string = (
            '\n'.join(indented_lpoint_entry_strings))
        return indented_lpoint_entries_string

    def write_file(self, string):
        """Prompts for a file name with is extension. Writes the string to the
        file
        """
        shape_name = rs.GetString(
            'Enter the name of the shape', '<shape name>')
        # filter = "IS file (*.is)|*.is|All files (*.*)|*.*||"
        # long_file_name = (
        #     rs.SaveFileName('Save shape as', filter, '', shape_name))
        # if not long_file_name: return

        header = ' '.join(['shape', shape_name])
        headed_string = '\n'.join([header, string])
        # file = open(long_file_name, "w" )
        # file.write(headed_string)
        # file.close()
        print(headed_string)

if __name__ == '__main__':
    # exporter = Exporter()
    # exporter.export_shape()
    import doctest
    doctest.testfile('tests/exporter_test.txt')
