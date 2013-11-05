#   shape_display_main.py
#   2013-10-04
#   Continues 2013-09-18
#   Starting shape subtraction

import controller
import model
import Tkinter as tk
import view

if __name__ == '__main__':
    root = tk.Tk()
    root.withdraw()
    model = model.Model()
    view = view.View(root)
    controller = controller.Controller(model, view)
    root.mainloop()
