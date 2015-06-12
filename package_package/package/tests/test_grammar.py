from package.view import frame_block as fb
from package.view import container as c
from package.view import grammar as g
from package.view import initial_shape as ish
from package.view import rule as r
import rhinoscriptsyntax as rs
from package.tests import utilities as u

def test_new():
    method_name = 'new'
    g.Grammar.clear_all()
    g.Grammar.new()

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

def test_export():
    pass

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

    def try_good_state_no_list():
        try_name = 'good_state_empty_list'
        _set_up()
        actual_value = g.Grammar.get_rules()
        expected_value = None
        if not actual_value == expected_value:
            u.Utilities.print_test_error_message(
                method_name, try_name, expected_value, actual_value)

    def try_good_state_non_empty_list():
        try_name = 'good_state_non_empty_list'
        _set_up()
        first = r.Rule.first_rule_name
        second = 'a_rule'
        r.Rule.add_first()
        print("Enter '%s'" % second)
        r.Rule.add_subsequent()
        actual_value = g.Grammar.get_rules()
        expected_value = sorted([first, second])
        if not actual_value == expected_value:
            u.Utilities.print_test_error_message(
                method_name, try_name, expected_value, actual_value)

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
    fb.FrameBlock.new()
    rs.AddGroup(ish.InitialShape.component_type)
    rs.AddGroup(r.Rule.component_type)
    ish.InitialShape.add_first()
    r.Rule.add_first()
    _add_two_ishapes()
    _add_two_rules()

def _make_new_grammar_3_ishapes():
    g.Grammar.clear_all()
    fb.FrameBlock.new()
    rs.AddGroup(ish.InitialShape.component_type)
    ish.InitialShape.add_first()
    _add_two_ishapes()

def _make_new_grammar_3_rules():
    g.Grammar.clear_all()
    fb.FrameBlock.new()
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
    fb.FrameBlock.new()

# test_new()                                    ##  to do
# test_export()                                 ##  to do
# test_get_name()
# test_get_initial_shapes()
test_get_rules()
# test_add_to_initial_shapes()
# test_add_to_rules()
