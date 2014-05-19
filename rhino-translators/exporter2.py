#   exporter2.py

import rhinoscriptsyntax as rs

class Exporter2(object):
    def __init__(self):
        self.indexed_coord_list = []
        self.indexed_line_coord_pair_list = []
        self.indexed_lpoint_list = []
        self.is_string = ''

    def export_shape(self):
        elements_in = self.receive_elements()
        element_lists = self.make_indexed_element_lists(elements_in)
        is_string = self.compose_string(element_lists)
        self.write_file(is_string)

    def receive_elements(self):
        """Prompts for curves and textdots.
        Returns a list of all selected elements: 
            [Guid, ...]
        """
        elements = rs.GetObjects(
            'Select curves and textdots', 
            rs.filter.curve + rs.filter.textdot)
        return elements

    def make_indexed_element_lists(self, elements_in):
        """Receives a list of element Guids:
            [Guids, ...]
        Returns a tuple of sorted lists of coords, line coord index pairs, and
        lpoint coord indices:
            ([(num, num, num), ...], [(int, int), ...], [(int, string), ...])
        """
        self.coords, self.lines, self.lpoints = (
            self.make_element_lists(elements_in))
        self.indexed_coord_list = self.make_indexed_coord_list(self.coords)
        self.indexed_line_coord_pair_list = (
            self.make_indexed_line_coord_pair_list(self.lines))
        self.indexed_lpoint_coord_list = (
            self.make_indexed_lpoint_list(self.lpoints))
        indexed_element_lists = (
            self.indexed_coord_list, 
            self.indexed_line_coord_pair_list, 
            self.indexed_lpoint_coord_list)
        return indexed_element_lists

    def make_element_lists(self, elements):
        """Receives a list of element Guids:
            [Guid, ...]
        Returns lists of coords, lines, and textdots:
            (   [(num, num, num), ...], 
                [((num, num, num), (num, num, num)), ...],
                [((num, num, num), str), ...]
            )
        """
        coords, lines, lpoints = [], [], []
        line_type = 4
        textdot_type = 8192
        for element in elements:
            element_type = rs.ObjectType(element)
            if element_type == line_type:
                # lines.append(element)   #   adds a Guid!
                line_coords = self.get_line_coords(element)
                lines.append(line_coords)
                for coord in line_coords:
                    coords.append(coord)
            elif element_type == textdot_type:
                coord = self.get_coord(element)
                label = self.get_label(element)
                coords.append(coord)
                lpoint = (coord, label)
                lpoints.append(lpoint)
        element_lists = (coords, lines, lpoints)
        return element_lists

    def get_line_coords(self, line):
        """Receives a line Guid:
            Guid
        Returns the line's coord pair:
            [(num, num, num), (num, num, num)]
        """
        point_pair = rs.CurvePoints(line)
        coord_pair = []
        for point in point_pair:
            coord = (point.X, point.Y, point.Z)
            coord_pair.append(coord)
        return coord_pair

    def get_coord(self, textdot):
        """Receives a textdot Guid:
            Guid
        Returns its coord:
            (num, num, num)
        """
        point = rs.TextDotPoint(textdot)
        coord = (point.X, point.Y, point.Z)
        return coord

    def get_label(self, textdot):
        """Receives a textdot Guid:
            Guid
        Returns its text:
            str
        """
        string = rs.TextDotText(textdot)
        return string
        
    def make_indexed_coord_list(self, coords):
        """Receives a list of coords:
            [(num, num, num), ...]
        Returns an ordered list of unique coords:
            [(num, num, num), ...]
        """
        coord_list = []
        for coord in coords:
            if not coord in coord_list:
                coord_list.append(coord)
        return sorted(coord_list)

    def make_indexed_line_coord_pair_list(self, lines):
        """Receives a list of line coord pairs:
            [((num, num, num), (num, num, num)), ...]
        Returns an ordered list of line coord index pairs:
            [(int, int), ...]
        """
        line_coord_pair_list = []
        for line in lines:
            # point_pair = rs.CurvePoints(line)
            coord_pair = line
            # coord_pair = []
            # for point in point_pair:
            #     coord = (point.X, point.Y, point.Z)
            #     coord_pair.append(coord)
            coord_index_pair = []
            for coord in coord_pair:
                index = self.get_coord_index(coord)
                coord_index_pair.append(index)
            line_coord_pair_list.append(coord_index_pair)
        return sorted(line_coord_pair_list)

    def get_coord_index(self, coord):
        """Receives a coord:
            (num, num, num)
        Returns its index:
            int
        """
        coord_index = self.indexed_coord_list.index(coord)
        return coord_index
        
    def make_indexed_lpoint_list(self, lpoints):
        """Receives a list of labeled points:
            [((num, num, num), string), ...]
        Returns a list of index-label pairs:
            [(int, string), ...]
        """
        lpoint_list = []
        for lpoint in lpoints:
            coord, label = lpoint
            index = self.indexed_coord_list.index(coord)
            indexed_lpoint = (index, label)
            lpoint_list.append(indexed_lpoint)
        return sorted(lpoint_list)

    def compose_string(self, element_lists):
        """Receives a list of coordinates, a list of coord index pairs, and a
        list of lpoint index-label pairs:
            ([(num, num, num), ...], [(int, int), ...], [(int, string), ...])
        PROVISIONAL:
        Returns a string of the lists
        """
        substrings = []
        for element_list in element_lists:
            substring = 'element list: %s' % element_list
            substrings.append(substring)
        string = '\n'.join(substrings)
        return string

    def write_file(self, string):
        print(string)

if __name__ == '__main__':
    exporter2 = Exporter2()
    exporter2.export_shape()
    # import doctest
    # doctest.testfile('tests/exporter2_test.txt')
