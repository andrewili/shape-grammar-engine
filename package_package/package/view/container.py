from package.view import frame_block as fb
from package.view import grammar as g
import rhinoscriptsyntax as rs

class Container(object):
    color = 'black'
    initial_shape_offset = (10, 10, 0)
    left_shape_offset = (10, 10, 0)
    right_shape_offset = (50, 10, 0)
    def __init__(self):
        pass

    @classmethod
    def new(cls, name, origin, ttype):          ##  05-31 09:13
        """Receives:
            name            str. The name of the component. Guaranteed to be 
                            valid by the calling method 
            origin          Point3d. The local origin of the container. z = 0
            ttype           str: 'initial shape' | 'rule'. The type of the 
                            component
        Creates a new component layer. Adds it to the grammar's appropriate 
        list. Returns:
            name            str. The name of the component, if successful
            None            otherwise
        """
        rs.AddLayer(name, cls.color)
        rs.CurrentLayer(name)
        if ttype == 'initial shape':
            cls.add_initial_shape_frame_block(name, origin)
            g.Grammar.add_to_initial_shape_list(name)   ##  06-01 08:15
        elif ttype == 'rule':
            cls.add_rule_frame_blocks(name, origin)
            g.Grammar.add_to_rule_list(name)
        else:
            pass
        cls.add_name_tag(name, origin)
        rs.CurrentLayer('Default')
        return name

    @classmethod
    def add_initial_shape_frame_block(cls, name, origin):
        """Receives:
            name            str. The name of the initial shape
            origin          Point3d. The origin of the container. z = 0
        Adds a frame block at the appropriate point. Returns:
            name            str. The name of the initial shape, if successful
            None            otherwise
        """
        position = rs.PointAdd(origin, cls.initial_shape_offset)
        guid = fb.FrameBlock.insert(position)
        if guid:
            return name
        else:
            return None

    @classmethod
    def add_rule_frame_blocks(cls, name, origin):
        """Receives:
            name            str. The name of the rule
            origin          Point3d. The origin of the container. z = 0
        Adds left and right frame blocks at the appropriate points. Returns:
            name            str. The name of the rule, if successful
            None            otherwise
        """
        left_shape_position = rs.PointAdd(origin, cls.left_shape_offset)
        right_shape_position = rs.PointAdd(origin, cls.right_shape_offset)
        left_shape_guid = fb.FrameBlock.insert(left_shape_position)
        right_shape_guid = fb.FrameBlock.insert(right_shape_position)
        if left_shape_guid and right_shape_guid:
            return name
        else:
            return None

    @classmethod
    def add_name_tag(cls, name, origin):
        """Receives:
            origin          Point3d. The origin of the container. z = 0
        Adds a name tag at the appropriate point. Returns:
            name            str. The name of the component, if successful
            None            otherwise
        """
        pass

