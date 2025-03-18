#import tkinter as tk
from tkinter import *

questions=[
    ("what is crct file extension in python",[".py",".txt",".java",".php"],".py"),
    ("how do you insert comments",["//","#","**","///"],"#"),
    ("keyword for creating function",["def","txt","fun","function"],"def"),
    ("method used for removing whitespace",["strip()","trim()","len()","del()"],"strip()"),
    ("loop available in python",["elif","if","else","for"],"for"),
    ("5+6",["10","11","13","15"],"11"),
    ("7+3",["10","11","13","15"],"10"),
    ("2*3",["10","11","6","15"],"6"),
    ("smallest prime",["0","1","2","3"],"2"),
]
ques_num=0
score=0
def n_question():
    global ques_num,score
    if ques_num<len(questions):
        question,options,answer=questions[ques_num]
        question_label.config(text=question)
        r_b[0].config(text=options[0],value=options[0])
        r_b[1].config(text=options[1],value=options[1])
        r_b[2].config(text=options[2],value=options[2])
        r_b[3].config(text=options[3],value=options[3])
        sel_opt.set("")
    else:



