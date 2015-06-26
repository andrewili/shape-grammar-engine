from package.view import frame as f
import rhinoscriptsyntax as rs
from package.view import settings as s

class Layer(object):
    prohibited_characters = [' ', '#']

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
    def get_layer_name_from_user(cls):
        """Gets a valid name from the user. Returns:
            name            str. A well-formed and available layer name
        """
        message_1 = "%s %s" % (
            "Enter the layer name.", 
            "It must be unique and contain no spaces or '#' characters")
        message_2 = "%s %s %s" % (
            "That name is already in use",
            "or it contains spaces or '#' characters.",
            "Try again")
        name = rs.GetString(message_1)
        while not (
            cls._is_well_formed(name) and 
            cls._is_available(name)
        ):
            name = rs.GetString(message_2)
        return name

    @classmethod
    def _is_well_formed(cls, name):
        """Receives:
            name            str. The name of a layer
        Returns:
            boolean         True, if the name is well-formed. False, 
                            otherwise
        """
        return_value = True
        for character in cls.prohibited_characters:
            if character in name:
                return_value = False
                break
        return return_value

    @classmethod
    def _is_available(cls, name):
        """Receives:
            name            str. The name of a layer
        Returns:
            boolean         True, if the name is available. False, otherwise
        """
        return_value = not rs.IsLayer(name)
        return return_value

    @classmethod                                ##  06-23 08:57
    def get_frame_positions_from_layer_name(cls, layer_name):
        """Receives:
            layer_name      str. The name of a layer. Type and value not 
                            guaranteed
        Returns:
            initial_shape_frame_position 
                            Point3D. The position of the frame of an initial 
                            shape. Or
            rule_shape_frame_positions
                            (Point3D, Point3D). A duple of the positions of 
                            the left and right frames of a rule. Or
            None            if unsuccessful
        """
        method_name = 'get_frame_positions_from_layer_name'
        try:
            if not type(layer_name) == str:
                raise TypeError
            layer_names = rs.LayerNames()
            if not layer_name in layer_names:
                raise ValueError
        except TypeError:
            message = "The layer name must be a string"
            print("%s.%s:\n    %s" % (cls.__name__, method_name, message))
            return_value = None
        except ValueError:
            message = "The layer name does not exist"
            print("%s.%s:\n    %s" % (cls.__name__, method_name, message))
            return_value = None
        else:
            frame_positions = []
            frame_guids = cls._get_frames(layer_name)
            if frame_guids == None:
                return_value = None
            else:
                for frame_guid in frame_guids:
                    frame_position = rs.FrameInstanceInsertPoint(frame_guid)
                    frame_positions.append(frame_position)
                return_value = frame_positions
        finally:
            return return_value

    @classmethod
    def _get_frames(cls, layer_name):
        """Receives:
            layer_name      str. The name of a layer. Type and value 
                            guaranteed
        Returns:
            frames          [initial_guid], for an initial shape layer, if 
                            successful. Or
                            [left_guid, right_guid], for a rule layer, if
                            successful. Or
            None            otherwise
        """
        method_name = '_get_frames'
        objects_on_layer = rs.ObjectsByLayer(layer_name)
        if len(objects_on_layer) == 0:
            return_value = None
        else:
            frames_on_layer = []
            for object_on_layer in objects_on_layer:
                object_type = rs.ObjectType(object_on_layer)
                if object_type == s.Settings.block_type:
                    frames_on_layer.append(object_on_layer)
            if len(frames_on_layer) == 1:
                return_value = frames_on_layer
            elif len(frames_on_layer) == 2:
                return_value = cls._order_left_right(frames_on_layer)
            else:
                message = (
                    "There should be 1 or 2 frame instances on this layer")
                print("%s.%s\n    %s" % (cls.__name__, method_name, message))
                return_value = None
        return return_value

    @classmethod
    def _order_left_right(cls, frame_guids):
        """Receives:
            frame_guids     [guid, ...]. A list of not more than 2 frame 
                            guids
        Returns:
            ordered_frame_guids
                            [guid, ...]. The same list, ordered by insertion 
                            point (i.e., smaller x first)
        """
        frame_guid_1, frame_guid_2 = frame_guids
        p1, p2 = (
            rs.BlockInstanceInsertPoint(frame_guid_1), 
            rs.BlockInstanceInsertPoint(frame_guid_2))
        x1, x2 = p1[0], p2[0]
        if x1 < x2:
            return_value = [frame_guid_1, frame_guid_2]
        elif x1 == x2:
            if y1 <= y2:
                return_value = [frame_guid_1, frame_guid_2]
            else:
                return_value = [frame_guid_2, frame_guid_1]
        else:
            return_value = [frame_guid_2, frame_guid_1]
        return return_value






