from package.view import frame as f
from package.view import component_name as cn
from package.view import grammar as g
from package.view import initial_shape as ish
from package.view import rule as r
import rhinoscriptsyntax as rs

class Container(object):                        ##  06-19 16:57
    color = 'black'                             ##  combine with LabeledShape?
    initial_shape_offset = (10, 10, 0)
    left_shape_offset = (10, 10, 0)
    right_shape_offset = (50, 10, 0)
    name_tag_offset = (-10, 0, 0)

    def __init__(self):
        pass

    @classmethod
    def new(cls, name, origin, ttype):
        """Receives:
            name            str. The name of the component. Type and valued 
                            guaranteed
            origin          Point3d. The local origin of the container. Type 
                            and value guaranteed
            ttype           str: {'initial shape' | 'rule'}. The type of the 
                            component. Type and value guaranteed
        Creates a new component layer, with name tag and one (initial shape) 
        or two (rule) frame blocks. Returns: 
            name            str. The name of the component, if successful
            None            otherwise
        """
        rs.AddLayer(name, cls.color)
        rs.CurrentLayer(name)
        if ttype == ish.InitialShape.component_type:
            cls._add_initial_shape_frame_block(name, origin)
        elif ttype == r.Rule.component_type:
            cls._add_rule_frame_blocks(name, origin)
        else:
            pass
        tag_guid = cls._add_name_tag(name, ttype, origin)
        actual_name = rs.TextObjectText(tag_guid)
        return_value = actual_name
        rs.CurrentLayer('Default')
        return return_value

    @classmethod
    def _add_initial_shape_frame_block(cls, name, origin):
        """Receives:
            name            str. The name of the initial shape. Value verified
            origin          Point3d. The origin of the container
        Adds a frame block at the appropriate point. Returns:
            name            str. The name of the initial shape, if successful
            None            otherwise
        """
        position = rs.PointAdd(origin, cls.initial_shape_offset)
        guid = f.Frame.insert(position)
        if guid:
            return name
        else:
            return None

    @classmethod
    def _add_rule_frame_blocks(cls, name, origin):
        """Receives:
            name            str. The name of the rule. Value verified
            origin          Point3d. The origin of the container
        Adds left and right frame blocks at the appropriate points. Returns:
            name            str. The name of the rule, if successful
            None            otherwise
        """
        left_shape_position = rs.PointAdd(origin, cls.left_shape_offset)
        right_shape_position = rs.PointAdd(origin, cls.right_shape_offset)
        left_shape_guid = f.Frame.insert(left_shape_position)
        right_shape_guid = f.Frame.insert(right_shape_position)
        if left_shape_guid and right_shape_guid:
            return name
        else:
            return None

    @classmethod
    def _add_name_tag(cls, name, component_type, origin):
        """Receives:
            name            str. The name of the container. Type and value 
                            guaranteed
            component_type  str: {'initial shape' | 'rule'}. Type and value 
                            guaranteed
            origin          Point3d. The origin of the container 
                                    ##  Position of the name tag? 
        Adds a name tag at the appropriate point. Adds it to the appropriate 
        Rhino group (i.e., initial shape or rule). Returns:
            guid            str. The guid of the component, if successful
            None            otherwise
        """
        position = rs.PointAdd(origin, cls.name_tag_offset)
        height = 2
        guid = rs.AddText(name, position, height)
        if not guid:
            return_value = None
        else:
            if not rs.IsGroup(component_type):
                rs.AddGroup(component_type)
            value = rs.AddObjectToGroup(guid, component_type)
            if value:
                return_value = guid
            else:
                return_value = None
        return return_value


