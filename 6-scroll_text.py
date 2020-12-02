import tkinter as tk
from tkinter import scrolledtext


window = tk.Tk()
txt = scrolledtext.ScrolledText(window,width =40, height = 10)
txt.grid(column=0, row=0)


window.mainloop()
