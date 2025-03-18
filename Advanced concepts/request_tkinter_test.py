import requests
import tkinter as tk
from tkinter import messagebox
window=tk.Tk()
frame=tk.Frame(window)
frame.pack()
window.title("data fetch")
def show_data():
    url="https://jsonplaceholder.typicode.com/posts/1"
    response=requests.get(url)
    data1=response.json()
    title=data1['title']
    title_label=tk.Label(frame,text=f"Title:{title}")
    title_label.pack()
    body= data1['body']
    body_label = tk.Label(frame, text=f"Body:{body}")
    body_label.pack()
data_fetch=tk.Button(window,text="click button to fetch data",command=show_data)
data_fetch.pack()
window.mainloop()