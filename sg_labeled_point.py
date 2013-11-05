#   sg_labeled_point.py
#   2013-10-04. Extends 2013-09-24

import sg_point


class SGLabeledPoint(object):
    #   Immutable
    def __init__(self, x, y, label):
        #   Label must be non-empty.
        try:
            if label == '':
                raise ValueError()
        except ValueError:
            print "You're trying to create a labeled point with an empty label"
        self.spec = (x, y, label)
        self.point = sg_point.SGPoint(x, y)
        self.x = x
        self.y = y
        self.label = label

        ####
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

        ####
    def __str__(self):
        string = '(%3.1f, %3.1f, %s)' % (self.x, self.y, self.label)
        return string

if __name__ == '__main__':
    import doctest
    doctest.testfile('sg_labeled_point_test.txt')
