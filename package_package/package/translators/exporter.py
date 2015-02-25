import rhinoscriptsyntax as rs
from package.translators import rule
from package.translators import shape

class Exporter(object):
    def __init__(self):
        pass

    def export_shape(self):
        initial_shape = self._get_shape('initial')
        self._write_shape_file(initial_shape)

    def export_rule(self):
        left_shape = self._get_shape('left')
        right_shape = self._get_shape('right')
        the_rule = self._get_rule(left_shape, right_shape)
        self._write_rule_file(the_rule)

    ###
    def _get_shape(self, side):                 ##  02-25 10:21
        """Receives 'initial', 'left', or 'right':
            str
        Prompts for elements (lines and textdots) and a name. Returns the new 
        shape:
            Shape
        """
        prompt_for_elements = (
            'Select the lines and textdots in the %s shape' % side)
        guids = rs.GetObjects(
            prompt_for_elements,
            rs.filter.curve + rs.filter.textdot)
                                                ##  rs.filter.annotation
        if side == 'initial':
            while guids == None:
                prompt_for_elements = (
                    'The initial shape may not be empty. ' +
                    'Select the lines and textdots in the initial shape')
                guids = rs.GetObjects(
                    prompt_for_elements,
                    rs.filter.curve + rs.filter.textdot)
                                                ##  rs.filter.annotation
        elif side == 'left':
            while guids == None:
                prompt_for_elements = (
                    'The left shape may not be empty. ' +
                    'Select the lines and textdots in the left shape')
                guids = rs.GetObjects(
                    prompt_for_elements,
                    rs.filter.curve + rs.filter.textdot)
                                                ##  rs.filter.annotation
        elif side == 'right':
            if guids == None:
                guids = []
        else:
            pass
        line_specs, lpoint_specs = (
            self._get_line_specs_and_lpoint_specs(guids))
        prompt_for_name = (
            'Enter the name of the %s shape' % side)
        name = rs.GetString(prompt_for_name)
        while not self._is_well_formed(name):
            prompt_for_name = (
                'The name may not contain a space or a #. ' +
                'Enter the name of the %s shape' % side)
            name = rs.GetString(prompt_for_name)
        new_shape = shape.Shape(name, line_specs, lpoint_specs)
        return new_shape

    def _is_well_formed(self, name):
        """Receives a name:
            str
        Return whether the name is non-empty, contains no spaces or #
        characters:
            boolean
        """
        value = False
        if (not name == '' and
            not ' ' in name and
            not '#' in name
        ):
            value = True
        return value

    def _get_line_specs_and_lpoint_specs(self, guids):
                                                ##  02-25 10:25
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
                line_spec = self._get_line_spec(guid)
                line_specs.append(line_spec)
            elif guid_type == textdot_type:     ##  or annotation
                coord, label = self._get_lpoint_spec(guid)
                lpoint_spec = (coord, label)
                lpoint_specs.append(lpoint_spec)
        return (line_specs, lpoint_specs)

    def _get_line_spec(self, line_guid):
        """Receives a line guid:
            Guid
        Returns a line spec:
            ((num, num, num,), (num, num, num))
        """
        point_pair = rs.CurvePoints(line_guid)
        coord_pair = []
        for point in point_pair:
            coord = self._point_to_coord(point)
            coord_pair.append(coord)
        return (coord_pair[0], coord_pair[1])

    def _get_lpoint_spec(self, textdot_guid):   ##  02-25 10:27 or annotation
        """Receives a textdot guid:
            Guid
        Returns a labeled point spec:
            ((num, num, num), label)
        """
        point = rs.TextDotPoint(textdot_guid)
        coord = self._point_to_coord(point)
        label = rs.TextDotText(textdot_guid)
        return (coord, label)

    def _point_to_coord(self, point):
        """Receives a point guid:
            Guid
        Returns a coord:
            ((num, num, num))
        """
        coord = (point.X, point.Y, point.Z)
        return coord

    ###
    def _get_rule(self, left_shape, right_shape):
        """Receives the left and right shapes:
            Shape
            Shape
        Prompts for a name. Returns the new rule:
            Rule
        """
        prompt_for_name = 'Enter the name of the rule'
        name = rs.GetString(prompt_for_name)
        while not self._is_well_formed(name):
            prompt_for_name = (
                'The name may not contain a space or a #. ' +
                'Enter the name of the rule')
            name = rs.GetString(prompt_for_name)
        new_rule = rule.Rule(name, left_shape, right_shape)
        return new_rule

    ###
    def _write_shape_file(self, shape_in):
        """Writes the shape string to the file <shape name>.is
        """
        filter = "IS file (*.is)|*.is|All files (*.*)|*.*||"
        shape_name = shape_in.name
        file_name = (
            rs.SaveFileName('Save shape as', filter, '', shape_name))
        if not file_name: 
            return
        file = open(file_name, "w" )
        empty_line = ''
        shape_string = '\n'.join([
            shape_in.__str__(), 
            empty_line])
        file.write(shape_string)
        file.close()
        print(shape_string)

    ###
    def _write_rule_file(self, rule_in):
        """Writes the rule string to the file <rule name>.rul
        """
        filter = "RUL file (*.rul)|*.rul|All files (*.*)|*.*||"
        rule_name = rule_in.name
        file_name = (
            rs.SaveFileName('Save rule as', filter, '', rule_name))
        if not file_name: 
            return
        file = open(file_name, "w" )
        empty_line = ''
        rule_string = '\n'.join([
            rule_in.__str__(), 
            empty_line])
        file.write(rule_string)
        file.close()
        print(rule_string)
