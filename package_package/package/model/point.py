class Point(object):

    ### construct
    def __init__(self, spec):
        """Receives:
            spec            (num, num, num=0)
        Immutable
        """
        method_name = '__init__'
        try:
            if not self._is_point_spec(spec):
                raise TypeError
        except TypeError:
            message = 'The argument must be a 2- or 3-tuple of numbers'
            self.__class__._print_error_message(method_name, message)
        else:
            if len(spec) == 2:
                self.x, self.y = spec
                self.z = 0
            else:
                self.x, self.y, self.z = spec
            self.spec = (self.x, self.y, self.z)

    def _is_point_spec(self, item):
        """Receives:
            item            any type
        Returns:
            boolean         True, if item is of the form (num, num) or
                            (num, num, num)
                            False, otherwise
        """
        if not (
            len(item) == 2 or
            len(item) == 3
        ):
            value = False
        elif not self._contains_only_numbers(item):
            value = False
        else:
            value = True
        return value

    def _contains_only_numbers(self, elements):
        value = True
        for element in elements:
            if not self._is_number(element):
                value = False
                break
        return value

    def _is_number(self, item):
        value = (
            item.__class__ == int or
            item.__class__ == float)
        return value

    @classmethod
    def from_coords(cls, x, y, z=0):
        method_name = 'from_coords'
        new_spec = (x, y, z)
        new_point = Point(new_spec)
        return new_point

    ### represent
    def __str__(self):
        string = '(%s, %s, %s)' % (self.x, self.y, self.z)
        return string

    def __repr__(self):
        string = "(%s, %s, %s)" % (self.x, self.y, self.z)
        return string

    def listing(self, decimal_places=0):
        """Receives:
            decimal_places  int >= 0
        Returns:
            string          (x, y, z), where x, y, and z have the specified 
                            number of decimal places
        """
        method_name = 'listing'
        try:
            if not decimal_places.__class__ == int:
                raise TypeError
            elif not decimal_places >= 0:
                raise ValueError
        except TypeError:
            message = 'The argument must be an integer'
            self.__class__._print_error_message(method_name, message)
        except ValueError:
            message = 'The argument must be non-negative'
            self.__class__._print_error_message(method_name, message)
        else:
            x_formatted = self.get_formatted_coord('x', decimal_places)
            y_formatted = self.get_formatted_coord('y', decimal_places)
            z_formatted = self.get_formatted_coord('z', decimal_places)
            string = '(%s, %s, %s)' % (x_formatted, y_formatted, z_formatted)
            return string

    def get_formatted_coord(self, dimension, decimal_places=0):
        """Receives the dimension (i.e., x, y, or z) of the coordinate and the 
        number of decimal places:
            String
            number
        Returns the specified coordinate formatted as specified
            String
        """
        method_name = 'get_formatted_coord'
        try:
            if not dimension.__class__ == str:
                raise TypeError
            elif not (
                dimension == 'x' or
                dimension == 'y' or
                dimension == 'z'
            ):
                raise ValueError
        except TypeError:
            message = "The dimension must be a string ('x', 'y', or 'z')"
            self.__class__._print_error_message(method_name, message)
        except ValueError:
            message = "The dimension must be either 'x', 'y', or 'z'"
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
            elif dimension == 'z':
                coord = self.z
            else:
                print '%s %s %s' % "We shouldn't have gotten here"
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
    def is_point_spec(cls, item):
        """Receives:
            item
        Returns:
            boolean             True, if item is a point spec
                                False, otherwise
        """
        value = (
            type(item) == tuple and
            len(item) == 3 and
            cls._elements_are_numbers(item)
        )
        return value

    @classmethod
    def _elements_are_numbers(cls, elements):
        """Receives:
            elements        3-tuple
        Returns:
            boolean         True, if each element in elements is a float or 
                            integer
                            False, otherwise
        """
        value = True
        for element in elements:
            if not (
                type(element) == int or
                type(element) == float 
            ):
                value = False
                break
        return value

    @classmethod
    def _print_error_message(cls, method_name, message):
        print '%s.%s:\n    %s' % (cls.__name__, method_name, message)

if __name__ == '__main__':
    import doctest
    doctest.testfile('tests/point_test.txt')
