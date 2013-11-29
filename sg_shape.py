#   sg_shape.py

import copy
import sg_line
import sg_partition

class SGShape(object):
        ### construct
    def __init__(self, partition):
        """Receives an SGPartition.
        """
        self.partition = partition

    @classmethod
    def from_lines(cls, lines):
        partition = sg_partition.SGPartition(lines)
        shape = SGShape(partition)
        return shape

    @classmethod
    def from_specs(cls, specs):
        """Receives a list of line specs:
            [(x1, y1, x2, y2), ...]
        Returns a shape consisting of those lines
            SGShape
        """
        lines = []
        for spec in specs:
            x1, y1, x2, y2 = spec
            line = sg_line.SGLine.from_spec(x1, y1, x2, y2)
            lines.append(line)
        partition = sg_partition.SGPartition(lines)
        shape = SGShape(partition)
        return shape

        ### represent
    def __str__(self):
        """Returns the string of the ordered line specs:
            [(x1, y1, x2, y2), ...]
        """
        return self.partition.__str__()

    def get_sorted_line_strings(self):
        """Returns an ordered list of line strings in the form:
            [(x1, y1, x2, y2), ...]
        """
        spec_strings = []
        for carrier in self.partition.dictionary:
            column = self.partition.dictionary[carrier]
            column_spec_strings = self.get_column_spec_strings_from(column)
            spec_strings.extend(column_spec_strings)
        return sorted(spec_strings)

    def get_column_spec_strings_from(self, column):
        """Receives an SGColumn
        Returns a list of spec strings of the lines in the column:
            ['(x1, y1, x2, y2)', ...]
        """
        spec_strings = []
        for line in column.lines:
            spec_strings.append(line.__str__())
        return spec_strings

    def listing(self):
        if self.is_empty():
            string = '<empty shape>'
        else:
            string = self.partition.listing()
        return string

    def get_partition_listing(self, partition):
        """Returns a string in the ordered form:
            carrier:
                line_spec
                ...
            ...
        """
        #   Refactor with join()
        s = ''
        i = 1
        n = len(partition)
        if n == 0:
            s = '<no lines>'
        else:
            for carrier in sorted(partition):
                carrier_listing = self.get_carrier_listing(carrier)
                column = partition[carrier]
                column_listing = self.get_column_listing(column)
                s += '%s:\n%s' % (carrier_listing, column_listing)
                if i < n:
                    s += '\n'
                i += 1
        return s

    def get_carrier_listing(self, carrier):
        bearing, intercept = carrier
        s = '(%3.1f, %3.1f)' % (bearing, intercept)
        return s

    def get_column_listing(self, column):
        #   len(column) >= 1
        s = ''
        tab = ' ' * 4
        i = 1
        n = len(column)
        for line in sorted(column):
            line_listing = '%s%s' % (tab, line)
            if i < n:
                line_listing += '\n'
            i += 1
            s += line_listing
        return s

        ### relations
    def __eq__(self, other):
        return self.partition == other.partition

    def __ne__(self, other):
        return self.partition != other.partition

    def is_empty(self):
        return self.partition.is_empty()

    def is_a_subshape_of(self, other):
        return self.partition.is_a_subpartition_of(other.partition)

        ### add
    def __add__(self, other):
        new_partition = self.partition + other.partition
        return SGShape(new_partition)

        ### subtract
    def __sub__(self, other):
        """Receives:
            SGShape
        Returns the difference:
            SGShape
        """
        if self.partition == {}:
            new_partition = {}
        elif other.partition == {}:
            new_partition = self.partition
        else:
            new_partition = self.subtract_non_empty_line_partitions(
                self.partition, other.partition)
        new_shape = SGShape(new_partition)
