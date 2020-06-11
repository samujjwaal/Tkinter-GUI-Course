from tkinter import *
from tkinter import ttk

root = Tk()

treeview = ttk.Treeview(root)
treeview.pack()

treeview.insert("", "0", "item1", text="First item")
treeview.insert("", "1", "item2", text="Second item")
treeview.insert("", "end", "item3", text="Thir d item")

treeview.insert("item2", "end", "python", text="Python")
treeview.config(height=5)

treeview.move("item2", "item1", "end")

treeview.item("item1", open=True)

treeview.detach("item3")

root.mainloop()
