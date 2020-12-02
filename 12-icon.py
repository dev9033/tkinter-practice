import tkinter as tk

window = tk.Tk()

icon = tk.PhotoImage(file = 'Google.png')
label = tk.Label(window,image=icon)
label.pack()

window.mainloop()