from package.model import frame_block as fb
from package.model import initial_shape as ish
from package.model import layer as l
from package.model import llist as ll
from package.model import rule_frame_block as rfb
from package.model import shape_layer as sl
import rhinoscriptsyntax as rs

class Grammar(object):
    initial_shape_name_list_name = 'initial_shape_names'
    rule_name_list_name = 'rule_names'

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

    @classmethod                                ##  you are here 02-08 18:18
    def _set_up(cls):
        fb.FrameBlock.new()
        cls._add_first_initial_shape()
        cls._add_first_rule()
        rfb.RuleFrameBlock.new()                ##  then work here

    @classmethod
    def _add_first_initial_shape(cls):
        """Adds the first initial shape layer and records it in the initial 
        shape list. Returns:
            str             the name of the first initial shape, if successful
            None            otherwise
        """
        return_value = None
        added_first_initial_shape = ish.InitialShape.add_first()
        recorded_initial_shape = cls._record_initial_shape(
            ish.InitialShape.first_initial_shape_name)
        if (added_first_initial_shape and
            recorded_initial_shape
        ):
            return_value = recorded_initial_shape
        return return_value

    @classmethod                                ##  you are here 02-09 11:31
    def _add_first_rule(cls):
        """Adds the first rule layer and records it in the rule list. Returns:
            str             the name of the first rule, if successful
            None            otherwise
        """
        return_value = None
        added_first_rule = r.Rule.add_first()
        recorded_rule = cls._record(r.Rule.first_rule_name)
        if (added_first_rule and
            recorded_rule
        ):
            return_value = recorded_rule
        return return_value

    @classmethod
                                                ##  generalize for left and
                                                ##  right shapes
    def _record_initial_shape(cls, initial_shape_name):
        """Receives:
            initial_shape_name
                            str; a valid initial shape name
        initial_shape_name is validated by the calling method. Records the 
        initial shape name in the initial shape name list. Returns:
            str             the name, if successful
            None            otherwise
        """
        return_value = ll.Llist.set_entry(
            cls.initial_shape_name_list_name,
            ish.InitialShape.first_initial_shape_name)
        return return_value

    ### initial shape methods __ InitialShape class?
    # @classmethod                                ##  you are here 02-05 09:43
    #                                             ##  ___ to IS
    # def _add_first_initial_shape_frame(cls):
        # """Adds a new layer. Inserts a shape frame block. Can be executed only 
        # once. Returns:
        #     str                 cls.first_initial_shape_name, if successful
        #     None                otherwise
        # """
        # return_value = cls._add_named_positioned_shape_frame(
        #     cls.first_initial_shape_name,
        #     cls.first_initial_shape_frame_position)
        # return return_value

    # @classmethod                                ##  you are here 02-05 16:18
    #                                             ##  ___ to IS
    # def _add_subsequent_initial_shape_frame(cls):
        # """Prompts the user for a name and a position. Adds a layer and 
        # inserts a shape frame block. Returns:
        #     str             the name of the new shape, if successful
        #     None            otherwise
        # """
        # name = cls._get_shape_name_from_user()
        # position = cls._get_frame_position_from_user()
        # return_value = cls._add_named_positioned_shape_frame(
        #     name, position)
        # return return_value

    # @classmethod                                ##  refactor for new method
    # def add_unnamed_initial_shape_frame(cls):   ##  you are here 01-28 17:07
        # """Prompts the user for a name for the shape. Creates a new grammar 
        # layer with that name, and inserts an initial shape frame block. 
        # Returns:
        #     str             the name of the new shape, if successful
        #     None            otherwise
        # """
        # method_name = 'add_unnamed_initial_shape_frame'
        # message1 = "%s %s" % (
        #     "Enter the name of the initial shape.",
        #     "It must be unique and contain no spaces or '#' characters)")
        # shape_name = rs.GetString(message1)
        # message2 = "%s %s" % (
        #     "That name either is in use or contains spaces or '#' characters.",
        #     "Please try again")
        # while not (
        #     cls._shape_name_is_available(shape_name) and
        #     cls._shape_name_is_well_formed(shape_name)
        # ):
        #     shape_name = rs.GetString(message2)
        # return_value = cls._add_named_initial_shape_frame(shape_name)
        # return return_value

    # @classmethod                                ##  refactor with new method
    # def _add_named_initial_shape_frame(cls, shape_name):
        #                                         ##  add_named_initial_shape_frame
        #                                         ##  add_named_initial_shape_layer
        #                                         ##  add_named_initial_shape
        # """Receives:
        #     shape_name      str
        # Creates a shape-layer named <shape_name>, prompts for a point, and 
        # inserts an initial shape frame block. Returns:
        #     str             name of the new initial shape, if successful
        #     None            otherwise
        # """
        # method_name = '_add_named_initial_shape_frame'
        # try:
        #     if not type(shape_name) == str:
        #         raise TypeError
        #     if not (
        #         cls._shape_name_is_available(shape_name) and
        #         cls._shape_name_is_well_formed(shape_name)
        #     ):
        #         raise ValueError
        # except TypeError:
        #     message = "%s.%s: %s" % (
        #         cls.__name__,
        #         method_name,
        #         "The name must be a string")
        #     print(message)
        #     return_value = None
        # except ValueError:
        #     message = "%s.%s: %s" % (
        #         cls.__name__,
        #         method_name,
        #         "%s %s" % (
        #         "The name must be unused",
        #         "and may not contain spaces or '#' characters"))
        #     print(message)
        #     return_value = None
        # else:
        #     l.Layer.new(shape_name)
        #     message = "Click on the base point in the xy plane"
        #     position = rs.GetPoint(message)
        #     result = fb.FrameBlock.insert(position)
        #     if result:
        #         return_value = shape_name
        #     else:
        #         return_value = None
        # finally:
        #     return return_value

    # @classmethod                                ##  ___ to IS
    # def _add_named_positioned_shape_frame(cls, name, position):
        # """Receives:
        #     name            str
        #     position        Point3d or [num, num, num]
        # Both arguments are tested by calling method. Adds a layer. Inserts a 
        # shape frame on that layer. Returns:
        #     str             the name of the shape, if successful
        #     None            otherwise
        # """
        # method_name = '_add_named_positioned_shape_frame'
        # return_value = sl.ShapeLayer.new(name, position)
        # return return_value

    ### rule methods __ Rule class?
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

    ### lower-level methods
    # @classmethod
    # def _get_shape_name_from_user(cls):
        # """Prompts the user for an unused and well-formed shape name. Returns:
        #     str             the shape name
        # """
        # message1 = "%s %s" % (
        #     "Enter the shape name.",
        #     "It must be unused and contain no spaces or '#' characters")
        # message2 = "%s %s %s" % (
        #     "That name either is already used",
        #     "or contains spaces or '#' characters.",
        #     "Please try again")
        # shape_name = rs.GetString(message1)
        # while not (
        #     cls._shape_name_is_available(shape_name) and
        #     cls._shape_name_is_well_formed(shape_name)
        # ):
        #     shape_name = rs.GetString(message2)
        # return shape_name

    # @classmethod                                ##  rethink use of 
    # def _shape_name_is_available(cls, shape_name): ##  Layer method
        #                                         ##  Shape or ShapeLayer method?
        # """Receives:
        #     shape_name      str
        # Determines whether the shape name is available to the user. Returns:
        #     boolean         True or False
        # """
        # return_value = ll.Llist.contains_entry(shape_names, shape_name)
        # # return_value = not(l.Layer.layer_name_is_in_use(shape_name))
        # return return_value

    # @classmethod
    # def _shape_name_is_well_formed(cls, shape_name):
        # """Receives:
        #     shape_name
        # Converts shape_name to a string, if it is not one. Returns:
        #     boolean         True, if the name is well formed; False otherwise
        # """
        # shape_name = str(shape_name)
        # prohibited_characters = [' ', '#']
        # for character in prohibited_characters:
        #     if character in shape_name:
        #         return_value = False
        #         break
        #     else:
        #         return_value = True
        # return return_value

    # @classmethod
    # def _get_frame_position_from_user(cls):
        # """Prompts the user for a point in the xy plane. Returns:
        #     Point3d         the point
        # """
        # message1 = "Pick a point in the xy plane"
        # message2 = "The point must be in the xy plane. Try again"
        # point = rs.GetPoint(message1)
        # while not point[2] == 0:
        #     point = rs.GetPoint(message2)
        # return point

    ### utility methods
    @classmethod
    def print_test_error_message(
        cls, method_name, try_name, expected_value, actual_value
    ):
        message = "%s: %s:\n    expected '%s'; got '%s'" % (
            method_name, try_name, expected_value, actual_value)
        print(message)

