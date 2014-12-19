from System.Drawing import Color
from package.model import data_entry as de
from package.model import frame_block as fb
from package.model import layer as l
import rhinoscriptsyntax as rs

class Grammar(object):
    def __init__(self):
        pass

    ### new
    def new(self):
        self._clear_objects()
        self._clear_settings()
        self._set_settings()
        # self._add_first_initial_shape_frame()
        # self._add_first_rule_frame()

    ##
    def _clear_objects(self):
        """Deletes all drawn objects. Returns the number of objects deleted:
            int
        """
        objects = rs.AllObjects()
        n_objects = rs.DeleteObjects(objects)
        print('Deleted %i object(s)' % n_objects)
        return n_objects

    ##
    def _clear_settings(self):
        fb.FrameBlock.delete()
        l.Layer.purge_all()
        de.DataEntry.clear_all()

    ##
    def _set_settings(self):
        fb.FrameBlock.new()
        # self._initialize_counters()
        l.Layer.set_to_default()

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

    def _initialize_counters(self):
        print('Pretending to initialize counters')

    ##
    def _add_first_initial_shape_frame(self):
        print('Pretending to add the first initial shape frame')

    ##
    def _add_first_rule_frame(self):
        print('Pretending to add the first rule frame')

