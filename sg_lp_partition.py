#   sg_lp_partition.py

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
        Returns a dictionary partitioned by label:
            {label: [SGLabeledPoint, ...]}
        """
        dictionary = {}
        for lpoint in lpoints:
            label = lpoint.label
            if label in dictionary:
                colabeling = dictionary[label]
                colabeling.append(lpoint)
            else:
                colabeling = [lpoint]
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
        lpoints = []
        for label in self.dictionary:
            colabeling = self.dictionary[label]
            lpoints.extend(colabeling)
        entry_strings = []
        for lpoint in sorted(lpoints):
            entry_strings.append(lpoint.__str__())
        entries_string = ', '.join(entry_strings)
        partition_string = '[%s]' % entries_string
        return partition_string

    def get_point_specs_from(self, lpoints_subset):             # no usage
        """Receives a set of labeled points:
            set(SGLabeledPoint, ...)
        Returns an ordered string of point specs:
            '(x, y), ...'
        """
        point_spec_strings = []
        for lpoint in sorted(lpoints_subset):
            point_spec_string = lpoint.point.__str__()
            point_spec_strings.append(point_spec_string)
        string = ', '.join(point_spec_strings)
        return string

    def listing(self):
        """Returns an ordered, formatted, multi-line string in the form:
            label:
                (x, y)
                ...
            ...
        """
        if self.is_empty():
            string = '<empty lp_partition>'
        else:
            entry_listings = []
            for label in sorted(self.dictionary):
                lpoints_subset = self.dictionary[label]
                indent_level = 1
                lpoints_subset_listing = self.get_lpoints_subset_listing(
                    lpoints_subset, indent_level)
                entry_listing = '%s:\n%s' % (
                    label, lpoints_subset_listing)
                entry_listings.append(entry_listing)
            string = '\n'.join(entry_listings)
        return string

    def get_lpoints_subset_listing(self, lpoints_subset, indent_level):
        """Receives a set of (identically) labeled points and an indent level:
            set(SGLabeledPoint, ...), n >= 0
            int >= 0
        Returns an indented ordered string of labeled point listings:
            <indent>(x, y)
            ...
        """
        lpoints_subset_listing = self.get_lpoint_listings(
            lpoints_subset, indent_level)
        string = '\n'.join(lpoints_subset_listing)
        return string

    def get_lpoint_listings(self, lpoints_subset, indent_level):
        """Returns an ordered list of listings in the form:
            [<indent_string>(x, y), ...]
        """
        lpoint_listings = []
        for lpoint in sorted(lpoints_subset):
            indent_string = self.get_indent_string(indent_level)
            lpoint_listing = lpoint.point.listing()
            indented_lpoint_listing = '%s%s' % (indent_string, lpoint_listing)
            lpoint_listings.append(indented_lpoint_listing)
        return lpoint_listings

    def get_indent_string(self, indent_level):
        indent_increment = 4
        if indent_level < 0:
            indent_level = 0
        indent = ' ' * indent_level * indent_increment
        return indent

        ### compare
    def __eq__(self, other):
        return self.dictionary == other.dictionary

    def colabelings_are_equal(self, self_colabeling, other_colabeling):
        """Receives two colabelings:
            set([LPoint, ...])
            set([LPoint, ...])
        """
        for lpoint in self_colabeling:
            if not other_colabeling.__contains__(lpoint):
                return False
        return True

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
                if not self.colabeling_is_a_subcolabeling_of(
                    self_colabeling, other_colabeling
                ):
                # if not self_colabeling.is_a_subcolabeling_of(other_colabeling):
                    return False
        return True

    def colabeling_is_a_subcolabeling_of(
        self, self_colabeling, other_colabeling
    ):
        """Receives two non-empty colabelings:
            [SGLabeledPoint, ...]
            [SGLabeledPoint, ...]
        Returns whether self_colabeling is a subcolabeling of other_colabeling
        """
        #   Should be a method of SGColabeling
        #   Colabeling should have no duplicates?
        for lpoint in self_colabeling:
            if not lpoint in other_colabeling:
                return False
        return True

        ###
if __name__ == '__main__':
    import doctest
    doctest.testfile('tests/sg_lp_partition_test.txt')
