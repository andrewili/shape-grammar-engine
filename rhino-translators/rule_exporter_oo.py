#   rule_exporter_oo.py

import rhinoscriptsyntax as rs
import rule
import shape

class RuleExporterOO(object):
    def __init__(self):
        pass

    ###
    def export_rule(self):
        left_shape = self.get_shape('left')
        right_shape = self.get_shape('right')
        the_rule = self.get_rule(left_shape, right_shape)
        rule_string = the_rule.__str__()
        self.write_rule_file()

    ###
    def get_shape(self, side):
        """Receives 'left' or 'right':
            str
        Prompts for a name. Returns the new shape:
            Shape
        """
        prompt_for_elements = (
            'Select the lines and textdots in the %s shape' % side)
        guids = rs.GetObjects(
            prompt_for_elements,
            rs.filter.curve + rs.filter.textdot)
        line_specs, lpoint_specs = self.get_line_specs_and_lpoint_specs(guids)
        prompt_for_name = (
            'Enter the name of the %s shape' % side)
        name = rs.GetString(prompt_for_name)
        new_shape = shape.Shape(name, line_specs, lpoint_specs)
        return new_shape

    def get_line_specs_and_lpoint_specs(self, guids):
        """Receives a list of line or textdot guids:
            [guid, ...]
        Returns a list of coord-coord pairs and a list of coord-label pairs:
            (   [((num, num, num), (num, num, num)), ...],
                [((num, num, num), str), ...]
            )
        """
        line_specs = []
        lpoint_specs = []
        line_type = 4
        textdot_type = 8192
        for guid in guids:
            guid_type = rs.ObjectType(guid)
            if guid_type == line_type:
                line_spec = self.get_line_spec(guid)
                line_specs.append(line_spec)
            elif guid_type == textdot_type:
                coord, label = self.get_lpoint_spec(guid)
                lpoint_spec = (coord, label)
                lpoint_specs.append(lpoint_spec)
        return (line_specs, lpoint_specs)
        # specs = []
        # for guid in guids:
        #     spec = self.guid_to_spec(guid)
        #     specs.append(spec)
        # return specs

    def get_line_spec(self, line_guid):
        """Receives a line guid:
            Guid
        Returns a line spec:
            ((num, num, num,), (num, num, num))
        """
        point_pair = rs.CurvePoints(line_guid)
        coord_pair = []
        for point in point_pair:
            coord = self.point_to_coord(point)
            coord_pair.append(coord)
        return (coord_pair[0], coord_pair[1])

    def get_lpoint_spec(self, textdot_guid):
        """Receives a textdot guid:
            Guid
        Returns a labeled point spec:
            ((num, num, num), label)
        """
        point = rs.TextDotPoint(textdot_guid)
        coord = self.point_to_coord(point)
        label = rs.TextDotText(textdot_guid)
        return (coord, label)

    def point_to_coord(self, point):
        """Receives a point guid:
            Guid
        Returns a coord:
            ((num, num, num))
        """
        coord = (point.X, point.Y, point.Z)
        return coord

    # def guid_to_spec(self, guid):
    #     """Receives a line or textdot guid:
    #         guid
    #     Returns a line or textdot spec:
    #         ((num, num, num), (num, num, num)) or
    #         ((num, num, num), str)
    #     """
    #     spec = '<spec>'            
    #     return spec

    ###
    def get_rule(self, left_shape, right_shape):
        """Receives the left and right shapes:
            Shape
            Shape
        Prompts for a name. Returns the new rule:
            Rule
        """
        prompt_for_name = 'Enter the name of the rule'
        name = rs.GetString(prompt_for_name)
        new_rule = rule.Rule(name, left_shape, right_shape)
        return new_rule

    ###
    def write_rule_file(self, rule_string):
        print(rule_string)

if __name__ == '__main__':
    exporter = RuleExporterOO()
    exporter.export_rule()
    # import doctest
    # doctest.testfile('tests/rule_exporter_oo_test.txt')
