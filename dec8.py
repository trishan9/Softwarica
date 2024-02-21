# # if i < j:
# #     if j < k:
# #         i = j
# #     else:
# #         j = k
# # else:
# #     if j > k:
# #         j = i
# #     else:
# #         i = k


# # 1. Print "1" if a is equal to b, print "2" if a is greater than b, otherwise print "3".
# a = input("Enter the value of a: ")
# b = input("Enter the value of b: ")
# if a == b:
#     print("1")
# elif a > b:
#     print("2")
# else:
#     print("3")

# # 2. Print "Hello" if a is equal to b, or if c is equal to d.
# a = input("Enter the value of a: ")
# b = input("Enter the value of b: ")
# c = input("Enter the value of c: ")
# d = input("Enter the value of d: ")
# if a == b or c == d:
#     print("Hello")

# # 3. Print "Hello" if a is equal to b, and c is equal to d
# a = input("Enter the value of a: ")
# b = input("Enter the value of b: ")
# c = input("Enter the value of c: ")
# d = input("Enter the value of d: ")
# if a == b and c == d:
#     print("Hello")

# # 4. For given integer x, print ‘True’ if it is positive, print ‘False’ if it is negative and print ‘zero’ if it is 0.
# x = 10
# if x > 0:
#     print("True")
# elif x < 0:
#     print("False")
# else:
#     print("zero")

# # 5. Check whether the user input number is even or odd and display it to user.
# n = int(input("Enter the value of n: "))
# if n % 2 == 0:
#     print(f"{n} is even")
# else:
#     print(f"{n} is odd")

# # 6. WAP which accepts marks of four subjects and display total marks, percentage and
# # grade.
# # Hint: more than 70% –> distinction, more than 60% –> first, more than 40% –> pass,
# # less than 40% –> fail
# subject_1_marks = int(input("Enter the marks of subject 1: "))
# subject_2_marks = int(input("Enter the marks of subject 2: "))
# subject_3_marks = int(input("Enter the marks of subject 3: "))
# subject_4_marks = int(input("Enter the marks of subject 4: "))

# total_marks = subject_1_marks + subject_2_marks + \
#     subject_3_marks + subject_4_marks
# percentage = (total_marks / 400) * 100
# if percentage > 70:
#     grade = "Distinction"
# elif percentage > 60 and percentage <= 70:
#     grade = "First"
# elif percentage > 40 and percentage <= 60:
#     grade = "Pass"
# else:
#     grade = "Fail"

# print(f"Total marks: {total_marks}\nPercentage: {percentage}\nGrade: {grade}")


# 7. What is the output of ‘APPLE’ > ‘apple’?
# print('APPLE' > 'apple')
# False

# 8. Write a program to accept the cost price of a bike qnd display the road tax to be paid according to the following criteria:
# Cost price(in Rs)                  Tax
# >100000                              15%
# >50000 and <=100000      10%
# <=50000                               5%
# price = int(input("Enter the cost price of bike: "))
# if price > 100000:
#     tax = price * 0.15
# elif price > 50000 and price <= 100000:
#     tax = price * 0.10
# else:
#     tax = price * 0.05
# print(f"You have to pay Rs.{tax} as road tax")


# 9. Accept the age of 4 people and display the youngest one.
# age1 = int(input("Enter the age of person 1"))
# age2 = int(input("Enter the age of person 2"))
# age3 = int(input("Enter the age of person 3"))
# age4 = int(input("Enter the age of person 4"))
# if age1 < age2 and age1 < age3 and age1 < age4:
#     print(f"The youngest person is the one with age {age1}")
# elif age2 < age1 and age2 < age3 and age2 < age4:
#     print(f"The youngest person is the one with age {age2}")
# elif age3 < age1 and age3 < age2 and age3 < age4:
#     print(f"The youngest person is the one with age {age3}")
# else:
#     print(f"The youngest person is the one with age {age4}")


