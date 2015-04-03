import point

class LabeledPoint(object):
    """Contains a Point and a label
    """
        ### construct
    def __init__(self, point_in, label):        ##  04-03 09:13
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
                label.__class__ == str
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
            self.spec = (point_in.spec, label)

    # @classmethod
    # def new_from_parts(cls, x, y, z=0, label):
    #     pass

        ### represent
    def __str__(self):
        if self.label == '':
            label_str = "''"
        else:
            label_str = self.label
        string = "(%s, %s)" % (self.point, label_str)
        return string

    def listing(self, decimal_places=0):        ##  04-03 09:55
        point_listing = self.point.listing(decimal_places)
        point_formatted = point_listing[1:-1]
        string = '(%s, %s)' % (point_formatted, self.label)
        return string

        ### relations
    @classmethod
    def are_lpoint_specs(cls, elements):
        """Receives a list of elements:
            [element, ...]
        Returns whether each element is a labeled point spec
        """
        value = True
        for element in elements:
            if not cls.is_lpoint_spec(element):
                value = False
                break
        return value

    @classmethod
    def is_lpoint_spec(cls, elements):
        value = (
            elements.__class__ == tuple and
            len(elements) == 3 and
            cls._is_number(elements[0]) and
            cls._is_number(elements[1]) and
            elements[2].__class__ == str)
        return value

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
    def _print_error_message(cls, method_name, message):
        print '%s.%s: %s' % (cls.__name__, method_name, message)

if __name__ == '__main__':
    import doctest
    doctest.testfile('tests/labeled_point_test.txt')
