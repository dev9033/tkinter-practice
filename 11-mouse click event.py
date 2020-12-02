import tkinter as tk

window = tk.Tk()
def say_hi():
    tk.Label(window,text='hi').pack()

btn = tk.Button(window,text='click me',command = say_hi)

# <Button-1>   is left click
# <Button-2>   is middle click
# <Button-3>   is right click

btn.bind('<Button-1>',say_hi)
btn.pack()

window.mainloop()