import tkinter as tk

window = tk.Tk()

# sufficient width
tk.Label(window, text= 'suf, width',fg = 'white',bg = 'purple').pack()
# width of x
tk.Label(window, text= 'x, width',fg = 'white',bg = 'green').pack(fill = 'x')
# height of y
tk.Label(window, text= 'y, height',fg = 'white',bg = 'black').pack(side='left', fill = 'y')

window.mainloop()