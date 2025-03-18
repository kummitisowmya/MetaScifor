import math
print(math.sqrt(10))
print(math.pow(3,2))
print(math.pi)

import random
print(random.randint(1,5))
print(random.randrange(10,20))

import tkinter as tk
import random
window=tk.Tk()
label=tk.Label(window,text=" ",bg="red")
label.pack()
def r():
    random1=random.randint(10,20)
    label.config(text=random1)
button=tk.Button(window,text="click",bg="Green",command=r)
button.pack()
window.mainloop()
