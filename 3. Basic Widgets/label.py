import tkinter as tk
from tkinter import ttk

root = tk.Tk()

label = ttk.Label(
    root, text="Samujjwaal here, working using tkinter python GUI library"
)
# attach label to root window
label.pack()

# wrap and center align label text
label.config(wraplength=100, justify="center")
# modify color of text and label
label.config(foreground="blue", background="yellow")
# change font of label text
label.config(font=("Fira Code", 12, "italic"))

# import image -- only gif images supported
pic = tk.PhotoImage(file="samujjwaal.gif")

# compound attribute to put image to left of label text
label.config(image=pic, compound="left")

root.mainloop()
