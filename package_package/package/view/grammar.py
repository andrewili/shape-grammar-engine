from package.view import arrow as a
from package.view import frame as f
from package.controller import guids_to_dat as gd
from package.view import layer as l
import rhinoscriptsyntax as rs
from package.view import settings as s

class Grammar(object):
    def __init__(self):
        pass

    ### new
    @classmethod                                ##  done 08-08
    def set_up_grammar(cls):
        cls.clear_all()
        cls._set_up_first_initial_shape()
        cls._set_up_first_rule()

    @classmethod                                ##  done 08-06
    def _set_up_first_initial_shape(cls):
        """Required state:
            There must be no layer with the first initial shape layer name
        Adds a new layer with the first initial shape layer name and one frame 
        instance. Should be executed only once. Returns:
            layer_name      str. The name of the layer, if successful. None, 
                            otherwise
        """
        method_name = '_set_up_first_initial_shape'
        try:
            layer_name = s.Settings.first_initial_shape_layer_name
            (   layer_name_is_in_use
            ) = (
                rs.IsLayer(layer_name))
            if layer_name_is_in_use:
                raise ValueError
        except ValueError:
            message = "The layer name '%s' is in use" % layer_name
            print("%s.%s:\n    %s" % (cls.__name__, method_name, message))
            return_value = None
        else:
            frame_instance_position = (
                s.Settings.first_initial_shape_frame_position)
            return_value = cls._set_up_initial_shape(
                layer_name, frame_instance_position)
        finally:
            return return_value

    @classmethod                                ##  done 08-06
    def set_up_subsequent_initial_shape(cls):
        """Prompts the user for a valid layer name and a valid point. Adds a 
        new layer with that name and one frame instance at that point. 
        Returns:
            layer_name      str. The name of the layer, if successful. None,
                            otherwise
        """
        (   layer_name, 
            frame_position
        ) = (
            l.Layer.get_layer_name_from_user(), 
            f.Frame.get_frame_position_from_user())
        return_value = cls._set_up_initial_shape(layer_name, frame_position)
        return return_value

    @classmethod                                ##  done 08-06
    def _set_up_initial_shape(cls, layer_name, frame_position):
        """Receives:
            layer_name      str. A well-formed and available layer name
            frame_position  Point3d. The position of the frame instance
        Creates a new layer with the specified name. Inserts a frame instance 
        on the new layer at the specified position. Returns:
            layer_name_out  str. The name of the layer
        """
        l.Layer.new(layer_name)
        frame_instance_out = f.Frame.new_instance(layer_name, frame_position)
        layer_name_out = rs.ObjectLayer(frame_instance_out)
        return layer_name_out

    @classmethod
    def _set_up_first_rule(cls):                ##  done 08-06
        """Required state:
            There must be no layer with the first rule layer name
        Adds a new layer with the first rule layer name and two frame 
        instances. Should be executed only once. Returns:
            layer_name      str. The name of the layer, if successful. None, 
                            otherwise
        """
        method_name = '_set_up_first_rule'
        try:
            layer_name = s.Settings.first_rule_layer_name
            (   layer_name_is_in_use
            ) = (
                rs.IsLayer(layer_name))
            if layer_name_is_in_use:
                raise ValueError
        except ValueError:
            message = "The layer name '%s' is in use" % layer_name
            print("%s.%s:\n    %s" % (cls.__name__, method_name, message))
            return_value = None
        else:
            (   left_frame_position
            ) = (
                s.Settings.first_rule_left_frame_position)
            return_value = cls._set_up_rule(layer_name, left_frame_position)
        finally:
            return return_value
        
    @classmethod                                ##  done 08-06
    def set_up_subsequent_rule(cls):
        """Prompts the user for a valid layer name and a valid point. Adds a 
        new layer with that name and two frame instances relative to that 
        point. Returns:
            layer_name      str. The name of the layer, if successful. None,
                            otherwise
        """
        (   layer_name,
            frame_position
        ) = (
            l.Layer.get_layer_name_from_user(),
            f.Frame.get_frame_position_from_user())
        return_value = cls._set_up_rule(layer_name, frame_position)
        return return_value

    @classmethod                                ##  done 08-06
    def _set_up_rule(cls, layer_name, left_frame_position):
        """Receives:
            layer_name      str. A well-formed and available layer name
            left_frame_position
                            Point3d. The position of the left frame instance
        Creates a new layer with the specified name. Inserts left frame, right 
        frame, and arrow instances on the new layer. Returns:
            layer_name_out  str. The name of the rule layer
        """
        l.Layer.new(layer_name)
        (   right_frame_position,
            arrow_position
        ) = (   
            s.Settings.get_right_frame_position(left_frame_position),
            s.Settings.get_arrow_position(left_frame_position))
        f.Frame.new_instance(layer_name, left_frame_position)
        f.Frame.new_instance(layer_name, right_frame_position)
        arrow_out = a.Arrow.new_instance(layer_name, arrow_position)
        layer_name_out = rs.ObjectLayer(arrow_out)
        return layer_name_out

    # @classmethod
    # def import(cls):                            ##  can't use this word
    #     pass

    ### export
    @classmethod                                ##  done 08-08
    def export(cls):
        """Writes the grammar's dat string to a file, proposing the Rhino 
        document name as the file name. Returns:
            dat_string      str. The dat string, if successful. None, 
                            otherwise
        """
        initial_shapes, rules = cls._get_element_layers()
        if (initial_shapes == [] or 
            rules == []
        ):
            (   error_message
            ) = (
                ' '.join([
                    "The grammar must have at least", 
                    "one initial shape and one rule"]))
            print(error_message)
            return_value = None
        else:
            (   suggested_file_name, 
                dat_string
            ) = (
                rs.DocumentName(), 
                gd.GuidsToDat.get_dat_string(initial_shapes, rules))
            dat_string_out = cls._write_to_file(
                suggested_file_name, dat_string)
            return_value = dat_string_out
        return return_value

    @classmethod
    def _get_element_layers(cls):               ##  done 08-07
        """Returns:
            initial_shapes  [str, ...]. A list of the names of layers 
                            containing one frame instance
            rules           [str, ...]. A list of the names of layers 
                            containing two frame instances
        """
        initial_shapes, rules = [], []
        layer_names = rs.LayerNames()
        for name in layer_names:
            if l.Layer.contains_initial_shape(name):
                initial_shapes.append(name)
            elif l.Layer.contains_rule(name):
                rules.append(name)
        return (initial_shapes, rules)

    @classmethod                                ##  done
    def _write_to_file(cls, file_name_in, dat_string):
        title = 'Save grammar'
        file_filter = 'DAT file (*.dat)|*.dat||'
        folder = None
        file_name = file_name_in
        extension = 'dat'
        file_name_out = (
            rs.SaveFileName(title, file_filter, folder, file_name, extension))
        if not file_name_out: 
            return
        file = open(file_name_out, "w" )
        file.write(dat_string)
        file.close()
        print(dat_string)

    ####

    @classmethod                                ##  for tests
    def get_labeled_shape_names(cls):
        """The grammar is guaranteed to be well-formed. Returns:
            labeled_shape_names
                            [str, ...]. A list of the names of the labeled 
                            shapes in initial shapes or rules, i.e., name, 
                            name_L, or name_R
        """
        labeled_shape_names = []
        layer_names = rs.LayerNames()
        for layer_name in layer_names:
            if l.Layer.contains_initial_shape(layer_name):
                labeled_shape_names.append(layer_name)
            elif l.Layer.contains_rule(layer_name):
                left_name = "%s_L" % layer_name
                right_name = "%s_R" % layer_name
                labeled_shape_names.extend([left_name, right_name])
        return labeled_shape_names

    @classmethod
    def remove_from_initial_shapes(cls):        ##  to do
        pass

    @classmethod
    def remove_from_rule(cls):                  ##  to do
        pass

    ### utilities
    @classmethod                                ##  called
    def clear_all(cls):                         ##  system-created blocks only?
        cls._clear_objects()
        cls._clear_blocks()
        cls._clear_layers()
        cls._clear_data()

    @classmethod                                ##  called
    def _clear_objects(cls):
        """Deletes all drawn objects. Returns:
            n_objects       int. The number of objects deleted, if successful
        """
        include_lights = True
        include_grips = True
        objects = rs.AllObjects(include_lights, include_grips)
        n_objects = rs.DeleteObjects(objects)
        return n_objects

    @classmethod                                ##  called
    def _clear_blocks(cls):
        block_names = rs.BlockNames()
        for name in block_names:
            rs.DeleteBlock(name)

    @classmethod                                ##  called
    def _clear_layers(cls):                     ##  clear only user layers
        """Deletes all layers. Leaves Default layer
        """
        default_layer_name = s.Settings.default_layer_name
        layer_names = rs.LayerNames()
        if not default_layer_name in layer_names:
            rs.AddLayer(default_layer_name)
        rs.CurrentLayer(default_layer_name)
        for layer_name in layer_names:
            if not layer_name == default_layer_name:
                rs.DeleteLayer(layer_name)

    @classmethod                                ##  called
    def _clear_data(cls):
        rs.DeleteDocumentData()

