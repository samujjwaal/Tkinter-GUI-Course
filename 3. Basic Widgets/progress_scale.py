from tkinter import *
from tkinter import ttk

root = Tk()

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

root.mainloop()
