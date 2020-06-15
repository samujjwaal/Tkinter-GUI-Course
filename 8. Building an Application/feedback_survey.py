import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
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
            "TLabel", background="#e1d8b9", font=["Cascadia Code", 10]
        )
        self.style.configure("Info.TLabel", font=["Cascadia Code", 14])


        # Frame for user info on top of window
        self.info_frame = ttk.Frame(master)
        self.info_frame.pack(pady=5)

        self.pic = tk.PhotoImage(file="tour_logo.gif")
        ttk.Label(self.info_frame, image=self.pic).grid(
            row=0, column=0, rowspan=2
        )
        ttk.Label(
            self.info_frame, text="Explore California", style="Info.TLabel"
        ).grid(row=0, column=1)
        ttk.Label(
            self.info_frame,
            text="Thank You for taking your time to fill up this Feedback Survey form and support us in our mission",
            wraplength=300,
            justify=tk.CENTER,
        ).grid(row=1, column=1)


        # Frame for all the input fields
        self.fields_frame = ttk.Frame(master)
        self.fields_frame.pack(pady=5)

        # Name field
        ttk.Label(self.fields_frame, text="Name:").grid(
            row=0, column=0, padx=5, sticky="nw"
        )
        self.name_entry = ttk.Entry(
            self.fields_frame, width=17, font=["JetBrains Mono", 10]
        )
        self.name_entry.grid(row=1, column=0, padx=5)
        self.name_entry.focus()

        # Email field
        ttk.Label(self.fields_frame, text="Email:").grid(
            row=0, column=1, padx=5, sticky="nw"
        )
        self.email_entry = ttk.Entry(
            self.fields_frame, width=17, font=["JetBrains Mono", 10]
        )
        self.email_entry.grid(row=1, column=1, padx=5)

        # Comments field
        ttk.Label(self.fields_frame, text="Comments:").grid(
            row=2, column=0, padx=5, sticky="nw"
        )
        self.comments_text = scrolledtext.ScrolledText(
            self.fields_frame,
            width=40,
            height=6,
            wrap="word",
            font=["JetBrains Mono", 10],
        )
        self.comments_text.grid(row=3, column=0, columnspan=2, padx=5)


        # Frame for the buttons at bottom of window
        self.buttons_frame = ttk.Frame(master)
        self.buttons_frame.pack(pady=5)

        # Submit button
        ttk.Button(
            self.buttons_frame, text="Submit", command=self.submit
        ).grid(row=0, column=0, padx=5, pady=5, sticky="e")

        # Clear button
        ttk.Button(
            self.buttons_frame, text="Clear", command=self.clear_fields
        ).grid(row=0, column=1, padx=5, pady=5, sticky="w")


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
    # to center the window on the screen
    root.eval("tk::PlaceWindow . center")
    Feedback(root)
    root.mainloop()


if __name__ == "__main__":
    main()
