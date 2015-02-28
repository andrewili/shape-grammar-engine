from package.translators import exporter
from package.view import component_name as cn
from package.view import insertion_point as ip
from package.view import llist as ll
from package.view import shape_layer as sl

class InitialShape(object):
    component_type = 'initial shape'
    first_initial_shape_name = 'initial_shape_1'
    first_initial_shape_frame_position = [0, -40, 0]
                                                ##  make this parametric
    initial_shape_name_list_name = 'initial shape names'

    def __init__(self):
        pass

    @classmethod
    def add_first(cls):
        """Adds a pre-named new shape layer. Inserts a shape frame block at a 
        predetermined position. Should be executed only once. Returns:
            str             cls.first_initial_shape_name, if successful
            None            otherwise
        """
        if cn.ComponentName._component_name_is_listed(
            cls.component_type, cls.first_initial_shape_name
        ):
            return_value = None
        else:
            return_value = sl.ShapeLayer.new(
                cls.first_initial_shape_name,
                cls.first_initial_shape_frame_position)
            cls._record(cls.first_initial_shape_name)
            return return_value

    @classmethod
    def add_subsequent(cls):                    ##  Initial Shape / New
        """Prompts the user for a name and a position. Adds a new shape 
        layer. Inserts a shape frame block. Returns:
            str             the name of the new shape layer, if successful
            None            otherwise
        """
        initial_shape_name = (
            cn.ComponentName.get_initial_shape_name_from_user())
        position = ip.InsertionPoint.get_insertion_point_from_user()
        return_value = sl.ShapeLayer.new(initial_shape_name, position)
        cls._record(initial_shape_name)
        return return_value

    @classmethod
    def _record(cls, initial_shape_name):
        """Receives:
            initial_shape_name       
                            str
        Records the initial shape name in the initial shape name list. 
        Returns:
            str             the initial shape name, if successful
            None            otherwise
        """
        method_name = '_record'
        try:
            if not (type(initial_shape_name) == str):
                raise TypeError
        except TypeError:
            message = "The argument must be a string"
            print("%s.%s:\n    %s" % (cls.__name__, method_name, message))
            return_value = None
        else:
            return_value = ll.Llist.set_entry(
                cls.initial_shape_name_list_name, initial_shape_name)
        finally:
            return return_value

    @classmethod                                ##  02-27 09:27 Account for origin
    def export(cls):                            ##  Initial shape / Export...
        """Prompts the user to select an initial shape and its origin. 
        Constructs the is_string of the initial shape, and writes it to a file 
        named <initial_shape_name>.is. Returns:
            str             the name of the initial shape, if successful
            None            otherwise
        """
        exp = exporter.Exporter()
        exp.export_shape()

    @classmethod                                ##  02-28 08:02
    def export2(cls):
        """Prompts the user to select an initial shape or other item that 
        specifies an initial shape (e.g., name, frame), if one is not already 
        selected. Constructs the repr string and writes it to a file named 
        <initial_shape_name>.is. (Delegated to translator.)
        """
        message = "Pretending to export2"
        print(message)

        initial_shape = x
        exp = exporter.Exporter()
        exp.export_initial_shape(initial_shape)



