#   colineation.py

import line

class Colineation(object):
    """Consists of a non-empty (and unordered) list of colinear lines. 
    Immutable.
    """
    ### construct
    def __init__(self, lines):
        """Receives a non-empty unsorted list of colinear lines:                #   May need to allow n = 0
            [Line, ...], n >= 1                                                 #   For colineation difference = 0
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
    def __sub__(self, working_colineation_2):
        """Receives 2 (non-empty colinear) colineations:
            Colineation, n(lines) >= 1
        Returns an ordered list, possibly empty, of the lines in self and not 
        in working_colineation_2:
            [Line, ...], n >= 0                                                 #   May be empty. Must be list?
                                                                                #   Can be Colineation?
        """
        trace_on = False
        if trace_on:
            method_name = 'Shape.subtract_colineations'
            print '||| %s.self\n%s' % (
                method_name, self.listing())
            print '||| %s.working_colineation_2\n%s' % (
                method_name, working_colineation_2.listing())
        colineation_colineation_differences = []
        for line_i in self.lines:
            if trace_on:
                print '||| %s.line_i:\n%s' % (method_name, line_i)
            if working_colineation_2.is_empty():
                colineation_colineation_differences.append(line_i)
            else:
                line_colineation_differences = self.subtract_line_colineation(
                    line_i, working_colineation_2)
                colineation_colineation_differences.extend(
                    line_colineation_differences)
                if trace_on:
                    print '||| %s.line_colineation_differences:\n%s' % (
                        method_name, line_colineation_differences)              #   need a __str__ method
                    print '||| %s.colineation_colineation_differences:\n%s' % (
                        method_name, 
                        colineation_colineation_differences)                    #   need a __str__ method
        return colineation_colineation_differences

    def subtract_line_colineation(self, line_minuend, working_colineation):
        """Receives a line minuend and a (non-empty) list of colinear working 
        line subtrahends:
            line_minuend: Line
            working_colineation: Colineation, len(lines) >= 1
        Returns an ordered list of the line differences obtained by subtracting
        the line subtrahends from the (single) line minuend:    #   do we want an ordered list or a Colineation?
            [Line, ...], n >= 0
        Removes from the working colineation 1) the line subtrahends that lie to 
        the left of the line minuend's tail and 2) those that have been 
        subtracted and leave the line minuend's head unchanged. (The remaining 
        line subtrahends will be subtracted from subsequent line minuends, if 
        any.)
        """
        # Discard the disjoint line subtrahends (if any) on the left of the line
        # minuend
        # Subtract and discard those line subtrahends that overlaps the left or
        # the middle of the line minuend
        # What about line subtrahends that overlaps the whole line minuend?
        # Subtract and retain the line subtrahend that overlaps the head of the
        # line minuend
        trace_on = False
        line_differences = []
        working_minuend = line_minuend
        last_line_line_difference_list = []
        if trace_on:
            method_name = 'Shape.subtract_line_colineation'
            print '||| %s.working_minuend:\n%s' % (method_name, working_minuend)
            working_colineation_listing = self.get_colineation_listing(
                working_colineation)
            print '||| %s.working_colineation:\n%s' % (
                method_name, working_colineation_listing)
        while not working_colineation.is_empty():
            line_line_differences = []
            line_subtrahend = working_colineation.lines[0]
            if trace_on:
                print '||| %s.line_subtrahend:\n%s' % (
                    method_name, line_subtrahend)
                print '||| %s.working_colineation.lines[1]:\n%s' % (
                    method_name, working_colineation.lines[1])
            if line_subtrahend.is_disjoint_left_of(working_minuend):
                # difference = empty line
                # discard subtrahend and try with next, if any
                last_line_line_difference_list = [working_minuend]
                working_colineation.lines.pop(0)
            elif line_subtrahend.overlaps_tail_of(working_minuend):
                # subtract; discard subtrahend and try with next, if any
                line_line_differences = working_minuend.subtract_line_tail(
                    line_subtrahend)
                working_minuend = line_line_differences[0]
                last_line_line_difference_list = [line_line_differences[0]]
                working_colineation.lines.pop(0)
            elif line_subtrahend.overlaps_all_of(working_minuend):
                # difference = empty line
                # retain subtrahend and try with next minuend
                line_line_differences = []
                last_line_line_difference_list = []
                break
            elif line_subtrahend.overlaps_middle_of(working_minuend):
                # subtract; discard subtrahend and try with next, if any
                line_line_differences = working_minuend.subtract_line_middle(
                    line_subtrahend)
                line_differences.append(line_line_differences[0])
                working_minuend = line_line_differences[1]
                last_line_line_difference_list = [line_line_differences[1]]
                working_colineation.lines.pop(0)
            elif line_subtrahend.overlaps_head_of(working_minuend):
                # subtract; retain subtrahend and try with next minuend
                line_line_differences = working_minuend.subtract_line_head(
                    line_subtrahend)
                line_differences.append(line_line_differences[0])
                last_line_line_difference_list = []
                if trace_on:
                    line_line_differences_listing = (
                        self.get_colineation_listing(
                            line_line_differences))
                    print '||| %s.line_line_differences:\n%s' % (
                        method_name, line_line_differences_listing)
                    line_differences_listing = (
                        self.get_colineation_listing(
                            line_differences))
                    print '||| %s.line_differences:\n%s' % (
                        method_name, line_differences_listing)
                    print '||| %s.last_line_line_difference: %s' % (
                        method_name, last_line_line_difference_list)
                break
            elif line_subtrahend.is_disjoint_right_of(working_minuend):
                # difference = empty line
                # retain subtrahend and try with next minuend
                last_line_line_difference_list = [working_minuend]
                break
            else:
                print "Shape.subtract_line_colineation"
                print "    Oops. This subtrahend is supposed to be impossible"
        line_differences.extend(last_line_line_difference_list)
        return line_differences
        ###

if __name__ == '__main__':
    import doctest
    doctest.testfile('tests/colineation_test.txt')
