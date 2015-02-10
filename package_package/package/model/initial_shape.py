from package.model import llist as ll
import rhinoscriptsyntax as rs
from package.model import shape_layer as sl

class InitialShape(object):
    first_initial_shape_name = 'initial_shape_1'
    first_initial_shape_frame_position = [0, -40, 0]
                                                ##  make this parametric

    def __init__(self):
        pass

    @classmethod
    def add_first(cls):                         ##  revisit after Rule
        """Adds a pre-named new shape layer. Inserts a shape frame block at a 
        predetermined position. Should be executed only once. Returns:
            str             cls.first_initial_shape_name, if successful
            None            otherwise
        """
        if not(sl.ShapeLayer._shape_name_is_available(
            cls.first_initial_shape_name
        )):
            return_value = None
        else:
            return_value = sl.ShapeLayer.new(
                cls.first_initial_shape_name,
                cls.first_initial_shape_frame_position)
            return return_value

    @classmethod
    def _first_initial_shape_name_exists(cls):
        """Determines whether the first_initial_shape_name already exists.
        Returns:
            boolean         True or False
        """
        return_value = sl.ShapeLayer.shape_name_is_listed(
            cls.first_initial_shape_name)
        return return_value

    @classmethod
    def add_subsequent(cls):
        """Prompts the user for a name and a position. Adds a new shape 
        layer. Inserts a shape frame block. Returns:
            str             the name of the new shape layer, if successful
            None            otherwise
        """
        name = sl.ShapeLayer.get_shape_name_from_user()
        position = sl.ShapeLayer.get_frame_position_from_user()
        return_value = sl.ShapeLayer.new(name, position)
        return return_value
