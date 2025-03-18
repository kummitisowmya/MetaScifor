import tkinter as tk
from tkinter import messagebox
class CovidVaccination:
    def __init__(self,window):
        self.window=window
        self.window.title("covid vaccination form")
        title=tk.Label(window,text="covid vaccination form")
        title.pack()
        self.input={}
        self.input1("name","enter your name")
        self.input1("age","enter your age")
        self.input1("gender","select gender",input_type="dropdown",options=["male","female","other"])
        self.input1("ph no","enter contact")
        self.input1("dose num","enter dose num (1 or 2)")
        button=tk.Button(window,text="submit",command=self.submit_form)
        button.pack(pady=20)
    def input1(self,label,placeholder,input_type="text",options=None):
        display=tk.Frame(self.window)
        display.pack(pady=10)
        label1=tk.Label(display,text=label)
        label1.pack(side="left")
        if input_type=="text":
            entry=tk.Entry(display,width=30)
            entry.insert(0,placeholder)
            entry.pack(side="left")
            self.input[label]=entry
        elif input_type=="dropdown":
            var=tk.StringVar
            var.set(options[0])
            dropdown=tk.OptionMenu(display,var,*options)
            dropdown.pack(side="left")
            self.input[label]=var

        def clear_placeholder(self, entry, placeholder):
            if entry.get() == placeholder:
                entry.delete(0, tk.END)
                entry.config(fg="black")

        def add_placeholder(self, entry, placeholder):
            if entry.get() == "":
                entry.insert(0, placeholder)
                entry.config(fg="gray")

        def submit_form(self):
            form_data = {field: widget.get() if isinstance(widget, tk.Entry) else widget.get() for field, widget in
                         self.inputs.items()}

            if not form_data["name"] or form_data["name"] == "enter your full name":
                messagebox.showerror("error", "please enter your name.")
                return

            if not form_data["age"].isdigit() or int(form_data["age"]) <= 0:
                messagebox.showerror("error", "please enter a valid age.")
                return

            if not form_data["contact number"].isdigit() or len(form_data["contact number"]) != 10:
                messagebox.showerror("error", "please enter a valid 10-digit contact number.")
                return

            summary = "\n".join(f"{key}: {value}" for key, value in form_data.items())
            messagebox.showinfo("form submitted", f"your form has been submitted successfully!\n\n{summary}")
if __name__=="__main__":
    window=tk.Tk()
    app=CovidVaccination(window)
    window.mainloop()