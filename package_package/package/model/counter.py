from package.model import dictionary as d
import rhinoscriptsyntax as rs

class Counter(object):
    def __init__(self):
        pass

    @classmethod                                ##  return boolean?
    def set_value(cls, counter_name, value_int):
        """Receives:
            counter_name    str
            value_int       int >= 0
        Sets the counter to the value. Returns:
            int >= 0        the new value, if successful
            None            otherwise
        """
        try:
            if not type(value_int) == int:
                raise TypeError
            elif not value_int >= 0:
                raise ValueError
        except TypeError:
            # message = "The value must be an integer"
            # print(message)
            return_value = None
        except ValueError:
            # message = "The value must be non-negative"
            # print(message)
            return_value = None
        else:
            dictionary_name = 'counters'
            value_str = str(value_int)
            value_was_set = d.Dictionary.set_value(
                dictionary_name, counter_name, value_str)
            if value_was_set:
                new_value_str = rs.GetDocumentData('counters', counter_name)
                new_value_int = int(new_value_str)
                return_value = new_value_int
            else:
                return_value = None
            return return_value

    @classmethod
    def get_value(cls, counter_name):
        """Receives:
            counter_name    str
        Returns:
            int >= 0        the value of the counter, if successful
            None            otherwise
        """
        try:
            counter_names = rs.GetDocumentData('counters')
            if not counter_name in counter_names:
                raise ValueError
        except ValueError:
            return_value = None
        else:
            value_str = rs.GetDocumentData('counters', counter_name)
            return_value = int(value_str)
            return return_value

    @classmethod
    def increment_value(cls, counter_name):
        """Receives:
            counter_name    str
        Increments the value. Returns:
            int             the new value, if successful
            None            otherwise
        """
        try:
            counter_names = d.Dictionary.get_keys('counters')
            if not counter_name in counter_names:
                raise ValueError
        except ValueError:
            return_value = None
        else:
            old_value_str = d.Dictionary.get_value('counters', counter_name)
            new_value_int = int(old_value_str) + 1
            new_value_str = str(new_value_int)
            new_value_str_set = d.Dictionary.set_value(
                'counters', counter_name, new_value_str)
            return_value = int(new_value_str_set)
            return return_value
