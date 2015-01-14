from package.model import layer as l
import rhinoscriptsyntax as rs

class Llist(object):
    class_name = 'Llist'
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
            message = "%s: Both arguments must be strings" % cls.class_name
            print(message)
            return_value = None
        except ValueError:
            message = "%s: The entry '%s' already exists" % (
                cls.class_name, entry)
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
        try:
            if not type(list_name) == str:
                raise TypeError
            list_names = rs.GetDocumentData()
            if not list_name in list_names:
                raise ValueError
        except TypeError:
            message = "%s: The list name must be a string" % cls.class_name
            print(message)
            return_value = None
        except ValueError:
            message = "%s: The list name '%s' does not exist" % (
                cls.class_name, list_name)
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
            message = "%s: Both arguments must be strings" % cls.class_name
            print(message)
            return_value = False
        except ValueError:
            message = "%s: Both arguments must exist" % cls.class_name
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
            message = "%s: Both arguments must be strings" % cls.class_name
            print(message)
            return_value = False
        except ValueError:
            message = "%s: There is no list named '%s'" % (
                cls.class_name, list_name)
            print(message)
            return_value = False
        else:
            entries = rs.GetDocumentData(list_name)
            return_value = (entry in entries)
            # print("%s: return_value: %s" % (cls.class_name, return_value))
        return return_value

