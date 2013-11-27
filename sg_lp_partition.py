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
            {string: set(SGLabeledPoint, ...), ...}
        """
        dictionary = {}
        for lpoint in lpoints:
            if lpoint.label in dictionary:
                lpoints_subset = dictionary[lpoint.label]
                lpoints_subset.add(lpoint)
            else:
                lpoints_subset = set([lpoint])
                dictionary[lpoint.label] = lpoints_subset
        return dictionary

        ### represent
    def __str__(self):
        """Returns an ordered string in the form:
            {<label>: [(<x>, <y>), ...], ...}
        """
        entry_strings = []
        for label in sorted(self.dictionary):
            point_specs = self.get_point_specs_from(self.dictionary[label])
            entry_string = '%s: [%s]' % (label, point_specs)
            entry_strings.append(entry_string)
        entries_string = ', '.join(entry_strings)
        string = '{%s}' % entries_string
        return string

    def get_point_specs_from(self, lpoints_subset):
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
            <label>:
                (<x>, <y>)
                ...
            ...
        """
        if self.dictionary == {}:
            dictionary_listing = '<empty lp_partition>'
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
                # entry_listing = self.get_carrier_listing(label)
                # entry_listings.append(entry_listing)
                # lpoints_subset = self.dictionary[label]
                # lpoints_subset_listing_indent_level = 1
                # entry_listing = self.get_lpoints_subset_listing(
                #     lpoints_subset, lpoints_subset_listing_indent_level)
                # entry_listings.append(entry_listing)
            dictionary_listing = '\n'.join(entry_listings)
        return dictionary_listing

    def get_lpoints_subset_listing(self, lpoints_subset, indent_level):
        """Receives a set of (identically) labeled points and an indent level:
            set(SGLabeledPoint, ...)
            int >= 0
        Returns an indented ordered string of labeled point listings:
            '<indent>(<x>, <y>), ...'
        """
        indent_string = self.get_indent_string(indent_level)
        lpoint_listings = self.get_lpoint_listings(lpoints_subset)
        string = '%s%s' % (indent_string, lpoint_listings)
        return string

    def get_indent_string(self, indent_level):
        indent_increment = 4
        if indent_level < 0:
            indent_level = 0
        indent_string = ' ' * indent_level * indent_increment
        return indent_string

    def get_lpoint_listings(self, lpoints_subset):
        lpoint_listings = []
        for lpoint in sorted(lpoints_subset):
            lpoint_listings.append(lpoint.point.listing())
        return lpoint_listings

        ###
if __name__ == '__main__':
    import doctest
    doctest.testfile('tests/sg_lp_partition_test.txt')