##        print '||| SGShape.__sub__.new_shape: %s' % new_shape
        return new_shape

    def subtract_non_empty_line_partitions(self, partition_1, partition_2):
        """Receives 2 line partitions:
            {carrier: column, ...}, n >= 1
        Returns a line partition, possibly empty, such that, for each
        carrier, each column is the difference column_1 - column_2. If a
        difference is the empty column, the entry is excluded from the
        partition
            {carrier: column, ...}, n >= 0
        """
        trace_on = False
        if trace_on:
            method_name = 'SGShape.subtract_non_empty_line_partitions'
            partition_1_listing = self.get_partition_listing(partition_1)
            print '||| %s.partition_1:\n%s' % (method_name, partition_1_listing)
            partition_2_listing = self.get_partition_listing(partition_2)
            print '||| %s.partition_2:\n%s' % (method_name, partition_2_listing)
        new_partition = {}
        for carrier in partition_1:
            column_1 = partition_1[carrier]
            if trace_on:
                carrier_listing = self.get_carrier_listing(carrier)
                print '||| %s.carrier:\n%s' % (method_name, carrier_listing)
                column_1_listing = self.get_column_listing(column_1)
                print '||| %s.column_1:\n%s' % (method_name, column_1_listing)
            if carrier in partition_2:
                column_2 = copy.copy(partition_2[carrier])
                new_column = self.subtract_column_column(column_1, column_2)
                if trace_on:
                    column_2_listing = self.get_column_listing(column_2)
                    print '||| %s.column_2:\n%s' % (method_name, column_2_listing)
                    new_column_listing = self.get_column_listing(new_column)
                    print '||| %s.new_column:\n%s' % (
                        method_name, new_column_listing)
            else:
                new_column = column_1
            if new_column == []:
                pass
            else:
                new_partition[carrier] = new_column
        if trace_on:
            new_partition_listing = self.get_partition_listing(new_partition)
            print '||| %s.new_partition: \n%s' % (method_name, new_partition_listing)
        return new_partition

    def subtract_column_column(self, column_1, working_column_2):
        """Receives 2 non-empty colinear columns:
            [SGLine, ...], n >= 1
        Returns an ordered column, possibly empty, of the lines in column_1 and
        not in working_column_2:
            [SGLine, ...], n >= 0
        """
        trace_on = False
        if trace_on:
            method_name = 'SGShape.subtract_column_column'
            column_1_listing = self.get_column_listing(column_1)
            print '||| %s.column_1\n%s' % (method_name, column_1_listing)
            working_column_2_listing = self.get_column_listing(working_column_2)
            print '||| %s.working_column_2\n%s' % (
                method_name, working_column_2_listing)
        column_column_differences = []
        for line_1 in column_1:
            if trace_on:
                print '||| %s.line_1:\n%s' % (method_name, line_1)
            if working_column_2 == []:
                column_column_differences.append(line_1)
            else:
                line_column_differences = self.subtract_line_column(
                    line_1, working_column_2)
                column_column_differences.extend(line_column_differences)
                if trace_on:
                    line_column_differences_listing = self.get_column_listing(
                        line_column_differences)
                    print '||| %s.line_column_differences:\n%s' % (
                        method_name, line_column_differences_listing)
                    column_column_differences_listing = self.get_column_listing(
                        column_column_differences)
                    print '||| %s.column_column_differences:\n%s' % (
                        method_name, column_column_differences_listing)
        return column_column_differences

    def subtract_line_column(self, line_minuend, working_column):
        """Receives a line minuend and a non-empty colinear working column of
        line subtrahends:
            line_minuend: SGLine
            working_column: [SGLine, ...], n >= 1
        Returns an ordered list of the line differences obtained by subtracting
        the line subtrahends from the (single) line minuend:
            [SGLine, ...], n >= 0
        Removes from the working column 1) the line subtrahends that lie to the
        left of the line minuend's tail and 2) those that have been subtracted 
        and leave the line minuend's head unchanged. (The remaining line 
        subtrahends will be subtracted from subsequent line minuends, if any.)
        """
        # Discard the disjoint line subtrahends (if any) on the left of the line
        # minuend
        # Subtract and discard those line subtrahends that overlaps the left or
        # the middle of the line minuend
        # What about line subtrahends that overlaps the whole line minuend?
        # Subtract and retain the line subtrahend that overlaps the head of the
        # line minuend

        trace_on = False
        line_column_differences = []
        working_minuend = line_minuend
        last_line_line_difference_list = []
        if trace_on:
            method_name = 'SGShape.subtract_line_column'
            print '||| %s.working_minuend:\n%s' % (method_name, working_minuend)
            working_column_listing = self.get_column_listing(working_column)
            print '||| %s.working_column:\n%s' % (
                method_name, working_column_listing)
        while working_column != []:
            line_line_differences = []
            line_subtrahend = working_column[0]
            if trace_on:
                print '||| %s.line_subtrahend:\n%s' % (
                    method_name, line_subtrahend)
                print '||| %s.working_column[1]:\n%s' % (
                    method_name, working_column[1])
            if line_subtrahend.is_disjoint_left_of(working_minuend):
                # difference = empty line
                # discard subtrahend and try with next, if any
                last_line_line_difference_list = [working_minuend]
                working_column.pop(0)
            elif line_subtrahend.overlaps_tail_of(working_minuend):
                # subtract; discard subtrahend and try with next, if any
                line_line_differences = working_minuend.subtract_line_tail(
                    line_subtrahend)
                working_minuend = line_line_differences[0]
                last_line_line_difference_list = [line_line_differences[0]]
                working_column.pop(0)
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
                line_column_differences.append(line_line_differences[0])
                working_minuend = line_line_differences[1]
                last_line_line_difference_list = [line_line_differences[1]]
                working_column.pop(0)
            elif line_subtrahend.overlaps_head_of(working_minuend):
                # subtract; retain subtrahend and try with next minuend
                line_line_differences = working_minuend.subtract_line_head(
                    line_subtrahend)
                line_column_differences.append(line_line_differences[0])
                last_line_line_difference_list = []
                if trace_on:
                    line_line_differences_listing = self.get_column_listing(
                        line_line_differences)
                    print '||| %s.line_line_differences:\n%s' % (
                        method_name, line_line_differences_listing)
                    line_column_differences_listing = self.get_column_listing(
                        line_column_differences)
                    print '||| %s.line_column_differences:\n%s' % (
                        method_name, line_column_differences_listing)
                    print '||| %s.last_line_line_difference: %s' % (
                        method_name, last_line_line_difference_list)
                break
            elif line_subtrahend.is_disjoint_right_of(working_minuend):
                # difference = empty line
                # retain subtrahend and try with next minuend
                last_line_line_difference_list = [working_minuend]
                break
            else:
                print "SGShape.subtract_line_column"
                print "    Oops. This subtrahend is supposed to be impossible"
        line_column_differences.extend(last_line_line_difference_list)
        return line_column_differences

        ###
if __name__ == '__main__':
    import doctest
    doctest.testfile('tests/sg_shape_test.txt')
