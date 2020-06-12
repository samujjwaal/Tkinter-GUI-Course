from tkinter import messagebox
from tkinter import filedialog
from tkinter import colorchooser

# messagebox.showinfo(title="Test Message", message="Just testing")

messagebox.askyesno(title="daft?", message="Are you punk?")

filename = filedialog.askopenfile()

colorchooser.askcolor(initialcolor="#ffffff")
