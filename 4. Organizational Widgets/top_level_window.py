from tkinter import *

root = Tk()
# create new window
window = Toplevel(root)
# add title new window
window.title("New Window")

# window.lower()
# display window above root window
window.lift(root)

# window.state(["iconic"])
# resize new window
window.geometry("640x480+50+100")

# disallow user from resizing window in X & Y directions
window.resizable(False, False)

# set resize limits
window.maxsize(640, 480)
window.minsize(200, 200)

window.resizable(True, True)

# window.destroy()

# root.destroy()

root.mainloop()
