# Task - 1
count = 0
while count < 10:
    print("softwarica")
    count += 1

# Task - 2
my_list = [1, 2, 3, 4, 5]
total = 0
index = 0
while index < len(my_list):
    total += my_list[index]
    index += 1
print(total)

# Task - 3
my_string = "softwarica"
index = 0
while index < len(my_string):
    print(my_string[index])
    index += 1

# Task - 4
my_list = [1, "a", "c", 2, 3, 4]
index = 0
while index < len(my_list):
    if isinstance(my_list[index], int):
        print(my_list[index])
    index += 1

# Task - 5
my_list = [4, 5, 3, 2]
index = 0
while index < len(my_list):
    print(my_list[index] * 2)
    index += 1

# Task - 6
num = 5
count = 1
while count <= 10:
    print(num * count)
    count += 1


# Task - 7
my_list = [1, 2, 3, 4]
index = len(my_list) - 1
while index >= 0:
    print(my_list[index])
    index -= 1


# Task - 8
my_list = [1, 2, 3, 4]
new_list = []
index = 0
while index < len(my_list):
    new_list.append(my_list[index] + 1)
    index += 1
print(new_list)


# Task - 9
my_list = [1, 2, 3, 4]
index = 0
while index < len(my_list):
    if my_list[index] == 1 or my_list[index] == 4:
        print(my_list[index])
    index += 1


# Task - 10
my_list = [1, 2, 3, 4]
index = 0
while index < len(my_list):
    if my_list[index] in [1, 2, 4]:
        print(my_list[index])
    index += 1


# Task - 11
my_list = [1, 2, 3, 4]
new_list = []
index = 0
while index < len(my_list):
    if my_list[index] == 1 or my_list[index] == 2 or my_list[index] == 4:
        new_list.append(my_list[index])
    index += 1
print(new_list)


# Task - 12
my_list = [1, 2, 3, 4, 5]
odd_list = []
even_list = []
index = 0
while index < len(my_list):
    if my_list[index] % 2 == 0:
        even_list.append(my_list[index])
    else:
        odd_list.append(my_list[index])
    index += 1
print("Odd:", odd_list)
print("Even:", even_list)


# Task - 13
my_list = [1, 2, 3, "d", 4, 5, "a"]
int_list = []
str_list = []
index = 0
while index < len(my_list):
    if isinstance(my_list[index], int):
        int_list.append(my_list[index])
    elif isinstance(my_list[index], str):
        str_list.append(my_list[index])
    index += 1
print("Integers:", int_list)
print("Strings:", str_list)


# Task - 14
my_list = [1, 2, 3, 4, "a", "b"]
int_list = []
str_list = []
index = 0
while index < len(my_list):
    if isinstance(my_list[index], int):
        int_list.append(type(my_list[index]))
    elif isinstance(my_list[index], str):
        str_list.append(type(my_list[index]))
    index += 1
print("Integers:", int_list)
print("Strings:", str_list)


# Task - 15
my_string = "Hello123 World!"
digits = letters = spaces = 0
index = 0
while index < len(my_string):
    if my_string[index].isdigit():
        digits += 1
    elif my_string[index].isalpha():
        letters += 1
    elif my_string[index].isspace():
        spaces += 1
    index += 1
print("Digits:", digits)
print("Letters:", letters)
print("Spaces:", spaces)


# Task - 16
username = input("Enter username: ")
password = input("Enter password: ")
valid = False
while not valid:
    if username.endswith("@gmail.com") and len(password) >= 8:
        valid = True
    else:
        print("Invalid username or password. Try again.")
        username = input("Enter username: ")
        password = input("Enter password: ")
print("Username and password are valid.")


# Task - 17
num = int(input("Enter a number: "))
while num % 2 == 0:
    print("Even")
    num += 1
    break
else:
    print("Odd")

# Task - 18
num = int(input("Enter a number: "))
factorial = 1
while num > 0:
    factorial *= num
    num -= 1
print("Factorial:", factorial)


# Task - 19
num = 1
while num <= 8:
    count = 1
    while count <= 10:
        print(num * count, end=" ")
        count += 1
    print()
    num += 1

# Task - 20
my_list = [1, 2, 3, 4]
index = 0
while index < len(my_list):
    if my_list[index] == 1 or my_list[index] == 2:
        print(my_list[index])
    index += 1

# Task - 21
start = int(input("Enter start of range: "))
end = int(input("Enter end of range: "))
sum_odd = 0
num = start
while num <= end:
    if num % 2 != 0:
        sum_odd += num
    num += 1
print("Sum of odd numbers:", sum_odd)


# Task - 22
start = int(input("Enter start of range: "))
end = int(input("Enter end of range: "))
sum_even = 0
num = start
while num <= end:
    if num % 2 == 0:
        sum_even += num
    num += 1
print("Sum of even numbers:", sum_even)

# Task - 23
my_string = "Hello World"
space_count = 0
index = 0
while index < len(my_string):
    if my_string[index].isspace():
        space_count += 1
    index += 1
print("Number of spaces:", space_count)

