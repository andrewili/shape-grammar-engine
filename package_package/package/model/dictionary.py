import rhinoscriptsyntax as rs

class Dictionary(object):
    def __init__(self):
        pass

    @classmethod
    def set_value(cls, dict_name, key, value):
        """Receives:
            dict_name       str
            key             str
            value           str
        Returns:
            str             the value set, if successful
            None            otherwise
        """
        method_name = 'set_value'
        try:
            if not (
                type(dict_name) == str and
                type(key) == str and
                type(value) == str
            ):
                raise TypeError
        except TypeError:
            message = "%s.%s: All arguments must be strings" % (
                cls.__name__, method_name)
            print(message)
            return_value = None
        else:
            rs.SetDocumentData(dict_name, key, value)
            actual_value = rs.GetDocumentData(dict_name, key)
            if not actual_value == value:
                return_value = None
            else:
                return_value = actual_value
        finally:
            return return_value

    @classmethod
    def get_value(cls, dict_name, key):
        """Receives:
            dict_name       str
            key             str
        Returns:
            str             the value, if successful
            None            otherwise
        """
        method_name = 'get_value'
        try:
            dict_names = rs.GetDocumentData()
            keys = rs.GetDocumentData(dict_name)
            if not (
                type(dict_name) == str and
                type(key) == str
            ):
                raise TypeError
            elif not (
                dict_name in dict_names and
                key in keys
            ):
                raise ValueError
        except TypeError:
            message = "%s.%s: Both arguments must be strings" % (
                cls.__name__, method_name)
            print(message)
            return_value = None
        except ValueError:
            message = "%s.%s: Both arguments must exist" % (
                cls.__name__, method_name)
            print(message)
            return_value = None
        else:
            actual_value = rs.GetDocumentData(dict_name, key)
            if actual_value == None:
                return_value = None
            else:
                return_value = actual_value
        return return_value

    @classmethod
    def delete_entry(cls, dict_name, key):
        """Receives:
            dict_name       str
            key             str
        Deletes the entry. Returns:
            boolean         True if successful; False otherwise
        """
        method_name = 'delete_entry'
        try:
            dict_names = rs.GetDocumentData()
            keys = rs.GetDocumentData(dict_name)
            if not (
                type(dict_name) == str and
                type(key) == str
            ):
                raise TypeError
            elif not (
                dict_name in dict_names and
                key in keys
            ):
                raise ValueError
        except TypeError:
            message = "%s.%s: Both arguments must be strings" % (
                cls.__name__, method_name)
            print(message)
            return_value = False
        except ValueError:
            message = "%s.%s: Both arguments must exist" % (
                cls.__name__, method_name)
            print(message)
            return_value = False
        else:
            rs.DeleteDocumentData(dict_name, key)
            keys = rs.GetDocumentData(dict_name)
            if key in keys:
                return_value = False
            else:
                return_value = True
        return return_value

    @classmethod
    def dictionary_exists(cls, dict_name):
        """Receives:
            dict_name       str
        Returns:
            boolean         True, if the dictionary exists;
                            False otherwise
        """
        method_name = 'dictionary_exists'
        try:
            if not type(dict_name) == str:
                raise TypeError
        except TypeError:
            message = "%s.%s: The argument must be a string" % (
                cls.__name__, method_name)
            print(message)
            return_value = None
        else:
            dict_names = rs.GetDocumentData()
            return_value = (dict_name in dict_names)
        finally:
            return return_value