# 10. Accept the age of 4 people and display the oldest one.
# age1 = int(input("Enter the age of person 1"))
# age2 = int(input("Enter the age of person 2"))
# age3 = int(input("Enter the age of person 3"))
# age4 = int(input("Enter the age of person 4"))
# if age1 > age2 and age1 > age3 and age1 > age4:
#     print(f"The oldest person is the one with age {age1}")
# elif age2 > age1 and age2 > age3 and age2 > age4:
#     print(f"The oldest person is the one with age {age2}")
# elif age3 > age1 and age3 > age2 and age3 > age4:
#     print(f"The oldest person is the one with age {age3}")
# else:
#     print(f"The oldest person is the one with age {age4}")


# 11. Accept the percentage from the user and display the grade according to the following criteria:
# Below 25 --D
# 25 to 45  -- C
# 45 to 50 -- B
# 50 to 60 --B+
# 60 to 80 -- A
# Above 80 -- A+
# percentage = int(input("Enter your percentage: "))
# if (percentage < 25):
#     print("Your final grade is D")
# elif (percentage >= 25 and percentage < 45):
#     print("Your final grade is C")
# elif (percentage >= 45 and percentage < 50):
#     print("Your final grade is B")
# elif (percentage >= 50 and percentage < 60):
#     print("Your final grade is B+")
# elif (percentage >= 60 and percentage < 80):
#     print("Your final grade is A")
# elif (percentage >= 80):
#     print("Your final grade is A+")


# 12. A company decided to give bonus to employee according to following criteria:
# Time period of service     Bonus
# More than 10 years            10%
# >=6 and <=10                       8%
# Less than 6 years                 5%
# time_period = int(input("Enter the employee's time period: "))
# if time_period > 10:
#     bonus_per = 10
# elif time_period >= 6 and time_period <= 10:
#     bonus_per = 8
# else:
#     bonus_per = 5
# print(f"Employee gets a bonus of {bonus_per}%")


# 13. Accept three numbers from the user and display the second largest number.
# n1 = int(input("Enter the first number: "))
# n2 = int(input("Enter the second number: "))
# n3 = int(input("Enter the third number: "))
# if n1 > n2 or n1 > n3:
#     print(f"{n1} is the second largest number")
# elif n2 > n1 or n2 > n3:
#     print(f"{n2} is the second largest number")
# elif n3 > n1 or n3 > n2:
#     print(f"{n3} is the second largest number")
# else:
#     print("All the numbers are equal")


# 14. Accept the number of days from the user and calculate the charge for library according to following:
# Till five days: Rs 2/day
# Six to ten days: Rs 3/day
# 11 to 15 days: Rs 4/day
# After 15 days: Rs 5/day
# days = int(input("Enter the number of days: "))
# if days <= 5:
#     charge = days * 2
# elif days > 5 and days <= 10:
#     charge = days * 3
# elif days > 10 and days <= 15:
#     charge = days * 4
# else:
#     charge = days * 5
# print(f"Your total library charge is Rs.{charge}")

# 15. A company decided to give bonus of 5% to employee if his/her year of service is more than 5years.
# Ask user for their salary and year of service and print the net bonus amount.
# time_period = int(input("Enter the employee's time period: "))
# salary = int(input("Enter the employee's salary: "))
# bonus_per = 5
# if time_period > 5:
#     net_bonus = bonus_per / 100 * salary
#     print(f"Employee gets a net bonus of Rs. {net_bonus}")
# else:
#     print("Employee is not eligible for bonus")


# 16. Write a program to check two strings are anagram or not.
# str1 = input("Enter the first word: ")
# str2 = input("Enter the second word: ")

# if len(str1) != len(str2):
#     print("Not Anagram!")
# else:
#     if sorted(str1.lower()) == sorted(str2.lower()):
#         print("Anagram!")
#     else:
#         print("Not Anagram!")

# 17. Write a Python program to display your details like name, age, address in three different lines.
# name = input("Enter your name: ")
# age = input("Enter your age: ")
# address = input("Enter your address: ")
# print(F"Your name is {name}\nYour age is {age}\nYour address is {address}")


# 18. Write a python program which accepts the radius of circle from user and compute the area.
# radius = int(input("Enter the radius of circle: "))

# area = 3.14 * (radius ** 2)
# print(f"Area of circle with radius {radius} is {area}")


