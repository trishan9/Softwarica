# Question 1
marks = int(input("Enter your total marks: "))
if (marks < 25):
    print("Your final grade is F")
elif (marks >= 25 and marks < 45):
    print("Your final grade is E")
elif (marks >= 45 and marks < 50):
    print("Your final grade is D")
elif (marks >= 50 and marks < 60):
    print("Your final grade is C")
elif (marks >= 60 and marks < 80):
    print("Your final grade is B")
elif (marks >= 80):
    print("Your final grade is A")

# Question 2
n1 = int(input("Enter the first number: "))
n2 = int(input("Enter the second number: "))
if n1 == n2:
    print("Both numbers are equal")
else:
    print("Both numbers are not equal")

# Question 3
n = int(input("Enter the number to check even or odd: "))
if n % 2 == 0:
    print(f"{n} is even")
else:
    print(f"{n} is odd")

# Question 4
n = int(input("Enter the number to check positive or negative: "))
if n > 0:
    print(f"{n} is positive")
else:
    print(f"{n} is negative")

# Question 5
age = int(input("Enter your age: "))
if age > 18:
    print("You are eligible to vote")
else:
    print("You are not eligible to vote")

# Question 6
m = int(input("Enter the number: "))
if m > 0:
    print("The value of n is 1")
elif m < 0:
    print("The value of n is -1")
else:
    print("The value of n is 0")

# Question 7
n1 = int(input("Enter the first number: "))
n2 = int(input("Enter the second number: "))
n3 = int(input("Enter the third number: "))

if n1 > n2 and n1 > n3:
    print(f"{n1} is the greatest number!")
elif n2 > n1 and n2 > n3:
    print(f"{n2} is the greatest number!")
else:
    print(f"{n3} is the greatest number!")

# Question 8
char = input("enter the character: ")
if char.isalpha():
    print(f"{char} is alphabet")
elif char.isdigit():
    print(f"{char} is digit")

# Question 9
alphabet = (input("Enter the alphabet: ")).lower()
if alphabet == 'a' or alphabet == 'e' or alphabet == 'i' or alphabet == 'o' or alphabet == 'u':
    print(f"{alphabet} is Vowel")
else:
    print(f"{alphabet} is Consonant")


# Question 11
n = int(input("Enter the number to check: "))
if n % 3 == 0:
    print(f"{n} is divisible by 3")
else:
    print(f"{n} is not divisible by 3")


# Question 12
n = int(input("Enter the number to check: "))
if n % 5 == 0:
    print("Hello")
else:
    print("Bye")

# # Question 13
day = int(input("Enter the day in number(1-7): "))
match day:
    case 1:
        print("Sunday")
    case 2:
        print("Monday")
    case 3:
        print("Tuesday")
    case 4:
        print("Wednesday")
    case 5:
        print("Thursday")
    case 6:
        print("Friday")
    case 7:
        print("Saturday")
    case _:
        print("Invalid")

# Question 14
day = int(input("Enter the month in number(1-7): "))
match day:
    case 1:
        print("January")
    case 2:
        print("February")
    case 3:
        print("March")
    case 4:
        print("April")
    case 5:
        print("May")
    case 6:
        print("June")
    case 7:
        print("July")
    case _:
        print("Invalid")


# Question 15
city = input("Enter the city: ").lower()
if city == "delhi":
    print("Red Fort")
elif city == "agra":
    print("Taj Mahal")
elif city == "jaipur":
    print("Jal Mahal")
else:
    print("Monument not available")


# Question 16
n = int(input("Enter the number to check: "))
if n % 2 == 0 and n % 3 == 0:
    print(f"{n} is divisble by both 2 and 3")
else:
    print(f"{n} is not divisble by both 2 and 3")


# Question 17
n1 = int(input("Enter the first number: "))
n2 = int(input("Enter the second number: "))
n3 = int(input("Enter the third number: "))

if n1 < n2 and n1 < n3:
    print(f"{n1} is the smallest number!")
elif n2 < n1 and n2 < n3:
    print(f"{n2} is the smallest number!")
else:
    print(f"{n3} is the smallest number!")


# Question 18
n1 = int(input("Enter the first number: "))
n2 = int(input("Enter the second number: "))
oper = input("Enter the operator: ")
if oper == "+":
    print(f"{n1} {oper} {n2} = {n1 + n2}")
elif oper == "-":
    print(f"{n1} {oper} {n2} = {n1 - n2}")
elif oper == "*":
    print(f"{n1} {oper} {n2} = {n1 * n2}")
elif oper == "/":
    print(f"{n1} {oper} {n2} = {n1 / n2}")
elif oper == "**":
    print(f"{n1} {oper} {n2} = {n1 ** n2}")
elif oper == "//":
    print(f"{n1} {oper} {n2} = {n1 // n2}")
else:
    print("invalid Mathematical Operator")


# Question 19
x = 1
if x > 0:
    print("True")
elif x < 0:
    print("False")
else:
    print("zero")


# Question 20
name = input("Enter your name: ")
age = input("Enter your age: ")
address = input("Enter your address: ")
print(F"Your name is {name}\nYour age is {age}\nYour address is {address}")


# Question 21
# Question : x = 5 then what will be the output after we run x += 3
# Answer = 8


# Question 22
a = True
b = True
c = True
d = True
print(c)  # True
print(d)  # True
print(not a)  # False
print(not b)  # False
print(not c)  # False
print(not d)  # False
print(a and b)  # True
print(a or b)  # True
print(a and b or c)  # True
print(not a or b or c)  # True
print(not a or not b or not c)  # False
print(not (not a or not b or not c))  # True
