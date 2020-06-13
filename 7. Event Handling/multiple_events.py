from tkinter import *
from tkinter import ttk

root = Tk()

label1 = ttk.Label(root, text="Label 1")
label1.pack()

label2 = ttk.Label(root, text="Label 2")
label2.pack()

label1.bind("<ButtonPress>", lambda e: print("<ButtonPress> Label"))
label1.bind("<1>", lambda e: print("<1> Label"))

root.bind("<1>", lambda e: print("<1> Root"))

label1.unbind("<ButtonPress>")
label1.unbind("<1>")

root.bind_all("<Escape>", lambda e: print("Escape !"))

root.mainloop()
