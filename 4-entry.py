import tkinter as tk
from tkinter.messagebox import showinfo

window = tk.Tk()
txt =  tk.Entry(window,width = 10) # creating a text box
txt.grid(column = 0, row= 0)

def clicked():
    res = 'you typed '+txt.get()
    showinfo('message',res)
    
btn = tk.Button(text='submit',command = clicked)
btn.grid(column = 0, row = 1)
window.mainloop()