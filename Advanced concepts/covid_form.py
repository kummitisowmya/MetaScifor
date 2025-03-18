import tkinter as tk
from tkinter import messagebox


class CovidVaccination:
    def __init__(self, window):
        self.window = window
        self.window.title("COVID Vaccination Form")
        self.window.geometry("400x400")  # Optional: Adjust the size of the window

        title = tk.Label(window, text="COVID Vaccination Form", font=("Arial", 16))
        title.pack(pady=10)

        self.input = {}
        self.create_input("Name", "Enter your name")
        self.create_input("Age", "Enter your age")
        self.create_input("Gender", "Select gender", input_type="dropdown", options=["Male", "Female", "Other"])
        self.create_input("Phone Number", "Enter contact number")
        self.create_input("Dose Number", "Enter dose number (1 or 2)")

        button = tk.Button(window, text="Submit", command=self.submit_form)
        button.pack(pady=20)

    def create_input(self, label, placeholder, input_type="text", options=None):
        frame = tk.Frame(self.window)
        frame.pack(pady=10, fill="x")

        label_widget = tk.Label(frame, text=label, width=15, anchor="w")
        label_widget.pack(side="left")

        if input_type == "text":
            entry = tk.Entry(frame, width=30)
            entry.insert(0, placeholder)
            entry.pack(side="left", padx=5)
            self.input[label] = entry
        elif input_type == "dropdown":
            var = tk.StringVar()
            var.set(options[0])  # Default option
            dropdown = tk.OptionMenu(frame, var, *options)
            dropdown.pack(side="left", padx=5)
            self.input[label] = var

    def submit_form(self):
        # Collecting data from the form
        try:
            name = self.input["Name"].get()
            age = int(self.input["Age"].get())
            gender = self.input["Gender"].get()
            phone_number = self.input["Phone Number"].get()
            dose_number = int(self.input["Dose Number"].get())

            # Simple validation
            if not name or not phone_number:
                raise ValueError("Name and Phone Number cannot be empty.")
            if age <= 0:
                raise ValueError("Age must be a positive number.")
            if dose_number not in [1, 2]:
                raise ValueError("Dose number must be 1 or 2.")

            # Displaying the data in a messagebox
            messagebox.showinfo(
                "Form Submitted",
                f"Name: {name}\n"
                f"Age: {age}\n"
                f"Gender: {gender}\n"
                f"Phone Number: {phone_number}\n"
                f"Dose Number: {dose_number}\n"
                f"Your form has been submitted successfully!"
            )

        except ValueError as e:
            messagebox.showerror("Input Error", str(e))



if __name__ == "__main__":
    root = tk.Tk()
    app = CovidVaccination(root)
    root.mainloop()
