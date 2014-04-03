#   rule_steps_main.py

import rule_steps_controller as controller
import rule_steps_model as model
import rule_steps_view as view
import Tkinter as tk

if __name__ == '__main__':
    root = tk.Tk()
    root.withdraw()
    model = model.Model()
    view = view.View(root)
    controller = controller.Controller(model, view)
    root.mainloop()
