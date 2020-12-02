import tkinter as tk
from tkinter.messagebox import showinfo     # pop up message


def clicked():
    button.configure(text='hey')
    showinfo('clicked','button clicked')

window = tk.Tk()
button = tk.Button(window, text='click me', bg='black',
                   fg='white', command=clicked)
button.grid(column=0, row=0)
window.mainloop()
