import point

class LabeledPoint(object):
    """Contains a Point and a label
    """
        ### construct
    def __init__(self, point_in, label):
        """Receives a Point and a (possibly empty) label:
            point_in        Point
            label           str. May be empty. Assume interpreter restrictions 
                            are enforced elsewhere
        Immutable
        """
        method_name = '__init__'
        try:
            if not (
                type(point_in) == point.Point and
                type(label) == str
            ):
                raise TypeError
        except TypeError:
            message = 'The arguments must be a Point and a string'
            self.__class__._print_error_message(method_name, message)
        else:
            self.point = point_in
            self.label = label
            self.x = self.point.x
            self.y = self.point.y
            self.z = self.point.z
            self.spec = (point_in.spec, label)  ##  != repr

    @classmethod
    def new_from_parts(cls, x, y, z=0, label=''):
        """Receives:
            x               num
            y               num
            z               num
            label           str
        Returns:
            LabeledPoint    ((x, y, z), label) if successful
            None            otherwise
        """
        method_name = 'new_from_parts'
        try:
            if not (
                cls._is_number(x) and
                cls._is_number(y) and
                cls._is_number(z) and
                type(label) == str
            ):
                raise TypeError
        except TypeError:
            message = "The arguments must be 3 numbers and a string"
            cls._print_error_message(method_name, message)
            return_value = None
        else:
            new_point = point.Point(x, y, z)
            new_lpoint = LabeledPoint(new_point, label)
            return_value = new_lpoint
        finally:
            return return_value

        ### represent
    def __str__(self):
        label_str = self._get_label_string()
        string = "(%s, %s)" % (self.point, label_str)
        return string

    def __repr__(self):
        point_str = str(self.point)
        label_str = self._get_label_string()
        string = "(%s, %s)" % (point_str, label_str)
        return string

    def _get_label_string(self):
        if self.label == '':
            label_str = "''"
        else:
            label_str = self.label
        return label_str

    def listing(self, decimal_places=0):
        point_listing = self.point.listing(decimal_places)
        if self.label == '':
            label_listing = "''"
        else:
            label_listing = str(self.label)
        string = '(%s, %s)' % (point_listing, label_listing)
        return string

    ### relations
    @classmethod
    def _is_number(cls, item):
        value = (
            item.__class__ == int or
            item.__class__ == float)
        return value

    def __eq__(self, other):
        if (self.point == other.point and
            self.label == other.label
        ):
            return True
        else:
            return False

    def __ge__(self, other):
        if self.point > other.point:
            return True
        elif self.point == other.point:
            if self.label > other.label:
                return True
            elif self.label == other.label:
                return True
            else:
                return False
        else:
            return False

    def __gt__(self, other):
        if self.point > other.point:
            return True
        elif self.point == other.point:
            if self.label > other.label:
                return True
            else:
                return False
        else:
            return False

    def __le__(self, other):
        if self.point < other.point:
            return True
        elif self.point == other.point:
            if self.label < other.label:
                return True
            if self.label == other.label:
                return True
            else:
                return False
        else:
            return False

    def __lt__(self, other):
        if self.point < other.point:
            return True
        elif self.point == other.point:
            if self.label < other.label:
                return True
            else:
                return False
        else:
            return False

    def __ne__(self, other):
        if (self.point != other.point or
            self.label != other.label
        ):
            return True
        else:
            return False

    ### other
    @classmethod
    def are_lpoint_specs(cls, items):
        """Receives:
            [item, ...]
        Returns:
            boolean         True, if each item is a labeled point spec
                            False, otherwise
        """
        value = True
        if not type(items) == list:
            value = False
        elif len(items) == 0:
            value = False
        else:
            for item in items:
                if not cls.is_lpoint_spec(item):
                    value = False
                    break
        return value

    @classmethod
    def is_lpoint_spec(cls, item):
        """Receives:
            item
        Returns:
            boolean         True, if item is an lpoint spec
                            False, otherwise
        """
        value = (
            len(item) == 2 and
            point.Point.is_a_spec(item[0]) and
            type(item[1]) == str)
        return value

    @classmethod
    def _print_error_message(cls, method_name, message):
        print '%s.%s:\n    %s' % (cls.__name__, method_name, message)

if __name__ == '__main__':
    import doctest
    doctest.testfile('tests/labeled_point_test.txt')
