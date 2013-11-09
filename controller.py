#   controller.py
#   2013-09-27

import model
import view
import sg_shape                                 #   for testing
import sg_labeled_point
import sg_labeled_shape
import sg_line                                  #   for testing
import sg_point                                 #   for testing

class Controller(object):
    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.view.add_observer(self)
        self.responses = {
            self.view.get_lshape_a_button: self.respond_get_lshape_a_button,
            self.view.get_lshape_b_button: self.respond_get_lshape_b_button,
            self.view.get_lshape_a_plus_b_button: (
                self.respond_get_a_plus_b_button),
            self.view.get_lshape_a_minus_b_button: (
                self.respond_get_a_minus_b_button),
            self.view.get_lshape_a_sub_lshape_b_button: (
                self.respond_get_a_sub_lshape_b_button)
        }
        self.es = sg_shape.SGShape()
        self.els = sg_labeled_shape.SGLabeledShape(self.es, {})

        ####
    def respond(self, widget):
        if widget in self.responses:
            self.responses[widget]()

    def respond_get_lshape_a_button(self):                      # root
        obj_file_a = self.view.file_a
        self.model.lshape_a = self.get_lshape_from(obj_file_a)
                                                                # 1
        self.display_lshape_on_canvas(
            self.model.lshape_a, self.view.canvas_a)            # 2
        text_a = self.model.lshape_a.listing()
        self.view.text_var_a.set(text_a)

    def respond_get_lshape_b_button(self):
        obj_file_b = self.view.file_b
        self.model.lshape_b = self.get_lshape_from(obj_file_b)
                                                                # 1
        self.display_lshape_on_canvas(
            self.model.lshape_b, self.view.canvas_b)            # 2
        text_b = self.model.lshape_b.listing()
        self.view.text_var_b.set(text_b)

    def respond_get_a_plus_b_button(self):
        self.model.lshape_c = \
            self.model.lshape_a + self.model.lshape_b
        self.display_lshape_on_canvas(
            self.model.lshape_c, self.view.canvas_c)            # 2
        text_c = self.model.lshape_c.listing()
        self.view.text_var_c.set(text_c)

    def respond_get_a_minus_b_button(self):
        self.model.lshape_c = \
            self.model.lshape_a - self.model.lshape_b
        self.display_lshape_on_canvas(
            self.model.lshape_c, self.view.canvas_c)            # 2
        text_c = self.model.lshape_c.listing()
        self.view.text_var_c.set(text_c)

    def respond_get_a_sub_lshape_b_button(self):
        empty_lshape = sg_labeled_shape.SGLabeledShape.new_empty()
        self.display_lshape_on_canvas(
            empty_lshape, self.view.canvas_c)                   # 2
        if self.model.lshape_a.is_a_sub_lshape_of(self.model.lshape_b):
            text_c = "A <= B: true"
        else:
            text_c = "A <= B: false"
        self.view.text_var_c.set(text_c)

        ####
    def get_lshape_from(self, obj_file):                        # 1
        """Receives an obj_file:
            openfile
        Returns:
            SGLabeledShape
        """
        elements = self.extract_elements_from(obj_file)         # 1.1
        lines, lpoints = elements
        lshape = self.els.make_lshape_from(lines, lpoints)
                                                                # 1.2
        return lshape

    def extract_elements_from(self, obj_file):                  # 1.1
        """Receives an obj_file:
            openfile
        Extracts the SG elements from the obj_file and returns a 2-tuple:
            ([SGLine, ...], [SGLabeledPoint, ...])
        """
        elements = ([], [])
        vertex_buffer = []
        for file_line in obj_file:
            if self.element_is_specified_by(file_line):         # 1.1.1
                if len(vertex_buffer) != 0:
                    self.extract_and_add_element(vertex_buffer, elements)
                                                                # 1.1.2
                    vertex_buffer = []
            elif self.vertex_is_specified_by(file_line):        # 1.1.3
                point = self.extract_point_from(file_line)      # 1.1.4
                vertex_buffer.append(point)
            else:
                #   ignore other file_lines
                pass
        self.extract_and_add_element(vertex_buffer, elements)   # 1.1.2
        return elements

    def element_is_specified_by(self, file_line):               # 1.1.1
        first_char = file_line[0]
        return first_char == 'o'

    def extract_and_add_element(self, vertex_buffer, elements): # 1.1.2
        """Receives a vertex_buffer and an element list 2-tuple:
            [SGPoint, ...]
            ([SGLine, ...], [SGLabeledPoint, ...])
        Extracts an element (SGLine or SGLabeledPoint) from the vertex buffer,
        and adds it to elements.
        """
        element = self.extract_element_from(vertex_buffer)      # 1.1.2.1
        self.add_element_to_elements(element, elements)         # 1.1.2.2

    def extract_element_from(self, vertex_buffer):              # 1.1.2.1
        """Receives a vertex_buffer:
            [SGPoint, ...]
        Returns:
            SGLabeledPoint (with default label), if the vertex contains 1 point.
            SGLine, if the buffer contains 2 points.
        """
        n = len(vertex_buffer)
        if n == 1:
            point = vertex_buffer[0]
            default_label = 'a'
            lpoint = sg_labeled_point.SGLabeledPoint(
                point.x, point.y, default_label)
            return lpoint
        elif n == 2:
            line = sg_line.SGLine(vertex_buffer[0], vertex_buffer[1])
            return line
        else:
            #   Shouldn't get here  #   Exception
            print 'extract_element_from():'
            print '    Vertex buffer must have 1 or 2 points'

    def add_element_to_elements(self, element, elements):       # 1.1.2.2
        """Receives an SGLine or SGLabeledPoint. Adds it to the appropriate list
        in the 2-tuple ([SGLine, ...], [SGLabeledPoint, ...]).
        """
        lines = elements[0]
        lpoints = elements[1]
        if type(element) == sg_line.SGLine:
            lines.append(element)
        elif type(element) == sg_labeled_point.SGLabeledPoint:
            lpoints.append(element)
        else:
            #   Shouldn't get here
            print 'add_element_to_elements(): element must be SGLine or SGLabeledPoint'

    def vertex_is_specified_by(self, file_line):                # 1.1.3
        first_char = file_line[0]
        return first_char == 'v'

    def extract_point_from(self, file_line):                    # 1.1.4
        tokens = file_line.split(' ')
        x = float(tokens[1])
        y = float(tokens[2])
        return sg_point.SGPoint(x, y)

    def display_lshape_on_canvas(self, lshape, canvas):         # 2
        element_specs = lshape.get_element_specs()              # 2.1
        items = self.get_items_from(element_specs)              # 2.2
        self.display_items(items, canvas)                       # 2.3

    def get_items_from(self, element_specs):                    # 2.2
        """Receives a 2-tuple of lists of SG element_specs:
            ([(x1, y1, x2, y2), ...], [(x, y, label), ...])
        Returns a 3-tuple of lists of display items:
            (   [(x1, y1, x2, y2), ...],
                [(x1, y1, x2, y2), ...],
                [(x0, y0, text), ...])
        """
        line_specs, lpoint_specs = element_specs
        line_items = self.get_line_items_from(line_specs)       # 2.2.1
        oval_items = self.get_oval_items_from(lpoint_specs)     # 2.2.2
        text_items = self.get_text_items_from(lpoint_specs)     # 2.2.3
        return (line_items, oval_items, text_items)

    def get_line_items_from(self, line_specs):                  # 2.2.1
        """Receives a list of SGLines:
            [SGLine, ...]
        Returns a list of line_items:
            [(x1, y1, x2, y2), ...]
        """
        line_items = []
        for line_spec in line_specs:
            line_items.append(line_spec)
        return line_items

    def get_oval_items_from(self, lpoint_specs):                # 2.2.2
        """Receives a list of. Returns a list of the corresponding
        oval items.
        """
        oval_items = []
        for lpoint_spec in lpoint_specs:
            oval_item = self.get_oval_item_from(lpoint_spec)    # 2.2.2.1
            oval_items.append(oval_item)
        return oval_items

    def get_oval_item_from(self, lpoint_spec):                  # 2.2.2.1
        """Receives an lpoint_spec:
            (x, y, label)
        Returns a 4-tuple of the corresponding oval item's coordinates:
            (x0, y0, x1, y1).
        """
        x = lpoint_spec[0]
        y = lpoint_spec[1]
        d = 2                                   #   where should this come from?
        r = d / 2
        x0 = x - r
        y0 = y - r
        x1 = x + r
        y1 = y + r
        oval_item = (x0, y0, x1, y1)
        return oval_item

    def get_text_items_from(self, lpoint_specs):                # 2.2.3
        """Receives a list of lpoint_specs:
            [(x, y, label), ...]
        Returns a list of the corresponding text items:
            [(x0, y0, label), ...]
        """
        text_items = []
        for lpoint_spec in lpoint_specs:
            text_item = self.get_text_item_from(lpoint_spec)    # 2.2.3.1
            text_items.append(text_item)
        return text_items

    def get_text_item_from(self, lpoint_spec):                  # 2.2.3.1
        """Receives a labeled_point_spec
            (x, y, label)
        Returns a text item
            (x0, y0, label)
        """
        offset_x = 5                           #   where should this come from?
        offset_y = 5
        x = lpoint_spec[0] + offset_x
        y = lpoint_spec[1] + offset_y
        label = lpoint_spec[2]
        text_item = (x, y, label)
        return text_item

    def display_items(self, items, canvas):                     # 2.3
        """Receives a 3-tuple of lists of display items (lines, ovals, texts):
            (   [(x1, y1, x2, y2), ...],
                [(x1, y1, x2, y2), ...],
                [(x0, y0, text), ...])
        Displays the items on the canvas.
        """
        canvas.delete('all')
        line_items, oval_items, text_items = items
        for line_item in line_items:
            canvas.create_line(line_item)
        for oval_item in oval_items:
            canvas.create_oval(oval_item, fill='black', outline='')
        for text_item in text_items:
            x, y, label = text_item
            canvas.create_text(x, y, text=label)

        ####                                    #   the methods below are needed 
                                                #   only for testing
    def make_ells(self):
        """
        _|   |_       ___       _|___|_
                     |   |       |   |
           X     +   |   |   =   | X |
        _     _      |___|      _|___|_
         |   |                   |   |
        """
##        es = sg_shape.SGShape()
        line0414 = self.make_line(10, 74, 26, 74)
        line0111 = self.make_line(10, 26, 26, 26)
        line1011 = self.make_line(26, 10, 26, 26)
        line1415 = self.make_line(26, 74, 26, 90)
        line4041 = self.make_line(74, 10, 74, 26)
        line4151 = self.make_line(74, 26, 90, 26)
        line4445 = self.make_line(74, 74, 74, 90)
        line4454 = self.make_line(74, 74, 90, 74)
        ells_lines = [line1011, line1415, line4041, line4445,
                      line0111, line4151, line0414, line4454]
        lpoint33X = self.make_lpoint(50, 50, 'X')
        ells_points = [lpoint33X]
        ells = self.es.make_shape_from(ells_lines, ells_points)
        return ells

    def make_point(self, x, y):
        return sg_point.SGPoint(x, y)

    def make_lpoint(self, x, y, label):
        return sg_point.SGPoint(x, y, label)

    def make_line(self, x1, y1, x2, y2):
        p1 = self.make_point(x1, y1)
        p2 = self.make_point(x2, y2)
        return sg_line.SGLine(p1, p2)

    def make_line_pp(self, p1, p2):
        return sg_line.SGLine(p1, p2)

    def make_square(self):
##        es = sg_shape.SGShape()
        line1114 = self.make_line(26, 26, 26, 74)
        line1141 = self.make_line(26, 26, 74, 26)
        line1444 = self.make_line(26, 74, 74, 74)
        line4144 = self.make_line(74, 26, 74, 74)
        square_lines = [line1114, line1141, line1444, line4144]
        square_points = []
        square = self.es.make_shape_from(square_lines, square_points)
        return square


if __name__ == '__main__':
    import doctest
    doctest.testfile('controller_test.txt')