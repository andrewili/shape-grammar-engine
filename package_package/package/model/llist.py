from package.model import layer as l
import rhinoscriptsyntax as rs

class Llist(object):
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
            message = "Both arguments must be strings"
            print(message)
            return_value = None
        except ValueError:
            message = "The entry '%s' already exists" % entry
            print(message)
            return_value = None
        else:
            dummy_entry_value = cls._get_dummy_entry_value()
            rs.SetDocumentData(list_name, entry, dummy_entry_value)
            entries = rs.GetDocumentData(list_name)
            if entry in entries:
                return_value = entry
            else:
                return_value = None
            return return_value

    @classmethod
    def get_entries(cls, list_name):
        """Receives:
            list_name       str
        Returns:
            [str, ...]      a sorted list of entries, if successful
            None            otherwise
        """
        try:
            if not type(list_name) == str:
                raise TypeError
            list_names = rs.GetDocumentData()
            if not list_name in list_names:
                raise ValueError
        except TypeError:
            message = "The list name must be a string"
            print(message)
            return_value = None
        except ValueError:
            message = "The list '%s' does not exist" % list_name
            print(message)
            return_value = None
        else:
            return_value = rs.GetDocumentData(list_name)
        return return_value

    @classmethod
    def delete_entry(cls, list_name, entry):
        """Receives:
            list_name       str
            entry           str
        Removes the entry from the list. Returns:
            boolean         True, if successful; False otherwise
        """
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
            message = "Both arguments must be strings"
            print(message)
            return_value = False
        except ValueError:
            message = "Both arguments must exist"
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
    def _get_dummy_entry_value(cls):
        """Returns a dummy value for Rhino's user data entry:
            str             'nil'
        """
        return 'nil'

    @classmethod
    def _contains_entry(cls, list_name, entry):
        """Receives:
            list_name       str
            entry           str
        Returns:
            boolean         True, if the list contains the entry; False 
                            otherwise
        """
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
            message = "Both arguments must be strings"
            print(message)
            return_value = False
        except ValueError:
            message = "There is no list named '%s'" % list_name
            print(message)
            return_value = False
        else:
            entries = rs.GetDocumentData(list_name)
            return_value = (entry in entries)
        return return_value

