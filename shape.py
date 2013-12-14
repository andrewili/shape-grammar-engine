#   shape.py

import copy
import line
import line_partition

class Shape(object):
        ### construct
    def __init__(self, line_partition_in):
        """Receives a LinePartition.
        """
        self.line_part = line_partition_in

    @classmethod
    def from_lines(cls, lines):
        new_line_partition = line_partition.LinePartition(lines)
        new_shape = Shape(new_line_partition)
        return new_shape

    @classmethod
    def from_specs(cls, specs):
        """Receives a list of line specs:
            [(x1, y1, x2, y2), ...]
        Returns a shape consisting of those lines
            Shape
        """
        lines = []
        for spec in specs:
            x1, y1, x2, y2 = spec
            line_i = line.Line.from_spec(x1, y1, x2, y2)
            lines.append(line_i)
        new_line_partition = line_partition.LinePartition(lines)
        new_shape = Shape(new_line_partition)
        return new_shape

    @classmethod
    def new_empty(cls):
        empty_line_partition = line_partition.LinePartition.new_empty()
        new_shape = Shape(empty_line_partition)
        return new_shape

        ### represent
    def __str__(self):
        """Returns the string of the ordered line specs:
            [(x1, y1, x2, y2), ...]
        """
        return self.line_part.__str__()

    def get_sorted_line_strings(self):
        """Returns an ordered list of line strings in the form:
            [(x1, y1, x2, y2), ...]
        """
        spec_strings = []
        for carrier in self.line_part.dictionary:
            new_colineation = self.line_part.dictionary[carrier]
            colineation_spec_strings = self.get_colineation_spec_strings_from(
                new_colineation)
            spec_strings.extend(colineation_spec_strings)
        return sorted(spec_strings)

    def get_colineation_spec_strings_from(self, colineation_in):    #   move to Colineation
        """Receives a Colineation
        Returns a list of spec strings of the lines in the colineation:
            ['(x1, y1, x2, y2)', ...]
        """
        spec_strings = []
        for line_i in colineation_in.lines:
            spec_strings.append(line_i.__str__())
        return spec_strings

    def listing(self):
        if self.is_empty():
            string = '<no lines>'
        else:
            string = self.line_part.listing()
        return string

    def get_partition_listing(self, line_partition_in):     #   to LinePartition
        """Returns a string in the ordered form:
            carrier:
                line_spec
                ...
            ...
        """
        #   Refactor with join()
        s = ''
        i = 1
        n = len(line_partition_in)
        if n == 0:
            s = '<no lines>'
        else:
            for carrier in sorted(line_partition_in):
                carrier_listing = self.get_carrier_listing(carrier)
                new_colineation = line_partition_in[carrier]
                colineation_listing = self.get_colineation_listing(
                    new_colineation)
                s += '%s:\n%s' % (carrier_listing, colineation_listing)
                if i < n:
                    s += '\n'
                i += 1
        return s

    def get_carrier_listing(self, carrier):                 #   to LinePartition?
        bearing, intercept = carrier
        s = '(%3.1f, %3.1f)' % (bearing, intercept)
        return s

    def get_colineation_listing(self, colineation_in):      #   to Colineation
        #   len(colineation_in) >= 1
        s = ''
        tab = ' ' * 4
        i = 1
        n = len(colineation_in)
        for line_i in sorted(colineation_in):
            line_listing = '%s%s' % (tab, line_i)
            if i < n:
                line_listing += '\n'
            i += 1
            s += line_listing
        return s

        ### relations
    def __eq__(self, other):
        return self.line_part == other.line_part

    def __ne__(self, other):
        return self.line_part != other.line_part

    def is_empty(self):
        return self.line_part.is_empty()

    def is_a_subshape_of(self, other):
        return self.line_part.is_a_sub_line_partition_of(other.line_part)

        ### add
    def __add__(self, other):
        new_line_partition = self.line_part + other.line_part
        return Shape(new_line_partition)

        ### subtract
    def __sub__(self, other):
        """Receives:
            Shape
        Returns the difference:
            Shape
        """
        if self.line_part == {}:
            new_partition = {}
        elif other.line_part == {}:
            new_partition = self.line_part
        else:
            new_partition = self.subtract_non_empty_line_partitions(
                self.line_part, other.line_part)
        new_shape = Shape(new_partition)
