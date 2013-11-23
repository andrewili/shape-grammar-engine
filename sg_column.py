#   sg_column.py

import sg_line

class SGColumn(object):
    """Consists of a non-empty list of collinear lines. Immutable
    """
        ### construct
    def __init__(self, lines):
        """Receives a non-empty unsorted list of collinear lines:
            [SGLine, ...], len >= 1
        """
        try:
            if (len(lines) == 0 or
                not self.collinear(lines)
            ):
                raise ValueError()
            else:
                self.lines = lines
        except ValueError:
            print '%s %s' % (
                "You're trying to make a column",
                "with non-collinear lines or no lines")

    def collinear(self, lines):
        carrier = lines[0].carrier
        for line in lines:
            if line.carrier != carrier:
                return False
        return True

        ### maximize
    def get_maximal_lines_from(self, maximal_lines_1, maximal_lines_2):
        """Receives 2 ordered lists of maximal collinear lines:
            [SGLine, ...], len() >= 1
        Returns an ordered list of maximal colinear lines:
            [SGLine, ...], len() >= 1, should not contain duplicates
        """
        new_non_maximal_unsorted_lines = []
        new_non_maximal_unsorted_lines.extend(maximal_lines_1)
        new_non_maximal_unsorted_lines.extend(maximal_lines_2)
        new_sorted_lines = sorted(new_non_maximal_unsorted_lines)
        new_maximal_lines = self.maximal(new_sorted_lines)      # 2.1.1.1
        return new_maximal_lines

    def maximal(self, non_maximal_lines):
        """Receives an ordered list of collinear, possibly non-maximal, lines:
            [SGLine, ...], len() >= 1
        Returns an ordered list of maximal collinear lines:
            [SGLine, ...], len() >= 1
        """
        maximal_lines = []
        while len(non_maximal_lines) >= 1:
            new_maximal_line = self.get_first_maximal_line_from(
                non_maximal_lines)
            maximal_lines.append(new_maximal_line)
        return maximal_lines

    def get_first_maximal_line_from(self, lines):   # 2.1.1.1.1
        """Receives an ordered list of possibly non-maximal collinear lines:
            SGColumn, len() >= 1
        Returns the first maximal line:
            SGLine
        """
        """Receives an ordered list of possibly non-maximal collinear lines:
            [SGLine, ...], len() >= 1
        Returns the first maximal line:
            SGLine
        """
        if len(lines) == 1:
            new_line = self.get_singleton_line_from(lines)
                                                                # 2.1.1.1.1.1
        else:
            new_line = self.get_first_maximal_line_from_non_singleton(
                lines)
                                                                # 2.1.1.1.1.2
        return new_line

    def get_singleton_line_from(self, singleton_lines):
        """Receives a list containing a singleton line:
            [SGLine], len() == 1
        Returns the singleton line:
            SGLine
        """
        new_line = singleton_lines.pop(0)
        return new_line

    def get_first_maximal_line_from_non_singleton(self, non_maximal_lines):
        """Receives an ordered list of possibly non-maximal collinear lines:
            [SGLine, ...], len() >= 2
        Returns the first maximal line:
            SGLine
        """
        working_line = non_maximal_lines.pop(0)
        while len(non_maximal_lines) >= 1:
            other_line = non_maximal_lines[0]
            if self.lines_can_be_merged(working_line, other_line):
                                                                # 2.1.1.1.1.2.1
                working_line = self.merge_lines(working_line, other_line)
                                                                # 2.1.1.1.1.2.2
                non_maximal_lines.pop(0)
            else:
                break
        first_maximal_line = working_line
        return first_maximal_line

    def lines_can_be_merged(self, line_1, line_2):              # 2.1.1.1.1.2.1
        """Receives 2 collinear lines.
        Returns a boolean whether the lines can be merged.
        See Krishnamurti (1980), 465
        """
        if line_1.tail == line_2.head:
            return True
        elif line_2.tail == line_1.head:
            return True
        elif (
            line_1.tail < line_2.head and
            line_2.tail < line_1.head
        ):
            return True
        else:
            return False

    def merge_lines(self, line_1, line_2):                      # 2.1.1.1.1.2.2
        """Receives 2 lines that can be merged.
        Returns the sum of the 2 lines.
        """
        new_tail = min(line_1.tail, line_2.tail)
        new_head = max(line_1.head, line_2.head)
        new_line = sg_line.SGLine(new_tail, new_head)
        return new_line

        ### represent
    def __str__(self):
        """Returns the string of ordered lines:
            (<x1>, <y1>, <x2>, <y2>), ...
        """
        line_strings = []
        for line in sorted(self.lines):
            line_strings.append(line.__str__())
        column_string = ', '.join(line_strings)
        return column_string

    def listing(self, indent_level=0):
        """Receives indent_level, i >= 0
        Returns an ordered, formatted, multi-line string in the form:
            (<bearing>, <intercept>):
                (<x1>, <y1>, <x2>, <y2>)
                ...
            ...
        """
        indent_increment = 4
        if indent_level < 0:
            indent_level = 0
        indent_string = ' ' * indent_level * indent_increment
        line_listings = []
        for line in sorted(self.lines):
            line_listings.append(indent_string + line.listing())
        column_listing = '\n'.join(line_listings)
        return column_listing

        ### relations
    def __eq__(self, other):
        if len(self.lines) != len(other.lines):
            return False
        for i in range(len(self.lines)):
            if self.lines[i] != other.lines[i]:
                return False
        return True

    def __ne__(self, other):
        if len(self.lines) != len(other.lines):
            return True
        for i in range(len(self.lines)):
            if self.lines[i] == other.lines[i]:
                return False
        return True

    def is_a_subcolumn_of(self, other):
        """Receives a non-empty colinear column:
            SGColumn
        """
        #   Refactor. Each iteration tests all lines in other column
        for line in self.lines:
            if not line.is_a_subline_in_column(other):
                return False
        return True

        ### add
    def get_first_maximal_line_from_non_singleton_unreduced_column(self):
        """Sorts and maximizes the column, and returns the first maximal line:
            SGLine
        """
        pass

        ### subtract

        ###
if __name__ == '__main__':
    import doctest
    doctest.testfile('tests/sg_column_test.txt')
