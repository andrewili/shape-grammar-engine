from package.model import frame_block as fb
import rhinoscriptsyntax as rs

# from System.Drawing import Color
# from package.model import counter as c
# from package.model import dictionary as d
# from package.model import layer as l

class Grammar(object):
    def __init__(self):
        pass

    ### new
    @classmethod
    def new(cls):
        cls._clear_objects()
        cls._clear_settings()
        cls._set_settings()
        cls._add_first_initial_shape_frame()
        # cls._add_first_rule()
        
    #
    @classmethod
    def _clear_objects(cls):
        """Deletes all drawn objects. Returns:
            int             the number of objects deleted, if successful
        """
        objects = rs.AllObjects()
        n_objects = rs.DeleteObjects(objects)
        return n_objects

    #
    @classmethod
    def _clear_settings(cls):
        fb.FrameBlock.delete()
        # l.Layer.purge_all()
        # c.Counter.purge_all()

    #
    @classmethod
    def _set_settings(cls):
        fb.FrameBlock.new()

        # c.Counter.initialize_all()
        # l.Layer.set_to_default()

    #
    @classmethod
    def _add_first_initial_shape_frame(self):
        rs.CurrentLayer('Default')
        origin = [0, 0, 0]
        fb.FrameBlock.insert(origin)

    # ##
    # def _add_first_rule_frame(self):
        # print('Pretending to add the first rule frame')

