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

    @classmethod                                ###
    def new_from_drv_text_lines(cls, text_lines_in):
        """Receives the text lines of the derivation record of a drv file:
            [str, ...]
        Returns:
            Derivation
        """
        (   initial_shape_text_lines,
            rules_text_lines,
            next_shapes_text_lines
        ) = self._get_sorted_drv_text_lines(text_lines_in)
        initial_shape = shape.Shape.new_from_is_text_lines(
            initial_shape_text_lines)
        rules = self._make_rules_from_text_lines(rules_text_lines)
        next_shapes = self._make_next_shapes_from_text_lines(
            next_shapes_text_lines)
        new_derivation = Derivation(initial_shape, rules, next_shapes)
        return new_derivation

    @classmethod                                ###
    def _get_sorted_drv_text_lines(cls, text_lines_in):
        """Returns a 3-tuple of text line lists for the initial shape, the 
        rules, and the next shapes:
            (   [<initial-shape-text-line>, ...],
                [<rule-text-line>, ...],
                [<next-shape-line>, ...])
        """
        initial_shape_text_lines = []
        rules_text_lines = []
        next_shape_text_lines = []
        for line in text_lines_in:
            if 
        drv_text_line_tuple = (
            initial_shape_text_lines,
            rules_text_lines,
            next_shape_text_lines)
        return drv_text_line_tuple

    @classmethod                                ###
    def _make_rules_from_text_lines(cls):
        """
        """
        pass

    @classmethod                                ###
    def _make_next_shapes_from_text_lines(cls):
        """
        """
        pass


    def get_final_shape(self):
        """Returns the final shape in the derivation:
            Shape
        """
        final_shape = self.next_shapes.pop()
        return final_shape

    def __str__(self):                          ###
        """Returns a string in the drv format:
            str
        """
        drv_header = (
            '# derivation file version 1.00' + 
            '                           ' + 
            '--chen liang 2007/08/06')
        blank_line = ''
        grammar_string = self._make_grammar_string()
        deriv_record_string = self._make_deriv_record_string()
        drv_string_parts = [
            drv_header,
            blank_line,
            grammar_string,
            deriv_record_string
        ]
        drv_string = '\n'.join(drv_string_parts)
        return drv_string

    def _make_grammar_string(self):             ###
        """Returns a (formatted) string containing the grammar part of the 
        drv file:
            <shape: initial or rule>
            ...
            <initial shape>
            <rule rule-name rule_L rule_R>
            ...
        """
        # shape_strings = self._make_shape_strings()
        # initial_shape_name_string = self.initial_shape.make_name_string()
        # rule_summary_strings = self._make_rule_summary_strings()
        # grammar_string_parts = [
        #     shape_strings,
        #     initial_shape_name_string,
        #     rule_summary_strings]
        # grammar_string = '\n'.join(grammar_string_parts)
        # return grammar_string
        pass

    def _make_shape_strings(self):              ###
        """Returns an ordered list of shape strings (i.e., initial shape and 
        rule shapes) in is format:
            [<shape string>, ...]
        """
        # all_shapes = self.next_shapes.append(self.initial_shape)
        # shape_strings = [shape.__str__() for shape in all_shapes]
        # return sorted(shape_strings)
        pass

    def _make_rule_summary_strings(self):       ###
        pass

    def _make_rules_string(self):               ###
        """Returns the rules part of the drv file:
            <rule_L>
            <rule_R>
            ...
            <rule>
            ...
        """
        # rule_strings = [rule.__str__() for rule in self.rules]
        # rules_string = '\n'.join(rule_strings)
        # return rules_string
        pass

    def __repr__(self):
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
        joined_repr_parts = ', '.join(repr_parts)
        repr_string = '(%s)' % joined_repr_parts
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
        next_shape_reprs = [
            next_shape.__repr__() for next_shape in self.next_shapes]
        joined_next_shape_reprs = ', '.join(next_shape_reprs)
        repr_string = '[%s]' % joined_next_shape_reprs
        return repr_string

if __name__ == '__main__':
    import doctest
    doctest.testfile('tests/derivation_test.txt')
