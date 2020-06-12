from tkinter import *

root = Tk()

# create canvas object
canvas = Canvas(root)
canvas.pack()

# to change size of canvas
canvas.config(width=640, height=480)

# create line between (160,360) & (480,120)
line = canvas.create_line(160, 360, 480, 120, fill="blue", width=5)

canvas.itemconfigure(line, fill="green")

print(canvas.coords(line))

# modify coordinates of a line
canvas.coords(line, 0, 0, 320, 240, 640, 0)

# creates a smooth appearance of the line
canvas.itemconfigure(line, smooth=True)
# to configure number of lines drawn to smooth the line
canvas.itemconfigure(line, splinesteps=5)
canvas.itemconfigure(line, splinesteps=100)

# to delete line from canvas
# canvas.delete(line)

root.mainloop()
