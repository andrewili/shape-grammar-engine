#   shape_display_main.py

import shape_display_controller
import shape_display_model
import shape_display_view
import Tkinter as tk

if __name__ == '__main__':
    root = tk.Tk()
    root.withdraw()
    model = shape_display_model.Model()
    view = shape_display_view.View(root)
    controller = shape_display_controller.Controller(model, view)
    root.mainloop()
