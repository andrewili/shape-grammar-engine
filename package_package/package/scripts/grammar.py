from package.scripts import arrow as a
from package.scripts import frame as f
from package.controller import guids_to_dat as gd
from package.scripts import layer as l
import rhinoscriptsyntax as rs
from package.scripts import settings as s

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

    @classmethod                                ##  12-12
    def _set_up_rule(cls, layer_name, left_frame_position):
        """Receives:
            layer_name      str. A well-formed and available layer name
            left_frame_position
                            Point3d. The position of the left frame instance
        Creates a new layer with the specified name. Inserts two frame 
        instances, an arrow instance, and a name plate on the new layer. 
        Returns:
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

    @classmethod                                ##  12-09
    def refresh_element_layer_name_texts(cls):
        """Draws (or redraws, if already drawn) the name texts of the initial 
        shape layers and rule layers
        """
        initial_shape_layers, rule_layers = cls._get_element_layers()
        for rule_layer in rule_layers:
            if cls._rule_layer_has_name_text(rule_layer):   ##  here
                cls._redraw_rule_layer_name_text(rule_layer)
            else:
                cls._draw_new_rule_layer_name_text(rule_layer)

    @classmethod                                ##  12-09
    def _rule_layer_has_name_text(cls, rule_layer):
        """Receives:
            rule_layer      str. The name of a rule layer
        Returns:
            value           boolean. True, if the rule layer has a name text. 
                            False otherwise
        """
        rule_layer_objects = rs.ObjectsByLayer(rule_layer)
        text_objects = cls._extract_text_objects(rule_layer_objects)
        unframed_text_objects = cls._extract_unframed_text_objects(
            text_objects)
                                                ##  12-12 paused
        if n_unframed_text_objects == 1:
            value = True
        else:
            value = None                        ##  ask user to select?
            print('Too many possibilities')
        return value

    @classmethod
    def _extract_text_objects(cls, rule_layer_objects):
        """Receives:
            rule_layer_objects
                            [guid]. A list of guids
        Returns:
            text_objects    [guid]. A list of text objects
        """
        text_objects = []
        for objectt in rule_layer_objects:
            if rs.IsText(objectt):
                text_objects.append(objectt)
        return text_objects

    @classmethod                                ##  11-01 08:03
    def _redraw_rule_layer_name_text(cls, rule_layer):
        """Receives:
            rule_layer      str. The name of a rule layer
        Redraws the layer name on the name text. Returns:
            name_text       guid. The guid of the name text
        """
        pass

    @classmethod                                ##  done 12-09
    def _draw_new_rule_layer_name_text(cls, rule_layer):
        """Receives:
            rule_layer      str. The name of a rule layer with no name text
        Draws a name text with the layer name. Returns:
            name_text       guid. The guid of the name text, if successful. 
                            None otherwise
        """
        rule_position = cls._get_rule_position(rule_layer)
        name_text_position = rs.PointAdd(
            rule_position, s.Settings.derivation_rule_name_offset)
        name_text = rs.AddText(
            rule_layer, 
            name_text_position, 
            s.Settings.rule_name_text_height, 
            s.Settings.rule_name_text_font, 
            s.Settings.rule_name_text_font_style, 
            s.Settings.rule_name_text_justification)
        return name_text


    # @classmethod                                ##  to do
    # def _draw_initial_shape_layer_name_text(cls, name):
        # """Receives:
        #     name            str. The name of an initial shape layer
        # Draws the initial shape layer name. If there is one already, it is 
        # overdrawn. Returns:
        #     name_text       guid. The guid of the name_text annotation
        # """
        # pass

    # @classmethod                                ##  in process 10-31
    # def _draw_rule_layer_name(cls, name):
        # """Receives:
        #     name            str. The name of a rule layer
        # Draws the rule layer name. If there is one already, it is 
        # overdrawn. Returns:
        #     name_text       guid. The guid of the name_text annotation
        # """
        # if name_plate_exists():
        #     rewrite_name_plate()
        # else:

        # rule_position = cls._get_rule_position(name)
        # name_position = rs.PointAdd(
        #     rule_position, s.Settings.derivation_rule_name_offset)
        # height = 2
        # font = 'Arial'
        # font_style = 0
        # justified_center = 2
        # name_text = rs.AddText(
        #     name, name_position, height, font, font_style, justified_center)
        # return name_text

    @classmethod                                ##  done 12-09
    def _get_rule_position(cls, name):
        """Receives:
            name            str. The name of a rule layer
        Returns:
            position        Point3D. The position of the left frame
        """
        frame_instance_pair = l.Layer.get_frame_instance_pair(name)
        left_frame = frame_instance_pair[0]
        position = rs.BlockInstanceInsertPoint(left_frame)
        return position

    ### export
    @classmethod                                ##  done 08-08
    def export(cls):                            ##  cf import deriv
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

    ### import 
    # @classmethod
    # def import(cls):                            ##  can't use this word
    #     pass

    # @classmethod
    # def import_derivation(cls):
    #     """Prompts the user for a drv file. Draws the derivation
    #     Put this in dats_to_guid?
    #     """
    #     draw_derivation(shape_specs, rules)

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

