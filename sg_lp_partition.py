#   sg_lp_partition.py

import sg_colabeling
import sg_labeled_point

class SGLPPartition(object):
    def __init__(self, lpoints):
        """Receives a (possibly unordered) list of labeled points:
            [SGLabeledPoint, ...]
        """
        try:
            if lpoints == []:
                self.dictionary = {}
            elif not self.are_lpoints(lpoints):
                raise ValueError()
            else:
                self.dictionary = self.make_dictionary(lpoints)
        except ValueError:
            print "You're trying to make a partition with non labeled-points"

    def are_lpoints(self, elements):
        value = True
        for element in elements:
            if element.__class__ != sg_labeled_point.SGLabeledPoint:
                value = False
                break
        return value

    def make_dictionary(self, lpoints):
        """Receives a list of labeled points:
            [SGLabeledPoint, ...], n >= 0
        Returns a dictionary of label-colabeling entries:
            {label: SGColabeling, ...}
        """
        dictionary = {}
        for lpoint in lpoints:
            label = lpoint.label
            if label in dictionary:
                colabeling = dictionary[label]
                colabeling.add(lpoint)
            else:
                colabeling = sg_colabeling.SGColabeling([lpoint])
                dictionary[label] = colabeling
        return dictionary

    @classmethod
    def new_empty(cls):
        lpoint_partition = SGLPPartition({})
        return lpoint_partition

    @classmethod
    def from_specs(cls, specs):
        """Receives a list of labeled point specs in the form:
            [(x, y, label), ...]
        """
        lpoints = []
        for spec in specs:
            x, y, label = spec
            lpoint = sg_labeled_point.SGLabeledPoint(x, y, label)
            lpoints.append(lpoint)
        partition = SGLPPartition(lpoints)
        return partition

        ### represent
    def __str__(self):
        """Returns an ordered string in the form:
            [(x, y, label), ...]
        """
        lpoint_specs = []
        for label in self.dictionary:
            colabeling = self.dictionary[label]
            lpoint_specs.extend(colabeling.lpoint_specs)
        entry_strings = []
        for lpoint_spec in sorted(lpoint_specs):
            lpoint_spec_string = self.get_lpoint_spec_string_from(lpoint_spec)
            entry_strings.append(lpoint_spec_string)
        entries_string = ', '.join(entry_strings)
        partition_string = '[%s]' % entries_string
        return partition_string

    def get_lpoint_spec_string_from(self, lpoint_spec):
        """Receives labeled point spec:
            (x, y, label)
        Returns a string in the form:
            (<x>, <y>, <label>)
        """
        lpoint_spec_string = '(%s, %s, %s)' % lpoint_spec
        return lpoint_spec_string

    def listing(self):
        """Returns an ordered, formatted, multi-line string in the form:
            label:
                (x, y)
                ...
            ...
        """
        if self.is_empty():
            partition_listing = '<empty lp_partition>'
        else:
            entry_listings = []
            for label in sorted(self.dictionary):
                colabeling = self.dictionary[label]
                indent_level = 1
                colabeling_listing = colabeling.listing(indent_level)
                entry_listing = '%s:\n%s' % (
                    label, colabeling_listing)
                entry_listings.append(entry_listing)
            partition_listing = '\n'.join(entry_listings)
        return partition_listing

        ### compare
    def __eq__(self, other):
        return self.dictionary == other.dictionary

    def __ne__(self, other):
        return self.dictionary != other.dictionary
        
    def is_empty(self):
        return self.dictionary == {}

    def is_a_sub_partition_of(self, other):
        self_label_set = set(self.dictionary.keys())
        other_label_set = set(other.dictionary.keys())
        if not self_label_set.issubset(other_label_set):
            return False
        else:
            return self.colabelings_are_sub_colabelings_in(other)

    def colabelings_are_sub_colabelings_in(self, other):
        """Receives a labeled point partition with the same labels
            SGLPPartition
        Returns whether each colabeling is a subcolabeling in the other 
        partition
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

        ###
if __name__ == '__main__':
    import doctest
    doctest.testfile('tests/sg_lp_partition_test.txt')
