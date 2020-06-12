from tkinter import *
from tkinter import ttk

root = Tk()

canvas = Canvas(root, scrollregion=(0, 0, 640, 480), bg="white")

# defining X & Y scroll bars
xscroll = ttk.Scrollbar(root, orient=HORIZONTAL, command=canvas.xview)
yscroll = ttk.Scrollbar(root, orient=VERTICAL, command=canvas.yview)
canvas.config(xscrollcommand=xscroll.set, yscrollcommand=yscroll.set)

canvas.grid(row=0, column=0)

# add scroll bars to canvas
xscroll.grid(row=1, column=0, sticky="ew")
yscroll.grid(row=0, column=1, sticky="ns")

# define mouse click function
def canvas_click(event):
    x = canvas.canvasx(event.x)
    y = canvas.canvasy(event.y)
    canvas.create_oval((x - 5, y - 5, x + 5, y + 5), fill="orange")


# bind mouse click function to canvas
canvas.bind("<1>", canvas_click)

root.mainloop()
