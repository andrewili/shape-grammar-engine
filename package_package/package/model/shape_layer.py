from package.model import frame_block as fb
from package.model import layer as l
from package.model import llist as ll
import rhinoscriptsyntax as rs

class ShapeLayer(object):
    component_type = 'shape'
    shape_layer_list_name = 'shape layer names'
    tag_offset = [0, -4, 0]
    text_height = 2

    def __init__(self):
        pass

    @classmethod
    def new(cls, shape_name, position):
        """Receives:
            shape_name      str; available name
            position        Point3d or [num, num, num]; in the xy plane
        Both arguments are validated upstream. Creates a new layer with a 
        shape frame and a tag. Records the name in the shape layer name list. 
        Used for initial shapes, left rule shapes, and right rule shapes. 
        Returns:
            str             shape_name, if successful
            None            otherwise
        """
        cls._record_name(shape_name)            ##  
        l.Layer.new(shape_name)
        rs.CurrentLayer(shape_name)
        guid = fb.FrameBlock.insert(position)
        tag_position = rs.PointAdd(position, cls.tag_offset)
        tag_guid = cls._add_tag(shape_name, tag_position)
        rs.CurrentLayer('Default')
        if guid:
            return_value = shape_name
        else:
            return_value = None
        return return_value

    @classmethod
    def _record_name(cls, name):
        """Receives:
            name            str
        Enters the name in the shape layer name list. Returns:
            str             the name, if successful
            None            otherwise
        """
        return_value = ll.Llist.set_entry(cls.shape_layer_list_name, name)
        return return_value

    @classmethod
    def _add_tag(cls, shape_name, tag_position):
        """Receives:
            shape_name      str
            tag_position    Point3d
        Adds the shape name as a text object. Returns:
            guid            the guid of the tag, if successful
            None            otherwise
        """
        return_value = rs.AddText(shape_name, tag_position, cls.text_height)
        return return_value

    @classmethod
    def get_is_text(cls):                       ##  02-14 18:35
        """Translates the drawn shape into an is-format text string. Returns:
            str             the is-format text string
        """
        select_objects_on_layer
        shape_name = identify_tag
        lines = identify_lines
        labels = identify_labels
        return_value = translate(shape_name, lines, labels)
        return_value = 'kilroy'
        return return_value
