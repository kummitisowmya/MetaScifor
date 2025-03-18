import tkinter as tk
def click(event):
    text=event.widget.cget("text")
    if text=="=":
        result=eval(entry.get())
        entry.delete(0,tk.END)
        entry.insert(tk.END,str(result))
    elif text=="C":
        entry.delete(0,tk.END)
    else:
        entry.insert(tk.END,text)
window=tk.Tk()
window.title("calculator")
entry=tk.Entry(window,justify=tk.RIGHT)
entry.grid(row=0,column=0,columnspan=4)
buttons=['1','2','3','/',
         '4','5','6','*',
         '7','8','9','-',
         'C','0','=','+']
for i,button in enumerate(buttons):
    b=tk.Button(window,text=button)
    b.grid(row=(i//4)+1,column=i%4,sticky="nsew")
    b.bind("<Button-1>",click)
# for i in range(4):
#     window.grid_columnconfigure(i,weight=1)
#     window.grid_rowconfigure(i+1,weight=1)
window.mainloop()
