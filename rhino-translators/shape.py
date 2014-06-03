#	shape.py

class Shape(object):
    def __init__(self, name, line_specs, lpoint_specs):
        """Receives a name; list of line specs; and a list of labeled point
        specs:
            str
            [((num, num, num), (num, num, num)), ...]
            [((num, num, num), str), ...]
        """
        self.name = name
        (   self.ordered_coord_list,
            self.ordered_codex_codex_list,
            self.ordered_codex_label_list
        ) = self.make_ordered_index_lists(line_specs, lpoint_specs)

    ###
    def make_ordered_index_lists(self, line_specs, lpoint_specs):
        """Receives a list of line specs and a list of labeled point specs:
            [((num, num, num), (num, num, num)), ...]
            [((num, num, num), str), ...]
        Returns a triple of ordered indexed element lists
            (   [(num, num, num), ...],
                [(int, int), ...],
                [(int, label), ...])
        """
        ordered_coord_list = self.make_ordered_coord_list(
            line_specs, lpoint_specs)
        ordered_codex_codex_list = self.make_ordered_codex_codex_list(
            line_specs, ordered_coord_list)
        ordered_codex_label_list = self.make_ordered_codex_label_list(
            lpoint_specs, ordered_coord_list)
        return (
            ordered_coord_list,
            ordered_codex_codex_list,
            ordered_codex_label_list)

    def make_ordered_coord_list(self, line_specs, lpoint_specs):
        """Receive a list of line specs and a list of labeled point specs:
            [((num, num, num), (num, num, num)), ...]
            [((num, num, num), str), ...]
        Returns an ordered list of unique coords:
            [(num, num, num), ...]
        """
        coords = []
        unique_coords = []
        for line_spec in line_specs:
            for coord in line_spec:
                coords.append(coord)
        for lpoint_spec in lpoint_specs:
            coord = lpoint_spec[0]
            coords.append(coord)
        for coord in coords:
            if not coord in unique_coords:
                unique_coords.append(coord)
        return sorted(unique_coords)

    def make_ordered_codex_codex_list(self, line_specs, ordered_coord_list):
        """Receives a list of line specs and an ordered list of coords:
            [((num, num, num), (num, num, num)), ...]
            [(num, num, num), ...]
        Returns an ordered list of codex-codex pairs:
            [(int, int), ...]
        """
        codex_codex_list = []
        for line_spec in line_specs:
            codex_codex = self.make_codex_codex(line_spec, ordered_coord_list)
            codex_codex_list.append(codex_codex)
        return sorted(codex_codex_list)

    def make_codex_codex(self, line_spec, ordered_coord_list):
        """Receives a line spec and an ordered coord list:
            ((num, num, num), (num, num, num))
            [(num, num, num), ...]
        Returns a codex-codex pair:
            (int, int)
        """
        try:
            if not (
                line_spec[0] in ordered_coord_list and
                line_spec[1] in ordered_coord_list
            ):
                raise ValueError
        except ValueError:
            message = 'At least one of the coords is not in the list'
            print(message)
        else:
            codex_list = []
            for coord in line_spec:
                codex = ordered_coord_list.index(coord)
                codex_list.append(codex)
            codex_codex = (codex_list[0], codex_list[1])
            return codex_codex

    def make_ordered_codex_label_list(self, lpoint_specs, ordered_coord_list):
        """Receives a list of labeled point specs and an ordered list of 
        coords:
            [((num, num, num), str), ...]
            [(num, num, num), ...]
        Returns an ordered list of codex-label pairs:
            [(int, str), ...]
        """
        codex_label_list = []
        for lpoint_spec in lpoint_specs:
            codex_label = self.make_codex_label(
                lpoint_spec, ordered_coord_list)
            codex_label_list.append(codex_label)
        return sorted(codex_label_list)

    def make_codex_label(self, lpoint_spec, ordered_coord_list):
        """Receives a labeled point spec and an ordered list of coords:
            ((num, num, num), str)
            [(num, num, num), ...]
        Returns a codex-label pair:
            (int, str)
        """
        coord, label = lpoint_spec
        try:
            if not coord in ordered_coord_list:
                raise ValueError
        except ValueError:
            message = 'The coord is not in the coord list'
            print(message)
        else:
            codex = ordered_coord_list.index(coord)
            codex_label = (codex, label)
            return codex_label

    ###
    def __str__(self):
        """Returns a string in the is format:
            str
        """
        string = '<shape string>'
        return string

if __name__ == '__main__':
    import doctest
    doctest.testfile('tests/shape_test.txt')
