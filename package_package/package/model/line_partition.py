import colineation
import copy
import line

class LinePartition(object):                ##  rename MaximalColineations?
    
    ### construct
    def __init__(self, lines):
        """Receives:
            lines           [Line, ...]. A list of lines
        Has a dictionary of carrier : colineation entries
        """
        method_name = '__init__'
        try:
            if not (
                lines.__class__ == list and 
                (
                    lines == [] or
                    self._are_lines(lines))
            ):
                raise TypeError
        except TypeError:
            message = 'The argument must be a list of lines'
            self._print_error_message(method_name, message)
        else:
            self.dictionary = self._make_dictionary(lines)

    @classmethod
    def _are_lines(cls, lines):
        value = True
        for line_i in lines:
            if type(line_i) != line.Line:
                value = False
                break
        return value

    @classmethod
    def _make_dictionary(cls, lines):           ##  inst meth? cf lpt-part
        """Receives:
            lines           [Line, ...]. A non-empty list of lines
        Returns:
            dict_of_colineations
                            {carrier : colineation, ...}, a dictionary 
                            partitioned by carrier, where:
                carrier     (unit_vector, intercept)
                unit_vector Vector
                intercept   Point
                colineation Colineation
        """
        dict_of_colines = cls._make_dict_of_colines(lines)
        dict_of_colineations = cls._make_dict_of_colineations(dict_of_colines)
        return dict_of_colineations

    @classmethod
    def _make_dict_of_colines(cls, lines):
        """Receives:
            lines           [Line, ...]. A non-empty list of lines
        Returns:
            dict_of_colines {carrier : colines, ...}, where:
                carrier     (unit_vector, intercept)
                unit_vector Vector
                intercept   Point
                colines     [Line, ...]. A non-empty list of colinear lines
        """
        d = {}
        for l in lines:
            if l.carrier in d:
                colines = d[l.carrier]
                colines.append(l)
            else:
                colines = [l]
                d[l.carrier] = colines
        return d

    @classmethod
    def _make_dict_of_colineations(cls, dict_of_colines):
        """Receives:
            dict_of_colines {carrier : colines, ...}. A non-empty dictionary 
                            of colines, where:
                carrier     (unit_vector, intercept)
                unit_vector Vector
                intercept   Point
                colines     [Line, ...]. A non-empty list of colinear lines
        Converts the colines lists to colineations. Returns:
            new_dict        {carrier : colineation, ...}. A non-empty 
                            dictionary of colineations, where:
                carrier     as above
                colineation Colineation. With a non-empty ordered list of 
                            colinear lines
        """
        new_dict = {}
        for carrier in dict_of_colines:
            colines = dict_of_colines[carrier]
            new_colin = colineation.Colineation(colines)
            new_dict[carrier] = new_colin
        return new_dict

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

    def listing(self, decimal_places=0):                #   back to shape
        """Returns an oredered, formatted, multi-line string in the form:
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
                carrier_listing = self.get_carrier_listing(
                    carrier_i, decimal_places)
                string_lines.append(carrier_listing)
                colineation_i = self.dictionary[carrier_i]
                indent_level = 1                        #   move out of loop
                colineation_listing = colineation_i.listing(
                    decimal_places, indent_level)       #   create indentation here?
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

    def get_carrier_listing(self, carrier, decimal_places):
        bearing, intercept = carrier
        if decimal_places < 0:
            n = 0
        else:
            n = int(decimal_places)
        format = '%1.' + str(n) + 'f'
        x_formatted = format % bearing
        y_formatted = format % intercept
        string = '(%s, %s):' % (x_formatted, y_formatted)
        # string = '(%3.1f, %3.1f):' % (bearing, intercept)
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
        """Receives a line partition:                                           #!  empty colineations?
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
            print 'self:\n%s' % self.listing()
            print 'other:\n%s' % other.listing()
        new_line_part = LinePartition([])
        line_dict_1 = self.dictionary
        if trace_on:
            print '||| %s' % method_name
            print 'new_line_part: %s' % new_line_part
            print 'line_dict_1'
            for carrier in line_dict_1:
                print carrier
                print '%s' % line_dict_1[carrier].listing(1)
        for carrier in line_dict_1:
            colineation_1 = line_dict_1[carrier]
            line_dict_2 = other.dictionary
            if carrier in line_dict_2:
                colineation_2 = copy.copy(line_dict_2[carrier])
                new_colineation = colineation_1 - colineation_2
            else:
                new_colineation = colineation_1
            new_line_part.dictionary[carrier] = new_colineation
        if trace_on:
            print '||| %s' % method_name
            print 'new_line_part: \n%s' % new_line_part.listing()
        new_line_part.reduce()
        return new_line_part

    def reduce(self):
        """Removes entries with empty colineations.
        """
        trace_on = False
        carriers_to_delete = []
        for carrier in self.dictionary:
            if self.dictionary[carrier].is_empty():
                carriers_to_delete.append(carrier)
        for carrier in carriers_to_delete:
            del self.dictionary[carrier]
        if trace_on == True:
            print '||| LinePartition.reduce():\n%s' % self.listing()

    @classmethod
    def _print_error_message(cls, method_name, message):
        print '%s.%s:\n    %s' % (cls.__name__, method_name, message)

    ###
if __name__ == '__main__':
    import doctest
    doctest.testfile('tests/line_partition_test.txt')
