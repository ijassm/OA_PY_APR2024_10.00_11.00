# def add(a):
#     return lambda b: a + b


# add5 = add(5)

# print(add5(3))
# print(add5(6))


# defining a decorator
# def hello_decorator(func):
#     def inner1():
#         print("Hello, this is before function execution")

#         func()

#         print("This is after function execution")

#     return inner1


# # defining a function, to be called inside wrapper
# def function_to_be_used():
#     print("This is inside the function !!")


# function_to_be_used = hello_decorator(function_to_be_used)


# # calling the function
# function_to_be_used()


# importing libraries
# import time
# import math


# # decorator to calculate duration
# # taken by any function.
# def calculate_time(func, num):

#     # added arguments inside the inner1,
#     # if function takes any arguments,
#     # can be added like this.
#     def inner1():

#         # storing time before function execution
#         begin = time.time()

#         func(num)

#         # storing time after function execution
#         end = time.time()
#         print("Total time taken in : ", func.__name__, end - begin)

#     return inner1


# # this can be added to any function present,
# # in this case to calculate a factorial
# def factorial(num):

#     # sleep 2 seconds because it takes very less time
#     # so that you can see the actual difference
#     time.sleep(2)
#     print(math.factorial(num))


# # calling the function.
# calculate_time(factorial, 5)()


# def greeting(func):
#     return "Hello" + " " + func()


# def name():
#     return "Sakthi"


# print(greeting(name))


# def greeting(func):
#     return "Hello" + " " + func()


# @greeting
# def name():
#     return "Sakthi"


# print(name)
