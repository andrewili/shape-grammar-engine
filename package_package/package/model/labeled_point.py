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
        Immutable?
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
            self._print_error_message(method_name, message)
        else:
            self.p = point_in
            self.label = label
            self.x = self.p.x
            self.y = self.p.y
            self.z = self.p.z
            self.spec = (self.x, self.y, self.z, self.label)

    @classmethod
    def from_parts(cls, x, y, z, label=''):
        """Receives:
            x, y, z         num
            label           str
        Returns:
            new_lpoint      LabeledPoint. If successful. Otherwise None
        """
        method_name = 'from_parts'
        try:
            if not (
                cls._is_a_number(x) and
                cls._is_a_number(y) and
                cls._is_a_number(z) and
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
        """Returns:
            string          str. In the form "(0, 0, 0, 'a')"
        """
        label_str = self._get_label_string()
        string = '(%s, %s, %s, %s)' % (self.x, self.y, self.z, label_str)
        return string

    def __repr__(self):
        """Returns:
            string          str. In the form "((0, 0, 0), 'a')"
        """
        point_str = str(self.p)
        label_str = self._get_label_string()
        string = '(%s, %s)' % (point_str, label_str)
        return string

    def listing(self, decimal_places=0):
        """Creates a formatted string. The label is in single quotes. Returns:
            lp_listing      str. In the form "(0.0, 0.0, 0.0, 'a')"
        """
        p_listing = self.p.listing(decimal_places)
        coords_listing = p_listing[1:-1]
        label_listing = self._get_label_string()
        lp_listing = "(%s, %s)" % (coords_listing, label_listing)
        return lp_listing

    def _get_label_string(self):
        """Returns:
            string          str. In the form 'a'
        """
        string = "'%s'" % self.label
        return string

    ### relations
    @classmethod
    def _is_a_number(cls, item):
        value = (
            type(item) == int or
            type(item) == float)
        return value

    def __eq__(self, other):
        if (self.p == other.p and
            self.label == other.label
        ):
            return True
        else:
            return False

    def __ge__(self, other):
        if self.p > other.p:
            return True
        elif self.p == other.p:
            if self.label > other.label:
                return True
            elif self.label == other.label:
                return True
            else:
                return False
        else:
            return False

    def __gt__(self, other):
        if self.p > other.p:
            return True
        elif self.p == other.p:
            if self.label > other.label:
                return True
            else:
                return False
        else:
            return False

    def __le__(self, other):
        if self.p < other.p:
            return True
        elif self.p == other.p:
            if self.label < other.label:
                return True
            if self.label == other.label:
                return True
            else:
                return False
        else:
            return False

    def __lt__(self, other):
        if self.p < other.p:
            return True
        elif self.p == other.p:
            if self.label < other.label:
                return True
            else:
                return False
        else:
            return False

    def __ne__(self, other):
        if (self.p != other.p or
            self.label != other.label
        ):
            return True
        else:
            return False

    def __hash__(self):
        """Returns:
            value           int
        """
        p_hash = hash(self.p)
        label_hash = hash(self.label)
        duple = (p_hash, label_hash)
        value = hash(duple)
        return value

    ### other
    @classmethod
    def are_lpoint_specs(cls, items):
        """Receives:
            items           [item]. A non-empty list of elements of any type
        Returns:
            boolean         True, if each item is a labeled point spec
                            False, otherwise
        """
        value = True
        if not type(items) == list:
            value = False
        elif items == []:
            value = False
        else:
            for item in items:
                if not cls.is_an_lpoint_spec(item):
                    value = False
                    break
        return value

    @classmethod
    def is_an_lpoint_spec(cls, item):
        """Receives:
            item            any type
        Returns:
            boolean         True, if item is an lpoint spec
                            False, otherwise
        """
        value = (
            type(item) == tuple and
            len(item) == 4 and
            cls._is_a_number(item[0]) and
            cls._is_a_number(item[1]) and
            cls._is_a_number(item[2]) and
            type(item[3]) == str)
        return value

    @classmethod
    def _print_error_message(cls, method_name, message):
        print '%s.%s:\n    %s' % (cls.__name__, method_name, message)

if __name__ == '__main__':
    import doctest
    doctest.testfile('tests/labeled_point_test.txt')
