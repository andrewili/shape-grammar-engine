import colineation
import copy
import line
import line_partition
# from package.translators import colineation
# from package.translators import copy
# from package.translators import line
# from package.translators import line_partition

class Shape(object):
        ### construct
    def __init__(self, line_partition_in):
        """Receives:
            LinePartition
        """
        method_name = '__init__()'
        try:
            if not (
                line_partition_in.__class__ == line_partition.LinePartition
            ):
                raise TypeError
        except TypeError:
            message = 'The argument must be a line partition'
            self.__class__._print_error_message(method_name, message)
        else:
            self.line_part = line_partition_in

    @classmethod
    def from_lines(cls, lines):
        new_line_part = line_partition.LinePartition(lines)
        new_shape = Shape(new_line_part)
        return new_shape

    @classmethod
    def from_specs(cls, specs):
        """Receives a list of line specs:
            [(x1, y1, x2, y2), ...]
        Returns a shape consisting of those lines:
            Shape
        """
        lines = []
        for spec in specs:
            x1, y1, x2, y2 = spec
            line_i = line.Line.from_specs(x1, y1, x2, y2)
            lines.append(line_i)
        new_line_part = line_partition.LinePartition(lines)
        new_shape = Shape(new_line_part)
        return new_shape

    @classmethod
    def new_empty(cls):
        empty_line_partition = line_partition.LinePartition.new_empty()
        new_shape = Shape(empty_line_partition)
        return new_shape

        ### represent
    def __str__(self):
        """Returns the string of the ordered line specs:
            [(x1, y1, x2, y2), ...]
        """
        return self.line_part.__str__()

    def listing(self, decimal_places=0):
        if self.is_empty():
            string = '<empty shape>'
        else:
            string = self.line_part.listing(decimal_places)
        return string

    def line_specs(self):
        """Returns an ordered list of line specs:
            [(x1, y1, x2, y2), ...]
        """
        specs = self.line_part.specs()
        return specs

        ### relations
    def __eq__(self, other):
        return self.line_part == other.line_part

    def __ne__(self, other):
        return self.line_part != other.line_part

    def is_empty(self):
        return self.line_part.is_empty()

    def is_a_subshape_of(self, other):
        return self.line_part.is_a_sub_line_partition_of(other.line_part)

        ### add
    def __add__(self, other):
        new_line_part = self.line_part + other.line_part
        return Shape(new_line_part)

        ### subtract
    def __sub__(self, other):
        """Receives:
            Shape
        Returns the difference self - other:
            Shape
        """
        trace_on = False
        if trace_on:
            method_name = 'Shape.__sub__()'
            print '||| %s' % method_name
        new_line_part = self.line_part - other.line_part
        new_shape = Shape(new_line_part)
        if trace_on:
            print '||| %s' % method_name
            print 'self:'
            print self.listing()
            print 'other:'
            print other.listing()
            print 'new_line_part:'
            print new_line_part.listing()
            print 'new_shape'
            print new_shape.listing()
        return new_shape

    @classmethod
    def _print_error_message(cls, method_name, message):
        print '%s.%s: %s' % (cls.__name__, method_name, message)

        ###
if __name__ == '__main__':
    import doctest
    doctest.testfile('tests/shape_test.txt')
