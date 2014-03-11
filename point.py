#   point.py


class Point(object):
        ### construct
    def __init__(self, x, y):
        """Receives 2 numbers
        Immutable
        """
        # self.class_name = self.__class__.__name__
        method_name = '__init__()'
        try:
            if not (
                self._is_number(x) and
                self._is_number(y)
            ):
                raise TypeError
        except TypeError:
            message = 'The arguments must both be numbers'
            self.__class__._print_error_message(method_name, message)
        else:
            self.x = x
            self.y = y
            self.spec = (x, y)

    def _is_number(self, item):
        value = (
            item.__class__ == int or
            item.__class__ == float)
        return value

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
        x_formatted = self.get_formatted_coord('x', decimal_places)
        y_formatted = self.get_formatted_coord('y', decimal_places)
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
        method_name = 'get_formatted_coord()'
        try:
            if not dimension.__class__ == str:
                raise TypeError
            elif not (
                dimension == 'x' or
                dimension == 'y'
            ):
                raise ValueError
        except TypeError:
            message = "The dimension must be a string ('x' or 'y')"
            self.__class__._print_error_message(method_name, message)
        except ValueError:
            message = "The dimension must be either 'x' or 'y'"
            self.__class__._print_error_message(method_name, message)
        else:
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
                print '%s %s' % "We shouldn't have gotten here"
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

    ### other
    @classmethod
    def _print_error_message(cls, method_name, message):
        print '%s.%s: %s' % (cls.__name__, method_name, message)

if __name__ == '__main__':
    import doctest
    doctest.testfile('tests/point_test.txt')
