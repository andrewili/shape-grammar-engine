from package.scripts import component_name as cn
from package.scripts import layer as l
from package.model import labeled_shape as ls
from package.model import point
from package.scripts import rule as r
import rhinoscriptsyntax as rs

class Exporter(object):
    def __init__(self):
        self.class_name = 'Exporter'

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
    def export_rule(self):                      ##  04-21 11:27 03-02 16:00
        """Prompts the user to select a rule name tag. Writes the rule's repr 
        string to a file named <rule_name>.rul. Returns:
            str             the repr string
        """
        rule_name = self._get_rule_name()
        rule_spec = self._get_spec_from_rule_name(rule_name)
        rule_repr = self._get_repr_from_rule_spec(rule_spec)
        self._write_file('rul', rule_repr)

    def _get_rule_name(self):
        """Prompts the user to select a rule name tag, if one is not already 
        selected. Returns:
            str             the name of a rule
        """
        while not self._a_rule_name_tag_is_selected():
            rule_name_tag = self._get_rule_name_tag()
            rs.SelectObject(rule_name_tag)
        rule_name = self._get_rule_name_from(rule_name_tag)
        return rule_name

    def _a_rule_name_tag_is_selected(self):
        """Returns:
            boolean         True, if the selected object is a rule name tag
                            False, otherwise
        """
        return_value = True
        selected_objects = rs.SelectedObjects()
        if not len(selected_objects) == 1:
            return_value = False
        else:
            selected_object = selected_objects[0]
            if not (
                rs.IsText(selected_object) and
                cn.ComponentName._component_name_is_listed(
                    'rule', 
                    rs.TextObjectText(selected_object))
            ):
                return_value = False
        return return_value

    def _get_rule_name_tag(self):
        """Prompts the user to select a rule name tag. Returns:
            guid            the guid of a rule name tag
        """
        message = "Select a rule name tag"
        text_filter = 512
        rule_name_tag = rs.GetObject(message, text_filter)
        return rule_name_tag

    def _get_rule_name_from(self, rule_name_tag):
        """Receives:
            rule_name_tag   the guid of a text object; the type is guaranteed 
                            by the calling method
        Returns:
            str             the text of the text object, i.e., the rule name
        """
        return_value = rs.TextObjectText(rule_name_tag)
        return return_value

    def _get_spec_from_rule_name(self, rule_name):  ##  05-09 08:43
        """Receives:
            rule_name       str; value guaranteed by the calling method
        Returns:
            rule_spec       (rule_name, left_shape_spec, right_shape_spec), if
                            successful
                            rule_name       str
                            left_shape_spec (   shape_name,
                                                line_specs,
                                                lpoint_specs)
                            right_shape_spec
                                            (   shape_name,
                                                line_specs,
                                                lpoint_specs)
            None otherwise  ##  implement!
        """
        method_name = '_get_spec_from_rule_name'
        left_shape_name = r.Rule._get_shape_name_from_rule_name('left')
        right_shape_name = r.Rule._get_shape_name_from_rule_name('right')
        left_shape_spec = self._get_spec_from_labeled_shape_name(
            left_shape_name)
        right_shape_spec = self._get_spec_from_labeled_shape_name(
            right_shape_name)
        rule_spec = (rule_name, left_shape_spec, right_shape_spec)
        return rule_spec

    def _get_spec_from_labeled_shape_name(self, shape_name):    ##  05-09 08:58
        """Receives:
            shape_name      str; value guaranteed?
        Returns:
            shape_spec      (   shape_name,
                                ordered_line_specs,
                                ordered_lpoint_specs)
                            shape_name:     str
                            ordered_line_specs:
                                            [line_spec, ...]
                            ordered_lpoint_specs:
                                            [lpoint_spec, ...]
                            line_spec:      (point_spec, point_spec)
                            lpoint_spec:    (str, point_spec)
                            point_spec:     (num, num, num)
        """
        guids = self._get_guids_from_shape_name(shape_name)
        line_guids, lpoint_guids = self._sort_guids(guids)
        ordered_line_specs = self._get_ordered_specs_from_line_guids(
            line_guids)
        ordered_lpoint_specs = self._get_ordered_specs_from_lpoint_guids(
            lpoint_guids)
        shape_spec = (shape_name, ordered_line_specs, ordered_lpoint_specs)
        return shape_spec

    def _get_guids_from_shape_name(self, shape_name):   ##  05-10 06:47
        """Receives:
            shape_name      the name of a shape in a rule; type and value
                            guaranteed by the calling function
        Returns:
            [guid, ...]     a list of the guids (lines and text objects) in
                            the shape, i.e., excluding the frame
        """
        guids = rs.ObjectsByLayer(shape_name)
        shape_guids = []
        for guid in guids:
            if not rs.IsBlockInstance(guid):
                shape_guids.append(guid)
        return shape_guids

    def _get_ordered_specs_from_line_guids(self, line_guids):   ##  05-10 06:50
        """Receives:
            line_guids  [guid, ...]; a list of line guids
        Returns:
            ordered_line_specs
                        [line_spec, ...], if successful
                        line_spec:      (point_spec, point_spec)
                        point_spec:     (num, num, num)
            None        otherwise
        """
        line_specs = []
        for line_guid in line_guids:
            # line_spec = self._get_ordered_spec_from_line_guid(line_guid)
            line_spec = self._get_spec_from_line_guid(line_guid)
            line_specs.append(line_spec)
        ordered_line_specs = sorted(line_specs)
        return ordered_line_specs

    # def _get_ordered_spec_from_line_guid(self, line_guid):  ##  05-10 07:26
        # """Receives:
        #     line_guid
        # Returns:
        #     ordered_line_spec
        #                 (p1_spec, p2_spec), where p1 < p2
        # """
        # point1_guid, point2_guid = self._get_point_guids_from_line_guid(
        #     line_guid)
        # p1_spec = self._get_spec_from_point_guid(point1_guid)
        # p2_spec = self._get_spec_from_point_guid(point2_guid)
        # line_spec = (p1_spec, p2_spec)
        # ordered_line_spec = sorted(line_spec)
        # return ordered_line_spec

    # def _get_point_guids_from_line_guid(self, line_guid):   ##  05-10 07:28
        # """Receives:
        #     line_guid
        # Returns:
        #     (point_guid, point_guid)
        # """
        # return (point1_guid, point2_guid)

    # def _get_spec_from_point_guid(self, point_guid):    ##  05-10 07:29
        # """Receives:
        #     point_guid
        # Returns:
        #     (num, num, num)
        # """
        # return point_spec

    def _get_ordered_specs_from_lpoint_guids(self, lpoint_guids):
        """Receives:
            lpoint_guids
                        [guid, ...]; a list of lpoint guids
        Returns:
            ordered_lpoint_specs
                        [lpoint_spec, ...], if successful
                        lpoint_spec:    (label, point_spec)
                        label:          str
                        point_spec:     (num, num, num)
            None        otherwise
        """
        lpoint_specs = []
        for lpoint_guid in lpoint_guids:
            lpoint_spec = self._get_spec_from_lpoint_guid(lpoint_guid)
            lpoint_specs.append(lpoint_spec)
        ordered_lpoint_specs = sorted(lpoint_specs)
        return ordered_lpoint_specs

    # def _get_shape_guids_from_rule_name(self, rule_name):   ##  05-02 10:17
        # """Receives:
        #     rule_name       str; the name of a rule; type and value guaranteed 
        #                     by the calling method
        # Returns:
        #     (   [guid, ...] the left shape guids (lines and text objects)
        #         [guid, ...] the right shape guids (lines and text objects)
        #     )               if successful       ##  shape names?
        #     None            otherwise
        # """
        # left_shape_name, right_shape_name = (
        #     self._get_shape_names_from_rule_name(rule_name))
        # left_shape_guids = self._get_guids_from_shape_name(
        #     left_shape_name)
        # right_shape_guids = self._get_guids_from_shape_name(
        #     right_shape_name)
        # return (left_shape_guids, right_shape_guids)

    # def _get_shape_names_from_rule_name(self, rule_name):
        # """Receives:
        #     rule_name       str; the name of a rule; type and value guaranteed
        #                     upstream
        # Returns:
        #     str             the name of the left shape
        #     str             the name of the right shape
        # """
        # left_shape_name = r.Rule._get_shape_name_from_rule_name(
        #     rule_name, 'left')
        # right_shape_name = r.Rule._get_shape_name_from_rule_name(
        #     rule_name, 'right')
        # return (left_shape_name, right_shape_name)

    # def _get_shape_spec_from_shape_guids(self, shape_guids):    ##  05-09 08:20
        # """Receives:
        #     shape_guids     [guid, ...]
        # Returns:
        #     shape_name      str
        #     line_specs      [((num, num, num), (num, num, num)), ...]. A list
        #                     of line specs
        #     lpoint_specs    [(str, (num, num, num)), ...]. A list of labeled 
        #                     point specs
        # """
        # return (shape_name, line_specs, lpoint_specs)

    # def _get_rule_spec_from_guids(
        # self, rule_name, left_shape_guids, right_shape_guids
    # ):                                          ##  04-23 09:05
        # """Receives:
        #     rule_name       str. The name of a rule
        #     left_shape_guids
        #                     [guid, ...]. The guids of the left shape
        #     right_shape_guids
        #                     [guid, ...]. The guids of the right shape
        # Returns:
        #     rule_name       str
        #     left_shape_spec ([line_spec, ...], [lpoint_spec, ...])
        #     right_shape_spec
        #                     ([line_spec, ...], [lpoint_spec, ...])
        # """
        
                                                ##  to do
    def _get_repr_from_rule_spec(self, rule_spec):
        """Receives:
            rule_spec: (rule_name, left_shape_spec, right_shape_spec)
                            rule_name: str
                            left_shape_spec:
                                ([line_spec, ...], [lpoint_spec, ...])
                            right_shape_spec:
                                ([line_spec, ...], [lpoint_spec, ...])
        Returns:
            str             the rule's repr, i.e., rul-format string
        """
        pass

    # def _get_rule(self):
        # """Returns:
        #     Rule            the SG object identified by the user
        # """
        # rule_name = self._get_selected_rule_name()
        # labeled_shape_names = (
        #     self._get_labeled_shape_names_from_rule_name(rule_name))
        # left_labeled_shape, right_labeled_shape = (
        #     self._get_labeled_shapes_from_labeled_shape_names(
        #         labeled_shape_names))
        # new_rule = rule.Rule.new(left_labeled_shape, right_labeled_shape)
        # return new_rule

    # def _get_selected_rule_name(self):          ##  03-03 08:15
        # """Prompts the user to select a rule name tag, if one is not already 
        # selected. Returns:
        #     str             the name of a rule
        # """
        # selected_objects = rs.SelectedObjects()
        # rule_name_tag = self._get_rule_name_tag_from(selected_objects)
        # if not rule_name_tag:
        #     message = "Please select the name tag of a rule"
        #     annotation_filter = 512
        #     rule_name_tag = rs.GetObject(message, annotation_filter)
        # rule_name = rs.TextObjectText(rule_name_tag)
        # return rule_name

    # def _get_rule_name_tag_from(self, objects): ##  03-13 10:21
        # """Extracts a rule name tag from a list of objects. Receives: 
        #     objects         [guid, ...]
        # Returns:
        #     guid            the guid of a rule name tag, if any
        #     None            otherwise
        # """
        # pass

    # def _get_labeled_shape_names_from_rule_name(self, rule_name):
        # """Gets the labeled shape names associated with the rule name. 
        # Receives:
        #     rule_name       str
        # Returns:
        #     (str, str)      the left and right labeled shape names
        # """
        # left_and_right_labeled_shape_names = 'shape_names'
        # return left_and_right_labeled_shape_names

    # def _get_labeled_shapes_from_labeled_shape_names(
    #     self, labeled_shape_names
    # ):
        # """Receives:
        #     labeled_shape_names
        #                     (str, str). The names of the left and right 
        #                     labeled shapes
        # Returns:
        #     [LabeledShape, LabeledShape]
        #                     the left and right labeled shapes
        # """
        # labeled_shapes = []
        # for name in labeled_shape_names:
        #     labeled_shape = self._get_labeled_shape_from_labeled_shape_name(
        #         name)
        #     labeled_shapes.append(labeled_shape)
        # return labeled_shapes

    ### Shared methods
    def _get_labeled_shape_from_labeled_shape_name(
        self, labeled_shape_name
    ):                                          ##  03-14 08:10
        """Receives:
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
            line_specs, lpoint_specs = (
                self._get_specs_from_labeled_shape_name(
                    labeled_shape_name))
            new_labeled_shape = ls.LabeledShape.new_from_specs(
                line_specs, lpoint_specs)            ##  trouble here
            return_value = new_labeled_shape
        finally:
            return return_value

    def _get_specs_from_labeled_shape_name(self, labeled_shape_name):
        """Gets the specs of a labeled shape. Receives:
            labeled_shape_name
                            str. Value confirmed by the calling method
        Returns:
            ([line_spec, ..], [labeled_point_spec, ...])
                            1. A list of line specs (point3d, point3d)
                            2. A list of labeled point specs: (point3d, str)
                            if successful
            None            otherwise
        """
        selected = True
        guids = rs.ObjectsByLayer(labeled_shape_name)
        line_guids, lpoint_guids = self._sort_guids(guids)
        line_specs = self._get_line_specs(line_guids)
        lpoint_specs = self._get_lpoint_specs(lpoint_guids)
        return (line_specs, lpoint_specs)

    def _sort_guids(self, guids):
        """Sorts guids by object type. Receives:
            guids           [guid, ...], n >= 0
        Returns:
            (line_guids, labeled_point_guids)
                            labeled_point_guids (textdot guids)
        """
        curve_type = 4
        textdot_type = 8192
        line_guids = self._extract_line_guids(guids)
        lpoint_guids = self._extract_lpoint_guids(guids)
        return (line_guids, lpoint_guids)

    def _extract_line_guids(self, guids):
        """Receives:
            [guid, ...]
        Returns:
            [guid, ...]     a list of line guids
        """
        line_guids = []
        for guid in guids:
            if rs.IsCurve(guid):
                line_guids.append(guid)
        return line_guids

    def _extract_lpoint_guids(self, guids):
        """Receives:
            [guid, ...]
        Returns:
            [guid, ...]     a list of lpoint guids
        """
        lpoint_guids = []
        for guid in guids:
            if rs.IsTextDot(guid):
                lpoint_guids.append(guid)
        return lpoint_guids

    def _get_line_specs(self, line_guids):
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
            for line_guid in line_guids:
                line_spec = self._get_spec_from_line_guid(line_guid)
                line_specs.append(line_spec)
            return_value = sorted(line_specs)
        finally:
            return return_value

    def _are_line_guids(self, guids):
        value = True
        for guid in guids:
            if not rs.IsLine(guid):
                value = False
                break
        return value

    def _get_spec_from_line_guid(self, line_guid):  ##  05-10 08:26
        """Receives:
            line_guid
        Returns:
            ((num, num, num), (num, num, num))
                            line spec
        """
        x1, y1, z1 = rs.CurveStartPoint(line_guid)
        x2, y2, z2 = rs.CurveEndPoint(line_guid)
        sg_p1 = point.Point(x1, y1, z1)
        sg_p2 = point.Point(x2, y2, z2)
        spec1 = sg_p1.spec
        spec2 = sg_p2.spec
        return (spec1, spec2)

    def _get_lpoint_specs(self, lpoint_guids):
        """Receives:
            lpoint_guids    [lpoint_guid, ...], n >= 0
        Returns:
            [lpoint_spec, ...], ordered
                            lpoint_spec: ((num, num, num), str), if 
                            successful
            None            otherwise
        """
        method_name = "_get_lpoint_specs"
        try:
            if not (
                type(lpoint_guids) == list and
                self._are_lpoint_guids(lpoint_guids)
            ):
                raise TypeError
        except TypeError:
            message = "The argument must be a list of labeled point guids"
            print("%s.%s:\n    %s" % (self.class_name, method_name, message))
            return_value = None
        else:
            lpoint_specs = []
            for lpoint_guid in lpoint_guids:
                lpoint_spec = self._get_lpoint_spec(lpoint_guid)
                lpoint_specs.append(lpoint_spec)
            return_value = sorted(lpoint_specs)
        finally:
            return return_value

    def _are_lpoint_guids(self, guids):
        value = True
        for guid in guids:
            if not rs.IsTextDot(guid):
                value = False
                break
        return value

    def _get_lpoint_spec(self, lpoint_guid):
        """Receives:
            lpoint_guid     textdot guid. Verified by calling method
        Returns:
            ((num, num, num), str)              ##  Note: SG spec: (x, y, str)
                            the labeled point spec
        """
        point = rs.TextDotPoint(lpoint_guid)
        point_spec = tuple(point)
        label = rs.TextDotText(lpoint_guid)
        return (point_spec, label)

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
