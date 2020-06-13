import tkinter as tk
from tkinter import ttk


class Feedback:
    def __init__(self, master):

        self.info_frame = ttk.Frame(master)
        self.info_frame.pack()

        self.pic = tk.PhotoImage(file="tour_logo.gif")
        self.info_label = ttk.Label(
            self.info_frame,
            text="Explore California Feedback Survey",
            image=self.pic,
            compound="left",
        )
        self.info_label.grid(row=0, column=0, columnspan=2, sticky="nsew")

        self.fields_frame = ttk.Frame(master)
        self.fields_frame.pack()

        ttk.Label(self.fields_frame, text="Name").grid(row=1, column=0, sticky="ew")
        self.name_entry = ttk.Entry(self.fields_frame)
        self.name_entry.grid(row=1, column=1)

        ttk.Label(self.fields_frame, text="Email").grid(row=2, column=0, sticky="ew")
        self.email_entry = ttk.Entry(self.fields_frame)
        self.email_entry.grid(row=2, column=1)

        ttk.Label(self.fields_frame, text="Comments").grid(row=3, column=0, sticky="ew")
        self.comments_text = tk.Text(self.fields_frame, height=4, wrap="word")
        self.comments_text.grid(row=3, column=1)

        self.buttons_frame = ttk.Frame(master)
        self.buttons_frame.pack()

        self.submit_button = ttk.Button(self.buttons_frame, text="Submit")
        self.submit_button.grid(row=4, column=0)
        self.clear_button = ttk.Button(self.buttons_frame, text="Clear")
        self.clear_button.grid(row=4, column=1)


def main():

    root = tk.Tk()
    feedback = Feedback(root)
    root.mainloop()


if __name__ == "__main__":
    main()
