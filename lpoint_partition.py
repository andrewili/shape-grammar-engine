#   lpoint_partition.py

import colabeling
import labeled_point
import lpoint_partition

class LPointPartition(object):
    def __init__(self, lpoints):
        """Receives a (possibly unordered) list of labeled points:
            [LabeledPoint, ...], n >= 0
        """
        method_name = '__init__()'
        try:
            if not (
                lpoints.__class__ == list and
                self._are_lpoints(lpoints)
            ):
                raise TypeError
            # if not lpoints.__class__ == list:
            #     raise TypeError
            # elif not self._are_lpoints(lpoints):
            #     raise TypeError
        except TypeError:
            message = 'Must be a list of labeled points'
            self.__class__._print_error_message(method_name, message)
        else:
            self.dictionary = self._make_dictionary(lpoints)

    def _are_lpoints(self, elements):
        value = True
        for element in elements:
            if element.__class__ != labeled_point.LabeledPoint:
                value = False
                break
        return value

    def _make_dictionary(self, lpoints):
        """Receives a list of labeled points:
            [LabeledPoint, ...], n >= 0
        Returns a dictionary of label-colabeling entries:
            {str: Colabeling, ...}
        """
        dictionary = {}
        for lpoint in lpoints:
            label = lpoint.label
            if label in dictionary:
                new_colabeling = dictionary[label]
                new_colabeling.add(lpoint)
            else:
                new_colabeling = colabeling.Colabeling([lpoint])
                dictionary[label] = new_colabeling
        return dictionary

    @classmethod
    def new_empty(cls):
        new_lpoint_part = LPointPartition([])
        return new_lpoint_part

    @classmethod
    def from_specs(cls, specs):
        """Receives a list of labeled point specs in the form:
            [(x, y, label), ...]
        """
        method_name = 'from_specs()'
        try:
            if not (
                specs.__class__ == list and
                labeled_point.LabeledPoint.are_lpoint_specs(specs)
            ):
                raise TypeError
        except TypeError:
            message = 'Must be a list of labeled point specs'
            cls._print_error_message(method_name, message)
        else:
            lpoints = []
            for spec in specs:
                x, y, label = spec
                lpoint = labeled_point.LabeledPoint(x, y, label)
                lpoints.append(lpoint)
            new_lpoint_part = LPointPartition(lpoints)
            return new_lpoint_part

        ### represent
    def __str__(self):
        """Returns an ordered string in the form:
            [(x, y, label), ...]
        """
        lpoint_specs = []
        for label_i in self.dictionary:
            colabeling_i = self.dictionary[label_i]
            lpoint_specs.extend(colabeling_i.specs_set)
        entry_strings = []
        for lpoint_spec in sorted(lpoint_specs):
            lpoint_spec_string = self._get_lpoint_spec_string_from(
                lpoint_spec)
            entry_strings.append(lpoint_spec_string)
        entries_string = ', '.join(entry_strings)
        lpoint_part_string = '[%s]' % entries_string
        return lpoint_part_string

    def _get_lpoint_spec_string_from(self, lpoint_spec):
        """Receives labeled point spec:
            (x, y, label)
        Returns a string in the form:
            (<x>, <y>, <label>)
        """
        lpoint_spec_string = '(%s, %s, %s)' % lpoint_spec
        return lpoint_spec_string

    def listing(self, decimal_places=0):
        """Returns a formatted, multi-line string in the form:
            label:
                (x, y)
                ...
            ...
        """
        if self._is_empty():
            lpoint_part_listing = '<no labeled points>'
        else:
            entry_listings = []
            for label_i in sorted(self.dictionary):
                colabeling_i = self.dictionary[label_i]
                indent_level = 1
                colabeling_listing_i = colabeling_i.listing(
                    decimal_places, indent_level)
                entry_listing_i = '%s:\n%s' % (
                    label_i, colabeling_listing_i)
                entry_listings.append(entry_listing_i)
            lpoint_part_listing = '\n'.join(entry_listings)
        return lpoint_part_listing

        ### get
    def specs(self):
        """Returns an ordered list of specs:
            [(x, y, label), ...]
        """
        specs = []
        for label_i in self.dictionary:
            colabeling_i = self.dictionary[label_i]
            specs_i = colabeling_i.get_lpoint_specs()
            specs.extend(specs_i)
        return sorted(specs)

        ### compare
    def __eq__(self, other):
        return self.dictionary == other.dictionary

    def __ne__(self, other):
        return self.dictionary != other.dictionary
        
    def _is_empty(self):
        return self.dictionary == {}

    def is_a_sub_lpoint_partition_of(self, other):
        self_label_set = set(self.dictionary.keys())
        other_label_set = set(other.dictionary.keys())
        if not self_label_set.issubset(other_label_set):
            return False
        else:
            return self._colabelings_are_sub_colabelings_in(other)

    def _colabelings_are_sub_colabelings_in(self, other):
        """Receives:
            LPointPartition
        Returns whether each colabeling is a subcolabeling in the other 
        partition:
            boolean
        """
        for label in self.dictionary:
            if label not in other.dictionary:
                return False
            else:
                self_colabeling = self.dictionary[label]
                other_colabeling = other.dictionary[label]
                if not self_colabeling.is_a_subcolabeling_of(other_colabeling):
                    return False
        return True

    ### operate

    def __add__(self, other):
        """Receives:
            LPointPartition
        Returns the sum of the two labeled point partitions:
            LPointPartition
        """
        new_dictionary = self.dictionary.copy()
        for label in other.dictionary:
            other_colabeling = other.dictionary[label]
            if label in new_dictionary:
                new_colabeling = new_dictionary[label]
                new_dictionary[label] = new_colabeling.union(other_colabeling)
            else:
                new_dictionary[label] = other_colabeling
        new_lpoint_part = LPointPartition([])
        new_lpoint_part.dictionary = new_dictionary
        return new_lpoint_part

    def __sub__(self, other):
        """Receives:
            LPointPartition
        Returns the difference self - other:
            LPointPartition
        """
        if self._is_empty():
            new_lpoint_part = LPointPartition.new_empty()
        elif other._is_empty():
            new_lpoint_part = self
        else:
            new_lpoint_specs = []
            for label in self.dictionary:
                self_colabeling = self.dictionary[label] 
                if label in other.dictionary:               #   copy?
                    other_colabeling = other.dictionary[label]
                    new_colabeling = self_colabeling - other_colabeling
                else:
                    new_colabeling = self_colabeling
                new_lpoint_spec_set = new_colabeling.specs_set
                for spec in new_lpoint_spec_set:
                    new_lpoint_specs.append(spec)
            new_lpoint_part = LPointPartition.from_specs(new_lpoint_specs)
        return new_lpoint_part

    @classmethod
    def _print_error_message(cls, method_name, message):
        print '%s.%s: %s' % (cls.__name__, method_name, message)

        ###
if __name__ == '__main__':
    import doctest
    doctest.testfile('tests/lpoint_partition_test.txt')
