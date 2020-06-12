from tkinter import *
from tkinter import ttk

root = Tk()

text = Text(root, width=40, height=10, wrap="word")
text.grid(row=0, column=0)
# create scroll bar object
scroll_bar = ttk.Scrollbar(root, orient=VERTICAL, command=text.yview)
# add next to text box
scroll_bar.grid(row=0, column=1, sticky="ns")

# to communicate back to scroll bar
# set method tells scroll bar % wise where to place scroll pad
text.config(yscrollcommand=scroll_bar.set)

root.mainloop()
