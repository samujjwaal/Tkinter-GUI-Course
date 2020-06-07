from tkinter import *
from tkinter import ttk

root = Tk()
#  progress bar object
progressbar = ttk.Progressbar(root, orient=HORIZONTAL, length=150)
progressbar.pack()

# progress bar in indeterminate mode
progressbar.config(mode="indeterminate")
progressbar.start()
progressbar.stop()

# progress bar in determinate mode
progressbar.config(mode="determinate", maximum=27.0, value=18.6)
#  set progress at 8/27
progressbar.config(value=8.0)
# increase progress by 1
progressbar.step()
# increase progress by 30, progress bar is wrapped
progressbar.step(30)

# doublevar object
value = DoubleVar()

# scale bar object
scale = ttk.Scale(root, orient=HORIZONTAL, length=400, variable=value, from_=0.0, to=27)
scale.pack()
# set value of scale
scale.set(18.6)

# set value of progressbar as selected by scale
progressbar.config(variable=value)

root.mainloop()
