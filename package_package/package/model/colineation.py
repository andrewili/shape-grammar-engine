import copy
import line

class Colineation(object):
    """Has an ordered, possibly empty, list of (unique) maximal colinear lines 
    Immutable
    """
    ### construct
    def __init__(self, lines):
        """Receives:
            lines           [Line, ...]. An unordered list of non-unique 
                            colinear lines
        """
        method_name = '__init__'
        try:
            if not (
                type(lines) == list and 
                self._are_lines(lines)
            ):
                raise TypeError
            elif not (
                lines == [] or
                self._are_colinear(lines)
            ):
                raise ValueError
        except TypeError:
            message = (
                "The argument must be a list of colinear lines")
            self._print_error_message(method_name, message)
        except ValueError:
            message = (
                "The list must be non-empty and the lines must be colinear")
            self._print_error_message(method_name, message)
        else:
            if lines == []:
                self.lines = []
            else:
                first_line = lines[0]
                self.carrier = first_line.carrier
                self.uv = first_line.uv
                self.int = first_line.int
                self.lines = self.maximize(lines)

    def _are_lines(self, items):
        """Receives:
            items           [item, ...]. A list of items
        Returns:
            value           boolean. True if all the items in the list are 
                            lines. False otherwise
        """
        value = True
        for item in items:
            if not type(item) == line.Line:
                value = False
                break
        return value

    def _are_colinear(self, lines):
        """Receives:
            lines           [Line, ...]. A non_empty list of lines. 
                            Guaranteed by the calling function
        Returns:
            value           boolean. True if the list is empty or if the 
                            lines are colinear. False otherwise
        """
        value = True
        carrier = lines[0].carrier
        for line_i in lines:
            if line_i.carrier != carrier:
                value = False
        return value

    @classmethod
    def new_empty(cls):                         ##  used for LinePartition 
                                                ##  test only
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
                new_line = line.Line.from_specs_2(x, y)
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

    # def lines_str(self, lines):                 ##  used by trace
        # """Receives a list of lines:
        #     [Line, ...]
        # Returns a string: 
        #     [(x1, y1, x2, y2), ...]
        # """
        # line_strings = []
        # for line_i in lines:
        #     line_string = line_i.__str__()
        #     line_strings.append(line_string)
        # lines_string = ', '.join(line_strings)
        # return '[%s]' % lines_string

    # def specs(self):                          ##  suspended
        # """Returns:
        #     line_specs      [line_spec, ...]. An ordered list of line specs, 
        #                     where:
        #         line_spec   (<x1>, <y1>, <z1>, <x2>, <y2>, <z2>)
        # """
        # line_specs = []
        # for l in self.lines:
        #     line_specs.append(l.spec)
        # return sorted(line_specs)

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

    def is_a_subcolineation_of(self, other):
        """Is called by:    LinePartition.colineations_are_subcolineations_in
        Receives:
            other           Colineation. Self and other are colinear. 
                            Guaranteed by the calling function 
        Returns:
            value           boolean. True if each line in self is a subline 
                            in other. False otherwise
        """
        value = True
        for line_i in self.lines:
            if not line_i.is_a_subline_in_colineation(other):
                value = False
                break
        return value

    ### add
    def __add__(self, other):                     ##  formerly merge
        """Receives:
            other           Colineation. Colinear with self
        Returns:
            new_colin       Colineation. Has a list of merged lines from 
                            self.lines and other.lines
        """
        method_name = '__add__'
        try:
            if not type(other) == Colineation:
                value = None
                raise TypeError
            if not self.carrier == other.carrier:
                value = None
                raise ValueError
        except TypeError:
            message = 'The argument must be a colineation'
            self._print_error_message(method_name, message)
        except ValueError:
            message = 'The colineations must be colinear'
            self._print_error_message(method_name, message)
        else:
            new_lines = copy.copy(self.lines)
            new_lines.extend(other.lines)
            self.maximize(new_lines)
            value = colin_sum = Colineation(new_lines)
        finally:
            return value

    def _get_maximal_lines_from(self, maximal_lines_1, maximal_lines_2):
        """Receives:
            maximal_lines_1 [Line, ...]. A non-empty ordered list of unique 
                            maximal lines
            maximal_lines_2 [Line, ...]. As for maximal_lines_1
        Returns:
            new_maximal_lines 
                            [Line, ...]. A list of the maximal lines obtained 
                            by merging max_lines_1 and max_lines_2
        """
        non_maximal_unsorted_lines = []
        non_maximal_unsorted_lines.extend(maximal_lines_1)
        non_maximal_unsorted_lines.extend(maximal_lines_2)
        sorted_non_maximal_lines = sorted(non_maximal_unsorted_lines)
        new_maximal_lines = self.maximize(sorted_non_maximal_lines)
        return new_maximal_lines

    def maximize(self, lines):
        """Is called by:    self and LinePartition.__init__
        Receives: 
            lines           [Line, ...]. A list, possibly empty, of colinear 
                            lines
        Returns:
            ordered_max_lines
                            [Line, ...]. An ordered list of maximal lines
        """
        ordered_lines = sorted(lines)
        ordered_max_lines = []
        while len(ordered_lines) >= 1:
            max_line = self._get_least_maximal_line_from(ordered_lines)
            ordered_max_lines.append(max_line)
        return ordered_max_lines

    def _get_least_maximal_line_from(self, lines):
        """Receives:
            lines           [Line, ...]. An ordered (non-empty) list of 
                            colinear lines. Guaranteed
        Returns:
            least_max_line  Line. The least maximal line in lines
        """
        if len(lines) == 1:
            least_max_line = self._get_singleton_line_from(lines)
        else:
            least_max_line = self._get_least_max_line_from_non_singleton(lines)
        return least_max_line

    def _get_singleton_line_from(self, singleton_list):
        """Receives:
            singleton_list  [Line]. A list containing a single line
        Returns:
            singleton_line  Line. The line in the list
        """
        singleton_line = singleton_list.pop(0)
        return singleton_line

    def _get_least_max_line_from_non_singleton(self, lines):
        """Receives:
            lines           [Line, ...]. An ordered list, n >= 2, of colinear 
                            lines
            least_max_line  Line. The least maximal line in lines
        """
        working_line = lines.pop(0)
        while len(lines) >= 1:
            least_line = lines[0]
            if working_line.can_be_merged_with(least_line):
                working_line = working_line.merge_with(least_line)
                lines.pop(0)
            else:
                break
        least_max_line = working_line
        return least_max_line

    ### subtract
    def __sub__(self, other):
        """Receives:
            other           Colineation. Colinear with self
        Returns:
            new_colineation Colineation. Has a non-empty list of the lines 
                            obtained by subtracting all the lines in other 
                            from all the lines in self. If there are no lines, 
                            returns None
        """
        trace_on = False
        method_name = '__sub__'
        try:
            if not type(other) == Colineation:
                raise TypeError
            elif not self.carrier == other.carrier:
                raise ValueError
        except TypeError:
            message = "The argument must be a colineation"
            self._print_error_message(method_name, message)
            new_colineation = None
        except ValueError:
            message = "The subtrahend and the minuend must be colinear"
            self._print_error_message(method_name, message)
            new_colineation = None
        else:
            if trace_on:
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
                        print 'line_col_diffs:\n%s' % (
                            self.lines_str(line_col_diffs))
                        print 'col_col_diffs:\n%s' % (
                            self.lines_str(col_col_diffs))
            new_colineation = Colineation(col_col_diffs)
        finally:
            return new_colineation

    def _subtract_line_colineation(self, line_min, colin_sub):
        """Receives:
            line_min        Line. The minuend
            colin_sub       Colineation. The subtrahend. By definition 
                            non-empty, ordered, unique, maximal
        Returns:
            lines_diff      [Line, ...]. An ordered, possibly empty, list of 
                            the line differences obtained by subtracting
                            the line subtrahend(s) from the (single) line 
                            minuend
        Removes from the working colineation 1) the line subtrahends that lie 
        to the left of the line minuend's tail and 2) those that have been 
        subtracted and leave the line minuend's head unchanged. (The 
        remaining line subtrahends will be subtracted from subsequent line 
        minuends, if any.)
        """
        # Discard the disjoint line subtrahends (if any) on the left of the line
        # minuend
        # Subtract and discard those line subtrahends that overlap the left or
        # the middle of the line minuend
        # What about line subtrahends that overlap the whole line minuend?
        # Subtract and retain the line subtrahend that overlaps the head of the
        # line minuend
        trace_on = False
        lines_diff = []
        working_min = line_min
        working_col = colin_sub
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
            if line_sub.is_disjoint_less_than(working_min):
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
                lines_diff.append(line_line_diffs[0])
                working_min = line_line_diffs[1]
                last_line_line_diff_list = [line_line_diffs[1]]
                working_col.lines.pop(0)
            elif line_sub.overlaps_head_of(working_min):
                # subtract; retain subtrahend and try with next minuend
                line_line_diffs = working_min.subtract_line_head(
                    line_sub)
                lines_diff.append(line_line_diffs[0])
                last_line_line_diff_list = []
                if trace_on:
                    print '||| %s' % method_name
                    line_line_diffs_listing = (
                        self.get_colineation_listing(
                            line_line_diffs))
                    print 'line_line_diffs:\n%s' % line_line_diffs_listing
                    line_diffs_listing = (
                        self.get_colineation_listing(
                            lines_diff))
                    print 'lines_diff:\n%s' % line_diffs_listing
                    print 'last_line_line_diff: %s' % last_line_line_diff_list
                break
            elif line_sub.is_disjoint_greater_than(working_min):
                # difference = empty line
                # retain subtrahend and try with next minuend
                last_line_line_diff_list = [working_min]
                break
            else:
                print "Shape._subtract_line_colineation"
                print "    Oops. This subtrahend is supposed to be impossible"
        lines_diff.extend(last_line_line_diff_list)
        return lines_diff

    def intersection(self, other):
        """Receives:
            other           Colineation
        Returns:
            colin_intersect Colineation. Has an (ordered) list of (maximal) 
                            lines such that each is a part both of a line in 
                            self.lines and a line in other.lines 
        """
        pass

    def union(self, other):                     ##  same as __add__?
        """Receives:
            other           Colineation
        Returns:
            colin_union     Colineation. Has an (ordered) list of (maximal) 
                            merged lines from self.lines and other.lines
        """
        pass

    @classmethod
    def _print_error_message(cls, method_name, message):
        print '%s.%s:\n    %s' % (cls.__name__, method_name, message)

    ###
if __name__ == '__main__':
    import doctest
    doctest.testfile('tests/colineation_test.txt')
