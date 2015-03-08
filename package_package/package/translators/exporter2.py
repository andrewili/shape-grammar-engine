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
        rule_name = self._get_rule_name()
        labeled_shape_names = (
            self._get_labeled_shape_names_from_rule_name(rule_name))
        left_labeled_shape, right_labeled_shape = (
            self._get_labeled_shapes_from_labeled_shape_names(
                labeled_shape_names))
        new_rule = rule.Rule.new(left_labeled_shape, right_labeled_shape)
        return new_rule

    def _get_rule_name(self):                   ##  03-03 08:15
        """Prompts the user to select a rule tag, if one is not already 
        selected. Returns:
            str             the name of a rule
        """
        rule_tag = rs.GetObject(filter='annotation')
        rule_name = rs.get_name_from_tag(rule_tag)
        return rule_name

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
    def _get_labeled_shape_from_labeled_shape_name(
        self, labeled_shape_name
    ):
        """Receives:
            labeled_shape_name
                            str
        Returns:
            LabeledShape    the SG labeled shape identified by the name
        """
        labeled_shape_elements = self._get_elements_from_labeled_shape_name(
            labeled_shape_name)
        new_labeled_shape = labeled_shape.LabeledShape.new_from_elements(
            labeled_shape_elements)
        return new_labeled_shape

    def _write_file(self, file_type, shape_name, string):   
                                                ##  03-06 10:59
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
        else:                                   ##  03-07 10:14
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
