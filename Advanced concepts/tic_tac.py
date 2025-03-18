import tkinter as tk
from tkinter import *
window=Tk()
window.title("tic tac")
class TicTac:
    def __init__(self,window):
        self.window=window
        self.player=0
        self.b00=self.b01=self.b02=" "
        self.b10 = self.b11 = self.b12=" "
        self.b20 = self.b21 = self.b22=" "
    def board(self):
        self.bt00=tk.Button(self.window,height=2,width=5,command=lambda:self.move(0,0))
        self.bt00.grid(row=0,column=0)
        self.bt01 = tk.Button(self.window, height=2, width=5, command=lambda: self.move(0, 1))
        self.bt01.grid(row=0, column=1)
        self.bt02 = tk.Button(self.window, height=2, width=5, command=lambda: self.move(0, 2))
        self.bt02.grid(row=0, column=2)
        self.bt10 = tk.Button(self.window, height=2, width=5, command=lambda: self.move(1, 0))
        self.bt10.grid(row=1, column=0)
        self.bt11 = tk.Button(self.window, height=2, width=5, command=lambda: self.move(1, 1))
        self.bt11.grid(row=1, column=1)
        self.bt12 = tk.Button(self.window, height=2, width=5, command=lambda: self.move(1, 2))
        self.bt12.grid(row=1, column=2)
        self.bt20 = tk.Button(self.window, height=2, width=5, command=lambda: self.move(2, 0))
        self.bt20.grid(row=2, column=0)
        self.bt21 = tk.Button(self.window, height=2, width=5, command=lambda: self.move(2, 1))
        self.bt21.grid(row=2, column=1)
        self.bt22 = tk.Button(self.window, height=2, width=5, command=lambda: self.move(2, 2))
        self.bt22.grid(row=2, column=2)



