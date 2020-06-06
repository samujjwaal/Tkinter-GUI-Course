from tkinter import *

# invoke tk constructor to create top level root window
root = Tk()

# create label as child of root and pack() to place label on root
Label(root, text="Hello World from Tkinter!!").pack()

# to run main of root
root.mainloop()
