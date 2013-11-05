#   sg_point.py
#   2013-10-04
#   Extends 2013-09-24


class SGPoint(object):
    #   Immutable
    def __init__(self, x, y):
        self.spec = (x, y)
        self.x = x
        self.y = y

    @classmethod
    def from_spec(cls, x, y):
        return SGPoint(x, y)

        ####
    def __eq__(self, other):
        return self.spec == other.spec

    def __ge__(self, other):
        return self.spec >= other.spec

    def __gt__(self, other):
        return self.spec > other.spec

    def __le__(self, other):
        return self.spec <= other.spec

    def __lt__(self, other):
        return self.spec < other.spec

    def __ne__(self, other):
        return self.spec != other.spec

        ####
    def __str__(self):
        string = '(%3.1f, %3.1f)' % (self.x, self.y)
        return string

    def listing(self):
        string = '(%3.1f, %3.1f)' % (self.x, self.y)
        return string


if __name__ == '__main__':
    import doctest
    doctest.testfile('sg_point_test.txt')