# Task - 24
my_list = [1, 2, 3, 4]
new_list = []
index = 0
while index < len(my_list):
    new_list.append(my_list[index] ** 3)
    index += 1
print(new_list)

# Task - 25
my_string = "programming"
reversed_string = ""
index = len(my_string) - 1
while index >= 0:
    reversed_string += my_string[index]
    index -= 1
print(reversed_string)

# Task - 26
num = 0
while num < 50:
    print(num)
    num += 1
    if num == 8:
        break

# Task - 27
my_string = "Hello"
index = 0
while index < len(my_string):
    print(my_string[index])
    index += 1

# Task - 28
names = ["ram", "shyam", 1, 2]
index = 0
while index < len(names):
    if isinstance(names[index], str):
        print("Hello!,", names[index])
    index += 1

# Task - 29
names = ["ram", "shyam", 1, 2]
new_list = []
index = 0
while index < len(names):
    new_list.append("Dr." + str(names[index]))
    index += 1
print(new_list)

# Task - 30
numbers = [1, 2, 3, 4]
squared_numbers = []
index = 0
while index < len(numbers):
    squared_numbers.append(numbers[index] ** 2)
    index += 1
print(squared_numbers)

# Task - 31
lst1 = [111, 32, -9, -45, -17, 9, 85, -10]
positive_numbers = []
index = 0
while index < len(lst1):
    if lst1[index] > 0:
        positive_numbers.append(lst1[index])
    index += 1
print(positive_numbers)

# Task - 32
my_list = [0, 1, 2, 3, 4, 5, 6]
index = 0
while index < len(my_list):
    if my_list[index] != 3 and my_list[index] != 6:
        print(my_list[index])
    index += 1

# Task - 33
first_list = [1, "a", 2, 4]
types_list = []
index = 0
while index < len(first_list):
    types_list.append(type(first_list[index]))
    index += 1
print(types_list)

# Task - 34
my_list = [1, 2, 3, 4]
index = 0
while index < len(my_list):
    print(my_list[index])
    index += 1
else:
    print("Done")

# Task - 35
num = 105
while num >= 7:
    print(num, end=" ")
    num -= 7

# Task - 36
bad_chars = [';', ':', '!', "*"]
my_string = "py;th* o:n ! ;py * t*h:o !n"
cleaned_string = ""
index = 0
while index < len(my_string):
    if my_string[index] not in bad_chars:
        cleaned_string += my_string[index]
    index += 1
print(cleaned_string)

# Task - 37
series = [1, 2, 3, 4, 5, 6, 7, 8, 9]
even_count = odd_count = 0
index = 0
while index < len(series):
    if series[index] % 2 == 0:
        even_count += 1
    else:
        odd_count += 1
    index += 1
print("Even numbers:", even_count)
print("Odd numbers:", odd_count)


# Task - 38
start = int(input("Enter start of range: "))
end = int(input("Enter end of range: "))
num = start
while num <= end:
    is_prime = True
    divisor = 2
    while divisor <= num // 2:
        if num % divisor == 0:
            is_prime = False
            break
        divisor += 1
    if is_prime and num > 1:
        print(num)
    num += 1

# Task - 39
num = int(input("Enter a number: "))
is_prime = True
divisor = 2
while divisor <= num // 2:
    if num % divisor == 0:
        is_prime = False
        break
    divisor += 1
if is_prime and num > 1:
    print(f"{num} is a prime number.")
else:
    print(f"{num} is not a prime number.")

# Task - 40
num = int(input("Enter a number: "))
original_num = num
reverse_num = 0
while num > 0:
    remainder = num % 10
    reverse_num = reverse_num * 10 + remainder
    num = num // 10
if original_num == reverse_num:
    print(f"{original_num} is a palindrome.")
else:
    print(f"{original_num} is not a palindrome.")


# Task - 41
num = int(input("Enter a number: "))
original_num = num
reverse_num = 0
while num > 0:
    remainder = num % 10
    reverse_num = reverse_num * 10 + remainder
    num = num // 10
if original_num == reverse_num:
    print(f"{original_num} is a palindrome.")
else:
    print(f"{original_num} is not a palindrome.")


# Task - 42
num = int(input("Enter a number: "))
original_num = num
order = len(str(num))
armstrong_sum = 0
while num > 0:
    digit = num % 10
    armstrong_sum += digit ** order
    num //= 10
if original_num == armstrong_sum:
    print(f"{original_num} is an Armstrong number.")
else:
    print(f"{original_num} is not an Armstrong number.")


# Task - 43
num = int(input("Enter a number: "))
sqrt_num = int(num ** 0.5)
if sqrt_num * sqrt_num == num:
    print(f"{num} is a perfect square.")
else:
    print(f"{num} is not a perfect square.")

num = int(input("Enter a number: "))
divisor = 1
sum_of_divisors = 0
while divisor <= num // 2:
    if num % divisor == 0:
        sum_of_divisors += divisor
    divisor += 1
if sum_of_divisors == num:
    print(f"{num} is a perfect number.")
else:
    print(f"{num} is not a perfect number.")
