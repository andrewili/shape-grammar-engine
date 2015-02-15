from package.view import grammar as g
from package.view import llist as ll
import rhinoscriptsyntax as rs

list_name = 'cities'
entry_1 = 'montreal'
entry_2 = 'tokyo'
dummy_value = ll.Llist.dummy_value

def _set_entries():
    rs.SetDocumentData(list_name, entry_1, dummy_value)
    rs.SetDocumentData(list_name, entry_2, dummy_value)
    
def test_contains_entry():
    method_name = 'contains_entry'

    def try_bad_type_list_name():
        try_name = 'bad_type_list_name'
        g.Grammar.clear_all()
        _set_entries()
        bad_type_list_name = 37
        good_entry = entry_1
        actual_value = ll.Llist.contains_entry(
            bad_type_list_name, good_entry)
        expected_value = False
        if not actual_value == expected_value:
            g.Grammar.print_test_error_message(
                method_name, try_name, expected_value, actual_value)

    def try_bad_type_entry():
        try_name = 'bad_type_entry'
        g.Grammar.clear_all()
        _set_entries()
        bad_type_entry = 29
        actual_value = ll.Llist.contains_entry(list_name, bad_type_entry)
        expected_value = False
        if not actual_value == expected_value:
            g.Grammar.print_test_error_message(
                method_name, try_name, expected_value, actual_value)

    def try_bad_value_list_name():
        try_name = 'bad_value_list_name'
        g.Grammar.clear_all()
        _set_entries()
        bad_value_list_name = 'molecules'
        actual_value = ll.Llist.contains_entry(bad_value_list_name, entry_1)
        expected_value = False
        if not expected_value == actual_value:
            g.Grammar.print_test_error_message(
                method_name, try_name, expected_value, actual_value)

    def try_good_args_false_entry():
        try_name = 'try_good_args_false_entry'
        g.Grammar.clear_all()
        _set_entries()
        false_entry = 'non-existent entry'
        actual_value = ll.Llist.contains_entry(list_name, false_entry)
        expected_value = False
        if not actual_value == expected_value:
            g.Grammar.print_test_error_message(
                method_name, try_name, expected_value, actual_value)

    def try_good_args_true_entry():
        try_name = 'try_good_args_true_entry'
        g.Grammar.clear_all()
        _set_entries()
        dict_name = list_name
        dict_entry = entry_1
        actual_value = ll.Llist.contains_entry(dict_name, dict_entry)
        expected_value = True
        if not actual_value == expected_value:
            g.Grammar.print_test_error_message(
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
        g.Grammar.clear_all()
        _set_entries()
        non_list_name = 37
        actual_value = ll.Llist.set_entry(non_list_name, entry_1)
        expected_value = None
        if not actual_value == expected_value:
            g.Grammar.print_test_error_message(
                method_name, try_name, expected_value, actual_value)

    def try_bad_value_entry():
        try_name = 'bad_value_entry'
        g.Grammar.clear_all()
        _set_entries()
        bad_value_entry = entry_1
        actual_value = ll.Llist.set_entry(list_name, bad_value_entry)
        expected_value = None
        if not actual_value == expected_value:
            g.Grammar.print_test_error_message(
                method_name, try_name, expected_value, actual_value)

    def try_good_args():
        try_name = 'good_args'
        g.Grammar.clear_all()
        _set_entries()
        good_arg_list_name = 'countries'
        good_arg_entry = 'canada'
        actual_value = ll.Llist.set_entry(good_arg_list_name, good_arg_entry)
        expected_value = good_arg_entry
        if not actual_value == expected_value:
            g.Grammar.print_test_error_message(
                method_name, try_name, expected_value, actual_value)

    try_bad_type_list_name()
    try_bad_value_entry()
    try_good_args()

def test_get_entries():
    method_name = 'get_entries'

    def try_bad_type_list_name():
        try_name = 'bad_type_list_name'
        g.Grammar.clear_all()
        _set_entries()
        bad_type_list_name = 37
        actual_value = ll.Llist.get_entries(bad_type_list_name)
        expected_value = None
        if not actual_value == expected_value:
            g.Grammar.print_test_error_message(
                method_name, try_name, expected_value, actual_value)
        
    def try_bad_value_list_name():
        try_name = 'bad_value_list_name'
        g.Grammar.clear_all()
        _set_entries()
        bad_value_list_name = 'things'
        actual_value = ll.Llist.get_entries(bad_value_list_name)
        expected_value = None
        if not actual_value == expected_value:
            g.Grammar.print_test_error_message(
                method_name, try_name, expected_value, actual_value)

    def try_good_arg():
        try_name = 'good_arg'
        g.Grammar.clear_all()
        _set_entries()
        actual_value = ll.Llist.get_entries(list_name)
        expected_value = ['montreal', 'tokyo']
        if not actual_value == expected_value:
            g.Grammar.print_test_error_message(
                method_name, try_name, expected_value, actual_value)

    try_bad_type_list_name()
    try_bad_value_list_name()
    try_good_arg()

def test_delete_entry():
    method_name = 'delete_entry'

    def try_bad_type_list_name():
        try_name = 'bad_type_list_name'
        g.Grammar.clear_all()
        _set_entries()
        bad_type_list_name = 37
        actual_value = ll.Llist.delete_entry(bad_type_list_name, entry_1)
        expected_value = False
        if not actual_value == expected_value:
            g.Grammar.print_test_error_message(
                method_name, try_name, expected_value, actual_value)

    def try_bad_type_entry():
        try_name = 'bad_type_entry'
        g.Grammar.clear_all()
        _set_entries()
        bad_type_entry = 37
        actual_value = ll.Llist.delete_entry(list_name, bad_type_entry)
        expected_value = False
        if not actual_value == expected_value:
            g.Grammar.print_test_error_message(
                method_name, try_name, expected_value, actual_value)

    def try_bad_value_list_name():
        try_name = 'bad_value_list_name'
        g.Grammar.clear_all()
        _set_entries()
        bad_value_list_name = 'things'
        actual_value = ll.Llist.delete_entry(bad_value_list_name, entry_1)
        expected_value = False
        if not actual_value == expected_value:
            g.Grammar.print_test_error_message(
                method_name, try_name, expected_value, actual_value)

    def try_bad_value_entry():
        try_name = 'bad_value_entry'
        g.Grammar.clear_all()
        _set_entries()
        bad_value_entry = 'bagels'
        actual_value = ll.Llist.delete_entry(list_name, bad_value_entry)
        expected_value = False
        if not actual_value == expected_value:
            g.Grammar.print_test_error_message(
                method_name, try_name, expected_value, actual_value)

    def try_good_args():
        try_name = 'good_args'
        g.Grammar.clear_all()
        _set_entries()
        actual_value = ll.Llist.delete_entry(list_name, entry_1)
        expected_value = True
        if not actual_value == expected_value:
            g.Grammar.print_test_error_message(
                method_name, try_name, expected_value, actual_value)

    try_bad_type_list_name()
    try_bad_type_entry()
    try_bad_value_list_name()
    try_bad_value_entry()
    try_good_args()

def test_list_name_exists():
    method_name = 'list_name_exists'

    def try_good_state_false():
        try_name = 'good_state_false'
        g.Grammar.clear_all()
        actual_value = ll.Llist.list_name_exists(list_name)
        expected_value = False
        if not actual_value == expected_value:
            g.Grammar.print_test_error_message(
                method_name, try_name, expected_value, actual_value)

    def try_good_state_true():
        try_name = 'good_state_true'
        g.Grammar.clear_all()
        rs.SetDocumentData(list_name, entry_1, dummy_value)
        actual_value = ll.Llist.list_name_exists(list_name)
        expected_value = True
        if not actual_value == expected_value:
            g.Grammar.print_test_error_message(
                method_name, try_name, expected_value, actual_value)

    try_good_state_false()
    try_good_state_true()

test_contains_entry()
test_set_entry()
test_get_entries()
test_delete_entry()
test_list_name_exists()
