#   element_cell.py

import line

class ElementCell(object):
    """Consists of a non-empty (and unordered) iterable of elements of a single 
    ilk and type (colinear line or colabeled point). Immutable.
    """
        ### construct
    def __init__(self, elements):
        """Receives a list of elements (from a child class: LineCell or 
        LabeledPointCell)
        """
        pass

    def same_ilk(self, elements):
        ilk = elements[0].ilk
        for element in elements:
            if element.ilk != ilk:
                return False
        return True

        ### subtract

        ###
if __name__ == '__main__':
    import doctest
    doctest.testfile('tests/element_cell_test.txt')
