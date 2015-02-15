from package.view import counter as c
from package.view import dictionary as d
import rhinoscriptsyntax as rs

### Counter methods
def test_set_value():
    dict_names = rs.GetDocumentData()
    counters_exists = 'counters' in dict_names
    if counters_exists:
        rs.DeleteDocumentData('counters')
    def try_good_args():
        d.Dictionary.purge_dicts()
        good_value_set = c.Counter.set_value('shapes', 0)
        if not good_value_set == 0:
            print("good_value_set: expected 0; got %s" % good_value_set)
    def try_bad_arg_neg_int_value():
        neg_int_value_set = c.Counter.set_value('shapes', -3)
        if not neg_int_value_set == None:
            print("neg_int_value_set: expected None; got %s" % (
                neg_int_value_set))
    def try_bad_arg_float_value():
        float_value_set = c.Counter.set_value('shapes', 3.7)
        if not float_value_set == None:
            print("float_value_set: expected None; got %s" % float_value_set)
    def try_bad_arg_str_value():
        str_value_set = c.Counter.set_value('shapes', 'zero')
        if not str_value_set == None:
            print("str_value_set: expected None; got %s" % str_value_set)
    try_good_args()
    try_bad_arg_neg_int_value()
    try_bad_arg_float_value()
    try_bad_arg_str_value()

def test_get_value():
    def try_good_arg():
        value_from_good_arg = c.Counter.get_value(counter_name)
        if not value_from_good_arg == value:
            print("%s %s" % (
                "value_from_good_arg: expected %i;" % value,
                "got %s" % value_from_good_arg))
    def try_non_existent_arg():
        non_counter_name = 'non counter name'
        value_from_non_counter_name = c.Counter.get_value(non_counter_name)
        if not value_from_non_counter_name == None:
            print("%s %s" % (
                "value_from_non_counter_name: expected None;",
                "got %s" % value_from_non_counter_name))
    d.Dictionary.purge_dicts()
    counter_name = 'shape'
    value = 0
    c.Counter.set_value(counter_name, value)
    try_good_arg()
    try_non_existent_arg()

def test_increment_value():                     ##  You are here
    def try_good_counter_name():
        actual_new_value = c.Counter.increment_value(counter_name)
        expected_new_value = value + 1
        if actual_new_value == None:
            print("actual_new_value 1: expected %i; got %s" % (
                expected_new_value, actual_new_value))
        elif not actual_new_value == expected_new_value:
            print("actual_new_value 2: expected %i; got %i" % (
                expected_new_value, actual_new_value))
        else:
            pass
    def try_non_counter_name():
        non_counter_name = 'non counter name'
        actual_value_from_non_counter_name = c.Counter.increment_value(
            non_counter_name)
        expected_value = None
        if not actual_value_from_non_counter_name == expected_value:
            print("%s %s %s" % (
                "actual_value_from_non_counter_name:",
                "expected %s;" % expected_value,
                "got %s" % actual_value_from_non_counter_name))
    counter_name = 'shape'
    value = 3
    c.Counter.set_value(counter_name, value)
    try_good_counter_name()
    try_non_counter_name()

test_set_value()
test_get_value()
test_increment_value()