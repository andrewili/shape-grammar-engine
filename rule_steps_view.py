#   rule_steps_view.py

import Tkinter as tk
import tkFileDialog
import tkFont
import ttk


class Observable(object):
    def __init__(self):
        self.observers = []

    def broadcast(self, widget):
        for observer in self.observers:
            observer.respond(widget)

    def add_observer(self, observer):
        self.observers.append(observer)


class View(tk.Toplevel, Observable):
    def __init__(self, master):
        tk.Toplevel.__init__(self, master)
        self.protocol('WM_DELETE_WINDOW', self.master.destroy)
        Observable.__init__(self)
        self.title('Rule steps 2014-04-03')
        self.text_var_a = tk.StringVar()
        self.text_var_b = tk.StringVar()
        self.text_var_a_minus_b = tk.StringVar()
        self.text_var_b_minus_a = tk.StringVar()
        self.label_width = 28
        self.label_height = 15
        self.label_font = ('Andale Mono', '11')
        self.background_color = '#EEEEEE'
        
        self._make_main_frame()
        self._make_label_frame_a(        0, 0)
        self._make_spacer(               1, 0)
        self._make_label_frame_b(        2, 0)
        self._make_spacer(               3, 0)
        # self._make_label_frame_buttons(  4, 0)
        # self._make_spacer(               5, 0)
        self._make_label_frame_a_minus_b(6, 0)
        self._make_spacer(               7, 0)
        self._make_label_frame_b_minus_a(8, 0)

    def _make_main_frame(self):
        self.mainframe = ttk.Frame(
            self,
            padding='10 10 10 10')
        self.mainframe.grid(
            column=0,
            row=0,
            sticky='NSEW')
        self.mainframe.rowconfigure(
            0,
            weight=1)
        self.mainframe.columnconfigure(
            0,
            weight=1)

    def _make_label_frame_a(self, column_in, row_in):
        self.label_frame_a = ttk.LabelFrame(
            self.mainframe)
        self.label_frame_a.grid(
            column=column_in,
            row=row_in,
            sticky='EW')
        self.canvas_a = self.make_canvas(
            self.label_frame_a,
            0, 0)
        self.get_lshape_a_button = ttk.Button(
            self.label_frame_a,
            width=15,
            text='Get A',
            command=(self.get_lshape_a))
        self.get_lshape_a_button.grid(
            column=0,
            row=2)
        self.label_a = tk.Label(
            self.label_frame_a,
            width=self.label_width,
            height=self.label_height,
            textvariable=self.text_var_a,
            anchor=tk.NW,
            justify=tk.LEFT,
            font=self.label_font)
        self.label_a.grid(
            column=0,
            row=3)

    def _make_label_frame_b(self, column_in, row_in):
        self.label_frame_b = ttk.LabelFrame(
            self.mainframe)
        self.label_frame_b.grid(
            column=column_in,
            row=row_in,
            sticky='EW')
        self.canvas_b = self.make_canvas(
            self.label_frame_b,
            0, 0)
        self.get_lshape_b_button = ttk.Button(
            self.label_frame_b,
            width=15,
            text='Get B',
            command=self.get_lshape_b)
        self.get_lshape_b_button.grid(
            column=0,
            row=2)
        self.label_b = tk.Label(
            self.label_frame_b,
            width=self.label_width,
            height=self.label_height,
            textvariable=self.text_var_b,
            anchor=tk.NW,
            justify=tk.LEFT,
            font=self.label_font)
        self.label_b.grid(
            column=0,
            row=3)

    def _make_label_frame_buttons(self, column_in, row_in):
        self.label_frame_buttons = ttk.LabelFrame(
            self.mainframe)
        self.label_frame_buttons.grid(
            column=column_in,
            row=row_in,
            sticky='NEW')
        self.result_button_frame_spacer_upper = tk.Label(
            self.label_frame_buttons,
            height=5,
            background=self.background_color)
        self.result_button_frame_spacer_upper.grid(
            column=0,
            row=0)
        self.get_lshape_a_plus_b_button = ttk.Button(
            self.label_frame_buttons,
            width=15,
            text='A + B',
            command=self.get_lshape_a_plus_b)
        self.get_lshape_a_plus_b_button.grid(
            column=0,
            row=1)
        self.get_lshape_a_minus_b_button = ttk.Button(
            self.label_frame_buttons,
            width=15,
            text='A - B',
            command=self.get_lshape_a_minus_b)
        self.get_lshape_a_minus_b_button.grid(
            column=0,
            row=2)
        self.get_lshape_a_sub_lshape_b_button = ttk.Button(
            self.label_frame_buttons,
            width=15,
            text='A <= B',
            command=self.get_lshape_a_sub_lshape_b)
        self.get_lshape_a_sub_lshape_b_button.grid(
            column=0,
            row=3)
        self.result_button_frame_spacer_lower = tk.Label(
            self.label_frame_buttons,
            height=17,
            background=self.background_color)
        self.result_button_frame_spacer_lower.grid(
            column=0,
            row=4)            

    def _make_label_frame_a_minus_b(self, column_in, row_in):
        self.label_frame_a_minus_b = ttk.LabelFrame(
            self.mainframe)
        self.label_frame_a_minus_b.grid(
            column=column_in,
            row=row_in,
            sticky='NEW')
        self.canvas_a_minus_b = self.make_canvas(
            self.label_frame_a_minus_b,
            0, 0)
        self.spacer_a_minus_b = tk.Label(
            self.label_frame_a_minus_b,
            width=2,
            background=self.background_color,
            text=' ')
        self.spacer_a_minus_b.grid(
            column=0,
            row=1)
        self.label_a_minus_b = tk.Label(
            self.label_frame_a_minus_b,
            width=self.label_width,
            height=self.label_height,
            textvariable=self.text_var_a_minus_b,
            anchor=tk.NW,
            justify=tk.LEFT,
            font=self.label_font)
        self.label_a_minus_b.grid(
            column=0,
            row=2)

    def _make_label_frame_b_minus_a(self, column_in, row_in):
        self.label_frame_b_minus_a = ttk.LabelFrame(
            self.mainframe)
        self.label_frame_b_minus_a.grid(
            column=column_in,
            row=row_in,
            sticky='NEW')
        self.canvas_b_minus_a = self.make_canvas(
            self.label_frame_b_minus_a,
            0, 0)
        self.spacer_b_minus_a = tk.Label(
            self.label_frame_b_minus_a,
            width=2,
            background=self.background_color,
            text=' ')
        self.spacer_b_minus_a.grid(
            column=0,
            row=1)
        self.label_b_minus_a = tk.Label(
            self.label_frame_b_minus_a,
            width=self.label_width,
            height=self.label_height,
            textvariable=self.text_var_b_minus_a,
            anchor=tk.NW,
            justify=tk.LEFT,
            font=self.label_font)
        self.label_b_minus_a.grid(
            column=0,
            row=2)

    def make_canvas(self, parent, column_in, row_in):
        canvas = tk.Canvas(
            parent,
            width=200,
            height=200,
            background='#DDDDDD')               #   use constant
        canvas.xview_moveto(0)                  #   move origin to visible area
        canvas.yview_moveto(0)
        canvas.grid(
            column=column_in,
            row=row_in,
            sticky='EW')
        return canvas

    def _make_spacer(self, column_in, row_in):
        self.spacer = tk.Label(
            self.mainframe,
            width=2,
            background=self.background_color,
            text=' ')
        self.spacer.grid(
            column=column_in,
            row=row_in)

##    def make_spacer_above_buttons(self, column_in, row_in):
##        spacer = tk.Label(
##            self.mainframe,
##            width=2,
##            height=5,
##            text=' ')
##        spacer.grid(
##            column=column_in,
##            row=row_in)

    def get_lshape_a(self):
        self.file_a = tkFileDialog.askopenfile()
        self.broadcast(self.get_lshape_a_button)

    def get_lshape_b(self):
        self.file_b = tkFileDialog.askopenfile()
        self.broadcast(self.get_lshape_b_button)

    def get_lshape_a_plus_b(self):
        self.broadcast(self.get_lshape_a_plus_b_button)

    def get_lshape_a_minus_b(self):
        self.broadcast(self.get_lshape_a_minus_b_button)

    def get_lshape_a_sub_lshape_b(self):
        self.broadcast(self.get_lshape_a_sub_lshape_b_button)


if __name__ == '__main__':
    import doctest
    doctest.testfile('tests/rule_steps_view_test.txt')
