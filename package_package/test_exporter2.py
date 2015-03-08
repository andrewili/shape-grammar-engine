from package.translators import exporter2 as e2
from package.view import grammar as g
import rhinoscriptsyntax as rs

method_name = '_write_file'
bad_type_file_type = 37
bad_type_string = 37
bad_value_file_type = 'txt'
file_type = 'is'
shape_name = 'test name'
string = 'test string'

def test__write_file():                         ##  03-06 12:24
    def try_bad_type_file_type():
        try_name = 'bad_type_file_type'
        my_exporter2 = e2.Exporter2()
        actual_value = my_exporter2._write_file(
            bad_type_file_type, shape_name, string)
        expected_value = None
        if not actual_value == expected_value:
            g.Grammar.print_test_error_message(
                method_name, try_name, expected_value, actual_value)
        
    def try_bad_type_string():
        try_name = 'bad_type_file_string'
        my_exporter2 = e2.Exporter2()
        actual_value = my_exporter2._write_file(
            file_type, shape_name, bad_type_string)
        expected_value = None
        if not actual_value == expected_value:
            g.Grammar.print_test_error_message(
                method_name, try_name, expected_value, actual_value)
        
    def try_bad_value_file_type():
        try_name = 'bad_value_file_type'
        my_exporter2 = e2.Exporter2()
        actual_value = my_exporter2._write_file(
            bad_value_file_type, shape_name, string)
        expected_value = None
        if not actual_value == expected_value:
            g.Grammar.print_test_error_message(
                method_name, try_name, expected_value, actual_value)

    def try_good_args():
        try_name = 'good_args'
        my_exporter2 = e2.Exporter2()
        actual_value = my_exporter2._write_file(file_type, shape_name, string)
        expected_value = string
        if not actual_value == expected_value:
            g.Grammar.print_test_error_message(
                method_name, try_name, expected_value, actual_value)
        
    # try_bad_type_file_type()
    # try_bad_type_string()
    # try_bad_value_file_type()
    try_good_args()

def test__get_filter_from_file_type():          ##  03-07 15:02
    method_name = '_get_filter_from_file_type'

    def try_good_arg():
        try_name = 'good_arg'
        my_exporter2 = e2.Exporter2()
        actual_value = my_exporter2._get_filter_from_file_type(file_type)
        expected_value = "IS file (*.is)|*.is|All files (*.*)|*.*||"
        if not actual_value == expected_value:
            g.Grammar.print_test_error_message(
                method_name, try_name, expected_value, actual_value)

    try_good_arg()

test__write_file()
# test__get_filter_from_file_type()