#   rule.py

# import rhinoscriptsyntax as rs

class Rule(object):
    def __init__(self, name, left_shape, right_shape):
        """Receives the rule's name; its left shape; and its right shape:
            str
            Shape
            Shape
        Prompts for the name of the rule.
        """

    ###
    def __str__(self):
        """Returns a string in the rul format
        """
        left_shape_string = self.left_shape.__str__()
        right_shape_string = self.right_shape_string.__str__()
        rule_name_string = self.make_rule_name_string(rule_name)
        string = '\n'.join(
            left_shape_string, right_shape_string, rule_name_string)

    def make_rule_name_string(self, rule_name):
        """Receives the rule name:
            str
        Returns the rule name string:
            rule    <rule name>    <rule name>_L -> <rule name>_R
        """
        rule_name_string = (
            'rule    <rule name>    <rule name>_L -> <rule name>_R')
        return rule_name_string

if __name__ == '__main__':
    import doctest
    doctest.testfile('tests/rule_test.txt')
