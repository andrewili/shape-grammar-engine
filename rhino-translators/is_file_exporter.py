#   is_file_exporter.py

import rhinoscriptsyntax as rs
import ledger

class ISFileExporter(object):
    def __init__(self):
        pass

    def export_shape(self):
        lines = rs.GetObjects('Select lines', rs.filter.curve)
        shape = Shape(lines)
        is_string = shape.compose_is_string()
        self.write_file(is_string)

    def write_file(self, string):
        print(string)

class Shape(object):
    def __init__(self, lines):
        """Receives a list of line Guids
            [Guid, ...]
        """
        self.coord_ledger = self.make_new_coord_ledger(lines)
        self.line_ledger = self.make_new_line_ledger(lines)
        self.tab = '    '

    def make_new_coord_ledger(self, lines):
        """Receives a list of line Guids:
            [Guid, ...]
        Returns a list of coords:
            [(num, num, num), ...]
        """
        coords = []
        for line in lines:
            points = rs.CurvePoints(line)
            for p in points:
                coord = (p.X, p.Y, p.Z)
                coords.append(coord)
        coord_ledger = ledger.Ledger(coords)
        return coord_ledger

    def make_new_line_ledger(self, lines):
        """Receives a list of line Guids:
            [Guid, ...]
        Returns a list of line coord index pairs:
            [(int, int), ...]
        """
        index_pairs = []
        for line in lines:
            points = rs.CurvePoints(line)
            coord_pair = []
            for p in points:
                coord = (p.X, p.Y, p.Z)
                coord_pair.append(coord)
            index_pair = []
            for coord in coord_pair:
                index = self.coord_ledger.get_index(coord)
                index_pair.append(index)
            index_pairs.append(index_pair)
        line_ledger = ledger.Ledger(index_pairs)
        return line_ledger

    def compose_is_string(self):
        """Returns a string in IS format
            <header>
                <name>
                <blank line>
                <coord entry 1>
                ...
                <line entry 1>
                ...
        """
        header_string = self.get_header_string()
        indented_name_string = self.tab + 'name'
        indented_coord_ledger_string = (
            self.get_indented_coord_ledger_string())
        indented_line_ledger_string = (
            self.get_indented_line_ledger_string())
        blank_line = ''
        component_strings = [
            header_string,
            indented_name_string,
            blank_line,
            indented_coord_ledger_string,
            indented_line_ledger_string]
        is_string = '\n'.join(component_strings)
        return is_string

    def get_header_string(self):
        """Returns 'shape <name>'
            string
        """
        header_string = 'shape <name>'
        return header_string

    def get_indented_coord_ledger_string(self):
        """Returns a string of the coord ledger entries, sorted by the index:
            tab 'coords' coord_index x y z
        """
        indented_entry_strings = []
        for coord in self.coord_ledger.elements:
            heading = 'coords'
            indented_heading = self.tab + heading
            coord_index = self.coord_ledger.get_index(coord)
            coord_index_str = str(coord_index)
            x, y, z = coord
            x_str, y_str, z_str = str(x), str(y), str(z)
            entry_elements = [
                indented_heading, coord_index_str, x_str, y_str, z_str]
            indented_entry_string = ' '.join(entry_elements)
            indented_entry_strings.append(indented_entry_string)
        indented_coord_ledger_string = '\n'.join(indented_entry_strings)
        return indented_coord_ledger_string

    def get_indented_line_ledger_string(self):
        """Returns a string of the line ledger entries, sorted by the index:
            tab 'line' line_index coord_index_1 coord_index_2
        """
        indented_entry_strings = []
        for line_coord_index_pair in self.line_ledger.elements:
            heading = 'line'
            indented_heading = self.tab + heading
            line_index = self.line_ledger.get_index(
                line_coord_index_pair)
            line_index_str = str(line_index)
            coord_index_1, coord_index_2 = line_coord_index_pair
            coord_index_str_1, coord_index_str_2 = (
                str(coord_index_1), str(coord_index_2))
            entry_elements = [
                indented_heading, line_index_str, 
                coord_index_str_1, coord_index_str_2]
            indented_entry_string = ' '.join(entry_elements)
            indented_entry_strings.append(indented_entry_string)
        indented_line_ledger_string = '\n'.join(indented_entry_strings)
        return indented_line_ledger_string

class FileWriter(object):
    def __init__(self):
        pass

    def write(self, is_string):
        print(is_string)

if __name__ == '__main__':
    exporter = ISFileExporter()
    exporter.export_shape()
    # import doctest
    # doctest.testfile('tests/is_file_exporter_test.txt')

