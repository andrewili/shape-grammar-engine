#   point.py


class Point(object):
        ### construct
    def __init__(self, x, y):
        """Receives 2 numbers
        Immutable
        """
        try:
            if not (
                (
                    x.__class__ == int or
                    x.__class__ == float
                ) and 
                (
                    y.__class__ == int or
                    y.__class__ == float
                )
            ):
                raise ValueError()
        except ValueError:
            print "You're trying to make a point with non-numbers"
        self.spec = (x, y)
        self.x = x
        self.y = y

    @classmethod
    def from_spec(cls, x, y):
        return Point(x, y)

        ### represent
    def __str__(self):
        string = '(%s, %s)' % (self.x, self.y)
        return string

    def listing(self, decimal_places=0):
        """Receives a number 
            num
        Returns a string of the form (x, y), where x and y have the specified
        number of decimal places
            String
        """
        # if decimal_places < 0:
        #     n = 0
        # else:
        #     n = int(decimal_places)
        # format = '%1.' + str(n) + 'f'
        # x_formatted = format % self.x
        # y_formatted = format % self.y
        x_formatted = self.get_formatted_coord('x')
        y_formatted = self.get_formatted_coord('y')
        string = '(%s, %s)' % (x_formatted, y_formatted)
        return string

    def get_formatted_coord(self, dimension, decimal_places=0):
        """Receives the dimension (i.e., x or y) of the coordinate and the 
        number of decimal places:
            String
            number
        Returns the specified coordinate formatted as specified
            String
        """
        try:
            if not (
                dimension == 'x' or 
                dimension == 'y'
            ):
                raise ValueError()
        except ValueError:
            print "You're specifying a dimension that is neither 'x' nor 'y'"   #   no output
        if decimal_places < 0:
            n = 0
        else:
            n = int(decimal_places)
        format = '%1.' + str(n) + 'f'
        if dimension == 'x':
            coord = self.x
        elif dimension == 'y':
            coord = self.y
        else:
            print 
                "This isn't supposed to happen,",
                "but you're specifying a dimension that is neither 'x' nor 'y'" #   no output
        formatted_coord = format % coord
        return formatted_coord

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

if __name__ == '__main__':
    import doctest
    doctest.testfile('tests/point_test.txt')
