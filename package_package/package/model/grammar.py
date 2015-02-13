from package.model import frame_block as fb
from package.model import initial_shape as ish
from package.model import rule as r
from package.model import rule_frame_block as rfb
import rhinoscriptsyntax as rs

class Grammar(object):
    def __init__(self):
        pass

    ### new
    @classmethod
    def new(cls):
        cls.clear_all()
        cls._set_up()
        
    @classmethod
    def clear_all(cls):
        cls._clear_objects()
        cls._clear_blocks()
        cls._clear_layers()
        cls._clear_data()

    @classmethod
    def _clear_objects(cls):
        """Deletes all drawn objects. Returns:
            int             the number of objects deleted, if successful
        """
        objects = rs.AllObjects()
        n_objects = rs.DeleteObjects(objects)
        return n_objects

    @classmethod
    def _clear_blocks(cls):
        block_names = rs.BlockNames()
        for name in block_names:
            rs.DeleteBlock(name)

    @classmethod
    def _clear_layers(cls):                     ##  clear only user layers
        """Deletes all layers. Leaves Default layer
        """
        default_name = 'Default'
        layer_names = rs.LayerNames()
        if not default_name in layer_names:
            rs.AddLayer(default_name)
        rs.CurrentLayer(default_name)
        for layer_name in layer_names:
            if not layer_name == default_name:
                rs.DeleteLayer(layer_name)

    @classmethod
    def _clear_data(cls):
        rs.DeleteDocumentData()

    @classmethod                                ##  02-08 18:18
    def _set_up(cls):
        fb.FrameBlock.new()
        rfb.RuleFrameBlock.new()                ##  then work here
        cls._add_first_initial_shape()
        cls._add_first_rule()

    @classmethod                                ##  02-13 09:24
    def _add_first_initial_shape(cls):
        """Adds the first initial shape layer. Returns:
            str             the name of the first initial shape, if successful
            None            otherwise
        """
        return_value = ish.InitialShape.add_first()
        return return_value

    @classmethod                                ##  02-09 11:31
    def _add_first_rule(cls):
        """Adds the first rule layer. Returns:
            str             the name of the first rule, if successful
            None            otherwise
        """
        return_value = r.Rule.add_first()
        return return_value

    ### utility methods
    @classmethod
    def print_test_error_message(
        cls, method_name, try_name, expected_value, actual_value
    ):
        message = "%s: %s:\n    expected '%s'; got '%s'" % (
            method_name, try_name, expected_value, actual_value)
        print(message)

