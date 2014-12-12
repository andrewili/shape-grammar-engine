#   exporter.py

import rhinoscriptsyntax as rs
import rule
import shape
from package.shape_grammar import labeled_shape as lshape

##  To do: implement abort method 

class Exporter(object):
    def __init__(self):
        self._initialize_layers()
        self._initialize_blocks()

    def _initialize_layers(self):
        rs.AddLayer('left')
        rs.AddLayer('right')
        rs.AddLayer('infrastructure')

    def _initialize_blocks(self):
        self._initialize_block('shape frame')

    # def _initialize_layer(self, name):
    #     rs.AddLayer(name)

    def _initialize_block(self, name):
        rs.CurrentLayer('infrastructure')
        x, y, z = 0, 0, 0
        frame_lines = self._draw_shape_frame(x, y, z)
        rs.AddBlock(frame_lines, [x, y, z], 'shape frame', True)
        rs.CurrentLayer('Default')

    def make_rule(self):
        """Prompts for rule and frames
        Returns the line specs and lpoint specs:
            [((num, num, num), (num, num, num)), ...]
            [((num, num, num), str), ...]
        """
        message = 'Select lines, labeled points, and frame'
        guids = rs.GetObjects(message)
        print('n guids: %i' % len(guids))
        # print('guids: %s' % guids)

        # left_guids, right_guids = self._separate_rule_guids(guids)
        # left_shape_specs = self._get_line_specs_and_lpoint_specs(left_guids)
        # right_shape_specs = self._get_line_specs_and_lpoint_specs(right_guids)
        # print('left line specs: %s' % left_line_specs)
        # print('left lpoint specs: %s' % left_lpoint_specs)
        # print('right line specs: %s' % right_line_specs)
        # print('right lpoint specs: %s' % right_lpoint_specs)

        # line_specs, lpoint_specs = (
        #     self._get_line_specs_and_lpoint_specs(guids))
        # print('line specs: %s' % line_specs)
        # print('lpoint specs: %s' % lpoint_specs)

    def _separate_rule_guids(self, guids):
        """Receives a list of line and text guids:
            [guid, ...]
        Returns the left shape guids and the right shape guids:
            [guid, ...]
            [guid, ...]
        """
        pass
        # return (left_guids, right_guids)

    ###
    def export_initial_shape(self):             ##  implement
        """Will invoke sg.shape.Shape()
        """
        print('Kilroy is trying to export an initial shape')
        # rhino_elements = self._get_lshape_elements()
        # initial_shape = lshape.LabeledShape.from_elements(rhino_elements)
        # initial_shape_str = str(initial_shape)
        # self._write_initial_shape_file(initial_shape_str)

    def export_shape(self):
        initial_shape = self._get_shape('initial')
        self._write_shape_file(initial_shape)

    def export_rule(self):
        left_shape = self._get_shape('left')
        right_shape = self._get_shape('right')
        the_rule = self._get_rule(left_shape, right_shape)
        self._write_rule_file(the_rule)

    def export_rule_in_frames(self):
        """Exports a rule with shapes in frames
        """

        left_elements = rs.ObjectsByLayer('left', True)
        right_elements = rs.ObjectsByLayer('right', True)
        n_left_elements = len(left_elements)
        print('number of left elements: %i' % n_left_elements)
        n_right_elements = len(right_elements)
        print('number of right elements: %i' % n_right_elements)

    def export_gif(self):                       ##  Prepare for animation
        pass

    def draw_initial_shape_frame(self):
        """Draws the frame at the origin
        """
        self._draw_shape_frame(2, 2, 0)

    def draw_rule_frame(self):
        """Draws a rule frame at the origin
        """
        rs.InsertBlock('shape frame', [0, 0, 0])
        rs.InsertBlock('shape frame', [50, 0, 0])
        # self._draw_shape_frame(0, 0, 0)
        # self._draw_shape_frame(48, 0, 0)

    def _draw_shape_frame(self, x0, y0, z0):
        """Draws a shape frame of side = 32 at [x0, y0, z0]
        """
        canvas_side = 32
        dx, dy, dz = canvas_side, canvas_side, canvas_side
        x1, y1, z1 = x0 + dx, y0 + dy, z0 + dz

        p0 = [x0, y0, z0]
        p1 = [x0, y0, z1]
        p2 = [x0, y1, z0]
        p3 = [x0, y1, z1]
        p4 = [x1, y0, z0]
        p5 = [x1, y0, z1]
        p6 = [x1, y1, z0]
        p7 = [x1, y1, z1]

        point_pairs = [
            (p0, p1), (p0, p2), (p0, p4), (p1, p3), (p1, p5), (p2, p3), 
            (p2, p6), (p3, p7), (p4, p5), (p4, p6), (p5, p7), (p6, p7)]

        # rs.CurrentLayer('infrastructure')
        lines = []
        for point_pair in point_pairs:
            lines.append(rs.AddLine(point_pair[0], point_pair[1]))
        # rs.CurrentLayer('Default')
        return lines

    ###
    def _get_shape(self, side):                 ##  Should produce maximal shape
        """Receives 'initial', 'left', or 'right':
            str
        Prompts for elements (lines and textdots) and a name. Returns the new 
        shape:
            Shape
        """
        prompt_for_elements = (
            'Select the lines and labeled points in the %s shape' % side
        )
        guids = rs.GetObjects(
            prompt_for_elements,
            rs.filter.curve + rs.filter.annotation + rs.filter.textdot
        )
        if side == 'initial':
            while guids == None:
                prompt_for_elements = (
                    'The initial shape may not be empty. ' +
                    'Select the lines and labeled points in the initial shape'
                )
                guids = rs.GetObjects(prompt_for_elements)
        elif side == 'left':
            while guids == None:
                prompt_for_elements = (
                    'The left shape may not be empty. ' +
                    'Select the lines and labeled points in the left shape')
                guids = rs.GetObjects(prompt_for_elements)
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
        """Receives a list of guids:
            [guid, ...]
        Returns a list of coord-coord pairs and a list of coord-label pairs:
            (   [((num, num, num), (num, num, num)), ...],
                [((num, num, num), str), ...]
            )
        """
        line_specs = []
        lpoint_specs = []
        line_type = 4                           ##  limit to straight lines
        annotation_type = 512
        textdot_type = 8192
        for guid in guids:
            guid_type = rs.ObjectType(guid)
            if guid_type == line_type:
                line_spec = self._get_line_spec(guid)
                line_specs.append(line_spec)
            elif guid_type == annotation_type:
                point = rs.TextObjectPoint(guid)
                x, y, z = point[0], point[1], point[2]
                coord = (x, y, z)
                label = rs.TextObjectText(guid)
                lpoint_spec = (coord, label)
                lpoint_specs.append(lpoint_spec)
            elif guid_type == textdot_type:
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

    def _get_lpoint_spec(self, textdot_guid):
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
