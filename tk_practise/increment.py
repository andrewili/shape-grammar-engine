#	increment.py

from Tkinter import *
import ttk


def increment(*args):
	value = int(number_label['text'])
	value += 1
	number.set(value)

root = Tk()
root.title('Increment')

mainframe = ttk.Frame(root, padding='5 5 5 5')
mainframe.grid(column=1, row=1, sticky=(N, E, S, W))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)

value = 0
number = StringVar()
number.set(value)
number_label = ttk.Label(mainframe, textvariable=number)
number_label.grid(column=1, row=1, sticky=(E, W))

increment_button = ttk.Button(mainframe, text='Increment!', command=increment)
increment_button.grid(column=1, row=2, sticky=(E, W))

for child in mainframe.winfo_children():
	child.grid_configure(padx=0, pady=0)

root.bind('<Return>', increment)

root.mainloop()
