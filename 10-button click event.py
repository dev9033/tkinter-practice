import tkinter as tk

window = tk.Tk()
def say_hi():
    tk.Label(window,text='hi').pack()

tk.Button(window,text='click me',command = say_hi).pack()
window.mainloop()