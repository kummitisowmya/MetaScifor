# import time
# class synchronous:
#   def task1(self,taskname):
#     print(f"{taskname} started")
#     time.sleep(4)
#     print(f"{taskname} completed")
#   def task2(self,taskname):
#     print(f"{taskname} started")
#     time.sleep(4)
#     print(f"{taskname} completed")
# s=synchronous()
# s.task1("t1")
# s.task2("t2")
import tkinter as tk
from tkinter import messagebox
import requests

BASE_URL = "https://jsonplaceholder.typicode.com/posts"

def get_data():
    response = requests.get(BASE_URL)
    if response.status_code == 200:
        data = response.json()
        result_text.delete(1.0, tk.END)
        for item in data[:5]:
            result_text.insert(tk.END, f"ID: {item['id']} - Title: {item['title']}\n")
    else:
        messagebox.showerror("Error", "Failed to retrieve data.")

def post_data():
    title = entry_title.get()
    body = entry_body.get()
    if title and body:
        response = requests.post(BASE_URL, json={"title": title, "body": body, "userId": 1})
        if response.status_code == 201:
            messagebox.showinfo("Success", "Data successfully created!")
        else:
            messagebox.showerror("Error", "Failed to create data.")
    else:
        messagebox.showerror("Error", "Title and Body cannot be empty!")

def put_data():
    post_id = entry_post_id.get()
    title = entry_title.get()
    body = entry_body.get()
    if post_id and title and body:
        response = requests.put(f"{BASE_URL}/{post_id}", json={"title": title, "body": body, "userId": 1})
        if response.status_code == 200:
            messagebox.showinfo("Success", "Data successfully updated!")
        else:
            messagebox.showerror("Error", "Failed to update data.")
    else:
        messagebox.showerror("Error", "Post ID, Title, and Body cannot be empty!")

def delete_data():
    post_id = entry_post_id.get()
    if post_id:
        response = requests.delete(f"{BASE_URL}/{post_id}")
        if response.status_code == 200:
            messagebox.showinfo("Success", "Data successfully deleted!")
        else:
            messagebox.showerror("Error", "Failed to delete data.")
    else:
        messagebox.showerror("Error", "Post ID cannot be empty!")

root = tk.Tk()
root.title("REST API with JSONPlaceholder")

tk.Label(root, text="Post ID:").grid(row=0, column=0, padx=10, pady=10)
entry_post_id = tk.Entry(root)
entry_post_id.grid(row=0, column=1)

tk.Label(root, text="Title:").grid(row=1, column=0, padx=10, pady=10)
entry_title = tk.Entry(root)
entry_title.grid(row=1, column=1)

tk.Label(root, text="Body:").grid(row=2, column=0, padx=10, pady=10)
entry_body = tk.Entry(root)
entry_body.grid(row=2, column=1)

tk.Button(root, text="GET Data", command=get_data).grid(row=3, column=0, padx=10, pady=10)
tk.Button(root, text="POST Data", command=post_data).grid(row=3, column=1, padx=10, pady=10)
tk.Button(root, text="PUT Data", command=put_data).grid(row=4, column=0, padx=10, pady=10)
tk.Button(root, text="DELETE Data", command=delete_data).grid(row=4, column=1, padx=10, pady=10)

result_text = tk.Text(root, height=10, width=50)
result_text.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

root.mainloop()
