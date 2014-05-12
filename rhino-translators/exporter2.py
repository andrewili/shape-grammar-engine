#   exporter2.py

# import rhinoscriptsyntax as rs

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
            'Select elements', 
            rs.filter.curve + rs.filter.textdot)
        return elements

    def make_indexed_element_lists(self, elements_in):
        """Receives a list of element Guids:
            [Guids, ...]
        Returns a tuple of sorted lists of coords, line coord index pairs, and
        lpoint coord indices:
            ([(num, num, num), ...], [(int, int), ...], [(int, string), ...])
        """
        coords, lines, lpoints = self.make_element_lists(elements_in)
        self.indexed_coord_list = self.make_indexed_coord_list(coords)
        self.indexed_line_coord_pair_list = (
            self.make_indexed_line_coord_pair_list(lines))
        self.indexed_lpoint_coord_list = (
            self.make_indexed_lpoint_list(lpoints))
        indexed_element_lists = (
            self.indexed_coord_list, 
            self.indexed_line_coord_pair_list, 
            self.indexed_lpoint_coord_list)
        return indexed_element_lists

    def make_element_lists(self, elements):
        """Receives a list of element Guids:
            [Guid, ...]
        Returns lists of coords, lines, and lpoints:
            (   [(num, num, num), ...], 
                [((num, num, num), (num, num, num)), ...],
                [((num, num, num), str), ...]
            )
        """
        element_lists = ('<coord list>', '<line list', '<lpoint list>')
        return element_lists

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
            coord1, coord2 = line
            index1 = self.indexed_coord_list.index(coord1)
            index2 = self.indexed_coord_list.index(coord2)
            coord_index_pair = (index1, index2)
            line_coord_pair_list.append(coord_index_pair)
        return sorted(line_coord_pair_list)

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

    def compose_string(self):
        pass

    def write_file(self):
        pass

if __name__ == '__main__':
    # exporter2 = Exporter2()
    # exporter2.export_shape()
    import doctest
    doctest.testfile('tests/exporter2_test.txt')
