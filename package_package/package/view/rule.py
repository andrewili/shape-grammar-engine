from package.view import container as c
from package.view import component_name as cn
from package.view import dictionary as d
from package.view import frame as f
from package.view import insertion_point as ip
from package.view import settings as s
from package.view import shape_layer as sl
import rhinoscriptsyntax as rs

class Rule(object):
    # component_type = 'rule'
    # first_rule_name = 'rule_1'
    # first_rule_insertion_point = [0, -100, 0]
    # tag_offset = [-10, 0, 0]
    # right_shape_offset_x_factor = 1.5
    # rule_name_list_name = 'rule names'
    # text_height = 2
    # left_lshape_suffix = '_L'
    # right_lshape_suffix = '_R'

    def __init__(self):
        pass

    @classmethod
    def set_up_first(cls):                      ##  06-19 23:22
        """Adds a new layer, named <name>. Inserts 2 frame blocks, named 
        <name>_L and <name>_R. <name> = cls.first_rule_name. 
        Should be executed only once. Returns:
            name            str. The name of the rule, if successful
            None            otherwise
        """
        method_name = 'set_up_first'
        try:
            if not required_name_is_available:
                raise ValueError
        except ValueError:
            message = "The first rule name is not available"
            print("%s.%s: %s" % (cls.__name__, method_name, message))
            return_value = None
        else:
            name = s.Settings.first_rule_name
            color = s.Settings.layer_color
            layer_name = rs.AddLayer(name, color)
            rs.CurrentLayer(layer_name)
            left_lshape_name = "%s_L" % name
            right_lshape_name = "%s_R" % name
            left_lshape_position = s.Settings.first_rule_lshape_origin
            right_lshape_position = s.Settings.get_right_lshape_position(
                left_lshape_position)
            left_block_guid = f.Frame.insert(
                left_lshape_name, left_lshape_position)
            right_block_guid = f.Frame.insert(
                right_lshape_name, right_position)
            rs.CurrentLayer(s.Settings.default_layer_name)
            if not (layer_name and left_block_guid and right_block_guid):
                return_value = None
            else:
                return_value = name
        finally:
            return return_value

    @classmethod
    def add_first(cls):                         ##  'add_first_container'?
        """Adds and names a new layer. Inserts two shape frame blocks at 
        predetermined insertion points. Should be executed only once. Returns:
            str             cls.first_rule_name, if successful
            None            otherwise
        """
        name = cls.first_rule_name
        insertion_point = cls.first_rule_insertion_point
        value = c.Container.new(name, insertion_point, cls.component_type)
        if value:
            return name
        else:
            return None

    @classmethod
    def add_subsequent(cls):
        """Prompts the user for a name and an insertion point. Adds a new 
        layer with the name. Inserts two frame blocks. Returns:
            name            str. The name of the new rule, if successful
            None            otherwise
        """
        name = cn.ComponentName.get_rule_name_from_user()
        while not cn.ComponentName._is_available(name):
            name = cn.ComponentName.get_rule_name_from_user()
        insertion_point = ip.InsertionPoint.get_insertion_point_from_user()
        return_value = c.Container.new(
            name, insertion_point, cls.component_type)
        return return_value

    @classmethod
    def get_def_from_rule(cls, name):           ##  bad cases?
        """Receives:
            name            str. The name of a rule. Type and value guaranteed
        Returns:
            definition      str in the form:
                                rule    <name>    <name>_L -> <name>_R
                            The definition of the rule
        """
        definition = "rule    %s    %s_L -> %s_R" % (name, name, name)
        return definition

    @classmethod
    def get_lshape_pair_from_rule(cls, rule):
        """Receives:
            rule            str. The name of a rule. Value guaranteed
        Returns:
            lshape_pair     (str, str). A 2-tuple of the rule's left and right 
                            labeled shape names, if successful
            None            otherwise
        """
        left_lshape = "%s%s" % (rule, cls.left_lshape_suffix)
        right_lshape = "%s%s" % (rule, cls.right_lshape_suffix)
        return (left_lshape, right_lshape)

    @classmethod
    def _add_tag(cls, rule_name, tag_position):
        """Receives:
            rule_name       str
            tag_position    Point3d, z = 0
        Adds the rule name as a text object. Returns:
            guid            the guid of the tag, if successful
            None            otherwise
        """
        return_value = rs.AddText(rule_name, tag_position, cls.text_height)
        return return_value

    @classmethod
    def _get_shape_name_from_rule_name(cls, rule_name, side):
        """Receives:
            rule_name       str; validated upstream
            side            str {'left' | 'right'}
        Creates the name of the left or right shape, as specified. Returns:
            str             the shape name, if successful
            None            otherwise
        """
        method_name = '_get_shape_name_from_rule_name'
        try:
            if not type(side) == str:
                raise TypeError
            if not (
                side == 'left' or
                side == 'right'
            ):
                raise ValueError
        except TypeError:
            message = "The side must be a string: 'left' or 'right'"
            print("%s.%s:\n    %s" % (cls.__name__, method_name, message))
            return_value = None
        except ValueError:
            message = "The side must be 'left' or 'right'"
            print("%s.%s:\n    %s" % (cls.__name__, method_name, message))
            return_value = None
        else:
            if side == 'left':
                suffix = '_L'
            elif side == 'right':
                suffix = '_R'
            else:
                pass
            return_value = "%s%s" % (rule_name, suffix)
        finally:
            return return_value

    @classmethod
    def _get_right_shape_position(cls, left_shape_position):
        """Receives:
            left_shape_position
                            Point3d. Validated upstream. 
        Calculates the position of the right shape. Returns:
            Point3d
        """
        frame_size_x = f.Frame.size[0]
        offset_x = frame_size_x * cls.right_shape_offset_x_factor
        offset = [offset_x, 0, 0]
        right_shape_position = rs.PointAdd(left_shape_position, offset)
        return right_shape_position

    @classmethod
    def _record(cls, rule_name, left_shape_name, right_shape_name):
        """Receives:
            rule_name       str
            left_shape_name str
            right_shape_name
                            str
        Records the rule name, the left shape name, and the right shape name 
        in the rule name list. Returns:
            str             the rule name, if successful
            None            otherwise
        """
        method_name = '_record'
        try:
            if not (
                type(rule_name) == str and
                type(left_shape_name) == str and
                type(right_shape_name) == str
            ):
                raise TypeError
        except TypeError:
            message = "The arguments must be strings"
            print("%s.%s:\n    %s" % (cls.__name__, method_name, message))
            return_value = None
        else:
            shape_name_pair = "%s %s" % (left_shape_name, right_shape_name)
            return_value = d.Dictionary.set_value(
                cls.rule_name_list_name, rule_name, shape_name_pair)
        finally:
            return return_value

    @classmethod
    def export(cls):                            ##  to do
        """Writes the rule's repr string (rul format) to a file. Returns:
            rule_name       str. The rule's name, if successful
            None            otherwise
        """
        return rule_name

    @classmethod
    def get_repr(cls, rule):                    ##  05-26 07:24
        """Receives:
            rule            str. The rule's name
        Returns:
            rule_repr       str. The rule's repr string, if successful
            None            otherwise
        """
        left_lshape_guids, right_lshape_guids = Rule.get_guids(rule)
        left_lshape_spec = LabeledShape.get_spec_from_lshape_guids(
            left_lshape_guids, left_lshape_origin)
        right_lshape_spec = LabeledShape.get_spec_from_lshape_guids(
            right_lshape_guids, right_lshape_origin)
        left_lshape_repr = get_repr_from_lshape_spec(
            left_lshape_spec)
        right_lshape_repr = get_repr_from_lshape_spec(
            right_lshape_spec)
        rule_repr = cls.get_rule_repr_from_lshape_reprs(
            left_lshape_repr, right_lshape_repr)
        return rule_repr

    @classmethod
    def get_guids(cls, rule):
        """Receives:
            rule            str. The name of a rule
        Returns:
            left_lshape_guids
                            [guid, ...]. A list of the element guids in the 
                            left labeled shape
            right_lshape_guids
                            [guid, ...]. A list of the element guids in the 
                            right labeled shape
        """
        return (left_lshape_guids, right_lshape_guids)

