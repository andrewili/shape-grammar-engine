import rhinoscriptsyntax as rs

class Llist(object):
    dummy_value = 'dummy value'

    def __init__(self):
        pass

    @classmethod
    def set_entry(cls, list_name, entry):
        """Receives:
            list_name       str
            entry           str
        Adds the entry to the list, unless it is already there. Returns:
            str             the entry, if successful
            None            otherwise
        """
        method_name = 'set_entry'
        try:
            if not (
                type(list_name) == str and
                type(entry) == str
            ):
                raise TypeError
            entries = rs.GetDocumentData(list_name)
            if entry in entries:
                raise ValueError
        except TypeError:
            message = "%s.%s: Both arguments must be strings" % (
                cls.__name__, method_name)
            print(message)
            return_value = None
        except ValueError:
            message = "%s.%s: The entry '%s' already exists" % (
                cls.__name__, method_name, entry)
            print(message)
            return_value = None
        else:
            dummy_value = cls.dummy_value
            rs.SetDocumentData(list_name, entry, dummy_value)
            entries = rs.GetDocumentData(list_name)
            if entry in entries:
                return_value = entry
            else:
                return_value = None
        finally:
            return return_value

    @classmethod
    def get_entries(cls, list_name):
        """Receives:
            list_name       str
        Returns:
            [str, ...]      a sorted list of entries, if successful
            None            otherwise
        """
        method_name = 'get_entries'
        try:
            if not type(list_name) == str:
                raise TypeError
            list_names = rs.GetDocumentData()
            if not list_name in list_names:
                raise ValueError
        except TypeError:
            message = "%s.%s: The list name must be a string" % (
                cls.__name__, method_name)
            print(message)
            return_value = None
        except ValueError:
            message = "%s.%s: The list name '%s' does not exist" % (
                cls.__name__, method_name, list_name)
            print(message)
            return_value = None
        else:
            return_value = sorted(rs.GetDocumentData(list_name))
        return return_value

    @classmethod
    def delete_entry(cls, list_name, entry):
        """Receives:
            list_name       str
            entry           str
        Removes the entry from the list. Returns:
            boolean         True, if successful;
                            False otherwise
        """
        method_name = 'delete_entry'
        try:
            list_names = rs.GetDocumentData()
            entries = rs.GetDocumentData(list_name)
            if not (
                type(list_name) == str and
                type(entry) == str
            ):
                raise TypeError
            elif not list_name in list_names:
                raise ValueError
            elif not entry in entries:
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
            rs.DeleteDocumentData(list_name, entry)
            entries = rs.GetDocumentData(list_name)
            if entry in entries:
                return_value = False
            else:
                return_value = True
        return return_value

    ##  private methods
    @classmethod
    def contains_entry(cls, list_name, entry):
        """Receives:
            list_name       str
            entry           str
        Returns:
            boolean         True, if the list contains the entry;
                            False otherwise
        """
        method_name = 'contains_entry'
        try:
            if not (
                type(list_name) == str and
                type(entry) == str
            ):
                raise TypeError
            list_names = rs.GetDocumentData()
            if not list_name in list_names:
                raise ValueError
        except TypeError:
            message = "%s.%s: Both arguments must be strings" % (
                cls.__name__, method_name)
            print(message)
            return_value = False
        except ValueError:
            message = "%s.%s: There is no list named '%s'" % (
                cls.__name__, method_name, list_name)
            print(message)
            return_value = False
        else:
            entries = rs.GetDocumentData(list_name)
            return_value = (entry in entries)
        finally:
            return return_value
