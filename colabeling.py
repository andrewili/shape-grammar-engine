#   sg_colabeling.py

import copy

class SGColabeling(object):
    """Contains a non-empty set of colabeled points:
        set([SGLabeledPoint, ...]), n >= 1
    """
    ### construct
    def __init__(self, lpoints_in):
        """Receives a non-empty unsorted list of colabeled points:
            [SGLabeledPoint, ...], n >= 1
        """
        try:
            if (len(lpoints_in) == 0 or
                not self.colabeled(lpoints_in)
            ):
                raise ValueError()
            else:
                self.lpoint_specs = self.make_lpoint_specs(lpoints_in)
        except ValueError:
            print '%s %s' % (
                "You're trying to make a colabeling",
                "with non-colabeled points or no points")

    def colabeled(self, lpoints_in):
        """Receives a non-empty list of labeled points:
            [SGLabeledPoint, ...], n >= 1
        Returns whether the labeled points all have the same label
        """
        label = lpoints_in[0].label
        for lpoint in lpoints_in:
            if label != lpoint.label:
                return False
        return True

    def make_lpoint_specs(self, lpoints_in):
        """Receives a list of labeled points:
            [SGLabeledPoint, ...]
        Returns a set of labeled point specs:
            set([(x, y, label), ...])
        """
        #   How to implement?
        #   1.  As a set of SGLPoint objects. Problem: a set does not 
        #       use an element's __eq__ method
        #   2.  As a list of lpoints. Have to implement equivalent methods to
        #       set methods
        #   3.  As a set of lpoint specs. Have to unpack and repack 
        #       lpoints. Try this
        lpoint_specs = set()
        for lpoint in lpoints_in:
            lpoint_specs.add(lpoint.spec)
        return lpoint_specs
        # self.lpoint_specs = set(lpoint_specs)

    ### represent
    def __str__(self):
        """Returns the string of the ordered list of colabeled points in the 
        form:
            [(x, y, label), ...]
        """
        spec_strings = []
        for spec in sorted(self.lpoint_specs):
            spec_string = self.get_spec_string(spec)
            spec_strings.append(spec_string)
        specs_string = ', '.join(spec_strings)
        colabeling_string = '[%s]' % specs_string
        return colabeling_string

    def get_spec_string(self, spec):
        """Receives a labeled point spec:
            (x, y, label)
        Returns a string:
            '(<x>, <y>)'
        """
        x, y = spec[0:2]
        spec_string = '(%s, %s)' % (x, y)
        return spec_string

    def listing(self, indent_level=0):
        """Returns an ordered, formatted, multi-line string in the form:
            label:
                (x, y)
                ...
        """
        indent_increment = 4
        if indent_level < 0:
            indent_level = 0
        indent_string = ' ' * indent_level * indent_increment
        lpoint_listings = []
        for lpoint_spec in sorted(self.lpoint_specs):
            lpoint_listing = self.get_lpoint_listing(lpoint_spec)
            lpoint_listings.append(indent_string + lpoint_listing)
        colabeling_listing = '\n'.join(lpoint_listings)
        return colabeling_listing

    def get_lpoint_listing(self, lpoint_spec):
        """Receives a labeled point spec:
            (x, y, label)
        Returns a string in the form:
            '(<x>, <y>)'
        """
        x, y = lpoint_spec[0:2]
        lpoint_listing = '(%3.1f, %3.1f)' % (x, y)
        return lpoint_listing

    ### compare
    def __eq__(self, other):
        return self.lpoint_specs == other.lpoint_specs

    def __ne__(self, other):
        return self.lpoint_specs != other.lpoint_specs

    def is_a_subcolabeling_of(self, other):
        """Receives a colabeling:
            SGColabeling
        """
        return self.lpoint_specs.issubset(other.lpoint_specs)

    ### operate
    def add(self, lpoint):
        """Receives a labeled point: 
            SGLabeledPoint
        Adds the labeled point spec to the set
        """
        self.lpoint_specs.add(lpoint.spec)

    def union(self, other):
        """Receives a colabeling:
            SGColabeling
        Returns the union of the two colabelings:
            SGColabeling
        """
        new_colabeling = copy.copy(self)
        new_lpoint_specs = new_colabeling.lpoint_specs
        new_colabeling.lpoint_specs = new_lpoint_specs | other.lpoint_specs
        return new_colabeling

if __name__ == '__main__':
    import doctest
    doctest.testfile('tests/colabeling_test.txt')
