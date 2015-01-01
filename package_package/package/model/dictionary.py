import rhinoscriptsyntax as rs

class Dictionary(object):
    def __init__(self):
        pass

    ### utilities
    @classmethod
    def purge_dicts(cls):
        """Purges all dictionaries. Returns:
            boolean         True if successful; False otherwise
        """
        rs.DeleteDocumentData()
        dict_names = rs.GetDocumentData()
        dicts_were_purged = (dict_names == [])
        return dicts_were_purged

    @classmethod
    def get_dict_names(cls):
        """Returns:
            [str, ...]      sorted user dictionary names, if successful
            None            otherwise
        """
        names = rs.GetDocumentData()
        return sorted(names)

    @classmethod
    def get_keys(cls, dict_name):
        """Receives:
            dict_name       str
        Returns:
            [str, ...]      keys in the dictionary, if successful
            None            otherwise
        """
        dict_names = cls.get_dict_names()
        if dict_names == None:
            return_value = None
        elif dict_name not in dict_names:
            return_value = None
        else:
            keys = rs.GetDocumentData(dict_name)
            if keys:
                return_value = keys
            else:
                return_value = None
        return return_value

    ### dictionaries
    @classmethod
    def purge_dict(cls, dict_name):
        """Receives:
            dict_name       str
        Purges the dictionary and its contents. Returns the success value:
            boolean         True if successful; False otherwise
        """
        dict_names = cls.get_dict_names()
        if not dict_name in dict_names:
            message = "No such dictionary name: '%s'" % dict_name
        else:
            rs.DeleteDocumentData(dict_name)
        dict_names = cls.get_dict_names()
        if dict_name in dict_names:
            dict_was_purged = False
        else:
            dict_was_purged = True
        return dict_was_purged

    ### entries
    @classmethod
    def set_value(cls, dict_name, key, value):
        """Receives:
            dict_name       str
            key             str
            value           str
        Returns:
            str             the value set, if successful
            None            otherwise
            # boolean         True if successful; False otherwise
        """
        dict_entry = "'%s': '%s': '%s'" % (
            dict_name, key, value)
        rs.SetDocumentData(dict_name, key, value)
        value_gotten = rs.GetDocumentData(dict_name, key)
        if not value_gotten == value:
            return_value = None
        else:
            return_value = value_gotten
        return return_value

    @classmethod
    def get_value(cls, dict_name, key):
        """Receives:
            dict_name       str
            key             str
        Returns:
            str             the value, if successful
            None            if unsuccessful
        """
        dict_names = cls.get_dict_names()
        keys = cls.get_keys(dict_name)
        if dict_name not in dict_names:
            return_value = None
        elif key not in keys:
            return_value = None
        else:
            value = rs.GetDocumentData(dict_name, key)
            return_value = value
        return return_value

    @classmethod
    def delete_entry(cls, dict_name, key):
        """Receives:
            dict_name       str
            key             str
        Deletes the entry. Returns:
            boolean         True if successful; False otherwise
        """
        entry_name = "%s: %s" % (dict_name, key)
        keys = cls.get_keys(dict_name)
        if keys == None:
            entry_was_deleted = False
        elif key not in keys:
            entry_was_deleted = False
        else:
            rs.DeleteDocumentData(dict_name, key)
            keys = cls.get_keys(dict_name)
            key_exists = key in keys            ##  keys = None
            if key_exists:
                entry_was_deleted = False
            else:
                entry_was_deleted = True
        return entry_was_deleted

