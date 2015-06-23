from package.view import container as c
from package.view import frame as f
from package.view import grammar as g
from package.view import initial_shape as ish
from package.view import rule as r
import rhinoscriptsyntax as rs
from package.view import settings as s
from package.tests import utilities as u

def test_new():
    method_name = 'new'
    g.Grammar.clear_all()
    g.Grammar.new()

def test__set_up_first_initial_shape():
    def try_bad_state_layer_exists():
        try_name = 'bad_state_layer_exists'
        g.Grammar.clear_all()
        rs.AddLayer(s.Settings.first_initial_shape_layer_name)
        actual_value = g.Grammar._set_up_first_initial_shape()
        expected_value = None
        if not actual_value == expected_value:
            u.Utilities.print_test_error_message(
                method_name, try_name, expected_value, actual_value)
        
    def try_good_state():
        try_name = 'good_state'
        g.Grammar.clear_all()
        actual_value = g.Grammar._set_up_first_initial_shape()
        expected_value = s.Settings.first_initial_shape_layer_name
        if not actual_value == expected_value:
            u.Utilities.print_test_error_message(
                method_name, try_name, expected_value, actual_value)
        
    method_name = '_set_up_first_initial_shape'
    try_bad_state_layer_exists()
    try_good_state()

def test__set_up_subsequent_initial_shape():
    def try_good_state():
        try_name = 'good_state'
        g.Grammar.clear_all()
        existing_name = 'abe'
        rs.AddLayer(existing_name)
        ill_formed_name = 'bob#'
        good_name = 'cal'
        print("Enter: 1, '%s'; 2, '%s'; 3, '%s'" % (
            existing_name, ill_formed_name, good_name))
        actual_value = g.Grammar._set_up_subsequent_initial_shape()
        expected_value = good_name
        if not actual_value == expected_value:
            u.Utilities.print_test_error_message(
                method_name, try_name, expected_value, actual_value)

    method_name = '_set_up_subsequent_initial_shape'
    try_good_state()

def test__set_up_initial_shape():
    def try_good_state():
        try_name = 'good_state'
        g.Grammar.clear_all()
        good_name = 'sam'
        origin = (20, 20, 0)
        actual_value = g.Grammar._set_up_initial_shape(good_name, origin)
        expected_value = good_name
        if not actual_value == expected_value:
            u.Utilities.print_test_error_message(
                method_name, try_name, expected_value, actual_value)

    method_name = '_set_up_initial_shape'
    try_good_state()

def test__set_up_first_rule():
    def try_bad_state_layer_exists():
        try_name = 'bad_state_layer_exists'
        g.Grammar.clear_all()
        rs.AddLayer(s.Settings.first_rule_layer_name)
        actual_value = g.Grammar._set_up_first_rule()
        expected_value = None
        if not actual_value == expected_value:
            u.Utilities.print_test_error_message(
                method_name, try_name, expected_value, actual_value)

    def try_good_state():
        try_name = 'good_state'
        g.Grammar.clear_all()
        actual_value = g.Grammar._set_up_first_rule()
        expected_value = s.Settings.first_rule_layer_name
        if not actual_value == expected_value:
            u.Utilities.print_test_error_message(
                method_name, try_name, expected_value, actual_value)

    method_name = '_set_up_first_rule'
    try_bad_state_layer_exists()
    try_good_state()

def test__set_up_subsequent_rule():
    def try_good_state():
        try_name = 'good_state'
        g.Grammar.clear_all()
        existing_name = 'abe'
        rs.AddLayer(existing_name)
        ill_formed_name = 'bob#'
        good_name = 'cal'
        print("Enter: 1, '%s'; 2, '%s'; 3, '%s'" % (
            existing_name, ill_formed_name, good_name))
        actual_value = g.Grammar._set_up_subsequent_rule()
        expected_value = good_name
        if not actual_value == expected_value:
            u.Utilities.print_test_error_message(
                method_name, try_name, expected_value, actual_value)

    method_name = '_set_up_subsequent_rule'
    try_good_state()

