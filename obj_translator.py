#   obj_translator
#   2013-10-30

import sg_labeled_point
import sg_labeled_shape
import sg_line
import sg_point
import sg_shape

es = sg_shape.SGShape()
els = sg_labeled_shape.SGLabeledShape(es, {})

class ObjTranslator(object):
    @classmethod
    def get_lshape_from(cls, obj_file):                        # 1
        """Receives an obj_file:
            openfile
        Returns:
            SGLabeledShape
        """
        trace_on = True
        elements = cls.extract_elements_from(obj_file)         # 1.1
        lines, lpoints = elements
        lshape = els.make_lshape_from(lines, lpoints)
##        lshape = cls.els.make_lshape_from(lines, lpoints)
                                                                # 1.2
        if trace_on:
            method_name = 'ObjTranslator.get_lshape_from'
            line_strings = []
            for line in lines:
                line_strings.append(line.__str__())
            lines_listing = '[' + ', '.join(line_strings) + ']'
            print '||| %s.lines:\n%s' % (method_name, lines_listing)
        return lshape

    @classmethod
    def extract_elements_from(cls, obj_file):                  # 1.1
        """Receives an obj_file:
            openfile
        Extracts the SG elements from the obj_file and returns a 2-tuple:
            ([SGLine, ...], [SGLabeledPoint, ...])
        """
        elements = ([], [])
        vertex_buffer = []
        for file_line in obj_file:
            if cls.element_is_specified_by(file_line):         # 1.1.1
                if len(vertex_buffer) != 0:
                    cls.extract_and_add_element(vertex_buffer, elements)
                                                                # 1.1.2
                    vertex_buffer = []
            elif cls.vertex_is_specified_by(file_line):        # 1.1.3
                point = cls.extract_point_from(file_line)      # 1.1.4
                vertex_buffer.append(point)
            else:
                #   ignore other file_lines
                pass
        cls.extract_and_add_element(vertex_buffer, elements)   # 1.1.2
        return elements

    @classmethod
    def element_is_specified_by(cls, file_line):               # 1.1.1
        first_char = file_line[0]
        return first_char == 'o'

    @classmethod
    def extract_and_add_element(cls, vertex_buffer, elements): # 1.1.2
        """Receives a vertex_buffer and an element list 2-tuple:
            [SGPoint, ...]
            ([SGLine, ...], [SGLabeledPoint, ...])
        Extracts an element (SGLine or SGLabeledPoint) from the vertex buffer,
        and adds it to elements.
        """
        element = cls.extract_element_from(vertex_buffer)      # 1.1.2.1
        cls.add_element_to_elements(element, elements)         # 1.1.2.2

    @classmethod
    def extract_element_from(cls, vertex_buffer):              # 1.1.2.1
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

    @classmethod
    def add_element_to_elements(cls, element, elements):       # 1.1.2.2
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

    @classmethod
    def vertex_is_specified_by(cls, file_line):                # 1.1.3
        first_char = file_line[0]
        return first_char == 'v'

    @classmethod
    def extract_point_from(cls, file_line):                    # 1.1.4
        tokens = file_line.split(' ')
        x = float(tokens[1])
        y = float(tokens[2])
        return sg_point.SGPoint(x, y)

    @classmethod
    def display_lshape_on_canvas(cls, lshape, canvas):         # 2
        element_specs = lshape.get_element_specs()              # 2.1
        items = cls.get_items_from(element_specs)              # 2.2
        cls.display_items(items, canvas)                       # 2.3

    @classmethod
    def get_items_from(cls, element_specs):                    # 2.2
        """Receives a 2-tuple of lists of SG element_specs:
            ([(x1, y1, x2, y2), ...], [(x, y, label), ...])
        Returns a 3-tuple of lists of display items:
            (   [(x1, y1, x2, y2), ...],
                [(x1, y1, x2, y2), ...],
                [(x0, y0, text), ...])
        """
        line_specs, lpoint_specs = element_specs
        line_items = cls.get_line_items_from(line_specs)       # 2.2.1
        oval_items = cls.get_oval_items_from(lpoint_specs)     # 2.2.2
        text_items = cls.get_text_items_from(lpoint_specs)     # 2.2.3
        return (line_items, oval_items, text_items)

    @classmethod
    def get_line_items_from(cls, line_specs):                  # 2.2.1
        """Receives a list of SGLines:
            [SGLine, ...]
        Returns a list of line_items:
            [(x1, y1, x2, y2), ...]
        """
        line_items = []
        for line_spec in line_specs:
            line_items.append(line_spec)
        return line_items

    @classmethod
    def get_oval_items_from(cls, lpoint_specs):                # 2.2.2
        """Receives a list of. Returns a list of the corresponding
        oval items.
        """
        oval_items = []
        for lpoint_spec in lpoint_specs:
            oval_item = cls.get_oval_item_from(lpoint_spec)    # 2.2.2.1
            oval_items.append(oval_item)
        return oval_items

    @classmethod
    def get_oval_item_from(cls, lpoint_spec):                  # 2.2.2.1
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

    @classmethod
    def get_text_items_from(cls, lpoint_specs):                # 2.2.3
        """Receives a list of lpoint_specs:
            [(x, y, label), ...]
        Returns a list of the corresponding text items:
            [(x0, y0, label), ...]
        """
        text_items = []
        for lpoint_spec in lpoint_specs:
            text_item = cls.get_text_item_from(lpoint_spec)    # 2.2.3.1
            text_items.append(text_item)
        return text_items

    @classmethod
    def get_text_item_from(cls, lpoint_spec):                  # 2.2.3.1
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

    @classmethod
    def display_items(cls, items, canvas):                     # 2.3
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
