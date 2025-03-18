import tkinter as tk
from tkinter import messagebox

questions=[
    ("what is crct file extension in python",".py"),
    ("how do you insert comments","#"),
    ("keyword for creating function","def"),
    ("method used for removing whitespace","strip()"),
    ("loop available in python","for"),
    ("5+6","11"),
    ("7+3","10"),
    ("2*3","6"),
    ("smallest prime","2"),
]
question_number = 0
score = 0
def next_question():
    global question_number
    if question_number < len(questions):
        question, _ = questions[question_number]
        question_label.config(text=question)
        entry.delete(0, tk.END)
    else:
        show_score()

def check_answer():
    global question_number, score
    user_answer = entry.get().strip()
    correct_answer = questions[question_number][1]
    if user_answer.lower() == correct_answer.lower():
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