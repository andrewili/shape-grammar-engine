import math
import numpy as np
almost_equal = np.allclose
tau = math.pi * 2

class FuzzyNumber(object):
    def __init__(self, number_in):
        """Receives:
            number_in       num
        """
        method_name = '__init__'
        try:
            if not self._is_a_number(number_in):
                raise TypeError
        except TypeError:
            message = "The argument must be a number"
            self.__class__._print_error_message(method_name, message)
        else:
            self.value = number_in

    def _is_a_number(self, x):
        """Receives:
            x               object
        Returns:
            value           boolean. True if x is an int, a float, an 
                            np.int64, or an np.float64. False otherwise
        """
        value = False
        if (type(x) == int or
            type(x) == float or
            type(x) == np.int64 or
            type(x) == np.float64
        ):
            value = True    
        return value

    def __eq__(self, other):
        return almost_equal(self.value, other.value)

    def __ge__(self, other):
        return (
            almost_equal(self.value, other.value) or
            self.value > other.value)

    def __gt__(self, other):
        if almost_equal(self.value, other.value):
            value = False
        elif self.value > other.value:
            value = True
        else:
            value = False
        return value

    def __le__(self, other):
        return(
            almost_equal(self.value, other.value) or
            self.value < other.value)

    def __lt__(self, other):
        if almost_equal(self.value, other.value):
            value = False
        elif self.value < other.value:
            value = True
        else:
            value = False
        return value

    def __ne__(self, other):
        return not almost_equal(self.value, other.value)

    ### utility
    @classmethod
    def _print_error_message(cls, method_name, message):
        print '%s.%s:\n    %s' % (cls.__name__, method_name, message)

    ### represent
    def __str__(self):
        return str(self.value)

if __name__ == '__main__':
    import doctest
    doctest.testfile('tests/fuzzy_number_test.txt')
