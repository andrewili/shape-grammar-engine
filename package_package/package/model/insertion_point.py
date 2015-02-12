import rhinoscriptsyntax as rs

class InsertionPoint(object):
    def __init__(self):
        pass

    @classmethod
    def get_insertion_point_from_user(cls):
        """Prompts the user for a point in the xy plane. Returns:
            Point3D
        """
        message1 = "Pick an insertion point in the xy plane"
        error_message = "%s %s" % (
            "The insertion point must be in the xy plane.",
            "Please try again")
        point = rs.GetPoint(message1)
        while not point[2] == 0:
            point = rs.GetPoint(error_message)
        return point
