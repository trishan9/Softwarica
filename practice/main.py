import math

a = 2 - 1j
a = 2 + 1j
a = 1J
a = 1J + 2
a = 0J

print(a.real, a.imag)

# Built in Functions
# id(variable) -> gives memory address
# type(variable) -> gives type
# isinstance(variable, datatype) -> True or False

# Logical Operators
print(2 < 3 and 3)  # True and Expression = Expression
print(2 > 3 and 3)  # False and Expression = False

print(2 < 3 or 3)  # True or Expression = True
print(2 > 3 or 3)  # False or Expression = Expression

# Bitwise Operations
print(~113)  # -> -114
print(~-114)  # -> 113
# &, |, ^ - XOR -> True False -> True, True/True, False/False -> False
print(26 >> 3)  # (26 // (2 ** 3))
print(5 << 3)  # (5 * (2 ** 3))

# Loops
i = 0
while i <= 5:
    print(i)
    if (i == 2):
        break
    i += 1
else:
    print("Else")

i = 0
while i <= 5:
    print(i)
    if (i == 2):
        i += 1
        continue

    i += 1
else:
    print("Else")

for i in range(5):
    print(i)

# Printing
print("Hello", "World", end="\t", sep="//")
# C style formatting
print("Hello %s %d" % ("Trishan", 10))
print("Hello", "World 2", sep="//")  # -> sep and end always on last
print("Hello {1} {0}".format("World", "2", "100"))

# String Methods
a = "-Tri"
b = "Tri"
print(a.zfill(5))
print(b.zfill(5))
print(a)  # -> zfill doesn't modifies the variable

print("Hello\rWorl")  # ->  Worlo
print(r"Hello \n World")
print("Hello\0World")

a = "Trishan"
print(a.replace("Tr", "FRI"))
print(a)  # -> replace also cant modify string

# A -> 65
# a -> 97
a = "Banana"
b = a.maketrans("Z", "A")
b = a.maketrans("B", "A")
print(b)
print(a.translate(b))

# Even Length of variable -> Left -> n+1/2
a = "Tri"
print(a.center(7, "*"))
a = "Tris"
print(a.center(7, "*"))
print(a.rjust(9, "*"))  # -> String on Right
print(a.rjust(9))  # -> takes space

print(a.find('o'))  # -1
print(a.rfind('o'))
# print(a.index('P'))  # error
# print(a.rindex('P'))

a = "trishan"
print(a.capitalize())
print(a.upper())
print(a.lower())
print(a.swapcase())
print(a.title())

print(a.isupper())
print(a.islower())
print(a.istitle())
print(a.isdigit())
print(a.isidentifier())
print(a.isalnum())
print(a.isalpha())
a = "    "
print(a.isspace())
a = "\t Trishan"  # -> False
print(a.isprintable())


# Functions
def greet():
    '''This function prints hello world'''
    print("Hello World")


print(greet.__doc__)


# List / Tuple -> list(tup), tuple(lst)
# -> map,filter(lambda, list)
# -> reduce(lambda, list, initial)
a = [1, 2, 3, 4]
a.append(5)
a.extend([1, 2])
a.insert(0, 100)
a.pop()  # -> last element
a.pop(0)
a.remove(3)
a[0] = 1000
del a[len(a) - 1]
print(a)

a = [1, 2, 3, 4]
b = a.copy()
b.append(5)
print(a)

# Sets
a = set()
print(type(a))
a = {1, 2, 3, 4}
b = {3, 4, 5}
a.add(5)
a.update(b)
a.remove(5)  # -> gives error
a.discard(900)  # -> doesnt give error
a.pop()  # -> removes first element
# print(a.union(b))-****
# print(a.intersection(b))
# print(a.difference(b))
print(a)

# Dictionary
a = {"a": 1, "b": 2, "a": 11}
a.setdefault("b", 3)
a.setdefault("d", 100)
print(a)

print(a.pop("a"), "TEST")
print(a.popitem(), "TEST2")  # -> removes last element
print(a)

b = a.get(
    "f", "Not Found"
)  # -> doesn't give error, instead retutns None but if Second Arg is passed then Second Arg is returned
print(b)

# Modules
print(math.floor(1.8))
print(math.ceil(1.8))
print(math.ceil(1.0))
print(math.sqrt(4))
print(math.pow(2, 3))
print(math.fabs(18))
print(math.fabs(-18))


# Namespace LEGB Rule
# global, nonlocal keyword

# Exception Handling
