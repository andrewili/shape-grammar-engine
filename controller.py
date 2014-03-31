#   controller.py

import model
import view
import shape                                    #   for testing
import labeled_point
import labeled_shape
import line                                     #   for testing
import point                                    #   for testing

class Controller(object):
    def __init__(self, model_in, view_in):
        self.the_model = model_in
        self.the_view = view_in
        self.the_view.add_observer(self)
        self.responses = {
            self.the_view.get_lshape_a_button: (
                self.respond_get_lshape_a_button),
            self.the_view.get_lshape_b_button: (
                self.respond_get_lshape_b_button)
            # ,
            # self.the_view.get_lshape_a_plus_b_button: (
            #     self.respond_get_a_plus_b_button),
            # self.the_view.get_lshape_a_minus_b_button: (
            #     self.respond_get_a_minus_b_button),
            # self.the_view.get_lshape_a_sub_lshape_b_button: (
            #     self.respond_get_a_sub_lshape_b_button)
        }

        ####
    def respond(self, widget):
        if widget in self.responses:
            self.responses[widget]()

    def respond_get_lshape_a_button(self):
        obj_file_a = self.the_view.file_a
        self.the_view.lshape_a = self.get_lshape_from(obj_file_a)   #   view.lshape_a is set
        self.display_lshape_on_canvas(
            self.the_view.lshape_a, self.the_view.canvas_a)
        text_a = self.the_view.lshape_a.listing()
        self.the_view.text_var_a.set(text_a)

    def respond_get_lshape_b_button(self):
        obj_file_b = self.the_view.file_b
        self.the_view.lshape_b = self.get_lshape_from(obj_file_b)
        self.display_lshape_on_canvas(
            self.the_view.lshape_b, self.the_view.canvas_b)
        text_b = self.the_view.lshape_b.listing()
        self.the_view.text_var_b.set(text_b)

    def respond_get_a_plus_b_button(self):
        self.the_view.lshape_c = (
            self.the_view.lshape_a + self.the_view.lshape_b)
        self.display_lshape_on_canvas(
            self.the_view.lshape_c, self.the_view.canvas_c)
        text_c = self.the_view.lshape_c.listing()
        self.the_view.text_var_c.set(text_c)

    def respond_get_a_minus_b_button(self):
        trace_on = False
        if trace_on:
            method_name = 'Controller.respond_get_a_minus_b_button()'
            print '||| %s' % method_name
        self.the_view.lshape_c = (
            self.the_view.lshape_a - self.the_view.lshape_b)    #   Trouble here!
        if trace_on:
            print '||| %s' % method_name
            print 'self.the_view.lshape_a:'
            print self.the_view.lshape_a.listing()
            print 'self.the_view.lshape_b:'
            print self.the_view.lshape_b.listing()
            print 'self.the_view.lshape_c:'
            print self.the_view.lshape_c.listing()
        self.display_lshape_on_canvas(
            self.the_view.lshape_c, self.the_view.canvas_c)
        text_c = self.the_view.lshape_c.listing()
        self.the_view.text_var_c.set(text_c)

    def respond_get_a_sub_lshape_b_button(self):
        empty_lshape = labeled_shape.LabeledShape.new_empty()
        self.display_lshape_on_canvas(
            empty_lshape, self.the_view.canvas_c)
        if self.the_view.lshape_a.is_a_sub_labeled_shape_of(
            self.the_view.lshape_b
        ):
            text_c = "A <= B: true"
        else:
            text_c = "A <= B: false"
        self.the_view.text_var_c.set(text_c)

        ####
    def get_lshape_from(self, obj_file):
        """Receives an obj_file:
            openfile
        Returns:
            LabeledShape
        """
        elements = self.extract_elements_from(obj_file)
        lines, lpoints = elements
        lshape = labeled_shape.LabeledShape.make_lshape_from(lines, lpoints)    #   new_from_lines_and_lpoints
        return lshape

    def extract_elements_from(self, obj_file):
        """Receives an obj_file:
            openfile
        Extracts the SG elements from the obj_file and returns a 2-tuple:
            ([Line, ...], [LabeledPoint, ...])
        """
        elements = ([], [])
        vertex_buffer = []
        for file_line in obj_file:
            if self.element_is_specified_by(file_line):
                if len(vertex_buffer) != 0:
                    self.extract_and_add_element(vertex_buffer, elements)
                    vertex_buffer = []
            elif self.vertex_is_specified_by(file_line):
                new_point = self.extract_point_from(file_line)
                vertex_buffer.append(new_point)
            else:
                #   ignore other file_lines
                pass
        self.extract_and_add_element(vertex_buffer, elements)                   #   explain why this is not in the loop
        return elements

    def element_is_specified_by(self, file_line):
        first_char = file_line[0]
        return first_char == 'o'

    def extract_and_add_element(self, vertex_buffer, elements):
        """Receives a vertex_buffer and an element list 2-tuple:
            [Point, ...]
            ([Line, ...], [LabeledPoint, ...])
        Extracts an element (Line or LabeledPoint) from the vertex buffer,
        and adds it to elements.
        """
        element = self.extract_element_from(vertex_buffer)
        self.add_element_to_elements(element, elements)

    def extract_element_from(self, vertex_buffer):
        """Receives a vertex_buffer:
            [Point, ...]
        Returns:
            LabeledPoint (with default label), if the vertex contains 1 point.
            Line, if the buffer contains 2 points.
        """
        n = len(vertex_buffer)
        if n == 1:
            new_point = vertex_buffer[0]
            default_label = 'a'
            lpoint = labeled_point.LabeledPoint(
                new_point.x, new_point.y, default_label)
            return lpoint
        elif n == 2:
            new_line = line.Line(vertex_buffer[0], vertex_buffer[1])
            return new_line
        else:
            #   Shouldn't get here  #   Exception
            print 'extract_element_from():'
            print '    Vertex buffer must have 1 or 2 points'

    def add_element_to_elements(self, element, elements):
        """Receives a Line or LabeledPoint. Adds it to the appropriate list
        in the 2-tuple ([Line, ...], [LabeledPoint, ...]).
        """
        lines = elements[0]
        lpoints = elements[1]
        if type(element) == line.Line:
            lines.append(element)
        elif type(element) == labeled_point.LabeledPoint:
            lpoints.append(element)
        else:
            #   Shouldn't get here
            print 'add_element_to_elements(): element must be Line or LabeledPoint'

    def vertex_is_specified_by(self, file_line):
        first_char = file_line[0]
        return first_char == 'v'

    def extract_point_from(self, file_line):
        tokens = file_line.split(' ')
        x = float(tokens[1])
        y = float(tokens[2])
        return point.Point(x, y)

    def display_lshape_on_canvas(self, lshape, canvas):
        element_specs = lshape.get_element_specs()
        items = self.get_items_from(element_specs)
        self.display_items(items, canvas)

    def get_items_from(self, element_specs):
        """Receives a 2-tuple of lists of SG element_specs:
            ([(x1, y1, x2, y2), ...], [(x, y, label), ...])
        Returns a 3-tuple of lists of display items:
            (   [(x1, y1, x2, y2), ...],
                [(x1, y1, x2, y2), ...],
                [(x0, y0, text), ...])
        """
        line_specs, lpoint_specs = element_specs
        line_items = self.get_line_items_from(line_specs)
        oval_items = self.get_oval_items_from(lpoint_specs)
        text_items = self.get_text_items_from(lpoint_specs)
        return (line_items, oval_items, text_items)

    def get_line_items_from(self, line_specs):
        """Receives a list of Lines:
            [Line, ...]
        Returns a list of line_items:
            [(x1, y1, x2, y2), ...]
        """
        line_items = []
        for line_spec in line_specs:
            line_items.append(line_spec)
        return line_items

    def get_oval_items_from(self, lpoint_specs):
        """Receives a list of. Returns a list of the corresponding
        oval items.
        """
        oval_items = []
        for lpoint_spec in lpoint_specs:
            oval_item = self.get_oval_item_from(lpoint_spec)
            oval_items.append(oval_item)
        return oval_items

    def get_oval_item_from(self, lpoint_spec):
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

    def get_text_items_from(self, lpoint_specs):
        """Receives a list of lpoint_specs:
            [(x, y, label), ...]
        Returns a list of the corresponding text items:
            [(x0, y0, label), ...]
        """
        text_items = []
        for lpoint_spec in lpoint_specs:
            text_item = self.get_text_item_from(lpoint_spec)
            text_items.append(text_item)
        return text_items

    def get_text_item_from(self, lpoint_spec):
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

    def display_items(self, items, canvas):
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

if __name__ == '__main__':
    import doctest
    doctest.testfile('tests/controller_test.txt')
