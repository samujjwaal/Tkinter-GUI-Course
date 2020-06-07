import tkinter as tk
from tkinter import ttk

root = tk.Tk()
# defining ttk button object
button = ttk.Button(root, text="Press me!")
button.pack()


def clicked():
    # method to be invoked on pressing button
    print("I was pressed")


button.config(command=clicked)

# programmatically invoke button
button.invoke()

# disable button
button.state(["disabled"])
# enable button
button.state(["!disabled"])

pic = tk.PhotoImage(file="samujjwaal.gif")
# compressing image for button
pic = pic.subsample(5, 5)

# adding image to button
button.config(image=pic, compound="left")

root.mainloop()
