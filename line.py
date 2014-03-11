#   line.py

import math
import point


class Line(object):
    ### construct
    def __init__(self, p1, p2):
        """Receives 2 distinct points:
            Point, Point
        Returns a line with head > tail (which implies that length > 0):
            Line
        Immutable. 2D implementation
        """
        method_name = '__init__()'
        try:
            if not (
                p1.__class__ == point.Point and
                p2.__class__ == point.Point
            ):
                raise TypeError
            elif p1 == p2:
                raise ValueError
        except TypeError:
            message = 'Must be 2 points'
            self.__class__._print_error_message(method_name, message)
        except ValueError:
            message = 'Must be different points'
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
            self.x2 = self.head.x
            self.y2 = self.head.y
            self.spec = (self.x1, self.y1, self.x2, self.y2)
            self.carrier = self.get_carrier_from(self.spec)
            self.bearing, self.intercept = self.carrier
            def compute_length():
                dx = self.head.x - self.tail.x
                dy = self.head.y - self.tail.y
                length_squared = math.pow(dx, 2) + math.pow(dy, 2)
                length = math.sqrt(length_squared)
                return length
            self.length = compute_length()

        # try:
        #     if p1 == p2:
        #         raise ValueError()
        # except ValueError:
        #     print "You're trying to create a zero-length line"
        # if p1 < p2:
        #     self.tail = p1
        #     self.head = p2
        # else:
        #     self.tail = p2
        #     self.head = p1
        # self.x1 = self.tail.x
        # self.y1 = self.tail.y
        # self.x2 = self.head.x
        # self.y2 = self.head.y
        # self.spec = (self.x1, self.y1, self.x2, self.y2)
        # self.carrier = self.get_carrier_from(self.spec)
        # self.bearing, self.intercept = self.carrier
        # def compute_length():
        #     dx = self.head.x - self.tail.x
        #     dy = self.head.y - self.tail.y
        #     length_squared = math.pow(dx, 2) + math.pow(dy, 2)
        #     length = math.sqrt(length_squared)
        #     return length
        # self.length = compute_length()

    def get_carrier_from(self, line_spec):
        """Receives line_spec:
            (x1, y1, x2, y2)
        Returns carrier:
            (bearing, intercept)
        """
        x1, y1, x2, y2 = line_spec
        dy = y2 - y1
        dx = x2 - x1
        #   0 <= bearing < 180, 0 = north, increasing clockwise
        if dx == 0:
            bearing = 0.0
            intercept = x1
        else:
            slope = dy / dx
            bearing = 90 - math.degrees(math.atan(slope))
            #   y = mx + b
            #   b = y - mx
            intercept = self.y1 - (slope * self.x1)
        return (bearing, intercept)

    @classmethod
    def from_spec(cls, x1, y1, x2, y2):
        p1 = point.Point(x1, y1)
        p2 = point.Point(x2, y2)
        new_line = Line(p1, p2)
        return new_line

    @classmethod
    def from_short_spec(cls, x1, x2):
        new_line = Line.from_spec(x1, x1, x2, x2)
        return new_line

    @classmethod
    def from_points(cls, p1, p2):
        return Line(p1, p2)

    ### represent
    def __str__(self):
        return '(%s, %s, %s, %s)' % (
            self.x1, self.y1, self.x2, self.y2)

    def listing(self, decimal_places=0):
        x1_formatted = self.tail.get_formatted_coord('x', decimal_places)
        y1_formatted = self.tail.get_formatted_coord('y', decimal_places)
        x2_formatted = self.head.get_formatted_coord('x', decimal_places)
        y2_formatted = self.head.get_formatted_coord('y', decimal_places)
        string = '(%s, %s, %s, %s)' % (
            x1_formatted, y1_formatted, x2_formatted, y2_formatted)
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
        print '%s.%s: %s' % (cls.__name__, method_name, message)

    ###
if __name__ == '__main__':
    import doctest
    doctest.testfile('tests/line_test.txt')
