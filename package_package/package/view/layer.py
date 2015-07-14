from package.view import frame as f
from package.controller import guids_to_dat as gd
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
            name            str. A unique and well-formed layer name
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

    @classmethod                                ##  07-13 13:55
    def get_frame_instance(cls, labeled_shape_name):
        """Receives:
            labeled_shape_name
                            str. The name of a labeled shape, i.e., initial 
                            shape, left rule shape, or right rule shape
        Returns:
            frame_instance  guid. The guid of the associated frame instance
        """
        if labeled_shape_name[-2:] == gd.GuidsToDat.left_labeled_shape_suffix:
            layer_name = labeled_shape_name[:-2]
            labeled_shape = 'left'
        elif labeled_shape_name[-2:] == (
            gd.GuidsToDat.right_labeled_shape_suffix
        ):
            layer_name = labeled_shape_name[:-2]
            labeled_shape = 'right'
        else:
            layer_name = labeled_shape_name
            labeled_shape = 'initial'
        all_frame_instances = rs.BlockInstances(s.Settings.frame_name)
        frame_instances_on_layer = []           ##  name-frame dictionary?
        for frame_instance in all_frame_instances:
            if rs.ObjectLayer(frame_instance) == layer_name:
                frame_instances_on_layer.append(frame_instance)
        if labeled_shape == 'left':
            frame_instance = cls.get_left_frame_instance(
                frame_instances_on_layer)
        elif labeled_shape == 'right':
            frame_instance = cls.get_right_frame_instance(
                frame_instances_on_layer)
        elif labeled_shape == 'initial':
            frame_instance = frame_instances_on_layer.pop()
        else:
            pass
        return frame_instance

    @classmethod
    def contains_initial_shape(cls, name):
        """Receives:
            name            str. The name of the layer
        Returns:
            boolean         True, if the layer contains an initial shape. 
                            False, otherwise
        """
        value = cls._get_number_of_frames(name) == 1
        return value

    @classmethod
    def contains_rule(cls, name):
        """Receives:
            name            str. The name of the layer_name
        Returns:
            boolean         True, if the layer contains a rule. False, 
                            otherwise
        """
        value = cls._get_number_of_frames(name) == 2
        return value

    @classmethod
    def _get_number_of_frames(cls, layer_name):
        """Receives:
            layer_name      str. The name of the layer
        Returns:
            n               int. The number of frame instances on the layer
        """
        frame_name = s.Settings.frame_name
        if not rs.IsBlock(frame_name):
            n = 0
        else:
            frame_instance_guids = rs.BlockInstances(frame_name)
            n = 0
            for guid in frame_instance_guids:
                if cls._contains_guid(guid, layer_name):
                    n = n + 1
        return n

    @classmethod
    def _contains_guid(cls, frame_guid, layer_name):
        """Receives:
            frame_guid      The guid of a frame instance
        Returns:
            value           boolean. True, if the layer contains the frame 
                            instance. False, otherwise
        """
        frame_layer_name = rs.ObjectLayer(frame_guid)
        value = frame_layer_name == layer_name
        return value

    @classmethod
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
                    frame_position = rs.BlockInstanceInsertPoint(frame_guid)
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

    @classmethod
    def is_in_frame_instance(cls, object_guid, frame_guid):
        """Receives:
            object_guid     guid. The guid of an object
            frame_guid      guid. The guid of a frame instance
        Returns:
            value           boolean. True, if the object is a line or textdot 
                            in the frame instance
        """
        return value


    # @classmethod                                ##  07-06 15:50
    # def _get_initial_labeled_shape_string(cls, layer_name):
    #     """Receives:
    #         layer_name      str. The layer name of an initial shape
    #     Returns:
    #         initial_labeled_shape_string
    #                         str. The string of the initial labeled shape on 
    #                         the layer, if successful
    #         None            otherwise
    #     """
    #     header_stringlet = "%s%s%s" % (
    #         'shape',
    #         cls.spacer,
    #         layer_name)
    #     indented_name_stringlet = 'name'
    #     ordered_indented_coord_lines_stringlet = (
    #         cls._make_ordered_indented_coord_lines_stringlet())
    #     blank_stringlet = ''
    #     ordered_indented_line_lines_stringlet = (
    #         cls._make_ordered_indented_line_lines_stringlet())
    #     ordered_indented_labeled_point_lines_stringlet = (
    #         cls._make_ordered_indented_labed_point_lines_stringlet())
    #     initial_labeled_shape_stringlets = [
    #         header_stringlet,
    #         indented_name_stringlet,
    #         ordered_indented_coord_lines_stringlet,
    #         blank_stringlet,
    #         ordered_indented_line_lines_stringlet,
    #         ordered_indented_labeled_point_lines_stringlet]
    #     initial_labeled_shape_string = '\n'.join(
    #         initial_labeled_shape_stringlets)
    #     return initial_labeled_shape_string

    # @classmethod
    # def _get_rule_labeled_shape_strings(cls, layer_name):
    #     """Receives:
    #         layer_name      str. The layer name of a rule
    #     Returns:
    #         rule_labeled_shape_strings
    #                         (str, str). A duple of the strings of the left and 
    #                         right labeled shapes on the layer
    #     """
    #     rule_labeled_shape_strings = (
    #         left_labeled_shape_string, rule_labeled_shape_strings)
    #     return rule_labeled_shape_strings

    #     # ishape_lshapes = cls.get_initial_shapes()
    #     # rule_lshapes = cls.get_rule_shapes()
    #     # named_lshapes = []
    #     # named_lshapes.extend(ishape_lshapes)
    #     # named_lshapes.extend(rule_lshapes)
    #     # ordered_named_lshapes = sorted(named_lshapes)
    #     # ordered_named_lshape_strings = []
    #     # for named_lshape in ordered_named_lshapes:
    #     #     named_lshape_string = (
    #     #         ls.LabeledShape.get_string_from_named_lshape(named_lshape))
    #     #     ordered_named_lshape_strings.append(named_lshape_string)
    #     # ordered_labeled_shapes_string = '\n'.join(ordered_named_lshape_strings)
    #     # return ordered_labeled_shapes_string

