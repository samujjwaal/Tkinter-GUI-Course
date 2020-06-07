import tkinter as tk
from tkinter import ttk

root = tk.Tk()

label = ttk.Label(
    root, text="Samujjwaal here, working using tkinter python GUI library"
)
# wrap and center align label text
label.config(wraplength=100, justify=tk.CENTER)
# modify color of text and label
label.config(foreground="blue", background="yellow")
# change font of label text
label.config(font=("Fira Code", 12, "italic"))

label.config()
label.pack()

root.mainloop()
