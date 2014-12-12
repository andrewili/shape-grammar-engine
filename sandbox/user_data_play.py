#   user_data_play.py

import rhinoscriptsyntax as rs

def delete_document_data():
    rs.DeleteDocumentData()
    document_data = rs.GetDocumentData()
    print('document data before: %s' % document_data)

def set_document_user_text():
    document_set_is_successful = rs.SetDocumentUserText('key1', 'value1')
    if document_set_is_successful:
        print('Document set is successful')
    else:
        print("Couldn't set")
    value1 = rs.GetDocumentUserText('key1')
    if value1:
        print('Document get is successful')
        print('key1: %s' % (value1))

def print_document_data():
    document_data = rs.GetDocumentData()
    print('document data after: %s' % document_data)

def set_document_data_with_section():
    """Assume that a section is like a dictionary. Set:
        dict1 = {'key1a': 'value1a', 'key1b', 'value1b'}
        dict2 = {'key2a': 'value2a', 'key2b', 'value2b'}
    """
    rs.SetDocumentData('dict1', 'key1a', 'value1a')
    rs.SetDocumentData('dict1', 'key1b', 'value1b')
    rs.SetDocumentData('dict2', 'key2a', 'value2a')
    rs.SetDocumentData('dict2', 'key2b', 'value2b')

def print_dict(dict_name):
    dict_keys = rs.GetDocumentData(dict_name)
    print('%s: %s' % (dict_name, dict_keys))

# delete_document_data()
# set_document_user_text()
# print_document_data()

set_document_data_with_section()
print_document_data()
print_dict('dict1')
print_dict('dict2')
