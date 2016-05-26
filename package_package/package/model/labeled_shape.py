import copy
import line_partition
import lpoint_partition
import shape
# from package.model import line_partition
# from package.model import lpoint_partition
# from package.model import shape

class LabeledShape(object):
    ### construct
    def __init__(self, shape_in, lpoint_part_in):
        """Receives:
            shape_in        Shape
            lpoint_part_in  LPointPartition
        """
        method_name = '__init__'
        try:
            if not (
                type(shape_in) == shape.Shape and
                type(lpoint_part_in) == (lpoint_partition.LPointPartition)
            ):
                raise TypeError
        except TypeError:
            message = '%s %s' % (
                'The arguments must be a shape',
                'and a labeled point partition')
            self._print_error_message(method_name, message)
        else:
            self.shape = shape_in
            self.lpoint_part = lpoint_part_in
            self.best_triad = self._find_best_triad()

    @classmethod                                ##  2016-03-15 08:46
    def _find_best_triad(cls):
        """
        Receives:
            best_triad      Triad
        """
        best_triad = None
        return best_triad

    @classmethod
    def from_parts(cls, x, y, z, label):
        """Receives:
            x               num
            y               num
            z               num
            label           Str
        Returns:
            new_lshape      LabeledShape
        """
        p = point.Point(x, y, z)
        new_lshape = LabeledShape(p, label)
        return new_lshape

    @classmethod
    def new_from_specs(cls, line_specs, lpoint_specs):
        """Receives:
            line_specs      [line_spec, ...]
            lpoint_specs    [lpoint_spec, ...]
        Returns:
            LabeledShape    the labeled shape specified by the specs
        """
        new_shape = shape.Shape.from_specs(line_specs)
        new_lpoint_partition = None
        new_labeled_shape = LabeledShape(new_shape, new_lpoint_partition)
        return new_labeled_shape

    @classmethod
    def new_empty(cls):
        empty_shape = shape.Shape.new_empty()
        empty_lpoint_part = lpoint_partition.LPointPartition.new_empty()
        empty_lshape = LabeledShape(empty_shape, empty_lpoint_part)
        return empty_lshape

    ### represent
    def __str__(self):
        """Returns:
            string          str. In the form (shape_str, lpoint_part):
                shape_str   Ordered by carrier and line in the form 
                            {<carrier>: <colineation>}
                carrier     (<unit_vector>, <intercept>)
                unit_vector Vector. In the form [<x> <y> <z>]
                intercept   Point. In the form (<x>, <y>, <z>)
                colineation Colineation. In the form [<line>, ...]
                line        Line. In the form 
                            ((<x1>, <y1>, <z1>), (<x2>, <y2>, <z2>))
                lpp_string  Ordered by label and point in the form 
                            {<label>: [(<x>, <y>, <z>), ...]}

            string          str. In the form of ordered lists 
                            ([line, ...], [lpoint, ...]):
                line        (point, point)
                point       (x, y, z)
                lpoint      (x, y, z, label)
        """
        if self.is_empty():
            string = ''
        else:
            shape_str = str(self.shape)
            lpoint_part_str = str(self.lpoint_part)
            string = '(%s, %s)' % (shape_str, lpoint_part_str)
        return string

    def listing(self, decimal_places=0):
        """Returns:
            string          str. Ordered in the form:
                            (<uv>, <intercept>)
                                <line>
                                ...
                            ...
                            <label>
                                <point>
                                ...
                            ...
                uv          [<x> <y> <z>]
                intercept   (<x>, <y>, <z>)
        """
        if self.is_empty():
            listing = ''
        else:
            shape_listing = self.shape.listing(decimal_places)
            lpoint_part_listing = self.lpoint_part.listing(decimal_places)
            listing = '%s\n%s' % (shape_listing, lpoint_part_listing)
        return listing

    ### compare
    def __hash__(self):
        shape_hash = hash(self.shape)
        lpoints_hash = hash(self.lpoint_part)
        value = hash((shape_hash, lpoints_hash))
        return value

    def __eq__(self, other):
        value = (
            self.shape == other.shape and
            self.lpoint_part == other.lpoint_part)
        return value

    def __ne__(self, other):
        value = (
            self.shape != other.shape or
            self.lpoint_part != other.lpoint_part)
        return value

    def is_empty(self):                         #   no test
        value = (
            self.shape.is_empty() and
            self.lpoint_part.is_empty())
        return value

    def is_a_sub_labeled_shape_of(self, other):
        """Receives:
            other           LabeledPoint
        Returns:
            value           boolean
        """
        value = (
            self.shape.is_a_subshape_of(other.shape) and
            self.lpoint_part.is_a_sub_lpoint_partition_of(other.lpoint_part))
        return value

    ### operations
    def __add__(self, other):
        """Receives:
            other           LabeledShape
        Returns:
            lshape_sum      LabeledShape. The sum of self and other
        """
        shape_sum = self.shape + other.shape
        lpoint_part_sum = self.lpoint_part + other.lpoint_part
        lshape_sum = LabeledShape(shape_sum, lpoint_part_sum)
        return lshape_sum

    def __sub__(self, other):
        """Receives:
            other           LabeledShape
        Returns:
            lshape_diff     LabeledShape. The difference self - other
        """
        trace_on = False
        if trace_on:
            method_name = 'LabeledShape.__sub__()'
            print '||| %s' % method_name
            print 'self.shape'
            print self.shape.listing()
            print 'other.shape'
            print other.shape.listing()
        shape_diff = self.shape - other.shape
        if trace_on:
            print '||| %s' % method_name
            print 'shape_diff'
            print shape_diff.listing()
        lpoint_part_diff = self.lpoint_part - other.lpoint_part
        lshape_diff = LabeledShape(shape_diff, lpoint_part_diff)
        return  lshape_diff

    def intersection(self, other):
        """Receives:
            other           LabeledShape
        Returns:
            lshape_intersection
                            LabeledShape. The intersection of self and other
        """
        shape_intersection = self.shape.intersection(other.shape)
        lpoints_intersection = (
            self.lpoint_part.intersection(other.lpoint_part))
        lshape_intersection = labeled_shape.LabeledShape(
            shape_intersection, lpoints_intersection)
        return lshape_intersection

    def union(self, other):
        """Receives:
            other           LabeledShape
        Returns:
            lshape_union    LabeledShape. The union of self and other
        """
        shape_union = self.shape.union(other.shape)
        lpoints_union = (
            self.lpoint_part.union(other.lpoint_part))
        lshape_union = labeled_shape.LabeledShape(shape_union, lpoints_union)
        return lshape_union

    ### other
    @classmethod
    def make_lshape_from(cls, lines, lpoints):  #   controller
        """Receives a list of lines and a list of labeled points:
            [Line, ...]
            [LabeledPoint, ...]
        Returns:
            LabeledShape
        """
        new_shape = shape.Shape.from_lines(lines)
        new_lpoint_part = lpoint_partition.LPointPartition(lpoints)
        return LabeledShape(new_shape, new_lpoint_part)

    ### export
    def get_element_specs(self):                #   controller, translator
        """Returns a 2-tuple of lists of element specs:
            ([(x1, y1, x2, y2), ...], [(x, y, label), ...])
        """
        line_specs = self.shape.line_specs()
        lpoint_specs = self.lpoint_part.specs()
        return (line_specs, lpoint_specs)

    @classmethod
    def _print_error_message(cls, method_name, message):
        print '%s.%s:\n    %s' % (cls.__name__, method_name, message)

if __name__ == '__main__':
    import doctest
    doctest.testfile('tests/labeled_shape_test.txt')
