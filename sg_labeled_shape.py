#   sg_labeled_shape.py
#   2013-09-24

import copy
import sg_labeled_point
import sg_line
import sg_point
import sg_shape


class SGLabeledShape(object):
        ### construction ###
    def __init__(self, shape, lpoint_partition):
        """Receives SGShape and lpoint_partition:
            SGShape
            {label: set([(x, y), ...]), ...}
        """
        self.shape = shape
        self.lpoint_partition = lpoint_partition    #   ordered?

    @classmethod
    def new_empty(cls):
        empty_shape = sg_shape.SGShape()    #   new_empty()?
        empty_lpoint_partition = {}
        return SGLabeledShape(empty_shape, empty_lpoint_partition)

    @classmethod
    def from_shape_and_lpoint_partition(cls, shape, lpoint_partition):
        return SGLabeledShape(shape, lpoint_partition)

    @classmethod
    def lpoint_partition_from_lpoint_specs(cls, lpoint_specs):
        """Receives:
            [(x, y, label), ...]
        Returns:
            {label: set([(x, y), ...]), ...}
        """
        lpoint_partition = {}
        for lpoint_spec in lpoint_specs:
            label = lpoint_spec[2]
            point_spec = lpoint_spec[0:2]
            if label in lpoint_partition:
                point_specs = lpoint_partition[label]
                point_specs.append(point_spec)
            else:
                lpoint_partition[label] = set([point_spec])
        return lpoint_partition

        ### relations ###
    def __eq__(self, other):
        return (self.shape == other.shape and
                self.lpoint_partition == other.lpoint_partition)

    def __ne__(self, other):
        return (self.shape != other.shape or
                self.lpoint_partition != other.lpoint_partition)

    def is_a_sub_lshape_of(self, other):
        return (self.shape.is_a_subshape_of(other.shape) and
                self.is_a_sub_lpartition(
                    self.lpoint_partition, other.lpoint_partition))

    def is_a_sub_lpartition(self, partition_1, partition_2):
        """Receives 2 lpoint_partitions:
            {label: set([(x, y), ...]), ...}
        """
        for label in partition_1:
            if label not in partition_2.keys():
                return False
            else:
                lpoints_1 = partition_1[label]
                lpoints_2 = partition_2[label]
                if not lpoints_1.issubset(lpoints_2):
                    return False
        return True
            

        ### operations ###
    def __add__(self, other):
        new_shape = self.shape + other.shape
        new_lpoint_partition = self.add_lpoint_partitions(
            self.lpoint_partition, other.lpoint_partition)
        return SGLabeledShape(new_shape, new_lpoint_partition)

    def add_lpoint_partitions(self, lpoint_partition_1, lpoint_partition_2):
        """Receives 2 lpoint_partitions; returns 1:
            {label: set([(x, y), ...]), ...}, len() >= 0
        """
        new_lpoint_partition = copy.copy(lpoint_partition_1)
        for label in lpoint_partition_2:
            point_set_2 = lpoint_partition_2[label]
            if label in new_lpoint_partition:
                point_set_1 = lpoint_partition_1[label]
                new_lpoint_partition[label] = point_set_1 | point_set_2
            else:
                new_lpoint_partition[label] = point_set_2
        return new_lpoint_partition

    def __sub__(self, other):
        new_shape = self.shape - other.shape
##        print '||| SGLabeledShape.__sub__.new_shape: %s' % new_shape
        new_lpoint_partition = self.subtract_lpoint_partitions(
            self.lpoint_partition, other.lpoint_partition)
        new_lshape = SGLabeledShape(new_shape, new_lpoint_partition)
        return new_lshape

    def subtract_lpoint_partitions(self, partition_1, partition_2):
        if partition_1 == {}:
            new_partition = {}
        elif partition_2 == {}:
            new_partition = partition_1
        else:
            new_partition = self.subtract_nonempty_lpoint_partitions(
                partition_1, partition_2)
        return new_partition

    def subtract_nonempty_lpoint_partitions(self, partition_1, partition_2):
        """Receives 2 nonempty lpoint partitions
        Returns an lpoint partition, possibly empty, such that each point set is
        the difference set_1 - set_2. If a difference is the empty set, the
        entry is excluded from the partition
        """
        new_partition = {}
        for label in partition_1:
            point_set_1 = partition_1[label]
            if label in partition_2:
                point_set_2 = partition_2[label]
                new_point_set = point_set_1.difference(point_set_2)
            else:
                new_point_set = point_set_1
            if new_point_set == set([]):
                pass
            else:
                new_partition[label] = new_point_set
        return new_partition

    def __and__(self, other):                   #   no test
        #   Intersection &
        new_line_partition = self.get_intersection_of_line_partitions(
            self.line_partition, other.line_partition)
        new_point_partition = self.get_intersection_of_point_partitions(
            self.point_partition, other.point_partition)
        return SGShape(new_line_partition, new_point_partition)

        ### other ###
    def make_lshape_from(self, lines, lpoints):                 # 1.2
        """Receives a list of SGLines and a list of SGLabeledPoints:
            [SGLine, ...]
            [SGLabeledPoint, ...]
        Returns:
            SGLabeledShape
        """
        #   class method?
        shape = sg_shape.SGShape.from_lines(lines)
        lpoint_partition = self.get_lpoint_partition_from(lpoints)
                                                                # 1.2.1
        return SGLabeledShape(shape, lpoint_partition)

    def get_lpoint_partition_from(self, lpoints):               # 1.2.1
        """Receives a list of lpoints:
            [SGLabeledPoint, ...]
        Returns an lpoint_partition:
            {label: set([(x, y), ...]), ...}
        """
        lpoint_partition = {}
        for lpoint in lpoints:
            point_coord = (lpoint.x, lpoint.y)
            label = lpoint.label
            if label in lpoint_partition:
                point_coord_set = lpoint_partition[label]
                point_coord_set.add(point_coord)
            else:
                lpoint_partition[label] = set([point_coord])
