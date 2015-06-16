from package.view import frame_block as fb
from package.view import initial_shape as ish
from package.view import llist as ll
from package.view import rule as r
import rhinoscriptsyntax as rs

class Grammar(object):
    initial_shapes = 'initial shapes'
    rules = 'rules'
    dat_header = "%s\n%s" % (
        "# shape data version 6.00",
        "unit  mm  # mm - millimetre, cm - centimetre, m - metre")

    def __init__(self):
        pass

    ### new
    @classmethod
    def new(cls):
        cls.clear_all()
        fb.FrameBlock.new()
        # rs.AddGroup(ish.InitialShape.component_type)
        # rs.AddGroup(r.Rule.component_type)
        ish.InitialShape.add_first()
        r.Rule.add_first()

        # dat_string
        # spec
        
    @classmethod
    def export(cls):                            ##  05-26 04:45
        """Writes the grammar's spec (dat string?) to a file. Returns:
            dat_string      str. The dat string, if successful
            None            otherwise
        """
        name = cls.get_name()
        dat_string = cls.get_dat_string()
        cls.write_to_file(name, dat_string)

    ### attribute equivalents
    @classmethod
    def get_name(cls):
        """Returns:
            name            str. The name of the Rhino document, if successful
            None            otherwise
        """
        name = rs.DocumentName()
        return name

    @classmethod
    def get_initial_shapes(cls):
        """Returns:
            initial_shapes  [str, ...]. A sorted list of the names of the 
                            initial shapes in the grammar, if successful
            None            otherwise
        """
        text_guids = rs.ObjectsByGroup(ish.InitialShape.component_type)
        names = []
        for guid in text_guids:
            name = rs.TextObjectText(guid)
            names.append(name)
        return sorted(names)
            
    @classmethod
    def get_rule_shapes(cls):
        """Returns:
            rule_shapes     [str, ...]. A sorted list of the names of the 
                            labeled shapes in the grammar's rules, if 
                            successful
            None            otherwise
        """
        rules = cls.get_rules()
        rule_lshapes = []
        for rule in rules:
            rule_lshape_pair = r.Rule.get_lshape_pair_from_rule(rule)
            rule_lshapes.extend(rule_lshape_pair)
        return sorted(rule_lshapes)

    @classmethod
    def get_rules(cls):
        """Returns:
            rules           [str, ...]. A sorted list of the names of the 
                            rules in the grammar, if successful
            None            otherwise
        """
        text_guids = rs.ObjectsByGroup(r.Rule.component_type)
        names = []
        for guid in text_guids:
            name = rs.TextObjectText(guid)
            names.append(name)
        return sorted(names)

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
    def get_dat_string(cls):                    ##  06-08 05:56
        """The dat string consists of: 
            header
            ordered_named_lshapes_string
            ordered_named_ishape_defs_string
            ordered_named_rule_defs_string
        Returns:
            dat_string      str. The grammar's dat string, if successful
            None            otherwise
        """
        ordered_named_lshapes_string = cls._get_ordered_named_lshapes_string()
        ordered_named_ishape_defs_string = (
            cls._get_ordered_named_ishape_defs_string())
        ordered_named_rule_defs_string = (
            cls._get_ordered_named_rule_defs_string())
        dat_string = '\n'.join([
            cls.dat_header,
            ordered_named_lshapes_string,
            ordered_named_ishape_defs_string,
            ordered_named_rule_defs_string])
        return dat_string

    @classmethod
    def _get_ordered_named_lshapes_string(cls): ##  06-08 08:46
        """Returns:
            ordered_named_lshapes_string
                            str. The ordered concatenation of named lshape 
                            strings, both those in initial shapes and those in 
                            rules
        """
        ishape_lshapes = g.Grammar.get_initial_shapes()
        rule_lshapes = g.Grammar.get_rule_shapes()
        named_lshapes = []
        named_lshapes.extend(ishape_lshapes)
        named_lshapes.extend(rule_lshapes)
        ordered_named_lshapes = sorted(named_lshapes)
        ordered_named_lshape_strings = []
        for named_lshape in ordered_named_lshapes:
            named_lshape_string = (
                ls.LabeledShape.get_string_from_named_lshape(named_lshape))
            ordered_named_lshape_strings.append(named_lshape_string)
        ordered_named_lshapes_string = '\n'.join(ordered_named_lshape_strings)
        return ordered_named_lshapes_string

    @classmethod
    def _get_ishape_lshape_strings():           ##  06-08 09:32
        """Returns:
            ishape_lshape_strings
                        [str, ...]. A list of lshape strings of the 
                        grammar's initial shapes
        """
        ishape_lshape_strings = []
        ishapes = cls.get_initial_shapes()
        for ishape in ishapes:
            lshape_string = cls._get_lshape_string_from_ishape(ishape)
            ishape_lshape_strings.append(lshape_string)
        return ishape_lshape_strings

    @classmethod
    def _get_rule_lshape_strings():
        """Returns:
            rule_lshape_strings
                        [str, ...]. A list of lshape strings of the 
                        grammar's rules
        """
        rule_lshape_strings = []
        rules = cls.get_rules()
        for rule in rules:
            lshape_string_pair = cls._get_lshape_string_pair_from_rule(rule)
            rule_lshape_strings.extend(lshape_string_pair)
        return rule_lshape_strings

    @classmethod
    def _get_ordered_named_ishape_defs_string(cls): ##  06-16 09:33
        """Returns:
            ordered_ishape_defs
                            [str, ...]. An ordered list (by name) of initial 
                            shape definitions
        """
        return ordered_ishape_defs

    @classmethod
    def _get_ordered_named_rule_defs_string(cls):
        """Returns:
            ordered_rule_defs
                            [str, ...]. An ordered list (by name) of rule 
                            definitions, if successful
            None            otherwise
        """
        ordered_rules = cls.get_rules()
        ordered_rule_defs = []
        for rule_i in ordered_rules:
            rule_def = r.Rule.get_def_from_rule(rule_i)
            ordered_rule_defs.append(rule_def)
        return ordered_rule_defs

    @classmethod
    def write_to_file(cls):
        pass

    @classmethod
    def clear_all(cls):
        cls._clear_objects()
        cls._clear_blocks()
        cls._clear_layers()
        cls._clear_data()
        cls._clear_groups()

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
    def _clear_groups(cls):
        rs.DeleteGroup(ish.InitialShape.component_type)
        rs.DeleteGroup(r.Rule.component_type)
