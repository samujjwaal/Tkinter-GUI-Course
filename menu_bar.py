from tkinter import *

root = Tk()

# to disable creation of tearable menu
root.option_add("*tearOff", False)

# create menu object
menu_bar = Menu(root)
# add menu to root window
root.config(menu=menu_bar)

# create menu bar options
file = Menu(menu_bar)
edit = Menu(menu_bar)
help_ = Menu(menu_bar)
# add menu options to menu bar
menu_bar.add_cascade(menu=file, label="File")
menu_bar.add_cascade(menu=edit, label="Edit")
menu_bar.add_cascade(menu=help_, label="Help")

# create menu command
file.add_command(label="New", command=lambda: print("New File"))
# add seperator between menu commands
file.add_separator()
file.add_command(label="Open", command=lambda: print("Open File"))
file.add_command(label="Save", command=lambda: print("Save File"))

# display shortcut keys next to menu command
file.entryconfig("New", accelerator="Ctrl+N")

# disable menu option
file.entryconfig("Open", state="disabled")

# delete menu command
file.delete("Save")

# create cascading menu command save
save = Menu(file)
#  add to 'File'
file.add_cascade(menu=save, label="Save")
save.add_command(label="Save As", command=lambda: print("Save As"))
save.add_command(label="Save All", command=lambda: print("Save All"))

# add radiobutton as menu entry
choice = IntVar()
edit.add_radiobutton(label="One", variable=choice, value=1)
edit.add_radiobutton(label="Two", variable=choice, value=2)
edit.add_radiobutton(label="Three", variable=choice, value=3)

# create popup menu
file.post(400, 300)

root.mainloop()
