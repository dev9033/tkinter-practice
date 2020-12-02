import tkinter as tk

window = tk.Tk()

tk.Label(window,text='hey').grid(row=0)
tk.Entry(window).grid(row=0,column=1)

tk.Label(window,text='pass').grid(row=1)
tk.Entry(window).grid(row=1, column=1)

tk.Checkbutton(window,text='keep me logged in').grid(columnspan=2)

window.mainloop()