from tkinter import *
from tkinter import ttk

root = Tk()

label = ttk.Label(root, text="One", background="yellow")
label.pack(side=LEFT, anchor="nw")

ttk.Label(root, text="Two", background="orange").pack(side=LEFT, padx=10, pady=10)

ttk.Label(root, text="Three", background="pink").pack(side=LEFT, ipadx=10, ipady=10)

for widget in root.pack_slaves():
    widget.pack_configure(fill=BOTH, expand=True)
    print(widget.pack_info())

label.pack_forget()

root.mainloop()
