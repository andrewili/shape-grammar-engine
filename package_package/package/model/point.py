import numpy as np
import vector
# from package.scripts import settings

almost_equal = np.allclose

class Point(object):
    ### construct
    def __init__(self, x_in, y_in, z_in=0):
        """Receives:
            x_in            num
            y_in            num
            z_in            num
        Immutable?
        """
        method_name = '__init__'
        try:
            if not (
                self._is_a_number(x_in) and
                self._is_a_number(y_in) and
                self._is_a_number(z_in)
            ):
                raise TypeError
        except TypeError:
            message = 'The arguments must all be numbers'
            self._print_error_message(method_name, message)
        else:
            self.x = x_in
            self.y = y_in
            self.z = z_in
            self.matrix = np.array([self.x, self.y, self.z])
            self.spec = (self.x, self.y, self.z)

    @classmethod
    def from_spec(cls, spec):
        """Receives:
            spec            (num, ...) or [num, ...], 2 <= length <= 3
        Constructs a 3d Point with z = 0 as default. Returns:
            point           Point
        """
        method_name = 'from_spec'
        try:
            if not cls.is_a_spec_in(spec):
                raise TypeError
        except TypeError:
            message = (
                'The argument must be a tuple or a list of 2 or 3 numbers')
            cls._print_error_message(method_name, message)
        else:
            x = spec[0]
            y = spec[1]
            if len(spec) == 2:
                z = 0
            else:
                z = spec[2]
            point = Point(x, y, z)
            return point

    @classmethod
    def is_a_spec_in(cls, item):
        """Receives:
            item            any type
        Returns:
            value           boolean. True, if item is a list or tuple of 2 or 
                            3 numbers
        """
        value = False
        if (cls._is_an_iterable(item) and
            cls._contains_2_or_3_elements(item) and
            cls._contains_only_numbers(item)
        ):
            value = True
        return value

    @classmethod
    def is_a_spec(cls, item):
        """Receives:
            item            any type
        Returns:
            boolean         True, if item is a list or tuple of 3 numbers. 
                            False, otherwise
        """
        value = False
        if (cls._is_an_iterable(item) and
            len(item) == 3 and
            cls._contains_only_numbers(item)
        ):
            value = True
        return value

    @classmethod
    def _is_an_iterable(cls, item):
        value = (
            type(item) == tuple or
            type(item) == list)
        return value

    @classmethod
    def _contains_2_or_3_elements(cls, item):
        value = (
            len(item) == 2 or
            len(item) == 3)
        return value

    @classmethod
    def _contains_only_numbers(cls, elements):
        value = True
        for element in elements:
            if not cls._is_a_number(element):
                value = False
                break
        return value

    @classmethod
    def _is_a_number(cls, item):
        value = (
            type(item) == int or
            type(item) == float or
            type(item) == np.int64 or
            type(item) == np.float64)
        return value

    @classmethod
    def from_matrix(cls, matrix_in):
        """Receives:
            matrix_in       np.ndarray. Length = 3
        Returns:
            point           Point
        """
        method_name = 'from_matrix'
        try:
            if not (
                cls._is_an_array(matrix_in) and
                cls._contains_only_numbers(matrix_in)
            ):
                raise TypeError
            elif not cls._contains_3_elements(matrix_in):
                raise ValueError
        except TypeError:
            message = "The argument must be a matrix of numbers"
            cls._print_error_message(method_name, message)
        except ValueError:
            message = "The matrix must have shape (3, )"
            cls._print_error_message(method_name, message)
        else:
            x = matrix_in[0]
            y = matrix_in[1]
            z = matrix_in[2]
            point = Point(x, y, z)
            return point

    @classmethod
    def _is_an_array(cls, item):
        value = (type(item) == np.ndarray)
        return value

    @classmethod
    def _contains_3_elements(cls, matrix):
        value = (len(matrix) == 3)
        return value

    ### represent
    def __str__(self):
        string = '(%s, %s, %s)' % (self.x, self.y, self.z)
        return string

    def __repr__(self):
        string = 'point.Point(%s, %s, %s)' % (
            self.x,
            self.y,
            self.z)
        return string

    def listing(self, decimal_places=0):
        """Receives:
            decimal_places  int. An integer >= 0
        Returns:
            listing         str. In the form '(<x>, <y>, <z>)', where x, y, 
                            and z have the specified number of decimal 
                            places, if successful. None otherwise
        """
        method_name = 'listing'
        try:
            if not type(decimal_places) == int:
                raise TypeError
            elif not decimal_places >= 0:
                raise ValueError
        except TypeError:
            message = "The argument must be an integer"
            self._print_error_message(method_name, message)
            value = None
        except ValueError:
            message = "The argument must be non-negative"
            self._print_error_message(method_name, message)
            value = None
        else:
            n = decimal_places
            x_listing = self.get_coord_listing('x', n)
            y_listing = self.get_coord_listing('y', n)
            z_listing = self.get_coord_listing('z', n)
            listing = '(%s, %s, %s)' % (x_listing, y_listing, z_listing)
            value = listing
        finally:
            return value

    def get_coord_listing(self, dimension, decimal_places=0):
        """Receives: 
            dimension       str. 'x', 'y', or 'z'
            decimal_places  int. The number of decimal places to include
        Types are guaranteed by the calling method. Returns:
            coord_listing   str. A number with the specified number of 
                            decimal places
        """
        n = decimal_places
        format = '%1.' + str(n) + 'f'
        if dimension == 'x':
            coord = self.x
        elif dimension == 'y':
            coord = self.y
        elif dimension == 'z':
            coord = self.z
        else:
            print("We shouldn't have gotten here")
        coord_listing = format % coord
        return coord_listing

    ### operations
    def __add__(self, v):
        """Receives:
            v               Vector
        Finds self + v. Returns:
            p2              Point
        """
        method_name = '__add__'
        try:
            if not type(v) == vector.Vector:
                raise TypeError
        except TypeError:
            message = "The argument must be a Vector"
            self._print_error_message(method_name, message)
        else:
            matrix2 = self.matrix + v.matrix
            p2 = Point.from_matrix(matrix2)
            return p2

    def __sub__(self, other):
        """Receives:
            other           Point
        Finds self - other. Returns:
            diff_vector     Vector
        """
        method_name = '__sub__'
        try:
            if not type(other) == Point:
                raise TypeError
        except TypeError:
            message = 'The argument must be a Point object'
            self._print_error_message(method_name, message)
        else:
            diff_matrix = self.matrix - other.matrix
            diff_vector = vector.Vector.from_matrix(diff_matrix)
            return diff_vector

    ### relations
    def __eq__(self, other):
        value = almost_equal(self.spec, other.spec)
        return value

    def __ge__(self, other):
        value = (
            almost_equal(self.spec, other.spec) or
            self.spec > other.spec)
        return value

    def __gt__(self, other):
        if almost_equal(self.spec, other.spec):
            value = False
        elif self.spec > other.spec:
            value = True
        else:
            value = False
        return value

    def __le__(self, other):
        value = (
            almost_equal(self.spec, other.spec) or
            self.spec < other.spec)
        return value

    def __lt__(self, other):
        if almost_equal(self.spec, other.spec):
            value = False
        elif self.spec < other.spec:
            value = True
        else:
            value = False
        return value

    def __ne__(self, other):
        value = not almost_equal(self.spec, other.spec)
        return value

    def __hash__(self):
        """Returns:
            value           int
        """
        n_digits = 14                           ##  relocate to settings
        list_rounded = [round(coord, n_digits) for coord in self.spec]
        triple_rounded = tuple(list_rounded)
        value = hash(triple_rounded)
        return value

    @classmethod
    def _print_error_message(cls, method_name, message):
        print '%s.%s:\n    %s' % (cls.__name__, method_name, message)

if __name__ == '__main__':
    import doctest
    doctest.testfile('tests/point_test.txt')
