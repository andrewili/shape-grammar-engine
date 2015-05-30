from package.view import frame_block as fb
from package.view import initial_shape as ish
from package.view import rule as r
from package.view import rule_frame_block as rfb
import rhinoscriptsyntax as rs

class Grammar(object):
    def __init__(self):
        pass

    ### new
    @classmethod
    def new(cls):
        cls.clear_all()
        cls._set_up()
        
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
        rfb.RuleFrameBlock.new()                ##  then work here
        ish.InitialShape.add_first()
        r.Rule.add_first()

    ### attribute equivalents
    @classmethod
    def get_name(cls):
        """Returns:
            name            str. The name of the Rhino document
        """
        name = rs.DocumentName()
        return name

    @classmethod
    def get_initial_shapes(cls):                ##  05-25 13:04 to do
        """Returns:
            ishapes         [str, ...]. A list of the names of the initial 
                            shapes in the grammar
        """
        return ishapes

    @classmethod
    def get_rules(cls):                         ##  05-25 13:05 to do
        """Returns:
            rules           [str, ...]. A list of the names of the rules in 
                            the grammar
        """
        return rules

    ### continuing methods
    @classmethod
    def export(cls):                            ##  05-26 04:45 to do
        """Writes the grammar's string to a file. Returns:
            dat_string      str. The dat string, if successful
            None            otherwise
        """
        name = cls.get_name()
        ishapes = cls.get_initial_shapes()
        rules = cls.get_rules()
        dat_string = cls.construct_dat_string(name, ishapes, rules)
        cls.write_to_file(name, dat_string)

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

    ### utility methods
    @classmethod
    def print_test_error_message(               ##  relocate
        cls, method_name, try_name, expected_value, actual_value
    ):
        message = "%s: %s:\n    expected '%s'; got '%s'" % (
            method_name, try_name, expected_value, actual_value)
        print(message)

