#   labeled_shape.py

import copy
import line_partition
import shape


class LabeledShape(object):
    ### construct
    def __init__(self, shape, lpoint_partition):
        """Receives:
            Shape
            LPointPartition
        """
        self.shape = shape
        self.lpoint_part = lpoint_partition

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
        return '(%s, %s)' % (self.shape, self.lpoint_part)

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
            shape_listing = self.shape.listing()
            lpoint_part_listing = self.lpoint_part.listing()
            # lpoint_part_listing = self.get_lpoint_partition_listing(
            #     self.lpoint_part)
            listing = '%s\n%s' % (shape_listing, lpoint_part_listing)
        return listing

    ### compare
    def __eq__(self, other):
        return (
            self.shape == other.shape and
            self.lpoint_part == other.lpoint_part)

    def __ne__(self, other):
        return (
            self.shape != other.shape or
            self.lpoint_part != other.lpoint_part)

    def is_empty(self):
        return (
            self.shape.is_empty() and
            self.lpoint_part.is_empty())

    ### operations
    def __add__(self, other):
        new_shape = self.shape + other.shape
        new_lpoint_part = self.lpoint_part + other.lpoint_part
        new_lshape = LabeledShape(new_shape, new_lpoint_part)
        return new_lshape

    def __sub__(self, other):
        new_shape = self.shape - other.shape
        new_lpoint_part = self.lpoint_part - other.lpoint_part
        new_lshape = LabeledShape(new_shape, new_lpoint_part)
        return new_lshape

    def __and__(self, other):                                                   #   not called, no test
        #   Intersection &                                                      #   not implemented
        new_shape = self.shape & other.shape
        new_lpoint_part = self.lpoint_part & other.lpoint_part
        return LabeledShape(new_shape, new_lpoint_part)

    ### other
    def make_lshape_from(self, lines, lpoints):                 # 1.2           #   called by controller
        """Receives a list of SGLines and a list of SGLabeledPoints:
            [SGLine, ...]
            [SGLabeledPoint, ...]
        Returns:
            LabeledShape
        """
        #   class method?
        shape = shape.Shape.from_lines(lines)
        lpoint_part = self.get_lpoint_partition_from(lpoints)   # 1.2.1
        return LabeledShape(shape, lpoint_part)

    def get_lpoint_partition_from(self, lpoints):               # 1.2.1
        """Receives a list of lpoints:
            [SGLabeledPoint, ...]
        Returns an lpoint_partition:
            {label: set([(x, y), ...]), ...}
        """
        lpoint_part = {}
        for lpoint in lpoints:
            point_coord = (lpoint.x, lpoint.y)
            label = lpoint.label
            if label in lpoint_part:
                point_coord_set = lpoint_part[label]
                point_coord_set.add(point_coord)
            else:
                lpoint_part[label] = set([point_coord])
                # lpoint_part[label] = point_coord_set
        return lpoint_part

    ### export
    def get_element_specs(self):                                # 2.1           #   controller, translator
        """Returns a 2-tuple of lists of SG element specs:
            ([(x1, y1, x2, y2), ...], [(x, y, label), ...])
        """                                                                     #   no test
        line_specs = self.get_line_specs()                      # 2.1.1
        lpoint_specs = self.get_lpoint_specs_from(self.lpoint_part)
                                                                # 2.1.2
        return (line_specs, lpoint_specs)

    def get_line_specs(self):                                   # 2.1.1
        """Receives a line_partition or shape (if transitive)
        Returns an ordered list of line_specs: maximal?
            [(x1, y1, x2, y2), ...]
        """
        return self.shape.get_line_specs()

    def get_lpoint_specs_from(self, lpoint_part):               # 2.1.2
        """Receives an lpoint_partition:
            {label: set([(x, y), ...]), ...}, len() >= 0
        Intermediate result: a list of colabeled_lpoint_specs
            [(x, y, label), ...], len() >= 0
        Returns an ordered list of lpoint_specs:
            [(x, y, label), ...], len() >= 0
        """                                                                     #   Why is this transitive?
        lpoint_specs = []
        for label in lpoint_part:
            colabeled_point_specs = lpoint_part[label]
            colabeled_lpoint_specs = self.get_colabeled_lpoint_specs_from(
                colabeled_point_specs, label)                   # 2.1.2.1
            lpoint_specs.extend(colabeled_lpoint_specs)
        return sorted(lpoint_specs)

    def get_colabeled_lpoint_specs_from(self, colabeled_point_specs, label):
                                                                # 2.1.2.1
        """Receives:
            a list of colabeled_point_specs:
                [(x, y), ...]
            label:
                string
        Returns a list of colabeled_lpoint_specs:
            [(x, y, label), ...]
        """
        colabeled_lpoint_specs = []
        for colabeled_point_spec in colabeled_point_specs:
            x, y = colabeled_point_spec
            colabeled_lpoint_spec = (x, y, label)
            colabeled_lpoint_specs.append(colabeled_lpoint_spec)
        return sorted(colabeled_lpoint_specs)

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
