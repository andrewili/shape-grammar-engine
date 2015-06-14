from package.view import component_name as cn
import rhinoscriptsyntax as rs

class LabeledPoint(object):
    text_height = 2

    def __init__(self):
        pass

    @classmethod
    def draw(cls):
        """Prompts the user for a label and an insertion point. Draws a group 
        consisting of a text object and a point marker. Returns: 
            guid            of the group, if successful
            None            otherwise
        """
        pass
        # label = 
        # point_marker = 
        # return_value = make_group(label, point_marker)
        # return return_value

    @classmethod
    def new(cls, label, point):
        """Draws a new labeled point (Rhino text object). Receives:
            label           str
            point           Point3d or [num, num, num] or (num, num, num)
        Both arguments are validated upstream, but we're checking again. 
        Returns:
            guid            the ID of the labeled point, if successful
            None            otherwise
        """
        method_name = 'new'
        try:
            if not (
                type(label) == str and (
                    type(point) == list or
                    type(point) == tuple or
                    rs.IsPoint(point))
            ):
                raise TypeError
            if not (cn.ComponentName._is_well_formed(label)):
                raise ValueError
        except TypeError:
            message = "The arguments must be a string and a point (or triple)"
            print("%s.%s:\n    %s" % (cls.__name__, method_name, message))
            return_value = None
        except ValueError:
            message = "The label must not contain spaces or #s"
            print("%s.%s:\n    %s" % (cls.__name__, method_name, message))
            return_value = None
        else:
            guid = rs.AddText(label, point, cls.text_height)
            return_value = guid
        finally:
            return return_value

