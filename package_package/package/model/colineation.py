import copy
import line

class Colineation(object):
    """Has an ordered list of maximal colinear lines. Immutable
    """
    ### construct
    def __init__(self, lines):
        """Receives:
            lines           [Line, ...]. An unordered list of colinear lines, 
                            possibly overlapping
        """
        method_name = '__init__'
        try:
            if not (
                type(lines) == list and 
                (   lines == [] or
                    self._are_lines(lines))
            ):
                raise TypeError
            elif not self._are_colinear(lines):
                raise ValueError
        except TypeError:
            message = (
                "The argument must be a list of colinear lines")
            self._print_error_message(method_name, message)
        except ValueError:
            message = "The lines must be colinear"
            self._print_error_message(method_name, message)
        else:
            self.lines = sorted(lines) # maximize
            self.lines = self.maximal()

    def _are_lines(self, lines):
        """Receives:
            lines           [Line, ...]. A list (guaranteed) of lines
        Returns:
            value           boolean. True if all the items in lines are lines.
                            False otherwise
        """
        value = True
        for l in lines:
            if not type(l) == line.Line:
                value = False
                break
        return value

    def _are_colinear(self, lines):
        """Receives:
            lines           [Line, ...]. A list, possibly empty, of lines. 
                            Guaranteed by the calling function
        Returns:
            value           boolean. True if the list is empty or if the 
                            lines are colinear. False otherwise
        """
        if lines == []:
            value = True
        else:
            value = True
            carrier = lines[0].carrier
            for line_i in lines:
                if line_i.carrier != carrier:
                    value = False
        return value

    @classmethod
    def new_empty(cls):
        new_colineation = Colineation([])
        return new_colineation

    @classmethod
    def from_specs_2(cls, specs):
        """Receives:
            specs           [(x1, x2), ...]. A list of pairs representing 
                            lines ((x1, x1, x1),(x2, x2, x2))
                x1, x2      num
        """
        method_name = 'from_specs_2'
        try:
            if not type(specs) == list:
                raise TypeError
        except TypeError:
            message = 'The argument must be a list of duples'
            cls._print_error_message(method_name, message)
        else:
            new_lines = []
            for spec in specs:
                x, y = spec
                new_line = line.Line.from_spec_2(x, y)
                new_lines.append(new_line)
            new_colineation = Colineation(new_lines)
            return new_colineation

    ### represent
    def __str__(self):
        """Returns: 
            string          '[<line_str>, ...]'. A list of line strings, 
                            where: 
                line_str    '((<x1>, <y1>, <z1>), (<x2>, <y2>, <z2>))'
        """
        line_strings = []
        for line_i in sorted(self.lines):
            line_strings.append(str(line_i))
        colineation_string = ', '.join(line_strings)
        return '[%s]' % colineation_string

    def __repr__(self):
        """Returns:
            string          str. In the form 
                            'colineation.Colineation(line_reprs)', where:
                lines_reprs [line_repr, ...]
        """
        line_reprs = []
        for l in self.lines:
            line_reprs.append(repr(l))
        lines_repr = ', '.join(line_reprs)
        lines_repr_str = '[%s]' % lines_repr
        string = 'colineation.Colineation(%s)' % lines_repr_str
        return string

    def listing(self, decimal_places=0, indent_level=0):
        """Receives:
            decimal_places  int >= 0
            indent_level    int >= 0
        Returns:
            colineation_listing
                            str. An ordered, formatted, multi-line string in 
                            the form:
                            (<unit_vector>, <intercept>):
                                ((x1, y1, z1), (x2, y2, z2))
                                ...
                            where:
                unit_vector Vector. [uv_x uv_y uv_z]
                intercept   Point. (int_x, int_y, int_z)
        """
        method_name = 'listing'
        try:
            if not (
                type(decimal_places) == int and
                type(indent_level) == int
            ):
                raise TypeError
            elif not (
                decimal_places >= 0 and
                indent_level >= 0
            ):
                raise ValueError
        except TypeError:
            message = 'The arguments must both be integers'
            self._print_error_message(method_name, message)
        except ValueError:
            message = 'The arguments must both be non-negative'
            self._print_error_message(method_name, message)
        else:
            indent_increment = 4                ##  4 spaces
            if indent_level < 0:
                indent_level = 0
            indent_string = ' ' * int(indent_level) * indent_increment
            if self.lines == []:
                colineation_listing = '%s<empty colineation>' % indent_string
            else:
                line_listings = []
                for line_i in self.lines:
                    line_listings.append(indent_string + line_i.listing(
                        decimal_places))
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

    def lines_str(self, lines):                 ##  used by trace
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
        """Receives:
            other           Colineation
        Returns: 
            value           boolean. True if self.lines and other.lines 
                            contain the same lines. False otherwise
        """
        value = (sorted(self.lines) == sorted(other.lines))
        return value

    def __ne__(self, other):
        """Receives:
            other           Colineation
        Returns: 
            value           boolean. True if self.lines and other.lines 
                            do not contain the same lines. False otherwise
        """
        value = (sorted(self.lines) != sorted(other.lines))
        return value

    def __hash__(self):
        line_hashes = tuple(self.lines)
        value = hash(line_hashes)
        return value

    def is_empty(self):
        return len(self.lines) == 0

    def is_a_subcolineation_of(self, other):    #   called by LinePartition
        """Receives:
            other           Colineation. Self and other are colinear
        Returns:
            value           boolean. True if each line in self is a subline 
                            in other. False otherwise
        """
        value = True
        for line_i in self.lines:               #   maximal lines!
            if not line_i.is_a_subline_in_colineation(other):
                value = False
                break
        return value

    ### add
    def __add__(self, other):
        """Receives a colineation of the same carrier:
            Colineation
        Returns the sum (in maximal lines):
            Colineation
        """
        new_lines = Colineation._get_maximal_lines_from(self.lines, other.lines)
        new_colineation = Colineation(new_lines)
        return new_colineation

    @classmethod
    def _get_maximal_lines_from(cls, maximal_lines_1, maximal_lines_2):
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
    def maximal(cls, lines):                    #   revert to instance meth?
        #   Called by Colineation and LinePartition.__init__
        """Receives: 
            lines           [Line, ...]. A list, possibly empty, of colinear 
                            lines. Guaranteed (esp. if instance meth)
        Returns:
            max_lines       [Line, ...]. An ordered list of maximal lines
        """
        ordered_lines = sorted(lines)
        max_lines = []
        while len(ordered_lines) >= 1:
            max_line = cls._get_least_maximal_line_from(ordered_lines)
            max_lines.append(max_line)
        return max_lines

    @classmethod
    def _get_least_maximal_line_from(cls, lines):
        """Receives:
            lines           [Line, ...]. An ordered (non-empty) list of 
                            colinear lines. Guaranteed
        Returns:
            least_max_line  Line. The least maximal line in lines
        """
        if len(lines) == 1:
            least_max_line = cls._get_singleton_line_from(lines)
        else:
            least_max_line = cls._get_least_max_line_from_non_singleton(lines)
        return least_max_line

    @classmethod
    def _get_singleton_line_from(cls, singleton_list):
        """Receives:
            singleton_list  [Line]. A list containing a single line
        Returns:
            singleton_line  Line. The line in the list
        """
        singleton_line = singleton_list.pop(0)
        return singleton_line

    @classmethod
    def _get_least_max_line_from_non_singleton(cls, lines):
        """Receives:
            lines           [Line, ...]. An ordered list, n >= 2, of colinear 
                            lines
            least_max_line  Line. The least maximal line in lines
        """
        working_line = lines.pop(0)
        while len(lines) >= 1:
            other_line = lines[0]
            if cls._lines_can_be_merged(working_line, other_line):
                working_line = cls._merge_lines(working_line, other_line)
                lines.pop(0)
            else:
                break
        least_max_line = working_line
        return least_max_line

    @classmethod
    def _lines_can_be_merged(cls, line_1, line_2):
        """Receives:
            line_1          Line
            line_2          Line. Lines are colinear and can be merged. 
                            Guaranteed
        Returns:
            value           boolean. True if the lines can be merged. False 
                            otherwise
        See Krishnamurti (1980), 465.
        """
        if line_1.tail == line_2.head:
            value = True
        elif line_2.tail == line_1.head:
            value = True
        elif (
            line_1.tail < line_2.head and
            line_2.tail < line_1.head
        ):
            value = True
        else:
            value = False
        return value

    @classmethod
    def _merge_lines(cls, line_1, line_2):
        """Receives:
            line_1          Line
            line_2          Line. The lines are colinear and can be merged.
                            line_1.tail <= line_2.tail
        Returns:
            line_sum        Line. The sum of line_1 and line_2
        """
        new_tail = min(line_1.tail, line_2.tail)
        new_head = max(line_1.head, line_2.head)
        line_sum = line.Line(new_tail, new_head)
        return line_sum

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
                line_col_diffs = self._subtract_line_colineation(
                    line_i, other_disposable)
                col_col_diffs.extend(line_col_diffs)
                if trace_on:
                    print '||| %s' % method_name
                    print 'line_col_diffs:\n%s' % self.lines_str(line_col_diffs)
                    print 'col_col_diffs:\n%s' % self.lines_str(col_col_diffs)
        new_colineation = Colineation(col_col_diffs)
        return new_colineation

    def _subtract_line_colineation(
        self, line_minuend, colineation_subtrahend
    ):
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
            method_name = 'Colineation._subtract_line_colineation'
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
                print "Shape._subtract_line_colineation"
                print "    Oops. This subtrahend is supposed to be impossible"
        line_diffs.extend(last_line_line_diff_list)
        return line_diffs

    @classmethod
    def _print_error_message(cls, method_name, message):
        print '%s.%s:\n    %s' % (cls.__name__, method_name, message)

    ###
if __name__ == '__main__':
    import doctest
    doctest.testfile('tests/colineation_test.txt')
