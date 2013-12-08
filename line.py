#   line.py

import math
import sg_point


class Line(object):
        ### construct
    def __init__(self, p1, p2):
        #   2D implementation
        try:
            if p1 == p2:
                raise ValueError()
        except ValueError:
            print "You're trying to create a zero-length line"
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
        p1 = sg_point.SGPoint(x1, y1)
        p2 = sg_point.SGPoint(x2, y2)
        line = Line(p1, p2)
        return line

    @classmethod
    def from_short_spec(cls, x1, x2):
        line = Line.from_spec(x1, x1, x2, x2)
        return line
##        pass

    @classmethod
    def from_points(cls, p1, p2):
        return Line(p1, p2)

        ### represent
    def __str__(self):
        return '(%s, %s, %s, %s)' % (
            self.x1, self.y1, self.x2, self.y2)

    def listing(self):
        return '(%0.1f, %0.1f, %0.1f, %0.1f)' % (
            self.x1, self.y1, self.x2, self.y2)

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

    def is_a_subline_in_column(self, column):
        """Receives a column:
            SGColumn
        Returns whether self is a subline of a line in the column
        """
        for other_line in column.lines:
            if self.is_a_subline_of(other_line):
                return True
        return False

##    def is_a_subline_in_column(self, column):
##        """Receives a column:
##            [Line, ...]
##        Returns whether self is a subline of a line in the column
##        """
##        for other_line in column:
##            if self.is_a_subline_of(other_line):
##                return True
##        return False

    def is_a_subline_of(self, other):
        if self.tail < other.tail:
            return False
        else: # self.tail >= other.tail:
            if self.head <= other.head:
                return True
            else:
                return False

    def is_disjoint_left_of(self, other):           #   assumes horizontal line
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

        ### called by SGShape.subtract_line_column(line_minuend, column)

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

        ###
if __name__ == '__main__':
    import doctest
    doctest.testfile('tests/line_test.txt')
