from tkinter import *
from tkinter import ttk

root = Tk()

button1 = ttk.Button(root, text="Button 1")
button1.pack()
button2 = ttk.Button(root, text="Button 2")
button2.pack()
# create style object
style = ttk.Style()
# current theme being used by widgets
print(style.theme_use())

# modify a style
style.configure("TButton", foreground="blue")

# derive custom style from standard style
style.configure("Alarm.TButton", foreground="orange", font=("Arial", 24, "bold"))
button2.config(style="Alarm.TButton")

# set foreground style wrt. state of widget
style.map("Alarm.TButton", foreground=[("pressed", "pink"), ("disabled", "grey")])
button2.state(['disabled'])

# print style layout
print(style.layout('TButton'))

root.mainloop()
