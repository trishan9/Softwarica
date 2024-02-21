# print "softwarica" 10 times
from string import punctuation


def print_softwarica():
    for _ in range(10):
        print("Softwarica")


print_softwarica()

# Sum of a list


def sum_of_list(list, sum):
    for n in list:
        sum += n
        print(sum)


sum_of_list([1, 2, 3, 4, 5], 0)


# print each character using indexing
def print_char(name):
    for i in range(len(name)):
        print(name[i])


print_char("Trishan")

# write a program to display integer from of a list. given list=[1,"a","c",2,3,4]


def print_integer(list):
    int_data = [n for n in list if isinstance(n, int)]
    print(int_data)


print([1, "a", "c", 2, 3, 4])

# multiplication of a each element. given list=[4,5,3,2]


def list_product(nums, product):
    for n in nums:
        product *= n
    print(product)


list_product([4, 5, 3, 2], 1)


# multiplication table of a given number
def multiplication_table(given_number):
    for i in range(1, 11):
        print(f"{given_number} X {i} = {given_number * i}")


multiplication_table(3)


# Reverse a list
def reverse_list(original_list):
    reversed_list = []
    for value in original_list:
        reversed_list = [value] + reversed_list
    print(reversed_list)


reverse_list([1, 2, 3, 4, 5])

# given list is [1,2,3,4] but expected output in new list [2,3,4,5]


def format_list(given_list):
    for i, n in enumerate(given_list):
        if n == 1:
            given_list.pop(i)
    given_list.append(5)
    print(given_list)


format_list([1, 2, 3, 4])

# Given list is lst=[1,2,3,4] but print 1 and 4 only


def format_list(lst):
    for n in lst:
        if n == 1 or n == 4:
            print(n)


format_list([1, 2, 3, 4])

# Given list is lst=[1,2,3,4] but print 1 2 and 4 only


def format_list(lst):
    for n in lst:
        if n % 2 == 0 or n == 1:
            print(n)


format_list([1, 2, 3, 4])


# Given list is [1,2,3,4] but expected output is [1,"a",2,4]
def format_list(lst):
    lst.insert(1, "a")
    lst.pop(len(lst) - 2)
    print(lst)


format_list([1, 2, 3, 4])


#  Given list is [1,2,3,4,5] separate the elements into odd and even categories.
def format_list_even_odd(lst):
    odd = [n for n in lst if n % 2 != 0]
    even = [n for n in lst if n % 2 == 0]
    print(odd)
    print(even)


format_list_even_odd([1, 2, 3, 4, 5])


# Given list is [1,2,3,"d",4,5,"a"] separate the elements based on their data types
def format_list_data_type(lst):
    int_data = [data for data in lst if isinstance(data, int)]
    str_data = [data for data in lst if isinstance(data, str)]
    print(int_data)
    print(str_data)


format_list_data_type([1, 2, 3, "d", 4, 5, "a"])


# Given list is [1,2,3,4,"a","b"] append each elements datatypes to separate lists.
def get_data_types(data):
    data_types = [type(a) for a in data]
    print(data_types)


get_data_types([1, 2, 3, 4, "a", "b"])

# Python program that accepts a string and calculate the number of digits and letters and space


def get_string_data(string):
    digits_count = 0
    letters_count = 0
    space_count = 0
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


get_string_data("Hello I am Trishan 123")

# Python program to check the validity of username and password input by users


def validate_login(email, password):
    database = {
        "mailtotrishan@gmail.com": "password@",
        "example@gmail.com": "password@"
    }
    attempts_left = 3
    special_chars = list(punctuation)
    is_password_valid = False

    while attempts_left != 0:
        print(
            f"\nPlease login using your email address and password: Attempts Left: {attempts_left}")

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
def check_even_odd(num):
    if num % 2 == 0:
        print(f"{num} is even")
    else:
        print(f"{num} is odd")


check_even_odd(4)

#  factorial of a given number


def factorial(num):
    fact = 1
    for i in range(1, num + 1):
        fact *= i
        print(fact)


factorial(4)


# Print multiplication table of  1,2,3,4,5,6,7,8
def multiplication_table_upto_8():
    for i in range(1, 9):
        for j in range(1, 11):
            print(f"{i} X {j} = {i * j}")


# Given list is lst=[1,2,3,4] but print 1 and 2 only
def format_list(lst):
    for n in lst:
        if n == 1 or n == 2:
            print(n)


format_list([1, 2, 3, 4])

# Python program to calculate the sum of all the odd numbers within the given range.


def sum_of_odd_with_range(given_range):
    total = 0
    for i in range(given_range):
        if i % 2 != 0:
            total += i
    print(total)


sum_of_odd_with_range(80)

# Python program to calculate the sum of all the even numbers within the given range.


def sum_of_even_numbers(given_range):
    total = 0
    for i in range(given_range):
        if i % 2 == 0:
            total += i
    return total


given_range = 50
print(sum_of_even_numbers(given_range))


# Python program to count the space of a given string
def count_spaces(string):
    space_count = 0
    for char in string:
        if char.isspace():
            space_count += 1
    return space_count


string = "   Hello   Trishan"
print(f"Total Spaces: {count_spaces(string)}")

# given list is [1,2,3,4] but expected output is [1,8,27,64]


def cube_list(lst):
    return [i ** 3 for i in lst]


