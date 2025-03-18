import tkinter as tk
from tkinter import messagebox

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

question_number = 0
score = 0
def next_question():
    global question_number
    if question_number < len(questions):
        question,options, _ = questions[question_number]
        question_label.config(text=f"{question}\noptions:{', '.join(options)}")
        entry.delete(0, tk.END)
    else:
        show_score()

def check_answer():
    global question_number, score
    user_answer = entry.get().strip()
    correct_answer = questions[question_number][2]
    if user_answer == correct_answer:
        score += 1
    question_number += 1
    next_question()

def show_score():
    messagebox.showinfo("quiz done", f"Your score is {score}/{len(questions)}")
    root.quit()

root = tk.Tk()
root.title("simple quiz")

question_label = tk.Label(root, text="")
question_label.pack(pady=20)

entry = tk.Entry(root)
entry.pack(pady=10)

submit_button = tk.Button(root, text="submit", command=check_answer)
submit_button.pack(pady=20)

next_question()
root.mainloop()
