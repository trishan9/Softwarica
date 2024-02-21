# def hello():
#     for _ in range(5):
#         print("Hello")


# def add(lst):
#     sum = 0
#     for i in lst:
#         sum += i

#     def inner(sum):
#         return sum + 1
#     return inner(sum)


# print(add([1, 2, 3, 4, 5]))
# print("Programming")
# hello()

from math import pi

pi = 2


def outer():
    pi = 3

    def inner():
        pi = 4
        print(pi)

    inner()


outer()
