import tkinter as tk
from tkinter import ttk

root = tk.Tk()

var = tk.StringVar()
var.set("Daft")

check = ttk.Checkbutton(root, text="Daft?")
check.pack()


def whats_var():
    print(var.get())


check.config(variable=var, onvalue="Yes", offvalue="No", command=whats_var)


ttk.Radiobutton(
    root, text="github", variable=var, value="github", command=whats_var
).pack()
ttk.Radiobutton(
    root, text="gitlab", variable=var, value="gitlab", command=whats_var
).pack()
ttk.Radiobutton(
    root, text="bitbucket", variable=var, value="bitbucket", command=whats_var
).pack()
ttk.Radiobutton(
    root, text="github", variable=var, value="github", command=whats_var
).pack()

check.config(textvariable=var)

root.mainloop()
