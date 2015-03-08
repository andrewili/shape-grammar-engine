import rhinoscriptsyntax as rs
from package.translators import rule
from package.translators import shape

class Exporter(object):
    def __init__(self):
        pass

    def export_shape(self):                     ##  to be superceded by 
                                                ##  Exporter
                                                ##  .export_initial_shape
        initial_shape = self._get_shape('initial')
        self._write_shape_file(initial_shape)

    def export_rule(self):
        left_shape = self._get_shape('left')
        right_shape = self._get_shape('right')
        the_rule = self._get_rule(left_shape, right_shape)
        self._write_rule_file(the_rule)

    ###
    def _get_shape(self, side):
        """Receives 'initial', 'left', or 'right':
            str
        Prompts for elements - lines, labeled points (i.e., text objects and 
        textdots) - and a name. Returns the new shape:
            Shape
        """
        prompt_for_elements = (
            'Select the lines and labeled points in the %s shape' % side)
        composite_filter = (
            rs.filter.curve + rs.filter.annotation + rs.filter.textdot)
        guids = rs.GetObjects(prompt_for_elements, composite_filter)
        if side == 'initial':
            while guids == None:
                prompt_for_elements = "%s %s %s" % (
                    "The initial shape may not be empty.",
                    "Select the lines and labeled points",
                    "in the initial shape")
                guids = rs.GetObjects(prompt_for_elements, composite_filter)
        elif side == 'left':
            while guids == None:
                prompt_for_elements = (
                    'The left shape may not be empty. ' +
                    'Select the lines and labeled points in the left shape')
                guids = rs.GetObjects(prompt_for_elements, composite_filter)
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
        """Receives a list of line or text dot guids:
            [guid, ...]
        Returns a list of coord-coord pairs and a list of coord-label pairs:
            (   [((num, num, num), (num, num, num)), ...],
                [((num, num, num), str), ...]
            )
        """
        line_specs = []
        lpoint_specs = []
        line_type = 4
        text_object_type = 512
        text_dot_type = 8192
        for guid in guids:
            guid_type = rs.ObjectType(guid)
            if guid_type == line_type:
                line_spec = self._get_line_spec(guid)
                line_specs.append(line_spec)
            elif (
                guid_type == text_dot_type or
                guid_type == text_object_type
            ):
                coord, label = self._get_lpoint_spec_from_text_item(guid)
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

    def _get_lpoint_spec_from_text_item(self, text_item_guid):
        """Receives the guid of a text item, i.e., a text dot or a text 
        object:
            Guid
        Returns a labeled point spec:
            ((num, num, num), label)
        """
        if rs.IsTextDot(text_item_guid):
            lpoint_spec = self._get_lpoint_spec_from_text_dot(text_item_guid)
        elif rs.IsText(text_item_guid):
            lpoint_spec = self._get_lpoint_spec_from_text_object(
                text_item_guid)
        else:
            pass
        return lpoint_spec

    def _get_lpoint_spec_from_text_dot(self, text_dot_guid):
        """Receives the guid of a text dot:
            Guid
        Returns the labeled point spec of the text dot:
            ((num, num, num), label)
        """
        point = rs.TextDotPoint(text_dot_guid)
        coord = self._point_to_coord(point)
        label = rs.TextDotText(text_dot_guid)
        return (coord, label)

    def _get_lpoint_spec_from_text_object(self, text_object_guid):
        """Receives the guid of a text object:
            Guid
        Returns the labeled point spec of the text object:
            ((num, num, num), label)
        """
        point = rs.TextObjectPoint(text_object_guid)
        coord = self._point_to_coord(point)
        label = rs.TextObjectText(text_object_guid)
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
