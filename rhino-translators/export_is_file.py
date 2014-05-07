import rhinoscriptsyntax as rs

def export_is_file():
    """Receives a list of line Guids
        [Guid, ...]
    Exports a text file in IS format
    """
    lines = rs.GetObjects('Select lines', rs.filter.curve)
    rhino_shape = RhinoShape(lines)
    is_string = rhino_shape.compose_is_string()
    file_writer = FileWriter()
    file_writer.write(is_string)

class RhinoShape(object):
    def __init__(self, lines):
        """Receives a list of line Guids
            [Guid, ...]
        """
        self.lines = lines
        self.shape_name = '<shape name>'
        self.coord_ledger = {}  # {(x1, y1, z1): i1, ...}
        self.line_ledger = {}   # {(i1, j1): k1, ...}
        self.tab = '    '
        self.complete_ledgers()

    def complete_ledgers(self):
        for line in self.lines:
            self.enter_in_ledgers(line)

    def enter_in_ledgers(self, line):
        """Receives a line Guid
            Guid
        Records the line in the coord and line ledgers
        """
        # check for line Guid
        point_object_1, point_object_2 = rs.CurvePoints(line)
        coord1, coord2 = self.get_coords(point_object_1, point_object_2)
        coord_index_1, coord_index_2 = self.get_coords_by_index(coord1, coord2)
        self.enter_in_line_ledger(coord_index_1, coord_index_2)

    def get_coords(self, point_object_1, point_object_2):
        """Receives 2 point objects
            Point3d, Point3d
        Returns 2 coords
            (num, num, num), (num, num, num)
        """
        x1, y1, z1 = point_object_1.X, point_object_1.Y, point_object_1.Z
        x2, y2, z2 = point_object_2.X, point_object_2.Y, point_object_2.Z
        coord1 = (x1, y1, z1)
        coord2 = (x2, y2, z2)
        return (coord1, coord2)

    def get_coords_by_index(self, coord1, coord2):
        """Receives 2 coords:
            (num, num, num), (num, num, num)
        Returns 2 coords by index: 
            (int, int) 
        """
        coord_index_1 = self.get_coord_by_index(coord1)
        coord_index_2 = self.get_coord_by_index(coord2)
        return (coord_index_1, coord_index_2)

    def get_coord_by_index(self, coord):
        """Receives coord:
            (num, num, num)
        Creates a new entry if necessary. Returns coord by index:
            int
        """
        if self.coord_ledger == {}:
            previous_index = 0
        else:
            previous_index = max(self.coord_ledger.values())
        if not self.coord_ledger.has_key(coord):
            current_index = previous_index + 1
            self.coord_ledger[coord] = current_index
        return current_index

    def enter_in_line_ledger(self, coord_index_1, coord_index_2):
        """Receives 2 coords by index
            int, int
        If they have not already been entered, enters them in the line ledger
        """
        if self.line_ledger == {}:
            previous_index = 0
        else:
            previous_index = max(self.line_ledger.values())
        if not self.line_ledger.has_key((coord_index_1, coord_index_2)):
            current_index = previous_index + 1
            self.line_ledger[(coord_index_1, coord_index_2)] = current_index

    def in_coord_ledger(self, point):
        """Receives a point
            [num, num, num]
        Returns whether the point is in the coord ledger
        """
        value = point in self.coord_ledger.values()
        return value

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
        """Returns a string of the ledger entries, sorted by the index:
            tab 'coords' coord_index x y z
        """
        indented_entry_strings = []
        for coord in sorted(self.coord_ledger.keys()):
            indented_heading = self.tab + 'coords'
            coord_index = self.coord_ledger[coord]
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
        indented_entry_strings = []
        for line_coord_index_pair in sorted(self.line_ledger.keys()):
            indented_heading = self.tab + 'line'
            line_index = self.line_ledger[line_coord_index_pair]
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
    export_is_file()
