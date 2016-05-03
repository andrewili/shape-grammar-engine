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
            self.spec = (self.x1, self.y1, self.z1, self.x2, self.y2, self.z2)
            self.v = self.head - self.tail
            self.length = self.v.length
            self.carrier = self._find_carrier(self.tail, self.head)
            self.unit_vector, self.intercept = self.carrier
            # self.carrier = self._find_carrier_from(self.spec)
            # self.direction, self.intercept = self.carrier

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
        new_line = Line.from_spec_4(x1, x1, x2, x2)
        return new_line

    ### represent
    def __str__(self):
        string = '((%s, %s, %s), (%s, %s, %s))' % (
            self.x1, self.y1, self.z1, self.x2, self.y2, self.z2)
        return string

    def __repr__(self):
        """Returns:
            string          str. In the form 
                            'line.Line.from_spec(
                                <x1>, <y1>, <z1>, <x2>, <y2>, <z2>)'
        """
        string = 'line.%s.from_spec(%s, %s, %s, %s, %s, %s)' % (
            self.__class__.__name__,
            self.x1, self.y1, self.z1,
            self.x2, self.y2, self.z2)
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

    def is_collinear_with(self, other):
        return self.carrier == other.carrier

    ### part relations
    def is_a_subline_in_colineation(self, colineation):
        """Receives a colineation:
            SGColumn
        Returns whether self is a subline of a line in the colineation
        """
        for other_line in colineation.lines:
            if self.is_a_subline_of(other_line):
                return True
        return False

    def is_a_subline_of(self, other):
        if self.tail < other.tail:
            return False
        else: # self.tail >= other.tail:
            if self.head <= other.head:
                return True
            else:
                return False

    def is_disjoint_left_of(self, other):       #   assumes horizontal line
        return  self.head <= other.tail

    def overlaps_tail_of(self, other):
        return (self.tail <= other.tail and
                self.head >  other.tail and
                self.head <  other.head)

    def overlaps_all_of(self, other):
        return (self.tail <= other.tail and
                self.head >= other.head)

    def overlaps_middle_of(self, other):
        return (self.tail >  other.tail and
                self.head <  other.head)

    def overlaps_head_of(self, other):
        return (self.tail >  other.tail and
                self.tail <  other.head and
                self.head >= other.head)

    def is_disjoint_right_of(self, other):
        return  self.tail >= other.head

    ### add

    def can_be_merged_with(self, other):
        """Receives a collinear line
        Returns whether self can be merged with other
        See Krishnamurti (1980), 465
        """
        def test():
            if self.tail == other.head:
                return True
            elif other.tail == self.head:
                return True
            elif (
                self.tail < other.head and
                other.tail < self.head
            ):
                return True
            else:
                return False
        try:
            if not self.is_collinear_with(other):
                raise ValueError()
            else:
                return test()
        except ValueError:
            print "You're trying to test non-collinear lines"

    def merge(self, other):
        """Receives a line that can be merged with.
        Returns the sum of the 2 lines.
        """
        new_tail = min(self.tail, other.tail)
        new_head = max(self.head, other.head)
        new_line = Line(new_tail, new_head)
        return new_line

    def subtract_line_tail(self, other):
        """Receives a line that overlaps self.tail
            Line
        Returns a list containing the single line difference self - other:
            [Line]
        """
        try:
            if not other.overlaps_tail_of(self):
                raise ValueError()
        except ValueError:
            print "The subtrahend does not overlap the tail of the minuend"
        new_tail = other.head
        new_head = self.head
        differences = [Line(new_tail, new_head)]
        return differences

    def subtract_line_middle(self, other):
        """Receives a line that overlaps in the middle:
            Line
        Returns a list of two line differences:
            [Line, Line]
        """
        new_tail_1 = self.tail
        new_head_1 = other.tail
        new_tail_2 = other.head
        new_head_2 = self.head
        difference_1 = Line(new_tail_1, new_head_1)
        difference_2 = Line(new_tail_2, new_head_2)
        return [difference_1, difference_2]

    def subtract_line_head(self, other):
        """Receives a line that overlaps the head:
        Returns a list containing the single line difference self - other
        """
        trace_on = False
        new_tail = self.tail
        new_head = other.tail
        differences = [Line(new_tail, new_head)]
        if trace_on:
            method_name = 'Line.subtract_line_head'
            print '||| %s.self:\n%s' % (method_name, self)
            print '||| %s.other:\n%s' % (method_name, other)
            print '||| %s.new_tail:\n%s' % (method_name, new_tail)
            print '||| %s.new_head:\n%s' % (method_name, new_head)
        return differences

    @classmethod
    def _print_error_message(cls, method_name, message):
        print '%s.%s:\n    %s' % (cls.__name__, method_name, message)

    ###
if __name__ == '__main__':
    import doctest
    doctest.testfile('tests/line_test.txt')
