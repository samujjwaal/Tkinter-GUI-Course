from tkinter import *
from tkinter import ttk

root = Tk()


def func(number):
    print(number)


ttk.Button(root, text="1", command=lambda: func(1)).pack()
ttk.Button(root, text="2", command=lambda: func(2)).pack()
ttk.Button(root, text="3", command=lambda: func(3)).pack()


root.mainloop()
