import copy
import line_partition
import lpoint_partition
import shape
# from package.model import line_partition
# from package.model import lpoint_partition
# from package.model import shape

class LabeledShape(object):
    ### construct
    def __init__(self, shape_in, lpoint_partition_in):
        """Receives:
            Shape
            LPointPartition
        """
        method_name = '__init__()'
        try:
            if not (
                shape_in.__class__ == shape.Shape and
                lpoint_partition_in.__class__ == (
                    lpoint_partition.LPointPartition)
            ):
                raise TypeError
        except TypeError:
            message = '%s %s' % (
                'The arguments must be a shape',
                'and a labeled point partition')
            self.__class__._print_error_message(method_name, message)
        else:
            self.the_shape = shape_in
            self.lpoint_part = lpoint_partition_in
            self.best_triad = self.__class__._find_best_triad()

    @classmethod                                ##  2016-03-15 08:46
    def _find_best_triad(cls):
        """
        Receives:
            best_triad      Triad
        """
        return best_triad

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
        """Returns a string of a duple of ordered line specs and ordered 
        labeled point specs:
            ([(x1, y1, x2, y2), ...], [(x, y, label), ...])
        """
        return '(%s, %s)' % (self.the_shape, self.lpoint_part)

    def listing(self, decimal_places=0):
        """An ordered string in the form:
            (bearing, intercept):
                (x1, y1, x2, y2)
                ...
            ...
            label:
                (x, y)
                ...
        """
        if self.is_empty():
            listing = '<empty labeled shape>'
        else:
            shape_listing = self.the_shape.listing(decimal_places)
            lpoint_part_listing = self.lpoint_part.listing(decimal_places)
            listing = '%s\n%s' % (shape_listing, lpoint_part_listing)
        return listing

    ### compare
    def __eq__(self, other):                    #   no test
        value = (
            self.the_shape == other.the_shape and
            self.lpoint_part == other.lpoint_part)
        return value

    def __ne__(self, other):                    #   no test
        value = (
            self.the_shape != other.the_shape or
            self.lpoint_part != other.lpoint_part)
        return value

    def is_empty(self):                         #   no test
        value = (
            self.the_shape.is_empty() and
            self.lpoint_part.is_empty())
        return value

    def is_a_sub_labeled_shape_of(self, other):
        value = (
            self.the_shape.is_a_subshape_of(other.the_shape) and
            self.lpoint_part.is_a_sub_lpoint_partition_of(other.lpoint_part))
        return value

    ### operations
    def __add__(self, other):
        new_shape = self.the_shape + other.the_shape
        new_lpoint_part = self.lpoint_part + other.lpoint_part
        new_lshape = LabeledShape(new_shape, new_lpoint_part)
        return new_lshape

    def __sub__(self, other):
        trace_on = False
        if trace_on:
            method_name = 'LabeledShape.__sub__()'
            print '||| %s' % method_name
            print 'self.the_shape'
            print self.the_shape.listing()
            print 'other.the_shape'
            print other.the_shape.listing()
        new_shape = self.the_shape - other.the_shape
        if trace_on:
            print '||| %s' % method_name
            print 'new_shape'
            print new_shape.listing()
        new_lpoint_part = self.lpoint_part - other.lpoint_part
        new_lshape = LabeledShape(new_shape, new_lpoint_part)
        return new_lshape

    def __and__(self, other):                   #   not called, no test
                                                #   Intersection &
                                                #   not implemented
        new_shape = self.the_shape & other.the_shape
        new_lpoint_part = self.lpoint_part & other.lpoint_part
        return LabeledShape(new_shape, new_lpoint_part)

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
        line_specs = self.the_shape.line_specs()
        lpoint_specs = self.lpoint_part.specs()
        return (line_specs, lpoint_specs)

    @classmethod
    def _print_error_message(cls, method_name, message):
        print '%s.%s: %s' % (cls.__name__, method_name, message)

if __name__ == '__main__':
    import doctest
    doctest.testfile('tests/labeled_shape_test.txt')
