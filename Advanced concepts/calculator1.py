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
entry=tk.Entry(window)
entry.grid(row=0,column=0,columnspan=4)
buttons=['1','2','3','/',
         '4','5','6','*',
         '7','8','9','-',
         'C','0','=','+']
row=1
col=0
for button in buttons:
    b=tk.Button(window,text=button)
    b.grid(row=row,column=col,sticky="nsew")
    b.bind("<Button-1>",click)
    col+=1
    if col>3:
        col=0
        row+=1
window.mainloop()
