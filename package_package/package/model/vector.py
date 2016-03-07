from numpy import linalg as la
import math
import numpy as np

class Vector(object):
    def __init__(self, x_in, y_in, z_in=0):     ##  2016-03-06 06:47
        method_name = '__init__'
        try:
            if not (
                self._is_a_number(x_in) and
                self._is_a_number(y_in) and
                self._is_a_number(z_in)
            ):
                raise TypeError
        except TypeError:
            message = 'The arguments must be numbers'
            self.__class__._print_error_message(method_name, message)
        else:
            self.matrix = np.array([x_in], [y_in], [z_in])
            # self.matrix = np.array([[x_in], [y_in], [z_in], [0]])
            self.x = self.matrix[0][0]
            self.y = self.matrix[1][0]
            self.z = self.matrix[2][0]
            self.length = la.norm(self.matrix)
            self.dir = self.direction_matrix = self.matrix / self.length
            self.bearing_from_x = self._find_bearing(self.dir)
            # self.bearing_from_y = self._find_bearing_from_y(self.dir)
            
            # self.bearing_from_x = math.degrees(math.acos(self.dir[0]))
            # self.bearing_from_y = math.degrees(math.asin(self.dir[1]))
            # print('(x, y, z) = (%s, %s, %s)' % (self.x, self.y, self.z))
            # print('length = s' % self.length)
            # print('dir =\n%s' % self.dir)
            # print('bearing from x = ' % self.bearing_from_x)
            # print('bearing from y = ' % self.bearing_from_y)
            # self.bearing = math.degrees(math.asin(self.y / self.length))
                #   clockwise from north

    def _is_a_number(self, x):
        """Receives:
            x               object
        Returns:
            value           boolean. True if x is a float, an np.int64 or an 
                            int. False otherwise
        """
        value = False
        if (type(x) == float or
            type(x) == np.int64 or
            type(x) == int
        ):
            value = True    
        return value

    def _find_bearing(self, dir_matrix):        ##  2016-03-05 15:23
        """Receives:
            dir_matrix      np.ndarray. A direction matrix
        Finds the bearing in degrees (clockwise positive from north), using 
        the mean of both the x- and the y-elements. Returns:
            angle           float. 
        """
        x = dir_matrix[0]
        y = dir_matrix[1]
        angle_x = math.degrees(math.asin(x))
        angle_y = math.degrees(math.acos(y))
        angle = (angle_x + angle_y) / 2.0
        return angle

    @classmethod                                ##  2016-03-03 11:41
    def from_matrix(cls, matrix_in):
        """Receives:
            matrix_in       array. The array contains 4 x 1 elements, and the 
                            final element is 0
        Returns:
            vector_out      Vector
        """
        method_name = 'from_matrix'
        try:
            if not type(matrix_in) == np.ndarray:
                raise TypeError
            elif not (
                matrix_in.shape == (4, 1) and
                matrix_in[3] == np.array([0])
            ):
                raise ValueError
        except TypeError:
            message = 'The argument must be a matrix'
            cls._print_error_message(method_name, message)
        except ValueError:
            message = '%s %s' % (
                "The matrix must have shape (4, 1)", 
                "and the final element must be array([0])"
            )
            cls._print_error_message(method_name, message)
        else:
            x, y, z = matrix_in[0][0], matrix_in[1][0], matrix_in[2][0]
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
