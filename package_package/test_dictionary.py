from package.model import dictionary as d
import rhinoscriptsyntax as rs

### self utilities
def purge_dicts():
    rs.DeleteDocumentData()

def set_test_value():
    dict_name, key, value = 'dict name', 'key', 'value'
    value_was_set = d.Dictionary.set_value(
        dict_name, key, value)
    return value_was_set

def set_test_values():
    rs.SetDocumentData('dict1', 'key1a', 'value1a')
    rs.SetDocumentData('dict1', 'key1b', 'value1b')
    rs.SetDocumentData('dict2', 'key2a', 'value2a')
    rs.SetDocumentData('dict2', 'key2b', 'value2b')

### Dictionary utilities
def test_get_dict_names():
    def try_0_dicts():
        purge_dicts()
        sorted_dict_names_gotten = d.Dictionary.get_dict_names()
        if not sorted_dict_names_gotten == []:
            print("%s %s" % (
                "sorted_dict_names_gotten: expected [];",
                "got %s" % sorted_dict_names_gotten))
    def try_1_dict():
        purge_dicts()
        set_test_value()
        sorted_dict_names_gotten = d.Dictionary.get_dict_names()
        if not sorted_dict_names_gotten == ['dict name']:
            print("%s %s" % (
                "sorted_dict_names_gotten: expected [dict name'];",
                "got %s" % sorted_dict_names_gotten))
    def try_2_dicts():
        purge_dicts()
        set_test_values()
        sorted_dict_names_gotten = d.Dictionary.get_dict_names()
        if not sorted_dict_names_gotten == ['dict1', 'dict2']:
            print("%s %s" % (
                "sorted_dict_names_gotten: expected ['dict1', 'dict2'];",
                "got %s" % sorted_dict_names_gotten))
    try_0_dicts()
    try_1_dict()
    try_2_dicts()

def test_get_keys():
    def try_good_arg():
        dict1_keys = d.Dictionary.get_keys('dict1')
        dict1_keys_are_correct = (
            len(dict1_keys) == 2 and
            'key1a' in dict1_keys and
            'key1b' in dict1_keys)
        if not dict1_keys_are_correct:
            print("Good keys: error")
    def try_non_existent_dict():
        keys_from_non_existent_dict = d.Dictionary.get_keys('non dict')
        if not keys_from_non_existent_dict == None:
            print("keys_from_non_existent_dict: %s" % (
                keys_from_non_existent_dict))
    purge_dicts()
    set_test_values()
    try_good_arg()
    try_non_existent_dict()

### Dictionary methods
def test_purge_dicts():
    set_test_values()
    d.Dictionary.purge_dicts()
    dict_names = rs.GetDocumentData()
    if not dict_names == []:
        print("dict_names: expected []; got %s" % dict_names)

def test_set_value():
    purge_dicts()
    dict_name, key, value = 'dict', 'key', 'value'
    value_set = d.Dictionary.set_value(dict_name, key, value)
    if not value_set == value:
        print("value_set: expected '%s'; got '%s'" % (value, value_set))
    # value_was_set = d.Dictionary.set_value(dict_name, key, value)
    # if not value_was_set:
    #     print("value was not set; expected True; got %s" % value_was_set)

def test_get_value():
    dict_name, key, value = 'dict1', 'key1', 'value1'
    def set_value():
        d.Dictionary.set_value(dict_name, key, value)
    def try_good_value():
        value_gotten = d.Dictionary.get_value(dict_name, key)
        if not value_gotten == 'value1':
            print("value: expected '%s'; got '%s'" % (value, value_gotten))
    def try_non_existent_dict_name():
        non_dict_name = 'non_dict'
        value_from_non_dict_name = d.Dictionary.get_value(
            non_dict_name, key)
        if not value_from_non_dict_name == None:
            print("Non dict name: expected None; got %s" % (
                value_from_non_dict_name))
    def try_non_existent_key():
        non_key = 'non_key'
        value_from_non_key = d.Dictionary.get_value(dict_name, non_key)
        if not value_from_non_key == None:
            print("Non key: expected None; got %s" % value_from_non_key)
    purge_dicts()
    set_value()
    try_good_value()
    try_non_existent_dict_name()
    try_non_existent_key()

def test_delete_entry():
    purge_dicts()
    set_test_values()
    good_entry_was_deleted = d.Dictionary.delete_entry('dict1', 'key1a')
    if not good_entry_was_deleted:
        print("good_entry_was_deleted: '%s'" % good_entry_was_deleted)
    bad_dict_entry_was_deleted = d.Dictionary.delete_entry('dict0', 'key1a')
    if bad_dict_entry_was_deleted:
        print("bad_dict_entry_was_deleted: '%s'" % bad_dict_entry_was_deleted)
    bad_key_entry_was_deleted = d.Dictionary.delete_entry('dict1', 'key1c')
    if bad_key_entry_was_deleted:
        print("test_delete_entry: bad key entry was deleted")

### Dictionary utilities tests
test_purge_dicts()
test_get_dict_names()
test_get_keys()

### Dictionary methods tests
test_set_value()
test_get_value()
test_delete_entry()
