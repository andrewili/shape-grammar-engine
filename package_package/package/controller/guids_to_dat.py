import rhinoscriptsyntax as rs

class GuidsToDat(object):
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
        The grammar is guaranteed to be well-formed. Returns:
            dat_string      str. The grammar's dat string, if successful
            None            otherwise


        """
        labeled_shape_layer_names = g.Grammar.get_labeled_shape_layer_names()
                            ##  [name, ...]
        if not one_initial_shape_and_one_rule:
            trouble
        labeled_shape_name_dat_dict = cls._make_lshape_name_dat_dict(
            labeled_shape_layer_names)
                            ##  {lshape_name: (
                            ##      [point_coord, ...], 
                            ##      [codex_codex, ...], 
                            ##      [codex_label, ...])}
        ordered_labeled_shapes_string = (
            cls._get_ordered_labeled_shapes_string(
                labeled_shape_name_dat_dict))
                            ##  'lshape_string\n...'
        ordered_initial_shapes_string = (
            cls._get_ordered_initial_shapes_string(
                labeled_shape_name_dat_dict))
                            ##  'initial    name\n...'
        ordered_rules_string = (
            cls._get_ordered_rules_string(labeled_shape_name_dat_dict))
                            ##  'rule    name    name_L -> name_R\n...'
        dat_string = '\n'.join([
            cls.dat_header,
            ordered_labeled_shapes_string,
            cls.blank_line,
            ordered_initial_shapes_string,
            ordered_rules_string])
        return_value = dat_string
        return return_value

    # @classmethod
    # def _separate_layer_names(cls, layer_names):
        # """Receives:
        #     layer_names     [str, ...]. A list of layer names
        # Returns:
        #     initial_shape_layer_names
        #                     [str, ...]. A list of initial shape layer names
        #     rule_layer_names
        #                     [str, ...]. A list of rule layer names
        # """
        # initial_shape_layer_names = []
        # rule_layer_names = []
        # for layer_name in layer_names:
        #     if l.Layer.contains_initial_shape(layer_name):
        #         initial_shape_layer_names.append(layer_name)
        #     elif l.Layer.contains_rule(layer_name):
        #         rule_layer_names.append(layer_name)
        #     else:
        #         pass
        # return (initial_shape_layer_names, rule_layer_names)

    @classmethod
    def _get_ordered_labeled_shapes_string(
        cls, labeled_shape_name_dat_dict
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
    def _get_ordered_initial_shapes_string(cls, labeled_shape_name_dat_dict):
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
    def _get_ordered_rules_string(cls, labeled_shape_name_dat_dict):
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

