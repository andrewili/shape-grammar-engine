from package.scripts import frame as f
import rhinoscriptsyntax as rs
from package.scripts import settings as s

class Layer(object):
    prohibited_characters = [' ', '#']

    def __init__(self):
        pass

    @classmethod                                ##  done 08-05
    def new(cls, name_in):
        """Receives:
            name_in         str. A well-formed and available layer name
        Adds a layer named <name_in>. Returns:
            name_out        str. The name of the layer
        """
        name_out = rs.AddLayer(name_in)
        return name_out

    @classmethod                                ##  done 08-06
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

    @classmethod                                ##  called
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

    @classmethod                                ##  called
    def _is_available(cls, name):
        """Receives:
            name            str. The name of a layer
        Returns:
            boolean         True, if the name is available. False, otherwise
        """
        return_value = not rs.IsLayer(name)
        return return_value

    @classmethod                                ##  called
    def get_frame_instance(cls, initial_shape):
        """Receives:
            initial_shape   str. The name of a layer containing one frame 
                            instance (i.e., an initial shape layer). The value 
                            is guaranteed
        Returns:
            frame_instance  guid. The guid of the frame instance on the layer 
                            Isn't this redundant?
        """
        if not rs.IsLayer(initial_shape):
            message = "There is no layer named '%s'" % initial_shape
        all_frame_instances = rs.BlockInstances(s.Settings.frame_name)
        frame_instances_on_layer = []
        for frame_instance in all_frame_instances:
            if rs.ObjectLayer(frame_instance) == initial_shape:
                frame_instances_on_layer.append(frame_instance)
        n_instances = len(frame_instances_on_layer)
        if n_instances == 0:
            message = "%s %s" % (
                "There is no frame instance", 
                "on the layer '%s'" % initial_shape)
            return_value = None
        elif n_instances == 1:
            message = None
            return_value = frame_instances_on_layer.pop()
        else:
            message = "%s %s" % (
                "There is more than 1 frame instance", 
                "on the layer '%s'" % initial_shape)
            return_value = None
        if message:
            print(message)
        return return_value

    @classmethod                                ##  called
    def get_frame_instance_pair(cls, rule):
        """Receives:
            rule            str. The name of a layer containing two frame 
                            instances (i.e., a rule layer). The value is 
                            guaranteed
        Returns:
            ordered_frame_instance_pair
                            (guid, guid). A pair of the guids of the two frame 
                            instances on the layer, ordered from left to right 
        """
        all_frame_instances = rs.BlockInstances(s.Settings.frame_name)
        frame_instances = []
        for instance_i in all_frame_instances:
            if rs.ObjectLayer(instance_i) == rule:
                frame_instances.append(instance_i)
        p0 = f.Frame.get_instance_position(frame_instances[0])
        p1 = f.Frame.get_instance_position(frame_instances[1])
        if p0 < p1:
            ordered_frame_instance_pair = (
                frame_instances[0], frame_instances[1])
        elif p0 > p1:
            ordered_frame_instance_pair = (
                frame_instances[1], frame_instances[0])
        else:
            pass
        return ordered_frame_instance_pair

    @classmethod                                ##  called
    def contains_initial_shape(cls, name):
        """Receives:
            name            str. The name of the layer
        Returns:
            boolean         True, if the layer contains an initial shape. 
                            False, otherwise
        """
        value = cls._get_number_of_frames(name) == 1
        return value

    @classmethod                                ##  called
    def contains_rule(cls, name):
        """Receives:
            name            str. The name of the layer_name
        Returns:
            boolean         True, if the layer contains a rule. False, 
                            otherwise
        """
        value = cls._get_number_of_frames(name) == 2
        return value

    @classmethod                                ##  called
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

    @classmethod                                ##  called
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

    @classmethod                                ##  called
    def get_objects_on_layer(cls, frame_instance):
        """Receives:
            frame_instance  The guid of a frame instance
        Returns:
            objects_on_layer
                            [guid, ...]. A list of the guids of the objects 
                            on the layer containing the frame instance, if 
                            successful
            None            otherwise
        """
        layer_name = rs.ObjectLayer(frame_instance)
        objects_on_layer = rs.ObjectsByLayer(layer_name)
        return objects_on_layer

