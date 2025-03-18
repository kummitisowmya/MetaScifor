# def main(num):
#     print(num)
#     a,b=0,1
#     for i in range(num):
#         print(a,end=" ")
#         a,b=b,a+b
# if '__name__'=='__main__':
#     main(10)

if __name__ == '__main__':
    student_list=[]
    score_list=[]
    grades=[]
    for _ in range(int(input())):
        name = input()
        score = float(input())
        grades.append([name,score])
        student_list.append(name)
        score_list.append(score)
    score_list = list(set(score_list))
    score_list.sort()
    second_lowest_score = score_list[1]
    output=[]
    for i in grades:
        if i[1]==second_lowest_score:
            output.append(i[0])
    output.sort()
    for i in output:
        print(i)
