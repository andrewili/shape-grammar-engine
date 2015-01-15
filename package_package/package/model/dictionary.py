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

    ### utilities
    # @classmethod
    # def purge_dicts(cls):                       ##  Purges lists too
        # """Purges all dictionaries. Returns:
        #     boolean         True if successful; False otherwise
        # """
        # rs.DeleteDocumentData()
        # dict_names = rs.GetDocumentData()
        # dicts_were_purged = (dict_names == [])
        # return dicts_were_purged

    # @classmethod
    # def get_dict_names(cls):
        # """Returns:
        #     [str, ...]      sorted user dictionary names, if successful
        #     None            otherwise
        # """
        # names = rs.GetDocumentData()
        # return sorted(names)

    # @classmethod
    # def get_keys(cls, dict_name):
        # """Receives:
        #     dict_name       str
        # Returns:
        #     [str, ...]      keys in the dictionary, if successful
        #     None            otherwise
        # """
        # dict_names = cls.get_dict_names()
        # if dict_names == None:
        #     return_value = None
        # elif dict_name not in dict_names:
        #     return_value = None
        # else:
        #     keys = rs.GetDocumentData(dict_name)
        #     if keys:
        #         return_value = keys
        #     else:
        #         return_value = None
        # return return_value

    # ### dictionaries
    # @classmethod
    # def purge_dict(cls, dict_name):
        # """Receives:
        #     dict_name       str
        # Purges the dictionary and its contents. Returns the success value:
        #     boolean         True if successful; False otherwise
        # """
        # dict_names = cls.get_dict_names()
        # if not dict_name in dict_names:
        #     message = "No such dictionary name: '%s'" % dict_name
        # else:
        #     rs.DeleteDocumentData(dict_name)
        # dict_names = cls.get_dict_names()
        # if dict_name in dict_names:
        #     dict_was_purged = False
        # else:
        #     dict_was_purged = True
        # return dict_was_purged

