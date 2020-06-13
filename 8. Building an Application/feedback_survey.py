import tkinter as tk
from tkinter import ttk


class Feedback:
    def __init__(self, master):

        self.pic = tk.PhotoImage(file="tour_logo.gif")
        self.info_label = ttk.Label(
            master,
            text="Explore California Feedback Survey",
            image=self.pic,
            compound="left",
        )
        self.info_label.grid(row=0, column=0, columnspan=2, sticky="nsew")

        ttk.Label(master, text="Name").grid(row=1, column=0, sticky="ew")
        self.name_entry = ttk.Entry(master)
        self.name_entry.grid(row=1, column=1)

        ttk.Label(master, text="Email").grid(row=2, column=0, sticky="ew")
        self.email_entry = ttk.Entry(master)
        self.email_entry.grid(row=2, column=1)

        ttk.Label(master, text="Comments").grid(row=3, column=0, sticky="ew")
        self.comments_text = tk.Text(master, height=4, wrap="word")
        self.comments_text.grid(row=3, column=1)

        self.submit_button = ttk.Button(master, text="Submit")
        self.submit_button.grid(row=4, column=0)
        self.clear_button = ttk.Button(master, text="Clear")
        self.clear_button.grid(row=4, column=1)


def main():

    root = tk.Tk()
    feedback = Feedback(root)
    root.mainloop()


if __name__ == "__main__":
    main()
