from package.view import container as c
from package.view import component_name as cn
from package.translators import exporter
from package.view import frame as f
from package.view import insertion_point as ip
from package.view import llist as ll
import rhinoscriptsyntax as rs
from package.view import settings as s
from package.view import shape_layer as sl

class InitialShape(object):
    component_type = 'initial shape'
    # first_initial_shape_name = 'initial_shape_1'
    # first_initial_shape_insertion_point = [0, -40, 0]
    initial_shape_name_list_name = 'initial shape names'

    def __init__(self):
        pass

    @classmethod
    def set_up_first(cls):                      ##  06-19 23:21
        """Adds a new layer with a frame block. Should be executed only once. 
        Returns:
            name            str. The name of the initial shape, if successful
            None            otherwise
        """
        method_name = 'set_up_first'
        try:
            name_is_in_use = rs.IsLayer(s.Settings.first_initial_shape_name)
            if name_is_in_use:
                raise ValueError
        except ValueError:
            message = "The first initial shape name is in use"
            print("%s.%s:\n    %s" % (cls.__name__, method_name, message))
            return_value = None
        else:
            name = s.Settings.first_initial_shape_name
            base_point = s.Settings.first_initial_shape_base_point
            component_type = cls.component_type
            value = l.Layer.new(name, base_point, component_type)
            if value:
                return_value = name
            else:
                return_value = None
        finally:
            return return_value

        #     name = s.Settings.first_initial_shape_name
        #     color = s.Settings.layer_color
        #     layer_name = rs.AddLayer(name, color)
        #     add_name_tag(layer_name, component_type, origin)
        #     rs.CurrentLayer(layer_name)
        #     position = s.Settings.first_initial_shape_origin
        #     block_guid = f.Frame.insert(name, origin, layer_name)
        #                                         ##  kilroy is here
        #     rs.CurrentLayer(s.Settings.default_layer_name)
        #     if not (layer_name and block_guid):
        #         return_value = None
        #     else:
        #         return_value = name
        # finally:
        #     return return_value

    @classmethod
    def add_first(cls):
        """Adds and names a new layer. Inserts a shape frame block at a 
        predetermined insertion point. Should be executed only once. Returns:
            str             cls.first_initial_shape_name, if successful
            None            otherwise
        """
        name = cls.first_initial_shape_name     ##  check for availability?
        insertion_point = cls.first_initial_shape_insertion_point
        value = c.Container.new(name, insertion_point, cls.component_type)
        if value:
            return name
        else:
            return None

    @classmethod
    def add_subsequent(cls):
        """Prompts the user for a name and an insertion point. Adds a new 
        layer with the name. Inserts a frame block. Returns:
            name            str. The name of the new initial shape, if 
                            successful
            None            otherwise
        """
        name = cn.ComponentName.get_initial_shape_name_from_user()
        while not cn.ComponentName._is_available(name):
            name = cn.ComponentName.get_initial_shape_name_from_user()
        insertion_point = ip.InsertionPoint.get_insertion_point_from_user()
        return_value = c.Container.new(
            name, insertion_point, cls.component_type)
        return return_value

    @classmethod
    def get_def_from_ishape(cls, name):
        """Receives:
            name            str. The name of an initial shape. Type and value 
                            guaranteed
        Returns:
            definition      str in the form:
                                shape    <name>
                            The definition of the initial shape
        """
        definition = "shape    %s" % name
        return definition

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

    @classmethod
    def export(cls):                            ##  to do
        """Writes the initial shape's repr string (is format) to a file. 
        Returns:
            ishape_name     str. The initial shape's name, if successful
            None            otherwise
        """
        return ishape_name

    @classmethod
    def get_repr(cls, ishape):                  ##  05-30 07:49
        """Receives:
            ishape          str. The initial shape's name
        Returns:
            rrepr           str. The initial shape's repr string, if 
                            successful
            None            otherwise
        """
        guids = cls.get_guids(ishape)
        origin = cls.get_origin(ishape)
        spec = LabeledShape.get_spec_from_lshape_guids(guids, origin)
        rrepr = get_repr_from_lshape_spec(spec)
        return rrepr

    @classmethod
    def get_guids(cls, ishape):                 ##  05-30 07:52
        """Receives:
            ishape          str. The name of an initial shape
        Returns:
            guids           [guid, ...]. A list of the guids of the elements 
                            in the initial shape 
        """
        return guids
