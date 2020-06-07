import tkinter as tk
from tkinter import ttk

root = tk.Tk()
# define a stringvar object
var = tk.StringVar()
var.set("Daft")

# create check button
check = ttk.Checkbutton(root, text="Daft?")
check.pack()


def whats_var():
    # method to get current value of stringvar object
    print(var.get())


# modify default value returned by checkbutton
check.config(variable=var, onvalue="Yes", offvalue="No", command=whats_var)

# create series of radio buttons
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

# assign current value of stringvar object as text for check button
check.config(textvariable=var)

root.mainloop()
