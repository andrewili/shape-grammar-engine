from package.model import frame_block as fb
import rhinoscriptsyntax as rs

# from System.Drawing import Color
# from package.model import counter as c
# from package.model import dictionary as d
# from package.model import layer as l

class Grammar(object):                          ##  convert to class methods
    def __init__(self):
        pass

    ### new
    @classmethod
    def new(cls):
        cls._set_settings()

        # cls._clear_objects()
        # cls._clear_settings()
        # cls._add_first_initial_shape()
        # cls._add_first_rule()
        
    #
    @classmethod
    def _clear_objects(cls):
        """Deletes all drawn objects. Returns the number of objects deleted:
            int
        """
        objects = rs.AllObjects()
        n_objects = rs.DeleteObjects(objects)
        return n_objects

    # #
    # @classmethod
    # def _clear_settings(cls):
    #     fb.FrameBlock.delete()
    #     l.Layer.purge_all()
    #     c.Counter.purge_all()

    #
    @classmethod
    def _set_settings(cls):
        fb.FrameBlock.new()

        # c.Counter.initialize_all()
        # l.Layer.set_to_default()

    # def _test_dictionary(self):
    #     dictionary_name = 'test dict'
    #     key = 'test key'
    #     value_in = 'test value'
    #     d.Dictionary.set_value(dictionary_name, key, value_in)
    #     new_value = d.Dictionary.get_value(dictionary_name, key)
    #     print('value should be "test value": %s' % new_value)
    #     d.Dictionary.purge_dictionary(dictionary_name)
    #     print('new_value again: %s' % d.Dictionary.get_value(
    #         dictionary_name, key))

    # ##
    # def _add_first_initial_shape_frame(self):
    #     print('Pretending to add the first initial shape frame')

    # ##
    # def _add_first_rule_frame(self):
    #     print('Pretending to add the first rule frame')

