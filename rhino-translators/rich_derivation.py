#   rich_derivation.py

import derivation
import grammar
import rule
import shape

class RichDerivation(object):
    def __init__(self, drv_text_lines):
        """Receives a list of drv text lines:
            [str, ...]
        """
        try:
            if not type(drv_text_lines) == list:
                raise TypeError
            if len(drv_text_lines) == 0:
                raise TypeError
            for item in drv_text_lines:
                if not type(item) == str:
                    raise TypeError
        except TypeError:
            message = 'The argument must be a non-empty list of strings'
            print(message)
        else:
            (   grammar_initial_shapes,
                grammar_rules,
                derivation_shapes,
                derivation_rules
            ) = self._get_rich_derivation_parts(drv_text_lines)
            self.grammar = grammar.Grammar(
                grammar_initial_shapes, 
                grammar_rules)
            self.derivation = derivation.Derivation(
                derivation_shapes,
                derivation_rules)

    @classmethod
    def new_from_drv_text_lines(cls, drv_text_lines):
        (   grammar_shapes_dict,
            grammar_initial_shapes,
            grammar_rules,
            derivation_shapes,
            derivation_rules
        ) = cls._get_rich_derivation_parts(drv_text_lines)
        new_rich_derivation = RichDerivation(
            grammar_shapes_dict,
            grammar_initial_shapes,
            grammar_rules,
            derivation_shapes,
            derivation_rules)
        return new_rich_derivation

    @classmethod
    def _get_rich_derivation_parts(cls, drv_text_lines):
        """Receives a list of drv text lines:
            [str, ...]
        Returns 1) a name-Shape dictionary of the grammar's shapes, 2) a list 
        of the grammar's initial shapes, 3) a list of the grammar's rules, 
        4) a list of the derivation's shapes, and 5) a list (of the names) of 
        the derivation's rules:
            (   
                [Shape, ...],
                [Rule, ...],
                [Shape, ...],
                [Rule, ...]
            )
        """
        grammar_shapes_dict = {}
        grammar_rules_dict = {}
        grammar_initial_shapes = []
        grammar_rules = []
        derivation_rules = []
        derivation_shapes = []
        shape_text_lines = []
        is_first_derivation_shape = True
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
                elif (
                    first_token == 'shape' and
                    subfile == 'grammar'        ##  grammar record
                ):
                    if cls._shape_pending(shape_text_lines):
                        cls._wrap_up_pending_grammar_shape(
                            shape_text_lines, grammar_shapes_dict)
                    shape_text_lines = cls._reset_shape_text_lines(
                        text_line, shape_text_lines)
                elif first_token in ['name', 'coords', 'line', 'point']:
                    shape_text_lines.append(text_line)
                elif first_token == 'initial':  ##  if none?
                    if cls._shape_pending(shape_text_lines):
                        cls._wrap_up_pending_grammar_shape(
                            shape_text_lines, grammar_shapes_dict)
                        shape_text_lines = []   ##  new
                    initial_shape_name = tokens[1]
                    initial_shape = grammar_shapes_dict[initial_shape_name]
                    grammar_initial_shapes.append(initial_shape)
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
                    grammar_rules.append(grammar_rule)
                elif (
                    first_token == 'shape' and
                    subfile == 'derivation'
                ):
                    if is_first_derivation_shape:
                        shape_text_lines = cls._reset_shape_text_lines(
                            text_line, shape_text_lines)
                        is_first_derivation_shape = False
                    else:
                        if cls._shape_pending(shape_text_lines):
                            cls._wrap_up_pending_derivation_shape(
                                shape_text_lines, derivation_shapes)
                    shape_text_lines = cls._reset_shape_text_lines(
                        text_line, shape_text_lines)
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
                shape_text_lines, derivation_shapes)
        return (
            # grammar_shapes_dict,
            grammar_initial_shapes,
            grammar_rules,
            derivation_shapes,
            derivation_rules)

    @classmethod
    def _shape_pending(cls, text_lines):
        value = True
        if text_lines == []:
            value = False
        return value

    @classmethod
    def _reset_shape_text_lines(cls, text_line, shape_text_lines):
        """Receives a shape text line and a list of shape text lines:
            str
            [str, ...]
        Resets the list with the text line and returns the list:
            [str]
        """
        shape_text_lines = [text_line]
        return shape_text_lines

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
        """Receives a list of shape text lines and dictionary of grammar 
        name-shape entries:
            [str, ...]
            {str: Shape, ...}
        Creates a Shape and adds the name-Shape entry to the dictionary
        """
        new_shape = shape.Shape.new_from_is_text_lines(shape_text_lines)
        grammar_shapes_dict[new_shape.name] = new_shape

    @classmethod
    def _wrap_up_pending_derivation_shape(
        cls, shape_text_lines, next_shapes
    ):
        """Receives a list of shape text lines and a list of shapes:
            [str, ...]
            [Shape, ...]
        Creates a shape and appends it to the derivation shape list
        """
        next_shape = (
            shape.Shape.new_from_is_text_lines(shape_text_lines))
        next_shapes.append(next_shape)

    @classmethod
    def _look_up_derivation_rule(cls, tokens, grammar_rules_dict):
        """Receives a list of one token (the name of a derivation rule) and a 
        dictionary of name-rule entries:
            [str]
            {str: Rule, ...}
        Returns the named rule:
            Rule
        """
        derivation_rule_name = tokens[0]
        derivation_rule = (grammar_rules_dict[derivation_rule_name])
        return derivation_rule

    ###
    def __repr__(self):
        string = '<__repr__>'
        return string

if __name__ == '__main__':
    import doctest
    doctest.testfile('tests/rich_derivation_test.txt')
