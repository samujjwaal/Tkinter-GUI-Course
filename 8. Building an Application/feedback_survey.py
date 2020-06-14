import tkinter as tk
from tkinter import ttk
from tkinter import messagebox


class Feedback:
    def __init__(self, master):

        # frame for user info on top of window
        self.info_frame = ttk.Frame(master)
        self.info_frame.pack(fill=tk.BOTH, expand=True)

        self.pic = tk.PhotoImage(file="tour_logo.gif")
        ttk.Label(
            self.info_frame,
            text="Explore California Feedback Survey",
            image=self.pic,
            compound="left",
            background="pink",
        ).pack()

        # frame for all the input fields
        self.fields_frame = ttk.Frame(master)
        self.fields_frame.pack(fill=tk.BOTH, expand=True)

        # Name field
        ttk.Label(self.fields_frame, text="Name").grid(
            row=0, column=0, sticky="ew"
        )
        self.name_entry = ttk.Entry(self.fields_frame, width=30)
        self.name_entry.grid(row=0, column=1, sticky="ew")

        # Email field
        ttk.Label(self.fields_frame, text="Email").grid(
            row=1, column=0, sticky="ew"
        )
        self.email_entry = ttk.Entry(self.fields_frame, width=30)
        self.email_entry.grid(row=1, column=1, sticky="ew")

        # Comments field
        ttk.Label(self.fields_frame, text="Comments").grid(
            row=2, column=0, sticky="ew"
        )
        self.comments_text = tk.Text(
            self.fields_frame, width=35, height=4, wrap="word"
        )
        self.comments_text.grid(row=2, column=1)

        # frame for the buttons at bottom of window
        self.buttons_frame = ttk.Frame(master)
        self.buttons_frame.pack(fill=tk.BOTH, expand=True)

        # Submit button
        self.submit_button = ttk.Button(
            self.buttons_frame, text="Submit", command=self.submit
        )
        self.submit_button.grid(row=0, column=0)

        # Clear button
        self.clear_button = ttk.Button(
            self.buttons_frame, text="Clear", command=self.clear_fields
        )
        self.clear_button.grid(row=0, column=1)

    # Submit button callback function
    def submit(self):
        # print input values to console
        print(f"Name: {self.name_entry.get()}")
        print(f"Email: {self.email_entry.get()}")
        print(f"Comments: {self.comments_text.get(1.0, 'end')}")

        # clear all input field values
        self.clear_fields()

        # message box to notify user
        messagebox.showinfo(
            title="Feedback Confirmation",
            message="Thank You for your valuable feedback !",
        )

    # Clear button callback function
    def clear_fields(self):
        self.name_entry.delete(0, "end")
        self.email_entry.delete(0, "end")
        self.comments_text.delete(1.0, "end")


def main():

    root = tk.Tk()
    feedback = Feedback(root)
    root.mainloop()


if __name__ == "__main__":
    main()
