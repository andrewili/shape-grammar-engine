#   sg_column.py

import sg_line

def SGColumn(object):
    def __init__(self, lines):
        """Receives an unordered list of non-maximal collinear lines:
            [SGLine, ...]
        """
        #   empty list error
        try:
            if self.not_collinear(lines):
                raise ValueError()
        except ValueError:
            print "You're trying to make a column with non-collinear lines"

    def not_collinear(self, lines):
        carrier = lines[0].carrier
        for line in lines:
            if line.carrier != carrier:
                return True
        return False


if __name__ == '__main__':
    import doctest
    doctest.testfile('tests/sg_column_test.txt')
