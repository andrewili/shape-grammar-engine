#   colabeling.py

import copy
import labeled_point

class Colabeling(object):
    """Contains a set of colabeled point specs:
        set([(x, y, label), ...]), n >= 0
    """
    ### construct
    def __init__(self, lpoints_in):
        """Receives an unsorted list of colabeled points:
            [LabeledPoint, ...], n >= 0
        """
        try:
            if (len(lpoints_in) >= 1 and 
                (   not self.are_lpoints(lpoints_in) or
                    not self.colabeled(lpoints_in))
            ):
                raise ValueError()
            else:
                self.lpoint_specs = self.make_lpoint_specs(lpoints_in)          #   rename as lpoint_spec_set?
        except ValueError:
            print '%s %s' % (
                "You're trying to make a colabeling",
                "with non-colabeled points")

    def are_lpoints(self, elements):
        """Receives a non-empty list of elements:
            [element, ...], n >= 1
        Returns whether all elements are LabeledPoint objects
        """
        for element in elements:
            if element.__class__ != labeled_point.LabeledPoint:
                return False
        return True

    def colabeled(self, lpoints_in):
        """Receives a non-empty list of labeled points:
            [LabeledPoint, ...], n >= 1
        Returns whether the labeled points all have the same label
        """
        label = lpoints_in[0].label
        for lpoint in lpoints_in:
            if label != lpoint.label:
                return False
        return True

    def make_lpoint_specs(self, lpoints_in):
        """Receives a list of labeled points:
            [LabeledPoint, ...]
        Returns a set of labeled point specs:
            set([(x, y, label), ...])
        """
        lpoint_specs = set()
        for lpoint in lpoints_in:
            lpoint_specs.add(lpoint.spec)
        return lpoint_specs

    @classmethod
    def from_lpoint_specs(cls, lpoint_specs_list):
        """Receives a list of lpoint specs:
            [(x, y, label), ...]
        """
        new_lpoints = []
        for spec in lpoint_specs_list:
            x, y, label = spec
            new_lpoint = labeled_point.LabeledPoint(x, y, label)
            new_lpoints.append(new_lpoint)
        new_colabeling = Colabeling(new_lpoints)
        return new_colabeling

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

    def listing(self, decimal_places=0, indent_level=0):
        """Receives 2 numbers
        Returns an ordered, formatted, multi-line string in the form:
            label:
                (x, y)
                ...
        """
        indent_increment = 4
        if indent_level < 0:
            indent_level = 0
        indent_string = ' ' * int(indent_level) * indent_increment
        lpoint_listings = []
        for lpoint_spec in sorted(self.lpoint_specs):
            lpoint_listing = self.get_lpoint_listing(
                lpoint_spec, decimal_places)
            lpoint_listings.append(indent_string + lpoint_listing)
        colabeling_listing = '\n'.join(lpoint_listings)
        return colabeling_listing

    def get_lpoint_listing(self, lpoint_spec, decimal_places=0):
        """Receives a labeled point spec:
            (x, y, label)
        Returns a string in the form:
            '(<x>, <y>)'
        """
        x, y = lpoint_spec[0:2]
        if decimal_places < 0:
            n = 0
        else:
            n = int(decimal_places)
        format = '%1.' + str(n) + 'f'
        x_formatted = format % x
        y_formatted = format % y
        lpoint_listing = '(%s, %s)' % (x_formatted, y_formatted)
        return lpoint_listing

    ### get
    def specs(self):
        """Returns a list of specs:
            [(x, y, label), ...]
        """
        specs = []
        for spec_i in self.lpoint_specs:
            specs.append(spec_i)
        return specs

    ### compare
    def __eq__(self, other):
        return self.lpoint_specs == other.lpoint_specs

    def __ne__(self, other):
        return self.lpoint_specs != other.lpoint_specs

    def is_a_subcolabeling_of(self, other):
        """Receives a colabeling:
            Colabeling
        """
        return self.lpoint_specs.issubset(other.lpoint_specs)

    ### operate
    # def __add__(self, other):                                                 #   implement?
    #     pass

    def __sub__(self, other):
        """Returns a colabeling with the set difference of lpoint_specs:
            Colabeling
        """
        new_lpoint_spec_set = self.lpoint_specs - other.lpoint_specs            #   messy: too much converting
        lpoints = []
        for spec in new_lpoint_spec_set:
            x, y, label = spec
            lpoint = labeled_point.LabeledPoint(x, y, label)
            lpoints.append(lpoint)
        new_colabeling = Colabeling(lpoints)
        return new_colabeling

    def add(self, lpoint):
        """Receives a labeled point: 
            LabeledPoint
        Adds the labeled point spec to the set
        """
        self.lpoint_specs.add(lpoint.spec)

    def union(self, other):
        """Receives a colabeling:
            Colabeling
        Returns the union of the two colabelings:
            Colabeling
        """
        new_colabeling = copy.copy(self)
        new_lpoint_specs = new_colabeling.lpoint_specs
        new_colabeling.lpoint_specs = new_lpoint_specs | other.lpoint_specs
        return new_colabeling

if __name__ == '__main__':
    import doctest
    doctest.testfile('tests/colabeling_test.txt')
