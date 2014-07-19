#   derivation.py

import rule
import shape

class Derivation(object):
    def __init__(self, initial_shape, rules, next_shapes):
        """Receives:
            Shape
            [Rule, ...]
            [Shape, ...]
        """
        try:
            if not (
                type(initial_shape) == shape.Shape and
                type(rules) == list and
                type(next_shapes) == list
            ):
                raise TypeError
            for item in rules:
                if not type(item) == rule.Rule:
                    raise TypeError
            for item in next_shapes:
                if not type(item) == shape.Shape:
                    raise TypeError
        except TypeError:
            message = '%s%s' % (
                "The arguments must be a shape, ", 
                "a list of rules, and a list of shapes")
            print(message)
        else:
            self.initial_shape = initial_shape
            self.rules = rules
            self.next_shapes = next_shapes

    # def __init__(self, shape_rule_list):    #   to do
    #     """Receives a list of alternating shapes and rules:
    #         [Shape, Rule, Shape, Rule, ..., Shape]
    #     # What about arguments initial_shape, rules, next_shapes?
    #     """
    #     try:
    #         if not (
    #             type(shape_rule_list) == list and
    #             type(even_item) == shape.Shape and
    #             type(odd_item) == rule.Rule
    #         ):
    #             raise TypeError
    #         if not self._is_odd(len(shape_rule_list)):
    #             raise ValueError
    #     except TypeError:
    #         message = (
    #             'The argument must be a list of alternating shapes and rules')
    #         print(message)
    #     except ValueError:
    #         message = (
    #             'ValueError message')
    #     else:
    #         self.shape_rule_list = shape_rule_list

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
        """Returns an (unformatted) string in the form:
            <initial shape>,
            <rules>,
            <next shapes>
        """
        rules_repr = self._make_rules_repr()
        next_shapes_repr = self._make_next_shapes_repr()
        repr_parts = [
            self.initial_shape.__repr__(),
            rules_repr,
            next_shapes_repr]
        repr_string = '\n'.join(repr_parts)
        return repr_string

    def _make_rules_repr(self):
        """Returns an (unformatted) string in the form:
            [<rule>, ...]
        """
        rule_reprs = [rule.__repr__() for rule in self.rules]
        joined_rule_reprs = ', '.join(rule_reprs)
        repr_string = '[%s]' % joined_rule_reprs
        return repr_string

    def _make_next_shapes_repr(self):
        """Returns an (unformatted) string in the form:
            [<shape>, ...]
        """
        pass

if __name__ == '__main__':
    import doctest
    doctest.testfile('tests/derivation_test.txt')
