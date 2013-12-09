#   element_cell.py

import line

class ElementCell(object):
    """Consists of a non-empty (and unordered) iterable of elements of a single 
    tag and type (colinear line or colabeled point). Immutable.
    """
        ### construct
    def __init__(self, elements):
        """Receives a non-empty unsorted iterable of elements of a single tag 
        and type (i.e., colinear line or colabeled point):
            [cotagged_element, ...], n >= 1
        """
        try:
            if (len(elements) == 0 or
                not self.cotagged(elements)
            ):
                raise ValueError()
            else:
                self.elements = elements
        except ValueError:
            print '%s %s' % (
                "You're trying to make an element cell",
                "with non-cotagged elements or no elements")

    def cotagged(self, elements):
        tag = elements[0].tag
        for element in elements:
            if element.tag != tag:							#	element.tag!
                return False
        return True

        ### subtract

        ###
if __name__ == '__main__':
    import doctest
    doctest.testfile('tests/element_cell_test.txt')
