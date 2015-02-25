from package.controller import controller as c
from package.view import grammar as g
import rhinoscriptsyntax as rs

bad_type_initial_shape_name = 37
bad_type_is_text = 37
empty_text = ''
multi_line_text = 'line1\nline2'
initial_shape_name = 'initial_shape'

def test__write_is_file():
    method_name = '_write_is_file'

    def try_bad_type_initial_shape_name():
        try_name = 'bad_type_initial_shape_name'
        actual_value = c.Controller._write_is_file(
            bad_type_initial_shape_name, multi_line_text)
        expected_value = None
        if not actual_value == expected_value:
            g.Grammar.print_test_error_message(
                method_name, try_name, expected_value, actual_value)

    def try_bad_type_is_text():
        try_name = 'bad_type_is_text'
        actual_value = c.Controller._write_is_file(
            initial_shape_name, bad_type_is_text)
        expected_value = None
        if not actual_value == expected_value:
            g.Grammar.print_test_error_message(
                method_name, try_name, expected_value, actual_value)

    def try_good_args_empty_text():
        try_name = 'good_args_empty_text'
        actual_value = c.Controller._write_is_file(
            initial_shape_name, empty_text)
        expected_value = initial_shape_name
        if not actual_value == expected_value:
            g.Grammar.print_test_error_message(
                method_name, try_name, expected_value, actual_value)

    def try_good_args_multi_line():
        try_name = 'good_args_multi_line'
        actual_value = c.Controller._write_is_file(
            initial_shape_name, multi_line_text)
        expected_value = initial_shape_name
        if not actual_value == expected_value:
            g.Grammar.print_test_error_message(
                method_name, try_name, expected_value, actual_value)

    try_bad_type_initial_shape_name()
    try_bad_type_is_text()
    try_good_args_empty_text()
    try_good_args_multi_line()

test__write_is_file()
