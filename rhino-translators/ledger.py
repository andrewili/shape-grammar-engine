#   ledger.py

# import rhinoscriptsyntax as rs

class Ledger(object):
    def __init__(self):
        self.elements = []

    # def __init__(self, elements_in):
    #     """Receives a list of elements, e.g., coords or coord index 
    #     pairs
    #     self.elements is an ordered list of unique elements
    #     """
    #     self.elements = []
    #     for element in elements_in:
    #         if not element in self.elements:
    #             self.elements.append(element)
    #     self.elements = sorted(self.elements)
    #     print('elements_in   : %s' % elements_in)
    #     print('self.elements : %s' % self.elements)

    def complete_as_coord_ledger(self):
        """Receives a list of line Guids:
            [Guid, ...]
        Extracts line coords and puts them (without duplicates) in 
        self.elements:
            [(num, num, num), ...]
        """
        coords = []
        for line in lines:
            points = rs.CurvePoints(line)
            for p in points:
                coord = (p.X, p.Y, p.Z)
                if not coord in coords:
                    coords.append(coord)
        self.elements = sorted(coords)
        print('coord ledger: %s' % self.elements)

    def complete_as_line_ledger(self, lines):
        """Receives a list of line Guids:
            [Guid, ...]
        Extracts line coord indices and puts them in elements
            [(int, int), ...]
        """
        pass

    def get_element(self, index):
        element = self.elements[index]
        return element

    def get_index(self, element):
        index = self.elements.index(element)
        return index

if __name__ == '__main__':
    import doctest
    doctest.testfile('tests/ledger_test.txt')
