from package.view import frame as f
from package.view import grammar as g
from package.view import rule as r
import rhinoscriptsyntax as rs
from package.tests import utilities as u

bad_type_rule_name = 37
bad_type_side = 37
bad_value_side = 'middle'
rule_name = 'subsequent_rule'
position = [0, 0, 0]
left_lshape_name = "%s_L" % rule_name
right_lshape_name = "%s_R" % rule_name
left_shape_position = [0, 0, 0]

def test_add_first():
    method_name = 'add_first'

    def try_bad_state_first_rule_exists():
        try_name = 'bad_state_first_rule_exists'
        _set_up()
        g.Grammar.add_to_initial_shapes(r.Rule.first_rule_name)
        actual_value = r.Rule.add_first()
        expected_value = None
        if not actual_value == expected_value:
            u.Utilities.print_test_error_message(
                method_name, try_name, expected_value, actual_value)

    def try_good_state():
        try_name = 'good_state'
        _set_up()
        actual_value = r.Rule.add_first()
        expected_value = r.Rule.first_rule_name
        if not actual_value == expected_value:
            u.Utilities.print_test_error_message(
                method_name, try_name, expected_value, actual_value)

    try_bad_state_first_rule_exists()
    try_good_state()

def test_add_subsequent():
    def try_good_state_existing_name():
        try_name = 'good_state_existing_name'
        _set_up()
        r.Rule.add_first()
        good_name = 'good_name'
        message = "Enter: 1, '%s'; 2, '%s'; 3, '%s'" % (
            'kil#roy', r.Rule.first_rule_name, good_name)
        print(message)
        actual_value = r.Rule.add_subsequent()
        expected_value = good_name
        if not actual_value == expected_value:
            u.Utilities.print_test_error_message(
                method_name, try_name, expected_value, actual_value)

    method_name = 'add_subsequent'
    try_good_state_existing_name()

def test_get_def_from_rule():
    def try_good_arg():
        try_name = 'good_arg'
        g.Grammar.clear_all()
        name = 'kilroy'
        actual_value = r.Rule.get_def_from_rule(name)
        expected_value = "rule    %s    %s_L -> %s_R" % (name, name, name)
        if not actual_value == expected_value:
            u.Utilities.print_test_error_message(
                method_name, try_name, expected_value, actual_value)

    method_name = 'get_def_from_rule'
    try_good_arg()

def test_get_lshape_pair_from_rule():
    def try_good_arg():
        try_name = 'good_arg'
        good_rule = 'good_rule'
        left_lshape_name = "%s%s" % (good_rule, r.Rule.left_lshape_suffix)
        right_lshape_name = "%s%s" % (good_rule, r.Rule.right_lshape_suffix)
        actual_value = r.Rule.get_lshape_pair_from_rule(good_rule)
        expected_value = (left_lshape_name, right_lshape_name)
        if not actual_value == expected_value:
            u.Utilities.print_test_error_message(
                method_name, try_name, expected_value, actual_value)

    method_name = 'get_lshape_pair_from_rule'
    try_good_arg()

def test__get_shape_name_from_rule_name():
    method_name = '_get_shape_name_from_rule_name'

    def try_bad_type_side():
        try_name = 'bad_type_side'
        actual_value = r.Rule._get_shape_name_from_rule_name(
            rule_name, bad_type_side)
        expected_value = None
        if not actual_value == expected_value:
            g.Grammar.print_test_error_message(
                method_name, try_name, expected_value, actual_value)

    def try_bad_value_side():
        try_name = 'bad_value_side'
        actual_value = r.Rule._get_shape_name_from_rule_name(
            rule_name, bad_value_side)
        expected_value = None
        if not actual_value == expected_value:
            g.Grammar.print_test_error_message(
                method_name, try_name, expected_value, actual_value)

    def try_good_args():
        try_name = 'good_args'
        actual_value = r.Rule._get_shape_name_from_rule_name(
            rule_name, 'left')
        expected_value = "%s_L" % rule_name
        if not actual_value == expected_value:
            g.Grammar.print_test_error_message(
                method_name, try_name, expected_value, actual_value)

    try_bad_type_side()
    try_bad_value_side()
    try_good_args()

def test__get_right_shape_position():
    method_name = '_get_right_shape_position'

    def try_good_args():
        try_name = 'good_args'
        actual_value = r.Rule._get_right_shape_position(left_shape_position)
        expected_value = rs.Str2Pt("48,0,0")
        if not actual_value == expected_value:
            g.Grammar.print_test_error_message(
                method_name, try_name, expected_value, actual_value)

    try_good_args()

def _set_up():
    g.Grammar.clear_all()
    f.Frame.new()

# test_add_first()
# test_add_subsequent()

# done
test_get_def_from_rule()
# test_get_lshape_pair_from_rule()
# test__get_shape_name_from_rule_name()
# test__get_right_shape_position()

# def test__record():
    # def try_bad_type():
    #     try_name = 'bad_type'
    #     actual_value = r.Rule._record(
    #         bad_type_rule_name, left_lshape_name, right_lshape_name)
    #     expected_value = None
    #     if not actual_value == expected_value:
    #         g.Grammar.print_test_error_message(
    #             method_name, try_name, expected_value, actual_value)

    # def try_good_args():
    #     try_name = 'good_args'
    #     actual_value = r.Rule._record(
    #         rule_name, left_lshape_name, right_lshape_name)
    #     expected_value = "%s %s" % (left_lshape_name, right_lshape_name)
    #     if not actual_value == expected_value:
    #         g.Grammar.print_test_error_message(
    #             method_name, try_name, expected_value, actual_value)

    # method_name = '_record'
    # try_bad_type()
    # try_good_args()

# def test__new():
    # method_name = '_new'

    # def try_good_args():
    #     try_name = 'good_args'
    #     g.Grammar.clear_all()
    #     f.Frame.new()
    #     actual_value = r.Rule._new(rule_name, position)
    #     expected_value = rule_name
    #     if not actual_value == expected_value:
    #         g.Grammar.print_test_error_message(
    #             method_name, try_name, expected_value, actual_value)

    # try_good_args()

# test__record()
# test__new()
