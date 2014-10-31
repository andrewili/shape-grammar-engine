#   derivation.py

import rule
import shape

class Derivation(object):
    def __init__(self, shapes, rules):
                                                ##  test for exceptions
                                                ##  len(shapes) = len(rules) + 1
        """Receives:
            [Shape, ...]
            [Rule, ...]
        """
        try:
            if not (
                type(shapes) == list and
                type(rules) == list and
                len(shapes) == len(rules) + 1
            ):
                raise TypeError
            for item in shapes:
                if not type(item) == shape.Shape:
                    raise TypeError
            for item in rules:
                if not type(item) == rule.Rule:
                    raise TypeError
        except TypeError:
            message = '%s %s %s' % (
                "The arguments must be",
                "a list of shapes (length = n + 1) and",
                "a list of rules (length = n)")
            print(message)
        else:
            self.rules = rules
            self.shapes = shapes

    @classmethod
    def new_from_drv_text_lines(cls, drv_text_lines):
        """Receives the text lines of a drv file:
            [<drv-text-line>, ...]
        Returns:
            Derivation
        """
        grammar_shapes_dict = {}
        grammar_rules_dict = {}
        derivation_rules = []
        next_shapes = []
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
                ##  grammar shapes
                elif (
                    first_token == 'shape' and
                    subfile == 'grammar'        ##  grammar record
                ):
                    if cls._shape_pending(shape_text_lines):
                        cls._wrap_up_pending_grammar_shape(
                            shape_text_lines, grammar_shapes_dict)
                    shape_text_lines = [text_line]  ##  start new shape
                elif first_token in ['name', 'coords', 'line', 'point']:
                    shape_text_lines.append(text_line)
                elif first_token == 'initial':  ##  if none?
                    if cls._shape_pending(shape_text_lines):
                        cls._wrap_up_pending_grammar_shape(
                            shape_text_lines, grammar_shapes_dict)
                        shape_text_lines = []   ##  new
                    initial_shape_name = tokens[1]
                    initial_shape = grammar_shapes_dict[initial_shape_name]
                elif (
                    first_token == 'rule' and
                    subfile == 'grammar'
                ):
                    grammar_rule_name, left_shape_name, right_shape_name = (
                        tokens[1], tokens[2], tokens[4])
                    left_shape = grammar_shapes_dict[left_shape_name]
                    right_shape = grammar_shapes_dict[right_shape_name]
                    grammar_rule = (
                        rule.Rule(grammar_rule_name, left_shape, right_shape))
                    grammar_rules_dict[grammar_rule_name] = grammar_rule
                ##  derivation shapes and rule names
                elif (
                    first_token == 'shape' and
                    subfile == 'derivation'
                ):
                    if cls._shape_pending(shape_text_lines):
                        cls._wrap_up_pending_derivation_shape(
                            shape_text_lines, next_shapes)
                    shape_text_lines = [text_line]  ##  start new shape
                elif (
                    first_token == 'rule' and
                    subfile == 'derivation'
                ):
                    if cls._rule_is_unidentified(tokens):
                        pass
                    elif cls._rule_is_unknown(tokens, grammar_rules_dict):
                        pass
                    else:
                        derivation_rule_name = tokens[1]
                        derivation_rule = (
                            grammar_rules_dict[derivation_rule_name])
                        derivation_rules.append(derivation_rule)
                ##  other case?
        if not shape_text_lines == []:
            cls._wrap_up_pending_derivation_shape(
                shape_text_lines, next_shapes)
        new_derivation = Derivation(
            initial_shape, derivation_rules, next_shapes)
        return new_derivation

    @classmethod
    def _shape_pending(cls, text_lines):
        value = True
        if text_lines == []:
            value = False
        return value

    @classmethod
    def _rule_is_unidentified(cls, tokens):
        value = False
        if len(tokens) == 1:
            value = True
        return value

    @classmethod
    def _rule_is_unknown(cls, tokens, grammar_rules_dict):
        rule_name = tokens[1]
        value = False
        if not rule_name in grammar_rules_dict:
            value = True
        return value

    @classmethod
    def _wrap_up_pending_grammar_shape(
        cls, shape_text_lines, grammar_shapes_dict
    ):
        """Receives a list of shape text lines and a dictionary of name-shape 
        entries:
            [str, ...]
            {str: Shape, ...}
        Creates a shape and enters it in the dictionary
        """
        new_shape = shape.Shape.new_from_is_text_lines(shape_text_lines)
        grammar_shapes_dict[new_shape.name] = new_shape

    @classmethod
    def _wrap_up_pending_derivation_shape(cls, shape_text_lines, next_shapes):
        """Receives a list of shape text lines and a list of shapes:
            [str, ...]
            [Shape, ...]
        Creates a shape and appends it to the derivation shape list
        """
        next_shape = (
            shape.Shape.new_from_is_text_lines(shape_text_lines))
        next_shapes.append(next_shape)

    def get_final_shape(self):
        """Returns the final shape in the derivation:
            Shape
        """
        final_shape = self.next_shapes[-1]
        return final_shape

    def __str__(self):                          ##  to do
        """Returns a string in the drv format:
            str
        """
        header = '# derivation record'
        item_strings = [header]
        interleaved_shapes_and_rules = (
            self._get_interleaved_shapes_and_rules())
        for item in interleaved_shapes_and_rules:
            item_string = self._get_item_string(item)
            item_strings.append(item_string)
        derivation_string = '\n'.join(item_strings)
        return derivation_string

    def _get_interleaved_shapes_and_rules(self):
        """Returns a list of shapes alternating with rules:
            [Shape, Rule, ...]
        """
        interleaved_items = []
        i = 0
        for i in range(len(self.rules)):
            interleaved_items.append(self.shapes[i])
            interleaved_items.append(self.rules[i])
            i = i + 1
        interleaved_items.append(self.shapes[i])
        return interleaved_items

    def _get_item_string(self, item):
        if type(item) == shape.Shape:
            item_string = str(item)
        elif type(item) == rule.Rule:
            rule_name_string_short = item.make_rule_name_string_short()
            item_string = rule_name_string_short
        else:
            pass
        return item_string

    def _make_grammar_string(self):             ##  to do
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
            (   <initial shape>,
                <rules>,
                <next shapes>
            )
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
