from package.view import grammar as g
from package.controller import guids_to_dat as gd
from package.tests import utilities as u

def test_get_dat_string():
	method_name = 'get_dat_string'

def test__get_ordered_labeled_shape_names():
    def try_bad_state_0_initial_shapes_0_rules():
        try_name = 'bad_state_0_initial_shapes_0_rules'
        u.Utilities.make_grammar_0_initial_shapes_0_rules()
        actual_value = gd.GuidsToDat._get_ordered_labeled_shape_names()
        expected_value = None
        if not actual_value == expected_value:
            u.Utilities.print_test_error_message(
                method_name, try_name, expected_value, actual_value)

    def try_bad_state_0_initial_shapes_3_rules():
        try_name = 'bad_state_no_initial_shapes_rules'
        u.Utilities.make_grammar_0_initial_shapes_3_rules()
        actual_value = gd.GuidsToDat._get_ordered_labeled_shape_names()
        expected_value = None
        if not actual_value == expected_value:
            u.Utilities.print_test_error_message(
                method_name, try_name, expected_value, actual_value)

    def try_bad_state_3_initial_shapes_0_rules():
        try_name = 'bad_state_initial_shapes_no_rules'
        u.Utilities.make_grammar_3_initial_shapes_0_rules()
        actual_value = gd.GuidsToDat._get_ordered_labeled_shape_names()
        expected_value = None
        if not actual_value == expected_value:
            u.Utilities.print_test_error_message(
                method_name, try_name, expected_value, actual_value)

    def try_good_state_3_initial_shapes_3_rules():
        try_name = 'good_state_initial_shapes_rules'
        u.Utilities.make_grammar_3_initial_shapes_3_rules()
        actual_value = gd.GuidsToDat._get_ordered_labeled_shape_names()
        expected_value = 'kilroy'
        if not actual_value == expected_value:
            u.Utilities.print_test_error_message(
                method_name, try_name, expected_value, actual_value)

    method_name = '_get_ordered_labeled_shape_names'
    try_bad_state_0_initial_shapes_0_rules()
    try_bad_state_0_initial_shapes_3_rules()
    try_bad_state_3_initial_shapes_0_rules()
    try_good_state_3_initial_shapes_3_rules()

def test__get_ordered_labeled_shapes_string():
    def try_no_ishapes_no_rules():
        try_name = 'no_ishapes_no_rules'
        g.Grammar.clear_all()
        f.Frame._new_definition()
        actual_value = g.Grammar._get_ordered_labeled_shapes_string()
        expected_value = ''
        if not actual_value == expected_value:
            u.Utilities.print_test_error_message(
                method_name, try_name, expected_value, actual_value)

    def try_no_ishapes_rules():
        try_name = 'no_ishapes_rules'
        pass

    def try_ishapes_no_rules():
        try_name = 'ishapes_no_rules'
        pass

    def try_ishapes_rules():
        try_name = 'ishapes_rules'
        pass

    method_name = '_get_ordered_labeled_shapes_string'
    try_no_ishapes_no_rules()
    # try_no_ishapes_rules()
    # try_ishapes_no_rules()
    # try_ishapes_rules()

