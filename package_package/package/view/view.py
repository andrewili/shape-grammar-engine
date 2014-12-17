import rhinoscriptsyntax as rs
from System.Drawing import Color

class View(object):
    def __init__(self):
        pass

    ### new grammar: clear objects
    def clear_objects(self):
        objects = rs.AllObjects()
        n_objects = rs.DeleteObjects(objects)
        return n_objects

    ### new grammar: clear settings
    def clear_blocks(self):
        names = rs.BlockNames()
        names_deleted = []
        if names:
            for name in names:
                deleted = rs.DeleteBlock(name)
                if deleted:
                    names_deleted.append(name)
        for name in names_deleted:
            print('Deleted block: %s' % name)
        return names_deleted

    def clear_layers(self):
        rs.CurrentLayer('Default')
        names_to_keep = [                       ##  Make customizable
            'Default', 
            'Layer 01', 'Layer 02', 'Layer 03', 'Layer 04', 'Layer 05']
        names_to_purge = rs.LayerNames()
        if names_to_purge:
            names_purged = []
            for name in names_to_purge:
                if not name in names_to_keep:
                    rs.PurgeLayer(name)
                    names_purged.append(name)
        for name in names_purged:
            print('Purged layer: %s' % name)
        return(names_purged)

    def clear_document_user_text(self):
        keys = rs.GetDocumentUserText()
        for key in keys:
            rs.SetDocumentUserText('')

    ### new grammar: set up
    def set_current_layer(self, layer_name):
        layer_name_out = rs.CurrentLayer(layer_name)
        print('Set current layer: %s' % layer_name)
        return layer_name_out

    def add_layer(self, layer_name, color_name='black'):
        if color_name == 'dark gray':
            color = Color.FromArgb(105, 105, 105)
        elif color_name == 'black':
            color = Color.Black
        else:
            color = Color.Black
        new_layer_name = rs.AddLayer(layer_name, color)
        print('Added layer: %s' % new_layer_name)
        return new_layer_name

    def add_block(
        self, point_pairs, lpoints, layer_name, position, block_name
    ):
        guids = self._add_shape(point_pairs, lpoints, layer_name)
        new_block_name = self._convert_shape_to_block(
            guids, position, block_name)
        print('Added block: %s' % new_block_name)
        return new_block_name

    def _add_shape(self, point_pairs, lpoints, layer_name):
        rs.CurrentLayer(layer_name)
        guids = []
        n_lines, n_lpoints = 0, 0
        for point_pair in point_pairs:
            line_guid = self._add_line(point_pair)
            guids.append(line_guid)
            n_lines += 1
        for lpoint in lpoints:
            lpoint_guid = self._add_labeled_point(lpoint)
            guids.append(lpoint_guid)
            n_lpoints += 1
        rs.CurrentLayer('Default')
        return guids

    def _add_line(self, point_pair):
        [p1, p2] = point_pair
        guid = rs.AddLine(p1, p2)
        return guid

    def _add_labeled_point(self, lpoint):       ##  To do
        # guid = ...
        # return guid
        pass

    def _convert_shape_to_block(self, guids, position, block_name):
        new_block_name = rs.AddBlock(guids, position, block_name, True)
        return new_block_name

    def set_initial_shape_counter(self):
        rs.SetDocumentUserText('initial shape counter', '0')
        
    def reset_counter(self, name):
        if name == 'initial shape counter':
            new_count_str = rs.SetDocumentUserText(
                'initial shape counter', '0')
        elif name == 'rule counter':
            new_count_str = rs.SetDocumentUserText('rule counter', '0')
        new_count_int = int(new_count_str)
        return new_count_int

    def increment_counter(self, name):
        old_i_str = rs.GetDocumentUserText(name)
        new_i_str = self._increment_str(old_i_str)
        success = rs.SetDocumentUserText(name, new_i_str)
        if success:
            value = int(new_i_str)
        else:
            value = False
        return value

    def _increment_str(self, old_i_str):
        """Receives a string representing an integer:
            str
        Returns the string form of the incremented integer
            str
        """
        old_i_int = int(old_i_str)
        new_i_int = old_i_int + 1
        new_i_str = str(new_i_int)
        return new_i_str

    ### initial shape
    def add_initial_shape_frame_at_prompt(self, layer_name):
        message = 'Select insertion point'
        position = rs.GetPoint(message)
        new_layer_name = self.add_initial_shape_frame(position, layer_name)
        return new_layer_name

    def add_initial_shape_frame(self, position, layer_name):
        rs.CurrentLayer(layer_name)
        self.insert_block('frame', layer_name, position)
        # rs.CurrentLayer('Default')
        print('Added initial shape frame: %s' % layer_name)
        return layer_name

    def insert_block(self, block_name, layer_name, position):
        # print('Pretending to insert block: %s' % block_name)
        layer_name
        guid = rs.InsertBlock(block_name, position)
        if guid:
            print('Inserted block: %s' % block_name)
            return block_name
        else:
            print("Didn't insert block: %s" % block_name)

    ### rule

    ### utilities
    def get_point(self, message):
        point = rs.GetPoint(message)
        return point