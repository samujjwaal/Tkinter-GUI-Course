from tkinter import *
from tkinter import ttk

root = Tk()

vehicle = StringVar()
# declaring combobox object
combobox = ttk.Combobox(root, textvariable=vehicle)
combobox.pack()

#  adding combobox items
combobox.config(
    value=("truck", "sedan", "hatchback", "SUV", "saloon", "semi", "EV", "MUV")
)


def what_vehicle(event):
    # method invoked when new item selected from combobox
    print(combobox.current(), combobox.get())


# binding event to combobox to execute callback
combobox.bind("<<ComboboxSelected>>", what_vehicle)

root.mainloop()
