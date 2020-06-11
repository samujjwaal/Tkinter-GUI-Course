from tkinter import *

root = Tk()

text = Text(root, width=50, height=5)

text.pack()

text.config(wrap="word")

print(text.get("1.0", "end"))
print(text.get("1.0", "1.end"))

text.insert("1.0 + 2 lines", "\ninserted message")

root.mainloop()
