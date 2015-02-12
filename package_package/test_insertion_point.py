from package.model import grammar as g
from package.model import insertion_point as ip
import rhinoscriptsyntax as rs

def test_get_insertion_point_from_user():
    method_name = 'get_insertion_point_from_user'
    
    def try_good_state():
        try_name = 'good_state'
        g.Grammar.clear_all()
        actual_value = ip.InsertionPoint.get_insertion_point_from_user()
        expected_value = rs.Str2Pt("0,0,0")
        if not actual_value == expected_value:
            g.Grammar.print_test_error_message(
                method_name, try_name, expected_value, actual_value)

    try_good_state()

test_get_insertion_point_from_user()
