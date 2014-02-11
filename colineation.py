#   colineation.py

import copy
import line

class Colineation(object):
    """Consists of an ordered list of colinear lines. Immutable.
    """
    ### construct
    def __init__(self, lines):
        """Receives an unsorted list of colinear lines:
            [Line, ...], n >= 0
        """
        try:
            if (len(lines) >= 1 and
                not self.colinear(lines)
            ):
                raise ValueError()
            else:
                self.lines = lines
        except ValueError:
            print "You're trying to make a colineation with non-colinear lines"

    def colinear(self, lines):
        carrier = lines[0].carrier
        for line_i in lines:
            if line_i.carrier != carrier:
                return False
        return True

    @classmethod
    def new_empty(cls):
        new_colineation = Colineation([])
        return new_colineation

    @classmethod
    def from_short_specs(cls, short_specs):
        """Receives a list of short line specs:
            [(x, y), ...]
        """
        mew_lines = []
        for spec in short_specs:
            x, y = spec
            new_line = line.Line.from_short_spec(x, y)
            mew_lines.append(new_line)
        new_colineation = Colineation(mew_lines)
        return new_colineation

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
        if self.lines == []:
            colineation_listing = '%s<empty colineation>' % indent_string
        else:
            line_listings = []
            for line_i in sorted(self.lines):
                line_listings.append(indent_string + line_i.listing())
            colineation_listing = '\n'.join(line_listings)
        return colineation_listing

    def listing_unordered(self, indent_level=0):
        """Receives indent_level:
            int >= 0
        Returns an unordered, formatted, multi-line string in the form:
            (bearing, intercept):
                (x1, y1, x2, y2)
                ...
        """
        indent_increment = 4
        if indent_level < 0:
            indent_level = 0
        indent_string = ' ' * indent_level * indent_increment
        if self.lines == []:
            colineation_listing = '%s<empty colineation>' % indent_string
        else:
            line_listings = []
            for line_i in self.lines:
                line_listings.append(indent_string + line_i.listing())
            colineation_listing = '\n'.join(line_listings)
        return colineation_listing


    def lines_str(self, lines):                                                 #   not called
        """Receives a list of lines:
            [Line, ...]
        Returns a string: 
            [(x1, y1, x2, y2), ...]
        """
        line_strings = []
        for line_i in lines:
            line_string = line_i.__str__()
            line_strings.append(line_string)
        lines_string = ', '.join(line_strings)
        return '[%s]' % lines_string

    ### get
    def specs(self):
        """Returns an ordered list of line specs:
            [(x1, y1, x2, y2), ...]
        """
        specs = []
        for line_i in self.lines:
            specs.append(line_i.spec)
        return sorted(specs)

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

    def is_a_subcolineation_of(self, other):
        """Receives a non-empty colinear colineation:
            Colineation
        """
        for line_i in self.lines:
            if not line_i.is_a_subline_in_colineation(other):
                return False
        return True

    ### add
    def __add__(self, other):
        """Receives a colineation of the same carrier:
            Colineation
        Returns the sum (in maximal lines):
            Colineation
        """
        new_lines = Colineation.get_maximal_lines_from(self.lines, other.lines)
        new_colineation = Colineation(new_lines)
        return new_colineation

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
            new_line = Colineation.get_first_maximal_line_from_non_singleton(
                lines)
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

    ### subtract
    def __sub__(self, other):
        """Receives 2 (colinear) colineations:
            Colineation, n(lines) >= 0
        Returns a colineation, possibly empty, of the lines in self and not in 
        other:
            Colineation, n(lines) >= 0
        """
        trace_on = False
        if trace_on:
            method_name = 'Colineation.__sub__()'
            print '||| %s' % method_name
            print 'self\n%s' % self.listing()
            print 'other\n%s' % other.listing()
        col_col_diffs = []
        for line_i in self.lines:
            if trace_on:
                print '||| %s' % method_name
                print 'line_i:\n%s' % line_i
            if other.is_empty():
                col_col_diffs.append(line_i)
            else:
                other_disposable = copy.deepcopy(other)
                line_col_diffs = self.subtract_line_colineation(
                    line_i, other_disposable)
                col_col_diffs.extend(line_col_diffs)
                if trace_on:
                    print '||| %s' % method_name
                    print 'line_col_diffs:\n%s' % self.lines_str(line_col_diffs)
                    print 'col_col_diffs:\n%s' % self.lines_str(col_col_diffs)
        new_colineation = Colineation(col_col_diffs)
        return new_colineation

    def subtract_line_colineation(self, line_minuend, colineation_subtrahend):
        """Receives a line minuend and a (non-empty) colineation of colinear 
        working line subtrahends:
            line_minuend: Line
            colineation_subtrahend: Colineation, len(lines) >= 1
        Returns an ordered list of the line differences obtained by subtracting
        the line subtrahends from the (single) line minuend:
            [Line, ...], n >= 0
        Removes from the working colineation 1) the line subtrahends that lie to 
        the left of the line minuend's tail and 2) those that have been 
        subtracted and leave the line minuend's head unchanged. (The remaining 
        line subtrahends will be subtracted from subsequent line minuends, if 
        any.)
        """
        # Discard the disjoint line subtrahends (if any) on the left of the line
        # minuend
        # Subtract and discard those line subtrahends that overlap the left or
        # the middle of the line minuend
        # What about line subtrahends that overlap the whole line minuend?
        # Subtract and retain the line subtrahend that overlaps the head of the
        # line minuend
        trace_on = False
        line_diffs = []
        working_min = line_minuend
        working_col = colineation_subtrahend
        last_line_line_diff_list = []
        if trace_on:
            method_name = 'Colineation.subtract_line_colineation'
            print '||| %s' % method_name
            print 'working_min:\n%s' % working_min
            # print 'working_col:\n%s' % working_col.listing()
            print 'working_col:\n%s' % working_col.listing_unordered()
        while not working_col.is_empty():
            line_line_diffs = []
            line_sub = working_col.lines[0]
            # if trace_on:
            #     print '||| %s' % method_name
            #     for i in range(len(working_col.lines)):
            #         print 'working_col.lines[%i]: %s' % (
            #             i, working_col.lines[i].listing())
            if line_sub.is_disjoint_left_of(working_min):
                # difference = empty line
                # discard subtrahend and try with next, if any
                last_line_line_diff_list = [working_min]
                working_col.lines.pop(0)
            elif line_sub.overlaps_tail_of(working_min):
                # subtract; discard subtrahend and try with next, if any
                line_line_diffs = working_min.subtract_line_tail(
                    line_sub)
                working_min = line_line_diffs[0]
                last_line_line_diff_list = [line_line_diffs[0]]
                working_col.lines.pop(0)
            elif line_sub.overlaps_all_of(working_min):
                # difference = empty line
                # retain subtrahend and try with next minuend
                line_line_diffs = []
                last_line_line_diff_list = []
                break
            elif line_sub.overlaps_middle_of(working_min):
                # subtract; discard subtrahend and try with next, if any
                line_line_diffs = working_min.subtract_line_middle(
                    line_sub)
                line_diffs.append(line_line_diffs[0])
                working_min = line_line_diffs[1]
                last_line_line_diff_list = [line_line_diffs[1]]
                working_col.lines.pop(0)
            elif line_sub.overlaps_head_of(working_min):
                # subtract; retain subtrahend and try with next minuend
                line_line_diffs = working_min.subtract_line_head(
                    line_sub)
                line_diffs.append(line_line_diffs[0])
                last_line_line_diff_list = []
                if trace_on:
                    print '||| %s' % method_name
                    line_line_diffs_listing = (
                        self.get_colineation_listing(
                            line_line_diffs))
                    print 'line_line_diffs:\n%s' % line_line_diffs_listing
                    line_diffs_listing = (
                        self.get_colineation_listing(
                            line_diffs))
                    print 'line_diffs:\n%s' % line_diffs_listing
                    print 'last_line_line_diff: %s' % last_line_line_diff_list
                break
            elif line_sub.is_disjoint_right_of(working_min):
                # difference = empty line
                # retain subtrahend and try with next minuend
                last_line_line_diff_list = [working_min]
                break
            else:
                print "Shape.subtract_line_colineation"
                print "    Oops. This subtrahend is supposed to be impossible"
        line_diffs.extend(last_line_line_diff_list)
        return line_diffs

    ###
if __name__ == '__main__':
    import doctest
    doctest.testfile('tests/colineation_test.txt')
