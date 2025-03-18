import tkinter as tk
from tkinter import messagebox

class VaccinationForm:
    def __init__(self,root):
        self.root = root
        self.root.title("COVID Vaccination Form")
        self.root.geometry("400x400")

        tk.Label(root, text="COVID Vaccination Form", font=("Arial", 16, "bold")).pack(pady=10)

        tk.Label(root, text="Full Name:").pack(anchor='w', padx=20, pady=5)
        self.name_entry = tk.Entry(root, width=30)
        self.name_entry.pack(padx=20, pady=5)

        tk.Label(root, text="Age:").pack(anchor='w', padx=20, pady=5)
        self.age_entry = tk.Entry(root, width=30)
        self.age_entry.pack(padx=20, pady=5)

        tk.Label(root, text="Gender:").pack(anchor='w', padx=20, pady=5)
        self.gender_var = tk.StringVar(value="None")
        for gender in ["Male", "Female", "Other"]:
            tk.Radiobutton(root, text=gender, variable=self.gender_var, value=gender).pack(anchor='w', padx=40)

        tk.Label(root, text="Vaccination Status:").pack(anchor='w', padx=20, pady=5)
        self.vaccine_var = tk.StringVar(value="None")
        for vaccine in ["Not Vaccinated", "Partially Vaccinated", "Fully Vaccinated"]:
            tk.Radiobutton(root, text=vaccine, variable=self.vaccine_var, value=vaccine).pack(anchor='w', padx=40)

        tk.Button(root, text="Submit", command=self.submit_form).pack(pady=20)

    def submit_form(self):
        name = self.name_entry.get()
        age = self.age_entry.get()
        gender = self.gender_var.get()
        vaccination_status = self.vaccine_var.get()

        if not name or not age or gender == "None" or vaccination_status == "None":
            messagebox.showerror("Error", "All fields are required!")
            return

        try:
            age = int(age)
            if age <= 0:
                raise ValueError
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid age!")
            return

        user_data = (
            f"Name: {name}\n"
            f"Age: {age}\n"
            f"Gender: {gender}\n"
            f"Vaccination Status: {vaccination_status}"
        )
        messagebox.showinfo("Form Submitted", f"Thank you for submitting your details!\n\n{user_data}")
        self.clear_form()

    def clear_form(self):
        self.name_entry.delete(0, tk.END)
        self.age_entry.delete(0, tk.END)
        self.gender_var.set("None")
        self.vaccine_var.set("None")

if __name__ == "__main__":
    root = tk.Tk()
    app = VaccinationForm(root)
    root.mainloop()