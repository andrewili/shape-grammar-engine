from package.view import frame as f
from package.controller import guids_to_dat as gd
# from package.view import initial_shape as ish   ##  to deprecate
from package.view import layer as l
from package.view import llist as ll
# from package.view import rule as r              ##  to deprecate
import rhinoscriptsyntax as rs
from package.view import settings as s

class Grammar(object):
    initial_shapes = 'initial shapes'
    rules = 'rules'

    def __init__(self):
        pass

    ### new
    @classmethod
    def new(cls):                               ##  set_up_grammar?
        cls.clear_all()
        cls._set_up_first_initial_shape()
        cls._set_up_first_rule()

    @classmethod
    def _set_up_first_initial_shape(cls):
        """Adds a new layer with one frame. Should be executed only once. 
        Returns:
            layer_name      str. The name of the layer, if successful
            None            otherwise
        """
        method_name = '_set_up_first_initial_shape'
        try:
            layer_name = s.Settings.first_initial_shape_layer_name
            layer_name_is_in_use = rs.IsLayer(layer_name)   ##  None
            if layer_name_is_in_use:
                raise ValueError
        except ValueError:
            message = "The layer name '%s' is in use" % layer_name
            print("%s.%s:\n    %s" % (cls.__name__, method_name, message))
            return_value = None
        else:
            frame_instance_origin = (
                s.Settings.first_initial_shape_frame_position)
            return_value = cls._set_up_initial_shape(
                layer_name, frame_instance_origin)
        finally:
            return return_value

    @classmethod
    def set_up_subsequent_initial_shape(cls):
        """Prompts the user for a layer name. Adds a new layer with one frame. 
        Returns:
            layer_name      str. The name of the layer, if successful
            None            otherwise
        """
        layer_name = l.Layer.get_layer_name_from_user()
        frame_origin = f.Frame.get_frame_position_from_user()
        return_value = cls._set_up_initial_shape(
            layer_name, frame_origin)
        return return_value

    @classmethod
    def _set_up_initial_shape(cls, layer_name, frame_position):
        """Receives:
            layer_name      str. The name of the initial shape layer
            frame_position  Point3D. The position of the frame instance
        Returns:
        """
        value_1 = l.Layer.new(layer_name)
        frame_name = layer_name
        value_2 = f.Frame.new_instance(
            frame_name, layer_name, frame_position)
        if value_1 and value_2:
            return_value = layer_name
        else:
            return_value = None
        return return_value

    @classmethod
    def _set_up_first_rule(cls):
        """Adds a new layer with two frame instances. Should be executed only 
        once. Returns:
            layer_name      str. The name of the layer, if successful
            None            otherwise
        """
        method_name = '_set_up_first_rule'
        try:
            layer_name = s.Settings.first_rule_layer_name
            layer_name_is_in_use = rs.IsLayer(layer_name)
            if layer_name_is_in_use:
                raise ValueError
        except ValueError:
            message = "The layer name %s is in use" % layer_name
            print("%s.%s:\n    %s" % (cls.__name__, method_name, message))
            return_value = None
        else:
            layer_name = s.Settings.first_rule_layer_name
            left_frame_position = s.Settings.first_rule_left_frame_position
            return_value = cls._set_up_rule(layer_name, left_frame_position)
        finally:
            return return_value
        
    @classmethod
    def set_up_subsequent_rule(cls):
        """Prompts the user for a layer name. Adds a new layer with two 
        frames. Returns:
            layer_name      str. The name of the layer, if successful
            None            otherwise
        """
        layer_name = l.Layer.get_layer_name_from_user()
        frame_origin = f.Frame.get_frame_position_from_user()
        return_value = cls._set_up_rule(layer_name, frame_origin)
        return return_value

    @classmethod
    def _set_up_rule(cls, layer_name, left_frame_position):
        """Receives:
            layer_name      str. The name of the rule layer
            left_frame_position
                            Point3D. The position of the left frame instance
        Inserts left and right frame instances on the layer. Returns:
            layer_name      str. The name of the rule layer, if successful
            None            otherwise
        """
        value_1 = l.Layer.new(layer_name)
        left_frame_name = "%s_L" % layer_name
        right_frame_name = "%s_R" % layer_name
        right_frame_position = (
            s.Settings.get_right_frame_position(left_frame_position))
        value_2 = f.Frame.new_instance(
            left_frame_name, layer_name, left_frame_position)
        value_3 = f.Frame.new_instance(
            right_frame_name, layer_name, right_frame_position)
        if value_1 and value_2 and value_3:
            return_value = layer_name
        else:
            return_value = None
        return return_value

    # @classmethod
    # def import(cls):                            ##  can't use this word
    #     pass

    @classmethod                                ##  07-07 08:42
    def export(cls):
        """Writes the grammar's dat string to a file, if the grammar is well-
        formed. Returns:
            dat_string      str. The dat string, if successful
            None            otherwise
        """
        if not cls._is_well_formed():
            message = "%s %s" % (
                "The grammar must contain",
                "at least one initial shape and one rule")
            print(message)
            return_value = None
        else:
            name = cls.get_doc_name()
            dat_string = gd.get_dat_string()        ##  if not well-formed?
            cls._write_to_file(name, dat_string)    ##  if unsuccessful?
            return_value = dat_string
        return return_value

    @classmethod                                    ##  07-09 08:50
    def _is_well_formed(cls):
        """Returns:
            value           boolean. True, if the grammar contains at least 
                            one initial shape and one rule. False, otherwise
                                                    ##  empty shapes / rules?
        """
        layer_names = rs.LayerNames()
        contains_one_initial_shape, contains_one_rule = False, False
        for layer_name in layer_names:
            if l.Layer.contains_initial_shape(layer_name):
                contains_one_initial_shape = True
            if l.Layer.contains_rule(layer_name):
                contains_one_rule = True
        value = contains_one_initial_shape and contains_one_rule
        return value

    @classmethod
    def get_doc_name(cls):
        """Returns:
            name            str. The name of the Rhino document, if successful
            None            otherwise
        """
        name = rs.DocumentName()
        return name


    # @classmethod                                ##  not called
    # def _get_ordered_initial_shape_defs_string(cls):
        # """Returns:
        #     ordered_initial_shape_defs_string
        #                     str: str\nstr\n...\nstr. The string form of 
        #                     [str, ...], an ordered list (by name) of initial 
        #                     shape definitions, if successful
        #                     '' otherwise
        # """
        # ordered_ishapes = cls.get_initial_shapes()
        #                     ##  also in _get_ordered_lshapes_string()
        # ordered_ishape_defs = []
        # for ishape in ordered_ishapes:
        #     ishape_def = ish.InitialShape.get_def_from_ishape(ishape)
        #     ordered_ishape_defs.append(ishape_def)
        # ordered_initial_shape_defs_string = '\n'.join(ordered_ishape_defs)
        # return ordered_initial_shape_defs_string

    
    # @classmethod                                ##  not called
    # def _get_ordered_rule_defs_string(cls):
        # """Returns:
        #     ordered_rule_defs_string
        #                     str: str\nstr\n...\nstr. The string form of 
        #                     [str, ...], an ordered list (by name) of rule 
        #                     definition strings, if successful
        #                     '' otherwise
        # """
        # ordered_rules = cls.get_rules()
        # ordered_rule_defs = []
        # for rule_i in ordered_rules:
        #     rule_def = r.Rule.get_def_from_rule(rule_i)
        #     ordered_rule_defs.append(rule_def)
        # ordered_rule_defs_string = '\n'.join(ordered_rule_defs)
        # return ordered_rule_defs_string

    @classmethod
    def _write_to_file(cls):
        pass

    ####

    @classmethod
    def get_labeled_shape_layer_names(cls):
        """The grammar is guaranteed to be well-formed. Returns:
            labeled_shape_layer_names
                            [str, ...]. A list of the names of the labeled 
                            shapes in initial shapes or rules, i.e., name, 
                            name_L, or name_R
        """
        labeled_shape_layer_names = []
        layer_names = rs.LayerNames()
        for layer_name in layer_names:
            if l.Layer.contains_initial_shape(layer_name):
                labeled_shape_layer_names.append(layer_name)
            elif l.Layer.contains_rule(layer_name):
                left_name = "%s_L" % layer_name
                right_name = "%s_R" % layer_name
                labeled_shape_layer_names.extend([left_name, right_name])
        return labeled_shape_layer_names

    @classmethod
    def get_initial_shapes(cls):                ##  07-03 14:53
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
    # @classmethod
    # def _get_ishape_lshape_strings():           ##  06-08 09:32
        # """Returns:
        #     ishape_lshape_strings
        #                 [str, ...]. A list of lshape strings of the 
        #                 grammar's initial shapes
        # """
        # ishape_lshape_strings = []
        # ishapes = cls.get_initial_shapes()
        # for ishape in ishapes:
        #     lshape_string = cls._get_lshape_string_from_ishape(ishape)
        #     ishape_lshape_strings.append(lshape_string)
        # return ishape_lshape_strings

    # @classmethod
    # def _get_rule_lshape_strings():
        # """Returns:
        #     rule_lshape_strings
        #                 [str, ...]. A list of lshape strings of the 
        #                 grammar's rules
        # """
        # rule_lshape_strings = []
        # rules = cls.get_rules()
        # for rule in rules:
        #     lshape_string_pair = cls._get_lshape_string_pair_from_rule(rule)
        #     rule_lshape_strings.extend(lshape_string_pair)
        # return rule_lshape_strings

    @classmethod
    def clear_all(cls):
        cls._clear_objects()
        cls._clear_blocks()
        cls._clear_layers()
        cls._clear_data()
        # cls._clear_groups()

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
