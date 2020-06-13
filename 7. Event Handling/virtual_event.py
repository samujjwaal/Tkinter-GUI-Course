from tkinter import *
from tkinter import ttk

root = Tk()

entry = ttk.Entry(root)
entry.pack()

# bind built in virtual events
entry.bind("<<Copy>>", lambda e: print("Copy"))
entry.bind("<<Paste>>", lambda e: print("Paste"))

# define custom virtual event
entry.event_add("<<OddNumber>>", "1", "3", "5", "7", "9")

# bind custom virtual event
entry.bind("<<OddNumber>>", lambda e: print("Odd Number!"))

# to view details about a virtual event
print(entry.event_info("<<OddNumber>>"))

# programmatically invoke virtual event
entry.event_generate("<<OddNumber>>")
entry.event_generate("<<Paste>>")

# delete virtual event
entry.event_delete("<<OddNumber>>")

root.mainloop()
