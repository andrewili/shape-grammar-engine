from System.Drawing import Color
from package.model import dictionary as d
from package.model import llist as ll
import rhinoscriptsyntax as rs

class Layer(object):
    def __init__(self):
        pass

##  make dict listing methods?

    @classmethod                                ##  called by FrameBlock.new()
    def new(cls, layer_name_in, color_name='black'):
        """Receives:
            layer_name_in   str
            color_name      str. Optional
        Checks whether the name is already in use. If not, adds a new layer. 
        Returns:
            str             the name of the layer, if successful
            None            otherwise
        """
        if cls._name_is_in_use(layer_name_in):
            print("The name '%s' is already in use" % layer_name_in)
            return_value = None
        else:
            return_value = cls._add_layer(layer_name_in, color_name)
                                                ##  You are here
        return return_value

    @classmethod
    def _name_is_in_use(cls, layer_name):
        """Receives:
            layer_name      str
        Returns:
            boolean         True if layer_name is in the user layer name
                            dictionary; False otherwise
        """
        dict_name = cls._get_dict_name()
        layer_names = d.Dictionary.get_keys(dict_name)
        name_is_in_use = (layer_name in layer_names)
        return name_is_in_use

    @classmethod
    def _get_dict_name(cls):
        """Returns:
            str             the name of the layer name dictionary
        """
        return "user layer names"

    @classmethod
    def _get_layer_value(cls):
        """Returns:
            str             the dummy value used in the layer name dictionary
                            cannot be ''
        """
        return "nil"

    @classmethod
    def _add_layer(cls, layer_name_in, color_name):
        """Receives:
            layer_name_in   str, not in layer name dictionary
            color_name      str: {'dark gray'}
        Adds a layer. Adds its name to the layer name dictionary.
        Returns:
            str             layer name, if successful
            None            otherwise
        """
        color = cls._get_color(color_name)
        return_value = rs.AddLayer(layer_name_in, color)
        if not return_value == layer_name_in:
            return_value = None
        else:
            cls._enter_in_layer_name_dict(layer_name_in)
        return return_value

    @classmethod                                ##  to be removed
    def _enter_in_layer_name_dict(cls, layer_name):
        """Receives:
            layer_name      str
        Enters the layer name and the dummy value. Returns:
            str             the layer name, if successful
            None            otherwise
        """
        layer_dict_name = cls._get_dict_name()
        layer_value_in = cls._get_layer_value()
        layer_value_out = d.Dictionary.set_value(
            layer_dict_name, layer_name, layer_value_in)
        if not layer_value_out == layer_value_in:
            return_value = None
        else:
            return_value = layer_name
        return return_value

    @classmethod
    def _record_layer_name(cls, layer_name):
        """Receives:
            layer_name      str
        Enters the name in the user layer name dict
        """
        ll.Llist.record_layer_name(layer_name)

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

