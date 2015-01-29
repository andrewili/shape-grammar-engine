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
        cls.clear_all()
        cls._set_up()
        # cls._add_first_initial_shape_frame()
        # cls._add_first_rule_frame()
        
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
    def _clear_layers(cls):
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

    @classmethod
    def _set_up(cls):
        # ShapeFrameBlock.new()
        rfb.RuleFrameBlock.new()                ##  then work here
        # # fb.FrameBlock.new()

    @classmethod
    def _add_first_initial_shape_frame(cls):
        rs.CurrentLayer('Default')
        origin = [0, 0, 0]
        fb.FrameBlock.insert(origin)

    @classmethod
    def _add_first_rule_frame(cls):             ##  first do generic 
                                                ##  add_rule_frame
        first_rule_frame_position = [0, -40, 0]
        first_rule_name = 'kilroy'
        rfb.RuleFrameBlock.insert(first_rule_frame_position, first_rule_name)

    @classmethod
    def add_initial_shape(cls):                 ##  you are here 01-28 17:07
        """Prompts the user for a name for the shape. Creates a new grammar 
        layer with that name, and inserts an initial shape frame block. 
        Returns:
            str             the user-assigned shape name, if successful
            None            otherwise
        """
        method_name = 'add_initial_shape'
        message = "%s %s" % (
            "Name of the initial shape.",
            "It must be unique and contain no spaces or '#' characters)")
        user_assigned_name = rs.GetString(message)
        while not (
            cls._name_is_well_formed(user_assigned_name) and
            cls._name_is_unused(user_assigned_name)
        ):
            user_assigned_name = rs.GetString(message)
        return_value = user_assigned_name
        # return_value = cls._add_named_initial_shape(user_assigned_name)
        return return_value

    @classmethod
    def _name_is_unused(cls, user_assigned_name):
        """Receives:
            user_assigned_name
                            str
        Returns:
            boolean         True or False
        """
        return_value = not(l.Layer.layer_name_is_in_use(user_assigned_name))
        return return_value

    @classmethod
    def _name_is_well_formed(cls, user_assigned_name):
        """Receives:
            user_assigned_name
                            str
        Returns:
            boolean         True or False
        """
        prohibited_characters = [' ', '#']
        for character in prohibited_characters:
            if character in user_assigned_name:
                return_value = False
                break
            else:
                return_value = True
        return return_value

    @classmethod
    def print_test_error_message(
        cls, method_name, try_name, expected_value, actual_value
    ):
        message = "%s: %s:\n    expected '%s'; got '%s'" % (
            method_name, try_name, expected_value, actual_value)
        print(message)

