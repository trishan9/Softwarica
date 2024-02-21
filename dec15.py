# print "softwarica" 10 times
from string import punctuation

for i in range(10):
    print("Softwarica")

# Sum of a list
nums = [1, 2, 3, 4, 5]
total = 0
for n in nums:
    total += n
print(total)

# print each character using indexing
name = "Trishan"
for i in range(len(name)):
    print(name[i])

# write a program to display integer from of a list. given list=[1,"a","c",2,3,4]
data = [1, "a", "c", 2, 3, 4]
int_data = [n for n in data if isinstance(n, int)]
print(int_data)

# multiplication of a each element. given list=[4,5,3,2]
nums = [4, 5, 3, 2]
product = 1
for n in nums:
    product *= n
print(product)

# multiplication table of a given number
given_number = 2
for i in range(1, 11):
    print(f"{given_number} X {i} = {given_number * i}")

# Reverse a list
original_list = [1, 2, 3, 4, 5]
reversed_list = []
for value in original_list:
    reversed_list = [value] + reversed_list
print(reversed_list)

# given list is [1,2,3,4] but expected output in new list [2,3,4,5]
given_list = [1, 2, 3, 4]
for i, n in enumerate(given_list):
    if n == 1:
        given_list.pop(i)
given_list.append(5)
print(given_list)

# Given list is lst=[1,2,3,4] but print 1 and 4 only
lst = [1, 2, 3, 4]
for n in lst:
    if n == 1 or n == 4:
        print(n)

# Given list is lst=[1,2,3,4] but print 1 2 and 4 only
lst = [1, 2, 3, 4]
for n in lst:
    if n % 2 == 0 or n == 1:
        print(n)

# Given list is [1,2,3,4] but expected output is [1,"a",2,4]
lst = [1, 2, 3, 4]
lst.insert(1, "a")
lst.pop(len(lst) - 2)
print(lst)


#  Given list is [1,2,3,4,5] separate the elements into odd and even categories.
lst = [1, 2, 3, 4, 5]
odd = [n for n in lst if n % 2 != 0]
even = [n for n in lst if n % 2 == 0]
print(odd)
print(even)


# Given list is [1,2,3,"d",4,5,"a"] separate the elements based on their data types
lst = [1, 2, 3, "d", 4, 5, "a"]
int_data = [data for data in lst if isinstance(data, int)]
str_data = [data for data in lst if isinstance(data, str)]
print(int_data)
print(str_data)

# Given list is [1,2,3,4,"a","b"] append each elements datatypes to separate lists.
data = [1, 2, 3, 4, "a", "b"]
data_types = [type(a) for a in data]
print(data_types)

# Python program that accepts a string and calculate the number of digits and letters and space
digits_count = 0
letters_count = 0
space_count = 0
string = "Hello I am Trishan 123"
for char in string:
    if char.isspace():
        space_count += 1
    elif char.isalpha():
        letters_count += 1
    elif char.isdigit():
        digits_count += 1
print(f"Letters: {letters_count}")
print(f"Digits: {digits_count}")
print(f"Space: {space_count}")

# Python program to check the validity of username and password input by users

database = {
    "mailtotrishan@gmail.com": "trishan1122@",
    "example@gmail.com": "password@"
}

attempts_left = 3
special_chars = list(punctuation)
is_password_valid = False

while attempts_left != 0:
    print(
        f"\nPlease login using your email address and password: Attempts Left: {attempts_left}")
    email = input("Enter your email address: ")
    password = input("Enter your password: ")

    for char in password:
        if (char in special_chars):
            is_password_valid = True
            break

    try:
        user = database[email]
        if user:
            user_exists = True
    except KeyError:
        user_exists = False

    if not email or not password:
        print("All fields are required")
        attempts_left -= 1
    elif not email.endswith("@gmail.com"):
        print("Please enter valid email address")
        attempts_left -= 1
    elif not user_exists:
        print("User with this email address doesn't exists!")
        attempts_left -= 1
    elif len(password) < 8 or not (is_password_valid):
        print("Password must be valid")
        attempts_left -= 1
    elif password != database[email]:
        print("Password is incorrect!")
        attempts_left -= 1
    else:
        break
else:
    print("You are blocked because your all all attempts are failed!")

if attempts_left != 0:
    print('Logged in Succesfully!')


# program to print the given number is odd or even
num = 4
if num % 2 == 0:
    print(f"{num} is even")
else:
    print(f"{num} is odd")

#  factorial of a given number
fact = 1
num = 4
for i in range(1, num + 1):
    fact *= i
print(fact)


# Print multiplication table of  1,2,3,4,5,6,7,8
for i in range(1, 9):
    for j in range(1, 11):
        print(f"{i} X {j} = {i * j}")

# Given list is lst=[1,2,3,4] but print 1 and 2 only
lst = [1, 2, 3, 4]
for n in lst:
    if n == 1 or n == 2:
        print(n)


# Python program to calculate the sum of all the odd numbers within the given range.
given_range = 50
total = 0
for i in range(given_range):
    if i % 2 != 0:
        total += i
