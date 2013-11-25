#   sg_partition.py

import copy
import sg_column
import sg_line

class SGPartition(object):
        ### construct
    def __init__(self, lines):
        """Receives a list of collinear lines:
            [SGLine, ...], n >= 0
        """
        try:
            if lines == []:
                self.dictionary = {}
            elif not self.are_lines(lines):
                raise ValueError()
            else:
                self.dictionary = self.make_dictionary(lines)
        except ValueError:
            print "You're trying to make a partition with non-lines"

    def are_lines(self, elements):
        value = True
        for element in elements:
            if element.__class__ != sg_line.SGLine:
                value = False
                break
        return value

    def make_dictionary(self, lines):
        """Receives a list of lines:
            [SGLine, ...], n >= 0
        Returns a dictionary partitioned by carrier:
            {(num, num): SGColumn, ...}
        """
        dictionary = {}
        for element in lines:
            if element.carrier in dictionary:
                elements_by_carrier = dictionary[element.carrier]
                elements_by_carrier.append(element)
            else:
                elements_by_carrier = [element]
                dictionary[element.carrier] = elements_by_carrier
        line_01 = sg_line.SGLine.from_short_spec(0, 1)
        drone_column = sg_column.SGColumn([line_01])
        for carrier in dictionary:
            elements_by_carrier = dictionary[carrier]
            maximal_elements_by_carrier = drone_column.maximal(
                elements_by_carrier)
            column = sg_column.SGColumn(maximal_elements_by_carrier)
            dictionary[carrier] = column
        return dictionary

        ### represent
    def __str__(self):
        entry_strings = []
        for carrier in self.dictionary:
            column_string = self.dictionary[carrier].__str__()
            entry_string = '%s: [%s]' % (carrier, column_string)
            entry_strings.append(entry_string)
        entries_string = ', '.join(sorted(entry_strings))
        return '{%s}' % entries_string

    def listing(self):
        """Returns an ordered, formatted, multi-line string in the form:
            (<bearing>, <intercept>):
                (<x1>, <y1>, <x2>, <y2>)
                ...
            ...
        """
        if self.dictionary == {}:
            string = '<empty partition>'
        else:
            string_lines = []
            for carrier in sorted(self.dictionary):
                carrier_listing = self.get_carrier_listing(carrier)
                string_lines.append(carrier_listing)
                column = self.dictionary[carrier]
                column_listing_indent_level = 1
                column_listing = column.listing(column_listing_indent_level)
                string_lines.append(column_listing)
            string = '\n'.join(string_lines)
        return string

    def get_carrier_listing(self, carrier):
        bearing, intercept = carrier
        string = '(%0.1f, %0.1f):' % (bearing, intercept)
        return string

        ### relations
    def __eq__(self, other):
        return self.dictionary == other.dictionary

    def __ne__(self, other):
        return self.dictionary != other.dictionary

    def is_a_subpartition_of(self, other):
        self_keyset = set(self.dictionary.keys())
        other_keyset = set(other.dictionary.keys())
        if not self_keyset.issubset(other_keyset):
            return False
        else:
            return self.columns_are_subcolumns_in(other)

    def columns_are_subcolumns_in(self, other):
        """Receives a partition with the same carriers:
            SGPartition
        Returns whether each column is a subcolumn in the other partition.
        """
        for carrier in self.dictionary:
            if carrier not in other.dictionary:
                return False
            else:
                self_column = self.dictionary[carrier]
                other_column = other.dictionary[carrier]
                if not self_column.is_a_subcolumn_of(other_column):
                    return False
        return True

        ### add
    def __add__(self, other):
        """Receives a partition of maximal lines:
            SGPartition, n >= 0
        Returns a partition of maximal lines:
            SGPartition, n >= 0
        """
        drone_line = sg_line.SGLine.from_short_spec(0, 1)
        drone_column = sg_column.SGColumn([drone_line])
        new_dictionary = self.dictionary.copy()
        for carrier in other.dictionary:
            if carrier in new_dictionary:
                new_lines = new_dictionary[carrier].lines
                other_lines = other.dictionary[carrier].lines
                new_lines = (
                    drone_column.get_maximal_lines_from(
                        new_lines, other_lines))
                new_column = sg_column.SGColumn(new_lines)
                new_dictionary[carrier] = new_column
            else:
                new_dictionary[carrier] = other.dictionary[carrier]
        new_partition = SGPartition([])
        new_partition.dictionary = new_dictionary
        return new_partition

        ### subtract

        ###
if __name__ == '__main__':
    import doctest
    doctest.testfile('tests/sg_partition_test.txt')
