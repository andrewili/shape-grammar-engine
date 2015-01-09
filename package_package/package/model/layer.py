from System.Drawing import Color
from package.model import dictionary as d
from package.model import llist as ll
import rhinoscriptsyntax as rs

class Layer(object):
    layer_dict_name = 'user layer names'
    layer_value = 'nil'
    class_name = 'Layer'

    def __init__(self):
        pass

##  make dict listing methods?

    @classmethod                                ##  called by FrameBlock.new()
    def new(cls, layer_name, color_name='black'):
        """Receives:
            layer_name      str
            color_name      str
        Adds a new layer and enters the name in the user layer name list, if 
        the name is available. Returns:
            str             the name of the layer, if successful
            None            otherwise
        """
        try:
            if not (
                type(layer_name) == str and
                type(color_name) == str
            ):
                raise TypeError
            elif cls._layer_name_is_in_use(layer_name):
                raise ValueError
        except TypeError:
            message = "%s: Both arguments must be strings" % cls.class_name
            print(message)
            return_value = None
        except ValueError:
            message = "%s: The layer name '%s' is in use" % (
                cls.class_name, layer_name)
            print(message)
            return_value = None
        else:
            rs.AddLayer(layer_name, color_name)
            layer_value = cls.layer_value
            layer_dict_name = cls.layer_dict_name
            d.Dictionary.set_value(layer_dict_name, layer_name, layer_value)
            user_layer_names = rs.GetDocumentData(layer_dict_name)
            system_layer_names = rs.LayerNames()
            if (
                layer_name in user_layer_names and
                layer_name in system_layer_names
            ):
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
        layer_dict_name = cls.layer_dict_name
        return_value = ll.Llist._contains_entry(layer_dict_name, layer_name)
        return return_value

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