def test__set_up_rule():
    def try_good_state():
        try_name = 'good_state'
        g.Grammar.clear_all()
        good_name = 'good_name'
        origin = (20, 20, 0)
        actual_value = g.Grammar._set_up_rule(good_name, origin)
        expected_value = good_name
        if not actual_value == expected_value:
            u.Utilities.print_test_error_message(
                method_name, try_name, expected_value, actual_value)

    method_name = '_set_up_rule'
    try_good_state()

####

def test_export():
    pass

def test_get_name():
    def try_good_state():
        try_name = 'good_state'
        actual_value = g.Grammar.get_name()
        expected_value = ''
        if not actual_value == expected_value:
            u.Utilities.print_test_error_message(
                method_name, try_name, expected_value, actual_value)

    method_name = 'get_name'
    try_good_state()

# def test_get_dat_string():
    # pass

def test__get_ordered_named_lshapes_string():
    def try_no_ishapes_no_rules():
        try_name = 'no_ishapes_no_rules'
        pass

    def try_no_ishapes_rules():
        try_name = 'no_ishapes_rules'
        pass

    def try_ishapes_no_rules():
        try_name = 'ishapes_no_rules'
        pass

    def try_ishapes_rules():
        try_name = 'ishapes_rules'
        pass

    method_name = '_get_ordered_named_lshapes_string'
    try_no_ishapes_no_rules()
    try_no_ishapes_rules()
    try_ishapes_no_rules()
    try_ishapes_rules()

def test__get_ordered_named_ishape_defs_string():
    def try_good_state_no_ishapes_no_rules():
        try_name = 'good_state_no_ishapes_no_rules'
        _set_up()
        actual_value = g.Grammar._get_ordered_named_ishape_defs_string()
        expected_value = ''
        # if actual_value == expected_value:
        if not actual_value == expected_value:
            u.Utilities.print_test_error_message(
                method_name, try_name, expected_value, actual_value)

    def try_good_state_no_ishapes_rules():
        try_name = 'good_state_no_ishapes_rules'
        _make_new_grammar_3_rules()
        actual_value = g.Grammar._get_ordered_named_ishape_defs_string()
        expected_value = ''
        if not actual_value == expected_value:
            u.Utilities.print_test_error_message(
                method_name, try_name, expected_value, actual_value)

    def try_good_state_ishapes_no_rules():
        try_name = 'good_state_ishapes_no_rules'
        _make_new_grammar_3_ishapes()
        name_1, name_2, name_3 = 'a_ishape', 'initial_shape_1', 'z_ishape'
        actual_value = g.Grammar._get_ordered_named_ishape_defs_string()
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
        actual_value = g.Grammar._get_ordered_named_ishape_defs_string()
        expected_value = "%s\n%s\n%s" % (
            "shape    %s" % (name_1),
            "shape    %s" % (name_2),
            "shape    %s" % (name_3))
        if not actual_value == expected_value:
            u.Utilities.print_test_error_message(
                method_name, try_name, expected_value, actual_value)

    method_name = '_get_ordered_named_ishape_defs_string'
    try_good_state_no_ishapes_no_rules()
    try_good_state_no_ishapes_rules()
    try_good_state_ishapes_no_rules()
    try_good_state_ishapes_rules()

def test__get_ordered_named_rule_defs_string():
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

