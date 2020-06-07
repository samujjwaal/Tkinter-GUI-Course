from tkinter import *
from tkinter import ttk

root = Tk()

label = Label(root, text="Password")
label.pack(side=LEFT)
entry = ttk.Entry(root, width=25)
entry.pack(side=RIGHT)

# to set default text in field
# entry.(0, "Enter password")

# to mask the user input with *
entry.config(show="*")

# to make the field read only
# entry.state(["readonly"])

root.mainloop()
