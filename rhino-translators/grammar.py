#   grammar.py

import rule
import shape

class Grammar(object):
    def __init__(self, initial_shapes, rules):
        try:
            if not (
                type(initial_shapes) == list and
                type(rules) == list and
                len(initial_shapes) == 0 and
                len(rules) == 0
            ):
                raise TypeError
            for item in initial_shapes:
                if not type(item) == shape.Shape:
                    raise TypeError
            for item in rules:
                if not type(item) == rule.Rule:
                    raise TypeError
        except TypeError:
            message = '%s %s %s' % (
                'The arguments must be:',
                '1) a non-empty list of Shapes, and',
                '2) a non-empty list of Rules')
            print(message)
        else:
            self.initial_shapes = initial_shapes
            self.rules = rules

    @classmethod
    def new_from_drv_text_lines(cls, drv_text_lines):
        """Receives the text lines of a derivation file:
            [str, ...]
        Returns:
            Grammar
        """
        try:
            if not type(drv_text_lines) == list:
                raise TypeError
            for item in drv_text_lines:
                if not type(item) == str:
                    raise TypeError
        except TypeError:
            message = 'The argument must be a list of strings'
            print(message)
        else:
            (   initial_shapes,
                rules
            ) = cls._extract_grammar_parts(drv_text_lines)
            new_grammar = Grammar(initial_shapes, rules)
            return new_grammar

    @classmethod
    def _extract_grammar_parts(cls, drv_text_lines):
        """Receives a list of derivation text lines:
            [str, ...]
        Returns a list of shapes and a list of rules:
            [Shape, ...]
            [Rule, ...]
        """
        initial_shapes = []
        rules = []
        shape_text_lines_buffer = []
        shapes_dict = {}
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
                elif (
                    first_token == 'shape' and
                    subfile == 'grammar'
                ):
                    if cls._grammar_shape_pending(shape_text_lines_buffer):
                        cls._wrap_up_pending_grammar_shape(
                            shape_text_lines_buffer, shapes_dict)
                    shape_text_lines_buffer = [text_line]
                elif (
                    first_token == 'shape' and
                    subfile == 'derivation'
                ):
                    pass
                elif (
                    first_token == 'name' or
                    first_token == 'coords' or
                    first_token == 'line' or
                    first_token == 'point'
                ):
                    shape_text_lines_buffer.append(text_line)
                elif first_token == 'initial':
                    cls._wrap_up_pending_grammar_shape(
                        shape_text_lines_buffer, shapes_dict)
                    shape_name = tokens[1]
                    new_initial_shape = shapes_dict[shape_name]
                    initial_shapes.append(new_initial_shape)
                elif (
                    first_token == 'rule' and
                    subfile == 'grammar'
                ):
                    cls._add_new_rule(tokens, shapes_dict, rules)
                elif (
                    first_token == 'rule' and
                    subfile == 'derivation'
                ):
                    pass
                else:
                    pass
        return (initial_shapes, rules)

    @classmethod
    def _grammar_shape_pending(cls, shape_text_lines):
        value = False
        if not shape_text_lines == []:
            value = True
        return value

    @classmethod
    def _wrap_up_pending_grammar_shape(
        cls, shape_text_lines_buffer, shapes_dict
    ):
        new_shape = (
            shape.Shape.new_from_is_text_lines(shape_text_lines_buffer))
        shapes_dict[new_shape.name] = new_shape

    @classmethod
    def _add_new_rule(cls, tokens, shapes_dict, rules):
        rule_name = tokens[1]
        left_shape_name = tokens[2]
        right_shape_name = tokens[4]
        left_shape = shapes_dict[left_shape_name]
        right_shape = shapes_dict[right_shape_name]
        new_rule = rule.Rule(rule_name, left_shape, right_shape)
        rules.append(new_rule)

    def __str__(self):
        """Returns a string in the drv format:
            str
        """
        shapes_dict = {}
        initial_shape_names = []
        rule_name_triples = []
        for shape_i in self.initial_shapes:
            shapes_dict[shape_i.name] = shape_i
            shape_i_name_spec = 'initial    %s' % shape_i.name
            initial_shape_names.add(shape_i_name_spec)
        print('len(initial_shapes): %i' % len(self.initial_shapes))
        for rule_i in self.rules:
            left_name = rule_i.left_shape.name
            left_shape = rule_i.left_shape
            right_name = rule_i.right_shape.name
            right_shape = rule_i.right_shape
            shapes_dict[left_name] = left_shape
            shapes_dict[right_name] = right_shape
            rule_i_name_triple = (
                'rule    %s    %s -> %s' % (
                    rule_i.name, left_name, right_name))
            rule_name_triples.add(rule_i_name_triple)
        print('len(rules): %i' % len(self.rules))
        drv_text_lines = []
        for shape_i in sorted(shapes_dict):
            drv_text_lines.extend(str(shape_i))
        for initial_shape_name_spec in initial_shape_names:
            drv_text_lines.extend(initial_shape_name_spec)
        for rule_name_triple in rule_name_triples:
            drv_text_lines.add(rule_name_triple)
        print('len(drv_text_lines): %i' % len(drv_text_lines))
        string = '\n'.join(drv_text_lines)
        return string

    def __repr__(self):
        """Returns an (unformatted) string in the form:
            (   <initial shape>,
                [<rule>, ...]
            )
        """
        string = '<repr place holder>'
        return string

if __name__ == '__main__':
    import doctest
    doctest.testfile('tests/grammar_test.txt')