import tkinter as tk
from tkinter import ttk
from tkinter import messagebox


class Feedback:
    def __init__(self, master):

        master.title("Explore California Feedback")
        master.resizable(False, False)
        master.configure(background="#e1d8b9")

        # Style object to configure style of widgets
        self.style = ttk.Style()

        self.style.configure("TFrame", background="#e1d8b9")
        self.style.configure("TButton", background="#e1d8b9")
        self.style.configure(
            "TLabel", background="#e1d8b9", font=["JetBrains Mono", 9]
        )
        self.style.configure("Info.TLabel", font=["JetBrains Mono", 15])

        # frame for user info on top of window
        self.info_frame = ttk.Frame(master)
        self.info_frame.pack()

        self.pic = tk.PhotoImage(file="tour_logo.gif")
        ttk.Label(self.info_frame, image=self.pic).grid(
            row=0, column=0, rowspan=2
        )
        ttk.Label(self.info_frame, text="Thank You", style="Info.TLabel").grid(
            row=0, column=1
        )
        ttk.Label(
            self.info_frame,
            text="Explore California Feedback Survey",
            wraplength=200,
        ).grid(row=1, column=1)

        # frame for all the input fields
        self.fields_frame = ttk.Frame(master)
        self.fields_frame.pack()

        # Name field
        ttk.Label(self.fields_frame, text="Name:").grid(row=0, column=0)
        self.name_entry = ttk.Entry(self.fields_frame, width=15)
        self.name_entry.grid(row=1, column=0)

        # Email field
        ttk.Label(self.fields_frame, text="Email:").grid(row=0, column=1)
        self.email_entry = ttk.Entry(self.fields_frame, width=15)
        self.email_entry.grid(row=1, column=1)

        # Comments field
        ttk.Label(self.fields_frame, text="Comments:").grid(row=2, column=0)
        self.comments_text = tk.Text(
            self.fields_frame, width=35, height=4, wrap="word"
        )
        self.comments_text.grid(row=3, column=0, columnspan=2)

        # frame for the buttons at bottom of window
        self.buttons_frame = ttk.Frame(master)
        self.buttons_frame.pack()

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
