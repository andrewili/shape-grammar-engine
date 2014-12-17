import rhinoscriptsyntax as rs
from System.Drawing import Color

class Model(object):
    def __init__(self):
        pass

    ###
    def new_grammar(self):
        self._clear_objects()
        self._clear_settings()
        self._set_settings()
        # self._add_first_initial_shape_frame()
        self._add_first_rule_frame_pair()

    ##  _clear_objects
    def _clear_objects(self):
        """Deletes drawn objects. Returns the number of objects deleted:
            int
        """
        objects = rs.AllObjects()
        n_objects = rs.DeleteObjects(objects)
        print('Deleted %i objects' % n_objects)
        return n_objects

    ##  _clear_settings
    def _clear_settings(self):
        self._clear_blocks()
        self._clear_layers()
        self._clear_document_data()

    def _clear_blocks(self):
        """Deletes all blocks. Returns the number of blocks deleted:
            int
        """
        n_blocks_deleted = 0
        sorted_block_names = rs.BlockNames(True)
        for block_name in sorted_block_names:
            rs.DeleteBlock(block_name)
            n_blocks_deleted += 1
        print('Deleted %i blocks' % n_blocks_deleted)
        return n_blocks_deleted

    def _clear_layers(self):
        """Deletes grammar layers. Returns the number of layers deleted:
            int
        """
        n_layers_deleted = 0
        layer_names = rs.LayerNames()
        layer_names_to_keep = ['Default',
            'Layer 01', 'Layer 02', 'Layer 03', 'Layer 04', 'Layer 05']
        for layer_name in layer_names:
            if not layer_name in layer_names_to_keep:
                rs.DeleteLayer(layer_name)
                n_layers_deleted += 1
        print('Deleted %i layers' % n_layers_deleted)
        return n_layers_deleted

    def _clear_document_data(self):
        """Clears entries, e.g., counters. Returns the number of entries
        deleted:
            int
        """
        n_entries_deleted = 0
        keys = rs.GetDocumentUserText()
        for key in keys:
            rs.SetDocumentUserText(key)
            n_entries_deleted += 1
        string = 'Deleted %i data entries' % n_entries_deleted
        print(string)
        return n_entries_deleted


    ##  _set_settings
    def _set_settings(self):
        self._set_layer_to_default()
        self._add_blocks()
        self._initialize_counters()

    def _add_blocks(self):
        self._add_shape_frame_block()

    def _add_shape_frame_block(self):
        layer_name = self._add_frames_layer()
        base_point = [0, 0, 0]
        line_guids = self._draw_shape_frame(base_point, layer_name)
        block_name = 'Frame'
        self._convert_to_block(line_guids, base_point, block_name)

    def _add_frames_layer(self):
        """Creates the 'Frames' layer. Returns the layer name:
            str
        """
        layer_name = 'Frames'
        dark_gray = Color.FromArgb(105, 105, 105)
        new_layer_name = rs.AddLayer(layer_name, dark_gray)
        print('Added layer: %s' % new_layer_name)
        return new_layer_name

    def _draw_shape_frame(self, base_point, layer_name):
        """Draws a shape frame of side = 32 at base_point. Returns the lines:
            [guid, ...]
        """
        canvas_side = 32
        canvas_size = [canvas_side, canvas_side, canvas_side]
        [x0, y0, z0] = base_point
        opposite_point = rs.PointAdd(base_point, canvas_size)
        [x1, y1, z1] = opposite_point
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
        line_guids = []
        print('Layer name: %s' % layer_name)
        rs.CurrentLayer(layer_name)
        current_layer_name = rs.CurrentLayer()
        print('Current layer: %s' % current_layer_name)
        for point_pair in point_pairs:
            line_guids.append(rs.AddLine(point_pair[0], point_pair[1]))
        self._set_layer_to_default()
        return line_guids
 
    def _convert_to_block(self, guids, base_point, block_name):
        """Receives a list of guids, the base point, and the block name:
            [guid, ...]
            [num, num, num]
            str
        """
        delete_yes = True
        new_block_name = rs.AddBlock(
            guids, base_point, block_name, delete_yes)
        print('Created block: %s' % new_block_name)
        return new_block_name

    def _set_layer_to_default(self):
        rs.CurrentLayer('Default')

    def _initialize_counters(self):
        self._initialize_counter('initial shape counter')
        self._initialize_counter('rule counter')

    def _initialize_counter(self, counter_name):
        """Receives the name of the counter:
            str
        Creates the counter and initializes it to '0'. Returns the int value
        if successful; None if not:
            int
        """
        initial_value = '0'
        success = rs.SetDocumentUserText(counter_name, initial_value)
        if success:
            print('Initialized counter: %s: %s' % (
                counter_name, initial_value))
            value = int(initial_value)
        else:
            value = None
        return value

    ##  _add_first_initial_shape_frame

    ##  _add_first_rule_frame_pair
    def _add_first_rule_frame_pair(self):
        self._add_rule_frame_pair()
        print('Pretending to add the first rule frame pair')

    def _add_rule_frame_pair(self):
        self._add_left_shape_frame()
        self._add_right_shape_frame()
        print('Pretending to add a rule frame pair')

    def _add_left_shape_frame(self):
        self._add_shape_frame()

    def _add_right_shape_frame(self):
        self._add_shape_frame()

    ##  _add_shape_frame
    def _add_shape_frame(self):
        # add_layer()
        # insert_shape_frame()
        print('Pretending to add a shape frame')