##                lpoint_partition[label] = point_coord_set
        return lpoint_partition

        ### export ###
    def get_element_specs(self):                                # 2.1
        """Returns a 2-tuple of lists of SG element specs:
            ([(x1, y1, x2, y2), ...], [(x, y, label), ...])
        """
                                                #   no test
        line_specs = self.get_line_specs()                      # 2.1.1
        lpoint_specs = self.get_lpoint_specs_from(self.lpoint_partition)
                                                                # 2.1.2
        return (line_specs, lpoint_specs)

    def get_line_specs(self):                                   # 2.1.1
        """Receives a line_partition or shape (if transitive)
        Returns an ordered list of line_specs: maximal?
            [(x1, y1, x2, y2), ...]
        """
        return self.shape.get_line_specs()

    def get_lpoint_specs_from(self, lpoint_partition):          # 2.1.2
        """Receives an lpoint_partition:
            {label: set([(x, y), ...]), ...}, len() >= 0
        Intermediate result: a list of colabeled_lpoint_specs
            [(x, y, label), ...], len() >= 0
        Returns an ordered list of lpoint_specs:
            [(x, y, label), ...], len() >= 0
        """
                                                #   Why is this transitive?
        lpoint_specs = []
        for label in lpoint_partition:
            colabeled_point_specs = lpoint_partition[label]
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

        ### representation ###
    def __str__(self):                          #   no test
        lpoint_partition_str = self.get_lpoint_partition_str()  #   sorted?
        return 's(lp%s, pp%s)' % (line_partition_str, lpoint_partition_str)

    def get_lpoint_partition_str(self):         #   no test
        partition = self.lpoint_partition
        s = '{'
        i = 1
        n = len(partition)
        for label in partition:
            point_coord_set = partition[label]
            point_coord_set_str = self.get_point_coord_set_str(point_coord_set)
            if i < n:
                point_coord_set_str += ', '
            s += '%s: %s' % (label, point_coord_set_str)
            i += 1
        s += '}'
        return s

    def get_point_coord_set_str(self, point_coord_set): #   no test
        s = '{'
        i = 1
        n = len(point_coord_set)
        for point in sorted(point_coord_set):
            point_str = '%s' % point.__str__()
            if i < n:
                point_str += ', '
            s += point_str
            i += 1
        s += '}'
        return s

    def listing(self):
        """A string in the ordered form:
            carrier:
                line_spec
                ...
            ...
            label:
                lpoint_spec
                ...
        """
        shape_listing = self.shape.listing()
        lpoint_partition_listing = self.get_lpoint_partition_listing(
            self.lpoint_partition)
        s = '%s\n%s' % (shape_listing, lpoint_partition_listing)
        return s

    def get_lpoint_partition_listing(self, partition):  #   no listing
        """Receives an lpoint_partition:
            {label: set([(x, y), ...]), ...]
        Returns an lpoint_partition_listing:
            label:
                (x, y)
                ...
            ...
        """
        s = ''
        n = len(partition)
        i = 1
        if n == 0:
            s = '<no labeled points>'
        else:
            for label in sorted(partition):
                point_specs = partition[label]
                point_specs_listing = self.get_point_specs_listing(
                    point_specs)
                s += '%s:\n%s' % (label, point_specs_listing)
                if i < n:
                    s += '\n'
                i += 1
        return s

    def get_point_specs_listing(self, point_specs): #   no listing
        """Receives point_specs:
            set([(x, y), ...])
        Returns point_specs_listing:
            (x, y)
            ...
        """
        s = ''
        tab = ' ' * 4
        i = 1
        n = len(point_specs)
        for point_spec in sorted(point_specs):
            x, y = point_spec
            s += '%s(%3.1f, %3.1f)' % (tab, x, y)
            if i < n:
                s += '\n'
            i += 1
        return s

    ####
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
##        print '||  ovhv_listing:\n%s' % ovhv.listing()
        print '||  ovhv:\n%s' % ovhv
        print '||  lshape_difference:\n%s' % lshape_difference.listing()

    ####
if __name__ == '__main__':
    subtract_test()

##    import doctest
##    doctest.testfile('sg_labeled_shape_test.txt')
