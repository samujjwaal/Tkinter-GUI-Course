from tkinter import *
from tkinter import ttk

root = Tk()

# create tabbed notebook window
notebook = ttk.Notebook(root)
notebook.pack()

frame1 = ttk.Frame(notebook)
frame2 = ttk.Frame(notebook)

#  add frames as tabs inside window
notebook.add(frame1, text="First")
notebook.add(frame2, text="Second")
# add  in tab 0
ttk.Button(frame1, text="Dont Click").pack()

frame3 = ttk.Frame(notebook)

# insert tab at specific index
notebook.insert(1, frame3, text="Third")

# to hide a tab
notebook.forget(1)

# returns selected tab's index
# print(notebook.index(notebook.select()))

notebook.select(1)

# change state of tab
notebook.tab(0, state="disabled")
# notebook.tab(1, state="hidden")
# notebook.tab(1, state="normal")

# returns properties of a tab
print(notebook.tab(0))
print(notebook.tab(0, "text"))

root.mainloop()
