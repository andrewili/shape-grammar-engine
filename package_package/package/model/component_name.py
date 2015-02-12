from package.model import initial_shape as ish
from package.model import llist as ll
from package.model import rule as r
from package.model import shape_layer as sl
import rhinoscriptsyntax as rs

class ComponentName(object):
    component_types = {'initial shape', 'rule', 'shape'}
    prohibited_characters = {' ', '#'}


    def __init__(self):
        pass

    @classmethod
    def get_initial_shape_name_from_user(cls):
        return_value = cls.get_component_name_from_user(
            ish.InitialShape.component_type)
        return return_value

    @classmethod
    def get_rule_name_from_user(cls):           
        return_value = cls.get_component_name_from_user(
            r.Rule.component_type)
        return return_value

    @classmethod
    def get_shape_name_from_user(cls):
        return_value = cls.get_component_name_from_user(
            sl.ShapeLayer.component_type)
        return return_value

    @classmethod
    def get_component_name_from_user(cls, component_type):
        """Receives:
            component_type  str (validated upstream)
                            {'initial shape' | 'rule' | 'shape'}
        Prompts the user for a user name that is available and well formed. 
        Returns:
            str             the component name, if successful
            None            otherwise
        """
        method_name = 'get_component_name_from_user'
        first_message = "%s %s" % (
            "%s %s %s" % (
                "Enter the", component_type, "name."),
            "It must be unique and contain no spaces or '#' characters")
        error_message = "%s %s %s" % (
            "That name is already being used",
            "or it contains spaces or '#' characters.",
            "Try again")
        component_name = rs.GetString(first_message)
        while not (
            not(cls._component_name_is_listed(
                component_type, component_name)) and
            cls._component_name_is_well_formed(component_name)
        ):
            component_name = rs.GetString(error_message)
        return_value = component_name
        return return_value

    @classmethod
    def _component_name_is_listed(cls, component_type, component_name):
        """Receives:
            component_type  str (validated upstream)
                            {'initial_shape' | 'rule' | 'shape'}
            component_name  str (validated upstream)
        Determines whether the component name is recorded. Returns:
            boolean         True or False
        """
        method_name = '_component_name_is_listed'
        try:
            if not component_type in cls.component_types:
                raise ValueError
        except ValueError:
            message = "%s %s" % (
                "The component type must be",
                "'initial shape', 'rule', or 'shape'")
            print("%s.%s:\n    %s" % (cls.__name__, method_name, message))
            return_value = False
        else:
            if component_type == 'initial shape':
                component_name_list_name = (
                    ish.InitialShape.initial_shape_name_list_name)
            elif component_type == 'rule':
                component_name_list_name = r.Rule.rule_name_list_name
            elif component_type == 'shape':
                component_name_list_name = sl.ShapeLayer.shape_layer_list_name
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

