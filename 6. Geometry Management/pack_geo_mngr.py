from tkinter import *
from tkinter import ttk

root = Tk()

ttk.Label(root, text="One", background="yellow").pack(fill=BOTH,expand=True)

ttk.Label(root, text="Two", background="orange").pack(fill=BOTH)

ttk.Label(root, text="Three", background="pink").pack(fill=BOTH,expand=True)



root.mainloop()
