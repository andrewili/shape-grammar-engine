#	shape.py

class Shape(object):
    def __init__(self, name, line_specs, lpoint_specs):
        """Receives a name; list of line specs; and a list of labeled point
        specs:
            str
            [((num, num, num), (num, num, num)), ...]
            [((num, num, num), str), ...]
        """
        try:
            if (not type(name) == str or
                not type(line_specs) == list or
                not type(lpoint_specs) == list
            ):
                raise TypeError
            if name == '':
                raise ValueError
        except TypeError:
            message = 'The arguments must be a string, a list, and a list'
            print(message)
        except ValueError:
            message = 'The name must not be empty'
            print(message)
        else:
            self.name = name
            (   self.ordered_coord_list,
                self.ordered_codex_codex_list,
                self.ordered_codex_label_list
            ) = self._make_ordered_index_lists(line_specs, lpoint_specs)
            self.tab = '    '

    def _make_ordered_index_lists(self, line_specs, lpoint_specs):
        """Receives a list of line specs and a list of labeled point specs:
            [((num, num, num), (num, num, num)), ...]
            [((num, num, num), str), ...]
        Returns a triple of ordered indexed element lists
            (   [(num, num, num), ...],
                [(int, int), ...],
                [(int, label), ...])
        """
        ordered_coord_list = self._make_ordered_coord_list(
            line_specs, lpoint_specs)
        ordered_codex_codex_list = self._make_ordered_codex_codex_list(
            line_specs, ordered_coord_list)
        ordered_codex_label_list = self._make_ordered_codex_label_list(
            lpoint_specs, ordered_coord_list)
        return (
            ordered_coord_list,
            ordered_codex_codex_list,
            ordered_codex_label_list)

    def _make_ordered_coord_list(self, line_specs, lpoint_specs):
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

    def _make_ordered_codex_codex_list(self, line_specs, ordered_coord_list):
        """Receives a list of line specs and an ordered list of coords:
            [((num, num, num), (num, num, num)), ...]
            [(num, num, num), ...]
        Returns an ordered list of codex-codex pairs:
            [(int, int), ...]
        """
        codex_codex_list = []
        for line_spec in line_specs:
            codex_codex = self._make_codex_codex(line_spec, ordered_coord_list)
            codex_codex_list.append(codex_codex)
        return sorted(codex_codex_list)

    def _make_codex_codex(self, line_spec, ordered_coord_list):
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

    def _make_ordered_codex_label_list(self, lpoint_specs, ordered_coord_list):
        """Receives a list of labeled point specs and an ordered list of 
        coords:
            [((num, num, num), str), ...]
            [(num, num, num), ...]
        Returns an ordered list of codex-label pairs:
            [(int, str), ...]
        """
        codex_label_list = []
        for lpoint_spec in lpoint_specs:
            codex_label = self._make_codex_label(
                lpoint_spec, ordered_coord_list)
            codex_label_list.append(codex_label)
        return sorted(codex_label_list)

    def _make_codex_label(self, lpoint_spec, ordered_coord_list):
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
    def make_initial_shape_string(self):
        """Returns a string of an initial shape in is format:
            str
        """
        initial_shape_header_and_name = (
            self._make_initial_shape_header_and_name())
        shape_string_remainder = self._make_shape_string_remainder()
        if len(shape_string_remainder) == 0:
            initial_shape_string = initial_shape_header_and_name
        else:
            initial_shape_string = '%s\n%s' % (
                initial_shape_header_and_name, 
                shape_string_remainder)
        initial_shape_string
        return initial_shape_string
        
    def _make_initial_shape_header_and_name(self):
        """Returns a string in the form:
            shape <shape name>
                name
        """
        initial_shape_header = 'shape %s' % self.name
        indented_shape_name_string = '%sname' % self.tab
        initial_shape_header_and_name = '\n'.join([
            initial_shape_header,
            indented_shape_name_string])
        return initial_shape_header_and_name

    ###
    def make_rule_shape_string(self, side, rule_name):
        """Receives the side and the name of the rule (as part of the rule 
        string):
            str
            str
        Returns the shape part of the rule string in rul format:
            str
        """
        rule_shape_header_and_name = (
            self._make_rule_shape_header_and_name(side, rule_name))
        shape_string_remainder = self._make_shape_string_remainder()
        rule_shape_substrings = [
            rule_shape_header_and_name,
            shape_string_remainder]
        rule_shape_string = '\n'.join(rule_shape_substrings)
        return rule_shape_string

    def _make_rule_shape_header_and_name(self, side, rule_name):
        """Receives the side and the name of the rule:
            str
            str
        Returns a string of the form:
            shape <rule name>_<side>
                name <shape name>
        """
        if side == 'left':
            side_string = 'L'
        elif side == 'right':
            side_string = 'R'
        else:
            pass
        rule_shape_header = 'shape %s_%s' % (rule_name, side_string)
        indented_rule_shape_name_string = '%sname %s' % (self.tab, self.name)
        rule_shape_header_and_name = '\n'.join([
            rule_shape_header,
            indented_rule_shape_name_string])
        return rule_shape_header_and_name

    ###
    def _make_shape_string_remainder(self):
        """Returns the shape string excluding the shape header and name lines.
            str
        """
        indented_coord_entries_string = (
            self._make_indented_coord_entries_string())
        blank_line = ''
        indented_line_entries_string = (
            self._make_indented_line_entries_string())
        indented_lpoint_entries_string = (
            self._make_indented_lpoint_entries_string())
        shape_remainder_substrings = []
        if len(indented_coord_entries_string) > 0:
            shape_remainder_substrings.append(indented_coord_entries_string)
            shape_remainder_substrings.append(blank_line)
        if len(indented_line_entries_string) > 0:
            shape_remainder_substrings.append(indented_line_entries_string)
        if len(indented_lpoint_entries_string) > 0:
            shape_remainder_substrings.append(indented_lpoint_entries_string)
        shape_string_remainder = '\n'.join(shape_remainder_substrings)
        return shape_string_remainder

    def _make_indented_coord_entries_string(self):
        """Returns a string of the form:
            <indented coord entry>\n...
        """
        indented_coord_entry_strings = (
            self._make_indented_coord_entry_strings())
        indented_coord_entries_string = (
            '\n'.join(indented_coord_entry_strings))
        return indented_coord_entries_string

    def _make_indented_coord_entry_strings(self):
        """Returns a list of indented coord entry strings:
            [<tab>coords <i_str> <x_str> <y_str> <z_str>, ...]
        """
        indented_coord_entry_strings = []
        for coord in self.ordered_coord_list:
            coord_entry_string = (
                self._make_coord_entry_string(coord))
            indented_coord_entry_string = (
                '%s%s' % (self.tab, coord_entry_string))
            indented_coord_entry_strings.append(indented_coord_entry_string)
        return indented_coord_entry_strings

    def _make_coord_entry_string(self, coord):
        """Receives a coord:
            (num, num, num)
        Returns a string of the form:
            coords <i_str> <x_str> <y_str> <z_str>
        """
        try:
            if not coord in self.ordered_coord_list:
                raise ValueError
        except ValueError:
            message = 'The coord is not in the list'
            print(message)
        else:
            i = self.ordered_coord_list.index(coord)
            x, y, z = coord
            coord_entry_string = 'coords %i %f %f %f' % (i, x, y, z)
            return coord_entry_string

    def _make_indented_line_entries_string(self):
        """Returns a string of the form:
            <indented line entry>\n...
        """
        indented_line_entry_strings = (
            self._make_indented_line_entry_strings())
        indented_line_entries_string = '\n'.join(indented_line_entry_strings)
        return indented_line_entries_string

    def _make_indented_line_entry_strings(self):
        indented_line_entry_strings = []
        for codex_codex in self.ordered_codex_codex_list:
            line_entry_string = self._make_line_entry_string(codex_codex)
            indented_line_entry_string = (
                '%s%s' % (self.tab, line_entry_string))
            indented_line_entry_strings.append(indented_line_entry_string)
        return indented_line_entry_strings

    def _make_line_entry_string(self, codex_codex):
        """Returns a string of the form:
            line <i> <x> <y> <z>
        """
        i = self.ordered_codex_codex_list.index(codex_codex)
        codex_1, codex_2 = codex_codex
        line_entry_string = 'line %i %i %i' % (i, codex_1, codex_2)
        return line_entry_string

    def _make_indented_lpoint_entries_string(self):
        """Returns a string of the form:
            <indented lpoint entry>\n...
        """
        indented_lpoint_entry_strings = (
            self._make_indented_lpoint_entry_strings())
        indented_lpoint_entries_string = (
            '\n'.join(indented_lpoint_entry_strings))
        return indented_lpoint_entries_string

    def _make_indented_lpoint_entry_strings(self):
        """Returns a list of lpoint entry strings:
            [str, ...]
        """
        indented_lpoint_entry_strings = []
        for codex_label in self.ordered_codex_label_list:
            lpoint_entry_string = self._make_lpoint_entry_string(codex_label)
            indented_lpoint_entry_string = (
                '%s%s' % (self.tab, lpoint_entry_string))
            indented_lpoint_entry_strings.append(indented_lpoint_entry_string)
        return indented_lpoint_entry_strings

    def _make_lpoint_entry_string(self, codex_label):
        """Receives a codex-label pair:
            (int, str)
        Returns a string of the form:
            point <codex> <label>
        """
        try:
            if not codex_label in self.ordered_codex_label_list:
                raise ValueError
        except ValueError:
            message = 'The codex-label pair is not in the list'
            print(message)
        else:
            codex, label = codex_label
            lpoint_entry_string = 'point %i %s' % (codex, label)
            return lpoint_entry_string

    ###
    def __str__(self):
        """Returns a string in the is format (i.e., a free-standing shape 
        string):
            str
        """
        is_string = self.make_initial_shape_string()
        return is_string

if __name__ == '__main__':
    import doctest
    doctest.testfile('tests/shape_test.txt')
