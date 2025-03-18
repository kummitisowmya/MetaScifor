import requests
import tkinter as tk
from tkinter import messagebox
window=tk.Tk()
window.title("data fetch")
def show_data():
    url="https://jsonplaceholder.typicode.com/posts/1"
    response=requests.get(url)
    data1=response.json()
    messagebox.showinfo("accessed data",f"{data1['title']}\n\n{data1['body']}")
data_fetch=tk.Button(window,text="click button to fetch data",command=show_data)
data_fetch.pack()
window.mainloop()