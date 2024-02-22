import random

# Complex Numbers
a = 1j + 10
print(a.real, a.imag)


# File Handling
# file = open("./myfile4.txt", "w")
# print(file.writable())

# import math
print('Hello Python'.istitle())
print("abc".isalnum())
print("hello python".capitalize())

print('hello' > 'hello')
print('python' < 'Python')

print([1, 2] + [1, 2])

print(r'hello \n python')

a = {1, 2, 3, 4}
a.add((1, 2))
print(a)

a = {1: 2, 2: 3, 3: 4}
a[1] = 3
print(a)

a = 5
b = 2
x = a > b and not (a == b)
y = a ** 3
z = a/b
t = 1, 2, 3, 4
print(x, y, z)
print(type(x), type(y), type(z), type(t))

a = {1: 2, 2: 3, 3: 4}
x = a.get(5)
print(x)

l = [1, 2]
print(l*2)

a = "9 "
print(a.isdigit())

print(random.randint(5, 15))

a = "Trishan is"
print(a.split())

# n = file.write("Hello World!\n")
# print(n)
# file.writelines(["Hello World 2!\n", "Hello World 3!"])
# file.close()

# f = open("./myfile4.txt")
# ndata = f.read(2)
# print(ndata)
# print(f.tell())
# f.seek(0)  # -> changes cursor position
# data = f.readline()
# data2 = f.readlines(20)
# print(data)
# print(data2)
# f.close()


# print(file.readable())
# print(file.closed)
# print(file.name)
# print(file.mode)

# Pickling and Unpickling
# import pickle

# with open("./myfile4.txt", "wb") as f:
#     dct = {"name": "Trishan"}
#     pickle.dump(dct, f)
#     pickle_repr = pickle.dumps(dct)

# with open("./myfile4.txt", "rb") as f:
#     dct = pickle.load(f)
#     print(dct)
#     dct2 = pickle.loads(pickle_repr)
#     print(dct2)

# Functions


def func(a, b):
    return a ** b


def func2():
    print("Trishan")


print(func2())
# print(func(2, 3))
# print(func(b=2, a=3))

# import math
# a = 2 - 1j
# a = 2 + 1j
# a = 1J
# a = 1J + 2
# a = 0J

# print(a.real, a.imag)

# # Built in Functions
# # id(variable) -> gives memory address
# # type(variable) -> gives type
# # isinstance(variable, datatype) -> True or False

# # Logical Operators
# print(2 < 3 and 3)  # True and Expression = Expression
# print(2 > 3 and 3)  # False and Expression = False

# print(2 < 3 or 3)  # True or Expression = True
# print(2 > 3 or 3)  # False or Expression = Expression

# # Bitwise Operations
# print(~18)
# print(~113)  # -> -114
# print(~-114)  # -> 113
# # &, |, ^ - XOR -> True False -> True, True/True, False/False -> False
# print(26 >> 3)  # (26 // (2 ** 3))
# print(5 << 3)  # (5 * (2 ** 3))

# # Loops
# for i in range(5):
#     if i == 3:
#         break  # -> if break is used then else wont get executed
#     print(i)
# else:
#     print("I am else of for loop")
# print("Outside")

# i = 0
# while i <= 5:
#     print(i)
#     if (i == 2):
#         break
#     i += 1
# else:
#     print("Else")

# i = 0
# while i <= 5:
#     if (i == 2):
#         continue
#     print(i)
#     i += 1

# else:
#     print("Else")

# # Printing
# print("Hello", "World", sep="//", end="asasas\n")

# a = "Trishan"

# print("Welcome {}".format(a, "Wagle", "sdsd"))
# print("Welcome {a} {1} {0}".format("Wagle", "Tri", a="Trishan"))
# print("Welcome {A} {1} softwarica {}".format("to", "ok", A="To"))

# # C style formatting
# print("Hello %s %d" % ("Trishan", 10))
# print("Hello", "World 2", sep="//")  # -> sep and end always on last
# print("Hello {1} {0}".format("World", "2", "100"))

# # String Methods
# txt = "Trishan\rWagle"
# print(txt)
# print(r"Hello\nWorld")  # raw string: nullifies escape sequence characters
# a = "+Tri"
# b = "Tri"
# print("Trishan".zfill(10))
# print(a.zfill(5))
# print(b.zfill(5))
# print(a)  # -> zfill doesn't modifies the variable

# print("Hello\rWorl")  # ->  Worlo
# print(r"Hello \n World")
# print("Hello\0World")

