from tkinter import *
from tkinter import ttk

root = Tk()

ttk.Label(root, text="Orange", background="orange").grid(row=1, column=1)
ttk.Label(root, text="Red", background="red").grid(row=1, column=0)
ttk.Label(root, text="Purple", background="purple").grid(row=0, column=0)
ttk.Label(root, text="Green", background="green").grid(row=0,column=1)

root.mainloop()
