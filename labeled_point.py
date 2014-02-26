#   labeled_point.py

import point


class LabeledPoint(object):
    """Contains a Point and a label
    """
        ### construct
    def __init__(self, x, y, label):
        """Receives 2 coordinates and a non-empty label:
            num, num, String
        2D implementation. Immutable
        """
        try:
            if not label.__class__ == str:
                raise TypeError
            elif label == '':
                raise ValueError
        except TypeError:
            print '%s %s' % (
                "You're trying to make a labeled point",
                "with a non-string label")
        except ValueError:
            print "You're trying to make a labeled point with an empty label"
        else:
            self.spec = (x, y, label)
            self.point = point.Point(x, y)
            self.x = x
            self.y = y
            self.label = label

        ### represent
    def __str__(self):
        string = '(%s, %s, %s)' % (self.x, self.y, self.label)
        return string

    def listing(self, decimal_places=0):
        point_listing = self.point.listing(decimal_places)
        point_formatted = point_listing[1:-1]
        string = '(%s, %s)' % (point_formatted, self.label)
        return string

        ### relations
    def __eq__(self, other):
        if (self.point == other.point and
            self.label == other.label
        ):
            return True
        else:
            return False

    def __ge__(self, other):
        if self.point > other.point:
            return True
        elif self.point == other.point:
            if self.label > other.label:
                return True
            elif self.label == other.label:
                return True
            else:
                return False
        else:
            return False

    def __gt__(self, other):
        if self.point > other.point:
            return True
        elif self.point == other.point:
            if self.label > other.label:
                return True
            else:
                return False
        else:
            return False

    def __le__(self, other):
        if self.point < other.point:
            return True
        elif self.point == other.point:
            if self.label < other.label:
                return True
            if self.label == other.label:
                return True
            else:
                return False
        else:
            return False

    def __lt__(self, other):
        if self.point < other.point:
            return True
        elif self.point == other.point:
            if self.label < other.label:
                return True
            else:
                return False
        else:
            return False

    def __ne__(self, other):
        if (self.point != other.point or
            self.label != other.label
        ):
            return True
        else:
            return False

if __name__ == '__main__':
    import doctest
    doctest.testfile('tests/labeled_point_test.txt')
