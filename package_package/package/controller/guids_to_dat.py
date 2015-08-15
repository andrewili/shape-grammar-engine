from package.view import frame as f
from package.view import layer as l
import rhinoscriptsyntax as rs
from package.view import settings as s

class GuidsToDat(object):
    dat_header = "%s\n%s" % (
        "# shape data version 6.00",
        "unit  mm  # mm - millimetre, cm - centimetre, m - metre")
    blank_line = ''
    spacer = '    '

    def __init__(self):
        pass

                                                ##  ill-formed components
    @classmethod                                ##  08-13 10:32
    def get_dat_string(cls, initial_shapes, rules):
        """Receives:
            initial_shapes  [str, ...]. A non-empty list of the names of 
                            layers containing one frame instance. Value 
                            guaranteed by caller
            rules           [str, ...]. A non-empty list of the names of 
                            layers containing two frame instances. Value 
                            guaranteed by caller
        Composes the grammar's dat string. The grammar consists of:
            header
            ordered_labeled_shapes_string
            blank_line
            ordered_initial_shape_names_string
            ordered_rule_names_string
            blank_line
        Omits empty initial shapes and rules with empty left shapes. Returns:
            dat_string      str. The grammar's dat string
        """
        initial_shape_frame_dict = (
            cls._make_initial_shape_frame_dict(initial_shapes))
                            ##  {rule_name: frame_instance}
        rule_frame_pair_dict = (
            cls._make_rule_frame_pair_dict(rules))
                            ##  {rule_name: (frame_instance, frame_instance)}
        labeled_shape_elements_dict = (
            cls._make_labeled_shape_elements_dict(
                initial_shape_frame_dict, rule_frame_pair_dict))
                            ##  {labeled_shape: [element]}
                                                ##  len(list) == 1 -> 
                                                ##  reduce lshape list
                                                ##  send message
        ordered_labeled_shapes_string = (
            cls._get_ordered_labeled_shapes_string(
                labeled_shape_elements_dict))
                            ##  'labeled_shape_string\n...'
        initial_shapes = initial_shape_frame_dict.keys()
                                                ##  replace
        ordered_initial_shape_names_string = (
            cls._get_ordered_initial_shape_names_string(initial_shapes))
                            ##  'initial    name\n...'
        rules = rule_frame_pair_dict.keys()
                                                ##  replace
        # initial_shapes, rules = cls._get_components(
        #     labeled_shape_elements_dict)
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

    @classmethod                                ##  called
    def _make_initial_shape_frame_dict(cls, initial_shapes):
        """Receives:
            initial_shapes  [str]. A non-empty list of names of layers 
                            containing one frame instance. The value is
                            guaranteed by the caller
        Returns:
            initial_shape_frame_dict
                            {str: guid}. A non-empty dictionary of initial 
                            shape names and frame instance guids
        """
        initial_shape_frame_dict = {}
        for initial_shape in initial_shapes:
            frame_instance = l.Layer.get_frame_instance(initial_shape)
            initial_shape_frame_dict[initial_shape] = frame_instance
        return initial_shape_frame_dict

    @classmethod                                ##  called
    def _make_rule_frame_pair_dict(cls, rules):
        """Receives:
            rules           [str]. A non-empty list of names of layers 
                            containing two frame instances. The value is 
                            guaranteed by the caller
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

    ####

    @classmethod
    def _make_labeled_shape_elements_dict(
        cls, initial_shape_frame_dict, rule_frame_pair_dict
    ):
        """Receives:
            initial_shape_frame_dict
                            {str: guid}. A non-empty dictionary of initial 
                            shape names and frame instance guids
            rule_frame_pair_dict
                            {str: (guid, guid)}. A non-empty dictionary of 
                            rule names and frame instance guid pairs
        Returns:
            labeled_shape_elements_dict
                            {str: [guid, ...]}. A non-empty dictionary of 
                            labeled shape names and lists of their element 
                            guids. The first guid is the guid of the frame 
                            instance
        """
        labeled_shape_elements_dict = {}
        ill_formed_components = []
        for initial_shape in initial_shape_frame_dict:
            (   frame_instance
            ) = (
                initial_shape_frame_dict[initial_shape])
            elements = cls._get_elements(frame_instance)
            if elements == []:
                ill_formed_components.append(initial_shape)
            else:
                elements.insert(0, frame_instance)
                frame_and_elements = elements
                labeled_shape_elements_dict[initial_shape] = (
                    frame_and_elements)
        for rule in rule_frame_pair_dict:
            (   left_frame, 
                right_frame
            ) = (
                rule_frame_pair_dict[rule])
            left_elements = cls._get_elements(left_frame)
            if left_elements == []:
                ill_formed_components.append(rule)
            else:
                left_shape = '%s_L' % rule
                right_shape = '%s_R' % rule
                right_elements = cls._get_elements(right_frame)
                left_elements.insert(0, left_frame)
                right_elements.insert(0, right_frame)
                left_frame_and_elements = left_elements
                right_frame_and_elements = right_elements
                labeled_shape_elements_dict[left_shape] = (
                    left_frame_and_elements)
                labeled_shape_elements_dict[right_shape] = (
                    right_frame_and_elements)
        if ill_formed_components:
            error_message = "%s %s" % (
                "The following initial shapes and rules were omitted", 
                "because they contained inappropriate empty shapes")
            print("%s: %s" % (error_message, ill_formed_components))
        return labeled_shape_elements_dict

    @classmethod                                ##  called
    def _get_elements(cls, frame_instance):
        """Receives:
            frame_instance  str. The name of a frame instance
        Returns:
            elements        [guid, ...]. A list of the guids of the elements 
                            in the frame instance. 
        """
        objects_on_layer = l.Layer.get_objects_on_layer(frame_instance)
        elements = cls._extract_elements_in_frame(
            frame_instance, objects_on_layer)
        return elements

    @classmethod                                ##  called
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

    @classmethod                                ##  called
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

    @classmethod                                ##  called
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

    @classmethod                                ##  called
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

    @classmethod                                ##  called / polystring?
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

    @classmethod                                ##  called
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

    @classmethod                                ##  called
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

    @classmethod                                ##  called
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

    @classmethod                                ##  called
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

    @classmethod                                ##  called
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

    @classmethod                                ##  called
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

    @classmethod                                ##  called / polystring?
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

    @classmethod                                ##  called
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

    @classmethod                                ##  called / polystring?
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

    @classmethod                                ##  called
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

