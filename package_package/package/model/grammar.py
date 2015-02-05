from package.model import frame_block as fb
from package.model import layer as l
from package.model import shape_layer as sl
from package.model import rule_frame_block as rfb
import rhinoscriptsyntax as rs

class Grammar(object):
    first_initial_shape_name = 'initial_shape_1'
    first_initial_shape_frame_position = [0, 0, 0]

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

    @classmethod
    def _set_up(cls):
        # isfb.InitialShapeFrameBlock.new()
        rfb.RuleFrameBlock.new()                ##  then work here
        # # fb.FrameBlock.new()

    ### initial shape methods
    @classmethod                                ##  you are here 02-05 09:43
    def _add_first_initial_shape_frame(cls):
        """Adds a new layer. Inserts a shape frame block. Can be executed only 
        once. Returns:
            str                 cls.first_initial_shape_name
        """
        cls._add_named_positioned_shape_frame(
            cls.first_initial_shape_name,
            cls.first_initial_shape_frame_position)

    @classmethod                                ##  refactor for new method
    def add_unnamed_initial_shape_frame(cls):   ##  you are here 01-28 17:07
        """Prompts the user for a name for the shape. Creates a new grammar 
        layer with that name, and inserts an initial shape frame block. 
        Returns:
            str             the name of the new shape, if successful
            None            otherwise
        """
        method_name = 'add_unnamed_initial_shape_frame'
        message1 = "%s %s" % (
            "Enter the name of the initial shape.",
            "It must be unique and contain no spaces or '#' characters)")
        shape_name = rs.GetString(message1)
        message2 = "%s %s" % (
            "That name either is in use or contains spaces or '#' characters.",
            "Please try again")
        while not (
            cls._name_is_unused(shape_name) and
            cls._name_is_well_formed(shape_name)
        ):
            shape_name = rs.GetString(message2)
        return_value = cls._add_named_initial_shape_frame(shape_name)
        return return_value

    @classmethod                                ##  refactor with new method
    def _add_named_initial_shape_frame(cls, shape_name):
                                                ##  add_named_initial_shape_frame
                                                ##  add_named_initial_shape_layer
                                                ##  add_named_initial_shape
        """Receives:
            shape_name      str
        Creates a shape-layer named <shape_name>, prompts for a point, and 
        inserts an initial shape frame block. Returns:
            str             name of the new initial shape, if successful
            None            otherwise
        """
        method_name = '_add_named_initial_shape_frame'
        try:
            if not type(shape_name) == str:
                raise TypeError
            if not (
                cls._name_is_unused(shape_name) and
                cls._name_is_well_formed(shape_name)
            ):
                raise ValueError
        except TypeError:
            message = "%s.%s: %s" % (
                cls.__name__,
                method_name,
                "The name must be a string")
            print(message)
            return_value = None
        except ValueError:
            message = "%s.%s: %s" % (
                cls.__name__,
                method_name,
                "%s %s" % (
                "The name must be unused",
                "and may not contain spaces or '#' characters"))
            print(message)
            return_value = None
        else:
            l.Layer.new(shape_name)
            message = "Click on the base point in the xy plane"
            position = rs.GetPoint(message)
            result = fb.FrameBlock.insert(position)
            if result:
                return_value = shape_name
            else:
                return_value = None
        finally:
            return return_value

    @classmethod                                ##   you are here 02-05 10:24
    def _add_named_positioned_shape_frame(cls, name, position):
        """Receives:
            name            str
            position        Point3d or [num, num, num]
        Both arguments are tested by calling method. Adds a layer. Inserts a 
        shape frame on that layer. Returns:
            str             the name of the shape, if successful
            None            otherwise
        """
        method_name = '_add_named_positioned_shape_frame'
        return_value = sl.ShapeLayer.new(name, position)
        return return_value

    @classmethod
    def _name_is_unused(cls, shape_name):
        """Receives:
            shape_name      str
        Returns:
            boolean         True or False
        """
        return_value = not(l.Layer.layer_name_is_in_use(shape_name))
        return return_value

    @classmethod
    def _name_is_well_formed(cls, shape_name):
        """Receives:
            shape_name      str
        Returns:
            boolean         True or False
        """
        prohibited_characters = [' ', '#']
        for character in prohibited_characters:
            if character in shape_name:
                return_value = False
                break
            else:
                return_value = True
        return return_value

    ### rule methods
    @classmethod
    def _add_first_rule_frame(cls):             ##  first do generic 
                                                ##  add_rule_frame
        first_rule_frame_position = [0, -40, 0]
        first_rule_name = 'kilroy'
        rfb.RuleFrameBlock.insert(first_rule_frame_position, first_rule_name)

    @classmethod
    def _add_unnamed_rule_frame(cls):
        pass
        # user_assigned_name = get_name_from_user()
        # cls._add_named_rule_frame(user_assigned_name)

    @classmethod
    def _add_named_rule_frame(cls, rule_name):  ##  add_named_rule_layer_pair
        """Receives:
            rule_name       str
        Creates 2 shape-layers, named <rule_name>-l and <rule_name>-r, prompts
        for a point, and inserts a shape frame block on each shape layer. 
        Returns:
            str             the rule name, if successful
            None            otherwise
        """
        print("Pretending to run Grammar._add_named_rule_frame")
        sl.ShapeLayer.new(left_shape_name, left_position)
        sl.ShapeLayer.new(right_shape_name, right_position)

    ### utility methods
    @classmethod
    def print_test_error_message(
        cls, method_name, try_name, expected_value, actual_value
    ):
        message = "%s: %s:\n    expected '%s'; got '%s'" % (
            method_name, try_name, expected_value, actual_value)
        print(message)

