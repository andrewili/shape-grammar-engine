#   derivation.py (formerly rich_derivation.py)

# import derivation
import grammar
import rule
import shape

class Derivation(object):
    def __init__(self, grammar_in, derivation_shapes_in, derivation_rules_in):
        """Receives:
            Grammar
            [Shape, ...]
            [Rule, ...]
        """
        self.grammar = grammar_in
        self.derivation_shapes = derivation_shapes_in
        self.derivation_rules = derivation_rules_in
        
    @classmethod                                ##  I am here 2014-11-02
                                                ##  check call from Importer
    def new_from_drv_text_lines(cls, drv_text_lines):
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
            (   grammar_in,
                derivation_shapes_in,
                derivation_rules_in
            ) = (cls._get_derivation_parts(drv_text_lines))
            new_derivation = Derivation(
                grammar_in, derivation_shapes_in, derivation_rules_in)
            return new_derivation

    @classmethod
    def _get_derivation_parts(cls, drv_text_lines):
        """Receives a list of drv text lines:
            [str, ...]
        Returns a grammar, a list of derivation shapes, and a list of
        derivation rules:
            Grammar
            [Shape, ...]
            [Rule, ...]
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
        grammar_out = grammar.Grammar(grammar_initial_shapes, grammar_rules)
        return (
            grammar_out,
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

    ###
    def __str__(self):
        """Returns a string in the drv format
            str
        """
        header = (
            '# derivation file version 1.00' + 
            '                           ' + 
            '--chen liang 2007/08/06')
        grammar_text_lines_string = str(self.grammar)
        derivation_marker = '# derivation record'
        derivation_text_lines_string = (
            self._make_derivation_text_lines_string())
        strings = [
            header,
            grammar_text_lines_string,
            derivation_marker,
            derivation_text_lines_string]
        string = '\n'.join(strings)
        return string

    def _make_derivation_text_lines_string(self):
        """Returns <
            shape_text_lines_string\n
            rule_text_lines_string\n
            ...
        >:
            str
        """
        interleaved_substrings = []
        i = 0
        for i in range(len(self.derivation_rules)):
            interleaved_substrings.append(str(self.derivation_shapes[i]))
            interleaved_substrings.append(
                self.derivation_rules[i].make_rule_name_string_short())
        i = i + 1
        interleaved_substrings.append(str(self.derivation_shapes[i]))
        string = '\n'.join(interleaved_substrings)
        return string

    def __repr__(self):
        """Returns <
            (   grammar_drv_string,
                derivation_shapes_string,       ##  interleave shapes and rules?
                derivation_rule_names_string
            )
        >:
            str
        """
        grammar_drv_string = self.grammar.__repr__()
        derivation_shapes_string = self._make_derivation_shapes_string()
        derivation_rule_names_string = (
            self._make_derivation_rule_names_string())
        substrings = [
            grammar_drv_string,
            derivation_shapes_string,
            derivation_rule_names_string]
        string = ', '.join(substrings)
        return '(%s)' % string

    def _make_derivation_shapes_string(self):
        """Returns the combined drv strings of the derivation shapes:
            str
        """
        substrings = [shape.__repr__() for shape in self.derivation_shapes]
        string = ', '.join(substrings)
        return '[%s]' % string

    def _make_derivation_rule_names_string(self):
        substrings = [rule.name for rule in self.derivation_rules]
        string = ', '.join(substrings)
        return '[%s]' % string

if __name__ == '__main__':
    import doctest
    doctest.testfile('tests/derivation_test.txt')
