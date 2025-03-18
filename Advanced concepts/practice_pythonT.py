# myset=set()
# for i in range(10):
#     if i % 2==0:
#         myset.add(i)
# print(myset)
# import asyncio
# async def t1():
#   print("t1 is start")
#   await asyncio.sleep(2)
#   print("completed t1")
# async def t2():
#   print("t2 is start")
#   await asyncio.sleep(2)
#   print("completed t2")
# async def t3():
#   print("t3 is start")
#   await asyncio.sleep(2)
#   print("completed t3")
# async def main():
#   await asyncio.gather(t1(),t2(),t3())
# asyncio.run(main())
# a=["hello","world","python","programming"]
# b=" ".join(a)
# print(b)
# c=" ? ".join(a)
# print(c)
# a="python programming language hello world"
# res1=a.split()
# res=a.split(" ",2)
# print(res1)
# print(res)
# num=2
# for i in range(0,11):
#     print(num,"x",i,"=",2*i)
# min=int(input("enter a num:"))
# max=int(input("enter a num"))
# for i in range(min,max+1):
#     for j in range(1,11):
#         print(i,"x",j,"=",i*j)
# Arvind just started learning python
# and he is very interested to know how he can
# print his name on the screen using python.
# Write a program to print Arvind on the screen.
# Print your name and age as well using a
# python print statement.
# name=input("enter your name:")
# age=int(input("enter your age:"))
# print(name,age)
# Himanshi is confused with different shapes.
# Write a program in python to print different shapes using these symbols
# : “|”, “-”, “/”, “\”.
# print("left angle triangle")
# print("   /|")
# print("  / |")
# print(" /  |")
# print("/___|")
# print("right angle traingle")
# print("|\\")
# print("| \\")
# print("|  \\")
# print("|___\\")
# print("traingle")
# print("  /\\ ")
# print(" /  \\ ")
# print("/____\\")
# print("diamond")
# print("  /\\")
# print(" /  \\")
# print(" \\  /")
# print("  \\/")
# print("sowmya\nsravs\nkiran\nvishnu")
# Its childrens day and the class teacher wanted to share chocolates
# with the entire class the details are as follows,The number of
# chocolates with the teacher are = 327 Number of kids in the class
# are = 78. Write a program to perform modulus division
# using (%) modulus operator and find out how many chocolates
# are remaining with the teacher after equally distributing
# # 327 chocolates to 78 students.
# tot_chocolates=327
# tot_students=78
# rem_chocolates=tot_chocolates%tot_students
# even=[]
# odd=[]
# for i in range(20):
#     if i%2==0:
#         even=even+[i]
#     else:
#         odd=odd+[i]
# print(even)
# print(odd)
# a="goodvibes123THANKS/&@"
# u=0
# l=0
# d=0
# s=0
# for i in a:
#     if i.isupper():
#         u+=1
#     elif i.islower():
#         l+=1
#     elif i.isdigit():
#         d+=1
#     else:
#         s+=1
# print(u)
# print(l)
# print(d)
# print(s)
# no_of_guest=0
#
# while True:
#     authorization_code = int(input("enter"))
#     if authorization_code==-1:
#         break
#     elif authorization_code==0:
#         no_of_guest+=1
#         print("door opened")
#     elif authorization_code==1:
#         print("Access Granted\nDoor Opened")
#     else:
#         print("enter num is invalid")
# print(no_of_guest)
# count=0
# essay="Python is one of the most popular and widely used programming languages in the world today. Known for its simplicity, readability, and versatility, Python has become a favorite among beginners and experienced developers alike. Whether you're building websites, analyzing data, or creating artificial intelligence models, Python is a powerful tool that can handle a wide range of tasks.One of the key reasons for Python's popularity is its easy-to-learn syntax. Unlike many other programming languages, Python uses a clean and straightforward structure that resembles everyday English. This makes it an excellent choice for beginners who are just starting their programming journey. For example, printing  in Python is as simple as writing print"
# for char in essay:
#     if char==" ":
#         count=count+1
# count_s=count
# print(count_s)
# if count_s>=250:
#     print("valid")
# else:
#     print("invalid")

import asyncio
class Asynchronous:
  async def task1(self):
    print("task1 started")
    await asyncio.sleep(2)
    print("task1 completed")
  async def task2(self):
    print("task2 started")
    await asyncio.sleep(2)
    print("task2 completed")
async def main():
  a=Asynchronous()
  await a.task1()
  await a.task2()
asyncio.run(main())



