from package.view import frame_block as fb
import rhinoscriptsyntax as rs
from package.view import settings as s

class Layer(object):
    def __init__(self):
        pass

    @classmethod
    def new(cls, name_in):
        """Receives:
            name_in         str. The name of the layer
        Adds a layer named name. Returns:
            name_out        str. The name of the layer, if successful
        """
        name_out = rs.AddLayer(name_in)
        return name_out

    @classmethod
    def new_1_frame_block(cls, name, origin):   ##  06-21 17:16
        """Receives:
            name            str. The name of the layer. Type and value 
                            guaranteed
            origin          Point3D. The origin of the layer
        Adds a new layer with 1 frame block. Returns:
            name            str. The name of the layer, if successful
            None            otherwise
        """
        rs.AddLayer(name)
        return_value = 'kilroy'
        return return_value

    @classmethod
    def new_2_frame_blocks(cls, name, origin):
        """Receives:
            name            str. The name of the layer. Type and value 
                            guaranteed
            origin          Point3D. The origin of the layer
        Adds a new layer with 2 frame blocks. Returns:
            name            str. The name of the layer, if successful
            None            otherwise
        """
        cls._add_layer(name)
        left_block_name = "%s_L" % name
        right_block_name = "%s_R" % name
        left_block_origin = origin
        right_block_origin = s.Settings.get_right_frame_block_origin(
            left_block_origin)
        right_block_origin = rs.PointAdd(
            left_block_origin, right_block_origin)
        fb.FrameBlock.add_frame_block(left_block_name, left_block_origin)
        fb.FrameBlock.add_frame_block(right_block_name, right_block_origin)
        return_value = 'kilroy'
        return return_value

    # @classmethod
    # def new(cls, name_in, base_point, ttype):      ##  06-21 05:51
        # """Receives:
        #     name_in         str. The name to be assigned to the layer. Type 
        #                     and value guaranteed
        #     base_point      Point3D. The layer's base point
        #     ttype           str: {ish.InitialShape.first_initial_shape_name | 
        #                     r.Rule.first_rule_name}. The layer's type
        # Creates a new layer. Sets up one or two labeled shapes. Returns:
        #     name_out        str. The name of the rule as assigned, if 
        #                     successful
        #     None            otherwise
        # """
        # color = s.Settings.layer_color
        # name_out = rs.AddLayer(name_in, color)
        # if ttype == ish.InitialShape.component_type:
        #     add_1_frame_block()
        #     # lshape_set_up_value = ls.LabeledShape.set_up(       ##  kilroy
        #     #     name_in, base_point, 'initial')
        # elif ttype == r.Rule.component_type:
        #     add_2_frame_blocks()
        #     # left_value = ls.LabeledShape.set_up(name_in, base_point, 'left')
        #     # right_value = ls.LabeledShape.set_up(name_in, base_point, 'right')
        #     # lshape_set_up_value = left_value and return_value
        # else:
        #     pass
        # if (name_out and
        #     tag_guid and
        #     lshape_set_up_value
        # ):
        #     return_value = name_out
        # else:
        #     return_value = None
        # return return_value

