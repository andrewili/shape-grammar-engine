from package.view import frame_block as fb
from package.view import grammar as g
from package.view import initial_shape as ish
from package.view import rule as r
import rhinoscriptsyntax as rs

class Container(object):
    color = 'black'
    initial_shape_offset = (10, 10, 0)
    left_shape_offset = (10, 10, 0)
    right_shape_offset = (50, 10, 0)
    name_tag_offset = (-10, 0, 0)

    def __init__(self):
        pass

    @classmethod
    def new(cls, name, origin, ttype):
        """Receives:
            name            str. The name of the component
            origin          Point3d. The local origin of the container. z = 0
            ttype           str: 'initial shape' | 'rule'. The type of the 
                            component
        Creates a new component layer, with name tag and one (initial shape) 
        or two (rule) frame blocks. Adds the layer to the grammar's initial 
        shape list or its rule list. Returns: 
            name            str. The name of the component, if successful
            None            otherwise
        """
        try:
            if g.Grammar.component_name_is_in_use(name):
                raise ValueError
        except ValueError:
            return_value = None
        else:
            rs.AddLayer(name, cls.color)
            rs.CurrentLayer(name)
            if ttype == ish.InitialShape.component_type:
                cls._add_initial_shape_frame_block(name, origin)
                return_value = g.Grammar.add_to_initial_shapes(name)
            elif ttype == r.Rule.component_type:
                cls._add_rule_frame_blocks(name, origin)
                return_value = g.Grammar.add_to_rules(name)
            else:
                pass
            cls._add_name_tag(name, origin)     ##  return_value?
            rs.CurrentLayer('Default')
        finally:
            return return_value

        # rs.AddLayer(name, cls.color)
        # rs.CurrentLayer(name)
        # if ttype == 'initial shape':
        #     cls._add_initial_shape_frame_block(name, origin)
        #     g.Grammar.add_to_initial_shapes(name)
        # elif ttype == 'rule':
        #     cls._add_rule_frame_blocks(name, origin)
        #     g.Grammar.add_to_rules(name)
        # else:
        #     pass
        # cls._add_name_tag(name, origin)
        # rs.CurrentLayer('Default')
        # if okay:
        #     return name
        # else:
        #     return None

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
        guid = fb.FrameBlock.insert(position)
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
        left_shape_guid = fb.FrameBlock.insert(left_shape_position)
        right_shape_guid = fb.FrameBlock.insert(right_shape_position)
        if left_shape_guid and right_shape_guid:
            return name
        else:
            return None

    @classmethod
    def _add_name_tag(cls, name, origin):
        """Receives:
            name            str. The name of the container. Value verified
            origin          Point3d. The origin of the container
        Adds a name tag at the appropriate point. Returns:
            name            str. The name of the component, if successful
            None            otherwise
        """
        position = rs.PointAdd(origin, cls.name_tag_offset)
        height = 2
        value = rs.AddText(name, position, height)
        if value:
            return name
        else:
            return None