def test_get_initial_shapes():
    def try_good_state_no_ishapes_no_rules():
        try_name = 'good_state_no_ishapes_no_rules'
        _set_up()
        actual_value = g.Grammar.get_initial_shapes()
        expected_value = []
        if not actual_value == expected_value:
            u.Utilities.print_test_error_message(
                method_name, try_name, expected_value, actual_value)

    def try_good_state_ishapes_no_rules():
        try_name = 'good_state_ishapes_no_rules'
        _make_new_grammar_3_ishapes()
        actual_value = g.Grammar.get_initial_shapes()
        expected_value = [
            'a_ishape', ish.InitialShape.first_initial_shape_name, 'z_ishape']
        if not actual_value == expected_value:
            u.Utilities.print_test_error_message(
                method_name, try_name, expected_value, actual_value)

    def try_good_state_no_ishapes_rules():
        try_name = 'good_state_no_ishapes_rules'
        _make_new_grammar_3_rules()
        actual_value = g.Grammar.get_initial_shapes()
        expected_value = []
        if not actual_value == expected_value:
            u.Utilities.print_test_error_message(
                method_name, try_name, expected_value, actual_value)

    def try_good_state_ishapes_rules():
        try_name = 'good_state_ishapes_rules'
        _make_new_grammar_3_ishapes_3_rules()
        actual_value = g.Grammar.get_initial_shapes()
        expected_value = [
            'a_ishape', ish.InitialShape.first_initial_shape_name, 'z_ishape']
        if not actual_value == expected_value:
            u.Utilities.print_test_error_message(
                method_name, try_name, expected_value, actual_value)

    method_name = 'get_initial_shapes'
    try_good_state_no_ishapes_no_rules()
    try_good_state_ishapes_no_rules()
    try_good_state_no_ishapes_rules()
    try_good_state_ishapes_rules()

def test_get_rule_shapes():
    def try_good_args_no_rules():
        try_name = 'good_args_no_rules'
        g.Grammar.clear_all()
        actual_value = g.Grammar.get_rule_shapes()
        expected_value = []
        if not actual_value == expected_value:
            u.Utilities.print_test_error_message(
                method_name, try_name, expected_value, actual_value)

    def try_good_args():
        try_name = 'good_args'
        _make_new_grammar_3_ishapes_3_rules()
        actual_value = g.Grammar.get_rule_shapes()
        expected_value = sorted([
            "%s%s" % (r.Rule.first_rule_name, r.Rule.left_lshape_suffix),
            "%s%s" % (r.Rule.first_rule_name, r.Rule.right_lshape_suffix),
            "%s%s" % ('a_rule', r.Rule.left_lshape_suffix),
            "%s%s" % ('a_rule', r.Rule.right_lshape_suffix),
            "%s%s" % ('z_rule', r.Rule.left_lshape_suffix),
            "%s%s" % ('z_rule', r.Rule.right_lshape_suffix)])
        if not actual_value == expected_value:
            u.Utilities.print_test_error_message(
                method_name, try_name, expected_value, actual_value)

    method_name = 'get_rule_shapes'
    try_good_args_no_rules()
    try_good_args()

def test_get_rules():
    def try_good_state_no_ishapes_no_rules():
        try_name = 'good_state_no_ishapes_no_rules'
        _set_up()
        actual_value = g.Grammar.get_rules()
        expected_value = []
        if not actual_value == expected_value:
            u.Utilities.print_test_error_message(
                method_name, try_name, expected_value, actual_value)

    def try_good_state_ishapes_no_rules():
        try_name = 'good_state_ishapes_no_rules'
        _make_new_grammar_3_ishapes()
        actual_value = g.Grammar.get_rules()
        expected_value = []
        if not actual_value == expected_value:
            u.Utilities.print_test_error_message(
                method_name, try_name, expected_value, actual_value)

    def try_good_state_no_ishapes_rules():
        try_name = 'good_state_no_ishapes_rules'
        _make_new_grammar_3_rules()
        actual_value = g.Grammar.get_rules()
        expected_value = [
            'a_rule', r.Rule.first_rule_name, 'z_rule']
        if not actual_value == expected_value:
            u.Utilities.print_test_error_message(
                method_name, try_name, expected_value, actual_value)

    def try_good_state_ishapes_rules():
        try_name = 'good_state_ishapes_rules'
        _make_new_grammar_3_ishapes_3_rules()
        actual_value = g.Grammar.get_rules()
        expected_value = [
            'a_rule', r.Rule.first_rule_name, 'z_rule']
        if not actual_value == expected_value:
            u.Utilities.print_test_error_message(
                method_name, try_name, expected_value, actual_value)
    
    method_name = 'get_rules'
    try_good_state_no_ishapes_no_rules()
    try_good_state_ishapes_no_rules()
    try_good_state_no_ishapes_rules()
    try_good_state_ishapes_rules()

