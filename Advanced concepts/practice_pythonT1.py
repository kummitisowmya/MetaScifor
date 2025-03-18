"""generator: generators are created by using functions
and yield keyword
generator creates an iteartor which allows you to
interate over a sequence of values without
stroring the entire sequence in memory.
Instead of returning a single value and terminating,
a generator yields values one at a time,
pausing its state between each yield.
yield is used in the generator function to produce values
and pause execution.
next is used on the generator object to retrieve values
and resume execution.
Together, they enable the lazy evaluation and
memory-efficient iteration that generators are known for."""

# def fibonacci_generator(limit):
#     a, b = 0, 1
#     while a < limit:
#         yield a
#         a, b = b, a + b
#
# # Using the generator
# fib_gen = fibonacci_generator(10)

# for number in fib_gen:
#     print(number)
# def fibonacci():
#     a, b = 0, 1
#     while True:
#         yield a
#         a, b = b, a + b
# # Using the generator
# fib_gen = fibonacci()
# for i in range(10):
#     print(next(fib_gen))
# # Output: 0 1 1 2 3 5 8 13 21 34
# def decorator1(func):
#     def wrapper():
#         print("before calling function")
#         func()
#         print("after")
#     return wrapper
# def decorator2(func):
#     def wrapper():
#         print("before calling function 2")
#         func()
#         print("after 2")
#     return wrapper
# @decorator1
# @decorator2
# #lifo
# def function():
#   print("hi")
# function()
# def decorator1(func):
#     def wrapper(*args,**kwargs):
#         print("hi")
#         func(*args,**kwargs)
#         print("bye")
#     return wrapper
# @decorator1
# def greet(name,sub,skills):
#     print(name,sub)
# greet("python","sowmya","python")
import asyncio
# async def t1():
#   print("t1 is start")
#   await asyncio.sleep(4)
#   print("completed t1")
# async def t2():
#   print("t2 is start")
#   await asyncio.sleep(4)
#   print("completed t2")
# async def t3():
#   print("t3 is start")
#   await asyncio.sleep(4)
#   print("completed t3")
# async def main():
#   await asyncio.gather(t1(),t2(),t3())
# asyncio.run(main())
x={"h":"jj","j":"jdf","u":"kjdf"}
# if x.get("h"):
#     print(x.get("h"))
# else:
#     print("no data")
for i in x:
    print(x[i])