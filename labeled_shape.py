#   labeled_shape.py

import copy
import line_partition
import lpoint_partition
import shape


class LabeledShape(object):
    ### construct
    def __init__(self, shape_in, lpoint_partition_in):
        """Receives:
            Shape
            LPointPartition
        """
        self.the_shape = shape_in
        self.lpoint_part = lpoint_partition_in

    @classmethod
    def new_empty(cls):
        empty_shape = shape.Shape.new_empty()
        empty_lpoint_part = line_partition.LinePartition.new_empty()
        empty_lshape = LabeledShape(empty_shape, empty_lpoint_part)
        return empty_lshape

    ### represent
    def __str__(self):
        """Returns a string of a duple of ordered line specs and ordered labeled 
        point specs:
            ([(x1, y1, x2, y2), ...], [(x, y, label), ...])
        """
        return '(%s, %s)' % (self.the_shape, self.lpoint_part)

    def listing(self):
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
            shape_listing = self.the_shape.listing()
            lpoint_part_listing = self.lpoint_part.listing()
            # lpoint_part_listing = self.get_lpoint_partition_listing(
            #     self.lpoint_part)
            listing = '%s\n%s' % (shape_listing, lpoint_part_listing)
        return listing

    ### compare
    def __eq__(self, other):                                                    #   no test
        return (
            self.the_shape == other.the_shape and
            self.lpoint_part == other.lpoint_part)

    def __ne__(self, other):                                                    #   no test
        return (
            self.the_shape != other.the_shape or
            self.lpoint_part != other.lpoint_part)

    def is_empty(self):                                                         #   no test
        return (
            self.the_shape.is_empty() and
            self.lpoint_part.is_empty())

    def is_a_sub_labeled_shape_of(self, other):                                 #   not called
        return (self.the_shape.is_a_subshape_of(other.the_shape) and
                self.lpoint_part.is_a_sub_lpoint_partition_of(
                    other.lpoint_part))

    ### operations
    def __add__(self, other):
        new_shape = self.the_shape + other.the_shape
        new_lpoint_part = self.lpoint_part + other.lpoint_part
        new_lshape = LabeledShape(new_shape, new_lpoint_part)
        return new_lshape

    def __sub__(self, other):
        new_shape = self.the_shape - other.the_shape
        new_lpoint_part = self.lpoint_part - other.lpoint_part
        new_lshape = LabeledShape(new_shape, new_lpoint_part)
        return new_lshape

    def __and__(self, other):                                                   #   not called, no test
        #   Intersection &                                                      #   not implemented
        new_shape = self.the_shape & other.the_shape
        new_lpoint_part = self.lpoint_part & other.lpoint_part
        return LabeledShape(new_shape, new_lpoint_part)

    ### other
    @classmethod
    def make_lshape_from(cls, lines, lpoints):              #   controller
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
    def get_element_specs(self):                    #   controller, translator
        """Returns a 2-tuple of lists of element specs:
            ([(x1, y1, x2, y2), ...], [(x, y, label), ...])
        """
        line_specs = self.the_shape.line_specs()
        lpoint_specs = self.lpoint_part.specs()
        return (line_specs, lpoint_specs)

    ### test
def subtract_test():
    import obj_translator
    trace_on = True
    w_vline_obj = open(
        '/Users/liandrew/Dropbox/F/FreeCad stuff/subtraction_test/w_vline.obj')
    w_vline = obj_translator.ObjTranslator.get_lshape_from(w_vline_obj)
    ovhv_obj = open(
        '/Users/liandrew/Dropbox/F/FreeCad stuff/subtraction_test/-vhv_sw_ell_nw_vline.obj')
    ovhv = obj_translator.ObjTranslator.get_lshape_from(ovhv_obj)
    lshape_difference = w_vline - ovhv
    if trace_on:
        print '||  w_vline:\n%s' % w_vline.listing()
        # print '||  ovhv_listing:\n%s' % ovhv.listing()
        print '||  ovhv:\n%s' % ovhv
        print '||  lshape_difference:\n%s' % lshape_difference.listing()

if __name__ == '__main__':
    import doctest
    doctest.testfile('tests/labeled_shape_test.txt')
