# from package.model import point
import point

class Triangle(object):
    def __init__(self, p1, p2, p3):
        """Receives:
            p1              Point
            p2              Point
            p3              Point. p1, p2, and p3 are not collinear 
        """
        method_name = '__init__'
        try:
            if not (
                p1.__class__ == point.Point and
                p2.__class__ == point.Point and
                p3.__class__ == point.Point
            ):
                raise TypeError
            elif self.__class__._points_are_collinear(p1, p2, p3):
                raise ValueError
            else:
                pass
        except TypeError:
            # message = 'Type error'
            message = 'The arguments must all be Point objects'
            self.__class__._print_error_message(method_name, message)
        except ValueError:
            # message = 'Value error'
            message = 'The points must not be collinear'
            self.__class__._print_error_message(method_name, message)
        else:
            print('success')

    @classmethod
    def _points_are_collinear(cls, p1, p2, p3):
        value = True
        # d12 = p2 - p1
        # d13 = p3 - p1
        # d23 = p3 - p2
        # if (d12 == d13 + d23 or
        #     d13 == d12 + d23 or
        #     d23 == d12 + d13
        # ):
        #     value = True
        # else:
        #     value = False
        return value

    @classmethod
    def new(cls, point_triple):
        """Receives:
            point_triple    (Point, Point, Point)
        Returns:
            triangle        Triangle
        """
        pass

    @classmethod
    def _print_error_message(cls, method_name, message):
        print '%s.%s:\n    %s' % (cls.__name__, method_name, message)

if __name__ == '__main__':
    import doctest
    doctest.testfile('tests/triangle_test.txt')
