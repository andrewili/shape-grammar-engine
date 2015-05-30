from package.view import layer as l
from package.view import llist as ll
import rhinoscriptsyntax as rs

class Exporter(object):
    def __init__(self):
        self.class_name = 'Exporter'

    def export_grammar(self):
        """Prompts the user for a grammar name; suggests the Rhino file name.
        Writes the grammar's repr string to a file named <grammar_name>.dat.
        """
        name = get_name()
        i_shape_guids, rule_guids = get_guids()
        i_shape_specs, rule_specs = get_specs_from_guids(guids)
        grammar_spec = Grammar.get_spec_from_i_shape_and_rule_specs(
            i_shape_specs, rule_specs)
        grammar_repr = Grammar.get_repr_from_spec(grammar_spec)
        _write_to_file(grammar_repr)
