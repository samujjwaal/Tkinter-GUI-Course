from tkinter import *
from tkinter import ttk

root = Tk()
# paned window object,panes stacked next to each other
paned_window = ttk.PanedWindow(root, orient=HORIZONTAL)

# BOTH: to expand and fill entire space inside window
# expand: to allow panes to expand on resizing window
paned_window.pack(fill=BOTH, expand=True)

frame1 = ttk.Frame(paned_window, width=100, height=300, relief=SUNKEN)
frame2 = ttk.Frame(paned_window, width=400, height=300, relief=SUNKEN)

# add frames with scale weight
paned_window.add(frame1, weight=1)
paned_window.add(frame2, weight=4)

frame3 = ttk.Frame(paned_window, width=50, height=300, relief=SUNKEN)

# insert new pane between 0 and 1 panes
paned_window.insert(1, frame3)

# to no longer display pane at index 1
paned_window.forget(1)

root.mainloop()
