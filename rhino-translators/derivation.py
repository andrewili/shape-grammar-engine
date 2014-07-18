#   derivation.py

import rule
import shape

class Derivation(object):
    def __init__(self, shape_rule_list):    #   to do
        """Receives a list of alternating shapes and rules:
            [Shape, Rule, Shape, Rule, ..., Shape]
        """
        try:
            if not (
                type(shape_rule_list) == list and
                type(even_item) == shape.Shape and
                type(odd_item) == rule.Rule
            ):
                raise TypeError
            if not self._is_odd(len(shape_rule_list)):
                raise ValueError
        except TypeError:
            message = (
                'The argument must be a list of alternating shapes and rules')
            print(message)
        except ValueError:
            message = (
                'ValueError message')
        else:
            self.shape_rule_list = shape_rule_list

    @classmethod                        #   to do
    def new_from_drv_text_lines(cls, text_lines_in):
        """Receives the text lines of the derivation record of a drv file:
            [str, ...]
        Returns:
            Derivation
        """
        pass

    def get_final_shape(self):          #   to do
        """Returns the final shape in the derivation:
            Shape
        """
        pass

    def __str__(self):                  #   to do
        """
        """
        return 'kilroy str'

    def __repr__(self):                 #   to do
        """
        """
        return 'kilroy repr'

if __name__ == '__main__':
    import doctest
    doctest.testfile('tests/derivation_test.txt')
