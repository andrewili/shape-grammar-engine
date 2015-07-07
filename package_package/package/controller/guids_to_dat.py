import rhinoscriptsyntax as rs

class GuidToDat(object):
    dat_header = "%s\n%s" % (
        "# shape data version 6.00",
        "unit  mm  # mm - millimetre, cm - centimetre, m - metre")
    blank_line = ''
    spacer = '    '

    def __init__(self):
        pass

    @classmethod                                ##  07-07 07:59
    def get_dat_string(cls):
        """The dat string consists of: 
            header
            ordered_labeled_shapes_string
            ordered_initial_shapes_string
            ordered_rules_string
        Returns:
            dat_string      str. The grammar's dat string, if successful
            None            otherwise
        """
        layer_names = rs.LayerNames()
        initial_shape_layer_names, rule_layer_names = (
            cls._separate_layer_names(layer_names))
                                                ##  kilroy was here
        ordered_labeled_shapes_string = (
            cls._get_ordered_labeled_shapes_string(
                initial_shape_layer_names, rule_layer_names))
        ordered_initial_shapes_string = (
            cls._get_ordered_initial_shapes_string(
                initial_shape_layer_names))
        ordered_rules_string = (
            cls._get_ordered_rules_string(rule_layer_names))
        dat_string = '\n'.join([
            cls.dat_header,
            ordered_labeled_shapes_string,
            cls.blank_line,
            ordered_initial_shapes_string,
            ordered_rules_string])
        return_value = dat_string
        return return_value

    @classmethod
    def _separate_layer_names(cls, layer_names):
        """Receives:
            layer_names     [str, ...]. A list of layer names
        Returns:
            initial_shape_layer_names
                            [str, ...]. A list of initial shape layer names
            rule_layer_names
                            [str, ...]. A list of rule layer names
        """
        initial_shape_layer_names = []
        rule_layer_names = []
        for layer_name in layer_names:
            if l.Layer._contains_initial_shape(layer_name):
                initial_shape_layer_names.append(layer_name)
            elif l.Layer._contains_rule(layer_name):
                rule_layer_names.append(layer_name)
            else:
                pass
        return (initial_shape_layer_names, rule_layer_names)

    @classmethod                                ##  07-06 10:27
    def _get_ordered_labeled_shapes_string(
        cls, initial_shape_layer_names, rule_layer_names
    ):
        """Receives:
            initial_shape_layer_names
                            [str, ...]. A list of initial shape layer names
            rule_layer_names
                            [str, ...]. A list of rule layer names
        Returns:
            ordered_labeled_shapes_string
                            str: str\nstr\n...\nstr. The string form of 
                            [str, ...], an ordered list (by shape name) of 
                            .is strings of labeled shapes from both initial 
                            shapes and rules
        """
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

        # labeled_shape_strings = []
        # for layer_name in layer_names:          ##  skip user layers
        #     if l.Layer.is_initial_shape(layer_name):
        #         initial_labeled_shape_string = (
        #             l.Layer._get_initial_labeled_shape_string(layer_name))
        #                                         ##  kilroy is here
        #         labeled_shape_strings.append(initial_labeled_shape_string)
        #     elif l.Layer.is_rule(layer_name):
        #         left_labeled_shape_string, right_labeled_shape_string = (
        #             l.Layer._get_rule_labeled_shape_strings(layer_name))
        #         labeled_shape_strings.append(left_labeled_shape_string)
        #         labeled_shape_strings.append(right_labeled_shape_string)
        #     else:
        #         pass
        # ordered_labeled_shape_strings = sorted(labeled_shape_strings)
        # ordered_labeled_shapes_string = '\n'.join(
        #     ordered_labeled_shape_strings)
        # return ordered_labeled_shapes_string

    @classmethod
    def _get_ordered_initial_shapes_string(cls, layer_names):
        """Receives:
            layer_names     [str, ...]. A list of layer names
        Returns:
            ordered_initial_shapes_string
                            str\nstr\n...\nstr. The joined string of an 
                            ordered list of initial shape strings
        """
        return ordered_initial_shapes_string

    @classmethod
    def _get_ordered_rules_string(cls, layer_names):
        """Receives:
            layer_names     [str, ...]. A list of layer names
        Returns:
            ordered_rules_string
                            str\nstr\n...\nstr. The joined string of an 
                            ordered list of rule strings
        """
        return ordered_rules_string

    # @classmethod
    # def _get_labeled_shape_names(cls):          ##  07-07 08:04
        # """Returns:
        #     names           [str, ...]. An ordered name list of labeled shapes 
        #                     in both initial shapes and rules, if successful
        #     None            otherwise
        # """
        # method_name = '_get_labeled_shape_names'
        # try:
        #     if not (
        #         cls._layers_include_one_initial_shape_and_one_rule()
        #     ):
        #         raise Error
        # except Error:
        #     message = 'message'
        #     print('%s.%s:\n%s' % (cls.__name__, method_name, message))
        #     return_value = None
        # else:
        #     return_value = ordered_labeled_shape_names
        # finally:
        #     return return_value
        
    # @classmethod                                ##  07-07 08:06
    # def _layers_include_one_initial_shape_and_one_rule(cls):
        # """Returns:
        #     value           boolean. True or False
        # """
        # layer_names = cls._get_layer_names()
        
        # value = (
        #     cls._there_is_at_least_one_initial_shape() and 
        #     cls._there_is_at_least_one_rule())
        # return value
        
    # @classmethod
    # def _there_is_at_least_one_rule(cls):
        # """Returns:
        #     value           boolean. True or False
        # """
        # return value

