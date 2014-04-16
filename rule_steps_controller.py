#   rule_steps_controller.py

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
                self.respond_get_lshape_b_button),
            self.the_view.get_lshape_c_button: (
                self.respond_get_lshape_c_button)
        }
        self.lshape_names = [
            'a', 'b', 'a_minus_b', 'b_minus_a', 'c', 'c_prime']
        self._initialize_view()

    def _initialize_view(self):
        for lshape_name in self.lshape_names:
            self._initialize_canvas(lshape_name)
            self._initialize_text_var(lshape_name)

    def _initialize_canvas(self, lshape_name):  #   refactor
        self._display_lshape_on_canvas(lshape_name)

    def _initialize_text_var(self, lshape_name):    #   refactor
        text_var = self.the_view.text_vars[lshape_name]
        lshape = self.the_model.lshapes[lshape_name]
        text = lshape.listing()
        text_var.set(text)

        ####
    def respond(self, widget):
        if widget in self.responses:
            self.responses[widget]()

    def respond_get_lshape_a_button(self):
        self._update_model_lshape('a')
        self._recompute_model_lshape('a_minus_b')   #   refactor
        self._recompute_model_lshape('b_minus_a')
        self._recompute_model_lshape('c_prime')

    def respond_get_lshape_b_button(self):
        self._update_model_lshape('b')
        self._recompute_model_lshape('a_minus_b')
        self._recompute_model_lshape('b_minus_a')
        self._recompute_model_lshape('c_prime')

    def respond_get_lshape_c_button(self):
        self._update_model_lshape('c')
        self._recompute_model_lshape('c_prime')

    def _update_model_lshape(self, lshape_name):
        """Receives 'a', 'b', or 'c'
        """
        method_name = '_update_model_lshape'
        try:
            if not lshape_name.__class__ == str:
                raise TypeError
            elif not (
                lshape_name == 'a' or
                lshape_name == 'b' or
                lshape_name == 'c'
            ):
                raise ValueError
        except TypeError:
            message = 'The argument must be a string'
            self.__class__._print_error_message(method_name, message)
        except ValueError:
            message = "The argument must be 'a', 'b', or 'c'"
            self.__class__._print_error_message(method_name, message)
        else:
            obj_file = self.the_view.files[lshape_name]
            self.the_model.lshapes[lshape_name] = self.get_lshape_from(obj_file)
            self._display_lshape_on_canvas(lshape_name)
            text = self.the_model.lshapes[lshape_name].listing()
            self.the_view.text_vars[lshape_name].set(text)

    def _recompute_model_lshape(self, lshape_name):
        """Receives 'a_minus_b', 'b_minus_a', or 'c_prime'
        """
        method_name = '_recompute_model_lshape'
        try:
            if not lshape_name.__class__ == str:
                raise TypeError
            elif not (
                lshape_name == 'a_minus_b' or
                lshape_name == 'b_minus_a' or
                lshape_name == 'c_prime'
            ):
                raise ValueError
        except TypeError:
            message = 'The argument must be a string'
            self.__class__._print_error_message(method_name, message)
        except ValueError:
            message = '%s %s' % (
                "The argument must be 'a_minus_b',",
                "'b_minus_a', or 'c_prime'")
            self.__class__._print_error_message(method_name, message)
        else:
            if lshape_name == 'a_minus_b':
                new_lshape = self._subtract_lshapes('a', 'b')
                new_text = new_lshape.listing()
            elif lshape_name == 'b_minus_a':
                new_lshape = self._subtract_lshapes('b', 'a')
                new_lshape = (
                    self.the_model.lshapes['b'] - 
                    self.the_model.lshapes['a'])
                new_text = new_lshape.listing()
            elif lshape_name == 'c_prime':
                if self.the_model.lshapes['a'].is_a_sub_labeled_shape_of(
                    self.the_model.lshapes['c']
                ):
                    new_lshape = self._apply_rule_to_lshape('c', 'a', 'b')
                    new_text = new_lshape.listing()
                else:
                    new_lshape = labeled_shape.LabeledShape.new_empty()
                    new_text = 'A is not a part of C'
            else:
                print "Shouldn't have gotten here"
            self.the_model.lshapes[lshape_name] = new_lshape
            self._display_lshape_on_canvas(lshape_name)
            # new_text = self.the_model.lshapes[lshape_name].listing()
            self.the_view.text_vars[lshape_name].set(new_text)

    def _subtract_lshapes(self, lshape_a_name, lshape_b_name):
        """Receives the names of labeled shapes A and B:
            str, str
        Returns the labeled shape difference A - B:
            LabeledShape
        """
        lshape_a = self.the_model.lshapes[lshape_a_name]
        lshape_b = self.the_model.lshapes[lshape_b_name]
        lshape_diff = lshape_a - lshape_b
        return lshape_diff

    def _apply_rule_to_lshape(
            self, lshape_c_name, lshape_a_name, lshape_b_name
        ):
        """Receives names of the current labeled shape C, left labeled 
        shape A, and right labeled shape B:
            str, str, str
        Returns the next labeled shape C prime:
            LabeledShape
        """
        lshape_a = self.the_model.lshapes[lshape_a_name]
        lshape_b = self.the_model.lshapes[lshape_b_name]
        lshape_c = self.the_model.lshapes[lshape_c_name]
        new_lshape = (lshape_c - lshape_a) + lshape_b
        return new_lshape

        ####
    def get_lshape_from(self, obj_file):
        """Receives an obj_file:
            openfile
        Returns:
            LabeledShape
        """
        elements = self.extract_elements_from(obj_file)
        lines, lpoints = elements
        lshape = labeled_shape.LabeledShape.make_lshape_from(lines, lpoints)
        #   new_from_lines_and_lpoints
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
        self.extract_and_add_element(vertex_buffer, elements)
        #   explain why this is not in the loop
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

    def _display_lshape_on_canvas(self, lshape_name):
        lshape = self.the_model.lshapes[lshape_name]
        element_specs = lshape.get_element_specs()
        items = self.get_items_from(element_specs)
        canvas = self.the_view.canvases[lshape_name]
        self._display_items(items, canvas)

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
        d = 2                           #   where should this come from?
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
        offset_x = 5                    #   where should this come from?
        offset_y = 5
        x = lpoint_spec[0] + offset_x
        y = lpoint_spec[1] + offset_y
        label = lpoint_spec[2]
        text_item = (x, y, label)
        return text_item

    def _display_items(self, items, canvas):
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

    @classmethod
    def _print_error_message(cls, method_name, message):
        print '%s.%s: %s' % (cls.__name__, method_name, message)

if __name__ == '__main__':
    import doctest
    doctest.testfile('tests/rule_steps_controller_test.txt')
