#   shape_display_main.py

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
