#   ledger.py

# import rhinoscriptsyntax as rs

class Ledger(object):
    def __init__(self, elements_in):
        """Receives a list of elements, e.g., coords or coord index 
        pairs
        self.elements is an ordered list of unique elements
        """
        self.elements = []
        for element in elements_in:
            if not self.elements.__contains__(element):
                self.elements.append(element)
        self.elements = sorted(self.elements)

    def get_element(self, index):
        element = self.elements[index]
        return element

    def get_index(self, element):
        index = self.elements.index(element)
        return index

if __name__ == '__main__':
    import doctest
    doctest.testfile('tests/ledger_test.txt')
