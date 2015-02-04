from package.model import frame_block as fb
from package.model import layer as l
import rhinoscriptsyntax as rs

class ShapeLayer(object):                       ##  difference from Layer?
    def __init__(self):
        pass

    @classmethod
    def new(cls, shape_name, position):
        """Receives:
            shape_name      str
            position        [num, num, num]
        Used for initial shapes, left rule shapes, and right rule shapes.
        Creates a new shape-layer. Inserts a shape frame. Returns:
            str             shape_name, if successful
            None            otherwise
        """
        method_name = 'new'
        try:
            if not (
                type(shape_name) == str and
                type(position) == list
            ):
                raise TypeError
            if not (
                not l.Layer.layer_name_is_in_use(shape_name) and
                position[2] == 0
            ):
                raise ValueError
        except TypeError:
            message = "%s.%s: %s" % (
                cls.__name__,
                method_name,
                "The arguments must be a string and a point")
            print(message)
            return_value = None
        except ValueError:
            message = "%s.%s: %s" % (
                cls.__name__,
                method_name,
                "%s %s" % (
                    "The shape name must be available",
                    "and the position must be on the xy plane"))
            print(message)
            return_value = None
        else:
            l.Layer.new(shape_name)
            rs.CurrentLayer(shape_name)
            guid = fb.FrameBlock.insert(position)
            rs.CurrentLayer('Default')
            if guid:
                return_value = shape_name
            else:
                return_value = None
        finally:
            return return_value
