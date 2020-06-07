import tkinter as tk
from tkinter import ttk

root = tk.Tk()

button_text = tk.StringVar()
button_text.set("Daft ?")

check = ttk.Checkbutton(root, textvariable=button_text)
check.pack()


root.mainloop()
