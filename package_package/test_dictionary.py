from package.model import dictionary as d
import rhinoscriptsyntax as rs

dict_name_1 = 'dict_name_1'
dict_name_2 = 'dict_name_2'
key_1a = 'key_1a'
key_1b = 'key_1b'
key_2a = 'key_2a'
key_2b = 'key_2b'
value_1a = 'value_1a'
value_1b = 'value_1b'
value_2a = 'value_2a'
value_2b = 'value_2b'

def _clear_all():
    rs.DeleteDocumentData()

def _set_entries():
    rs.SetDocumentData(dict_name_1, key_1a, value_1a)
    rs.SetDocumentData(dict_name_1, key_1b, value_1b)
    rs.SetDocumentData(dict_name_2, key_2a, value_2a)
    rs.SetDocumentData(dict_name_2, key_2b, value_2b)

def _print_error_message(method_name, try_name, expected_value, actual_value):
    message = "%s: %s: expected '%s'; got '%s'" % (
        method_name, try_name, expected_value, actual_value)
    print(message)

### class methods
def test_set_value():
    method_name = 'set_value'

    def try_bad_type_dict_name():
        try_name = 'bad_type_dict_name'
        _clear_all()
        _set_entries()
        bad_type_dict_name = 37
        actual_value = d.Dictionary.set_value(
            bad_type_dict_name, key_1a, value_1a)
        expected_value = None
        if not actual_value == expected_value:
            _print_error_message(
                method_name, try_name, expected_value, actual_value)

    def try_bad_type_key():
        try_name = 'bad_type_key'
        _clear_all()
        _set_entries()
        bad_type_key = 23
        actual_value = d.Dictionary.set_value(
            dict_name_1, bad_type_key, value_1a)
        expected_value = None
        if not actual_value == expected_value:
            _print_error_message(
                method_name, try_name, expected_value, actual_value)

    def try_bad_type_value():
        try_name = 'bad_type_value'
        _clear_all()
        _set_entries()
        bad_type_value = 23
        actual_value = d.Dictionary.set_value(
            dict_name_1, key_1a, bad_type_value)
        expected_value = None
        if not actual_value == expected_value:
            _print_error_message(
                method_name, try_name, expected_value, actual_value)

    def try_good_args():
        try_name = 'good_args'
        _clear_all()
        _set_entries()
        dict_name_3 = 'dict_name_3'
        key_3 = 'key_3'
        value_3 = 'value_3'
        actual_value = d.Dictionary.set_value(dict_name_3, key_3, value_3)
        expected_value = 'value_3'
        if not actual_value == expected_value:
            _print_error_message(
                method_name, try_name, expected_value, actual_value)

    try_bad_type_dict_name()
    try_bad_type_key()
    try_bad_type_value()
    try_good_args()

def test_get_value():
    method_name = 'get_value'

    def try_bad_type_dict_name():
        try_name = 'bad_type_dict_name'
        _clear_all()
        _set_entries()
        bad_type_dict_name = 37
        actual_value = d.Dictionary.get_value(bad_type_dict_name, key_1a)
        expected_value = None
        if not actual_value == expected_value:
            _print_error_message(
                method_name, try_name, expected_value, actual_value)

    def try_bad_type_key():
        try_name = 'bad_type_key'
        _clear_all()
        _set_entries()
        bad_type_key = 23
        actual_value = d.Dictionary.get_value(dict_name_1, bad_type_key)
        expected_value = None
        if not actual_value == expected_value:
            _print_error_message(
                method_name, try_name, expected_value, actual_value)

    def try_bad_value_dict_name():
        try_name = 'bad_value_dict_name'
        _clear_all()
        _set_entries()
        bad_value_dict_name = 'dict_name_0'
        actual_value = d.Dictionary.get_value(bad_value_dict_name, key_1a)
        expected_value = None
        if not actual_value == expected_value:
            _print_error_message(
                method_name, try_name, expected_value, actual_value)

    def try_bad_value_key():
        try_name = 'bad_value_key'
        _clear_all()
        _set_entries()
        bad_value_key = 'key_0'
        actual_value = d.Dictionary.get_value(dict_name_1, bad_value_key)
        expected_value = None
        if not actual_value == expected_value:
            _print_error_message(
                method_name, try_name, expected_value, actual_value)

    def try_good_args():
        try_name = 'good_args'
        _clear_all()
        _set_entries()
        actual_value = d.Dictionary.get_value(dict_name_1, key_1a)
        expected_value = value_1a
        if not actual_value == expected_value:
            _print_error_message(
                method_name, try_name, expected_value, actual_value)

    try_bad_type_dict_name()
    try_bad_type_key()
    try_bad_value_dict_name()
    try_bad_value_key()
    try_good_args()

