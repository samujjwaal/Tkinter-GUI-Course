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
canvas.delete(line)

# create rectangle using coordinates of opposite corners
rect = canvas.create_rectangle(160, 120, 480, 360)
canvas.itemconfigure(rect, fill="yellow")
# create oval by coordinates of opposite corners
oval = canvas.create_oval(160, 120, 480, 360)
# create arc, by default 0 to 90 degree
arc = canvas.create_arc(160, 1, 480, 240)
# arc fromm 0 to 180 deg
canvas.itemconfigure(arc, start=0, extent=180, fill="green")
# create triangle using coordinate pairs
poly = canvas.create_polygon(160, 360, 320, 480, 480, 360, fill="blue")

# add text to canvas
text = canvas.create_text(320, 240, text="Python", font=("Courier", 32))

# add image to canvas
img = PhotoImage(file=".\\3. Basic Widgets\samujjwaal.gif")
image = canvas.create_image(320, 240, image=img)

# to place text above image
canvas.lift(text)
# to move image below
canvas.lower(image)
# places image just below text
canvas.lower(image, text)

button = Button(canvas, text="Button here")
# add button to canvas
canvas.create_window(320, 60, window=button)

# add tags to canvas items
canvas.itemconfigure(rect, tag=["shape"])
canvas.itemconfigure(oval, tag=["shape", "round"])
# modify items of a particular tag together
canvas.itemconfigure("shape", fill="grey")

root.mainloop()
