from package.view import frame as f
from package.view import grammar as g
import rhinoscriptsyntax as rs

def test_new():
    method_name = 'new'
    try_name = 'nil'
    g.Grammar.clear_all()
    position = (0, 0, 0)
    guids = f.Frame.new(position)
    actual_value = type(guids)
    expected_value = list
    if not actual_value == expected_value:
        g.Grammar.print_test_error_message(
            method_name, try_name, expected_value, actual_value)

test_new()
