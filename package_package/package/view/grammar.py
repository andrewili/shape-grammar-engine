from package.view import frame_block as fb
from package.view import initial_shape as ish
from package.view import llist as ll
from package.view import rule as r
import rhinoscriptsyntax as rs

class Grammar(object):
    initial_shapes = 'initial shapes'
    rules = 'rules'

    def __init__(self):
        pass

    ### new
    @classmethod
    def new(cls):
        cls.clear_all()
        cls._set_up()
        
    @classmethod
    def export(cls):                            ##  05-26 04:45
        """Writes the grammar's string to a file. Returns:
            dat_string      str. The dat string, if successful
            None            otherwise
        """
        name = cls.get_name()
        ishapes = cls.get_initial_shapes()      ##  
        rules = cls.get_rules()
        dat_string = cls.construct_dat_string(name, ishapes, rules)
        cls.write_to_file(name, dat_string)

    @classmethod
    def get_initial_shapes(cls):
        """Returns:
            initial_shapes  [str, ...]. A sorted list of the names of the 
                            initial shapes in the grammar, if successful
            None            otherwise
        """
        ishapes = ll.Llist.get_entries(cls.initial_shapes)
        return ishapes
            
    @classmethod
    def get_rules(cls):
        """Returns:
            rules           [str, ...]. A sorted list of the names of the 
                            rules in the grammar, if successful
            None            otherwise
        """
        rules = ll.Llist.get_entries(cls.rules)
        return rules

    ### attribute equivalents
    @classmethod
    def get_name(cls):
        """Returns:
            name            str. The name of the Rhino document
        """
        name = rs.DocumentName()
        return name

    @classmethod
    def add_to_initial_shapes(cls, name):
        """Receives:
            name            str. The name of an initial shape. Value verified
        Adds the name to the grammar's list of initial shape names. Returns:
            name            str. The name of the initial shape, if successful
            None            otherwise
        """
        value = ll.Llist.set_entry(cls.initial_shapes, name)
        if value:
            return name
        else:
            return None

    @classmethod
    def add_to_rules(cls, name):
        """Receives:
            name            str. The name of a rule. Value verified
        Adds the name to the grammar's list of rule names. Returns:
            name            str. The name of the rule, if successful
            None            otherwise
        """
        value = ll.Llist.set_entry(cls.rules, name)
        if value:
            return name
        else:
            return None

    @classmethod
    def remove_from_initial_shapes(cls):        ##  to do
        pass

    @classmethod
    def remove_from_rule(cls):                  ##  to do
        pass

    @classmethod
    def component_name_is_in_use(cls, name):
        """Receives:
            name            str. The name of a component
        Returns:
            boolean         True, if the name is on either the grammar's list 
                            of initial shapes or its list of rules
                            False, otherwise
        """
        value = (
            ll.Llist.contains_entry(cls.initial_shapes, name) or
            ll.Llist.contains_entry(cls.rules, name))
        return value

    ### continuing methods
    @classmethod
    def construct_dat_string(cls, name, ishapes, rules):
        """Receives:
            ishapes         [str, ...]. A list of the names of the initial 
                            ishapes in the grammar
            rules           [str, ...]. A list of the names of the rules in 
                            the grammar
        Returns:
            dat_string      str. The grammar's dat string, if successful
            None            otherwise
        """
        return dat_string

    @classmethod
    def write_to_file(cls):
        pass

    @classmethod
    def clear_all(cls):
        cls._clear_objects()
        cls._clear_blocks()
        cls._clear_layers()
        cls._clear_data()

    @classmethod
    def _clear_objects(cls):
        """Deletes all drawn objects. Returns:
            int             the number of objects deleted, if successful
        """
        objects = rs.AllObjects()
        n_objects = rs.DeleteObjects(objects)
        return n_objects

    @classmethod
    def _clear_blocks(cls):
        block_names = rs.BlockNames()
        for name in block_names:
            rs.DeleteBlock(name)

    @classmethod
    def _clear_layers(cls):                     ##  clear only user layers
        """Deletes all layers. Leaves Default layer
        """
        default_name = 'Default'
        layer_names = rs.LayerNames()
        if not default_name in layer_names:
            rs.AddLayer(default_name)
        rs.CurrentLayer(default_name)
        for layer_name in layer_names:
            if not layer_name == default_name:
                rs.DeleteLayer(layer_name)

    @classmethod
    def _clear_data(cls):
        rs.DeleteDocumentData()

    @classmethod
    def _set_up(cls):
        fb.FrameBlock.new()
        ish.InitialShape.add_first()
        r.Rule.add_first()

