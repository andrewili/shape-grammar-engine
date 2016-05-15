import math
import numpy as np
import point
import vector

almost_equal = np.allclose

class Line(object):
    ### construct
    def __init__(self, p1, p2):
        """Receives:
            p1              Point
            p2              Point != p1
        Returns:
            Line            head > tail, implying that length > 0
        Immutable. 3D implementation started
        """
        method_name = '__init__'
        try:
            if not (
                p1.__class__ == point.Point and
                p2.__class__ == point.Point
            ):
                raise TypeError
            elif p1 == p2:
                raise ValueError
        except TypeError:
            message = 'The arguments must both be points'
            self.__class__._print_error_message(method_name, message)
        except ValueError:
            message = 'The points must be different'
            self.__class__._print_error_message(method_name, message)
        else:
            if p1 < p2:
                self.tail = p1
                self.head = p2
            else:
                self.tail = p2
                self.head = p1
            self.x1 = self.tail.x
            self.y1 = self.tail.y
            self.z1 = self.tail.z
            self.x2 = self.head.x
            self.y2 = self.head.y
            self.z2 = self.head.z
            self.spec = (self.tail.spec, self.head.spec)
            self.v = self.head - self.tail
            self.l = self.length = self.v.length
            self.carrier = self._find_carrier(self.tail, self.head)
            self.uv = self.unit_vector = self.carrier[0]
            self.int = self.intercept = self.carrier[1]

    @classmethod
    def _find_carrier(cls, tail, head):
        """Receives:
            tail            Point
            head            Point. head > tail
        Returns:
            uv              = unit vector. Vector. Indicating the direction 
                            of the line
            int             = intercept. Point 
                                In the xy-plane, if parallel to the z-axis
                                In the xz-plane, if parallel to the yz-plane
                                In the yz-plane, otherwise
        """
        v = head - tail
        uv = v.uv()
        if cls._unit_vector_is_parallel_to_z_axis(uv):
            x, y = tail.x, tail.y
            int = point.Point(x, y, 0)
        elif cls._unit_vector_is_parallel_to_yz_plane(uv):
            int = cls._find_xz_intercept(uv, tail)
        else:
            int = cls._find_yz_intercept(uv, tail)
        return (uv, int)

    @classmethod
    def _unit_vector_is_parallel_to_z_axis(cls, unit_vector):
        """Receives:
            unit_vector     Vector. Length = 1
        Returns:
            value           boolean. True if the unit vector is parallel to 
                            the z-axis. False otherwise
        """
        value = (
            almost_equal(unit_vector.x, 0) and
            almost_equal(unit_vector.y, 0) and
            almost_equal(unit_vector.z, 1))
        return value

    @classmethod
    def _unit_vector_is_parallel_to_yz_plane(cls, unit_vector):
        """Receives:
            unit_vector     Vector. Length = 1
        Returns:
            value           boolean
        """
        value = almost_equal(unit_vector.x, 0)
        return value

    @classmethod
    def _find_xz_intercept(cls, uv, p1):
        """Receives:
            uv              Vector. Unit vector, x = 0. The direction of a 
                            line 
            p1              Point. A point on the line
        Finds the xz-intercept of a line parallel to the yz-plane. Returns:
            p0              Point. The xz-intercept (x, 0, z)
        """
        p0_y = 0
        t = (p0_y - p1.y) / uv.y
        p0 = p1 + (uv * t)
        return p0

    @classmethod
    def _find_yz_intercept(cls, uv, p1):
        """Receives:
            uv              Vector. Unit vector, not parallel to the 
                            yz-plane. The direction of a line
            p1              Point. A point on the line
        Returns:
            p0              Point. The yz-intercept (0, y, z)
        """
        p0_x = 0
        t = (p0_x - p1.x) / uv.x
        p0 = p1 + (uv * t)
        return p0

    @classmethod
    def from_spec(cls, x1, y1, z1, x2, y2, z2):
        method_name = 'from_spec'
        try:
            if not (
                point.Point._is_a_number(x1) and
                point.Point._is_a_number(y1) and
                point.Point._is_a_number(z1) and
                point.Point._is_a_number(x2) and
                point.Point._is_a_number(y2) and
                point.Point._is_a_number(z2)
            ):
                raise TypeError
        except TypeError:
            message = "The arguments must all be numbers"
            cls._print_error_message(method_name, message)
        else:
            p1 = point.Point(x1, y1, z1)
            p2 = point.Point(x2, y2, z2)
            new_line = Line(p1, p2)
            return new_line

    @classmethod
    def from_spec_4(cls, x1, y1, x2, y2):
        method_name = 'from_spec_4'
        try:
            if not (
                point.Point._is_a_number(x1) and
                point.Point._is_a_number(y1) and
                point.Point._is_a_number(x2) and
                point.Point._is_a_number(y2)
            ):
                raise TypeError
        except TypeError:
            message = "The arguments must all be numbers"
            cls._print_error_message(method_name, message)
        else:
            p1 = point.Point(x1, y1)
            p2 = point.Point(x2, y2)
            new_line = Line(p1, p2)
            return new_line

    @classmethod
    def from_spec_2(cls, x1, x2):
        new_line = Line.from_spec(x1, x1, x1, x2, x2, x2)
        return new_line

    ### represent
    def __str__(self):
        string = '((%s, %s, %s), (%s, %s, %s))' % (
            self.x1, self.y1, self.z1, self.x2, self.y2, self.z2)
        return string

    def __repr__(self):
        """Returns:
            string          str. In the form 
                            'line.Line(
                                point.Point(<x1>, <y1>, <z1>), 
                                point.Point(<x2>, <y2>, <z2>))'
        """
        string = 'line.Line(%s, %s)' % (
            'point.Point(%s, %s, %s)' % (self.x1, self.y1, self.z1),
            'point.Point(%s, %s, %s)' % (self.x2, self.y2, self.z2))
        return string
        
    def listing(self, decimal_places=0):
        x1_formatted = self.tail.get_coord_listing('x', decimal_places)
        y1_formatted = self.tail.get_coord_listing('y', decimal_places)
        z1_formatted = self.tail.get_coord_listing('z', decimal_places)
        x2_formatted = self.head.get_coord_listing('x', decimal_places)
        y2_formatted = self.head.get_coord_listing('y', decimal_places)
        z2_formatted = self.head.get_coord_listing('z', decimal_places)
        string = '((%s, %s, %s), (%s, %s, %s))' % (
            x1_formatted, y1_formatted, z1_formatted,
            x2_formatted, y2_formatted, z2_formatted)
        return string

    ### relations
    def __eq__(self, other):
        if (self.tail == other.tail and
            self.head == other.head
        ):
            return True
        else:
            return False

    def __ge__(self, other):
        if self.tail > other.tail:
            return True
        elif self.tail == other.tail:
            if self.head > other.head:
                return True
            elif self.head == other.head:
                return True
            else:
                return False
        else:
            return False

    def __gt__(self, other):
        if self.tail > other.tail:
            return True
        elif self.tail == other.tail:
            if self.head > other.head:
                return True
            elif self.head == other.head:
                return False
            else:
                return False
        else:
            return False

    def __le__(self, other):
        if self.tail < other.tail:
            return True
        elif self.tail == other.tail:
            if self.head < other.head:
                return True
            elif self.head == other.head:
                return True
            else:
                return False
        else:
            return False

    def __lt__(self, other):
        if self.tail < other.tail:
            return True
        elif self.tail == other.tail:
            if self.head < other.head:
                return True
            elif self.head == other.head:
                return False
            else: return False
        else:
            return False

    def __ne__(self, other):
        if (self.tail != other.tail or
            self.head != other.head
        ):
            return True
        else:
            return False

    def is_colinear_with(self, other):
        value = (self.carrier == other.carrier)
        return value

    def can_be_merged_with(self, other):
        """Receives:
            other           Line. Colinear with self. Guaranteed [Test?]
        Returns:
            value           boolean. True if 
                            a. self <= other, and 
                            b. self and other overlap
                            False otherwise
        See Krishnamurti (1980), 465.
        """
        if self.tail == other.head:
            value = True
        elif other.tail == self.head:
            value = True
        elif (
            self.tail < other.head and
            other.tail < self.head
        ):
            value = True
        elif self.tail > other.tail:
            value = False
        else:
            value = False
        return value

    def merge_with(self, other):
        """Receives:
            other           Line. Colinear and mergeable with self. 
                            self.tail <= other.tail. Guaranteed
        Returns:
            line_sum        Line. The merged line of self and other
        """
        new_tail = min(self.tail, other.tail)
        new_head = max(self.head, other.head)
        line_sum = Line(new_tail, new_head)
        return line_sum

    def __hash__(self):
        value = hash((
            hash(self.tail), 
            hash(self.head)))
        return value

    ### part relations
    def is_a_subline_in_colineation(self, colineation):
        """Is called by:    Colineation.is_a_subcolineation_of
        Receives:
            colineation     Colineation. Colinear with self. Guaranteed by 
                            the calling function
        Returns:
            value           boolean. True if self is a subline of a line in 
                            maximized colineation. False otherwise
        """
        value = False
        for other_line in colineation.lines:
            if self.is_a_subline_of(other_line):
                value = True
        return value

    # def is_a_subline_in_colines(self, colines):     #   Looks redundant
        # """Receives:
        #     colines         [Line, ...]. A list of colinear, possibly non-
        #                     maximal, lines. Colinearity guaranteed by calling 
        #                     function
        # Returns:
        #     value           boolean. True if the line is a subline of some 
        #                     line in colines. False otherwise
        # """
        # value = False
        # for line_i in colines:
        #     if self.is_a_subline_of(line_i):
        #         value = True
        #         break
        # return value

    def is_a_subline_of(self, other):
        """Receives:
            other           Line
        Returns:
            value           boolean. True, if self is a subline of other. 
                            False otherwise
        """
        value = False
        if (self.is_colinear_with(other) and
            self.tail >= other.tail and
            self.head <= other.head
        ):
            value = True
        return value

    ### overlap relations
    def is_disjoint_less_than(self, other):
        """Is called by:    Colineation.subtract_line_colineation as 
                            is_disjoint_left_of
        Receives:
            other           Line. Colinear. Guaranteed by the calling function
        Returns:
            value           boolean. True if all of self is less than all of 
                            other. False otherwise
        """
        value = (self.head <= other.tail)
        return value

    def overlaps_tail_of(self, other):
        """Is called by:    Colineation.subtract_line_colineation
        Receives:
            other           Line. Colinear. Guaranteed by the calling function
        Returns:
            value           boolean. True if self overlaps the the tail of 
                            other. False otherwise
        """
        value = (
            self.tail <= other.tail and
            self.head >  other.tail and
            self.head <  other.head)
        return value

    def overlaps_all_of(self, other):
        """Is called by:    Colineation.subtract_line_colineation
        Receives:
            other           Line. Colinear. Guaranteed by the calling function
        Returns:
            value           boolean. True if self overlaps all of (and is 
                            longer than) other. False otherwise
        """
        value = (
            self.tail <= other.tail and
            self.head >= other.head)
        return value

    def overlaps_exactly(self, other):
        """Is called by:    Not yet. Colineation?
        Receives:
            other           Line. Colinear. Guaranteed by the calling function 
        Returns:
            value           boolean. True if self is coterminous with other. 
                            False otherwise
        """
        value = (self == other)
        return value

    def overlaps_middle_of(self, other):
        """Is called by:    Colineation.subtract_line_colineation
        Receives:
            other           Line. Colinear. Guaranteed by the calling function
        Returns:
            value           boolean. True if self overlaps other, but not 
                            other's end points. False otherwise
        """
        value = (
            self.tail >  other.tail and
            self.head <  other.head)
        return value

    def overlaps_head_of(self, other):
        """Is called by:    Colineation.subtract_line_colineation
        Receives:
            other           Line. Colinear. Guaranteed by the calling function 
        Returns:
            value           boolean. True if self overlaps the head of other. 
                            False otherwise
        """
        value = (
            self.tail >  other.tail and
            self.tail <  other.head and
            self.head >= other.head)
        return value

    def is_disjoint_greater_than(self, other):
        """Is called by:    Colineation.subtract_line_colineation
        Receives:
            other           Line. Colinear. Guaranteed by the calling function 
        Returns:
            value           boolean. True if all of self is greater than all 
                            of other. False otherwise
        """
        value = self.tail >= other.head
        return value

    ### add

    # def can_be_merged_with(self, other):        ##  not called
        # """Receives a collinear line
        # Returns whether self can be merged with other
        # See Krishnamurti (1980), 465
        # """
        # def test():
        #     if self.tail == other.head:
        #         return True
        #     elif other.tail == self.head:
        #         return True
        #     elif (
        #         self.tail < other.head and
        #         other.tail < self.head
        #     ):
        #         return True
        #     else:
        #         return False
        # try:
        #     if not self.is_colinear_with(other):
        #         raise ValueError()
        #     else:
        #         return test()
        # except ValueError:
        #     print "You're trying to test non-collinear lines"

    # def merge(self, other):                     ##  not called
        # """Receives a line that can be merged with.
        # Returns the sum of the 2 lines.
        # """
        # new_tail = min(self.tail, other.tail)
        # new_head = max(self.head, other.head)
        # new_line = Line(new_tail, new_head)
        # return new_line

    def subtract_line_tail(self, other):
        """Is called by:    Colineation.subtract_line_colineation
        Receives:
            other           Line. Colinear. Overlaps the tail of self. 
                            Guaranteed by the calling function
        Returns: 
            differences     [Line]. A list containing the single line 
                            difference self - other
        """
        method_name = 'subtract_line_tail'
        try:
            if not other.overlaps_tail_of(self):
                raise ValueError
        except ValueError:
            message = '%s %s' % (
                "The subtrahend does not overlap",
                "the tail of the minuend")
            self._print_error_message(method_name, message)
        new_tail = other.head
        new_head = self.head
        differences = [Line(new_tail, new_head)]
        return differences

    def subtract_line_middle(self, other):
        """Receives:
            other           Line. Colinear. Overlaps only the middle of self, 
                            not its head or tail. Guaranteed by the calling 
                            function
        Returns: 
            [diff1, diff2]  [Line, Line]. An ordered list of the line 
                            differences of self - other, diff1 < diff2
        """
        new_tail_1 = self.tail
        new_head_1 = other.tail
        new_tail_2 = other.head
        new_head_2 = self.head
        difference_1 = Line(new_tail_1, new_head_1)
        difference_2 = Line(new_tail_2, new_head_2)
        return [difference_1, difference_2]

    def subtract_line_head(self, other):
        """Receives:
            other           Line. Colinear. Overlaps the head of self. 
                            Guaranteed by the calling function
        Returns:
            diffs           [Line, ...]. A list containing the single 
                            line difference self - other
        """
        method_name = 'subtract_line_head'
        try:
            if not other.overlaps_head_of(self):
                raise ValueError
        except ValueError:
            message = '%s %s' % (
                'The subtrahend does not overlap',
                'the head of the minuend')
            self._print_error_message(method_name, message)
        else:
            trace_on = False
            new_tail = self.tail
            new_head = other.tail
            diffs = [Line(new_tail, new_head)]
            if trace_on:
                print '||| %s.self:\n%s' % (method_name, self)
                print '||| %s.other:\n%s' % (method_name, other)
                print '||| %s.new_tail:\n%s' % (method_name, new_tail)
                print '||| %s.new_head:\n%s' % (method_name, new_head)
            return diffs

    @classmethod
    def _print_error_message(cls, method_name, message):
        print '%s.%s:\n    %s' % (cls.__name__, method_name, message)

    ###
if __name__ == '__main__':
    import doctest
    doctest.testfile('tests/line_test.txt')
