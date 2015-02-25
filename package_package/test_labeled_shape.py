from package.view import grammar as g
from package.view import labeled_point as lp
import rhinoscriptsyntax as rs

bad_type_label = 37
bad_type_point = 37
bad_value_label = 'kil#roy'
label = 'label'
point = (0, 0, 0)

def test_new():
    method_name = 'new'

    def try_bad_type_label():
        try_name = 'bad_type_label'
        g.Grammar.clear_all()
        actual_value = lp.LabeledPoint.new(bad_type_label, point)
        expected_value = None
        if not actual_value == expected_value:
            g.Grammar.print_test_error_message(
                method_name, try_name, expected_value, actual_value)

    def try_bad_type_point():
        try_name = 'bad_type_point'
        g.Grammar.clear_all()
        actual_value = lp.LabeledPoint.new(label, bad_type_point)
        expected_value = None
        if not actual_value == expected_value:
            g.Grammar.print_test_error_message(
                method_name, try_name, expected_value, actual_value)

    def try_bad_value_label():
        try_name = 'bad_value_label'
        g.Grammar.clear_all()
        actual_value = lp.LabeledPoint.new(bad_value_label, point)
        expected_value = None
        if not actual_value == expected_value:
            g.Grammar.print_test_error_message(
                method_name, try_name, expected_value, actual_value)

    def try_bad_value_point():
        """No bad values"""
        pass

    def try_good_args():
        try_name = 'good_args'
        g.Grammar.clear_all()
        actual_value = lp.LabeledPoint.new(label, point)
        actual_value_is_guid = rs.IsObject(actual_value)
        expected_value = True
        if not actual_value_is_guid == expected_value:
            g.Grammar.print_test_error_message(
                method_name, try_name, expected_value, actual_value_is_guid)

    try_bad_type_label()
    try_bad_type_point()
    try_bad_value_label()
    try_good_args()

test_new()
