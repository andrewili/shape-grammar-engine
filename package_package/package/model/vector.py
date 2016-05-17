from numpy import linalg as la
import math
import numpy as np

almost_equal = np.allclose
TAU = math.pi * 2

class Vector(object):
    def __init__(self, x_in, y_in, z_in=0):
        """Receives:
            x_in            num
            y_in            num
            z_in            num
        Mutable? Immutable?
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
            message = "The arguments must be numbers"
            self._print_error_message(method_name, message)
        else:
            num = north_unit_matrix = np.array([0, 1, 0])
            self.x = x_in
            self.y = y_in
            self.z = z_in
            self.m = self.matrix = np.array([x_in, y_in, z_in])
            self.l = self.length = la.norm(self.m)
            if self.l == 0:
                self.um = self.unit_matrix = None
            else:
                self.um = self.unit_matrix = self.m / self.l
                #   creating a unit vector starts an infinite regress

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
    def from_matrix(cls, matrix_in):
        """Receives:
            matrix_in       array([num, num, num])
        Returns:
            vector_out      Vector
        """
        method_name = 'from_matrix'
        try:
            if not (
                type(matrix_in) == np.ndarray and
                matrix_in.shape == (3, )
            ):
                raise TypeError
        except TypeError:
            message = 'The argument must be a matrix of shape (3, )'
            cls._print_error_message(method_name, message)
        else:
            x, y, z = matrix_in[0], matrix_in[1], matrix_in[2]
            vector_out = Vector(x, y, z)
            return vector_out

    ### represent
    def __str__(self):
        string = str(self.matrix)
        return string

    def __repr__(self):
        """Returns:
            string          str. In the form '[<x>, <y>, <z>]'
        """
        string = 'vector.%s(%s, %s, %s)' % (
            self.__class__.__name__,
            self.x,
            self.y,
            self.z)
        return string

    def listing(self, decimal_places=0):
        """Returns:
            string          str. In the form 
                            [<x_listing> <y_listing> <z_listing>]
        """
        n = decimal_places
        x_listing = self._get_element_listing(self.x, n)
        y_listing = self._get_element_listing(self.y, n)
        z_listing = self._get_element_listing(self.z, n)
        string = '[%s %s %s]' % (x_listing, y_listing, z_listing)
        return string

    def _get_element_listing(self, element, decimal_places=0):
        n = decimal_places
        format = '%1.' + str(n) + 'f'
        string = format % element
        return string

    ### operations
    def find_unit_vector(self):
        """Returns:
            uv              Vector. The unit vector of v, if length > 0. None 
                            otherwise
        """
        if self.l == 0:
            uv = None
        else:
            uv = Vector.from_matrix(self.um)
        return uv

    uv = find_unit_vector

    def find_additive_inverse(self):
        """Returns:
            v_inv           Vector. The inverse of v
        """
        v000 = Vector(0, 0, 0)
        v_inv = v000 - self
        return v_inv

    inv = find_additive_inverse

    def __add__(self, other):
        """Receives:
            other           Vector
        Returns:
            v_sum           Vector. The sum of self and other
        """
        x_sum = self.x + other.x
        y_sum = self.y + other.y
        z_sum = self.z + other.z
        v_sum = Vector(x_sum, y_sum, z_sum)
        return v_sum

    def __sub__(self, other):
        """Receives:
            other           Vector
        Returns:
            v_diff          Vector. The difference other - self
        """
        x_diff = self.x - other.x
        y_diff = self.y - other.y
        z_diff = self.z - other.z
        v_diff = Vector(x_diff, y_diff, z_diff)
        return v_diff

    def __mul__(self, num):
        """Receives:
            num             number
        Finds the product of self * num. Returns:
            v2              Vector
        """
        m2 = self.matrix * num
        v2 = Vector.from_matrix(m2)
        return v2

    ### relations
    def __eq__(self, other):
        value = almost_equal(self.matrix, other.matrix)
        return value

    def __ge__(self, other):
        value = False
        self_tuple = (self.x, self.y, self.z)
        other_tuple = (other.x, other.y, other.z)
        if (almost_equal(self_tuple, other_tuple) or
            self_tuple > other_tuple
        ):
            value = True
        return value

    def __gt__(self, other):
        value = False
        self_tuple = (self.x, self.y, self.z)
        other_tuple = (other.x, other.y, other.z)
        if (not almost_equal(self_tuple, other_tuple) and
            self_tuple > other_tuple
        ):
            value = True
        return value

    def __le__(self, other):
        value = False
        self_tuple = (self.x, self.y, self.z)
        other_tuple = (other.x, other.y, other.z)
        if (almost_equal(self_tuple, other_tuple) or
            self_tuple < other_tuple
        ):
            value = True
        return value

    def __lt__(self, other):
        value = False
        self_tuple = (self.x, self.y, self.z)
        other_tuple = (other.x, other.y, other.z)
        if (not almost_equal(self_tuple, other_tuple) and
            self_tuple < other_tuple
        ):
            value = True
        return value

    def __ne__(self, other):
        value = not almost_equal(self.matrix, other.matrix)
        return value

    def __hash__(self):
        hash_x = hash(self.x)
        hash_y = hash(self.y)
        hash_z = hash(self.z)
        value = hash((hash_x, hash_y, hash_z))
        return value

    ### utility
    @classmethod
    def _print_error_message(cls, method_name, message):
        print '%s.%s:\n    %s' % (cls.__name__, method_name, message)

if __name__ == '__main__':
    import doctest
    doctest.testfile('tests/vector_test.txt')
