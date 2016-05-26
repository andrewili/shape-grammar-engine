import colineation
import copy
import line
import line_partition
# from package.translators import colineation
# from package.translators import copy
# from package.translators import line
# from package.translators import line_partition

class Shape(object):
    """Has a line partition
    """
    ### construct
    def __init__(self, line_part_in):
        """Receives:
            line_part_in    LinePartition
        """
        method_name = '__init__'
        try:
            if not (
                type(line_part_in) == line_partition.LinePartition
            ):
                raise TypeError
        except TypeError:
            message = 'The argument must be a line partition'
            self._print_error_message(method_name, message)
        else:
            self.line_part = line_part_in

    @classmethod
    def from_lines(cls, lines):
        new_line_part = line_partition.LinePartition(lines)
        new_shape = Shape(new_line_part)
        return new_shape

    @classmethod
    def from_specs(cls, specs):
        """Receives:
            specs           [spec, ...] A list of line specs: 
                spec        ((x1, y1, z1), (x2, y2, z2))
        Returns: 
            new_shape       Shape
        """
        lines = []
        for spec in specs:
            p1_spec, p2_spec = spec
            x1, y1, z1 = p1_spec
            x2, y2, z2 = p2_spec
            line_i = line.Line.from_specs(x1, y1, z1, x2, y2, z2)
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
        """Returns:
            string          str. Ordered by carrier and line. In the form 
                            {carrier: colineation}, where:
                carrier     (unit_vector, intercept)
                unit_vector Vector. In the form [<x> <y> <z>]
                intercept   Point. In the form (<x>, <y>, <z>)
                colineation Colineation. In the form [line, ...]
                line        Line. In the form 
                            ((<x1>, <y1>, <z1>), (<x2>, <y2>, <z2>))
        """
        string = str(self.line_part)
        return string

    def __repr__(self):
        line_part_repr = repr(self.line_part)
        string = '%s(%s)' % (
            'shape.Shape',
            line_part_repr)
        return string

    def listing(self, decimal_places=0):
        """Receives:
            decimal_places  int. The number of decimal places to be shown
        Returns:
            string          str. In the form: 
                            (<uv>, <int>)
                                ((<x1>, <y1>, <z1>), (<x2>, <y2>, <z2>))
                                ...
                            ...
        """
        if self.is_empty():
            string = ''
        else:
            string = self.line_part.listing(decimal_places)
        return string

    # def line_specs(self):
        # """Returns an ordered list of line specs:
        #     [(x1, y1, x2, y2), ...]
        # """
        # specs = self.line_part.specs()
        # return specs

        ### relations
    def __hash__(self):
        value = hash(self.line_part)
        return value

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
        """Receives:
            other           Shape
        Returns:
            shape_sum       Shape. The sum of self and other
        """
        new_line_part = self.line_part + other.line_part
        shape_sum = Shape(new_line_part)
        return shape_sum

        ### subtract
    def __sub__(self, other):
        """Receives:
            other           Shape
        Returns the difference self - other:
            shape_diff      Shape
        """
        trace_on = False
        if trace_on:
            method_name = 'Shape.__sub__'
            print('||| %s' % method_name)
        line_part_diff = self.line_part - other.line_part
        shape_diff = Shape(line_part_diff)
        if trace_on:
            print('||| %s' % method_name)
            print('self:')
            print(self.listing())
            print('other:')
            print(other.listing())
            print('line_part_diff:')
            print(line_part_diff.listing())
            print('shape_diff')
            print(shape_diff.listing())
        return shape_diff

    def intersection(self, other):
        pass

    def union(self, other):
        pass

    @classmethod
    def _print_error_message(cls, method_name, message):
        print '%s.%s:\n    %s' % (cls.__name__, method_name, message)

        ###
if __name__ == '__main__':
    import doctest
    doctest.testfile('tests/shape_test.txt')
