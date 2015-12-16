from package.scripts import arrow as a
import rhinoscriptsyntax as rs
from package.scripts import settings as s

class LabeledArrow(object):
    def __init__(self):
        pass

    @classmethod
    def new(cls, layer, position):
        """Receives:
            layer           str. The name of the layer
            position        point3d. The position of the arrow
        Creates an arrow-name group with the name <name>-labeled-arrow. 
        Inserts it at the arrow position. Returns:
            group_out       str. The name of the new group, if successful. 
                            None otherwise.
        """
        group = '%s-labeled-arrow' % layer
        arrow_instance = a.Arrow.new_instance(layer, position)
        text_position = rs.PointAdd(
            position,
            s.Settings.arrow_label_offset_from_arrow)
        arrow_text = rs.AddText(
            layer, text_position, height=2, justification=2)
        group_out = rs.AddGroup(group)
        n_objects_added = rs.AddObjectsToGroup(
            [arrow_instance, arrow_text], 
            group)
        if n_objects_added:
            return_value = group_out
        else:
            return_value = None
        return return_value

