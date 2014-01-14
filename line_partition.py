#   line_partition.py

import colineation
import copy
import line

class LinePartition(object):
    
    ### construct
    def __init__(self, lines):
        """Receives a list of collinear lines:
            [Line, ...], n >= 0
        """
        try:
            if lines == []:
                self.dictionary = {}
            elif not self.are_lines(lines):
                raise ValueError()
            else:
                self.dictionary = self.make_dictionary(lines)
        except ValueError:
            print "You're trying to make a line partition with non-lines"

    def are_lines(self, lines):
        value = True
        for line_i in lines:
            if line_i.__class__ != line.Line:
                value = False
                break
        return value

    def make_dictionary(self, lines):
        """Receives a list of lines:
            [Line, ...], n >= 0
        Returns a dictionary partitioned by carrier:
            {(num, num): Colineation, ...}
        """
        dictionary = {}
        for line_i in lines:
            if line_i.carrier in dictionary:
                lines_by_carrier = dictionary[line_i.carrier]
                lines_by_carrier.append(line_i)
            else:
                lines_by_carrier = [line_i]
                dictionary[line_i.carrier] = lines_by_carrier
        for carrier in dictionary:
            lines_by_carrier = dictionary[carrier]
            maximal_lines_by_carrier = colineation.Colineation.maximal(
                lines_by_carrier)
            new_colineation = colineation.Colineation(
                maximal_lines_by_carrier)
            dictionary[carrier] = new_colineation
        return dictionary

    @classmethod
    def from_dictionary(cls, dictionary):
        """Receives a dictionary of carrier-colineation entries:
        {(num, num): Colineation, ...}
        """
        new_line_partition = LinePartition([])
        new_line_partition.dictionary = dictionary
        return new_line_partition

    ### represent
    def __str__(self):
        """Returns the string of ordered line specs:
            [(x1, y1, x2, y2), ...]
        """
        lines = []
        for carrier_i in self.dictionary:
            colineation_i = self.dictionary[carrier_i]
            lines_by_carrier = colineation_i.lines
            lines.extend(lines_by_carrier)
        line_strings = []
        for line_i in sorted(lines):
            line_strings.append(line_i.__str__())
        line_string = ', '.join(sorted(line_strings))
        string = '[%s]' % line_string
        return string

    def listing(self):                                                          #   back to shape
        """Returns an ordered, formatted, multi-line string in the form:
            (bearing, intercept):
                (x1, y1, x2, y2)
                ...
            ...
        """
        if self.dictionary == {}:
            string = '<empty line partition>'
        else:
            string_lines = []
            for carrier_i in sorted(self.dictionary):
                carrier_listing = self.get_carrier_listing(carrier_i)
                string_lines.append(carrier_listing)
                colineation_i = self.dictionary[carrier_i]
                indent_level = 1                                                #   move out of loop
                colineation_listing = colineation_i.listing(indent_level)       #   create indentation here?
                string_lines.append(colineation_listing)
            string = '\n'.join(string_lines)
        return string

    ### get
    def specs(self):
        """Returns an ordered list of line specs:
            [(x1, y1, x2, y2), ...]
        """
        specs = []
        for carrier_i in self.dictionary:
            colineation_i = self.dictionary[carrier_i]
            colineation_i_specs = colineation_i.specs()
            specs.extend(colineation_i_specs)
        return sorted(specs)

    def get_carrier_listing(self, carrier):
        bearing, intercept = carrier
        string = '(%3.1f, %3.1f):' % (bearing, intercept)
        return string

    @classmethod
    def new_empty(cls):
        empty_partition = LinePartition([])
        return empty_partition
        
    ### relations
    def __eq__(self, other):
        return self.dictionary == other.dictionary

    def __ne__(self, other):
        return self.dictionary != other.dictionary

    def is_empty(self):
        return self.dictionary == {}
        
    def is_a_sub_line_partition_of(self, other):
        self_keyset = set(self.dictionary.keys())
        other_keyset = set(other.dictionary.keys())
        if not self_keyset.issubset(other_keyset):
            return False
        else:
            return self.colineations_are_subcolineations_in(other)

    def colineations_are_subcolineations_in(self, other):
        """Receives a line partition with the same carriers:
            LinePartition
        Returns whether each colineation is a subcolineation in the other 
        line partition.
        """
        for carrier in self.dictionary:
            if carrier not in other.dictionary:
                return False
            else:
                self_colineation = self.dictionary[carrier]
                other_colineation = other.dictionary[carrier]
                if not self_colineation.is_a_subcolineation_of(
                    other_colineation
                ):
                    return False
        return True

    ### add
    def __add__(self, other):
        """Receives a line partition of maximal lines:
            LinePartition, n >= 0
        Returns a line partition of maximal lines:
            LinePartition, n >= 0
        """
        new_dictionary = self.dictionary.copy()
        for carrier in other.dictionary:
            if carrier in new_dictionary:
                self_colineation = new_dictionary[carrier]
                other_colineation = other.dictionary[carrier]
                new_colineation = self_colineation + other_colineation
                new_dictionary[carrier] = new_colineation
            else:
                new_dictionary[carrier] = other.dictionary[carrier]
        new_partition = LinePartition.from_dictionary(new_dictionary)
        return new_partition

    ### subtract
    def __sub__(self, other):
        """Receives a line partition:                                           #   empty colineations?
            LinePartition, n(entries) >= 0
        Returns the line partition, possibly empty, such that for each carrier 
        each colineation is the difference colineation_1 - colineation_2. If a 
        difference is the empty colineation, the entry is excluded from the 
        partition.
            LinePartition, n(entries) >= 0
        """
        trace_on = False
        if trace_on:
            method_name = 'LinePartition.__sub__'
            print '||| %s.self:\n%s' % (method_name, self.listing())
            print '||| %s.other:\n%s' % (method_name, other.listing())
        new_line_part = LinePartition([])
        line_dict_1 = self.dictionary
        for carrier in line_dict_1:
            colineation_1 = line_dict_1[carrier]
            if trace_on:
                carrier_listing = self.get_carrier_listing(carrier)
                print '||| %s.carrier:\n%s' % (method_name, carrier_listing)
                print '||| %s.colineation_1:\n%s' % (
                    method_name, colineation_1.listing())
            line_dict_2 = other.dictionary
            if carrier in line_dict_2:
                colineation_2 = copy.copy(line_dict_2[carrier])
                new_colineation = colineation_1 - colineation_2                 #    if new_colineation is empty?
                if trace_on:
                    print '||| %s.colineation_2:\n%s' % (
                        method_name, colineation_2.listing())
                    print '||| %s.new_colineation:\n%s' % (
                        method_name, new_colineation.listing())
            else:
                new_colineation = colineation_1
            new_line_part.dictionary[carrier] = new_colineation
        if trace_on:
            print '||| %s.new_line_part: \n%s' % (
                method_name, new_line_part.listing())
        new_line_part.reduce()
        return new_line_part

    def reduce(self):
        """Removes entries with empty colineations.
        """
        carriers_to_delete = []
        for carrier in self.dictionary:
            if self.dictionary[carrier].is_empty():
                carriers_to_delete.append(carrier)
        for carrier in carriers_to_delete:
            del self.dictionary[carrier]

    ###
if __name__ == '__main__':
    import doctest
    doctest.testfile('tests/line_partition_test.txt')
