from numpy import linalg as la
import math
import numpy as np

almost_equal = np.allclose
TAU = math.pi * 2

class Vector(object):
    def __init__(self, x_in, y_in, z_in=0):
        method_name = '__init__'
        try:
            if not (
                self._is_a_number(x_in) and
                self._is_a_number(y_in) and
                self._is_a_number(z_in)
            ):
                raise TypeError
        except TypeError:
            message = "The arguments must be numbers"
            self.__class__._print_error_message(method_name, message)
        else:
            num = north_unit_matrix = np.array([0, 1, 0, 0])
            self.x = x_in
            self.y = y_in
            self.z = z_in
            self.matrix = np.array([x_in, y_in, z_in, 0])
            self.length = la.norm(self.matrix)
            if self.length == 0:
                self.unit_matrix = None
                self.bearing = None
                self.bearing_in_degrees = None
            else:
                self.unit_matrix = self.matrix / self.length
                self.bearing = self._find_bearing(self.unit_matrix)
                self.bearing_in_degrees = math.degrees(self.bearing)

    def _is_a_number(self, x):
        """Receives:
            x               object
        Returns:
            value           boolean. True if x is an int, a float, an 
                            np.int64, or an np.float64. False otherwise
        """
        value = False
        if (
            type(x) == int or
            type(x) == float or
            type(x) == np.int64 or
            type(x) == np.float64
        ):
            value = True    
        return value

    @classmethod
    def _find_bearing(cls, unit_matrix):
        """Receives:
            unit_matrix     np.array, shape = (3, ), norm = 1
        Finds the angle (in radians) from north. Clockwise is positive. 
        Returns:
            bearing         num. 0 <= num < TAU
        """
        method_name = '_find_bearing'
        num = north_unit_matrix = np.array([0, 1, 0, 0])
        try:
            if not type(unit_matrix) == np.ndarray:
                raise TypeError
        except TypeError:
            message = "The argument must be an np.array"
            cls._print_error_message(method_name, message)
        else:
            absolute_bearing = math.acos(np.dot(num, unit_matrix))
            x, y = unit_matrix[0], unit_matrix[1]
            if (almost_equal(x, 0) and
                almost_equal(y, 0)
            ):
                bearing = None
            elif (
                almost_equal(x, 0) and
                almost_equal(y, -1)
            ):
                bearing = TAU / 2
            elif (
                almost_equal(x, 0) and
                almost_equal(y, 1)
            ):
                bearing = 0
            elif x < 0:
                bearing = TAU - absolute_bearing
            elif x > 0:
                bearing = absolute_bearing
            else:
                bearing = None
            return bearing

    @classmethod
    def from_matrix(cls, matrix_in):
        """Receives:
            matrix_in       array([num, num, num, 0])
        Returns:
            vector_out      Vector
        """
        method_name = 'from_matrix'
        try:
            if not (
                type(matrix_in) == np.ndarray and
                matrix_in.shape == (4, )
            ):
                raise TypeError
            elif not matrix_in[3] == 0:
                raise ValueError
        except TypeError:
            message = 'The argument must be a matrix of shape (4, )'
            cls._print_error_message(method_name, message)
        except ValueError:
            message = "The final element of the matrix must be 0"
            cls._print_error_message(method_name, message)
        else:
            x, y, z = matrix_in[0], matrix_in[1], matrix_in[2]
            vector_out = Vector(x, y, z)
            return vector_out

    ### operations and relations

    ### utility
    @classmethod
    def _print_error_message(cls, method_name, message):
        print '%s.%s:\n    %s' % (cls.__name__, method_name, message)

    ### represent
    def __str__(self):
        string = str(self.matrix)
        return string

if __name__ == '__main__':
    import doctest
    doctest.testfile('tests/vector_test.txt')






























