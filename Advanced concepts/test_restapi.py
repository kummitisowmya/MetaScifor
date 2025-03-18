import tkinter as tk
from tkinter import messagebox
import requests
from synchronous import result_text
url="https://jsonplaceholder.typicode.com/posts"
def get():
    response=requests.get(url)
    if response.status_code==200:
        result_text.delete(1.0,tk.END)
        result_text.insert(tk.END,response.json()[:5])
    else:
        messagebox.showerror("request failed")
def post():
    response = requests.post(url,json={"title":"python","userId":1})
    messagebox.showinfo(f"{response.status_code}")
def put():
    response=requests.put(f"{url}/1",json={"title":"python django","userId":1})
    messagebox.showinfo(f"{response.status_code}")
def delete_d():
    response = requests.put(f"{url}/1")
    messagebox.showinfo(f"{response.status_code}")
window=tk.Tk()
window.title("api app")
tk.Button(window,text="get",command=get).pack(pady=5)
tk.Button(window,text="post",command=post).pack(pady=5)
tk.Button(window,text="put",command=put).pack(pady=5)
tk.Button(window,text="delete",command=delete_d).pack(pady=5)
result_text=tk.Text(window,height=10,width=50).pack(pady=5)
result_text.pack(pady=5)
window.mainloop()





