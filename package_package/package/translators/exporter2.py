from package.view import layer as l
import rhinoscriptsyntax as rs

class Exporter2(object):
    def __init__(self):
        self.class_name = 'Exporter2'

    ### Initial shape methods
    def export_initial_shape(self):             ##  03-02 16:00
        """Writes the repr string of an initial shape to a file named 
        <initial_shape>.is. Returns:
            str             the repr string
        """
        new_shape = self._get_labeled_shape()
        shape_repr = repr(new_shape)
        self._write_file('is', shape_repr)

    def _get_labeled_shape(self):               ##  03-02 16:57
        """Returns:
            LabeledShape    the SG object identified by the user
        """
        labeled_shape_name = self._get_labeled_shape_name()
        new_labeled_shape = self._get_labeled_shape_from_labeled_shape_name(
            labeled_shape_name)
        return new_labeled_shape

    def _get_labeled_shape_name(self):          ##  03-02 16:03
        """Prompts the user to select a labeled shape tag, if one is not 
        already selected. Returns:
            str             the name of a shape
        """                                     ##  How about entering name?
        labeled_shape_tag = rs.GetObject(filter='annotation')
        labeled_shape_name = rs.get_name_from_tag(labeled_shape_tag)
        return labeled_shape_name

    ### Rule methods
    def export_rule(self):                      ##  03-02 16:00
        """Writes the repr string of a rule to a file named <rule_name>.rul. 
        Returns:
            str             the repr string
        """
        new_rule = self._get_rule()
        rule_repr = repr(new_rule)
        self._write_file('rul', rule_repr)

    def _get_rule(self):
        """Returns:
            Rule            the SG object identified by the user
        """
        rule_name = self._get_selected_rule_name()
        labeled_shape_names = (
            self._get_labeled_shape_names_from_rule_name(rule_name))
        left_labeled_shape, right_labeled_shape = (
            self._get_labeled_shapes_from_labeled_shape_names(
                labeled_shape_names))
        new_rule = rule.Rule.new(left_labeled_shape, right_labeled_shape)
        return new_rule

    def _get_selected_rule_name(self):          ##  03-03 08:15
        """Prompts the user to select a rule name tag, if one is not already 
        selected. Returns:
            str             the name of a rule
        """
        selected_objects = rs.SelectedObjects()
        rule_name_tag = self._get_rule_name_tag_from(selected_objects)
        if not rule_name_tag:
            message = "Please select the name tag of a rule"
            annotation_filter = 512
            rule_name_tag = rs.GetObject(message, annotation_filter)
        rule_name = rs.TextObjectText(rule_name_tag)
        return rule_name

    def _get_rule_name_tag_from(self, objects): ##  03-13 10:21
        """Extracts a rule name tag from a list of objects. Receives: 
            objects         [guid, ...]
        Returns:
            guid            the guid of a rule name tag, if any
            None            otherwise
        """
        pass

    def _get_labeled_shape_names_from_rule_name(self, rule_name):
        """Gets the labeled shape names associated with the rule name. 
        Receives:
            rule_name       str
        Returns:
            (str, str)      the left and right labeled shape names
        """
        left_and_right_labeled_shape_names = 'shape_names'
        return left_and_right_labeled_shape_names

    def _get_labeled_shapes_from_labeled_shape_names(
        self, labeled_shape_names
    ):
        """Receives:
            labeled_shape_names
                            (str, str). The names of the left and right 
                            labeled shapes
        Returns:
            [LabeledShape, LabeledShape]
                            the left and right labeled shapes
        """
        labeled_shapes = []
        for name in labeled_shape_names:
            labeled_shape = self._get_labeled_shape_from_labeled_shape_name(
                name)
            labeled_shapes.append(labeled_shape)
        return labeled_shapes

    ### Shared methods
    def _get_labeled_shape_from_labeled_shape_name(self, labeled_shape_name):
        """Receives:                            ##  03-14 08:10
            labeled_shape_name
                            str; type guaranteed by the calling method
        Returns:
            LabeledShape    the SG labeled shape identified by the name, if
                            successful
            None            otherwise
        """
        method_name = '_get_labeled_shape_from_labeled_shape_name'
        try:
            if not l.Layer.layer_name_is_in_use(labeled_shape_name):
                raise ValueError
        except ValueError:
            message = "There is no labeled shape with that name"
            print("%s.%s:\n    %s" % (self.class_name, method_name, message))
            return_value = None
        else:
            labeled_shape_elements = (
                self._get_elements_from_labeled_shape_name(
                    labeled_shape_name))        ##  to do
            new_labeled_shape = labeled_shape.LabeledShape.new_from_elements(
                labeled_shape_elements)         ##  to do
            return_value = new_labeled_shape
        finally:
            return return_value

    def _get_elements_from_labeled_shape_name(self, labeled_shape_name):
                                                ##  03-20 09:36
        """Gets the elements of a labeled shape. Receives:
            labeled_shape_name
                            str. Value confirmed by the calling method
        Returns:
            ([line_spec, ..], [labeled_point_spec, ...])
                            1. A list of line specs (point3d, point3d)
                            2. A list of labeled point specs: (point3d, str)
                            if successful
            None            otherwise
        """
        guids = rs.ObjectsByLayer(labeled_shape_name)
        line_guids, lpoint_guids = self._sort_guids(guids)
        line_specs = self._get_line_specs(line_guids)
        lpoint_specs = self._get_lpoint_specs(lpoint_guids)
        # line_specs = 'line_specs'
        # lpoint_specs = 'lpoint_specs'
        return (line_specs, lpoint_specs)

    def _sort_guids(self, guids):
        """Sorts guids by object type. Receives:
            guids           [guid, ...], n >= 0
        Returns:
            (line_guids, labeled_point_guids)
                            labeled_point_guids (textdot guids)
        """
        print("len(guids): %i" % len(guids))
        print("guids: %s" % guids)
        curve_type = 4
        textdot_type = 8192
        line_guids = rs.ObjectsByType(curve_type)
        lpoint_guids = rs.ObjectsByType(textdot_type)
        return (line_guids, lpoint_guids)

    def _get_line_specs(self, line_guids):      ##  03-26 10:25
        """Receives:
            line_guids      [line_guid, ...], n >= 0
        Returns:
            [line_spec, ...], ordered
                            line_spec: ((num, num, num), (num, num, num)),
                            if successful
            None            otherwise
        """
        method_name = "_get_line_specs"
        try:
            if not (
                type(line_guids) == list and
                self._are_line_guids(line_guids)
            ):
                raise TypeError
        except TypeError:
            message = "The argument must be a list of line guids"
            print("%s.%s:\n    %s" % (self.class_name, method_name, message))
            return_value = None
        else:
            line_specs = []
            for guid in line_guids:
                line_spec = self._get_line_spec_from(guid)
                line_specs.append(line_spec)
            return_value = sorted(line_specs)   ##  doesn't work
        finally:
            return return_value

    def _are_line_guids(self, guids):
        value = True
        for guid in guids:
            if not rs.IsLine(guid):
                value = False
                break
        return value

    def _get_line_spec_from(self, line_guid):   ##  03-29 08:33
        """Receives:
            line_guid
        Returns:
            (num, num, num) line spec
        """
        p1 = rs.CurveStartPoint(line_guid)
        p2 = rs.CurveEndPoint(line_guid)
        p1_spec = rs.PointCoordinates(p1)
        p2_spec = rs.PointCoordinates(p2)
        return (p1_spec, p2_spec)
        # return (p1, p2)

    def _get_lpoint_specs(self, lpoint_guids):
        """Receives:
            lpoint_guids    [lpoint_guid, ...], n >= 0
        Returns:
            [lpoint_spec, ...], ordered
                            lpoint_spec: ((num, num, num), str)
        """
        pass

    def _write_file(self, file_type, shape_name, string):
        """Writes a string to a file with the name shape_name and the 
        appropriate suffix. Receives:
            file_type       str: 'is' | 'rul' | 'dat'
            shape_name      str
            string          str
        Returns:
            str             the string, if successful
            None            otherwise
        """
        method_name = "_write_file"
        legal_file_types = ['is', 'rul', 'dat']
        try:
            if not (
                type(file_type) == str and
                type(string) == str
            ):
                raise TypeError
            if not file_type in legal_file_types:
                raise ValueError
        except TypeError:
            message = "The file_type and string must both be strings"
            print("%s.%s:\n    %s" % (self.class_name, method_name, message))
            return_value = None
        except ValueError:
            message = "The file type must be 'is', 'rul', or 'dat"
            print("%s.%s:\n    %s" % (self.class_name, method_name, message))
            return_value = None
        else:
            filter = self._get_filter_from_file_type(file_type)
            file_name = (
                rs.SaveFileName('Save shape as', filter, '', shape_name))
            if not file_name:
                return
            file = open(file_name, 'w')
            empty_line = ''
            shape_string = '\n'.join([
                string,
                empty_line])
            file.write(shape_string)
            file.close()
            print(shape_string)
            return_value = string
        finally:
            return return_value

    def _get_filter_from_file_type(self, file_type):
        """Constructs the filter string appropriate to the file type. 
        Receives:
            file_type       str
        Returns:
            str             the filter string
        """
        file_type_caps = file_type.upper()
        filter_string = "%s file (*.%s)|*.%s|All files (*.*)|*.*||" % (
            file_type_caps, file_type, file_type)
        return filter_string
