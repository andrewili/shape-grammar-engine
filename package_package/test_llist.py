from package.model import llist as ll
import rhinoscriptsyntax as rs

list_name = 'cities'
entry_1 = 'montreal'
entry_2 = 'tokyo'
dummy_value = ll.Llist.dummy_value

def _clear_all():
    rs.DeleteDocumentData()

def _set_entries():
    rs.SetDocumentData(list_name, entry_1, dummy_value)
    rs.SetDocumentData(list_name, entry_2, dummy_value)
    
def _print_error_message(method_name, try_name, expected_value, actual_value):
        message = ("%s: %s:\n    expected '%s'; got '%s'" % (
            method_name, try_name, expected_value, actual_value))
        print(message)

def test__contains_entry():
    method_name = '_contains_entry'

    def try_bad_type_list_name():
        try_name = 'bad_type_list_name'
        _clear_all()
        _set_entries()
        bad_type_list_name = 37
        good_entry = entry_1
        actual_value = ll.Llist._contains_entry(
            bad_type_list_name, good_entry)
        expected_value = False
        if not actual_value == expected_value:
            _print_error_message(
                method_name, try_name, expected_value, actual_value)

    def try_bad_type_entry():
        try_name = 'bad_type_entry'
        _clear_all()
        _set_entries()
        bad_type_entry = 29
        actual_value = ll.Llist._contains_entry(list_name, bad_type_entry)
        expected_value = False
        if not actual_value == expected_value:
            _print_error_message(
                method_name, try_name, expected_value, actual_value)

    def try_bad_value_list_name():
        try_name = 'bad_value_list_name'
        _clear_all()
        _set_entries()
        bad_value_list_name = 'molecules'
        actual_value = ll.Llist._contains_entry(bad_value_list_name, entry_1)
        expected_value = False
        if not expected_value == actual_value:
            _print_error_message(
                method_name, try_name, expected_value, actual_value)

    def try_good_args_false_entry():
        try_name = 'try_good_args_false_entry'
        _clear_all()
        _set_entries()
        false_entry = 'non-existent entry'
        actual_value = ll.Llist._contains_entry(list_name, false_entry)
        expected_value = False
        if not actual_value == expected_value:
            _print_error_message(
                method_name, try_name, expected_value, actual_value)

    def try_good_args_true_entry():
        try_name = 'try_good_args_true_entry'
        _clear_all()
        _set_entries()
        dict_name = list_name
        dict_entry = entry_1
        actual_value = ll.Llist._contains_entry(dict_name, dict_entry)
        expected_value = True
        if not actual_value == expected_value:
            _print_error_message(
                method_name, try_name, expected_value, actual_value)

    try_bad_type_list_name()
    try_bad_type_entry()
    try_bad_value_list_name()
    try_good_args_false_entry()
    try_good_args_true_entry()

def test_set_entry():
    method_name = 'set_entry'

    def try_bad_type_list_name():
        try_name = 'bad_type_list_name'
        _clear_all()
        _set_entries()
        non_list_name = 37
        actual_value = ll.Llist.set_entry(non_list_name, entry_1)
        expected_value = None
        if not actual_value == expected_value:
            _print_error_message(
                method_name, try_name, expected_value, actual_value)

    def try_bad_type_entry():
        try_name = 'bad_type_entry'
        _clear_all()
        _set_entries()
        bad_type_entry = 29
        actual_value = ll.Llist.set_entry(list_name, bad_type_entry)
        expected_value = None
        if not actual_value == expected_value:
            _print_error_message(
                method_name, try_name, expected_value, actual_value)

    def try_bad_value_entry():
        try_name = 'bad_value_entry'
        _clear_all()
        _set_entries()
        bad_value_entry = entry_1
        actual_value = ll.Llist.set_entry(list_name, bad_value_entry)
        expected_value = None
        if not actual_value == expected_value:
            _print_error_message(
                method_name, try_name, expected_value, actual_value)

    def try_good_args():
        try_name = 'good_args'
        _clear_all()
        _set_entries()
        good_arg_list_name = 'countries'
        good_arg_entry = 'canada'
        actual_value = ll.Llist.set_entry(good_arg_list_name, good_arg_entry)
        expected_value = good_arg_entry
        if not actual_value == expected_value:
            _print_error_message(
                method_name, try_name, expected_value, actual_value)

    try_bad_type_list_name()
    try_bad_type_entry()
    try_bad_value_entry()
    try_good_args()

def test_get_entries():
    method_name = 'get_entries'

    def try_bad_type_list_name():
        try_name = 'bad_type_list_name'
        _clear_all()
        _set_entries()
        bad_type_list_name = 37
        actual_value = ll.Llist.get_entries(bad_type_list_name)
        expected_value = None
        if not actual_value == expected_value:
            _print_error_message(
                method_name, try_name, expected_value, actual_value)
        
    def try_bad_value_list_name():
        try_name = 'bad_value_list_name'
        _clear_all()
        _set_entries()
        bad_value_list_name = 'things'
        actual_value = ll.Llist.get_entries(bad_value_list_name)
        expected_value = None
        if not actual_value == expected_value:
            _print_error_message(
                method_name, try_name, expected_value, actual_value)

    def try_good_arg():
        try_name = 'good_arg'
        _clear_all()
        _set_entries()
        actual_value = ll.Llist.get_entries(list_name)
        expected_value = ['montreal', 'tokyo']
        if not actual_value == expected_value:
            _print_error_message(
                method_name, try_name, expected_value, actual_value)

    try_bad_type_list_name()
    try_bad_value_list_name()
    try_good_arg()

def test_delete_entry():
    method_name = 'delete_entry'

    def try_bad_type_list_name():
        try_name = 'bad_type_list_name'
        _clear_all()
        _set_entries()
        bad_type_list_name = 37
        actual_value = ll.Llist.delete_entry(bad_type_list_name, entry_1)
        expected_value = False
        if not actual_value == expected_value:
            _print_error_message(
                method_name, try_name, expected_value, actual_value)

    def try_bad_type_entry():
        try_name = 'bad_type_entry'
        _clear_all()
        _set_entries()
        bad_type_entry = 37
        actual_value = ll.Llist.delete_entry(list_name, bad_type_entry)
        expected_value = False
        if not actual_value == expected_value:
            _print_error_message(
                method_name, try_name, expected_value, actual_value)

    def try_bad_value_list_name():
        try_name = 'bad_value_list_name'
        _clear_all()
        _set_entries()
        bad_value_list_name = 'things'
        actual_value = ll.Llist.delete_entry(bad_value_list_name, entry_1)
        expected_value = False
        if not actual_value == expected_value:
            _print_error_message(
                method_name, try_name, expected_value, actual_value)

    def try_bad_value_entry():
        try_name = 'bad_value_entry'
        _clear_all()
        _set_entries()
        bad_value_entry = 'bagels'
        actual_value = ll.Llist.delete_entry(list_name, bad_value_entry)
        expected_value = False
        if not actual_value == expected_value:
            _print_error_message(
                method_name, try_name, expected_value, actual_value)

    def try_good_args():
        try_name = 'good_args'
        _clear_all()
        _set_entries()
        actual_value = ll.Llist.delete_entry(list_name, entry_1)
        expected_value = True
        if not actual_value == expected_value:
            _print_error_message(
                method_name, try_name, expected_value, actual_value)

    try_bad_type_list_name()
    try_bad_type_entry()
    try_bad_value_list_name()
    try_bad_value_entry()
    try_good_args()

test__contains_entry()
test_set_entry()
test_get_entries()
test_delete_entry()