print(total)

# Python program to calculate the sum of all the even numbers within the given range.
given_range = 50
total = 0
for i in range(given_range):
    if i % 2 == 0:
        total += i
print(total)


# Python program to count the space of a given string
string = "   Hello   Trishan"
space_count = 0
for char in string:
    if char.isspace():
        space_count += 1
print(f"Total Spaces: {space_count}")

# given list is [1,2,3,4] but expected output is [1,8,27,64]
lst = [1, 2, 3, 4]
output = [i ** 3 for i in lst]
print(output)

# reverse of a string a="programming".
a = "programming"
print(a[::-1])

# Place a break statement in the for loop so that it prints from 0 to 7 only (including 7). Given range(50)
for i in range(50):
    if i > 7:
        break
    print(i)

# Write a for loop that iterates through a string and prints every letter.
string = "Trishan"
for char in string:
    print(char)

# Write a for loop which print "Hello!, " plus each name in the list. i.e.: "Hello!, Ram". Hint a=["ram","shyam",1,2] expected output:  Hello!ram Hello!shyam
a = ["ram", "shyam", 1, 2]
for name in a:
    if isinstance(name, str):
        print(f"Hello!{name}")

# Using a for loop and .append() method append each item with a Dr. prefix to the lst. Hint a=["ram","shyam"] expected output:  ['Dr.ram', 'Dr.shyam','Dr.1','Dr.2']
a = ["ram", "shyam"]
a_with_prefix = [f"Dr. {name}" for name in a]
print(a_with_prefix)

# Write a for loop which appends the square of each number to the new list.
lst = [1, 2, 3, 4]
squared_list = [n ** 2 for n in lst]
print(squared_list)


# Write a for loop using an if statement, that appends each number to the new list if it's positive. given lst1=[111, 32, -9, -45, -17, 9, 85, -10]
lst1 = [111, 32, -9, -45, -17, 9, 85, -10]
pos_list = [num for num in lst1 if num > 0]
print(pos_list)

# Write a Python program that prints all the numbers from 0 to 6 except 3 and 6. given list=[0,1,2,3,4,5,6]
lst = [0, 1, 2, 3, 4, 5, 6]
for n in lst:
    if n == 3 or n == 6:
        continue
    print(n)

# Write a for loop which appends the type of each element in the first list to the second list.
data = [1, 2, 3, 4, "a", "b"]
data_types = [type(a) for a in data]
print(data_types)

# Use else block to display a message “Done” after successful execution of for loop.
for i in range(3):
    print("For loop")
else:
    print("Done")

# Write a for loop statement to print the following series:

# 105 98 -------7
for i in range(105, 1, -7):
    print(i)

# removal bad characters from the given string. Given bad_chars = [';', ':', '!', "*"], string = "py;th* o:n ! ;py * t*h:o !n".  Expected output = pythonpython
bad_chars = [';', ':', '!', "*"]
string = "py;th* o:n ! ;py * t*h:o !n"
list_string = list(string)
for i, char in enumerate(list_string):
    if char in bad_chars:
        list_string.pop(i)
string = "".join(list_string)
print(string)

# Python program to count the number of even and odd numbers from a series of numbers.
odd_count = 0
even_count = 0
for i in range(1, 101):
    if i % 2 == 0:
        even_count += 1
    else:
        odd_count += 1
print(odd_count, even_count)

# Write a python program to display all the prime numbers within a given range.
for num in range(1, 101):
    if num == 0 or num == 1:
        pass
    elif num == 2:
        pass
    else:
        for i in range(2, num):
            if i % num != 0:
                print(i)

# given number is prime or not
n = int(input("Enter the number to check prime number: "))
is_prime = True
is_divisble_by = 0
if n == 0 or n == 1:
    print("Not a Prime Number!")
elif n == 2:
    print("Prime number!")
else:
    for i in range(2, n):
        if n % i == 0:
            is_prime = False
            is_divisble_by = i
            break
if is_prime:
    print("Prime number!")
else:
    print(f"Not a Prime Number!, because {n} is divisible by {is_divisble_by}")


# program to check given number is palindrome or not
if (num := input("Enter the number to check palindrome: ")) == num[::-1]:
    print("Palindrome!")
else:
    print("Not Palindrome!")

# program to check given number is armstrong or not
sum_of_num = 0
for n in (num := input("Enter the number to check Armstrong: ")):
    sum_of_num += int(n) ** len(num)
if str(sum_of_num) == num:
    print("Armstrong")
else:
    print("Not Armstrong!")

# Python program to check a number is perfect square
number = 2500
if str(number ** (1/2)).endswith(".0"):
    print("Perfect square!")
else:
    print("Not perfect square number!")


# python program to check a number is perfect number


def is_perfect_number(n):
    divisors_sum = sum([x for x in range(1, n) if n % x == 0])
    return divisors_sum == n


number = 28
if is_perfect_number(number):
    print(number, "is a perfect number.")
else:
    print(number, "is not a perfect number.")
