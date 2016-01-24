from package.scripts import grammar as g
from package.scripts import labeled_arrow as la
import rhinoscriptsyntax as rs
from package.scripts import settings as s
from package.tests import utilities as u

def test_new():
    def try_good_args():
        try_name = 'good_args'
        g.Grammar.clear_all()
        layer_name = s.Settings.default_layer_name
        position = (0, 0, 0)
        actual_value = la.LabeledArrow.new(layer_name, position)
        expected_value = '%s-labeled-arrow' % layer_name
        if not actual_value == expected_value:
            u.Utilities.print_test_error_message(
                method_name, try_name, expected_value, actual_value)

    method_name = 'new'
    try_good_args()

test_new()
