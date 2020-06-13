from tkinter import *
from tkinter import ttk

root = Tk()

root.geometry("640x480+200+200")

ttk.Label(root, text="Orange", background="orange").place(
    x=100, y=50, width=100, height=50
)

ttk.Label(root, text="Red", background="red").place(
    relx=0.5, rely=0.5, anchor="center", relwidth=0.5, relheight=0.5
)

ttk.Label(root, text="Purple", background="purple").place(
    relx=0.5, x=100, rely=0.5, y=50
)

ttk.Label(root, text="Green", background="green").place(relx=1, x=-5, y=5, anchor="ne")


root.mainloop()
