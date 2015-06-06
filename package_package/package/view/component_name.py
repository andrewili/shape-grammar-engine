from package.view import grammar as g
from package.view import initial_shape as ish
from package.view import llist as ll
from package.view import rule as r
from package.view import shape_layer as sl
import rhinoscriptsyntax as rs

class ComponentName(object):
    component_types = {'initial shape', 'rule'}
    prohibited_characters = {' ', '#'}

    def __init__(self):
        pass

    @classmethod
    def get_initial_shape_name_from_user(cls):
        """Gets a valid initial shape name from the user. Returns:
            name            str. A valid initial shape name
        """
        return_value = cls.get_component_name_from_user(
            ish.InitialShape.component_type)
        return return_value

    @classmethod
    def get_rule_name_from_user(cls):
        """Gets a valid rule name from the user. Returns:
            name            str. A valid rule name
        """
        return_value = cls.get_component_name_from_user(
            r.Rule.component_type)
        return return_value

    @classmethod
    def get_component_name_from_user(cls, component_type):
        """Receives:
            component_type  str: {'initial shape' | 'rule'}
        Prompts the user for a name that is available and well formed. 
        Returns:
            name            str. The component name, if successful
            None            otherwise
        """
        method_name = 'get_component_name_from_user'
        first_message = "%s %s" % (
            "%s %s %s" % ("Enter the", component_type, "name."),
            "It must be unique and contain no spaces or '#' characters")
        error_message = "%s %s %s" % (
            "That name is already being used",
            "or it contains spaces or '#' characters.",
            "Try again")
        component_name = rs.GetString(first_message)
        while not (
            cls._component_name_is_available(component_name) and
            cls._component_name_is_well_formed(component_name)
        ):
            component_name = rs.GetString(error_message)
        return_value = component_name
        return return_value

    @classmethod
    def _component_name_is_available(cls, name):
        """Receives:
            name            str
        Returns:
            boolean         True, if the name is available for use (i.e., not 
                            in the grammar's list of initial shapes or in its
                            list of rules)
        """
        value = not (
            ll.Llist.contains_entry(g.Grammar.initial_shapes, name) or
            ll.Llist.contains_entry(g.Grammar.rules, name))
        return value

    @classmethod
    def _component_name_is_listed(cls, component_name, component_type):
        """Receives:
            component_name  str (validated upstream)
            component_type  str (validated upstream): {
                                ish.InitialShape.component_type | 
                                r.Rule.component_type}
        Determines whether the component name is in either the grammar's list 
        of initial shapes or its list of rules. Returns:
            boolean         True or False
        """
        method_name = '_component_name_is_listed'
        try:
            if not component_type in cls.component_types:
                raise ValueError
        except ValueError:
            message = "%s %s" % (
                "The component type must be",
                "'%s' or '%s'" % (
                    ish.InitialShape.component_type, 
                    r.Rule.component_type))
            print("%s.%s:\n    %s" % (cls.__name__, method_name, message))
            print("You gave: '%s'" % component_type)
            return_value = False
        else:
            if component_type == ish.InitialShape.component_type:
                component_name_list_name = (
                    g.Grammar.initial_shapes)
            elif component_type == r.Rule.component_type:
                component_name_list_name = g.Grammar.rules
            else:
                pass
            return_value = ll.Llist.contains_entry(
                component_name_list_name, component_name)
        finally:
            return return_value

    @classmethod
    def _component_name_is_well_formed(cls, component_name):
        """Receives:
            component_name  str (validated upstream)
        Determines whether the component name is well formed. Returns:
            boolean         True or False
        """
        return_value = True
        for character in cls.prohibited_characters:
            if character in component_name:
                return_value = False
                break
        return return_value

    @classmethod
    def record_component_name(cls, component_type, component_name):
        pass

