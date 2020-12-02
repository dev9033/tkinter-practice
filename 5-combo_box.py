import tkinter as tk
from tkinter.ttk import *

window = tk.Tk()
combo = Combobox(window)
combo['values'] = (1,2,3,4,'txt')
combo.current(4)    # default selected item takes index value
combo.grid(column=0,row=0)

window.mainloop()