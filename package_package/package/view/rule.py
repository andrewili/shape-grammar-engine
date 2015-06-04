from package.view import container as c
from package.view import component_name as cn
from package.view import dictionary as d
from package.view import frame as f
from package.view import insertion_point as ip
from package.view import shape_layer as sl
import rhinoscriptsyntax as rs

class Rule(object):
    component_type = 'rule'
    first_rule_name = 'rule_1'
    first_rule_origin = [0, -100, 0]
    tag_offset = [-10, 0, 0]
    right_shape_offset_x_factor = 1.5           ##  centralize presentation info?
    rule_name_list_name = 'rule names'
    text_height = 2
    
    @classmethod
    def add_first(cls):
        """Adds and names a new layer. Inserts two shape frame blocks at 
        predetermined positions. Should be executed only once. Returns:
            str             cls.first_rule_name, if successful
            None            otherwise
        """
        name = cls.first_rule_name
        origin = cls.first_rule_origin
        value = c.Container.new(name, origin, cls.component_type)
        if value:
            return name
        else:
            return None

    @classmethod
    def add_subsequent(cls):
        """Prompts the user for a name and a position. Adds a new shape 
        layer pair. Inserts a shape frame block on each layer. Returns:
            str             the name of the new rule, if successful
            None            otherwise
        """
        rule_name = cn.ComponentName.get_component_name_from_user(
            cls.component_type)
        point = ip.InsertionPoint.get_insertion_point_from_user()
        return_value = cls._new(rule_name, point)
        return return_value

    @classmethod
    def _new(cls, rule_name, position):         ##  04-26 08:26
        """Receives validated arguments:
            rule_name       str; validated upstream
            position        Point3d; validated upstream
        Creates a new rule. Records it in the rule name list. Returns:
            str             the name of the rule, if successful
            None            otherwise
        """
        method_name = '_new'
        (   left_shape_name,
            left_shape_position,
            right_shape_name,
            right_shape_position
        ) = (
            cls._get_shape_name_from_rule_name(rule_name, 'left'),
            position,
            cls._get_shape_name_from_rule_name(rule_name, 'right'),
            cls._get_right_shape_position(position)
        )
        tag_position = rs.PointAdd(position, cls.tag_offset)
        tag_guid = cls._add_tag(rule_name, tag_position)
        left_shape = sl.ShapeLayer.new(
            left_shape_name, left_shape_position)
        right_shape = sl.ShapeLayer.new(
            right_shape_name, right_shape_position)
        recorded_rule = cls._record(
            rule_name, left_shape_name, right_shape_name)
        if (left_shape and
            right_shape and
            recorded_rule
        ):
            return_value = rule_name
        else:
            return_value = None
        return return_value

    @classmethod
    def new(cls, name, origin):                 ##  05-25 13:36
        """Receives:
            name            str. The name of the rule
            origin          Point3d. The origin of the rule, z = 0
        Creates a rule layer. Adds it to the grammar's list of rules. Returns:
            name            str. The name of the rule, if successful
            None            otherwise
        """
        pass

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

