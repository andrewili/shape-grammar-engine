#   shape_exporter_oo.py

import rhinoscriptsyntax as rs
import shape

class ShapeExporterOO(object):
    def __init__(self):
        pass

    def export_shape(self):
        the_shape = self._get_shape()
        self._write_is_file(the_shape)

    def _get_shape():
        """Prompts for elements (line and textdots) and a name. The shape may 
        not be empty. Returns the new shape:
            Shape
        """
        prompt_for_elements = ('Select the lines and textdots')
        guids = rs.GetObjects(
            prompt_for_elements,
            rs.filter.curve + rs.filter.textdot)

    def _write_is_file(self, shape):
        pass

if __name__ == '__main__':
    shape_exporter = ShapeExporterOO()
    shape_exporter.export_shape()
