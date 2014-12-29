import rhinoscriptsyntax as rs
# from package.model import dictionary as d
# from System.Drawing import Color

class Layer(object):
    def __init__(self):
        pass

    @classmethod
    def new(cls, layer_name_in, color_name='black'):
        """Receives:
            layer_name_in   str
            color_name      str. Optional
        Checks whether the name is in use. If not, adds a new layer. Returns:
            str             The name of the layer, if successful
            None            If unsuccessful
        """
        if cls._name_is_in_use(layer_name_in):
            print("The name '%s' is already in use" % layer_name_in)
            return_value = None
        else:
            cls._add_layer(layer_name_in, color_name)
        # return return_value

    @classmethod
    def _name_is_in_use(cls, layer_name):       ##  implement with Dictionary
        name_is_in_use = False
        return name_is_in_use

    @classmethod
    def _add_layer(cls, layer_name_in, color_name):
        """Receives:
            layer_name_in   str
            color_name      str
        Adds a layer. Returns:
            str             Layer name, if successful
            None            Otherwise
        """
        new_layer_name = rs.AddLayer(layer_name_in, color_name)
        if new_layer_name:
            print("Added new layer: '%s'" % new_layer_name)

                                                ##  refactor with Dictionary
                                                ##  check FrameBlock.delete()
        # user_layer_names = cls.get_user_layer_names()
        # if layer_name in user_layer_names:
        #     message = 'The layer "%s" already exists' % layer_name
        # else:
        #     if color_name == 'dark gray':
        #         color = Color.FromArgb(105, 105, 105)
        #     else:
        #         color = Color.Black
        #     rs.AddLayer(layer_name, color)
        #     d.Dictionary.set_value('user layer names', layer_name, '')
        #     message = 'Added layer: %s' % layer_name
        # print(message)
        # return layer_name

    # @classmethod
    # def set(cls, layer_name):
    #     """Receives a layer name:
    #         str
    #     Sets the current layer to the named layer. Returns the name of the new
    #     current layer:
    #         str
    #     """
    #     rs.CurrentLayer(layer_name)
    #     current_layer_name = rs.CurrentLayer()
    #     # print('Current layer: %s' % current_layer_name)
    #     return current_layer_name

    # @classmethod
    # def set_to_default(cls):
    #     cls.set('Default')

    # @classmethod
    # def purge(cls, layer_name):
    #     """Receives a layer name:
    #         str
    #     Deletes both the layer and its contents. Returns the success value:
    #         boolean
    #     """
    #     user_layer_names = cls.get_user_layer_names()
    #     if layer_name not in user_layer_names:
    #         message = 'The layer "%s" does not exist' % layer_name
    #     layer_was_purged = rs.PurgeLayer(layer_name)
    #     if layer_was_purged:
    #         d.Dictionary.delete_entry('user layer names', layer_name)
    #         message = 'Deleted layer: %s' % layer_name
    #     else:
    #         message = 'Failed to delete layer "%s"' % layer_name
    #     print(message)
    #     return layer_was_purged

    # @classmethod
    # def purge_all(cls):
    #     """Purges all grammar-defined layers and their contents. Returns the 
    #     number of layers purged:
    #         int
    #     """
    #     n_layers_purged = 0
    #     user_layer_names = cls.get_user_layer_names()
    #     for name in user_layer_names:
    #         name_was_purged = cls.purge(name)
    #         if name_was_purged:
    #             n_layers_purged += 1
    #     return n_layers_purged

    # @classmethod
    # def get_user_layer_names(cls):
    #     """Returns all user layer names, sorted:
    #         [str, ...]
    #     """
    #     names = d.Dictionary.get_keys('user layer names')
    #     return names

