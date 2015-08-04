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

    @classmethod
    def get_dat_string(cls):
        """Composes the grammar's dat string, if the grammar is well-formed. 
        The grammar consists of:
            header
            ordered_labeled_shapes_string
            blank_line
            ordered_initial_shape_names_string
            ordered_rule_names_string
            blank_line
        The grammar is well-formed if and only if:
            it has at least one initial shape layer
            it has at least one rule layer
        Returns:
            dat_string      str. The grammar's dat string, if successful
            None            otherwise
        """
        #   try / error / else?
        initial_shape_frame_dict, rule_frame_pair_dict = (
            cls._make_element_frame_dicts())
                        ##  {rule_name: frame_instance}
                        ##  {rule_name: (frame_instance, frame_instance)}
        if (initial_shape_frame_dict == {} or 
            rule_frame_pair_dict == {}
        ):
            error_message = ' '.join([
                "The dat string could not be written", 
                "because the grammar must have", 
                "at least one initial shape layer", 
                "and at least one rule layer"])
            print(error_message)
            return_value = None
        else:
            labeled_shape_elements_dict = (
                cls._make_labeled_shape_elements_dict(
                    initial_shape_frame_dict, rule_frame_pair_dict))
                            ##  {labeled_shape: [element]}
            ordered_labeled_shapes_string = (
                cls._get_ordered_labeled_shapes_string(
                    labeled_shape_elements_dict))
                            ##  'labeled_shape_string\n...'
            initial_shapes = initial_shape_frame_dict.keys()
            ordered_initial_shape_names_string = (
                cls._get_ordered_initial_shape_names_string(initial_shapes))
                            ##  'initial    name\n...'
            rules = rule_frame_pair_dict.keys()
            ordered_rule_names_string = (
                cls._get_ordered_rule_names_string(rules))
                            ##  'rule    <name>    <name_L> -> <name_R>\n...'
            dat_header = cls.dat_header
            blank_line = cls.blank_line
            dat_string = '\n'.join([
                dat_header,
                ordered_labeled_shapes_string,  ##  polystring?
                blank_line,
                ordered_initial_shape_names_string, ##  polystring?
                ordered_rule_names_string,      ##  polystring?
                blank_line])
            return_value = dat_string
        return return_value

    @classmethod
    def _make_element_frame_dicts(cls):
        """Returns:
            (initial_shape_frame_dict, rule_frame_pair_dict), where:
                initial_shape_frame_dict
                            {str: guid}. A dictionary, possibly empty, of 
                            initial shape layer names and frame instance 
                            guids, if successful; None otherwise
                rule_frame_pair_dict
                            {str: (guid, guid)}. A dictionary, possibly empty, 
                            of rule shape layer names and frame instance guid 
                            pairs, if successful; None otherwise
        """
        initial_shapes, rules = g.Grammar.get_initial_shapes_and_rules()
        initial_shape_frame_dict = cls._make_initial_shape_frame_dict(
            initial_shapes)
        rule_frame_pair_dict = cls._make_rule_frame_pair_dict(rules)
        return_value = (
            initial_shape_frame_dict, 
            rule_frame_pair_dict)
        return return_value

    @classmethod                                ##  not called
    def _add_frame_instance_to_element_frame_dicts(
        cls,
        element_layer,
        frame_instance,
        initial_shape_frame_dict,
        rule_frame_pair_dict
    ):
        """Receives:
            element_layer   str. The name of an initial shape layer or a rule 
                            layer (guaranteed)
            frame_instance  guid. The guid of a frame instance on that layer 
                            (guaranteed)
            initial_shape_frame_dict
                            {str: guid}. A dictionary, possibly empty, of 
                            initial shape layer names and frame instance guids
            rule_frame_pair_dict
                            {str: (guid, guid)}. A dictionary, possibly empty, 
                            of rule shape layer names and frame instance guid 
                            pairs
        If there is no entry for element_layer in initial_shape_frame_dict, 
        adds a new entry to initial_shape_frame_dict. If there is an entry for 
        element_layer in initial_shape_frame_dict, deletes that entry and adds 
        a new entry (with both frame instances) to rule_frame_pair_dict. 
        Returns:
            initial_shape_frame_dict
                            {str: guid}. A dictionary, possibly empty, of 
                            initial shape layer names and frame instance guids
            rule_frame_pair_dict
                            {str: (guid, guid)}. A dictionary, possibly empty, 
                            of rule shape layer names and frame instance guid 
                            pairs
        """
        if element_layer in initial_shape_frame_dict:
            frame_instance_1 = initial_shape_frame_dict.pop(element_layer)
            frame_instance_2 = frame_instance
            cls._add_entry_to_rule_frame_pair_dict(
                element_layer, 
                frame_instance_1, 
                frame_instance_2, 
                rule_frame_pair_dict)
        else:
            cls._add_entry_to_initial_shape_frame_dict(
                element_layer, 
                frame_instance, 
                initial_shape_frame_dict)
        return (initial_shape_frame_dict, rule_frame_pair_dict)

    @classmethod
    def _add_entry_to_rule_frame_pair_dict(
        cls, 
        element_layer, 
        frame_instance_1, 
        frame_instance_2, 
        rule_frame_pair_dict
    ):
        """Receives:
            element_layer   str. The name of a rule layer (guaranteed)
            frame_instance_1
                            guid. The guid of the first frame instance on the 
                            layer (guaranteed)
            frame_instance_2
                            guid. The guid of the second frame instance on the 
                            layer (guaranteed)
            rule_frame_pair_dict
                            {str: (guid, guid)}. A dictionary, possibly empty, 
                            of rule shape layer names and frame instance guid 
                            pairs
        Adds a new layer-guid-pair entry, with the left guid first. Returns:
            rule_frame_pair_dict
                            {str: (guid, guid)}. A non-empty dictionary of 
                            rule shape layer names and frame instance guid 
                            pairs.
        """
        p1 = rs.BlockInstanceInsertPoint(frame_instance_1)
        p2 = rs.BlockInstanceInsertPoint(frame_instance_2)
        if p1 < p2:
            frame_instance_left = frame_instance_1
            frame_instance_right = frame_instance_2
        elif p1 > p2:
            frame_instance_left = frame_instance_2
            frame_instance_right = frame_instance_1
        else:
            error_message = "The two frame instances have the same location"
            print(error_message)
        rule_frame_pair_dict[element_layer] = (
            frame_instance_left, frame_instance_right)
        return rule_frame_pair_dict

    @classmethod
    def _add_entry_to_initial_shape_frame_dict(
        cls, element_layer, frame_instance, initial_shape_frame_dict):
        """Receives:
            element_layer   str. The name of an initial shape layer 
                            (guaranteed)
            frame_instance  guid. The guid of a frame instance on the layer 
                            (guaranteed)
            initial_shape_frame_dict
                            {str: guid}. A dictionary, possibly empty, of 
                            initial shape layer names and frame instance guids
        Adds a new layer_guid entry to the initial shape-frame dictionary. 
        Returns:
            initial_shape_frame_dict
                            {str: guid}. A non-empty dictionary of initial 
                            shape layer names and frame instance guids
        """
        initial_shape_frame_dict[element_layer] = frame_instance
        return initial_shape_frame_dict

    # @classmethod                                ##  not called
    # def _add_frame_instance_guid_to_rule_dict(
    #     cls, frame_instance_guid, frame_instance_layer, rule_frame_pair_dict
    # ):
        # """Receives:
        #     frame_instance_guid
        #                     guid. The guid of a frame instance
        #     frame_instance_layer
        #                     str. The name of the layer containing the frame 
        #                     instance
        #     rule_frame_pair_dict
        #                     {str: (guid, guid)}
        # Adds the frame guid to an entry, if one exists. Creates a new rule-
        # frame entry, otherwise
        # """
        # if frame_instance_layer in rule_frame_pair_dict:
        #     frame_instance_guid_1 = rule_frame_pair_dict[frame_instance_layer]
        #     frame_instance_guid_2 = frame_instance_guid
        #     p1 = rs.BlockInstanceInsertPoint(frame_instance_guid_1)
        #     p2 = rs.BlockInstanceInsertPoint(frame_instance_guid_2)
        #     if p1 < p2:
        #         rule_frame_pair_dict[frame_instance_layer] = (
        #             frame_instance_guid_1, frame_instance_guid_2)
        #     else:
        #         rule_frame_pair_dict[frame_instance_layer] = (
        #             frame_instance_guid_2, frame_instance_guid_1)
        # else:
        #     rule_frame_pair_dict[frame_instance_layer] = frame_instance_guid
        #     return rule_frame_pair_dict

    @classmethod
    def _make_initial_shape_frame_dict(cls, initial_shapes):
        """Receives:
            initial_shapes  [str]. A list, possibly empty, of names of layers 
                            containing one frame instance. The values are 
                            guaranteed
        Returns:
            initial_shape_frame_dict
                            {str: guid}. A dictionary, possibly empty, of 
                            initial shape names and frame instance guids
        """
        initial_shape_frame_dict = {}
        for initial_shape in initial_shapes:
            frame_instance = l.Layer.get_frame_instance(initial_shape)
            initial_shape_frame_dict[initial_shape] = frame_instance
        return initial_shape_frame_dict

    @classmethod
    def _make_rule_frame_pair_dict(cls, rules):
        """Receives:
            rules           [str]. A list, possibly empty, of names of layers 
                            containing two frame instances. The values are 
                            guaranteed
        Returns:
            rule_frame_pair_dict
                            {str: (guid, guid)}. A dictionary, possibly empty, 
                            of rule names and (ordered) frame instance guid 
                            pairs
        """
        rule_frame_pair_dict = {}
        for rule in rules:
            frame_pair = l.Layer.get_frame_instance_pair(rule)
            rule_frame_pair_dict[rule] = frame_pair
        return rule_frame_pair_dict

    @classmethod
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
                            names and lists of their element guids. The first 
                            guid is the guid of the frame instance
        """
        labeled_shape_elements_dict = {}
        for initial_shape in initial_shape_frame_dict:  ##  no such thing
            frame_instance = initial_shape_frame_dict[initial_shape]
            elements = cls._get_elements(frame_instance)
            elements.insert(0, frame_instance)
            frame_and_elements = elements
            labeled_shape_elements_dict[initial_shape] = frame_and_elements
        for rule in rule_frame_pair_dict:
            left_shape = '%s_L' % rule
            right_shape = '%s_R' % rule
            left_frame, right_frame = rule_frame_pair_dict[rule]
            left_elements = cls._get_elements(left_frame)
            right_elements = cls._get_elements(right_frame)
            left_elements.insert(0, left_frame)
            right_elements.insert(0, right_frame)
            left_frame_and_elements = left_elements
            right_frame_and_elements = right_elements
            labeled_shape_elements_dict[left_shape] = left_frame_and_elements
            labeled_shape_elements_dict[right_shape] = (
                right_frame_and_elements)
        return labeled_shape_elements_dict

    @classmethod
    def _get_elements(cls, frame_instance):
        """Receives:
            frame_instance  str. The name of a frame instance
        Returns:
            elements        [guid, ...]. A list of the guids of the elements 
                            in the frame instance. 
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
            name_elements_dict
                            {str: [guid, ...]}. A dictionary of 
                            name-guidlist entries of labeled shapes
        Returns a dictionary of name-datspec entries of labeled shapes:
            name_dat_dict   {str: (
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

    @classmethod                                ##  polystring?
    def _get_ordered_labeled_shapes_string(
        cls, labeled_shape_name_elements_dict
    ):
        """Receives:
            labeled_shape_name_elements_dict
                            {str: [guid, ...]}. A dictionary of labeled shape 
                            names and lists of the guids of their elements
        Returns:
            ordered_labeled_shapes_string       ##  poly_string
                            str\nstr\n...\nstr. The string form of [str, ...], 
                            an ordered list (by shape name) of .is strings of 
                            labeled shapes from both initial shapes and rules
        """
        method_name = '_get_ordered_labeled_shapes_string'
        try:
            if labeled_shape_name_elements_dict == {}:
                raise ValueError
        except ValueError:
            message = "The labeled shape name-elements dictionary is empty"
            print("%s.%s\n    %s" % (cls.__name__, method_name, message))
            return_value = None
        else:
            labeled_shape_strings = []
            for name in labeled_shape_name_elements_dict:
                element_guids = labeled_shape_name_elements_dict[name]
                                                ##  [guid, ...]
                line_and_labeled_point_specs = (
                    cls._get_ordered_line_and_labeled_point_specs(
                        element_guids))
                                                ##  (   [line_spec], 
                                                ##      [labeled_point_spec])
                labeled_shape_string = cls._get_labeled_shape_string(
                    line_and_labeled_point_specs)
                                                ##  str
                named_labeled_shape_string = '\n'.join([
                    'shape    %s' % name,
                    labeled_shape_string])
                labeled_shape_strings.append(named_labeled_shape_string)
            ordered_labeled_shape_strings = sorted(labeled_shape_strings)
            ordered_labeled_shapes_string = '\n'.join(
                ordered_labeled_shape_strings)
            return_value = ordered_labeled_shapes_string
        finally:
            return return_value

    @classmethod
    def _get_ordered_line_and_labeled_point_specs(cls, element_guids):
        """Receives:
            element_guids   [guid, ...]. A list of the guids of (first) the 
                            frame instance and (then) the lines and labeled 
                            points
        Returns:
            ordered_line_and_labeled_point_specs
                            ([line_spec, ...], [labeled_point_spec, ...]). A 
                            list of line specs 
                                (   (num, num, num), 
                                    (num, num, num)) 
                            and a list of labeled point specs
                                (   str,
                                    (num, num, num))
                            where the specs are relative to the frame 
                            instance, if successful
            None            otherwise
        """
        method_name = '_get_ordered_line_and_labeled_point_specs'
        try:
            if element_guids == []:
                raise ValueError
        except ValueError:
            message = "There is no frame instance"
            print("%s.%s\n    %s" % (cls.__name__, method_name, message))
            return_value = None
        else:
            line_specs , labeled_point_specs = [], []
            frame_instance = element_guids.pop(0)
            frame_position = rs.BlockInstanceInsertPoint(frame_instance)
            curve_type, textdot_type = 4, 8192
            for element_guid in element_guids:
                if rs.ObjectType(element_guid) == curve_type:
                    p1_absolute = rs.CurveStartPoint(element_guid)
                    p2_absolute = rs.CurveEndPoint(element_guid)
                    p1_relative = rs.PointSubtract(p1_absolute, frame_position)
                    p2_relative = rs.PointSubtract(p2_absolute, frame_position)
                    p1_spec = tuple(p1_relative)
                    p2_spec = tuple(p2_relative)
                    if p1_spec < p2_spec:
                        tail = p1_spec
                        head = p2_spec
                    elif p1_spec > p2_spec:
                        tail = p2_spec
                        head = p1_spec
                    line_spec = (tail, head)
                    line_specs.append(line_spec)
                elif rs.ObjectType(element_guid) == textdot_type:
                    label = rs.TextDotText(element_guid)
                    p_absolute = rs.TextDotPoint(element_guid)
                    p_relative = rs.PointSubtract(p_absolute, frame_position)
                    p_spec = tuple(p_relative)
                    labeled_point_spec = (label, p_spec)
                    labeled_point_specs.append(labeled_point_spec)
                else:
                    pass
            ordered_line_and_labeled_point_specs = (
                sorted(line_specs), sorted(labeled_point_specs))
            return_value = ordered_line_and_labeled_point_specs
        finally:
            return return_value

    @classmethod
    def _get_labeled_shape_string(cls, line_and_labeled_point_specs):
        """Receives:
            line_and_labeled_point_specs
                            (   [((num, num, num), (num, num, num)), ...], 
                                [(str, (num, num, num)), ...])
                            A duple: 1) a list of line specs, and 2) a list of 
                            labeled point specs
        Returns:
            labeled_shape_string
                            str. The .is string of the labeled shape, without 
                            the 'shape    <name>' line
        """
        spacer = cls.spacer
        indented_name_string = '%sname' % spacer
                            ##  '    name'
        line_specs, labeled_point_specs = line_and_labeled_point_specs
        ordered_point_specs = (
            cls._make_ordered_point_specs(line_specs, labeled_point_specs))
                            ##  [(0, 0, 0), (0, 0, 1), ...]
        ordered_indented_coord_codex_xyz_polystring = (
            cls._make_ordered_indented_coord_codex_xyz_polystring(
                ordered_point_specs))
                            ##  '    coords 0 0 0 0\n    coords 1 0 0 1\n...'
        blank_line = cls.blank_line
        ordered_indented_line_lindex_codex_codex_polystring = (
            cls._make_ordered_indented_line_lindex_codex_codex_polystring(
                line_specs, ordered_point_specs))
                            ##  '    line 0 0 1\n    line 1 1 0\n...'
        ordered_indented_point_codex_label_polystring = (
            cls._make_ordered_indented_point_codex_label_polystring(
                labeled_point_specs, ordered_point_specs))
                            ##  '    point 0 a\n    point 1 a\n...'
        indented_name_string_parts = []
        indented_name_string_parts.append(indented_name_string)
        if ordered_indented_coord_codex_xyz_polystring:
            indented_name_string_parts.append(
                ordered_indented_coord_codex_xyz_polystring)
        if (ordered_indented_line_lindex_codex_codex_polystring or
            ordered_indented_point_codex_label_polystring
        ):
            indented_name_string_parts.append(blank_line)
        if ordered_indented_line_lindex_codex_codex_polystring:
            indented_name_string_parts.append(
                ordered_indented_line_lindex_codex_codex_polystring)
        if ordered_indented_point_codex_label_polystring:
            indented_name_string_parts.append(
                ordered_indented_point_codex_label_polystring)
        labeled_shape_string = '\n'.join(indented_name_string_parts)
        return labeled_shape_string

    @classmethod
    def _make_ordered_point_specs(cls, line_specs, labeled_point_specs):
        """Receives:
            line_specs      [line_spec, ...]. A list of line specs, each of 
                            the form 
                                ((num, num, num), (num, num, num))
            labeled_point_specs
                            [labeled_point_spec, ...]. A list of labeled point 
                            specs, each of the form 
                                (str, (num, num, num))
        Returns:
            ordered_point_specs
                            [point_spec, ...]. An ordered list of point specs, 
                            each of the form 
                                (num, num, num)
        """
        point_specs = []
        for line_spec in line_specs:
            for point_spec in line_spec:
                if not point_spec in point_specs:
                    point_specs.append(point_spec)
        for labeled_point_spec in labeled_point_specs:
            point_spec = labeled_point_spec[1]
            if not point_spec in point_specs:
                point_specs.append(point_spec)
        ordered_point_specs = sorted(point_specs)
        return ordered_point_specs

    @classmethod
    def _make_ordered_indented_coord_codex_xyz_polystring(
        cls, ordered_point_specs
    ):
        """Receives:
            ordered_point_specs
                            [point_spec, ...]. An ordered list of point specs 
                            of the form 
                                (num, num, num)
        Returns:
            ordered_indented_coord_codex_xyz_polystring
                            str\n.... An ordered joining of indented coord 
                            line strings, each of the form 
                                '    coords int num num num'
        """
        ordered_indented_coord_codex_xyz_strings = []
        for point_spec in ordered_point_specs:
            codex = ordered_point_specs.index(point_spec)
            x, y, z = point_spec
            indented_coord_codex_xyz_string = '%scoords %i %s %s %s' % (
                cls.spacer, codex, x, y, z)
            ordered_indented_coord_codex_xyz_strings.append(
                indented_coord_codex_xyz_string)
        ordered_indented_coord_codex_xyz_polystring = '\n'.join(
            ordered_indented_coord_codex_xyz_strings)
        return ordered_indented_coord_codex_xyz_polystring

    @classmethod
    def _make_ordered_indented_line_lindex_codex_codex_polystring(
        cls, line_specs, ordered_point_specs
    ):
        """Receives:
            line_specs      [line_spec, ...]. A list of line specs, each of 
                            the form
                                ((num, num, num), (num, num, num))
            ordered_point_specs
                            [point_spec, ...]. A list of point specs, each of 
                            the form
                                (num, num, num)
        Returns:
            ordered_indented_line_lindex_codex_codex_polystring
                            str\n.... An ordered joining of indented line- 
                            lindex-codex-codex strings, each of the form
                                '    line 0 0 0'
        """
        ordered_indented_line_lindex_codex_codex_strings = []
        ordered_line_specs = sorted(line_specs)
        for line_spec in ordered_line_specs:
            lindex = ordered_line_specs.index(line_spec)
            tail, head = sorted(line_spec)
            codex1 = ordered_point_specs.index(tail)
            codex2 = ordered_point_specs.index(head)
            ordered_indented_line_lindex_codex_codex_string = (
                '%sline %i %i %i' % (cls.spacer, lindex, codex1, codex2))
            ordered_indented_line_lindex_codex_codex_strings.append(
                ordered_indented_line_lindex_codex_codex_string)
        ordered_indented_line_lindex_codex_codex_polystring = '\n'.join(
            ordered_indented_line_lindex_codex_codex_strings)
        return ordered_indented_line_lindex_codex_codex_polystring

    @classmethod
    def _make_ordered_indented_point_codex_label_polystring(
        cls, labeled_point_specs, ordered_point_specs
    ):
        """Receives:
            labeled_point_specs
                            [labeled_point_spec, ...]. A list of labeled point 
                            specs, each of the form
                                (str, (num, num, num))
            ordered_point_specs
                            [point_spec, ...]. A list of point specs, each of 
                            the form
                                (num, num, num)
        Returns:
            ordered_indented_point_codex_label_polystring
                            str\n.... An ordered joining of indented point-
                            codex-label strings, each of the form
                                '    point 0 a'
        """
        ordered_indented_point_codex_label_strings = []
        ordered_labeled_point_specs = sorted(labeled_point_specs)
        for labeled_point_spec in ordered_labeled_point_specs:
            label, point = labeled_point_spec
            codex = ordered_point_specs.index(point)
            indented_point_codex_label_string = '%spoint %i %s' % (
                cls.spacer, codex, label)
            ordered_indented_point_codex_label_strings.append(
                indented_point_codex_label_string)
        ordered_indented_point_codex_label_polystring = '\n'.join(
            ordered_indented_point_codex_label_strings)
        return ordered_indented_point_codex_label_polystring


    @classmethod                                ##  polystring?
    def _get_ordered_initial_shape_names_string(cls, initial_shapes):
        """Receives:
            initial_shapes  [str, ...]. A list of names of initial shapes
        Returns:
            ordered_initial_shape_names_string
                            str\nstr\n...\nstr. The joining of an ordered 
                            list of initial shape name strings, each of the 
                            form 
                                '    initial    <name>'
        """
        initial_shape_name_strings = []
        for name in initial_shapes:
            initial_shape_name_string = (
                cls._get_initial_shape_name_string(name))
            initial_shape_name_strings.append(initial_shape_name_string)
        ordered_initial_shape_name_strings = sorted(
            initial_shape_name_strings)
        ordered_initial_shape_names_string = '\n'.join(
            ordered_initial_shape_name_strings)
        return ordered_initial_shape_names_string

    @classmethod
    def _get_initial_shape_name_string(cls, name):
        """Receives:
            name            str. The name of an initial shape
        Returns:
            initial_shape_name_string
                            str. In the form:
                                'initial    <name>'
        """
        initial_shape_name_string = "initial%s%s" % (
            cls.spacer, name)
        return initial_shape_name_string

    @classmethod                                ##  polystring?
    def _get_ordered_rule_names_string(cls, rules):
        """Receives:
            rules           [str, ...]. A list of names of rules
        Returns:
            ordered_rule_names_string
                            str\nstr\n...\nstr. The joining of an ordered list 
                            of rule strings
        """
        rule_name_strings = []
        for name in rules:
            rule_name_string = cls._get_rule_name_string(name)
            rule_name_strings.append(rule_name_string)
        ordered_rule_name_strings = sorted(rule_name_strings)
        ordered_rule_names_string = '\n'.join(ordered_rule_name_strings)
        return ordered_rule_names_string

    @classmethod
    def _get_rule_name_string(cls, name):
        """Receives:
            name            str. The name of a rule
        Returns:
            rule_name_string
                            str. In the form:
                                'rule    <name>    <name>_L -> <name>_R'
        """
        spacer = cls.spacer
        rule_name_string = 'rule%s%s%s%s_L -> %s_R' % (
            spacer, name, spacer, name, name)
                                                ##  centralize?
        return rule_name_string

