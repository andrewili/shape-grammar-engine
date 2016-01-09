from package.scripts import arrow as a
from package.scripts import frame as f
from package.controller import guids_to_dat as gd
from package.scripts import layer as l
from package.scripts import labeled_arrow as la
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
        Adds a new layer with the first initial shape layer name and one 
        frame instance. Should be executed only once. Returns:
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

    @classmethod
    def _set_up_rule(cls, layer_name, left_frame_position):
        """Receives:
            layer_name      str. A well-formed and available layer name
            left_frame_position
                            Point3d. The position of the left frame instance
        Creates a new layer with the specified name. Inserts two frame 
        instances and a labeled arrow group on the new layer. Returns:
            layer_name_out  str. The name of the rule layer
        """
        l.Layer.new(layer_name)
        right_frame_position = s.Settings.get_right_frame_position(
            left_frame_position)
        arrow_position = s.Settings.get_arrow_position(left_frame_position)
        left_frame_out = f.Frame.new_instance(layer_name, left_frame_position)
        right_frame_out = f.Frame.new_instance(
            layer_name, right_frame_position)
        labeled_arrow_out = la.LabeledArrow.new(layer_name, arrow_position)
        return_value = False
        if (left_frame_out and
            right_frame_out and
            labeled_arrow_out
        ):
            return_value = layer_name
        return return_value

    @classmethod                                ##  01-03
    def change_text_dots_to_annotation_groups(cls):
        """Changes the display of labeled points from text dots to annotation 
        groups. 
            Hides text dots and shows / creates annotation groups
        Returns:
            n_changes       int. The number of changes made
        Alternate names: 
            show_hatch_annotations
            show_annotation_groups
            show_annotation_dots
        """
        n_dots_shown = cls._show_text_dots()    ##  or create
        n_groups_hidden = cls._hide_annotation_groups()

        hidden_group = cls._create_hidden_text_dot_group()
        text_dots = cls._get_text_dots()
        for text_dot in text_dots:
            cls._change_text_dot_to_annotation_group(text_dot)
        n_changes = rs.HideGroup(hidden_group)
        cls._update_display()
        return n_changes

    @classmethod
    def _create_hidden_text_dot_group(cls):
        """Returns:
            group           str. The name of the group
        """
        group_in = s.Settings.hidden_text_dot_group
        group = rs.AddGroup(group_in)
        return group

    @classmethod
    def _get_text_dots(cls):
        """Returns:
            text_dots       [guid]. A list of text dot guids.
        """
        text_dot_filter = s.Settings.text_dot_filter
        text_dots = rs.ObjectsByType(text_dot_filter)
        return text_dots

    @classmethod
    def _change_text_dot_to_annotation_group(cls, text_dot):
        """Receives:
            text_dot        guid
        Adds text_dot to the hidden text dot group. Adds an annotation group. 
        Returns:
            value           boolean. True if successful; False otherwise
        """
        text, point = cls._get_text_and_position_from_text_dot(text_dot)
        value_hide = cls._add_text_dot_to_hidden_group(text_dot)
        value_show = cls._add_annotation_group(text, point)
        value = value_hide and value_show
        return value

    @classmethod
    def _get_text_and_position_from_text_dot(cls, text_dot):
        text = rs.TextDotText(text_dot)
        point = rs.TextDotPoint(text_dot)
        return (text, point)

    @classmethod
    def _add_text_dot_to_hidden_group(cls, text_dot):
        """Receives:
            text_dot        guid
        Adds text_dot to the hidden text dot group. Returns:
            value           boolean. True if successful; False if not
        """
        hidden_group = s.Settings.hidden_text_dot_group
        value = rs.AddObjectToGroup(text_dot, hidden_group)
        return value

    @classmethod
    def _add_annotation_group(cls, text, point):
        """Receives:
            text            str
            point           Point3d
        Creates an annotation, a circle, and a hatch. Puts them into an 
        (unlocked) group. Returns:
            n_objects       int. the number of objects added to the group, if 
                            successful
        """
        annotation = cls._add_annotation(text, point)
        circle, hatch = cls._add_hatch(point)
        group = rs.AddGroup()
        objects = [circle, hatch, annotation]
        n_objects = rs.AddObjectsToGroup(objects, group)
        # rs.LockGroup(group)

    @classmethod
    def _add_annotation(cls, text, point):
        text_offset = s.Settings.hatch_annotation_text_offset
        position = rs.PointAdd(point, text_offset)
        height = s.Settings.hatch_annotation_text_height
        annotation = rs.AddText(text, position, height)
        return(annotation)

    @classmethod
    def _add_hatch(cls, point):
        radius = s.Settings.hatch_radius
        circle = rs.AddCircle(point, radius)
        hatch = rs.AddHatch(circle, 'Solid')
        return(circle, hatch)

    @classmethod
    def _update_display(cls):
        """Forces the display to update itself. Returns:
            value           boolean. True if successful; False otherwise
        """
        dummy_point = rs.AddPoint(0, 0, 0)
        value = rs.DeleteObject(dummy_point)
        return value

    @classmethod                                ##  12-30
    def change_annotation_groups_to_text_dots(cls):
        """Changes the display of labeled points from annotation groups to 
        text dots. 
        Required state: 
            There must be both annotation groups and hidden text dots
        Hides / deletes annotation groups and shows text dots. 
        Returns:
            n_dots_shown    int. The number of dots shown, if n > 0; None 
                            otherwise
        """
        n_groups_hidden = cls._hide_annotation_groups()
        n_dots_shown = cls._show_text_dots()
        if n_dots_shown > 0:
            value = n_dots_shown
        else:
            value = None
        return value

    @classmethod                                ##  01-03 10:46
    def _hide_annotation_groups(cls):
        """Hides annotation groups. Returns:
            n               int. The number of annotation groups hidden, if 
                            n > 0; None otherwise
        """
        pass

    @classmethod                                ##  01-03 10:47
    def _show_text_dots(cls):
        """Shows hidden text dots. Returns:
            n               int. The number of hidden text dots shown, if 
                            n > 0; None
        """
        pass

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
        # pass

    # @classmethod
    # def import_derivation(cls):
        # """Prompts the user for a drv file. Draws the derivation
        # Put this in dats_to_guid?
        # """
        # draw_derivation(shape_specs, rules)

    ### utilities
    @classmethod                                ##  called
    def clear_all(cls):                         ##  system-created blocks 
                                                ##  only?
        cls._clear_objects()
        cls._clear_blocks()
        cls._clear_layers()
        cls._clear_groups()
        cls._clear_data()

    @classmethod
    def _clear_objects(cls):
        """Deletes all drawn objects, including locked and hidden objects, if 
        any. Returns:
            n_objects       int. The number of objects deleted, if successful
        """
        cls._show_hidden_text_dots()
        dummy_point = rs.AddPoint(0, 0, 0)
        value = rs.DeleteObject(dummy_point)
        include_lights = True
        include_grips = True
        objects = rs.AllObjects(include_lights, include_grips)
        n_objects = rs.DeleteObjects(objects)
        remaining_objects = rs.AllObjects(include_lights, include_grips)
        rs.UnlockObjects(remaining_objects)
        m_objects = rs.DeleteObjects(remaining_objects)
        return n_objects + m_objects

    @classmethod
    def _show_hidden_text_dots(cls):
        """Shows hidden text dots. Returns:
            n_text_dots     int. The number of text dots shown
        """
        hidden_group = s.Settings.hidden_text_dot_group
        n_text_dots = rs.ShowGroup(hidden_group)
        cls._update_display()
        return n_text_dots

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
                value = rs.DeleteLayer(layer_name)
                print('Cleared layer %s: %s' % (layer_name, value))

    @classmethod
    def _clear_groups(cls):
        """Deletes all groups 
        """
        groups = rs.GroupNames()
        if groups:
            for group in groups:
                rs.DeleteGroup(group)

    @classmethod                                ##  called
    def _clear_data(cls):
        rs.DeleteDocumentData()
