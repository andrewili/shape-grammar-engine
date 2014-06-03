#   rule_exporter_oo.py

# import rhinoscriptsyntax as rs

class RuleExporterOO(object):
    def __init__(self):
        pass

    ###
    def export_rule(self):
        left_shape = self.get_shape('left')
        right_shape = self.get_shape('right')
        the_rule = get_rule(left_shape, right_shape)
        rule_string = the_rule.__str__()
        self.write_rule_file()

    ###
    def get_shape(self, side):
        """Receives 'left' or 'right':
            str
        Prompts for a name. Returns the new shape:
            Shape
        """
        guids = rs.GetObjects(
            prompt_for_elements,
            rs.filter.curve + rs.filter.textdot)
        line_specs, lpoint_specs = self.guids_to_specs(guids)
        name = rs.GetString(prompt_for_name)
        new_shape = shape.Shape(name, line_specs, lpoint_specs)
        return new_shape

    def guids_to_specs(self, guids):
        """Receives a list of line or textdot guids:
            [guid, ...]
        Returns a list of line or labeled point specs:
            [spec, ...]
        where spec =
            ((num, num, num), (num, num, num)) or
            ((num, num, num), str)
        """
        specs = []
        for guid in guids:
            spec = self.guid_to_spec(guid)
            specs.append(spec)
        return specs

    def guid_to_spec(self, guid):
        """Receives a line or textdot guid:
            guid
        Returns a line or textdot spec:
            ((num, num, num), (num, num, num)) or
            ((num, num, num), str)
        """
        spec = '<spec>'            
        return spec

    ###
    def get_rule(self, left_name_and_specs, right_name_and_specs):
        """Receives the name and specs of the left and right shapes:
            (str, [spec, ...])
            (str, [spec, ...])
        Prompts for a name. Returns the new rule:
            Rule
        """
        prompt_for_name = '<prompt for rule name>'
        name = rs.GetString(prompt_for_name)
        new_rule = rule.Rule(name, left_name_and_specs, right_name_and_specs)
        return new_rule

    ###
    def write_rule_file(self, rule_string):
        print(rule_string)

if __name__ == '__main__':
    import doctest
    doctest.testfile('tests/rule_exporter_oo_test.txt')
