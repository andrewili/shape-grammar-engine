from package.view import layer as l
from package.view import llist as ll
import rhinoscriptsyntax as rs

class Exporter(object):
    def __init__(self):
        self.class_name = 'Exporter'

    def export_grammar(self):
        """Prompts the user for a name; suggests the Rhino file name. Writes 
        the grammar's repr string to a file named <name>.dat.
        """
        name = _get_name()
        initial_shape_specs = self._get_specs_from_initial_shape_guids(
            initial_shape_guids)
        rule_specs = self._get_specs_from_rule_guids(rule_guids)
        grammar_spec = (initial_shape_specs, rule_specs)
        grammar_repr = _get_repr_from_grammar_spec(grammar_spec)
        self._write_grammar_repr_to_file(grammar_repr)

    def export_component(self):
        """Prompts the user to select an initial shape or a rule. Writes the 
        component's repr string to a file named <component_name>.<suffix>, 
        suffix: <is> | <rul>.
        """
        pass

    def export_initial_shape(self):
        pass

    def export_rule(self):
        """Prompts the user to select items specifying a rule. Writes the
        rule's repr string to a file named <rule_name>.rul. Returns:
            repr_string     string
        """
        rule_item = self._request_rule_item()
        rule_name = self._get_name_from_rule_item(rule_item)
        rule_spec = self._get_spec_from_rule_name(rule_name)
        rule_repr = self._get_repr_from_rule_spec(rule_spec)
        self._write_rule_file(rule_repr)
        return rule_repr

    def _request_rule_item(self):               ##  05.19 10:42
                                                ##  Reject initial shape items
        """Prompts the user to select an item to specify a rule. Returns:
            rule_item       guid
        """
        message = "Select an item in the rule"
        rule_item = rs.GetObject(message)
        return rule_item

    # def _get_name_from_rule_item(self, rule_item):  ##  05-18 19:36
    #     """Receives:
    #         rule_item       guid
    #     Returns:
    #         rule_name       str. The name of the rule associated with the item
    #     """
    #     rule_name = self._get_rule_from_guid(rule_item)
    #     return rule_name

        # selected_items = rs.SelectedObjects()
        # message = "Select one or more elements in one rule"
        # ffilter = 0
        # group = True
        # preselect = False
        # select = True
        # while not self._one_rule_is_specified_by(selected_items):
        #     selected_items = rs.GetObjects(
        #         message, ffilter, group, preselect, select)
        # return selected_items

    # def _one_rule_is_specified_by(self, guids):
        # """Receives:
        #     guids           [guid, ...]
        # Returns:
        #     boolean         True, if the guids all specify the same rule
        #                     False, otherwise
        # """
        # return_value = True
        # if len(guids) == 0:
        #     return_value = False
        # else:
        #     first_guid = guids[0]
        #     first_specified_rule = self._get_rule_from_guid(first_guid)
        #     for guid in guids:
        #         specified_rule = self._get_rule_from_guid(guid)
        #         if not specified_rule == first_specified_rule:
        #             return_value = False
        #             break
        # return return_value

    def _get_name_from_rule_item(self, rule_item):
        """Receives:
            rule_item       guid
        Returns:
            rule_name       str. The name of the rule, if any, associated with 
                            the layer containing the guid, if successful
            None            Otherwise
        """
        default_layer = 'Default'
        guid_layer = rs.ObjectLayer(rule_item)
        if self._is_a_shape_layer(guid_layer):
            rule_name = self._get_rule_name_from_shape_layer(guid_layer)
        elif guid_layer == default_layer:
            rule_name = rs.TextObjectText(rule_item)
        else:
            rule_name = None
        return rule_name

    def _is_a_shape_layer(self, guid_layer):
        """Receives:
            guid_layer      str. The name of a layer
        Returns:
            boolean         True, if the named layer is a shape layer
        """
        list_name = l.Layer.layer_name_list_name
        value = ll.Llist.contains_entry(list_name, guid_layer)
        return value

    def _get_rule_name_from_shape_layer(self, guid_layer):
        """Receives:
            guid_layer      str. The name of a shape layer
        Returns:
            rule_name       str. The name of the rule containing the shape
        """
        rule_name = guid_layer[:-2]
        return rule_name

    # def _get_name_from_rule_item(self, guids): ##  05-18 12:18
        # """Receives:
        #     [guid, ...]     guids of the selected items. guids are guaranteed 
        #                     to be associated with the same rule
        # Returns:
        #     rule_name       str. The name of the rule specified by the 
        #                     items
        # """
        # rule_name = 'kilroy'
        # return rule_name

    def _get_spec_from_rule_name(self, rule_name):
        """Receives:
            rule_name       str. The name of a rule
        Returns:
            rule_spec       (name, line_specs, lpoint_specs)
        """
        pass

    def _get_repr_from_rule_spec(self, rule_spec):
        """Receives:
            rule_spec       (name, line_specs, lpoint_specs)
        Returns:
            rule_repr       str
        """
        pass

    def _write_rule_file(self, rule_repr):
        """Receives:
            rule_repr       str
        """
        pass