def test_add_to_initial_shapes():
    def try_good_args():
        try_name = 'good_args'
        g.Grammar.clear_all()
        list_name = g.Grammar.initial_shapes
        initial_shape_name = 'initial_shape'
        actual_value = g.Grammar.add_to_initial_shapes(initial_shape_name)
        expected_value = initial_shape_name
        if not actual_value == expected_value:
            u.Utilities.print_test_error_message(
                method_name, try_name, expected_value, actual_value)

    method_name = 'add_to_initial_shapes'
    try_good_args()

def test_add_to_rules():
    def try_good_args():
        try_name = 'good_args'
        g.Grammar.clear_all()
        list_name = 'rules'
        rule_name = 'rule'
        actual_value = g.Grammar.add_to_rules(rule_name)
        expected_value = rule_name
        if not actual_value == expected_value:
            u.Utilities.print_test_error_message(
                method_name, try_name, expected_value, actual_value)

    method_name = 'add_to_rules'
    try_good_args()

def _make_new_grammar_3_ishapes_3_rules():
    g.Grammar.clear_all()
    f.Frame.new()
    rs.AddGroup(ish.InitialShape.component_type)
    rs.AddGroup(r.Rule.component_type)
    ish.InitialShape.add_first()
    r.Rule.add_first()
    _add_two_ishapes()
    _add_two_rules()

def _make_new_grammar_3_ishapes():
    g.Grammar.clear_all()
    f.Frame.new()
    rs.AddGroup(ish.InitialShape.component_type)
    rs.AddGroup(r.Rule.component_type)
    ish.InitialShape.add_first()
    _add_two_ishapes()

def _make_new_grammar_3_rules():
    g.Grammar.clear_all()
    f.Frame.new()
    rs.AddGroup(ish.InitialShape.component_type)
    rs.AddGroup(r.Rule.component_type)
    r.Rule.add_first()
    _add_two_rules()

def _add_two_ishapes():
    ishapes = [
        ('a_ishape', (100, -40, 0)), 
        ('z_ishape', (200, -40, 0))]
    ttype = ish.InitialShape.component_type
    for ishape in ishapes:
        name, origin = ishape
        c.Container.new(name, origin, ttype)

def _add_two_rules():
    rules = [
        ('a_rule', (100, -100, 0)), 
        ('z_rule', (200, -100, 0))]
    ttype = r.Rule.component_type
    for rule in rules:
        name, origin = rule
        c.Container.new(name, origin, ttype)

def _set_up():
    g.Grammar.clear_all()
    f.Frame.new()
    rs.AddGroup(ish.InitialShape.component_type)
    rs.AddGroup(r.Rule.component_type)

# test_new()                                    ##  pending

test__set_up_first_initial_shape()              ##  done
test__set_up_subsequent_initial_shape()         ##  done
test__set_up_initial_shape()                    ##  done
test__set_up_first_rule()                       ##  done
test__set_up_subsequent_rule()                  ##  done
test__set_up_rule()                             ##  done

# test_export()

# test_get_name()                               ##  done
# test_get_dat_string()
# test__get_ordered_named_lshapes_string()

# done
# test_get_initial_shapes()
# test_get_rule_shapes()
# test_get_rules()
# test_add_to_initial_shapes()
# test_add_to_rules()
# test__get_ordered_named_ishape_defs_string()
# test__get_ordered_named_rule_defs_string()