##        print '||| Shape.__sub__.new_shape: %s' % new_shape
        return new_shape

    def subtract_non_empty_line_partitions(self, partition_1, partition_2):
        """Receives 2 line partitions:
            {carrier: colineation, ...}, n >= 1
        Returns a line partition, possibly empty, such that, for each
        carrier, each colineation is the difference 
        colineation_1 - colineation_2. If a difference is the empty colineation, 
        the entry is excluded from the partition
            {carrier: colineation, ...}, n >= 0
        """
        trace_on = False
        if trace_on:
            method_name = 'Shape.subtract_non_empty_line_partitions'
            partition_1_listing = self.get_partition_listing(partition_1)
            print '||| %s.partition_1:\n%s' % (method_name, partition_1_listing)
            partition_2_listing = self.get_partition_listing(partition_2)
            print '||| %s.partition_2:\n%s' % (method_name, partition_2_listing)
        new_partition = {}
        for carrier in partition_1:
            colineation_1 = partition_1[carrier]
            if trace_on:
                carrier_listing = self.get_carrier_listing(carrier)
                print '||| %s.carrier:\n%s' % (method_name, carrier_listing)
                colineation_1_listing = self.get_colineation_listing(
                    colineation_1)
                print '||| %s.colineation_1:\n%s' % (
                    method_name, colineation_1_listing)
            if carrier in partition_2:
                colineation_2 = copy.copy(partition_2[carrier])
                new_colineation = self.subtract_colineation_colineation(
                    colineation_1, colineation_2)
                if trace_on:
                    colineation_2_listing = self.get_colineation_listing(
                        colineation_2)
                    print '||| %s.colineation_2:\n%s' % (
                        method_name, colineation_2_listing)
                    new_colineation_listing = self.get_colineation_listing(
                        new_colineation)
                    print '||| %s.new_colineation:\n%s' % (
                        method_name, new_colineation_listing)
            else:
                new_colineation = colineation_1
            if new_colineation == []:
                pass
            else:
                new_partition[carrier] = new_colineation
        if trace_on:
            new_partition_listing = self.get_partition_listing(new_partition)
            print '||| %s.new_partition: \n%s' % (
                method_name, new_partition_listing)
        return new_partition

    def subtract_colineation_colineation(
        self, colineation_1, working_colineation_2
    ):
        """Receives 2 non-empty colinear colineations:
            [Line, ...], n >= 1
        Returns an ordered colineation, possibly empty, of the lines in 
        colineation_1 and not in working_colineation_2:
            [Line, ...], n >= 0
        """
        trace_on = False
        if trace_on:
            method_name = 'Shape.subtract_colineation_colineation'
            colineation_1_listing = self.get_colineation_listing(colineation_1)
            print '||| %s.colineation_1\n%s' % (
                method_name, colineation_1_listing)
            working_colineation_2_listing = self.get_colineation_listing(
                working_colineation_2)
            print '||| %s.working_colineation_2\n%s' % (
                method_name, working_colineation_2_listing)
        colineation_colineation_differences = []
        for line_1 in colineation_1:
            if trace_on:
                print '||| %s.line_1:\n%s' % (method_name, line_1)
            if working_colineation_2 == []:
                colineation_colineation_differences.append(line_1)
            else:
                line_colineation_differences = self.subtract_line_colineation(
                    line_1, working_colineation_2)
                colineation_colineation_differences.extend(
                    line_colineation_differences)
                if trace_on:
                    line_colineation_differences_listing = (
                        self.get_colineation_listing(
                            line_colineation_differences))
                    print '||| %s.line_colineation_differences:\n%s' % (
                        method_name, line_colineation_differences_listing)
                    colineation_colineation_differences_listing = (
                        self.get_colineation_listing(
                            colineation_colineation_differences))
                    print '||| %s.colineation_colineation_differences:\n%s' % (
                        method_name, 
                        colineation_colineation_differences_listing)
        return colineation_colineation_differences

    def subtract_line_colineation(self, line_minuend, working_colineation):
        """Receives a line minuend and a non-empty colinear working colineation 
        of line subtrahends:
            line_minuend: Line
            working_colineation: [Line, ...], n >= 1
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
        # Subtract and discard those line subtrahends that overlaps the left or
        # the middle of the line minuend
        # What about line subtrahends that overlaps the whole line minuend?
        # Subtract and retain the line subtrahend that overlaps the head of the
        # line minuend

        trace_on = False
        line_colineation_differences = []
        working_minuend = line_minuend
        last_line_line_difference_list = []
        if trace_on:
            method_name = 'Shape.subtract_line_colineation'
            print '||| %s.working_minuend:\n%s' % (method_name, working_minuend)
            working_colineation_listing = self.get_colineation_listing(
                working_colineation)
            print '||| %s.working_colineation:\n%s' % (
                method_name, working_colineation_listing)
        while working_colineation != []:
            line_line_differences = []
            line_subtrahend = working_colineation[0]
            if trace_on:
                print '||| %s.line_subtrahend:\n%s' % (
                    method_name, line_subtrahend)
                print '||| %s.working_colineation[1]:\n%s' % (
                    method_name, working_colineation[1])
            if line_subtrahend.is_disjoint_left_of(working_minuend):
                # difference = empty line
                # discard subtrahend and try with next, if any
                last_line_line_difference_list = [working_minuend]
                working_colineation.pop(0)
            elif line_subtrahend.overlaps_tail_of(working_minuend):
                # subtract; discard subtrahend and try with next, if any
                line_line_differences = working_minuend.subtract_line_tail(
                    line_subtrahend)
                working_minuend = line_line_differences[0]
                last_line_line_difference_list = [line_line_differences[0]]
                working_colineation.pop(0)
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
                line_colineation_differences.append(line_line_differences[0])
                working_minuend = line_line_differences[1]
                last_line_line_difference_list = [line_line_differences[1]]
                working_colineation.pop(0)
            elif line_subtrahend.overlaps_head_of(working_minuend):
                # subtract; retain subtrahend and try with next minuend
                line_line_differences = working_minuend.subtract_line_head(
                    line_subtrahend)
                line_colineation_differences.append(line_line_differences[0])
                last_line_line_difference_list = []
                if trace_on:
                    line_line_differences_listing = (
                        self.get_colineation_listing(
                            line_line_differences))
                    print '||| %s.line_line_differences:\n%s' % (
                        method_name, line_line_differences_listing)
                    line_colineation_differences_listing = (
                        self.get_colineation_listing(
                            line_colineation_differences))
                    print '||| %s.line_colineation_differences:\n%s' % (
                        method_name, line_colineation_differences_listing)
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
        line_colineation_differences.extend(last_line_line_difference_list)
        return line_colineation_differences

        ###
if __name__ == '__main__':
    import doctest
    doctest.testfile('tests/shape_test.txt')
