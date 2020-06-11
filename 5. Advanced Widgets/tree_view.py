from tkinter import *
from tkinter import ttk

root = Tk()
# create treeview object
treeview = ttk.Treeview(root)
treeview.pack()
# add hierarchy ite treeview
treeview.insert("", "0", "item1", text="First item")
treeview.insert("", "1", "item2", text="Second item")
treeview.insert("", "end", "item3", text="Thir d item")

# add item under an item
treeview.insert("item2", "end", "python", text="Python")
# to restrict how many treeview items are displayed
treeview.config(height=5)

# moving treeview items
treeview.move("item2", "item1", "end")

# expand nodes programmatically
treeview.item("item2", open=True)
treeview.item("item1", open=True)

# remove item from treeview
treeview.detach("item3")

# add column to treeview
treeview.config(columns=("version"))
treeview.column("version", width=50, anchor="center")
# add title column
treeview.heading("version", text="Version")

# add value under column
treeview.set("python", "version", "3.8.3")

# add tag for treeview item
treeview.item("python", tags=["software"])
treeview.tag_configure("software", background="yellow")


# define callback function
def function(event):
    print(treeview.selection())


# bind callback function to treeview
# press ctrl to select multiple nodes
treeview.bind("<<TreeviewSelect>>", function)

# to allow selection of single node  at a time
treeview.config(selectmode="browse")

# to disallow selection of any nodes
treeview.config(selectmode="browse")

# programatically select nodes
treeview.selection_add("python")
treeview.selection_remove("python")
treeview.selection_toggle("python")

root.mainloop()
