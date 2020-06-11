from tkinter import *
from tkinter import ttk

root = Tk()
# create frame object
frame = ttk.Frame(root)
frame.pack()
# modify dimensions of frame
frame.config(height=100, width=200)
# modify frame relief type
frame.config(relief=RIDGE)

# add button inside frame
ttk.Button(frame, text="Click Me").grid()

# adding paddig around button
frame.config(padding=(30, 15))

# create LabelFrame
ttk.LabelFrame(root, height=100, width=200, text="New Frame").pack()

root.mainloop()
