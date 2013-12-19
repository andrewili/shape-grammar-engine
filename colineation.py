#   colineation.py

import line

class Colineation(object):
    """Consists of a non-empty (and unordered) list of colinear lines. 
    Immutable.
    """
        ### construct
    def __init__(self, lines):
        """Receives a non-empty unsorted list of colinear lines:
            [Line, ...], n >= 1
        """
        try:
            if (len(lines) == 0 or
                not self.colinear(lines)
            ):
                raise ValueError()
            else:
                self.lines = lines
        except ValueError:
            print '%s %s' % (
                "You're trying to make a colineation",
                "with non-colinear lines or no lines")

    def colinear(self, lines):
        carrier = lines[0].carrier
        for line_i in lines:
            if line_i.carrier != carrier:
                return False
        return True

        ### maximize
    @classmethod
    def get_maximal_lines_from(cls, maximal_lines_1, maximal_lines_2):
        """Receives 2 ordered lists of maximal colinear lines:
            [Line, ...], n >= 1
        Returns an ordered list of maximal colinear lines:
            [Line, ...], n >= 1, should not contain duplicates
        """
        non_maximal_unsorted_lines = []
        non_maximal_unsorted_lines.extend(maximal_lines_1)
        non_maximal_unsorted_lines.extend(maximal_lines_2)
        sorted_non_maximal_lines = sorted(non_maximal_unsorted_lines)
        new_maximal_lines = Colineation.maximal(sorted_non_maximal_lines)
        return new_maximal_lines

    @classmethod
    def maximal(cls, non_maximal_lines):
        """Receives an ordered list of (possibly non-maximal) colinear lines:
            [Line, ...], n >= 1
        Returns an ordered list of maximal colinear lines:
            [Line, ...], n >= 1
        """
        maximal_lines = []
        while len(non_maximal_lines) >= 1:
            new_maximal_line = Colineation.get_first_maximal_line_from(
                non_maximal_lines)
            maximal_lines.append(new_maximal_line)
        return maximal_lines

    @classmethod
    def get_first_maximal_line_from(cls, lines):
        """Receives an ordered list of (possibly non-maximal) colinear lines:
            [Line, ...], n >= 1
        Returns the first maximal line in the list:
            Line
        """
        if len(lines) == 1:
            new_line = Colineation.get_singleton_line_from(lines)
        else:
            new_line = Colineation.get_first_maximal_line_from_non_singleton(lines)
        return new_line

    @classmethod
    def get_singleton_line_from(cls, singleton_lines):
        """Receives a list containing a singleton line:
            [Line], n = 1
        Returns the singleton line:
            Line
        """
        new_line = singleton_lines.pop(0)
        return new_line

    @classmethod
    def get_first_maximal_line_from_non_singleton(cls, non_maximal_lines):
        """Receives an ordered list of (possibly non-maximal) colinear lines:
            [Line, ...], n >= 2
        Returns the first maximal line:
            Line
        """
        working_line = non_maximal_lines.pop(0)
        while len(non_maximal_lines) >= 1:
            other_line = non_maximal_lines[0]
            if Colineation.lines_can_be_merged(working_line, other_line):
                working_line = Colineation.merge_lines(working_line, other_line)
                non_maximal_lines.pop(0)
            else:
                break
        first_maximal_line = working_line
        return first_maximal_line

    @classmethod
    def lines_can_be_merged(cls, line_1, line_2):
        """Receives 2 colinear lines.
        Returns a boolean whether the lines can be merged.
        See Krishnamurti (1980), 465.
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

    @classmethod
    def merge_lines(cls, line_1, line_2):
        """Receives 2 mergeable lines, line_1.tail <= line_2.tail:
            [Line, Line]
        Returns the sum of the 2 lines:
            Line
        """
        new_tail = min(line_1.tail, line_2.tail)
        new_head = max(line_1.head, line_2.head)
        new_line = line.Line(new_tail, new_head)
        return new_line

        ### represent
    def __str__(self):
        """Returns the string of ordered line specs:
            [(x1, y1, x2, y2), ...]
        """
        line_strings = []
        for line_i in sorted(self.lines):
            line_strings.append(line_i.__str__())
        colineation_string = ', '.join(line_strings)
        return '[%s]' % colineation_string

    def listing(self, indent_level=0):
        """Receives indent_level:
            int >= 0
        Returns an ordered, formatted, multi-line string in the form:
            (bearing, intercept):
                (x1, y1, x2, y2)
                ...
        """
        indent_increment = 4
        if indent_level < 0:
            indent_level = 0
        indent_string = ' ' * indent_level * indent_increment
        line_listings = []
        for line_i in sorted(self.lines):
            line_listings.append(indent_string + line_i.listing())
        colineation_listing = '\n'.join(line_listings)
        return colineation_listing

        ### relations
    def __eq__(self, other):
        """Receives a colineation:
            Colineation
        Returns whether both colineations contain the same lines.
        """
        return sorted(self.lines) == sorted(other.lines)

    def __ne__(self, other):
        """Receives a colineation:
            Colineation
        Returns whether both colineations do not contain the same lines.
        """
        return sorted(self.lines) != sorted(other.lines)

    def is_empty(self):
        return len(self.lines) == 0
        # print 'Colineation.is_empty()'

    def is_a_subcolineation_of(self, other):
        """Receives a non-empty colinear colineation:
            Colineation
        """
        for line_i in self.lines:
            if not line_i.is_a_subline_in_colineation(other):
                return False
        return True

        ### subtract
    def __sub__(self, other):
        pass

        ###
if __name__ == '__main__':
    import doctest
    doctest.testfile('tests/colineation_test.txt')
