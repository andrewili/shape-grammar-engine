#   sg_column.py

import sg_line

class SGColumn(object):
    ### construct
    def __init__(self, lines):
        """Receives a list of lines, possibly non-collinear, possibly
        unordered, possibly non-maximal:
            [SGLine, ...], len >= 1
        """
        try:
            if (len(lines) == 0 or
                self.not_collinear(lines)
            ):
                raise ValueError()
            else:
                self.lines = self.maximal(sorted(lines))
        except ValueError:
            print '%s %s' % (
                "You're trying to make a column",
                "with non-collinear lines or no lines")

    def not_collinear(self, lines):
        carrier = lines[0].carrier
        for line in lines:
            if line.carrier != carrier:
                return True
        return False

        ### maximize
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

    def get_first_maximal_line_from(self, non_maximal_lines):   # 2.1.1.1.1
        """Receives an ordered list of possibly non-maximal collinear lines:
            [SGLine, ...], len() >= 1
        Returns the first maximal line:
            SGLine
        """
        if len(non_maximal_lines) == 1:
            new_line = self.get_singleton_line_from(non_maximal_lines)
                                                                # 2.1.1.1.1.1
        else:
            new_line = self.get_first_maximal_line_from_non_singleton(
                non_maximal_lines)
                                                                # 2.1.1.1.1.2
        return new_line

    def get_singleton_line_from(self, singleton_line_set):
        """Accepts a list containing a singleton line:
            [SGLine], len() == 1
        Returns the line:
            SGLine
        """
        new_line = singleton_line_set.pop(0)
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
        line_strings = []
        for line in self.lines:
            line_strings.append(line.__str__())
        column_string = ', '.join(line_strings)
        return '[%s]' % column_string

if __name__ == '__main__':
    import doctest
    doctest.testfile('tests/sg_column_test.txt')
