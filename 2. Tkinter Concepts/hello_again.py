from tkinter import *
from tkinter import ttk


class Hello:

    # constructor of class
    def __init__(self, master):

        self.label = ttk.Label(master, text="Hello Tkinter!")
        self.label.grid(row=0, column=0, columnspan=2)

        ttk.Button(master, text="Chicago", command=self.chicago_hello).grid(
            row=1, column=0
        )

        ttk.Button(master, text="Mumbai", command=self.mumbai_hello).grid(
            row=1, column=1
        )

    # handle methods defined for buttons
    def chicago_hello(self):
        self.label["text"] = "Ciao Chicago !"

    def mumbai_hello(self):
        self.label["text"] = "Namaste Mumbai !"


def main():

    root = Tk()
    app = Hello(root)

    # to enter tk event loop
    root.mainloop()


if __name__ == "__main__":
    main()
