#   rule.py

# import rhinoscriptsyntax as rs
import shape

class Rule(object):
    def __init__(self, name, left_shape, right_shape):
        """Receives the rule's name; its left shape; and its right shape:
            str
            Shape
            Shape
        """
        self.name = name
        self.left_shape = left_shape
        self.right_shape = right_shape

    ###
    def __str__(self):
        """Returns a string in the rul format
        """
        left_shape_string = (
            self.left_shape.get_rule_shape_string('left', self.name))
        right_shape_string = (
            self.right_shape.get_rule_shape_string('right', self.name))
        # left_shape_string = self.left_shape.__str__()
        # right_shape_string = self.right_shape.__str__()
        rule_name_string = self.make_rule_name_string()
        substrings = [
            left_shape_string,
            right_shape_string,
            rule_name_string]
        string = '\n'.join(substrings)
        return string

    def make_rule_name_string(self):
        """Returns the rule name string:
            rule    <rule name>    <rule name>_L -> <rule name>_R
        """
        rule_name_string = (
            'rule    %s    %s_L -> %s_R' % (self.name, self.name, self.name))
        return rule_name_string

if __name__ == '__main__':
    import doctest
    doctest.testfile('tests/rule_test.txt')
