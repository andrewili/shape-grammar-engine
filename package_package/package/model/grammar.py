from package.model import frame_block as fb
from package.model import layer as l
from package.model import rule_frame_block as rfb
import rhinoscriptsyntax as rs
# from package.model import counter as c
# from System.Drawing import Color
# from package.model import dictionary as d

class Grammar(object):
    def __init__(self):
        pass

    ### new
    @classmethod
    def new(cls):
        cls._clear_objects()
        cls._clear_settings()
        cls._set_settings()
        # cls._add_first_initial_shape_frame()
        # cls._add_first_rule_frame()
        
    @classmethod
    def _clear_objects(cls):
        """Deletes all drawn objects. Returns:
            int             the number of objects deleted, if successful
        """
        objects = rs.AllObjects()
        n_objects = rs.DeleteObjects(objects)
        return n_objects

    @classmethod
    def _clear_settings(cls):
        cls._clear_blocks()
        # fb.FrameBlock.delete()
        # rfb.RuleFrameBlock.delete()             ##  working here
        cls._clear_layers()
        rs.DeleteDocumentData()

    @classmethod
    def _clear_blocks(cls):
        block_names = rs.BlockNames()
        for name in block_names:
            rs.DeleteBlock(name)

    @classmethod
    def _clear_layers(cls):
        layer_names = rs.LayerNames()
        for layer_name in layer_names:
            rs.DeleteLayer(layer_name)

    @classmethod
    def _set_settings(cls):
        cls._add_frames_layer()
        # ShapeFrameBlock.new()
        rfb.RuleFrameBlock.new()                ##  then work here
        # # fb.FrameBlock.new()

    @classmethod
    def _add_frames_layer(cls):
        layer_name = fb.FrameBlock.layer_name
        color_name = fb.FrameBlock.color_name
        l.Layer.new(layer_name, color_name)

    @classmethod
    def _add_first_initial_shape_frame(self):
        rs.CurrentLayer('Default')
        origin = [0, 0, 0]
        fb.FrameBlock.insert(origin)

    @classmethod
    def _add_first_rule_frame(self):
        print('Trying to add the first rule frame')
        # first_rule_frame_position = [0, -40, 0]
        # rf.RuleFrame.insert(first_rule_frame_position)

