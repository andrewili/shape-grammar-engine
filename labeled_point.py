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
        method_name = '__init__()'
        try:
            if not label.__class__ == str:
                raise TypeError
            elif label == '':
                raise ValueError
        except TypeError:
            message = 'The label must be a string'
            self._print_error_message(method_name, message)
        except ValueError:
            message = 'The label must be non-empty'
            self._print_error_message(method_name, message)
        else:
            self.x = x
            self.y = y
            self.label = label
            self.spec = (x, y, label)
            self.point = point.Point(x, y)

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

    ### other
    def _print_error_message(self, method_name, message):
        print '%s.%s: %s' % (self.__class__.__name__, method_name, message)

if __name__ == '__main__':
    import doctest
    doctest.testfile('tests/labeled_point_test.txt')
