#   sg_colabeling.py

class SGColabeling(object):
    """Contains a non-empty set of colabeled points:
        set([SGLabeledPoint, ...]), n >= 1
    """
    ### construct
    def __init__(self, lpoints_in):
        """Receives a non-empty unsorted list of colabeled points:
            [SGLabeledPoint, ...], n >= 1
        """
        try:
            if (len(lpoints_in) == 0 or
                not self.colabeled(lpoints_in)
            ):
                raise ValueError()
            else:
                self.lpoints = set(lpoints_in)
        except ValueError:
            print '%s %s' % (
                "You're trying to make a colabeling",
                "with non-colabeled points or no points")

    def colabeled(self, lpoints_in):
        """Receives a non-empty list of labeled points:
            [SGLabeledPoint, ...], n >= 1
        Returns whether the labeled points all have the same label
        """
        label = lpoints_in[0].label
        for lpoint in lpoints_in:
            if label != lpoint.label:
                return False
        return True

    ### represent
    def __str__(self):
        """Returns the string of the ordered list of colabeled points in the 
        form:
            [(x, y, label), ...]
        """
        point_strings = []
        for lpoint in sorted(self.lpoints):
            point_strings.append(lpoint.point.__str__())
        points_string = ', '.join(point_strings)
        colabeling_string = '[%s]' % points_string
        return colabeling_string

    def listing(self, indent_level=0):
        """Returns an ordered, formatted, multi-line string in the form:
            label:
                (x, y)
                ...
        """
        indent_increment = 4
        if indent_level < 0:
            indent_level = 0
        indent_string = ' ' * indent_level * indent_increment
        lpoint_listings = []
        for lpoint in sorted(self.lpoints):
            lpoint_listings.append(indent_string + lpoint.point.listing())
        colabeling_listing = '\n'.join(lpoint_listings)
        return colabeling_listing

    ### compare
    def __eq__(self, other):
        return self.lpoints == other.lpoints

    def __ne__(self, other):
        return self.lpoints != other.lpoints

    ###
    def add(self, lpoint):
        """Receives a labeled point: 
            SGLabeledPoint
        Adds the labeled point to the set
        """
        self.lpoints.add(lpoint)

if __name__ == '__main__':
    import doctest
    doctest.testfile('tests/sg_colabeling_test.txt')