# 19. A school decided to replace the desks in three classrooms. Each desk sits two students.
# Given the number of students in each class, print the smallest possible number of desks that can be purchased.
# The program should read three integers: the number of students in each of the three
# classes, a, b and c respectively.
# Hint. In the first test there are three groups. The first group has 20 students and thus needs 10 desks.
# The second group has 21 students, so they can get by with no fewer than 11 desks.
# 11 desks are also enough for the third group of 22 students. So, we need 32 desks in total.
# sits_per_desk = 2
# students_in_class_a = int(input("Enter the number of students in class A: "))
# students_in_class_b = int(input("Enter the number of students in class B: "))
# students_in_class_c = int(input("Enter the number of students in class C: "))

# if students_in_class_a % sits_per_desk != 0:
#     desk_a = students_in_class_a // sits_per_desk + 1
# else:
#     desk_a = students_in_class_a // sits_per_desk

# if students_in_class_b % sits_per_desk != 0:
#     desk_b = students_in_class_b // sits_per_desk + 1
# else:
#     desk_b = students_in_class_b // sits_per_desk

# if students_in_class_c % sits_per_desk != 0:
#     desk_c = students_in_class_c // sits_per_desk + 1
# else:
#     desk_c = students_in_class_c // sits_per_desk


# print(
#     f"The smallest possible number of desks that can be purchased is {desk_a + desk_b + desk_c}")


# 20. N students take K apples and distribute them among each other evenly. The remaining (the undivisible) part remains in the basket. How many apples will each single student get? How many apples will remain in the basket? The program reads the numbers N and K. It should print the two answers for the questions above.
n = int(input("Enter the number of students: "))
k = int(input("Enter the number of apples: "))
remaining = k % n
if k > n:
    if remaining == 0:
        apple_per_person = k // n
        basket = 0
    elif remaining < k:
        apple_per_person = k // n
        basket = remaining
else:
    apple_per_person = 0
    basket = k

print(f"{n} students get {apple_per_person} apples each and apples in the basket is {basket}")

# 24. Write a program to check whether a number is divisible by 7 or not.
# n = int(input("Enter the number to check: "))
# if n % 7 == 0:
#     print(f"{n} is divisble by 7")
# else:
#     print(f"{n} is not divisble by 7")

# 28. Write a program to check whether a number entered is three digit number or not.
# n = input("Enter the number to check: ")
# if (len(n) == 3):
#     print(f"{n} is three digit number")
# else:
#     print(f"{n} is not three digit number")


# 29. Accept the following from the user and calculate the percentage of class attended:
# a. Total number of working days
# b. Total number of days for absent
# After calculating percentage show that, if the percentage is less than 75, than student will not be able to sit in exam.
# working_days = int(input("Enter the total number of working days: "))
# absent_days = int(input("Enter the total number of absent days: "))
# percentage = (absent_days // working_days) * 100
# if percentage < 75:
#     print("Student can't sit in exam")
# else:
#     print("Student can sit in exam")


# 30. Write a program to accept percentage and display the category according to the following criteria:
# Percentage                                   Category
# <40                       Failed
# >=40 and <55                             Fair
# >=55 and <65                   Good
# >=65                       Excellent
# percentage = int(input("Enter the percentage: "))
# if percentage < 40:
#     print("Failed")
# elif percentage >= 40 and percentage < 55:
#     print("Fair")
# elif percentage >= 55 and percentage < 65:
#     print("Good")
# else:
#     print("Excellent")


# 31. Accept the age, sex('M', 'F'), number of days and display the wages accordingly.
# Age        Sex    Wage/day
# >=18 and <30    M    700
#         F    750
# >=30 and <=40    M    800
#         F    850
# age = int(input("Enter the age: "))
# sex = input("Enter the sex('M' or 'F'): ").lower()
# number_of_days = int(input("Enter the number of days: "))

# if age >= 18 and age < 30:
#     if sex == "m":
#         wage_per_day = 700
#     else:
#         wage_per_day = 750
# elif age >= 30 and age <= 40:
#     if sex == "m":
#         wage_per_day = 800
#     else:
#         wage_per_day = 850
# print(f"Total wage_per_days you earned is {number_of_days * wage_per_day}")
