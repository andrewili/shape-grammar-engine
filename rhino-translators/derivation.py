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

    @classmethod
    def new_from_drv_text_lines(cls, drv_text_lines):
        """Receives the text lines of a drv file:
            [<drv-text-line>, ...]
        Returns:
            Derivation
        """
        grammar_shapes = []
        grammar_rules = []
        derivation_rules = []
        next_shapes = []
        # initial_shape = None
        shape_text_lines = []
        for text_line in drv_text_lines:
            tokens = text_line.split()
            if tokens == []:
                pass
            else:
                first_token = tokens[0]
                if first_token == '#':
                    if tokens[2] == 'file':
                        subfile = 'grammar'
                    elif tokens[2] == 'record':
                        subfile = 'derivation'
                    else:
                        pass
                #   grammar shapes
                elif (
                    first_token == 'shape' and
                    subfile == 'grammar'        ##  grammar record
                ):
                    new_grammar_shape = (
                        shape.Shape.new_from_is_text_lines(shape_text_lines))
                    grammar_shapes.append(new_grammar_shape)
                    shape_text_lines = [tokens] ##  start new shape
                elif first_token == 'name':
                    shape_text_lines.append(tokens)
                elif first_token == 'coords':
                    shape_text_lines.append(tokens)
                elif first_token == 'line':
                    shape_text_lines.append(tokens)
                elif first_token == 'point':
                    shape_text_lines.append(tokens)
                ##  grammar summary
                elif first_token == 'initial':
                    initial_shape_name = tokens[0]
                    initial_shape = (           ###
                        cls._get_shape_from_name(initial_shape_name))
                elif (
                    first_token == 'rule' and
                    subfile == 'grammar'
                ):
                    name, left_shape, right_shape = (
                        tokens[0], tokens[1], tokens[3])
                    new_rule = rule.Rule(name, left_shape, right_shape)
                    grammar_rules.append(new_rule)
                ##  derivation shapes and rule names
                elif (
                    first_token == 'shape' and
                    subfile == 'derivation'     ##  derivation record
                ):
                    derivation_shape = (
                        shape.Shape.new_from_is_text_lines(shape_text_lines))
                    derivation_shapes.append(derivation_shape)
                    shape_text_lines = [tokens]
                elif (
                    first_token == 'rule' and
                    subfile == 'derivation'
                ):
                    derivation_rule_name = tokens[0]
                    derivation_rule = (         ###
                        cls._get_rule_from_name(
                            derivation_rule_name, grammar_rules))
                    derivation_rules.append(derivation_rule)

        new_derivation = Derivation(
            initial_shape, derivation_rules, derivation_shapes)
        return new_derivation

    @classmethod
    def _get_shape_from_name(cls, name, shapes):
        """Receives a shape name and a list of shapes:
            str
            [Shape, ...]
        Returns the shape with that name:
            Shape
        """
        pass
        # return shape

    @classmethod
    def _get_rule_from_name(cls, name, rules):
        """Receives a rule name and a list of rules:
            str
            [Rule, ...]
        Returns the rule with that name:
            Rule
        """
        pass
        # return rule

    def get_final_shape(self):
        """Returns the final shape in the derivation:
            Shape
        """
        final_shape = self.next_shapes[-1]
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
