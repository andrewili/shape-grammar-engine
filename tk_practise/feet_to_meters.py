#	feet_to_meters.py

from Tkinter import *
import ttk

def convert(*args):
	try:
		value = float(feet.get())
		meters.set((0.3048 * value * 10000.0 + 0.5)/10000.0)
	except ValueError:
		pass

root = Tk()
root.title('Feet to meters')

mainframe = ttk.Frame(root, padding='3 3 12 12')
mainframe.grid(column=1, row=1, sticky=(N, E, W, S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)

feet = StringVar()
meters = StringVar()

feet_entry = ttk.Entry(mainframe, width=5, textvariable=feet)
feet_entry.grid(column=2, row=1, sticky=(E, W))

feet_string_label = ttk.Label(mainframe, text='feet')
feet_string_label.grid(column=3, row=1, sticky=W)

equals_string_label = ttk.Label(mainframe, text='equals')
equals_string_label.grid(column=1, row=2, sticky=E)

meters_label = ttk.Label(mainframe, textvariable=meters)
meters_label.grid(column=2, row=2, sticky=(E, W))

meters_string_label = ttk.Label(mainframe, text='meters')
meters_string_label.grid(column=3, row=2, sticky=W)

go_button = ttk.Button(mainframe, text='Go!', command=convert)
go_button.grid(column=3, row=3, sticky=W)

for child in mainframe.winfo_children():
	child.grid_configure(padx=5, pady=5)

feet_entry.focus()
root.bind('<Return>', convert)

root.mainloop()
