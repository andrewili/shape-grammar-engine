from package.model import dictionary as d
from package.model import frame as f
from package.model import llist as ll
from package.model import shape_layer as sl
import rhinoscriptsyntax as rs

class Rule(object):
    first_rule_name = 'rule_1'
    first_rule_position = [0, -40, 0]
    right_shape_offset_x_factor = 1.5           ##  centralize presentation info?
    rule_name_list_name = 'rule names'

    def __init__(self):
        pass

    @classmethod
    def add_first(cls):
        """Adds a pre-named new shape layer pair. Inserts a shape frame block 
        at a predetermined position on each layer. Should be executed only 
        once. Returns:
            str             cls.first_rule_name, if successful
            None            otherwise
        """
        if not cls._rule_name_is_available(cls.first_rule_name):
            return_value = None
        else:
            rule_made = cls._new(cls.first_rule_name, cls.first_rule_position)
            if rule_made:
                return_value = cls.first_rule_name
            else:
                return_value = None
        return return_value

    @classmethod                                ##  02-11 04:07
    def add_subsequent(cls):                    ##  Name class?
        """Prompts the user for a name and a position. Adds a new shape 
        layer pair. Inserts a shape frame block on each layer. Returns:
            str             the name of the new rule, if successful
            None            otherwise
        """
        name_message_1 = "%s %s %s" % (
            "Enter the rule name.",
            "It must be unique and",
            "contain no spaces or '#' characters")
        name_message_2 = "%s %s %s" % (
            "That name either is already used",
            "or contains spaces or '#' characters.",
            "Please try again")
        rule_name = rs.GetString(name_message_1)
        while not (
            cls._rule_name_is_available(rule_name) and
            cls._rule_name_is_well_formed(rule_name)
        ):
            rule_name = rs.GetString(name_message_2)
        point_message_1 = "Pick a point in the xy plane"
        point_message_2 = "%s %s" % (
            "The point must be in the xy plane.",
            "Please try again")
        point = rs.GetPoint(point_message_1)
        while not point[2] == 0:
            point = rs.GetPoint(point_message_2)
        return_value = cls._new(rule_name, point)
        return return_value

    @classmethod
    def _rule_name_is_available(cls, rule_name):
        """Receives:
            rule_name       str
        Returns:
            boolean         True or False
        """
        return_value = not(ll.Llist.contains_entry(
            cls.rule_name_list_name, rule_name))
        return return_value

    @classmethod
    def _rule_name_is_well_formed(cls, rule_name):
        """Receives:
            rule_name       str
        Determines whether the rule name is well formed. Returns:
            boolean         True or False
        """
        prohibited_characters = [' ', '#']
        return_value = True
        for character in prohibited_characters:
            if character in rule_name:
                return_value = False
                break
        return return_value

    @classmethod
    def _new(cls, rule_name, position):
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
        left_shape = sl.ShapeLayer.new(
            left_shape_name, left_shape_position)
        right_shape = sl.ShapeLayer.new(
            right_shape_name, right_shape_position)
        recorded_rule = cls._record_rule(
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
    def _record_rule(cls, rule_name, left_shape_name, right_shape_name):
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
        method_name = '_record_rule'
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

