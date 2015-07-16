from package.view import frame as f
from package.view import grammar as g
from package.view import layer as l
import rhinoscriptsyntax as rs
from package.view import settings as s

class GuidsToDat(object):
    dat_header = "%s\n%s" % (
        "# shape data version 6.00",
        "unit  mm  # mm - millimetre, cm - centimetre, m - metre")
    blank_line = ''
    spacer = '    '
    left_labeled_shape_suffix = '_L'
    right_labeled_shape_suffix = '_R'

    def __init__(self):
        pass

    @classmethod                                ##  07-14 08:39
    def get_dat_string(cls):
        """Composes the grammar's dat string, i.e.: 
            header
            ordered_labeled_shapes_string
            ordered_initial_shapes_string
            ordered_rules_string
        The grammar must be well-formed, i.e., 
            it must have at least one well-formed initial shape layer (i.e., 
                a layer with one frame instance and at least one line or 
                textdot)
            it must have at least one well-formed rule layer (i.e., a layer 
                with two frame instances and at least one line or textdot)
        Returns:
            dat_string      str. The grammar's dat string, if successful
            None            otherwise
        """
        initial_shapes, rules = g.Grammar.get_initial_shapes_and_rules()
        initial_shape_frame_dict = cls._make_initial_shape_frame_dict(
            initial_shapes)
        rule_frame_pair_dict = cls._make_rule_frame_pair_dict(rules)
                            ##  {rule_name: (frame_instance, frame_instance)}
        labeled_shape_elements_dict = (
            cls._make_labeled_shape_elements_dict(
                initial_shape_frame_dict, rule_frame_pair_dict))
                            ##  {labeled_shape: [element, ...]}
                                                ##  kilroy was here
        ordered_labeled_shapes_string = (
            cls._get_ordered_labeled_shapes_string(
                labeled_shape_elements_dict))
                            ##  'labeled_shape_string\n...'
        ordered_initial_shapes_string = (
            cls._get_ordered_initial_shapes_string(
                labeled_shape_elements_dict))
                            ##  'initial    name\n...'
        ordered_rules_string = (
            cls._get_ordered_rules_string(labeled_shape_elements_dict))
                            ##  'rule    name    name_L -> name_R\n...'
        dat_header = cls.dat_header
        blank_line = cls.blank_line
        dat_string = '\n'.join([
            dat_header,
            ordered_labeled_shapes_string,
            blank_line,
            ordered_initial_shapes_string,
            ordered_rules_string])
        return_value = dat_string
        return return_value

    @classmethod
    def _make_initial_shape_frame_dict(cls, initial_shapes):
        """Receives:
            initial_shapes  [str, ...]. A list of names of layers containing 
                            one frame instance. Values are guaranteed
        Returns:
            initial_shape_frame_dict
                            {str: guid}. A dictionary of initial shape names 
                            and frame instance guids
        """
        initial_shape_frame_dict = {}
        for initial_shape in initial_shapes:
            frame_instance = l.Layer.get_frame_instance(initial_shape)
            initial_shape_frame_dict[initial_shape] = frame_instance
        return initial_shape_frame_dict

    @classmethod
    def _make_rule_frame_pair_dict(cls, rules):
        """Receives:
            rules           [str, ...]. A list of names of layers containing 
                            two frame instances. Values are guaranteed
        Returns:
            rule_frame_pair_dict
                            {str: (guid, guid)}. A dictionary of rule names 
                            and frame instance guid pairs
        """
        rule_frame_pair_dict = {}
        for rule in rules:
            frame_pair = l.Layer.get_frame_instance_pair(rule)
            rule_frame_pair_dict[rule] = frame_pair
        return rule_frame_pair_dict

    @classmethod                                ##  07-16 07:45
    def _make_labeled_shape_elements_dict(
        cls, initial_shape_frame_dict, rule_frame_pair_dict
    ):
        """Receives:
            initial_shape_frame_dict
                            {str: guid}. A dictionary of initial shape names 
                            and frame instance guids
            rule_frame_pair_dict
                            {str: (guid, guid)}. A dictionary of rule names 
                            and frame instance guid pairs
        Returns:
            labeled_shape_elements_dict
                            {str: [guid, ...]}. A dictionary of labeled shape 
                            names and lists of their element guids
        """
        labeled_shape_elements_dict = {}
        for initial_shape in initial_shape_frame_dict:
            frame_instance = initial_shape_frame_dict[initial_shape]
            elements = cls._get_elements(frame_instance)
            labeled_shape_elements_dict[initial_shape] = elements
        for rule in rule_frame_pair_dict:
            left_shape = '%s_L' % rule
            right_shape = '%s_R' % rule
            left_frame, right_frame = rule_frame_pair_dict[rule]
            left_elements = cls._get_elements(left_frame)
            right_elements = cls._get_elements(right_frame)
            labeled_shape_elements_dict[left_shape] = left_elements
            labeled_shape_elements_dict[right_shape] = right_elements
        return labeled_shape_elements_dict

    @classmethod
    def _get_elements(cls, frame_instance):
        """Receives:
            frame_instance  str. The name of a frame instance
        Returns:
            elements        [guid, ...]. A list of the guids of the elements 
                            in the frame instance, if successful
            None            otherwise           ?
        """
        objects_on_layer = cls._get_objects_on_layer(frame_instance)
        elements = cls._extract_elements_in_frame(
            frame_instance, objects_on_layer)
        return elements

    @classmethod
    def _get_objects_on_layer(cls, frame_instance):
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

    @classmethod
    def _extract_elements_in_frame(cls, frame_instance, objects_on_layer):
        """Receives:
            frame_instance  guid. The guid of a frame instance
            objects_on_layer
                            [guid, ...]. A list of the guids of the objects  
                            on the layer containing the frame instance
        Returns:
            elements_in_frame
                            [guid, ...]. A list of the line and textdot guids 
                            in the frame instance
        """
        elements_in_frame = []
        frame_position = f.Frame.get_instance_position(frame_instance)
        frame_size = s.Settings.frame_size
        for object_guid in objects_on_layer:
            if (cls._is_element(object_guid) and
                cls._object_is_in_box(
                    object_guid, frame_position, frame_size)
            ):
                element_guid = object_guid
                elements_in_frame.append(element_guid)
        return elements_in_frame

    @classmethod
    def _is_element(cls, object_guid):
        """Receives:
            object_guid     guid. The guid of an object
        Returns:
            value           boolean. True, if the object is a line or a 
                            textdot. False, otherwise
        """
        curve_type = 4
        textdot_type = 8192
        value = (
            rs.ObjectType(object_guid) == curve_type or 
            rs.ObjectType(object_guid) == textdot_type)
        return value

    @classmethod
    def _object_is_in_box(cls, object_guid, box_position, box_size):
        """Receives:
            object_guid     guid. The guid of an object
            box_position    Point3d. The position of the frame instance
            box_size        (num, num, num). The size of the frame block
        """
        curve_type = 4
        textdot_type = 8192
        if rs.ObjectType(object_guid) == curve_type:
            tail = rs.CurveStartPoint(object_guid)
            head = rs.CurveEndPoint(object_guid)
            points = [tail, head]
        elif rs.ObjectType(object_guid) == textdot_type:
            point = rs.TextDotPoint(object_guid)
            points = [point]
        else:
            pass
        value = True
        for point in points:
            if not cls._point_is_in_box(point, box_position, box_size):
                value = False
                break
        return value

    @classmethod
    def _point_is_in_box(cls, point, position, size):
        """Receives:
            point           Point3d or (num, num, num)
            position        Point3d or (num, num, num). The position of the 
                            box
            size            Point3d or (num, num, num). The diagonal size of 
                            the box
        Returns:
            value           boolean. True, if the point is inside or on the 
                            surface of the box
        """
        p1 = position
        p2 = rs.PointAdd(p1, size)
        x0, y0, z0 = point
        x1, y1, z1 = p1
        x2, y2, z2 = p2
        value = (
            x1 <= x0 <= x2 and
            y1 <= y0 <= y2 and 
            z1 <= z0 <= z2)
        return value

    @classmethod
    def _remove_bad_names(cls, name, names):
        """Receives:
            name            str. without the right labeled shape suffix. The 
                            name of a labeled shape
            names           [str, ...]. A list of labeled shape names
        If the name of an initial shape, removes the name from the list of 
        labeled shape names. If the name of a rule, removes both the left and
        right labeled shape names from the list of labeled shape names
        """
        names.remove(name)
        left_suffix = cls.left_labeled_shape_suffix
        suffix_length = len(left_suffix)
        if name[-suffix_length:] == cls.left_labeled_shape_suffix:
            right_shape_name = cls._get_right_name_from_left(name)
            names.remove(right_shape_name)

    @classmethod                                ##  to Layer?
    def _get_right_name_from_left(cls, left_name):
        """Receives:
            left_name       str. The name of a left rule labeled shape
        Returns:
            right_name      str. The name of the associated right labeled 
                            shape
        """
        left_suffix = cls.left_labeled_shape_suffix
        suffix_length = len(left_suffix)
        rule_name = left_name[:-suffix_length]
        right_name = '%s%s' % (rule_name, cls.right_labeled_shape_suffix)
        return right_name

    @classmethod                                ##  07-11 06:10
    def _make_name_dat_dict(cls, name_elements_dict):
        """Receives:
            name_elements_dict {str: [guid, ...]}. A dictionary of 
                            name-guidlist entries of labeled shapes
        Returns a dictionary of name-datspec entries of labeled shapes:
            name_dat_dict
                            {str: (
                                [coord, ...],
                                [codex_codex, ...],
                                [codex_label])}
                            if the labeled shape is well-formed
                            {str: None}, if the labeled shape is ill-formed
            None            if unsuccessful
        """
        name_dat_dict = {}
        for labeled_shape_name in name_elements_dict:
            guids = name_dat_dict[labeled_shape_name]
            dat_spec = cls._get_dat_spec(guids)
            name_dat_dict[labeled_shape_name] = dat_spec
        return name_dat_dict

    @classmethod                                ##  07-11 06:45
    def _get_dat_spec(cls, guids):
        """Receives:
            guids           [guid, ...]. A list of guids of elements in a 
                            labeled shape, i.e., initial shape, left rule 
                            shape, or right rule shape
        Returns:
            dat_spec        (   [coord, ...],
                                [codex_codex, ...],
                                [codex_label, ...])
                            a triple consisting of a point coordinate list, a 
                            codex-codex list, and a codex-label list, if the 
                            labeled shape is well-formed, i.e., if it contains 
                            at least one guid (for initial and left shapes)
            None            otherwise           ?           
        """
        coord_list = []
        codex_codex_list = []
        codex_label_list = []
        dat_spec = (coord_list, codex_codex_list, codex_label_list)
        return dat_spec

    @classmethod
    def _get_ordered_labeled_shapes_string(
        cls, name_dat_dict
    ):
        """Receives:
            layer_names     [str, ...]
            x
        Returns:
            ordered_labeled_shapes_string
                            str: str\nstr\n...\nstr. The string form of 
                            [str, ...], an ordered list (by shape name) of 
                            .is strings of labeled shapes from both initial 
                            shapes and rules
        """
        labeled_shape_string_or_string_pairs = []
        for layer_name in layer_names:
            labeled_shape_string_or_string_pair = (
                cls._get_labeled_shape_string_or_string_pair(
                    layer_name))
            labeled_shape_string_or_string_pairs.append(
                labeled_shape_string_or_string_pair)

        labeled_shape_strings = []
        initial_shape_strings = cls._get_initial_shape_strings(
            initial_shape_layer_names)
        rule_shape_strings = cls._get_rule_shape_strings(
            rule_layer_names)
        labeled_shape_strings.append(initial_shape_strings)
        labeled_shape_strings.append(rule_shape_strings)
        ordered_labeled_shape_strings = sorted(labeled_shape_strings)
        ordered_labeled_shapes_string = '\n'.join(
            ordered_labeled_shape_strings)
        return ordered_labeled_shapes_string

    @classmethod
    def _get_ordered_initial_shapes_string(cls, name_dat_dict):
        """Receives:
            initial_shape_names
                            [str, ...]
            y
        Returns:
            ordered_initial_shapes_string
                            str\nstr\n...\nstr. The joined string of an 
                            ordered list of initial shape strings
        """
        initial_shape_strings = []
        for initial_shape_name in initial_shape_names:
            initial_shape_string = cls._get_initial_shape_string(
                initial_shape_name)
            initial_shape_strings.append(initial_shape_string)
        ordered_initial_shape_strings = sorted(initial_shape_strings)
        ordered_initial_shapes_string = '\n'.join(
            ordered_initial_shape_strings)
        return ordered_initial_shapes_string

    @classmethod
    def _get_ordered_rules_string(cls, name_dat_dict):
        """Receives:
            rule_names      [str, ...]
            z
        Returns:
            ordered_rules_string
                            str\nstr\n...\nstr. The joined string of an 
                            ordered list of rule strings
        """
        rule_strings = []
        for rule_name in rule_names:
            rule_string = cls._get_rule_string(rule_name)
            rule_strings.append(rule_string)
        ordered_rule_strings = sorted(rule_strings)
        ordered_rules_string = '\n'.join(ordered_rule_strings)
        return ordered_rules_string