# a = "Trishan"
# print(a[0::2])
# print(a.replace("Tri", "s"))
# print(a.replace("z", "FRI"))
# print(a)  # -> replace also cant modify string

# # A -> 65
# # a -> 97
# a = "Banana"
# b = a.maketrans("Z", "A")
# print(b)
# b = a.maketrans("Bn", "As")
# print(b)
# print(a.translate(b))

# # Even Length of variable -> Left -> n+1/2
# a = "Tri"
# print(a.center(7, "*"))
# a = "Tris"
# print(a.center(7, "*"))
# a = "Tris"
# print(a.center(7, "*"))
# print(a.rjust(9, "*"))  # -> String on Right
# print(a.rjust(9))  # -> takes space

# a = "Pythono"
# print(a.find('p'))  # -1
# print(a.rfind('o'))
# print(a.index('p'))  # error
# print(a.rindex('n'))

# a = "Pythonoo"
# print(a.count("o"))

# a = "trishan wagle"
# print(a.capitalize())
# print(a.title())
# print(a.upper())
# print(a.lower())
# print(a.swapcase())

# print(a.startswith(""))  # -> True
# print(a.endswith(""))  # -> True

# a = "@@PYTHON"
# print(a.isupper()) # -> True
# print(a.isupper())
# print(a.islower())
# print(a.istitle())
# a = "99"
# print(a.isdigit())
# a = "Trishan9"
# print(a.isalpha())
# a = "#capital"
# print(a.isalnum())
# print(a.isalnum())
# a = "\t   "
# print(a.isspace())
# a = "trishan"
# print(a.isidentifier())
# a = "\t"  # -> False
# print(a.isprintable())

# # Functions
# def greet():
#     '''This function prints hello world'''
#     print("Hello World")


# print(greet.__doc__)


# # List / Tuple -> list(tup), tuple(lst)
# # -> map,filter(lambda, list)
# # -> reduce(lambda, list, initial)
# a = [1, 2, 3, 4]
# print(a[0::3], "Slicing")
# print(list(range(0, 10, 2)), "Range")
# a.append(5)
# a.extend([1, 2])
# print(a, "Extend")
# a.insert(0, 100)
# print(a.pop(), "Pop CHeck")  # -> last element
# print(a.pop(0))
# # a.remove(30) -> gives error
# # print(a, "Removed")
# a[0] = 1000
# del a[len(a) - 1]
# print(a)
# # del a
# # print(a, "Not Found")
# a.clear()
# print(a, "Cleared")

# a = [1, 2, 3, 4]
# b = a.copy()
# b.append(5)
# print(a)

# a = 1, 2, 3, 4, 5
# a = (1,)
# print(a, "Tuple")

# Sets
# a = {2, 4, 1}
# b = {2, 6, 4, 10, 8}
# print(a, b)
# print(a.add(12))
# print(a)
# a.update(b)
# a.remove(12)
# a.discard(2121)
# print(a)

# set1 = {1, 2, 3, 4, 5}
# set2 = {2, 4, 6, 8}
# print(set1 | set2, set1 & set2)
# print(set1.union(set2), set1.intersection(set2))
# print(set1.difference(set2))
# print(set2.difference(set1))
# print(set1.difference(set2).union(set2.difference(set1)))
# print(set1.symmetric_difference(set2))

# set1 = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
# set2 = {2, 4, 6, 8}
# print(set2.issubset(set1), set1.issuperset(set2))

# a.clear()
# print(a)

# Dictionary
# a = {"a": 1, "b": 2, "a": 11}
# a.setdefault("b", 3)
# a.setdefault("d", 100)
# print(a, "Dictionary")

# print(a.pop("a"), "TEST")
# print(a.popitem(), "TEST2")  # -> removes last element
# print(a)
# b = a.get(
#     "f", "Not Found"
# )  # -> doesn't give error, instead retutns None but if Second Arg is passed then Second Arg is returned
# print(b)

# Modules
# print(math.floor(1.8))
# print(math.ceil(1.1))
# print(math.ceil(1.1))
# print(math.sqrt(4))
# print(math.pow(2, 3))
# print(math.fabs(18))
# print(math.fabs(-18))

# s = "Trishan is handsome"
# print(s.split(None, 0))
# i = 1
# while True:
#     if i % 2 == 0:
#         break
#     print(i)
#     i += 2

# Namespace LEGB Rule
# global, nonlocal keyword

# Exception Handling
