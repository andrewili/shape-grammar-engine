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
        """Receives:
            dictionary      dict. Of carrier-colineation entries
                            {carrier: Colineation, ...}
                carrier     (unit_vector, intercept)
                unit_vector Vector
                intercept   Point
        Returns:
            line_part       LinePartition. Has dictionary
        """
        line_part = LinePartition([])
        line_part.dictionary = dictionary
        return line_part

    ### represent
    def __str__(self):
        """Returns:
            string          str. Ordered by carrier and line. In the form 
                            {carrier: colineation}, where:
                carrier     (unit_vector, intercept)
                unit_vector Vector. In the form [<x> <y> <z>]
                intercept   Point. In the form (<x>, <y>, <z>)
                colineation Colineation. In the form [line, ...]
                line        Line. In the form (<x>, <y>, <z>)
        """
        item_strs = []
        items = self.dictionary.items()
        for item in sorted(items):
            carrier, colin = item
            uv, int_ = carrier
            carrier_str = '(%s, %s)' % (str(uv), str(int_))
            colin_str = str(colin)
            item_str = '%s: %s' % (carrier_str, colin_str)
            item_strs.append(item_str)
        items_str = ', '.join(item_strs)
        string = '{%s}' % items_str
        return string

    def listing(self, decimal_places=0):
        """Returns an ordered, formatted, multi-line string in the form:
                            (<unit_vector>, <intercept>)
                                <line>
                                ...
                            ...
                unit_vector Vector
                intercept   Point
                line        Line
        """
        n = decimal_places
        item_strs = []
        items = sorted(self.dictionary.items())
        for item in items:
            carrier, colin = item
            uv, intercept = carrier
            carrier_str = '(%s, %s)' % (uv.listing(n), intercept.listing(n))
            colines = colin.lines
            indented_coline_strs = []
            indentation = '    '
            for line_i in colines:
                indented_coline_str = (
                    '%s%s' % (indentation, line_i.listing(n)))
                indented_coline_strs.append(indented_coline_str)
            colin_str = '\n'.join(indented_coline_strs)
            item_str = '%s\n%s' % (carrier_str, colin_str)
            item_strs.append(item_str)
        string = '\n'.join(item_strs)
        return string

    ### get
    # def specs(self):                          ##  suspended
        # """Returns:
        #     specs           {carrier_spec: colin_spec, ...}. Ordered by 
        #                     carrier and by line
        #         carrier_spec
        #                     (uv_spec, int_spec)
        #         uv_spec     [num num num]
        #         int_spec    (num, num, num)
        #         colin_spec  [line_spec, ...]
        #         line_spec   (point_spec, point_spec)
        #         point_spec  (num, num, num)
        # """
        # item_specs = []
        # carrier = 
        # for carrier in sorted(carriers):
        #     item_spec = 
        #     item_specs.append(item_spec)
        # specs = '\n'.join(item_specs)
        # return specs

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
        """Receives:
            other           LinePartition
        Returns:
            value           boolean. True if every colineation in self is a 
                            subcolineation in other. False otherwise
        """
        value = True
        self_keyset = set(self.dictionary.keys())
        other_keyset = set(other.dictionary.keys())
        if not self_keyset.issubset(other_keyset):
            value = False
        else:
            for carrier in self.dictionary:
                self_colin = self.dictionary[carrier]
                other_colin = other.dictionary[carrier]
                if not self_colin.is_a_subcolineation_of(other_colin):
                    value = False
                    break
        return value

    ### operations
    def __add__(self, other):
        """Receives:
            other           LinePartition
        Returns:
            sum_part        LinePartition. A line partition of the 
                            colineation sums of self and other
        """
        sum_dict = self.dictionary.copy()
        for carrier in other.dictionary:
            if carrier in sum_dict:
                self_colin = sum_dict[carrier]
                other_colin = other.dictionary[carrier]
                sum_colin = self_colin + other_colin
                sum_dict[carrier] = sum_colin
            else:
                sum_dict[carrier] = other.dictionary[carrier]
        sum_part = LinePartition.from_dictionary(sum_dict)
        return sum_part

    def __sub__(self, other):
        """Receives:
            other           LinePartition
        Returns:
            diff_part       LinePartition. The line partition such that for 
                            each carrier the corresponding colineation is the 
                            difference self.colineation - other.colineation. 
                            If a difference is the empty colineation, the 
                            entry is removed from the partition.
        """
        trace_on = False
        if trace_on:
            method_name = 'LinePartition.__sub__'
            print 'self:\n%s' % self.listing()
            print 'other:\n%s' % other.listing()
        diff_part = LinePartition([])
        self_dict = self.dictionary
        if trace_on:
            print '||| %s' % method_name
            print 'diff_part: %s' % diff_part
            print 'self_dict'
            for carrier in self_dict:
                print carrier
                print '%s' % self_dict[carrier].listing(1)
        for carrier in self_dict:
            self_colin = self_dict[carrier]
            other_dict = other.dictionary
            if carrier in other_dict:
                other_colin = copy.copy(other_dict[carrier])
                diff_colin = self_colin - other_colin
            else:
                diff_colin = self_colin
            diff_part.dictionary[carrier] = diff_colin
        if trace_on:
            print '||| %s' % method_name
            print 'diff_part: \n%s' % diff_part.listing()
        diff_part._reduce()
        return diff_part

    def _reduce(self):
        """Removes entries with empty colineations
        """
        trace_on = False
        carriers_to_delete = []
        for carrier in self.dictionary:
            if self.dictionary[carrier].is_empty():
                carriers_to_delete.append(carrier)
        for carrier in carriers_to_delete:
            del self.dictionary[carrier]
        if trace_on == True:
            print '||| LinePartition._reduce():\n%s' % self.listing()

    @classmethod
    def _print_error_message(cls, method_name, message):
        print '%s.%s:\n    %s' % (cls.__name__, method_name, message)

    ###
if __name__ == '__main__':
    import doctest
    doctest.testfile('tests/line_partition_test.txt')
