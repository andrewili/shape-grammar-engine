#   rule.py

import shape

class Rule(object):
    def __init__(self, name, left_shape, right_shape):
        """Receives the rule's name; its left shape; and its right shape:
            str
            Shape
            Shape
        """
                                        #   Allow empty right shape
        try:
            if not (
                type(name) == str and
                type(left_shape) == shape.Shape and
                type(right_shape) == shape.Shape
            ):
                raise TypeError
        except TypeError:
            message = 'The arguments must be str, Shape, and Shape'
            print(message)
        else:
            self.name = name
            self.left_shape = left_shape
            self.right_shape = right_shape

    @classmethod
    def new_from_rul_text_lines(cls, text_lines_in):
        """Receives the lines of a file in .rul format:
            [str, ...]
        Returns:
            Rule
        """
        text_lines_out = [[], []]
        i = -1
        for text_line in text_lines_in:
            tokens = text_line.split()
            if tokens == []:
                pass
            else:
                first_token = tokens[0]
                if first_token == 'shape':
                    i = i + 1                   ##  start new list
                elif first_token == 'rule':
                    name = tokens[1]
                else:
                    text_lines_out[i].append(text_line)
        left_shape = shape.Shape.new_from_is_text_lines(
            text_lines_out[0])
        right_shape = shape.Shape.new_from_is_text_lines(
            text_lines_out[1])
        new_rule = Rule(name, left_shape, right_shape)
        return new_rule

    def get_source_shape(self):
        """Returns a shape containing the unique elements of the left and 
        right shapes. (This is not an SG shape, so there is no reduction.)
            Shape
        #   Accommodate empty right shape
        """
        source_name = '%s-source' % self.name
        source_line_specs = self._get_source_line_specs()
        source_lpoint_specs = self._get_source_lpoint_specs()
        source_shape = shape.Shape(
            source_name, source_line_specs, source_lpoint_specs)
        return source_shape

    def _get_source_line_specs(self):
        """Returns the list of unique (not maximal) line specs in one or both
        shapes:
            [((num, num, num), (num, num, num)), ...]
        """
        left_line_specs = self.left_shape.get_line_specs()
        right_line_specs = self.right_shape.get_line_specs()
        left_line_specs.extend(right_line_specs)
        line_spec_list = sorted(list(set(left_line_specs)))
        return line_spec_list

    def _get_source_lpoint_specs(self):
        """Returns the list of unique lpoint specs in one or both shapes:
            [((num, num, num), str), ...]
        """
        left_lpoint_specs = self.left_shape.get_lpoint_specs()
        right_lpoint_specs = self.right_shape.get_lpoint_specs()
        left_lpoint_specs.extend(right_lpoint_specs)
        lpoint_spec_list = sorted(list(set(left_lpoint_specs)))
        return lpoint_spec_list

    ###
    def __str__(self):
        """Returns a string in the rul format
            str
        """
        left_shape_string = (
            self.left_shape.make_rule_shape_string('left', self.name))
        right_shape_string = (
            self.right_shape.make_rule_shape_string('right', self.name))
        rule_name_string = self._make_rule_name_string()
        substrings = [
            left_shape_string,
            right_shape_string,
            rule_name_string]
        string = '\n'.join(substrings)
        return string

    def _make_rule_name_string(self):
        """Returns the rule name string:
            rule    <rule name>    <rule name>_L -> <rule name>_R
        """
        rule_name_string = (
            'rule    %s    %s_L -> %s_R' % (self.name, self.name, self.name))
        return rule_name_string

    ### to do
    def __repr__(self):
        """Returns an (unformatted) string in the form:
            <rule name>,
            <left shape repr>,
            <right shape repr>
        """
        repr_parts = (
            self.name, 
            self.left_shape.__repr__(), 
            self.right_shape.__repr__())
        joined_repr_parts = ', '.join(repr_parts)
        repr_string = '(%s)' % joined_repr_parts
        return repr_string

if __name__ == '__main__':
    import doctest
    doctest.testfile('tests/rule_test.txt')