def test_delete_entry():
    method_name = 'delete_entry'

    def try_bad_type_dict_name():
        try_name = 'bad_type_dict_name'
        _clear_all()
        _set_entries()
        bad_type_dict_name = 29
        actual_value = d.Dictionary.delete_entry(bad_type_dict_name, key_1a)
        expected_value = False
        if not actual_value == expected_value:
            _print_error_message(
                method_name, try_name, expected_value, actual_value)

    def try_bad_type_key():
        try_name = 'bad_type_key'
        _clear_all()
        _set_entries()
        bad_type_key = 37
        actual_value = d.Dictionary.delete_entry(dict_name_1, bad_type_key)
        expected_value = False
        if not actual_value == expected_value:
            _print_error_message(
                method_name, try_name, expected_value, actual_value)

    def try_bad_value_dict_name():
        try_name = 'bad_value_dict_name'
        _clear_all()
        _set_entries()
        bad_value_dict_name = 'dict_name_0'
        actual_value = d.Dictionary.delete_entry(bad_value_dict_name, key_1a)
        expected_value = False
        if not actual_value == expected_value:
            _print_error_message(
                method_name, try_name, expected_value, actual_value)

    def try_bad_value_key():
        try_name = 'bad_value_key'
        _clear_all()
        _set_entries()
        bad_value_key = 'key_0'
        actual_value = d.Dictionary.delete_entry(dict_name_1, bad_value_key)
        expected_value = False
        if not actual_value == expected_value:
            _print_error_message(
                method_name, try_name, expected_value, actual_value)

    def try_good_args():
        try_name = 'good_args'
        _clear_all()
        _set_entries()
        actual_value = d.Dictionary.delete_entry(dict_name_1, key_1a)
        expected_value = True
        if not actual_value == expected_value:
            _print_error_message(
                method_name, try_name, expected_value, actual_value)

    try_bad_type_dict_name()
    try_bad_type_key()
    try_bad_value_dict_name()
    try_bad_value_key()
    try_good_args()

def test_dictionary_exists():
    method_name = 'dictionary_exists'

    def try_bad_type_dict_name():
        try_name = 'bad_type_dict_name'
        bad_type_dict_name = 37
        actual_value = d.Dictionary.dictionary_exists(bad_type_dict_name)
        expected_value = None
        if not actual_value == expected_value:
            _print_error_message(
                method_name, try_name, expected_value, actual_value)

    def try_good_arg_false_dict_name():
        try_name = 'good_arg_false_dict_name'
        good_arg_false_dict_name = 'dict_name_0'
        actual_value = d.Dictionary.dictionary_exists(
            good_arg_false_dict_name)
        expected_value = False
        if not actual_value == expected_value:
            _print_error_message(
                method_name, try_name, expected_value, actual_value)

    def try_good_arg_true_dict_name():
        try_name = 'good_arg_true_dict_name'
        good_arg_true_dict_name = dict_name_1
        actual_value = d.Dictionary.dictionary_exists(dict_name_1)
        expected_value = True
        if not actual_value == expected_value:
            _print_error_message(
                method_name, try_name, expected_value, actual_value)

    try_bad_type_dict_name()
    try_good_arg_false_dict_name()
    try_good_arg_true_dict_name()

test_set_value()
test_get_value()
test_delete_entry()
test_dictionary_exists()


### class utilities
# def purge_dicts():
    # rs.DeleteDocumentData()

### Dictionary utilities
# def test_get_dict_names():
    # def try_0_dicts():
    #     purge_dicts()
    #     sorted_dict_names_gotten = d.Dictionary.get_dict_names()
    #     if not sorted_dict_names_gotten == []:
    #         print("%s %s" % (
    #             "sorted_dict_names_gotten: expected [];",
    #             "got %s" % sorted_dict_names_gotten))
    # def try_1_dict():
    #     purge_dicts()
    #     set_test_value()
    #     sorted_dict_names_gotten = d.Dictionary.get_dict_names()
    #     if not sorted_dict_names_gotten == ['dict name']:
    #         print("%s %s" % (
    #             "sorted_dict_names_gotten: expected [dict name'];",
    #             "got %s" % sorted_dict_names_gotten))
    # def try_2_dicts():
    #     purge_dicts()
    #     set_test_values()
    #     sorted_dict_names_gotten = d.Dictionary.get_dict_names()
    #     if not sorted_dict_names_gotten == ['dict1', 'dict2']:
    #         print("%s %s" % (
    #             "sorted_dict_names_gotten: expected ['dict1', 'dict2'];",
    #             "got %s" % sorted_dict_names_gotten))
    # try_0_dicts()
    # try_1_dict()
    # try_2_dicts()

# def test_get_keys():
    # def try_good_arg():
    #     dict1_keys = d.Dictionary.get_keys('dict1')
    #     dict1_keys_are_correct = (
    #         len(dict1_keys) == 2 and
    #         'key1a' in dict1_keys and
    #         'key1b' in dict1_keys)
    #     if not dict1_keys_are_correct:
    #         print("Good keys: error")
    # def try_non_existent_dict():
    #     keys_from_non_existent_dict = d.Dictionary.get_keys('non dict')
    #     if not keys_from_non_existent_dict == None:
    #         print("keys_from_non_existent_dict: %s" % (
    #             keys_from_non_existent_dict))
    # purge_dicts()
    # set_test_values()
    # try_good_arg()
    # try_non_existent_dict()

### Dictionary methods
# def test_purge_dicts():
    # set_test_values()
    # d.Dictionary.purge_dicts()
    # dict_names = rs.GetDocumentData()
    # if not dict_names == []:
    #     print("dict_names: expected []; got %s" % dict_names)

### test private methods

### test public methods

### Dictionary utilities tests
# test_purge_dicts()
# test_get_dict_names()
# test_get_keys()

### Dictionary methods tests
