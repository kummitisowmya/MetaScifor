def questions():
    return[
        {"question":"correct keyword to define functions",
            "options":["a) fun","b) def","c) ques","d) func"],
            "answer":"b"},
        {"question": "which loop is present in python",
         "options": ["a) for", "b) do while", "c) if", "d) if else"],
         "answer": "a"
         },
        {"question": "which keyword is used to importing modules",
         "options": ["a) module", "b) def", "c) import", "d) func"],
         "answer": "c"},
        ]
def ask_question(ques_data):
    print(ques_data["question"])
    for option in ques_data["options"]:
        print(option)
    user_data=input("enter option:")
    return user_data==ques_data["answer"]
def quiz():
    question=questions()
    score=0
    for ques_data in question:
        if ask_question(ques_data):
            print("correct")
            score+=1
        else:
            print("wrong")

