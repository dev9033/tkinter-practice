import tkinter as tk

window = tk.Tk()

# creating 2 frames top and bottom
top_frame = tk.Frame(window).pack()
bottom_frame = tk.Frame(window).pack(side = 'bottom', expand= True)

# create some random widgets  in the top/bottom frame
btn1= tk.Button(top_frame, text = "button 1 top").pack()
btn2= tk.Button(top_frame, text = "button 2 top").pack()
btn3= tk.Button(bottom_frame, text = "button 1 bottom").pack(side = 'left')
btn4= tk.Button(bottom_frame, text = "button 2 bottom").pack(side = 'left')

window.mainloop()