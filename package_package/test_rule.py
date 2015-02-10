from package.model import frame_block as fb
from package.model import grammar as g
from package.model import llist as ll
from package.model import rule as r
import rhinoscriptsyntax as rs

bad_type_rule_name = 37
bad_type_side = 37
bad_value_side = 'middle'
rule_name = 'rule_i'
position = [0, 0, 0]
left_shape_name = "%s_L" % rule_name
right_shape_name = "%s_R" % rule_name
left_shape_position = [0, 0, 0]

def test__record_rule():
    method_name = '_record_rule'

    def try_bad_type():
        try_name = 'bad_type'
        actual_value = r.Rule._record_rule(
            bad_type_rule_name, left_shape_name, right_shape_name)
        expected_value = None
        if not actual_value == expected_value:
            g.Grammar.print_test_error_message(
                method_name, try_name, expected_value, actual_value)

    def try_good_args():
        try_name = 'good_args'
        actual_value = r.Rule._record_rule(
            rule_name, left_shape_name, right_shape_name)
        expected_value = "%s %s" % (left_shape_name, right_shape_name)
        if not actual_value == expected_value:
            g.Grammar.print_test_error_message(
                method_name, try_name, expected_value, actual_value)

    try_bad_type()
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

def test__new():
    method_name = '_new'

    def try_good_args():
        try_name = 'good_args'
        g.Grammar.clear_all()
        fb.FrameBlock.new()
        actual_value = r.Rule._new(rule_name, position)
        expected_value = rule_name
        if not actual_value == expected_value:
            g.Grammar.print_test_error_message(
                method_name, try_name, expected_value, actual_value)

    try_good_args()

def test__rule_name_is_available():
    method_name = '_rule_name_is_available'

    def try_false():
        try_name = 'false'
        g.Grammar.clear_all()
        ll.Llist.set_entry(r.Rule.rule_name_list_name, r.Rule.first_rule_name)
        actual_value = r.Rule._rule_name_is_available(r.Rule.first_rule_name)
        expected_value = False
        if not actual_value == expected_value:
            g.Grammar.print_test_error_message(
                method_name, try_name, expected_value, actual_value)

    def try_true():
        try_name = 'true'
        g.Grammar.clear_all()
        actual_value = r.Rule._rule_name_is_available(r.Rule.first_rule_name)
        expected_value = True
        if not actual_value == expected_value:
            g.Grammar.print_test_error_message(
                method_name, try_name, expected_value, actual_value)

    try_false()
    try_true()

def test_add_subsequent():
    method_name = 'add_subsequent'
    
    def try_good_state():
        try_name = 'good_state'
        g.Grammar.clear_all()
        fb.FrameBlock.new()
        actual_value = r.Rule.add_subsequent()
        expected_value = rule_name
        if not actual_value == expected_value:
            g.Grammar.print_test_error_message(
                method_name, try_name, expected_value, actual_value)

    try_good_state()
    
def test_add_first():
    method_name = 'add_first'

    def try_bad_state():
        try_name = 'bad_state'
        g.Grammar.clear_all()
        fb.FrameBlock.new()
        r.Rule._new(r.Rule.first_rule_name, position)
        actual_value = r.Rule.add_first()
        expected_value = None
        if not actual_value == expected_value:
            g.Grammar.print_test_error_message(
                method_name, try_name, expected_value, actual_value)

    def try_good_state():
        try_name = 'good_state'
        g.Grammar.clear_all()
        fb.FrameBlock.new()
        actual_value = r.Rule.add_first()
        expected_value = r.Rule.first_rule_name
        if not actual_value == expected_value:
            g.Grammar.print_test_error_message(
                method_name, try_name, expected_value, actual_value)

    try_bad_state()
    try_good_state()

test__record_rule()
test__get_right_shape_position()
test__get_shape_name_from_rule_name()
test__new()
test__rule_name_is_available()
test_add_subsequent()
test_add_first()
