a = 1
while a <= 10:
    print("Hello World")
    a += 1

string = "Softwarica"
i = 0
while i < len(string):
    print(string[i], i)
    i += 1

number = int(input("Enter a number: "))
i = 1
while i <= 10:
    print(f"{number} X {i} = {number * i}")
    i += 1

i = 10
while i >= 1:
    print(f"{number} X {i} = {number * i}")
    i -= 1

list1 = [1, 2, 3, 4, 5]
i = 0
total = 0
while i < len(list1):
    total += list1[i]
    i += 1
print(total)

list1 = [1, 2, 3, 4]
i = 0
prod = 1
while i < len(list1):
    prod *= list1[i]
    i += 1
print(prod)

a = [1, 2, 3, "a", "b", "C"]
i = 0
while i < len(a):
    element = a[i]
    if isinstance(element, str):
        print(element)
    i += 1

a = [1, 2, 3, "a", "b", "C"]
i = 0
str_list = []
int_list = []
while i < len(a):
    element = a[i]
    if isinstance(element, str):
        str_list.append(element)
    elif isinstance(element, int):
        int_list.append(element)
    i += 1
print(int_list, str_list)

a = [1, 2, 3, "a", "b", "C"]
i = 0
str_list = []
int_list = []
while i < len(a):
    element = a[i]
    if isinstance(element, str):
        str_list.append(type(element))
    elif isinstance(element, int):
        int_list.append(type(element))
    i += 1
print(int_list, str_list)
