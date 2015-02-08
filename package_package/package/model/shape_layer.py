from package.model import frame_block as fb
from package.model import layer as l
from package.model import llist as ll
import rhinoscriptsyntax as rs

class ShapeLayer(object):
    shape_layer_list_name = 'shape layer names'

    def __init__(self):
        pass

    @classmethod
    def new(cls, shape_name, position):
        """Receives:
            shape_name      str; available name
            position        Point3d or [num, num, num]; in the xy plane
        Both arguments are tested by the calling method. Creates a new layer 
        with a shape frame. Records the name in the shape layer name list. 
        Used for initial shapes, left rule shapes, and right rule shapes.
        Returns:
            str             shape_name, if successful
            None            otherwise
        """
        cls._record_name(shape_name)
        l.Layer.new(shape_name)
        rs.CurrentLayer(shape_name)
        guid = fb.FrameBlock.insert(position)
        rs.CurrentLayer('Default')
        if guid:
            return_value = shape_name
        else:
            return_value = None
        return return_value

    @classmethod
    def _record_name(cls, name):
        """Receives:
            name            str
        Enters the name in the shape layer name list. Returns:
            str             the name, if successful
            None            otherwise
        """
        return_value = ll.Llist.set_entry(cls.shape_layer_list_name, name)
        return return_value

    @classmethod
    def get_shape_name_from_user(cls):
        """Prompts the user for an unused and well-formed shape name. Returns:
            str             the shape name
        """
        message1 = "%s %s %s" % (
            "Enter the shape name.",
            "It must be unique",
            "and contain no spaces or '#' characters")
        message2 = "%s %s %s" % (
            "That name either is already used",
            "or contains spaces or '#' characters.",
            "Please try again")
        shape_name = rs.GetString(message1)
        while not (
            cls._shape_name_is_available(shape_name) and
            cls._shape_name_is_well_formed(shape_name)
        ):
            shape_name = rs.GetString(message2)
        return shape_name

    @classmethod
    def _shape_name_is_available(cls, shape_name):
        """Receives:
            shape_name      str
        Determines whether the shape name is available to the user. Returns:
            boolean         True or False
        """
        return_value = (
            not(cls._shape_layer_list_name_exists()) or
            not(cls.shape_name_is_listed(shape_name)))
        return return_value

    @classmethod
    def _shape_layer_list_name_exists(cls):
        """Determines whether the shape layer list name exists. Returns:
            boolean         True or False
        """
        return_value = ll.Llist.list_name_exists(cls.shape_layer_list_name)
        return return_value

    @classmethod
    def shape_name_is_listed(cls, shape_name):
        """Receives:
            shape_name      str
        Determines whether shape layer list contains the shape name. Returns:
            boolean         True or False
        """
        return_value = ll.Llist.contains_entry(
            cls.shape_layer_list_name, shape_name)
        return return_value

    @classmethod
    def _shape_name_is_well_formed(cls, shape_name):
        """Receives:
            shape_name      str
        Determines whether the shape name is well formed. Returns:
            boolean         True or False
        """
        method_name = '_shape_name_is_well_formed'
        try:
            if not type(shape_name) == str:
                raise TypeError
        except TypeError:
            message = "%s.%s:\n    %s" % (
                cls.__name__,
                method_name,
                "The shape name must be a string")
            print(message)
            return_value = False
        else:
            prohibited_characters = [' ', '#']
            for character in prohibited_characters:
                if character in shape_name:
                    return_value = False
                    break
                else:
                    return_value = True
        finally:
            return return_value

    @classmethod
    def get_frame_position_from_user(cls):
        """Prompts the user for a point in the xy plane. Returns:
            Point3d         the point
        """
        message1 = "Pick a point in the xy plane"
        message2 = "The point must be in the xy plane. Try again"
        point = rs.GetPoint(message1)
        while not point[2] == 0:
            point = rs.GetPoint(message2)
        return point

