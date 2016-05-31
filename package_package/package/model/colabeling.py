#   colabeling.py

import copy
import labeled_point
import numpy as np
import point

##  This may be unnecessary. Maybe we can use a set in the lpoint partition
##  And why does it have to be empty?

class Colabeling(object):
    """Contains a non-empty set of labeled points with the same label
    """
    ### construct
    def __init__(self, lpoints_in):
        """Receives:
            lpoints_in      [LabeledPoint] or set(LabeledPoint), label = k, 
                            n >= 0. A non-empty list or set of labeled points 
                            with the same label
        Mutable
        """
        method_name = '__init__'
        try:
            if not (
                (   type(lpoints_in) == list or
                    type(lpoints_in) == set) and
                self._contains_only_lpoints(lpoints_in)
            ):
                raise TypeError
            elif (
                len(lpoints_in) >= 1 and 
                not self._are_colabeled(lpoints_in)
            ):
                raise ValueError
        except TypeError:
            message = 'The argument must be a list or set of labeled points'
            self._print_error_message(method_name, message)
        except ValueError:
            message = 'The labeled points must have the same label'
            self._print_error_message(method_name, message)
        else:
            if type(lpoints_in) == set:
                self.lpoints = lpoints_in
            else:
                self.lpoints = set(lpoints_in)

    @classmethod
    def _contains_only_lpoints(cls, elements_in):
        """Receives:
            elements_in     [element] or set(element). A non-empty list or 
                            set of elements
        Returns:
            value           boolean. True if all elements are LabeledPoint 
                            objects. False otherwise
        """
        value = True
        if elements_in == []:
            value = False
        else:
            for element in elements_in:
                if not type(element) == labeled_point.LabeledPoint:
                    value = False
                    break
        return value

    @classmethod
    def _are_colabeled(cls, lpoints_in):
        """Receives: 
            lpoints_in      [LabeledPoint] or set(LabeledPoint). A non-empty 
                            list or set of labeled points
        Returns:
            value           boolean. True, if the labeled points all have the 
                            same label
        """
        lpoints_copy = copy.copy(lpoints_in)
        arbitrary_lpoint = lpoints_copy.pop()
        label = arbitrary_lpoint.label
        for lpoint in lpoints_in:
            if label != lpoint.label:
                return False
        return True

    @classmethod
    def from_lpoint_specs_list(cls, lpoint_specs_list):
        """Receives a list of lpoint specs:
            lpoint_specs_list
                            [lpoint_spec]. A non-empty list of labeled point 
                            specs (x, y, z, label):
                x, y, z     num
                label       str
        Returns:
            new_colabeling  Colabeling
        """
        method_name = 'from_lpoint_specs_list'
        try:
            if not type(lpoint_specs_list) == list:
                raise TypeError
            elif not labeled_point.LabeledPoint.are_lpoint_specs(
                lpoint_specs_list
            ):
                raise TypeError
        except TypeError:
            message = 'Not a list of labeled point specs'
            cls._print_error_message(method_name, message)
        else:
            new_lpoints = []
            for spec in lpoint_specs_list:
                x, y, z, label = spec
                p = point.Point(x, y, z)
                new_lpoint = labeled_point.LabeledPoint(p, label)
                new_lpoints.append(new_lpoint)
            new_colabeling = Colabeling(new_lpoints)
            return new_colabeling

    @classmethod
    def _is_number(cls, element):
        value = (
            element.__class__ == int or
            element.__class__ == float)
        return value

    @classmethod
    def _is_label(cls, element):
        value = element.__class__ == str 
        return value

    ### represent
    def __str__(self):
        """Returns:
            string          str. In the form '[<spec>, ...]'; <spec> is in 
                            the form '(<x>, <y>, <z>, <label>)'
        """
        spec_strings = []
        for lpoint in sorted(self.lpoints):
            spec_strings.append(str(lpoint.spec))
        specs_string = ', '.join(spec_strings)
        string = '{%s}' % specs_string
        return string

    def get_spec_string(self, spec):
        """Receives:
            spec            (x, y, z, label), (num, num, num, str)
        Returns:
            spec_string     str. '(<x>, <y>)'
        """
        x, y = spec[0:2]
        spec_string = '(%s, %s)' % (x, y)
        return spec_string

    def points_listing(self, decimal_places=0, indent_level=0):
        """Receives:
            decimal_places  num
            indent_level    num
        Returns: 
            string          str. Ordered, formatted, multi-line, in the form:
                            '(0, 0, 0)\n...'
        """
        method_name = 'points_listing'
        try:
            if not (
                self._is_a_number(decimal_places) and
                self._is_a_number(indent_level)
            ):
                raise TypeError
        except TypeError:
            message = 'The arguments must be integers'
            self._print_error_message(method_name, message)
        else:
            indent_increment = 4
            if indent_level < 0:
                indent_level = 0
            indent_string = ' ' * int(indent_level) * indent_increment
            point_listings = []
            for lpoint in sorted(self.lpoints):
                point_listing = lpoint.p.listing(decimal_places)
                point_listings.append(indent_string + point_listing)
            string = '\n'.join(point_listings)
            return string

    def _is_a_number(self, item):
        """Receives:
            item            any type
        Returns:
            value           boolean
        """
        value = (
            type(item) == int or
            type(item) == float or
            type(item) == np.int64 or
            type(item) == 64)
        return value

    ### get
    def get_lpoint_specs(self):
        """Returns: 
            specs           [spec]. A list of labeled point specs in the form 
                            [(x, y, z, label)]:
                x, y, z     num
                label       str
        """
        specs = []
        for lpoint in self.lpoints:
            spec = lpoint.spec
            specs.append(spec)
        return specs

    ### compare
    def __eq__(self, other):
        value = (self.lpoints == other.lpoints)
        return value

    def __ne__(self, other):
        value = (self.lpoints != other.lpoints)
        return value

    def __hash__(self):
        """Returns:
            value           int
        """
        lpoint_hash_list = []
        for lpoint in sorted(self.lpoints):
            lpoint_hash_list.append(hash(lpoint))
        lpoint_hash_tuple = tuple(lpoint_hash_list)
        value = hash(lpoint_hash_tuple)
        return value

    def is_a_subcolabeling_of(self, other):
        """Receives:
            other           Colabeling
        Returns:
            value           boolean. True if every lpoint in self is an 
                            lpoint in other
        """
        value = self.lpoints.issubset(other.lpoints)
        return value

    ### operate
    def union(self, other):
        """Receives:
            other           Colabeling. Has the same label as self
        Returns:
            cl_union        Colabeling. Has lpoints equal to self.lpoints | 
                            other.lpoints
        """
        lpoints_union = self.lpoints | other.lpoints
        new_colabeling = Colabeling(lpoints_union)
        return new_colabeling

    def difference(self, other):
        """Receives:
            other           Colabeling. Has the same label as self
        Returns:
            cl_diff         Colabeling. Has lpoints equal to self.lpoints - 
                            other.lpoints
        """
        lpoints_diff = self.lpoints - other.lpoints
        cl_diff = Colabeling(lpoints_diff)
        return cl_diff

    def add(self, lpoint):
        """Receives a labeled point: 
            LabeledPoint
        Adds the labeled point spec to the set
        """
        self.specs_set.add(lpoint.spec)

    def union(self, other):                 #   refactor as __add__ or __or__?
        """Receives:
            other           Colabeling
        Returns:
            new_colabeling  Colabeling. The colabeling of the union of 
                            self.lpoints and other.lpoints
        """
        new_lpoints = self.lpoints.union(other.lpoints)
        new_colabeling = Colabeling(new_lpoints)
        return new_colabeling
        # new_colabeling = copy.copy(self)
        # new_lpoint_specs = new_colabeling.specs_set
        # new_colabeling.specs_set = new_lpoint_specs | other.specs_set
        # return new_colabeling

    ### other
    @classmethod
    def _print_error_message(cls, method_name, message):
        print '%s.%s:\n    %s' % (cls.__name__, method_name, message)

if __name__ == '__main__':
    import doctest
    doctest.testfile('tests/colabeling_test.txt')
