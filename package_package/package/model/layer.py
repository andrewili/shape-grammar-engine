from System.Drawing import Color
from package.model import dictionary as d
from package.model import llist as ll
import rhinoscriptsyntax as rs

class Layer(object):
    layer_dict_name = 'user layer names'

    def __init__(self):
        pass

    @classmethod                                ##  called by FrameBlock.new()
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
                not cls._layer_name_is_in_use(layer_name) and
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
            if cls._layer_name_is_in_use(layer_name):
                return_value = layer_name
            else:
                return_value = None
        finally:
            return return_value

    @classmethod
    def _layer_name_is_in_use(cls, layer_name):
        """Receives:
            layer_name      str
        Returns:
            boolean         True if layer_name is being used in the Rhino user
                            data structure (i.e., including Dictionary 
                            entries); False otherwise
        """
        method_name = '_layer_name_is_in_use'
        try:
            if not type(layer_name) == str:
                raise TypeError
        except TypeError:
            message = "%s.%s: The argument must be a string" % (
                cls.__name__, method_name)
            print(message)
            return_value = False
        else:
            return_value = ll.Llist._contains_entry(
                cls.layer_dict_name, layer_name)
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
            elif cls._layer_name_is_in_use(layer_name):
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
            return_value = ll.Llist.set_entry(cls.layer_dict_name, layer_name)
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
    def delete(cls, layer_name):                ##  You are here
        """Receives:
            layer_name      str
        Deletes the layer and removes its name from the layer name list.
        Returns:
            boolean         True if successful; False otherwise ##  Do this!
        """
        method_name = 'delete'
        try:
            if not type(layer_name) == str:
                raise TypeError
            if not cls._layer_name_is_in_use(layer_name):   ##  Moved on
                raise ValueError
        except TypeError:
            message = "The argument must be a string"
            print("%s.%s: %s" % (cls.__name__, method_name, message))
            return_value = None
        except ValueError:
            message = "The layer name '%s' does not exist" % layer_name
            print("%s.%s: %s" % (cls.__name__, method_name, message))
            return_value = None
        else:
            layer_name_was_deleted = cls._delete_layer_name(layer_name)
            layer_was_deleted = rs.DeleteLayer(layer_name)
            return_value = (
                layer_name_was_deleted and
                layer_was_deleted
            )
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
            if not cls._layer_name_is_in_use(layer_name):
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
                cls.layer_dict_name, layer_name)
        finally:
            return return_value

    # @classmethod
    # def set(cls, layer_name):
        # """Receives a layer name:
        #     str
        # Sets the current layer to the named layer. Returns the name of the new
        # current layer:
        #     str
        # """
        # rs.CurrentLayer(layer_name)
        # current_layer_name = rs.CurrentLayer()
        # # print('Current layer: %s' % current_layer_name)
        # return current_layer_name

    # @classmethod
    # def set_to_default(cls):
        # cls.set('Default')

    # @classmethod
    # def purge(cls, layer_name):
        # """Receives a layer name:
        #     str
        # Deletes both the layer and its contents. Returns the success value:
        #     boolean
        # """
        # user_layer_names = cls.get_user_layer_names()
        # if layer_name not in user_layer_names:
        #     message = 'The layer "%s" does not exist' % layer_name
        # layer_was_purged = rs.PurgeLayer(layer_name)
        # if layer_was_purged:
        #     d.Dictionary.delete_entry('user layer names', layer_name)
        #     message = 'Deleted layer: %s' % layer_name
        # else:
        #     message = 'Failed to delete layer "%s"' % layer_name
        # print(message)
        # return layer_was_purged

    # @classmethod
    # def purge_all(cls):
        # """Purges all grammar-defined layers and their contents. Returns the 
        # number of layers purged:
        #     int
        # """
        # n_layers_purged = 0
        # user_layer_names = cls.get_user_layer_names()
        # for name in user_layer_names:
        #     name_was_purged = cls.purge(name)
        #     if name_was_purged:
        #         n_layers_purged += 1
        # return n_layers_purged

    # @classmethod
    # def get_user_layer_names(cls):
        # """Returns all user layer names, sorted:
        #     [str, ...]
        # """
        # names = d.Dictionary.get_keys('user layer names')
        # return names

