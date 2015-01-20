from System.Drawing import Color
from package.model import llist as ll
import rhinoscriptsyntax as rs

class Layer(object):
    layer_name_list_name = 'user layer names'

    def __init__(self):
        pass

    @classmethod
    def new(cls, layer_name, color_name='black'):
        """Receives:
            layer_name      str
            color_name      str: {'black', 'dark gray'}
        Adds a new layer and enters the name in the user layer name list, if 
        the name is available. Returns:
            str             the name of the layer, if successful
            None            otherwise
        """
        method_name = 'new'
        try:
            if not (
                type(layer_name) == str and
                type(color_name) == str
            ):
                raise TypeError
            elif not (
                not cls.layer_name_is_in_use(layer_name) and
                cls._color_name_is_allowed(color_name)
            ):
                raise ValueError
        except TypeError:
            message = "%s.%s: Both arguments must be strings" % (
                cls.__name__, method_name)
            print(message)
            return_value = None
        except ValueError:
            message = "%s.%s: The layer name '%s' is in use" % (
                cls.__name__, method_name, layer_name)
            print(message)
            return_value = None
        else:
            rs.AddLayer(layer_name, color_name)
            cls._add_layer_name(layer_name)
            if cls.layer_name_is_in_use(layer_name):
                return_value = layer_name
            else:
                return_value = None
        finally:
            return return_value

    @classmethod
    def layer_name_is_in_use(cls, layer_name):
        """Receives:
            layer_name      str
        Returns:
            boolean         True if layer_name is being used in the Rhino user
                            data structure (i.e., including Dictionary 
                            entries); False otherwise
        """
        method_name = 'layer_name_is_in_use'
        try:
            if not type(layer_name) == str:
                raise TypeError
        except TypeError:
            message = "%s.%s: The argument must be a string" % (
                cls.__name__, method_name)
            print(message)
            return_value = False
        else:
            # if not cls._layer_name_list_name_exists():
            #     return_value = False
            # else:
            #     return_value = cls._layer_name_list_contains_name(layer_name)

            # list_exists = cls._layer_name_list_name_exists()
            # list_contains_name = cls._layer_name_list_contains_name(
            #     layer_name)
            # return_value = (
            #     list_exists and
            #     list_contains_name)
            return_value = (
                cls._layer_name_list_name_exists() and
                cls._layer_name_list_contains_name(layer_name))
        finally:
            return return_value

    @classmethod
    def _layer_name_list_name_exists(cls):
        """Returns:
            boolean     True, if the user layer name list name exists;
                        False otherwise
        """
        list_names = rs.GetDocumentData()
        return_value = (cls.layer_name_list_name in list_names)
        return return_value

    @classmethod
    def _layer_name_list_contains_name(cls, layer_name):
        """Receives:
            layer_name  str
        Returns:
            boolean     True, if the user layer name list contains
                        layer_name
        """
        method_name = '_layer_name_list_contains_name'
        try:
            if not type(layer_name) == str:
                raise TypeError
        except TypeError:
            message = "%s.%s: The argument must be a string" % (
                cls.__name__, method_name)
            print(message)
            return_value = False
        else:
            return_value = (
                cls._layer_name_list_name_exists() and
                ll.Llist.contains_entry(cls.layer_name_list_name, layer_name))
        finally:
            return return_value

    @classmethod
    def _color_name_is_allowed(cls, color_name):
        """Receives:
            color_name      str
        Returns:
            boolean         True, if the color name is allowed;
                            False otherwise
        """
        allowed_colors = ['black', 'dark gray']
        return_value = (color_name in allowed_colors)
        return return_value

    @classmethod
    def _add_layer_name(cls, layer_name):
        """Receives:
            layer_name      str
        Enters the name in the user layer name dict. Returns:
            str             the layer name, if successful
            None            otherwise
        """
        method_name = '_add_layer_name'
        try:
            if not type(layer_name) == str:
                raise TypeError
            elif cls.layer_name_is_in_use(layer_name):
                raise ValueError
        except TypeError:
            message = "%s.%s: The argument must be a string" % (
                cls.__name__, method_name)
            print(message)
            return_value = None
        except ValueError:
            message = "%s.%s: The name '%s' is in use" % (
                cls.__name__, method_name, layer_name)
            print(message)
            return_value = None
        else:
            return_value = ll.Llist.set_entry(
                cls.layer_name_list_name, layer_name)
        finally:
            return return_value

    @classmethod
    def _get_color(cls, color_name):
        """Receives:
            str             color name: {'dark gray'}
        Returns:
            color           from Color module
        """
        if color_name == 'dark gray':
            color = Color.FromArgb(105, 105, 105)
        else:
            color = Color.Black
        return color

    @classmethod
    def delete(cls, layer_name):
        """Receives:
            layer_name      str
        Deletes the layer and removes its name from the layer name list.
        Returns:
            boolean         True if successful; False otherwise
        """
        method_name = 'delete'
        try:
            if not type(layer_name) == str:
                raise TypeError
            if not cls.layer_name_is_in_use(layer_name):
                raise ValueError
        except TypeError:
            message = "The argument must be a string"
            print("%s.%s: %s" % (cls.__name__, method_name, message))
            return_value = False
        except ValueError:
            message = "The layer name '%s' does not exist" % layer_name
            print("%s.%s: %s" % (cls.__name__, method_name, message))
            return_value = False
        else:
            layer_name_was_deleted = cls._delete_layer_name(layer_name)
            layer_was_deleted = rs.DeleteLayer(layer_name)
            return_value = (
                layer_name_was_deleted and
                layer_was_deleted)
        finally:
            return return_value

    @classmethod
    def _delete_layer_name(cls, layer_name):
        """Receives:
            layer_name      str
        Deletes the name from the layer name list, if present. Returns:
            boolean         True, if successful; False otherwise
        """
        method_name = '_delete_layer_name'
        try:
            if not type(layer_name) == str:
                raise TypeError
            if not cls.layer_name_is_in_use(layer_name):
                raise ValueError
        except TypeError:
            message = "%s.%s: The argument must be a string" % (
                cls.__name__, method_name)
            print(message)
            return_value = False
        except ValueError:
            message = "%s.%s: The name '%s' does not exist" % (
                cls.__name__, method_name, layer_name)
            print(message)
            return_value = False
        else:
            return_value = ll.Llist.delete_entry(
                cls.layer_name_list_name, layer_name)
        finally:
            return return_value