lst = [1, 2, 3, 4]
print(cube_list(lst))

# reverse of a string a="programming".


def reverse_string(a):
    return a[::-1]


a = "programming"
print(reverse_string(a))

# Place a break statement in the for loop so that it prints from 0 to 7 only (including 7). Given range(50)


def print_up_to_seven():
    for i in range(50):
        if i > 7:
            break
        print(i)


print_up_to_seven()

# Write a for loop that iterates through a string and prints every letter.


def print_letters(string):
    for char in string:
        print(char)


string = "Trishan"
print_letters(string)

# Write a for loop which print "Hello!, " plus each name in the list. i.e.: "Hello!, Ram". Hint a=["ram","shyam",1,2] expected output:  Hello!ram Hello!shyam


def greet_names(names):
    for name in names:
        if isinstance(name, str):
            print(f"Hello!{name}")


a = ["ram", "shyam", 1, 2]
greet_names(a)

# Using a for loop and .append() method append each item with a Dr. prefix to the lst. Hint a=["ram","shyam"] expected output:  ['Dr.ram', 'Dr.shyam','Dr.1','Dr.2']


def add_prefix_with_doctor(a):
    return [f"Dr. {name}" for name in a]


a = ["ram", "shyam"]
a_with_prefix = add_prefix_with_doctor(a)
print(a_with_prefix)

# Write a for loop which appends the square of each number to the new list.


def square_list(lst):
    return [n ** 2 for n in lst]


lst = [1, 2, 3, 4]
print(square_list(lst))

# Write a for loop using an if statement, that appends each number to the new list if it's positive. given lst1=[111, 32, -9, -45, -17, 9, 85, -10]


def positive_numbers(lst1):
    return [num for num in lst1 if num > 0]


lst1 = [111, 32, -9, -45, -17, 9, 85, -10]
print(positive_numbers(lst1))

# Write a Python program that prints all the numbers from 0 to 6 except 3 and 6. given list=[0,1,2,3,4,5,6]


def print_except_3_and_6(lst):
    for n in lst:
        if n == 3 or n == 6:
            continue
        print(n)


lst = [0, 1, 2, 3, 4, 5, 6]
print_except_3_and_6(lst)

# Write a for loop which appends the type of each element in the first list to the second list.


def get_data_types(data):
    return [type(a) for a in data]


data = [1, 2, 3, 4, "a", "b"]
data_types = get_data_types(data)
print(data_types)

# Use else block to display a message “Done” after successful execution of for loop.


def loop_with_else():
    for i in range(3):
        print("For loop")
    else:
        print("Done")


loop_with_else()

# Write a for loop statement to print the following series:

# 105 98 -------7


def print_series():
    for i in range(105, 1, -7):
        print(i)


print_series()

# removal bad characters from the given string. Given bad_chars = [';', ':', '!', "*"], string = "py;th* o:n ! ;py * t*h:o !n".  Expected output = pythonpython


def remove_bad_chars(string, bad_chars):
    list_string = list(string)
    for i, char in enumerate(list_string):
        if char in bad_chars:
            list_string.pop(i)
    return "".join(list_string)


bad_chars = [';', ':', '!', "*"]
string = "py;th* o:n ! ;py * t*h:o !n"
print(remove_bad_chars(string, bad_chars))

# Python program to count the number of even and odd numbers from a series of numbers.


def count_even_odd_numbers():
    odd_count = 0
    even_count = 0
    for i in range(1, 101):
        if i % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
    print(odd_count, even_count)


count_even_odd_numbers()

# Write a python program to display all the prime numbers within a given range.


def print_prime_numbers():
    for num in range(1, 101):
        if num == 0 or num == 1:
            pass
        elif num == 2:
            pass
        else:
            for i in range(2, num):
                if i % num != 0:
                    print(i)


print_prime_numbers()

# given number is prime or not


def check_prime_number(n):
    is_prime = True
    is_divisible_by = 0
    if n == 0 or n == 1:
        print("Not a Prime Number!")
    elif n == 2:
        print("Prime number!")
    else:
        for i in range(2, n):
            if n % i == 0:
                is_prime = False
                is_divisible_by = i
                break
        if is_prime:
            print("Prime number!")
        else:
            print(
                f"Not a Prime Number!, because {n} is divisible by {is_divisible_by}")


check_prime_number(13)

# program to check given number is palindrome or not


def check_palindrome(num):
    if num == num[::-1]:
        print("Palindrome!")
    else:
        print("Not Palindrome!")


check_palindrome("121")

# program to check given number is armstrong or not


def check_armstrong(num):
    sum_of_num = sum([int(n) ** len(num) for n in num])
    if str(sum_of_num) == num:
        print("Armstrong")
    else:
        print("Not Armstrong!")


check_armstrong("9474")

# Python program to check a number is perfect square


def check_perfect_square(number):
    if str(number ** (1/2)).endswith(".0"):
        print("Perfect square!")
    else:
        print("Not perfect square number!")


check_perfect_square(81)

# python program to check a number is perfect number


def is_perfect_number(n):
    divisors_sum = sum([x for x in range(1, n) if n % x == 0])
    return divisors_sum == n


number = 28
if is_perfect_number(number):
    print(number, "is a perfect number.")
else:
    print(number, "is not a perfect number.")