def test__get_ordered_initial_shape_defs_string():
    def try_good_state_no_ishapes_no_rules():
        try_name = 'good_state_no_ishapes_no_rules'
        _set_up()
        actual_value = g.Grammar._get_ordered_named_initial_shape_defs_string()
        expected_value = ''
        # if actual_value == expected_value:
        if not actual_value == expected_value:
            u.Utilities.print_test_error_message(
                method_name, try_name, expected_value, actual_value)

    def try_good_state_no_ishapes_rules():
        try_name = 'good_state_no_ishapes_rules'
        _make_new_grammar_3_rules()
        actual_value = g.Grammar._get_ordered_named_initial_shape_defs_string()
        expected_value = ''
        if not actual_value == expected_value:
            u.Utilities.print_test_error_message(
                method_name, try_name, expected_value, actual_value)

    def try_good_state_ishapes_no_rules():
        try_name = 'good_state_ishapes_no_rules'
        _make_new_grammar_3_ishapes()
        name_1, name_2, name_3 = 'a_ishape', 'initial_shape_1', 'z_ishape'
        actual_value = g.Grammar._get_ordered_named_initial_shape_defs_string()
        expected_value = "%s\n%s\n%s" % (
            "shape    %s" % (name_1),
            "shape    %s" % (name_2),
            "shape    %s" % (name_3))
        if not actual_value == expected_value:
            u.Utilities.print_test_error_message(
                method_name, try_name, expected_value, actual_value)

    def try_good_state_ishapes_rules():
        try_name = 'good_state_ishapes_rules'
        _make_new_grammar_3_ishapes_3_rules()
        name_1, name_2, name_3 = 'a_ishape', 'initial_shape_1', 'z_ishape'
        actual_value = g.Grammar._get_ordered_named_initial_shape_defs_string()
        expected_value = "%s\n%s\n%s" % (
            "shape    %s" % (name_1),
            "shape    %s" % (name_2),
            "shape    %s" % (name_3))
        if not actual_value == expected_value:
            u.Utilities.print_test_error_message(
                method_name, try_name, expected_value, actual_value)

    method_name = '_get_ordered_named_initial_shape_defs_string'
    try_good_state_no_ishapes_no_rules()
    try_good_state_no_ishapes_rules()
    try_good_state_ishapes_no_rules()
    try_good_state_ishapes_rules()

def test__get_ordered_rule_defs_string():
    def try_good_state_no_ishapes_no_rules():
        try_name = 'good_state_no_ishapes_no_rules'
        _set_up()
        actual_value = g.Grammar._get_ordered_named_rule_defs_string()
        expected_value = ''
        if not actual_value == expected_value:
            u.Utilities.print_test_error_message(
                method_name, try_name, expected_value, actual_value)

    def try_good_state_no_ishapes_rules():
        try_name = 'good_state_no_ishapes_rules'
        _make_new_grammar_3_rules()
        name_1, name_2, name_3 = 'a_rule', 'rule_1', 'z_rule'
        actual_value = g.Grammar._get_ordered_named_rule_defs_string()
        expected_value = "%s\n%s\n%s" % (
            "rule    %s    %s_L -> %s_R" % (name_1, name_1, name_1),
            "rule    %s    %s_L -> %s_R" % (name_2, name_2, name_2),
            "rule    %s    %s_L -> %s_R" % (name_3, name_3, name_3))
        if not actual_value == expected_value:
            u.Utilities.print_test_error_message(
                method_name, try_name, expected_value, actual_value)

    def try_good_state_ishapes_no_rules():
        try_name = 'good_state_ishapes_no_rules'
        _make_new_grammar_3_ishapes()
        actual_value = g.Grammar._get_ordered_named_rule_defs_string()
        expected_value = ''
        if not actual_value == expected_value:
            u.Utilities.print_test_error_message(
                method_name, try_name, expected_value, actual_value)

    def try_good_state_ishapes_rules():
        try_name = 'good_state_ishapes_rules'
        _make_new_grammar_3_ishapes_3_rules()
        name_1, name_2, name_3 = 'a_rule', 'rule_1', 'z_rule'
        actual_value = g.Grammar._get_ordered_named_rule_defs_string()
        expected_value = "%s\n%s\n%s" % (
                    "rule    %s    %s_L -> %s_R" % (name_1, name_1, name_1),
                    "rule    %s    %s_L -> %s_R" % (name_2, name_2, name_2),
                    "rule    %s    %s_L -> %s_R" % (name_3, name_3, name_3))
        if not actual_value == expected_value:
            u.Utilities.print_test_error_message(
                method_name, try_name, expected_value, actual_value)

    method_name = '_get_ordered_named_rule_defs_string'
    try_good_state_no_ishapes_no_rules()
    try_good_state_no_ishapes_rules()
    try_good_state_ishapes_no_rules()
    try_good_state_ishapes_rules()

# test_get_dat_string()
test__get_ordered_labeled_shape_names()

# test__get_ordered_labeled_shapes_string()
# test__get_ordered_initial_shape_defs_string()
# test__get_ordered_rule_defs_string()
