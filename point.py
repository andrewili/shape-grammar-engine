#   point.py


class Point(object):
    def __init__(self, x, y):
        """Immutable
        """
        self.spec = (x, y)
        self.x = x
        self.y = y

    @classmethod
    def from_spec(cls, x, y):
        return Point(x, y)

        ### relations
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

        ### represent
    def __str__(self):
        string = '(%s, %s)' % (self.x, self.y)
        return string

    def listing(self, decimal_places=0):
        """Receives an integer
        """
        if decimal_places < 0:
            n = 0
        else:
            n = decimal_places
        format = '%1.' + str(n) + 'f'
        x_formatted = format % self.x
        y_formatted = format % self.y
        string = '(%s, %s)' % (x_formatted, y_formatted)
        # string = '(%3.1f, %3.1f)' % (self.x, self.y)
        return string


if __name__ == '__main__':
    import doctest
    doctest.testfile('tests/point_test.txt')
