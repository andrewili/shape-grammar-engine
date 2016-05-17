import colabeling
import labeled_point
import lpoint_partition

class LPointPartition(object):
    def __init__(self, lpoints):
        """Receives:
            lpoints         [LabeledPoint, ...]. A list of labeled points, 
                            possibly duplicated or empty
        Mutable?
        """
        method_name = '__init__'
        try:
            if not (
                type(lpoints) == list and
                self._are_lpoints(lpoints)
            ):
                raise TypeError
        except TypeError:
            message = 'The argument must be a list of labeled points'
            self._print_error_message(method_name, message)
        else:
            self.dictionary = self._make_dictionary(lpoints)

    @classmethod
    def _are_lpoints(cls, items):
        """Receives:
            items           [item, ...]. A list of items, possibly duplicated 
                            or empty
        Returns:
            value           boolean. True if every item is a labeled point or 
                            if the list is empty. False otherwise
        """
        value = True
        for item in items:
            if type(item) != labeled_point.LabeledPoint:
                value = False
                break
        return value

    @classmethod
    def _make_dictionary(cls, lpoints):
        """Receives:
            lpoints         [LabeledPoint, ...]. A possibly empty list of labeled 
                            points. Guaranteed by the calling function
        Creates a partition of points by label. Returns:
            dictionary      dict. Label-point-set entries in the form:
                            {label: point_set, ...}, where:
                label       str
                point_set   set([Point, ...]). A set of (unlabeled) points
        """
        dictionary = {}
        for lpoint in lpoints:
            label = lpoint.label
            if label in dictionary:
                points_set = dictionary[label]
                points_set.add(lpoint.p)
            else:
                dictionary[label] = set([lpoint.p])
        return dictionary

    @classmethod
    def new_empty(cls):
        new_lpp = LPointPartition([])
        return new_lpp

    @classmethod
    def from_specs(cls, specs):
        """Receives:
            specs           [lp_spec, ...], where:
                lp_spec     (num, num, num, str)
        Returns:
            lpp             LPointPartition
        """
        method_name = 'from_specs'
        try:
            if not (
                type(specs) == list and
                labeled_point.LabeledPoint.are_lpoint_specs(specs)
            ):
                raise TypeError
        except TypeError:
            message = 'Must be a list of labeled point specs'
            cls._print_error_message(method_name, message)
        else:
            lpoints = []
            for spec in specs:
                x, y, z, label = spec
                lpoint = labeled_point.LabeledPoint.from_parts(x, y, z, label)
                lpoints.append(lpoint)
            new_lpoint_part = LPointPartition(lpoints)
            return new_lpoint_part

        ### represent
    def __str__(self):
        """The empty label is shown as ''. Returns:
            lpp_string      str. Ordered by label and point in the form:
                            {<label>: [(<x>, <y>, <z>), ...], ...}
        """
        entry_strings = []
        for label in sorted(self.dictionary):
            points = self.dictionary[label]
            label_string = "'%s'" % label
            ordered_points_string = self._get_ordered_points_string(
                points)
            entry_string = '%s: %s' % (label_string, ordered_points_string)
            entry_strings.append(entry_string)
        entries_string = ', '.join(entry_strings)
        lpp_string = '{%s}' % entries_string
        return lpp_string

    def __repr__(self):
        """Returns:
            string          str. In the form:
                            'lpoint_partition.LPointPartition([<lp1_repr>, ...])'
        """
        lpoint_reprs = []
        for label in sorted(self.dictionary):
            clpoint_reprs = self._get_clpoint_reprs(label)
            lpoint_reprs.extend(clpoint_reprs)
        lpoints_repr = '[%s]' % (', '.join(lpoint_reprs))
        string = 'lpoint_partition.%s(%s)' % (
            self.__class__.__name__,
            lpoints_repr)
        return string

    def _get_clpoint_reprs(self, label):
        """Receives:
            label           str
        Returns:
            reprs           [lp_repr, ...]. An ordered list of colabeled 
                            point reprs, where:
                lp_repr     str. A labeled point repr
        """
        reprs = []
        for p in sorted(self.dictionary[label]):
            lpoint = labeled_point.LabeledPoint(p, label)
            lpoint_repr = repr(lpoint)
            reprs.append(lpoint_repr)
        return reprs

    def _get_points_repr(self, points):
        """Receives:
            points          set([Point, ...])
        Returns:
            pp_repr         str. An ordered string of point reprs in the form 
                            "point.Point(<x>, <y>, <z>), ..."
        """
        p_reprs = []
        for p in sorted(points):
            p_repr = repr(p)
            p_reprs.append(p_repr)
        pp_repr = ', '.join(p_reprs)
        return pp_repr

    @classmethod
    def _get_ordered_points_string(self, points):
        """Receives:
            points          set([Point]). A set of points
        Returns:
            ordered_points_string
                            str. An ordered string of point strings:
                            'p_string, ...', where:
                p_string    '(<x>, <y>, <z>)'
        """
        ordered_point_strings = [str(p) for p in sorted(points)]
        ordered_points_string = ', '.join(ordered_point_strings)
        ordered_points_string = '[%s]' % ordered_points_string
        return ordered_points_string

    def listing(self, decimal_places=0):
        """Receives:
            decimal_places  int. The number of decimal places, n >= 0
        Creates an ordered, formatted, multi-line string. Returns:
            lpp_listing     str. In the form:
                                <label>:
                                    (<x>, <y>, <z>)
                                    ...
                                ...
        """
        if self.is_empty():
            lpp_listing = '<no labeled points>'
        else:
            entry_listings = []
            for label_i in sorted(self.dictionary):
                points_set_i = self.dictionary[label_i]
                indent_level = 1
                points_listing_i = self._get_points_listing(
                    points_set_i, decimal_places, indent_level)
                entry_listing_i = "'%s':\n%s" % (
                    label_i, points_listing_i)
                entry_listings.append(entry_listing_i)
            lpp_listing = '\n'.join(entry_listings)
        return lpp_listing

    def _get_points_listing(self, points, decimal_places, indent_level):
        """Receives:
            points          set([Point, ...])
            decimal_places  num
            indent_level    int
        Creates an ordered, formatted, multi-line string. Returns:
            points_listing  str. In the form:
                                (<x>, <y>, <z>)
                                ...
        """
        point_listings = []
        for p in sorted(points):
            p_listing = p.listing(decimal_places)
            indent = '    ' * indent_level
            indented_p_listing = '%s%s' % (indent, p_listing)
            point_listings.append(indented_p_listing)
        points_listing = '\n'.join(point_listings)
        return points_listing

        ### get
    # def get_specs(self):                        ##  suspended
        # """Returns: 
        #     lp_specs        [lp_spec, ...]. An ordered list of lpoint specs 
        #                     (x, y, z, label), where:
        #         x, y, z     num
        #         label       str
        # """
        # lp_specs = []
        # for label in self.dictionary:
        #     points = self.dictionary[label]
        #     for p in sorted(points):
        #         lp_spec = (p.x, p.y, p.z, label)
        #         lp_specs.append(lp_spec)
        # return lp_specs

        ### compare
    def __eq__(self, other):
        value = (self.dictionary == other.dictionary)
        return value

    def __ne__(self, other):
        value = self.dictionary != other.dictionary
        return value
        
    def is_empty(self):
        value = (self.dictionary == {})
        return value

    def is_an_lpoint_subpartition_of(self, other):
        """Receives:
            other           LPointPartition
        Returns:
            value           boolean. True if every lpoint set in self is a 
                            subset of an lpoint set in other
        """
        self_label = set(self.dictionary.keys())
        other_labels = set(other.dictionary.keys())
        if self_label.issubset(other_labels):
            value = self._point_sets_are_subsets_in(other)
        else:
            value = False
        return value

    def _point_sets_are_subsets_in(self, other):
        """Receives:
            other           LPointPartition. Every label in self is a label 
                            in other
        Returns:
            value           boolean. True if each colabeled point set in self 
                            is a subset of a colabeled point set in other. 
                            False otherwise
        """
        value = True
        for label in self.dictionary:
            self_points = self.dictionary[label]
            other_points = other.dictionary[label]
            if not self_points.issubset(other_points):
                value = False
                break
        return value

        ### operate
    def __add__(self, other):
        """Receives:
            other           LPointPartition
        Returns: 
            lpp_sum         LPointPartition. Contains items consisting of (1) 
                            every label in self or other or both and (2) the 
                            union of the corresponding colabeled point sets 
        """
        dict_sum = self.dictionary.copy()
        for label in other.dictionary:
            other_points = other.dictionary[label]
            if label in dict_sum:
                points_sum = dict_sum[label]
                dict_sum[label] = points_sum.union(other_points)
            else:
                dict_sum[label] = other_points
        lpp_sum = LPointPartition([])
        lpp_sum.dictionary = dict_sum
        return lpp_sum

    def __sub__(self, other):
        """Receives:
            other           LPointPartition
        Returns the difference self - other:
            lpp_diff        LPointPartition. Contains items consisting of (1) 
                            every label in other not in self and (2) the 
                            difference (self - other) of the corresponding 
                            colabeled point sets
        """
        if self.is_empty():
            lpp_diff = LPointPartition.new_empty()
        elif other.is_empty():
            lpp_diff = self
        else:
            lpoints_diff = []
            for label in self.dictionary:
                self_points = self.dictionary[label] 
                if label in other.dictionary:
                    other_points = other.dictionary[label]
                    points_diff = self_points - other_points
                else:
                    points_diff = self_points
                for p in points_diff:
                    lp = labeled_point.LabeledPoint(p, label)
                    lpoints_diff.append(lp)
            lpp_diff = LPointPartition(lpoints_diff)
        return lpp_diff

    @classmethod
    def _print_error_message(cls, method_name, message):
        print '%s.%s:\n    %s' % (cls.__name__, method_name, message)

        ###
if __name__ == '__main__':
    import doctest
    doctest.testfile('tests/lpoint_partition_test.txt')
