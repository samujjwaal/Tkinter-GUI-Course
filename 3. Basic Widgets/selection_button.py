import tkinter as tk
from tkinter import ttk

root = tk.Tk()

value = tk.StringVar()
value.set("Daft")

check = ttk.Checkbutton(root, text="Daft?")
check.pack()


def whats_value():
    print(value.get())


check.config(variable=value, onvalue="Yes", offvalue="No", command=whats_value)


# ttk.Radiobutton(root, text='github')

root.mainloop()
