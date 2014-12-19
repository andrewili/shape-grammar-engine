from System.Drawing import Color
from package.model import data_entry as de
import rhinoscriptsyntax as rs

class Layer(object):
    def __init__(self):
        pass

    @classmethod
    def new(cls, layer_name, color_name='black'):
        """Receives a layer name and a color name:
            str
            str: 'black' | 'dark gray'
        Returns the layer name:
            str
        """
                                                ##  add to data_entry
        layer_names = de.DataEntry.get_grammar_layer_names()
        if layer_name in layer_names:
            message = 'The layer %s already exists' % layer_name
        else:
            if color_name == 'dark gray':
                color = Color.FromArgb(105, 105, 105)
            else:
                color = Color.Black
            rs.AddLayer(layer_name, color)
            de.DataEntry.add_grammar_layer_name(layer_name)
            message = 'Added the layer "%s"' % layer_name
        print(message)
        return layer_name

    @classmethod
    def purge(cls, layer_name):
        """Receives a layer name:
            str
        Deletes both the layer and its contents. Returns the success value:
            boolean
        """
        layer_names = rs.LayerNames()
        if layer_name not in layer_names:
            message = 'The layer "%s" does not exist' % layer_name
        layer_was_purged = rs.PurgeLayer(layer_name)
        if layer_was_purged:
            message = 'Deleted the layer "%s"' % layer_name
        else:
            message = 'Failed to delete the layer "%s"' % layer_name
        print(message)
        return layer_was_purged

    @classmethod
    def purge_all(cls):
        """Purges all grammar-defined layers and their contents. Returns the 
        number of layers purged:
            int
        """
        n_layers_purged = 0
        names = de.DataEntry.get_grammar_layer_names()
                                                ##  not working yet
        for layer_name in names:
            layer_was_purged = cls.purge(layer_name)
            if layer_was_purged:
                n_layers_purged += 1
        message = 'Purged %i layers' % n_layers_purged
        return n_layers_purged

    @classmethod
    def set(cls, layer_name):
        """Receives a layer name:
            str
        Sets the current layer to the named layer. Returns the name of the new
        current layer:
            str
        """
        rs.CurrentLayer(layer_name)
        current_layer_name = rs.CurrentLayer()
        print('Current layer: %s' % current_layer_name)
        return current_layer_name

    @classmethod
    def set_to_default(cls):
        cls.set('Default')
        # rs.CurrentLayer('Default')
