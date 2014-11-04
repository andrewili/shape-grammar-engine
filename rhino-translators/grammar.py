#   grammar.py

import rule
import shape

class Grammar(object):
    def __init__(self, initial_shapes, rules):  ##  name?
        try:
            if not (
                type(initial_shapes) == list and
                type(rules) == list and
                len(initial_shapes) > 0 and
                len(rules) > 0
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
                '1) a non-empty list of Shapes and',
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
            initial_shape_names.append(shape_i_name_spec)
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
            rule_name_triples.append(rule_i_name_triple)
        drv_text_lines = []
        for shape_name_i in sorted(shapes_dict):
            shape_i = shapes_dict[shape_name_i]
            drv_text_lines.append(str(shape_i))
        for initial_shape_name_spec in initial_shape_names:
            drv_text_lines.append(initial_shape_name_spec)
        for rule_name_triple in rule_name_triples:
            drv_text_lines.append(rule_name_triple)
        string = '\n'.join(drv_text_lines)
        return string

    def __repr__(self):
        """Returns an (unformatted) string in the form:
            (   <sorted_shapes>,
                <initial_shape_names>,
                <rule_name_triples>)
        """
        repr_parts = self._extract_repr_parts()
        repr_part_strings = self._get_strings_from_repr_parts(repr_parts)
        joined_repr_part_strings = ', '.join(repr_part_strings)
        repr_string = '(%s)' % joined_repr_part_strings
        return repr_string

    def _extract_repr_parts(self):
        """Returns 1) a sorted list of shapes, 2) a list of initial shape 
        names, and 3) a list of rule-shape-shape name triples:
            [Shape, ...]
            [str, ...]
            [(str, str, str), ...]
        """
        shapes = []
        initial_shape_names = []
        rule_name_triples = []
        for shape_i in self.initial_shapes:
            shapes.append(shape_i)
            initial_shape_names.append(shape_i.name)
        for rule_i in self.rules:
            shapes.append(rule_i.left_shape)
            shapes.append(rule_i.right_shape)
            rule_name_triple_i = (
                rule_i.name,
                rule_i.left_shape.name,
                rule_i.right_shape.name)
            rule_name_triples.append(rule_name_triple_i)
        sorted_shapes = sorted(shapes, key=lambda shape_i: shape_i.name)
        return (
            sorted_shapes,
            initial_shape_names,
            rule_name_triples)

    def _get_strings_from_repr_parts(self, repr_parts):
        """Receives 1) a sorted list of shapes, 2) a list of initial shape 
        names, and 3) a list of rule-shape-shape name triples:
            [Shape, ...]
            [str, ...]
            [(str, str, str), ...]
        Returns the corresponding strings:
            str
            str
            str
        """
        (   sorted_shapes,
            initial_shape_names,
            rule_name_triples
        ) = repr_parts
        shape_reprs_string = self._get_reprs_string_from_shapes(sorted_shapes)
        initial_shape_names_string = (
            self._get_string_from_initial_shape_names(initial_shape_names))
        rule_name_triples_string = (
            self._get_string_from_rule_name_triples(rule_name_triples))
        return (
            shape_reprs_string,
            initial_shape_names_string,
            rule_name_triples_string)

    def _get_reprs_string_from_shapes(self, shapes):
        """Receives a list of shapes:
            [Shape, ...]
        Returns the combined reprs of the shapes:
            str
        """
        shape_reprs = []
        for shape_i in shapes:
            shape_repr = shape_i.__repr__()
            shape_reprs.append(shape_repr)
        reprs_string = ', '.join(shape_reprs)
        return '[%s]' % reprs_string

    def _get_string_from_initial_shape_names(self, names):
        """Receives a list of shape names:
            [str, ...]
        Returns the combined names in brackets:
            str
        """
        names_string = ', '.join(names)
        return '[%s]' % names_string

    def _get_string_from_rule_name_triples(self, name_triples):
        """Receives a list of rule-shape-shape name triples:
            [(str, str, str), ...]
        Returns the combined triples in brackets:
            str
        """
        name_triple_strings = []
        for name_triple in name_triples:
            name_triple_string = self._get_string_from_name_triple(name_triple)
            name_triple_strings.append(name_triple_string)
        name_triples_string = ', '.join(name_triple_strings)
        return '[%s]' % name_triples_string

    def _get_string_from_name_triple(self, name_triple):
        """Receives a rule-shape-shape name triple:
            (str, str, str)
        Returns the combined string in parentheses:
            str
        """
        string = ', '.join(name_triple)
        return '(%s)' % string

if __name__ == '__main__':
    import doctest
    doctest.testfile('tests/grammar_test.txt')