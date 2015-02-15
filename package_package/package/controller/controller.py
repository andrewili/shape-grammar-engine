from package.view import grammar as g

class Controller(object):
    def __init__(self):
        pass

    ### grammar
    @classmethod
    def new_grammar(cls):
        g.Grammar.new()


    # def _set_up(self):
        # self._set_layers()
        # self._add_blocks()
        # self._reset_counters()

    # def _set_layers(self):
        # self.v.set_current_layer('Default')
        # self.v.add_layer('frames', 'dark gray')

    # def _add_blocks(self):
        # self._add_frame_block()

    # def _add_frame_block(self):                 ##  should this info be in view?
    #                                             ##  combine with add_layer?
        # position = [0, 0, 0]
        # [x0, y0, z0] = position
        # side = 32
        # dx, dy, dz = side, side, side
        # x1, y1, z1 = x0 + dx, y0 + dy, z0 + dz

        # p0 = [x0, y0, z0]
        # p1 = [x0, y0, z1]
        # p2 = [x0, y1, z0]
        # p3 = [x0, y1, z1]
        # p4 = [x1, y0, z0]
        # p5 = [x1, y0, z1]
        # p6 = [x1, y1, z0]
        # p7 = [x1, y1, z1]

        # point_pairs = [
        #     (p0, p1), (p0, p2), (p0, p4), (p1, p3), (p1, p5), (p2, p3), 
        #     (p2, p6), (p3, p7), (p4, p5), (p4, p6), (p5, p7), (p6, p7)]
        # lpoints = []
        # layer_name = 'frames'
        # block_name = 'frame'
        # block_name = self.v.add_block(
        #     point_pairs, lpoints, layer_name, position, block_name)

    # def _reset_counters(self):
        # n_shapes = self.v.reset_counter('initial shape counter')
        # n_rules = self.v.reset_counter('rule counter')

    # def _add_first_initial_shape_frame(self):   ##  specify layout
        # position = [0, -50, 0]
        # i = self.v.increment_counter('initial shape counter')
        # layer_name = 'Shape %i' % i
        # self.v.add_layer(layer_name)
        # self.v.add_initial_shape_frame(position, layer_name)

    # def _add_first_rule_frame(self):
        # # position = [50, -50, 0]
        # # i = self.v.increment_counter('rule counter')
        # # layer_name = 'Rule %i' % i
        # pass        

    # def open_grammar(self):
        # pass

    # def save_grammar(self):
        # pass

    # def export_grammar(self):
        # pass

    ### initial shape
    def new_initial_shape(self, position, layer_name='Default'):
        i = self._increment_counter('initial shape counter')
        layer_name = 'Shape %i' % i
        self.v.add_layer(layer_name)
        self.v.add_initial_shape_frame_at_prompt(layer_name)

    # def import_initial_shape(self):
        # pass

    # def export_initial_shape(self):
        # pass

    ### rule
    def new_rule(self):
        """Prompts for a position and inserts a shape frame pair
        """
        i = self._increment_counter('rule counter')
        rule_name = 'Rule %i' % i
        position = self._get_point()
        self._new_shape_frame('left', rule_name, position)
        self._new_shape_frame('right', rule_name, position)

    def _increment_counter(self, counter_name):
        """Receives the name of a counter:
            str
        Increments the counter and returns the new value:
            int
        """
        new_i = self.v.increment_counter(counter_name)
        return new_i

    def _get_point(self):
        """Prompts for and returns a point:
            [num, num, num]
        """
        message = 'Select the insertion point'
        point = self.v.get_point(message)
        return point

    def _new_shape_frame(self, side, rule_name, position):
        """Receives the side ('initial', 'left', 'right'), the rule name, and
        the position:
            str
            str
            [num, num, num]
        Adds a layer named '<rule name> L' or '<rule name> R'. Prompts for a
        point and inserts a shape frame there
        """
        # print('Pretending to add a new shape frame')
        self.v.add_shape_frame(position, layer_name)

    # def import_rule(self):
    #     pass

    # def export_rule(self):
    #     pass

    # ###
    # def _set_shape_frame_block(self):
    #     name = 'shape frame'
    #     rs.CurrentLayer('frames')
    #     base_point = [0, 0, 0]
    #     frame_lines = self._draw_shape_frame(base_point)
    #     rs.AddBlock(frame_lines, base_point, name, True)
    #     rs.CurrentLayer('Default')
    #     return name

    # def _draw_shape_frame(self, base_point):
    #     """Draws a shape frame of side = 32 at base_point
    #     """
    #     canvas_side = 32
    #     canvas_size = [canvas_side, canvas_side, canvas_side]
    #     [x0, y0, z0] = base_point
    #     [x1, y1, z1] = rs.PointAdd(base_point, canvas_size)

    #     p0 = [x0, y0, z0]
    #     p1 = [x0, y0, z1]
    #     p2 = [x0, y1, z0]
    #     p3 = [x0, y1, z1]
    #     p4 = [x1, y0, z0]
    #     p5 = [x1, y0, z1]
    #     p6 = [x1, y1, z0]
    #     p7 = [x1, y1, z1]

    #     point_pairs = [
    #         (p0, p1), (p0, p2), (p0, p4), (p1, p3), (p1, p5), (p2, p3), 
    #         (p2, p6), (p3, p7), (p4, p5), (p4, p6), (p5, p7), (p6, p7)]

    #     lines = []
    #     for point_pair in point_pairs:
    #         lines.append(rs.AddLine(point_pair[0], point_pair[1]))
    #     return lines

    # def add_rule_layer_pair(self, base_point):
    #     """Receives the 3D base point of the left shape frame:
    #         [num, num, num]
    #     Prompts for the rule name. Adds a suitably named layer and a shape
    #     frame for each of the left and right shapes
    #     """
    #     right_base_point_offset = [50, 0, 0]
    #     right_base_point = rs.PointAdd(base_point, right_base_point_offset)
    #     rule_name = rs.GetString('Enter the name of the rule')
    #     left_shape_name = '%s left' % rule_name
    #     right_shape_name = '%s right' % rule_name
    #     self._add_shape_layer(left_shape_name, base_point)
    #     self._add_shape_layer(right_shape_name, right_base_point)

    # def add_initial_shape_layer(self, base_point):
    #     """Receives the 3D base point of the shape frame:
    #         [num, num, num]
    #     Prompts for a name. Adds a layer and shape frame
    #     """
    #     shape_name = rs.GetString('Enter the name of the shape')
    #     self._add_shape_layer(shape_name, base_point)
    #     print('Added an initial shape layer')

    # def _add_shape_layer(self, shape_name, base_point):
    #     """Receives the shape's name and 3D base point:
    #         str
    #         [num, num, num]
    #     Adds the layer with a shape frame
    #     """
    #     rs.AddLayer(shape_name)
    #     rs.CurrentLayer(shape_name)
    #     rs.InsertBlock('shape frame', base_point)
    #     rs.CurrentLayer('Default')
    #     print('Added shape layer "%s" at %s' % (shape_name, base_point))

    # ###
    # def export_rule(self, rule_name='nix'):
    #     """Receives a rule name <name>:
    #         str
    #     Saves a file <name>.rul
    #     """
    #     # shape_layer_name = rule_name + ['left' / 'right']
    #     # line_guids = get_line_guids
    #     # lpoint_guids = get_lpoint_guids
    #     # frame_guid = get_frame_guid
    #     # get_left_shape_specs(guids, base_point)
    #     # get_right_shape_specs(guids, base_point)
    #     # string = make_string
    #     # print(string)
    #     print('Pretending to export rule')