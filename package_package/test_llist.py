from package.model import dictionary as d
from package.model import layer as l
from package.model import llist as ll
import rhinoscriptsyntax as rs

list_name = 'cities'
entry_1 = 'montreal'
entry_2 = 'tokyo'
dummy_entry_value = ll.Llist._get_dummy_entry_value()

def test_add_entry():
    def try_bad_type_list_name():
        _initialize_test()
        non_list_name = 37
        actual_value = ll.Llist.add_entry(non_list_name, entry_1)
        expected_value = None
        if not actual_value == expected_value:
            print("%s %s" % (
                "bad_type_list_name: actual_value:",
                "expected %s; got %s" % (expected_value, actual_value)))

    def try_bad_type_entry():
        _initialize_test()
        bad_type_entry = 29
        actual_value = ll.Llist.add_entry(list_name, bad_type_entry)
        expected_value = None
        if not actual_value == expected_value:
            print("%s %s" % (
                "bad_type_entry: actual_value:",
                "expected %s; got %s" % (expected_value, actual_value)))

    def try_bad_value_entry():
        _initialize_test()
        bad_value_entry = entry_1
        entry_value_1 = l.Layer._get_dict_name()
        rs.SetDocumentData(list_name, entry_1, entry_value_1)
        actual_value = ll.Llist.add_entry(list_name, bad_value_entry)
        expected_value = None
        if not actual_value == expected_value:
            print("%s %s" % (
                "bad_value_entry: actual_value:",
                "expected %s; got '%s'" % (expected_value, actual_value)))

    def try_good_args():
        _initialize_test()
        good_arg_list_name = 'countries'
        good_arg_entry = 'canada'
        actual_value = ll.Llist.add_entry(good_arg_list_name, good_arg_entry)
        expected_value = good_arg_entry
        if not actual_value == expected_value:
            print("%s %s" % (
                "good_args: actual_value:",
                "expected '%s'; got '%s'" % (expected_value, actual_value)))

    try_bad_type_list_name()
    try_bad_type_entry()
    try_bad_value_entry()
    try_good_args()

def test_get_entries():
    def try_bad_type_list_name():
        _initialize_test()
        bad_type_list_name = 37
        actual_value = ll.Llist.get_entries(bad_type_list_name)
        expected_value = None
        if not actual_value == expected_value:
            print("get_entries: expected %s; got %s" % (
                    expected_value, actual_value))
        
    def try_bad_value_list_name():
        _initialize_test()
        bad_value_list_name = 'things'
        actual_value = ll.Llist.get_entries(bad_value_list_name)
        expected_value = None
        if not actual_value == expected_value:
            print("bad_value_list_name: expected %s; got %s" % (
                expected_value, actual_value))

    def try_good_arg():
        _initialize_test()
        actual_value = ll.Llist.get_entries(list_name)
        expected_value = ['montreal', 'tokyo']
        if not actual_value == expected_value:
            print("good_arg: expected %s; got %s" % (
                expected_value, actual_value))

    try_bad_type_list_name()
    try_bad_value_list_name()
    try_good_arg()

def test_contains_entry():
    def try_bad_type_list_name():
        _initialize_test()
        bad_type_list_name = 37
        good_entry = entry_1
        actual_value = ll.Llist._contains_entry(bad_type_list_name, good_entry)
        expected_value = False
        if not actual_value == expected_value:
            print("%s %s" % (
                "bad_type_list_name: actual_value:",
                "expected %s; got %s" % (expected_value, actual_value)))

    def try_bad_type_entry():
        _initialize_test()
        bad_type_entry = 29
        actual_value = ll.Llist._contains_entry(list_name, bad_type_entry)
        expected_value = False
        if not actual_value == expected_value:
            print("%s %s" % (
                "bad_type_entry: actual_value:",
                "expected %s; got '%s'" % (expected_value, actual_value)))

    def try_bad_value_list_name():
        _initialize_test()
        bad_value_list_name = 'non-existent list name'
        actual_value = ll.Llist._contains_entry(bad_value_list_name, entry_1)
        expected_value = False
        if not expected_value == actual_value:
            print("%s %s" % (
                "bad_value_list_name: actual_value:",
                "expected %s; got '%s'" % (expected_value, actual_value)))

    def try_good_args_false_entry():
        _initialize_test()
        entry_value = l.Layer._get_layer_value()
        d.Dictionary.set_value(list_name, entry_1, entry_value)
        false_entry = 'non-existent entry'
        actual_value = ll.Llist._contains_entry(list_name, false_entry)
        expected_value = False
        if not actual_value == expected_value:
            print("false_entry: actual_value: expected %s; got '%s'" % (
                expected_value, actual_value))

    def try_good_args_true_entry():
        _initialize_test()
        dict_name = l.Layer._get_dict_name()
        dict_entry = 'excellent'
        dict_entry_value = l.Layer._get_layer_value()
        d.Dictionary.set_value(dict_name, dict_entry, dict_entry_value)
        actual_value = ll.Llist._contains_entry(dict_name, dict_entry)
        expected_value = True
        if not actual_value == expected_value:
            print("%s %s" % (
                "try_good_args_true_entry: actual_value:",
                "expected %s; got %s" % (expected_value, actual_value)))

    try_bad_type_list_name()
    try_bad_type_entry()
    try_bad_value_list_name()
    try_good_args_false_entry()
    try_good_args_true_entry()

def test_delete_entry():                        ##  fix try_good_args()
    def try_bad_type_list_name():
        _initialize_test()
        bad_type_list_name = 37
        actual_value = ll.Llist.delete_entry(bad_type_list_name, entry_1)
        expected_value = False
        if not actual_value == expected_value:
            print("delete_entry: bad_type_list_name: expected %s; got %s" % (
                expected_value, actual_value))

    def try_bad_type_entry():
        _initialize_test()
        bad_type_entry = 37
        actual_value = ll.Llist.delete_entry(list_name, bad_type_entry)
        expected_value = False
        if not actual_value == expected_value:
            print("delete_entry: bad_type_entry: expected %s; got %s" % (
                expected_value, actual_value))

    def try_bad_value_list_name():
        _initialize_test()
        bad_value_list_name = 'things'
        actual_value = ll.Llist.delete_entry(bad_value_list_name, entry_1)
        expected_value = False
        if not actual_value == expected_value:
            print("delete_entry: bad_value_list_name: expected %s; got %s" % (
                expected_value, actual_value))

    def try_bad_value_entry():
        _initialize_test()
        bad_value_entry = 'bagels'
        actual_value = ll.Llist.delete_entry(list_name, bad_value_entry)
        expected_value = False
        if not actual_value == expected_value:
            print("delete_entry: bad_value_entry: expected %s; got %s" % (
                expected_value, actual_value))


    def try_good_args():                        ##  fix me!
        _initialize_test()
        actual_value = ll.Llist.delete_entry(list_name, entry_1)
        expected_value = True
        if not actual_value == expected_value:
            print("delete_entry: good_args: expected %s; got %s" % (
                expected_value, actual_value))

    # try_bad_type_list_name()
    # try_bad_type_entry()
    # try_bad_value_list_name()
    # try_bad_value_entry()
    try_good_args()

def _initialize_test():
    rs.DeleteDocumentData()
    rs.SetDocumentData(list_name, entry_1, dummy_entry_value)
    rs.SetDocumentData(list_name, entry_2, dummy_entry_value)


### test private methods
# test_contains_entry()

### test public methods
# test_add_entry()
# test_get_entries()
test_delete_entry()

